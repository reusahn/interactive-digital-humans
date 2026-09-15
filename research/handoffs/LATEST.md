# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Frozen left-wrist benchmark

The completed left-wrist causal finding is now frozen across **three independently pretrained HUGS NeuMan checkpoints**.

Independent unit: pretrained checkpoint, `n = 3`.

Within-checkpoint pose diagnostics: `18` total, nested within those three checkpoints and not to be counted as 18 independent replications.

| Checkpoint | Poses | Learned contra % HC mean | Learned contra % HC range | Mean K6 reduction | Minimum K6 reduction | Minimum selective reduction | Mean removed-mass correlation | Minimum correlation | Max ablated contra | Causal pass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Seattle | 4 | 4.993387 | 4.930677-5.034862 | 99.818441% | 99.817537% | 100.0% | 0.981149 | 0.980829 | 0.0 | True |
| Parkinglot | 4 | 3.394478 | 3.392597-3.397105 | 99.708796% | 99.708575% | 100.0% | 0.997534 | 0.997517 | 0.0 | True |
| Jogging | 10 | 8.453632 | 8.343905-8.673447 | 99.819317% | 99.817791% | 100.0% | 0.990030 | 0.989911 | 0.0 | True |

Checkpoint-level synthesis:

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

> In three independently pretrained HUGS NeuMan checkpoints, Seattle, Parkinglot, and Jogging, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding subject-specific SMPL-derived K=6 target under the tested left-wrist perturbation. The causal pattern is stable across the tested base poses within each checkpoint.

Do not pool raw displacement across sequences because sequence scale differs. Prefer normalized contralateral `% HC`, reduction ratios, and causal correlations for cross-checkpoint comparison.

Do not describe the 18 frame tests as independent replications.

## Second-joint protocol is predeclared

The next generalization target was frozen before inspecting any second-joint result:

- joint: `left_elbow` (`SMPL 18`)
- axis: `z`
- perturbation: `+10 deg`
- independent checkpoints: Seattle, Parkinglot, Jogging
- same predeclared pose schedules as the wrist benchmark
- K6 confidence threshold: `>=0.9`
- fixed contralateral upper-body anatomy: `{right_collar 14, right_shoulder 17, right_elbow 19, right_wrist 21, right_hand 23}`
- perturbed branch channels: `{left_elbow 18, left_wrist 20, left_hand 22}`
- expected changed SMPL transforms for every pose: exactly `[18,20,22]`
- selective intervention: zero only channels `{18,20,22}` on the fixed HC contralateral subset, then renormalize

Frozen diagnostic thresholds, unchanged after observing wrist results:

```text
K6 reduction vs learned >= 95%
selective-ablation reduction >= 99.999%
removed-mass vs displacement-reduction correlation >= 0.90
maximum ablated contralateral displacement <= 1e-8
changed transforms exactly [18,20,22]
```

Failures are to be retained as scientific results. Do not change joint, axis, angle, mask, or thresholds in response to outcome.

## Immediate next action

Run a **pre-perturbation second-joint precursor audit** only. For Seattle, Parkinglot, and Jogging, use the already-authoritative learned LBS and subject-specific K6 targets, define the same fixed K6-HC contralateral upper-body subset, and compare aggregate learned-vs-K6 support on the predeclared left-elbow branch channels `{18,20,22}`.

Do not apply the elbow perturbation until this precursor audit is reviewed.

## Continuity files

- `research/sessions/2026-09-15-step16e0.md`
- `experiments/07-cross-sequence-replication/analysis/16E0_left_wrist_cross_checkpoint_summary.csv`
- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/sessions/2026-09-15-step16d5.md`
