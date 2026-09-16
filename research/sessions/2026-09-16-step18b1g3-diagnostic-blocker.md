# Research Session Checkpoint — 2026-09-16 Step 18B1G3 diagnostic blocker

## Purpose

Diagnose why the isolated official-HUGS-style legacy environment failed before producing any Step-17B1 elbow regression result.

## Legacy environment verification

The isolated runtime itself is valid:

```text
Python: 3.8.20
Torch: 1.13.1+cu117
Torch CUDA build: 11.7
CUDA available: True
GPU: NVIDIA A100-SXM4-40GB
NumPy: 1.24.4
SciPy: 1.10.1
SMPLX import: OK
```

## Failure

The actual legacy regression subprocess failed before any scientific computation while loading `private_assets/smpl/SMPL_NEUTRAL_clean.pkl`.

```text
ModuleNotFoundError: No module named 'numpy._core'
```

The failure occurs at `pickle.load(f)`.

## Interpretation

This is a serialization compatibility problem, not a CUDA, SMPL, elbow, or shoulder scientific result. `SMPL_NEUTRAL_clean.pkl` was regenerated under a NumPy 2.x runtime, whose pickle references the private module path `numpy._core`. The isolated legacy environment intentionally uses NumPy 1.24.4, where the corresponding implementation lives under `numpy.core`, so the pickle cannot be imported directly.

The numerical environment itself successfully initializes CUDA 11.7 / PyTorch 1.13.1 on the A100. Therefore the legacy regression remains testable once this pickle compatibility layer is repaired.

No elbow displacement was computed in this failed run. No shoulder causal computation was run. No tolerance changed.

## Exact next action

Patch only the legacy subprocess loader by installing temporary `sys.modules` aliases from `numpy._core*` to the corresponding `numpy.core*` modules before `pickle.load`. First validate that the clean SMPL pickle loads and has the expected SMPL array shapes under NumPy 1.24.4. If that validation passes, rerun the same unchanged Step 18B1G3 elbow regression in the legacy environment.
