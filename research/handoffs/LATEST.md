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

> In three independently pretrained HUGS NeuMan checkpoints, Seattle, Parkinglot, and Jogging, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding subject-specific SMPL-derived K=6 target under the tested left-wrist perturbation. The causal pattern is stable across the tested base poses within each checkpoint.

Do not pool raw displacement across sequences because sequence scale differs. Prefer normalized contralateral `% HC`, reduction ratios, and causal correlations for cross-checkpoint comparison. Do not describe the 18 frame tests as independent replications.

## Predeclared second-joint protocol

The second-joint generalization target was frozen before inspecting second-joint results:

- joint: `left_elbow` (`SMPL 18`)
- axis: `z`
- perturbation: `+10 deg`
- checkpoints: Seattle, Parkinglot, Jogging
- same pose schedules as the wrist benchmark
- K6 confidence threshold: `>=0.9`
- fixed contralateral anatomy: `{14,17,19,21,23}`
- perturbed branch channels: `{18,20,22}`
- expected changed SMPL transforms: exactly `[18,20,22]`
- selective intervention: zero only channels `{18,20,22}` on the fixed HC contralateral subset, then renormalize

Frozen diagnostic thresholds:

```text
K6 reduction vs learned >= 95%
selective-ablation reduction >= 99.999%
removed-mass vs displacement-reduction correlation >= 0.90
maximum ablated contralateral displacement <= 1e-8
changed transforms exactly [18,20,22]
```

Failures remain results. Do not change joint, axis, angle, mask, or thresholds in response to outcome.

## Step 17A - left-elbow pre-perturbation precursor

No elbow perturbation has been applied yet.

| Checkpoint | Contra count | K6 branch mean | Learned branch mean | Learned/K6 ratio | Learned >1e-3 | K6 >1e-3 |
|---|---:|---:|---:|---:|---:|---:|
| Seattle | 33074 | 5.8264015e-7 | 4.1305361e-4 | 708.9343x | 0.0953922 | 0.0 |
| Parkinglot | 77622 | 2.1632670e-7 | 2.3983797e-4 | 1108.6841x | 0.0502048 | 0.0 |
| Jogging | 20887 | 2.7637162e-7 | 3.7456353e-4 | 1355.2894x | 0.0780390 | 0.0 |

Learned left-elbow-branch support exceeds K6 support in all three checkpoints while K6-HC dominant-joint agreement remains above `0.99992`. This is descriptive precursor evidence only, not a second-joint causal replication.

## Active blocker before elbow perturbation

Step 17A exposed a Seattle mask-count mismatch that must be reconciled before causal testing:

```text
Step 17A recomputed from 13A effective_lbs:
HC count:     197781
contra count: 33074

Previously reviewed corrected Seattle benchmark:
HC count:     197778
contra count: 33072
```

The Seattle K6 file contains both `effective_lbs` and saved anatomy fields `saved_dominant` / `saved_confidence`. The 3-HC / 2-contralateral difference may be a threshold-boundary or assignment-source issue, but no explanation is accepted until directly audited.

**Do not run the left-elbow perturbation yet.**

## Immediate next action

Run **Step 17A1: Seattle K6 mask reconciliation**. Compare recomputed anatomy from `effective_lbs` against `saved_dominant` / `saved_confidence`, identify the exact discrepant rows and their confidence values around `0.9`, and determine which source reproduces the already-frozen corrected Seattle benchmark counts `197778` HC and `33072` contralateral.

The predeclared elbow protocol remains unchanged.

## Continuity files

- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/sessions/2026-09-15-step17a.md`
- `experiments/08-second-joint-generalization/analysis/17A_left_elbow_cross_checkpoint_precursor.csv`
- `research/sessions/2026-09-15-step16e0.md`
- `experiments/07-cross-sequence-replication/analysis/16E0_left_wrist_cross_checkpoint_summary.csv`
