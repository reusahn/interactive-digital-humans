# 2026-09-17 — Step 19I1A integration smoke import failure

Status: `IMPLEMENTATION_SMOKE_FAILURE_PRESERVED`

Scientific training performed: **NO**

Scientific Step-19 outcome observed: **NO**

## Context

Step 19 preregistration was already frozen. Step 19I0 had successfully implemented and smoke-tested the isolated 99%-support-envelope locality primitive on branch `step19-locality-impl`, commit:

`f6065a9ca07a3dac2133f14d9e7f135e7a2c3f87`

Step 19I1A then began integrating the frozen A1 locality loss into the audited HUGS source base.

## What succeeded before failure

The cell verified:

- input HEAD exactly matched I0 commit `f6065a9ca07a3dac2133f14d9e7f135e7a2c3f87`
- worktree was clean at start
- existing HUGS `gt_lbs_weights` path was present
- normalized learned `lbs_weights` reached the loss path
- existing `loss.backward()` path was present
- two `gt_lbs_weights` reference calls were changed to make `K=6` explicit
- HUGS softmax temperature was not changed
- deformation equation was not changed
- `cfg.human.loss.locality_w = 0.0` was added
- `HumanSceneLoss` constructor style was detected and trainer construction was patched
- patched files passed `py_compile`

## Failure

The actual HUGS deformation-decoder gradient smoke test failed before the decoder was instantiated.

The test attempted:

```python
importlib.import_module("hugs.models.modules.decoders")
```

Python therefore executed `hugs/models/__init__.py`, which imports `SceneGS`, then `hugs/models/scene.py`, which imports `loguru`.

The canonical legacy environment did not have `loguru` installed, producing:

```text
ModuleNotFoundError: No module named 'loguru'
```

The test stdout had only reached:

```text
candidate decoder classes: ['DeformationDecoder']
```

No locality gradient result was produced.

## Interpretation

This is an **implementation-test import failure**, not evidence against the locality method.

The failure occurred before:

- actual `DeformationDecoder` construction
- locality forward computation through that decoder
- locality backward computation through that decoder
- any scientific HUGS training
- any Seattle validation/test evaluation
- any Parkinglot/Jogging evaluation
- any Step-19 scientific metric

The source modifications made before the crash are expected to remain as an uncommitted dirty worktree and must be inspected/recovered rather than silently discarded or overwritten.

## Recovery rule

Do not install or substitute a different HUGS version merely to bypass this failure.

Recover from the current dirty implementation worktree. Re-run the decoder-gradient smoke by directly loading the exact audited `decoders.py` / `activation.py` source without importing the full `hugs.models` package, so unrelated runtime dependencies such as `loguru` are not required.

Preserve this failure record even after recovery succeeds.
