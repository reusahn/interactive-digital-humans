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

## Step 17A2 verification

Step 17A2 froze these sources into one cross-checkpoint mask artifact before any elbow perturbation and reproduced the expected counts exactly:

| Checkpoint | HC | Contralateral |
|---|---:|---:|
| Seattle | 197778 | 33072 |
| Parkinglot | 292095 | 77622 |
| Jogging | 148392 | 20887 |

Seattle's recomputed mask had only two additional contralateral rows, indices `239232` and `269473`. Both have dominant joint 21 under both saved and recomputed anatomy, but their saved confidence is below 0.9 while recomputed confidence is above 0.9. Excluding those rows changes the Seattle precursor negligibly:

- K6 branch mean: `5.82640155e-7` -> `5.82675398e-7`
- learned branch mean: `4.13053611e-4` -> `4.13076516e-4`

The qualitative precursor ordering remains learned > K6 in Seattle and in all three checkpoints.

Canonical mask artifact:

`experiments/08-second-joint-generalization/17A2_frozen_canonical_anatomy_masks.npz`

The exact historical reason `saved_confidence` differs from `max(effective_lbs)` for a few Seattle rows remains unresolved. This does not alter the implementation rule above, which is now frozen before the causal elbow test.
