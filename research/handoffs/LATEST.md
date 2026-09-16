# Latest Research Handoff

Current continuation date: **2026-09-16**.

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints and are not independent model-level replications
- wrist, elbow, and shoulder are repeated joint diagnostics within the same three checkpoints

## Frozen wrist benchmark

Step 16E0 left wrist:

```text
checkpoint passes: 3/3
nested pose diagnostics: 18
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9808287038512752
global maximum ablated contralateral sum: 0.0
```

## Frozen elbow benchmark

Step 17C0 predeclared left elbow generalization:

```text
checkpoint passes: 3/3
nested pose diagnostics: 18
global minimum K6 reduction: 99.81874059431833%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral: 0.0
```

Combined wrist + elbow benchmark:

```text
independent checkpoints: 3
tested joints: 2
nested pose diagnostics: 36
joint x checkpoint cells passing: 6/6
```

## Historical Step-17 numerical reproduction note

Historical Step-17 output explicitly records `deformation device: cuda`, but the original GPU model/runtime versions are not preserved.

Exact reconstruction of the historical elbow archive under a frozen `1e-5` aggregate tolerance gives `5/6` on all tested replacement runtimes:

- modern A100, PyTorch 2.11 / CUDA 12.8
- A100, PyTorch 1.13.1 / CUDA 11.7
- T4, PyTorch 1.13.1 / CUDA 11.7

Parkinglot learned changes magnitude and sign across runtimes while field Pearson correlations remain effectively `1.0`. This is treated as historical float32/runtime numerical sensitivity, not disappearance of the scientific field. The historical gate was not widened.

## Frozen primary Step-18 runtime

```text
GPU: Tesla T4
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

This is a continuation choice, not a claim that historical Step 17 used T4.

## Frozen shoulder protocol

Predeclared before shoulder causal output:

- joint: left shoulder, SMPL 16
- perturbation: local `z +10°`
- descendant branch: `[16,18,20,22]`
- expected changed transforms: `[16,18,20,22]`
- frozen contralateral subset: `{14,17,19,21,23}`
- Seattle poses: `[2,7,12,17]`
- Parkinglot poses: `[2,7,12,17]`
- Jogging poses: `[2,7,12,17,22,27,32,37,42,47]`
- K6 reduction threshold: `>=95%`
- selective-ablation reduction threshold: `>=99.999%`
- max/summed ablated response: `<=1e-8`
- removed-mass/displacement-reduction correlation: `>=0.90`

Protocol: `research/protocols/2026-09-16-third-joint-generalization.md`

## Step 18B2 shoulder result

The predeclared universal shoulder generalization failed and remains failed.

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
corr passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction range: -77.671145% to 76.389818%
correlation range: 0.798583 to 0.981240
predeclared third-joint universal pass: False
```

Parkinglot has K6 > learned shoulder displacement in all four tested poses. Seattle is mixed. Jogging has learned > K6 in all ten poses but remains far below the frozen `95%` K6-reduction criterion.

Archived: `research/sessions/2026-09-16-step18b2.md`.

## Step 18C0 three-joint synthesis FROZEN

Drive artifact:

`experiments/08-second-joint-generalization/18C0_three_joint_synthesis.json`

Frozen comparison:

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification | Global minimum K6 reduction |
|---|---|---|---|---:|
| left wrist | PASS | supported | supported | `99.708575%` |
| left elbow | PASS | supported | supported | `99.818741%` |
| left shoulder | FAIL | supported | not supported | `-77.671145%` |

Frozen claims:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

Archived: `research/sessions/2026-09-16-step18c0.md`.

## Step 18C1 exploratory shoulder support-mass decomposition COMPLETE

Status: exploratory/post-hoc. No confirmatory claim changed.

Checkpoint-level aggregate shoulder branch support and majority displacement direction agree in `3/3` checkpoints:

