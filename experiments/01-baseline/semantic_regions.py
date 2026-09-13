from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable

import torch


SMPL_JOINT_NAMES = (
    "pelvis",
    "left_hip",
    "right_hip",
    "spine1",
    "left_knee",
    "right_knee",
    "spine2",
    "left_ankle",
    "right_ankle",
    "spine3",
    "left_foot",
    "right_foot",
    "neck",
    "left_collar",
    "right_collar",
    "head",
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_wrist",
    "right_wrist",
    "left_hand",
    "right_hand",
)

REGION_NAMES = (
    "torso",
    "head",
    "left_arm",
    "right_arm",
    "left_hand",
    "right_hand",
    "left_leg",
    "right_leg",
)

REGION_TO_ID: Dict[str, int] = {name: idx for idx, name in enumerate(REGION_NAMES)}
ID_TO_REGION: Dict[int, str] = {idx: name for name, idx in REGION_TO_ID.items()}

JOINT_TO_REGION = {
    "pelvis": "torso",
    "spine1": "torso",
    "spine2": "torso",
    "spine3": "torso",
    "neck": "torso",
    "left_collar": "torso",
    "right_collar": "torso",
    "head": "head",
    "left_shoulder": "left_arm",
    "left_elbow": "left_arm",
    "left_wrist": "left_hand",
    "left_hand": "left_hand",
    "right_shoulder": "right_arm",
    "right_elbow": "right_arm",
    "right_wrist": "right_hand",
    "right_hand": "right_hand",
    "left_hip": "left_leg",
    "left_knee": "left_leg",
    "left_ankle": "left_leg",
    "left_foot": "left_leg",
    "right_hip": "right_leg",
    "right_knee": "right_leg",
    "right_ankle": "right_leg",
    "right_foot": "right_leg",
}


@dataclass
class SemanticAssignment:
    nearest_vertex: torch.Tensor
    dominant_joint: torch.Tensor
    region_id: torch.Tensor
    joint_confidence: torch.Tensor

    def region_mask(self, names: Iterable[str]) -> torch.Tensor:
        ids = [REGION_TO_ID[name] for name in names]
        mask = torch.zeros_like(self.region_id, dtype=torch.bool)
        for region_id in ids:
            mask |= self.region_id == region_id
        return mask


def nearest_vertex_indices(
    points: torch.Tensor,
    vertices: torch.Tensor,
    chunk_size: int = 8192,
) -> torch.Tensor:
    """Return the nearest SMPL vertex for every Gaussian without materializing a huge distance matrix."""
    if points.ndim != 2 or points.shape[-1] != 3:
        raise ValueError(f"points must have shape [N, 3], got {tuple(points.shape)}")
    if vertices.ndim != 2 or vertices.shape[-1] != 3:
        raise ValueError(f"vertices must have shape [V, 3], got {tuple(vertices.shape)}")

    nearest = []
    for start in range(0, points.shape[0], chunk_size):
        end = min(start + chunk_size, points.shape[0])
        distances = torch.cdist(points[start:end], vertices)
        nearest.append(distances.argmin(dim=1))
    return torch.cat(nearest, dim=0)


def assign_gaussian_regions(
    gaussian_xyz_canon: torch.Tensor,
    smpl_vertices_canon: torch.Tensor,
    smpl_lbs_weights: torch.Tensor,
    chunk_size: int = 8192,
) -> SemanticAssignment:
    """Assign each canonical Gaussian to a coarse semantic body region.

    The assignment is deliberately non-learning. Each Gaussian is linked to its nearest
    canonical SMPL vertex, then inherits the dominant SMPL skinning joint of that vertex.
    This gives us an interpretable diagnostic layer before proposing a new model.
    """
    if smpl_lbs_weights.ndim != 2 or smpl_lbs_weights.shape[1] != len(SMPL_JOINT_NAMES):
        raise ValueError(
            "smpl_lbs_weights must have shape [V, 24] for the standard SMPL joint set"
        )
    if smpl_vertices_canon.shape[0] != smpl_lbs_weights.shape[0]:
        raise ValueError("SMPL vertex and LBS-weight counts do not match")

    nearest_vertex = nearest_vertex_indices(
        gaussian_xyz_canon,
        smpl_vertices_canon,
        chunk_size=chunk_size,
    )
    nearest_weights = smpl_lbs_weights[nearest_vertex]
    joint_confidence, dominant_joint = nearest_weights.max(dim=1)

    joint_to_region_id = torch.tensor(
        [REGION_TO_ID[JOINT_TO_REGION[name]] for name in SMPL_JOINT_NAMES],
        dtype=torch.long,
        device=gaussian_xyz_canon.device,
    )
    region_id = joint_to_region_id[dominant_joint]

    return SemanticAssignment(
        nearest_vertex=nearest_vertex,
        dominant_joint=dominant_joint,
        region_id=region_id,
        joint_confidence=joint_confidence,
    )


def summarize_assignment(assignment: SemanticAssignment) -> dict:
    summary = {
        "num_gaussians": int(assignment.region_id.numel()),
        "mean_joint_confidence": float(assignment.joint_confidence.mean().item()),
        "regions": {},
    }
    for region_id, region_name in ID_TO_REGION.items():
        mask = assignment.region_id == region_id
        count = int(mask.sum().item())
        confidence = (
            float(assignment.joint_confidence[mask].mean().item()) if count > 0 else None
        )
        summary["regions"][region_name] = {
            "count": count,
            "fraction": count / max(1, summary["num_gaussians"]),
            "mean_joint_confidence": confidence,
        }
    return summary
