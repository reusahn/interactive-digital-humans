# Research Session Checkpoint — 2026-09-16 Step 18B1C namespace blocker

## Attempt

After installing the HUGS-pinned dependency `smplx==0.1.28`, Step 18B1C was rerun to compare the current manual SMPL transform path against source-exact `smplx.lbs` functions.

## Failure

Execution stopped immediately in Seattle before any transform comparison or displacement audit:

```text
TypeError: blend_shapes() missing 1 required positional argument: 'shape_disps'
```

The cause was notebook namespace pollution from the dependency-recovery verification cell. That cell imported `batch_rodrigues`, `blend_shapes`, `vertices2joints`, and `batch_rigid_transform` without aliases. Step 18B1's earlier `compute_A` resolves helper names dynamically from the notebook globals, so its intended one-argument local `blend_shapes(betas)` helper had been replaced by `smplx.lbs.blend_shapes(betas, shape_disps)`.

## Interpretation

This is an implementation/runtime-state failure only. It provides no scientific evidence about the manual-versus-SMPLX transform discrepancy and no shoulder causal computation ran.

No tolerance, mask, joint, axis, perturbation angle, branch, or pose schedule is changed.

## Correction

Patch Step 18B1C so that:

- source-exact SMPLX functions are imported only under `sx_*` aliases
- manual reconstruction helpers are redefined under isolated `manual_*` names
- the audit does not call the namespace-polluted global `compute_A`
- elbow frame 2 remains the only scientific target
- shoulder remains uncomputed

Failure ledger: `A013`.
