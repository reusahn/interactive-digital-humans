# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Frozen left-wrist benchmark

The completed left-wrist causal finding is frozen across **three independently pretrained HUGS NeuMan checkpoints**.

Independent unit: pretrained checkpoint, `n = 3`.

Within-checkpoint pose diagnostics: `18` total, nested within those three checkpoints and not to be counted as 18 independent replications.

```text
checkpoint causal passes: 3 / 3
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9808287038512752
global maximum ablated contralateral sum: 0.0
LEFT-WRIST CROSS-CHECKPOINT BENCHMARK FROZEN: True
```

Frozen primary claim:

> In three independently pretrained HUGS NeuMan checkpoints, Seattle, Parkinglot, and Jogging, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding subject-specific SMPL-derived K6 target under the tested left-wrist perturbation. The causal pattern is stable across the tested base poses within each checkpoint.

Do not pool raw displacement across sequences because sequence scale differs. Do not describe the 18 frame tests as independent replications.

## Predeclared second-joint protocol

Frozen before any left-elbow displacement was inspected:

- joint: `left_elbow` (`SMPL 18`)
- axis: `z`
- perturbation: `+10 deg`
- checkpoints: Seattle, Parkinglot, Jogging
- pose schedules: Seattle `[2,7,12,17]`, Parkinglot `[2,7,12,17]`, Jogging `[2,7,12,17,22,27,32,37,42,47]`
- confidence threshold: `>=0.9`
- contralateral anatomy: `{14,17,19,21,23}`
- perturbed branch channels: `{18,20,22}`
- expected changed transforms: exactly `[18,20,22]`

Frozen diagnostic thresholds:

```text
K6 reduction vs learned >= 95%
selective-ablation reduction >= 99.999%
removed-mass vs displacement-reduction correlation >= 0.90
maximum ablated contralateral displacement <= 1e-8
changed transforms exactly [18,20,22]
```

Failures remain results. Do not change joint, axis, angle, mask, or thresholds in response to outcome.

## Canonical anatomy sources frozen at Step 17A2

- Seattle masks: `saved_dominant` + `saved_confidence` from Step 13A
- Parkinglot masks: stored `dominant_joint` + `joint_confidence` from Step 16C2
- Jogging masks: stored `dominant_joint` + `joint_confidence` from Step 16D3
- K6 deformation condition: checkpoint-specific `effective_lbs`

Counts:

```text
Seattle    HC 197778  contra 33072
Parkinglot HC 292095  contra 77622
Jogging    HC 148392  contra 20887
CANONICAL ANATOMY SOURCES FROZEN: True
```

Seattle's saved/recomputed anatomy discrepancy is a provenance issue. The deeper historical reason `saved_confidence` differs from `max(effective_lbs)` for a few rows remains unresolved, but the benchmark-consistent anatomy source is frozen.

## Step 17B1 - left-elbow raw-frame-2 causal result

The predeclared left-elbow `z +10 deg` causal test passed in all three independently pretrained checkpoints on the common raw frame 2.

| Checkpoint | Learned contra | K6 contra | Ablated contra | Learned contra % HC | K6 reduction | Ablation reduction | Removed-mass corr | Changed transforms | Pass |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Seattle | 2.6505639553 | 0.0048044017 | 0.0 | 0.5360253% | 99.8187404% | 100.0% | 0.9708237 | `[18,20,22]` | True |
| Parkinglot | 11.0941810608 | 0.0116030509 | 0.0 | 0.5745978% | 99.8954132% | 100.0% | 0.9958911 | `[18,20,22]` | True |
| Jogging | 1.2263532877 | 0.0009509723 | 0.0 | 0.6924628% | 99.9224553% | 100.0% | 0.9863545 | `[18,20,22]` | True |

```text
checkpoint frame-2 passes: 3 / 3
minimum K6 reduction: 99.81874039866663%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation: 0.9708236964422226
maximum ablated contralateral displacement: 0.0
ALL THREE FRAME-2 ELBOW CAUSAL PASSES: True
```

Interpretation: this is strong second-joint causal evidence at one common base pose per checkpoint. It is **not yet** elbow pose-robustness evidence over the full predeclared schedules.

## Foundational source-semantics caveat now prioritized

Before running and interpreting the full elbow pose schedules, perform the exact official-source semantics audit that has remained unresolved since Parkinglot learned-LBS reconstruction.

Reason:

- exact source commit is fixed at `86ebe5522a384fc553f07f090b63a76dd4af8d33`
- checkpoints/configs use `hugs_triplane`
- packaged configs include `human.activation` (Parkinglot observed `relu`; audit all relevant configs)
- learned-LBS reconstructions instantiated the official decoder classes with strict state loading
- **activation functions are not encoded in the state dict**, so strict loading alone cannot prove that the reconstruction used the exact activation semantics of official `hugs_triplane`

The audit must establish from the exact source:

1. how `hugs_triplane` constructs `GeometryDecoder` and `DeformationDecoder`,
2. whether `human.activation` is passed or ignored,
3. decoder default activation values,
4. exact canonical forward equations including `softmax(lbs_weights / 0.1)`,
5. exact canonical xyz formula,
6. `disable_posedirs` behavior and `A_vitruvian2pose` convention,
7. whether the Step-16C1 / Step-16D2 reconstruction matches official semantics.

If semantics match, all current Parkinglot/Jogging results stand. If they do not, reconstruction-dependent results must be rerun before further interpretation.

## Immediate next action

Run **Step 17B1A / source-semantics audit** only. Do not run the full elbow pose schedules until it is reviewed.

## Continuity files

- `research/sessions/2026-09-15-step17b1.md`
- `experiments/08-second-joint-generalization/analysis/17B1_left_elbow_frame2_cross_checkpoint.csv`
- `research/sessions/2026-09-15-step17a2.md`
- `experiments/08-second-joint-generalization/analysis/17A2_left_elbow_canonical_precursor.csv`
- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/protocols/2026-09-15-second-joint-generalization-implementation-note.md`
