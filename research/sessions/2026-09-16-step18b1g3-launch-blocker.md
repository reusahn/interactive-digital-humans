# Research Session Checkpoint — 2026-09-16 Step 18B1G3 launch blocker

## Context

After Step 18B1G2 ruled out displacement norm/evaluation placement, the next action was to reproduce Step-17B1 elbow frame 2 in an isolated legacy HUGS-compatible environment targeting Python 3.8, PyTorch 1.13.1 + CUDA 11.7, NumPy 1.24.4, SciPy 1.10.1, and SMPLX 0.1.28.

A complete regression script was downloaded to:

`/content/step18b1g3_legacy_elbow_regression.py`

and the isolated interpreter was:

`/content/hugs_legacy_torch113_py38/bin/python`

## Failure

The wrapper reached:

```text
STARTING LEGACY ELBOW REGRESSION
```

but `subprocess.run(..., check=True)` raised:

```text
CalledProcessError: Command '['/content/hugs_legacy_torch113_py38/bin/python', '/content/step18b1g3_legacy_elbow_regression.py']' returned non-zero exit status 1.
```

The wrapper did not capture or print the child process stderr, so the underlying exception inside the legacy script is currently unknown.

## Interpretation

This is an execution-wrapper diagnostic failure, not a scientific result. The legacy elbow regression did not complete and no conclusion can be drawn about PyTorch 1.13.1 + CUDA 11.7 numerical equivalence.

No shoulder computation ran. No tolerance, joint, mask, perturbation, branch, or pose schedule changed.

## Exact next action

Rerun the same legacy script with `capture_output=True`, `text=True`, and `check=False`, printing child return code, stdout, and stderr in full. Do not reinstall or alter the environment until the actual child exception is visible.
