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

## Step 17A precursor

Before perturbation, aggregate learned branch support `{18,20,22}` exceeds K6 support on the contralateral subset in all three checkpoints. This is descriptive precursor evidence only.

Original Step-17A Seattle recomputation used `argmax/max(effective_lbs)` and returned `197781` HC / `33074` contralateral, creating a small mismatch with the frozen Seattle benchmark.

## Step 17A1 Seattle reconciliation

The Seattle mismatch is an anatomy-source provenance issue, not a threshold comparator issue.

```text
recomputed effective_lbs anatomy: HC 197781, contra 33074
saved Step-13A anatomy:           HC 197778, contra 33072
frozen corrected benchmark:       HC 197778, contra 33072
```

Only `saved_dominant` / `saved_confidence` reproduce the reviewed Step-13A / Step-14E Seattle benchmark. The two extra recomputed contralateral rows are indices `239232` and `269473`.

## Step 17A2 canonical anatomy freeze

Canonical anatomy sources are now frozen before causal elbow testing:

- Seattle masks: `saved_dominant` + `saved_confidence` from Step 13A
- Parkinglot masks: stored `dominant_joint` + `joint_confidence` from Step 16C2
- Jogging masks: stored `dominant_joint` + `joint_confidence` from Step 16D3
- K6 deformation condition for all checkpoints: checkpoint-specific `effective_lbs`

Expected anatomy counts are reproduced exactly:

| Checkpoint | HC | Contra | K6 branch mean | Learned branch mean | Learned/K6 ratio |
|---|---:|---:|---:|---:|---:|
| Seattle | 197778 | 33072 | 5.826754e-7 | 4.130765e-4 | 708.9308x |
| Parkinglot | 292095 | 77622 | 2.163267e-7 | 2.398380e-4 | 1108.6841x |
| Jogging | 148392 | 20887 | 2.763716e-7 | 3.745635e-4 | 1355.2894x |

Seattle's two-row correction is negligible for the precursor:

```text
K6 mean delta:      +3.52429e-11
learned mean delta: +2.29047e-8
precursor ordering preserved: True
CANONICAL ANATOMY SOURCES FROZEN: True
```

The deeper historical reason Seattle `saved_confidence` differs from `max(effective_lbs)` for a few rows remains unresolved, but the implementation source mapping is now fixed and benchmark-consistent.

## Immediate next action

Run **Step 17B1: predeclared left-elbow causal diagnostic on raw frame 2 across Seattle, Parkinglot, and Jogging** using the frozen Step-17A2 masks.

For every checkpoint:

1. perturb `left_elbow z +10 deg`,
2. require changed transforms exactly `[18,20,22]`,
3. compare learned, K6 target, and selective `{18,20,22}` ablation on the fixed contralateral subset,
4. evaluate the already-frozen causal thresholds independently per checkpoint,
5. do not pool raw displacement magnitudes across checkpoints.

Only after frame-2 results are reviewed should the full nested pose schedules be run.

## Continuity files

- `research/sessions/2026-09-15-step17a2.md`
- `experiments/08-second-joint-generalization/analysis/17A2_left_elbow_canonical_precursor.csv`
- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/protocols/2026-09-15-second-joint-generalization-implementation-note.md`
- `research/sessions/2026-09-15-step17a1.md`
- `experiments/08-second-joint-generalization/analysis/17A1_seattle_mask_reconciliation.json`
- `research/sessions/2026-09-15-step17a.md`
