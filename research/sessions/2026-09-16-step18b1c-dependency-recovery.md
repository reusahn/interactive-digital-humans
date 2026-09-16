# Research Session Checkpoint - 2026-09-16 Step 18B1C Dependency Recovery

## Purpose

Recover the exact SMPLX dependency required for the source-exact Step 18B1C audit after the prior Colab runtime failed with `ModuleNotFoundError: No module named 'smplx'`.

## Result

Installed and verified the HUGS-pinned dependency:

```text
smplx version: 0.1.28
smplx module: /usr/local/lib/python3.13/dist-packages/smplx/__init__.py
SMPLX 0.1.28 EXACT DEPENDENCY PASS: True
```

The following exact `smplx.lbs` functions imported successfully:

- `batch_rodrigues`
- `blend_shapes`
- `vertices2joints`
- `batch_rigid_transform`

## Interpretation

This resolves the environment blocker only. No elbow source-exact comparison and no shoulder causal computation were performed in the recovery cell.

The frozen Step 18 shoulder protocol and the frozen `1e-5` historical elbow regression tolerance remain unchanged.

## Exact next action

Rerun Step 18B1C in the same runtime now that `smplx==0.1.28` is available. The audit remains elbow-only and must compare manual transforms against source-exact SMPLX transforms before any shoulder result is accepted.