```text
Seattle    learned/K6 support ratio = 1.576428, support favors learned, displacement majority favors learned
Parkinglot learned/K6 support ratio = 0.837905, support favors K6,      displacement majority favors K6
Jogging    learned/K6 support ratio = 5.555706, support favors learned, displacement majority favors learned
```

Per-Gaussian delta-support vs delta-displacement correlations are high overall, approximately `0.802` to `0.982` across poses.

Interpretation: branch-support amount and spatial distribution are major explanatory factors, but pose geometry and/or within-branch composition still modulate the final displacement field.

Archived: `research/sessions/2026-09-16-step18c1.md`.

## Step 18C2 exploratory support-matching counterfactual COMPLETE

Counterfactual on frozen contralateral rows:

- preserve learned within-branch composition on `[16,18,20,22]`
- replace learned total shoulder-branch mass with the corresponding K6 total branch mass
- preserve learned non-branch proportions while maintaining row sum
- fallback to K6 composition only if learned composition is undefined

Validation:

```text
pure learned-composition fraction: 1.0 in all 3 checkpoints
branch fallback rows: 0
outside fallback rows: 0
row-sum max error: <= 2.384185791015625e-07
K6 branch-mass match max error: <= 6.984919309616089e-10
```

Field MAE-gap reduction after branch-mass matching:

```text
Seattle    min/median/max: 68.341709 / 94.495471 / 96.352339%
Parkinglot min/median/max: 73.579259 / 83.846952 / 87.244704%
Jogging    min/median/max: 71.242567 / 93.517130 / 96.921237%
```

Field RMSE-gap reduction:

```text
Seattle    min/median/max: 66.823938 / 94.260978 / 95.829274%
Parkinglot min/median/max: 92.691984 / 95.606291 / 96.571410%
Jogging    min/median/max: 52.197888 / 88.838528 / 94.903711%
```

Counterfactual-vs-K6 field correlations:

```text
Seattle    min/median/max: 0.993263 / 0.994395 / 0.999783
Parkinglot min/median/max: 0.989209 / 0.996750 / 0.998534
Jogging    min/median/max: 0.789515 / 0.958796 / 0.994655
```

Most contralateral Gaussians move closer to K6 after mass matching. The fraction improved is roughly `0.90-0.94` in Seattle, `0.95` in Parkinglot, and `>0.99` in Jogging.

### C2 interpretation

Total shoulder-descendant branch mass is a **dominant exploratory explanatory factor** for the shoulder learned-vs-K6 displacement difference. Matching only total branch mass while preserving learned within-branch composition removes most of the original spatial-field gap in most poses.

This is not a complete mechanism:

- residual error remains
- some poses have lower RMSE-gap reduction/correlation
- aggregate displacement sums can overshoot K6 even when field MAE/RMSE improve strongly
- within-branch composition and pose geometry remain plausible residual determinants

The shoulder confirmatory result remains failed. Step 18C2 does not rescue it and does not establish kinematic depth as causal.

Archived:

- `research/sessions/2026-09-16-step18c2.md`
- Drive `experiments/08-second-joint-generalization/18C2_shoulder_support_match_counterfactual.json`
- Drive `experiments/08-second-joint-generalization/18C2_shoulder_support_match_counterfactual_displacements.npz`

## Exact next action

Run one reciprocal **Step 18C3 within-branch composition counterfactual** before ending the shoulder decomposition:

- preserve each learned row's total shoulder-descendant branch mass
- replace only the learned within-branch allocation over `[16,18,20,22]` with the K6 within-branch composition
- keep the same frozen shoulder perturbation and pose schedules
- compare learned-vs-K6 field-gap reduction against Step 18C2

Interpretation goal: directly separate the contribution of **total branch mass** from **within-branch joint allocation**. Keep the analysis exploratory/post-hoc. Do not introduce another joint yet.

## Research-record rule

Preserve the negative shoulder generalization result. Exploratory mechanism decomposition after Step 18C0 cannot change the predeclared pass/fail outcome. Do not tune shoulder thresholds or add joints merely to seek a passing result.
