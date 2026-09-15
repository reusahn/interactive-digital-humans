# Second-Joint Protocol Implementation Note

Date: 2026-09-15

This note was added after Step 17A1 and **before any left-elbow perturbation**. It does not change the predeclared joint, axis, angle, anatomical IDs, branch channels, confidence threshold, pose schedules, or causal pass thresholds.

## Seattle anatomy-source reconciliation

The historical Seattle Step-13A K6 artifact contains both:

- `effective_lbs`, used as the actual K6 deformation-weight condition
- `saved_dominant` / `saved_confidence`, used by the frozen Seattle anatomical benchmark

Recomputing `argmax/max(effective_lbs)` gives `197781` high-confidence and `33074` contralateral Gaussians. The saved anatomy fields give `197778` high-confidence and `33072` contralateral Gaussians, exactly reproducing the reviewed Step-13A / Step-14E Seattle benchmark.

This is not a `>= 0.9` versus `> 0.9` issue. Step 17A1 found no exact confidence values at `0.9` and identified five HC membership differences, including two contralateral rows.

## Frozen implementation rule for second-joint testing

For Seattle:

- anatomical mask source: `saved_dominant` + `saved_confidence` from `13A_k6_effective_mapping.npz`
- K6 deformation weights: `effective_lbs` from the same artifact

For Parkinglot:

- anatomical mask source: stored `dominant_joint` + `joint_confidence` from `16C2_parkinglot_k6_effective_mapping.npz`
- K6 deformation weights: stored `effective_lbs`

For Jogging:

- anatomical mask source: stored `dominant_joint` + `joint_confidence` from `16D3_jogging_k6_effective_mapping.npz`
- K6 deformation weights: stored `effective_lbs`

The confidence rule remains `>= 0.9` for all three checkpoints. The Seattle source distinction is a provenance correction required to preserve the already-frozen benchmark anatomy, not a post-hoc threshold or endpoint change.
