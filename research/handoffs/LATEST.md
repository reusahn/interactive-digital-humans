# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Frozen left-wrist benchmark

The completed left-wrist causal finding is frozen across **three independently pretrained HUGS NeuMan checkpoints**.

Independent unit: pretrained checkpoint, `n = 3`.

Within-checkpoint pose diagnostics: `18` total, nested within those three checkpoints and not to be counted as 18 independent replications.

| Checkpoint | Poses | Learned contra % HC mean | Learned contra % HC range | Mean K6 reduction | Minimum K6 reduction | Minimum selective reduction | Mean removed-mass correlation | Minimum correlation | Max ablated contra | Causal pass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Seattle | 4 | 4.993387 | 4.930677-5.034862 | 99.818441% | 99.817537% | 100.0% | 0.981149 | 0.980829 | 0.0 | True |
| Parkinglot | 4 | 3.394478 | 3.392597-3.397105 | 99.708796% | 99.708575% | 100.0% | 0.997534 | 0.997517 | 0.0 | True |
| Jogging | 10 | 8.453632 | 8.343905-8.673447 | 99.819317% | 99.817791% | 100.0% | 0.990030 | 0.989911 | 0.0 | True |

```text
ALL FRAME-2 REGRESSIONS PASS: True
independent pretrained checkpoints: 3
within-checkpoint pose diagnostics: 18
checkpoint causal passes: 3 / 3
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9808287038512752
global maximum ablated contralateral sum: 0.0
ALL THREE CHECKPOINTS CAUSALLY REPLICATE: True
LEFT-WRIST CROSS-CHECKPOINT BENCHMARK FROZEN: True
```

## Frozen primary claim

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

## Step 17A precursor

Before perturbation, aggregate learned branch support `{18,20,22}` exceeds K6 support on the contralateral subset in all three checkpoints. This is descriptive precursor evidence only.

Original Step-17A Seattle recomputation used `argmax/max(effective_lbs)` and returned `197781` HC / `33074` contralateral, creating a small mismatch with the frozen Seattle benchmark.

## Step 17A1 Seattle reconciliation

The mismatch is now explained at the **anatomy-source** level.

```text
recomputed effective_lbs anatomy: HC 197781, contra 33074
saved Step-13A anatomy:           HC 197778, contra 33072
frozen corrected benchmark:       HC 197778, contra 33072
```

Only `saved_dominant` / `saved_confidence` reproduce the already-reviewed Seattle Step-13A / Step-14E benchmark. This is not a `>=0.9` versus `>0.9` issue: no exact threshold-boundary rows exist.

Detailed differences:

```text
dominant mismatch count: 2
HC decision differences: 5 rows
contralateral differences: 2 rows
HC indices: [239232,269473,287191,296137,299167]
contra indices: [239232,269473]
```

### Frozen anatomy-source implementation rule

- Seattle anatomy masks: `saved_dominant` + `saved_confidence` from `13A_k6_effective_mapping.npz`
- Seattle K6 deformation weights: `effective_lbs` from the same file
- Parkinglot anatomy masks: stored `dominant_joint` + `joint_confidence` from Step 16C2
- Jogging anatomy masks: stored `dominant_joint` + `joint_confidence` from Step 16D3

The predeclared elbow protocol itself is unchanged. This source mapping was frozen **before any elbow perturbation**.

## Immediate next action

Run **Step 17A2** before causal testing:

1. recompute the Seattle elbow precursor using the canonical saved Seattle mask (`197778` HC / `33072` contralateral),
2. compare it with the original Step-17A recomputed-mask precursor,
3. freeze one cross-checkpoint anatomy-source manifest for Seattle/Parkinglot/Jogging,
4. verify the two-row Seattle correction does not change the qualitative precursor conclusion.

Only after Step 17A2 is reviewed should the predeclared left-elbow `z +10 deg` causal perturbation begin.

## Continuity files

- `research/sessions/2026-09-15-step17a1.md`
- `experiments/08-second-joint-generalization/analysis/17A1_seattle_mask_reconciliation.json`
- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/protocols/2026-09-15-second-joint-generalization-implementation-note.md`
- `research/sessions/2026-09-15-step17a.md`
- `experiments/08-second-joint-generalization/analysis/17A_left_elbow_cross_checkpoint_precursor.csv`
