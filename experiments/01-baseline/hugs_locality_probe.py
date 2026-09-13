from __future__ import annotations

import argparse
import glob
import json
import math
import sys
from pathlib import Path

import numpy as np
import torch
from omegaconf import OmegaConf

from locality_metrics import locality_report
from semantic_regions import (
    REGION_TO_ID,
    SMPL_JOINT_NAMES,
    assign_gaussian_regions,
    summarize_assignment,
)


DEFAULT_TARGET_REGIONS = {
    "head": ("head",),
    "left_wrist": ("left_hand",),
    "left_hand": ("left_hand",),
    "right_wrist": ("right_hand",),
    "right_hand": ("right_hand",),
    "left_elbow": ("left_arm", "left_hand"),
    "right_elbow": ("right_arm", "right_hand"),
    "left_shoulder": ("left_arm", "left_hand"),
    "right_shoulder": ("right_arm", "right_hand"),
    "left_knee": ("left_leg",),
    "right_knee": ("right_leg",),
    "left_ankle": ("left_leg",),
    "right_ankle": ("right_leg",),
}


def load_hugs_trainer(hugs_root: Path, output_dir: Path):
    hugs_root = hugs_root.resolve()
    output_dir = output_dir.resolve()
    sys.path.insert(0, str(hugs_root))

    from hugs.cfg.config import cfg as default_cfg
    from hugs.trainer import GaussianTrainer
    from hugs.utils.general import safe_state

    config_path = output_dir / "config_train.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"Missing HUGS training config: {config_path}")

    saved_cfg = OmegaConf.load(config_path)
    cfg = OmegaConf.merge(default_cfg, saved_cfg)
    cfg.eval = True
    cfg.logdir = str(output_dir)
    cfg.logdir_ckpt = str(output_dir)

    human_ckpts = sorted(
        glob.glob(str(output_dir / "*human*.pth"))
        + glob.glob(str(output_dir / "ckpt" / "*human*.pth"))
    )
    if not human_ckpts:
        raise FileNotFoundError(f"No HUGS human checkpoint found under {output_dir}")

    cfg.human.ckpt = human_ckpts[-1]
    if cfg.mode not in ("human", "human_scene"):
        raise ValueError(f"This probe requires a human model, but config mode is {cfg.mode!r}")

    safe_state(seed=cfg.seed)
    trainer = GaussianTrainer(cfg)
    return trainer, cfg, Path(cfg.human.ckpt)


def perturb_body_pose(
    body_pose: torch.Tensor,
    joint_name: str,
    axis: str,
    degrees: float,
) -> torch.Tensor:
    if joint_name not in SMPL_JOINT_NAMES:
        raise ValueError(f"Unknown SMPL joint {joint_name!r}")

    joint_id = SMPL_JOINT_NAMES.index(joint_name)
    if joint_id == 0:
        raise ValueError("Pelvis/root orientation is not part of SMPL body_pose; use a non-root joint")

    axis_to_index = {"x": 0, "y": 1, "z": 2}
    if axis not in axis_to_index:
        raise ValueError("axis must be one of: x, y, z")

    pose = body_pose.detach().clone().reshape(23, 3)
    pose[joint_id - 1, axis_to_index[axis]] += math.radians(degrees)
    return pose.reshape(-1)


