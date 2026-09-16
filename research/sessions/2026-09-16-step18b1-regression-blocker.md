# Research Session Checkpoint — 2026-09-16 Step 18B1 Regression Blocker

## Purpose

Run the frozen left-shoulder frame-2 causal diagnostic only after reproducing the archived Step-17B1 left-elbow frame-2 computation across Seattle, Parkinglot, and Jogging.

The Step-18B1 cell intentionally placed the elbow regression before any shoulder interpretation.

## Result

The elbow regression gate **failed in all three checkpoints**, so execution stopped before the shoulder causal section.

| Checkpoint | Current learned contra | Frozen learned contra | Abs diff | Current K6 contra | Frozen K6 contra | Abs diff | Current corr | Frozen corr | Regression pass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Seattle | 2.650197376676 | 2.650563955300 | 0.000366578624 | 0.004803800226 | 0.004804401660 | 0.000000601434 | 0.970826263032 | 0.970823696400 | False |
| Parkinglot | 11.092557772695 | 11.094181060800 | 0.001623288105 | 0.011602326001 | 0.011603050900 | 0.000000724899 | 0.995891130849 | 0.995891100000 | False |
| Jogging | 1.226277361622 | 1.226353287700 | 0.000075926078 | 0.000953316052 | 0.000950972300 | 0.000002343752 | 0.986356606925 | 0.986354500000 | False |

Other invariants remained correct:

- changed transforms were exactly `[18,20,22]` for all three checkpoints
- selective ablation produced contralateral displacement `0.0` for all three checkpoints
- removed-mass/reduction correlations remained extremely close to the archived values

The frozen aggregate-sum regression tolerance was `1e-5`. Learned contra differences exceeded that tolerance in every checkpoint.

## Interpretation

This is a **pipeline-regression blocker**, not a shoulder result and not evidence against the shoulder hypothesis.

The current manual source-equivalent SMPL/LBS reconstruction is numerically very close to the archived Step-17 computation, but it is not identical enough to pass the frozen regression gate. The pattern is consistent with a small implementation/numerical mismatch in the reconstruction path rather than a change in anatomy, branch definition, or perturbation kinematics.

The guardrail worked as intended: shoulder causal metrics were not interpreted or archived.

Do not widen the tolerance after seeing the failure. Do not alter the frozen shoulder joint, axis, angle, branch, masks, or thresholds.

## Source context

The released HUGS implementation uses its `SMPL` wrapper and imported `smplx.lbs` operations for the posed transforms, then forms `A_vitruvian2pose = A_t2pose @ inv_A_t2vitruvian` and applies `lbs_extra` with the learned weights. The Step-18B1 manual reimplementation reproduced this structure but did not numerically match the archived aggregate results within `1e-5`.

## Exact next action

Run a non-shoulder diagnostic, Step 18B1A:

1. load the archived `17B1_left_elbow_frame2_displacements.npz`
2. recompute the same elbow frame-2 arrays with the currently defined Step-18B1 functions
3. compare per-Gaussian learned, K6, and ablated displacement arrays against the archived arrays
4. compare sums, mean/p99/max absolute differences, and correlations
5. inspect whether the discrepancy is global/proportional or spatially structured
6. do not compute or interpret shoulder causal metrics

Only after the exact numerical source of the regression is isolated should Step 18B1 be repaired and rerun unchanged.
