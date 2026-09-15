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

The exact historical reason `saved_confidence` differs from `max(effective_lbs)` for a few Seattle rows remains unresolved. This does not alter the implementation rule above, which was frozen before the causal elbow test.

## Step 17B1 frame-2 causal result

The predeclared left-elbow `z +10 deg` diagnostic passed on raw frame 2 in Seattle, Parkinglot, and Jogging using the frozen Step-17A2 masks. Changed transforms were exactly `[18,20,22]` in every checkpoint. Minimum K6 reduction was `99.8187404%`, selective branch ablation reduction was `100%` in all three, minimum removed-mass correlation was `0.9708237`, and maximum ablated contralateral displacement was `0.0`.

This is one common tested pose per independent checkpoint and does not yet establish elbow pose robustness over the complete predeclared schedules.

## Step 17B1A exact source-semantics audit

The reconstruction semantics used by the current experiments were checked against exact HUGS commit `86ebe5522a384fc553f07f090b63a76dd4af8d33`.

All Seattle, Parkinglot, and Jogging packaged configs contain `human.name: hugs_triplane` and `human.activation: relu`. The located triplane implementation is `hugs/models/hugs_trimlp.py`, class `HUGS_TRIMLP`.

Its constructor does not pass an activation argument into either decoder:

```text
DeformationDecoder(n_features=n_features*3, disable_posedirs=disable_posedirs)
GeometryDecoder(n_features=n_features*3, use_surface=use_surface)
```

The exact decoder classes instead default to `act='gelu'`. Thus the packaged `human.activation: relu` value is not routed into these decoder constructors in the located implementation, and the reconstruction used the same default GELU semantics.

The source audit also confirmed:

- learned LBS softmax temperature `0.1`
- canonical xyz as checkpoint xyz plus geometry xyz offset
- `A_vitruvian2pose = A_t2pose @ inv_A_t2vitruvian`
- `disable_posedirs=True` causes zero pose offsets and `v_posed = v_shaped`

Numeric source-exact reconstruction matched stored experimental arrays exactly:

- Seattle learned LBS: all absolute differences `0.0`, dominant mismatch `0`
- Parkinglot learned LBS and canonical xyz: all absolute differences `0.0`
- Jogging learned LBS and canonical xyz: all absolute differences `0.0`

Therefore the previous activation caveat is resolved and no reconstruction rerun is indicated by this audit.

### Remaining provenance-link check

Step 17B1A located `HUGS_TRIMLP` heuristically from the source tree. Because the packaged config literal is `hugs_triplane` while the class/file is named `HUGS_TRIMLP`, one final lightweight check should explicitly traverse the official model factory or registry and record the `hugs_triplane -> HUGS_TRIMLP` alias. This is a source-provenance closure only. It does not change any reconstruction, mask, threshold, perturbation, or endpoint.