@torch.no_grad()
def run_probe(
    trainer,
    frame_index: int,
    joint_name: str,
    axis: str,
    degrees: float,
    active_threshold: float,
) -> tuple[dict, dict, dict]:
    model = trainer.human_gs
    data = trainer.val_dataset[frame_index]

    canon = model.canon_forward()

    forward_kwargs = {
        "global_orient": data["global_orient"],
        "body_pose": data["body_pose"],
        "betas": data["betas"],
        "transl": data["transl"],
        "smpl_scale": data.get("smpl_scale"),
    }
    before = model.forward_test(canon, **forward_kwargs)

    changed_pose = perturb_body_pose(
        data["body_pose"],
        joint_name=joint_name,
        axis=axis,
        degrees=degrees,
    )
    forward_kwargs["body_pose"] = changed_pose
    after = model.forward_test(canon, **forward_kwargs)

    assignment = assign_gaussian_regions(
        gaussian_xyz_canon=before["xyz_canon"],
        smpl_vertices_canon=model.vitruvian_verts,
        smpl_lbs_weights=model.smpl.lbs_weights,
    )

    target_region_names = DEFAULT_TARGET_REGIONS.get(joint_name)
    if target_region_names is None:
        raise ValueError(
            f"No default target-region definition for {joint_name!r}. "
            f"Choose one of: {', '.join(sorted(DEFAULT_TARGET_REGIONS))}"
        )
    target_region_ids = [REGION_TO_ID[name] for name in target_region_names]

    metrics = locality_report(
        before_xyz=before["xyz"],
        after_xyz=after["xyz"],
        region_id=assignment.region_id,
        target_region_ids=target_region_ids,
        active_threshold=active_threshold,
    )
    metrics.update(
        {
            "frame_index": int(frame_index),
            "joint": joint_name,
            "axis": axis,
            "degrees": float(degrees),
            "target_regions": list(target_region_names),
        }
    )

    semantic_summary = summarize_assignment(assignment)
    arrays = {
        "xyz_before": before["xyz"].detach().cpu().numpy(),
        "xyz_after": after["xyz"].detach().cpu().numpy(),
        "xyz_canon": before["xyz_canon"].detach().cpu().numpy(),
        "region_id": assignment.region_id.detach().cpu().numpy(),
        "dominant_joint": assignment.dominant_joint.detach().cpu().numpy(),
        "joint_confidence": assignment.joint_confidence.detach().cpu().numpy(),
        "nearest_vertex": assignment.nearest_vertex.detach().cpu().numpy(),
    }
    return metrics, semantic_summary, arrays


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Probe geometric locality in a pretrained HUGS human representation."
    )
    parser.add_argument("--hugs-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path, help="HUGS experiment/checkpoint directory")
    parser.add_argument("--frame", type=int, default=0)
    parser.add_argument("--joint", default="left_wrist", choices=sorted(DEFAULT_TARGET_REGIONS))
    parser.add_argument("--axis", default="z", choices=("x", "y", "z"))
    parser.add_argument("--degrees", type=float, default=10.0)
    parser.add_argument("--active-threshold", type=float, default=1e-5)
    parser.add_argument("--save-dir", type=Path, default=Path("probe_results"))
    args = parser.parse_args()

    trainer, cfg, checkpoint = load_hugs_trainer(args.hugs_root, args.output_dir)
    if args.frame < 0 or args.frame >= len(trainer.val_dataset):
        raise IndexError(f"frame must be in [0, {len(trainer.val_dataset) - 1}]")

    metrics, semantic_summary, arrays = run_probe(
        trainer=trainer,
        frame_index=args.frame,
        joint_name=args.joint,
        axis=args.axis,
        degrees=args.degrees,
        active_threshold=args.active_threshold,
    )

    save_dir = args.save_dir.resolve()
    save_dir.mkdir(parents=True, exist_ok=True)

    run_name = f"frame{args.frame:03d}_{args.joint}_{args.axis}_{args.degrees:g}deg"
    metadata = {
        "baseline": "HUGS",
        "checkpoint": str(checkpoint),
        "dataset": str(cfg.dataset.name),
        "sequence": str(cfg.dataset.seq),
        **metrics,
    }

    with (save_dir / f"{run_name}.json").open("w") as f:
        json.dump(metadata, f, indent=2)
    with (save_dir / "semantic_assignment.json").open("w") as f:
        json.dump(semantic_summary, f, indent=2)
    np.savez_compressed(save_dir / f"{run_name}.npz", **arrays)

    print(json.dumps(metadata, indent=2))
    print(f"Saved probe outputs to: {save_dir}")


if __name__ == "__main__":
    main()
