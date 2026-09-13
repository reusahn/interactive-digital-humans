from __future__ import annotations

from typing import Iterable

import torch


def displacement_magnitude(before_xyz: torch.Tensor, after_xyz: torch.Tensor) -> torch.Tensor:
    if before_xyz.shape != after_xyz.shape:
        raise ValueError(
            f"before/after shapes must match, got {tuple(before_xyz.shape)} and {tuple(after_xyz.shape)}"
        )
    if before_xyz.ndim != 2 or before_xyz.shape[-1] != 3:
        raise ValueError("before/after positions must have shape [N, 3]")
    return torch.linalg.vector_norm(after_xyz - before_xyz, dim=-1)


def locality_report(
    before_xyz: torch.Tensor,
    after_xyz: torch.Tensor,
    region_id: torch.Tensor,
    target_region_ids: Iterable[int],
    active_threshold: float = 1e-5,
    eps: float = 1e-12,
) -> dict:
    """Measure how much a targeted interaction-like pose change affects non-target Gaussians.

    This is a diagnostic metric, not a claim of perceptual quality. A low leakage ratio is
    only desirable when the requested target motion is also successfully realized.
    """
    magnitude = displacement_magnitude(before_xyz, after_xyz)

    target_mask = torch.zeros_like(region_id, dtype=torch.bool)
    for rid in target_region_ids:
        target_mask |= region_id == int(rid)
    outside_mask = ~target_mask

    if not bool(target_mask.any()):
        raise ValueError("Target region contains no Gaussians")

    target_change = magnitude[target_mask]
    outside_change = magnitude[outside_mask]

    target_sum = target_change.sum()
    outside_sum = outside_change.sum()
    total_sum = target_sum + outside_sum

    active = magnitude > active_threshold
    active_outside = active & outside_mask
    active_target = active & target_mask

    return {
        "num_gaussians": int(magnitude.numel()),
        "num_target_gaussians": int(target_mask.sum().item()),
        "num_outside_gaussians": int(outside_mask.sum().item()),
        "target_change_sum": float(target_sum.item()),
        "outside_change_sum": float(outside_sum.item()),
        "target_change_mean": float(target_change.mean().item()),
        "outside_change_mean": (
            float(outside_change.mean().item()) if bool(outside_mask.any()) else 0.0
        ),
        "leakage_ratio": float((outside_sum / (total_sum + eps)).item()),
        "target_active_fraction": float(
            active_target.sum().item() / max(1, target_mask.sum().item())
        ),
        "outside_active_fraction": float(
            active_outside.sum().item() / max(1, outside_mask.sum().item())
        ),
        "max_target_displacement": float(target_change.max().item()),
        "max_outside_displacement": (
            float(outside_change.max().item()) if bool(outside_mask.any()) else 0.0
        ),
        "active_threshold": float(active_threshold),
    }


def compare_semantic_assignments(before_region_id: torch.Tensor, after_region_id: torch.Tensor) -> dict:
    if before_region_id.shape != after_region_id.shape:
        raise ValueError("Semantic assignment arrays must have the same shape")
    changed = before_region_id != after_region_id
    return {
        "num_gaussians": int(changed.numel()),
        "num_changed": int(changed.sum().item()),
        "semantic_drift_fraction": float(changed.float().mean().item()),
    }
