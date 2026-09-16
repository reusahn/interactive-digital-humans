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

Checkpoint-level aggregate shoulder branch support and majority displacement direction agree in `3/3` checkpoints. Per-Gaussian delta-support vs delta-displacement correlations are high overall, approximately `0.802` to `0.982` across poses.

Interpretation: branch-support amount and spatial distribution are major explanatory factors, but pose geometry and/or within-branch composition still modulate the final displacement field.

Archived: `research/sessions/2026-09-16-step18c1.md`.

## Step 18C2 exploratory support-matching counterfactual COMPLETE

Per-row shoulder-branch mass matching preserves learned within-branch composition but replaces total branch mass with K6 branch mass.

```text
pure learned-composition fraction: 1.0 in all 3 checkpoints
branch fallback rows: 0
outside fallback rows: 0
```

Field MAE-gap reduction:

```text
Seattle    min/median/max: 68.341709 / 94.495471 / 96.352339%
Parkinglot min/median/max: 73.579259 / 83.846952 / 87.244704%
Jogging    min/median/max: 71.242567 / 93.517130 / 96.921237%
```

Interpretation: per-row branch-support magnitude/topology is a dominant exploratory explanatory factor.

Archived: `research/sessions/2026-09-16-step18c2.md`.

## Step 18C3 exploratory within-branch composition counterfactual COMPLETE

K6 shoulder-branch composition is undefined on most contralateral rows because K6 branch mass is zero there, while learned branch mass is positive on every tested contralateral row.

```text
Seattle K6-zero fraction: 0.7824141267537494
Parkinglot K6-zero fraction: 0.7384762051995568
Jogging K6-zero fraction: 0.9145401445875425
```

Full-field composition matching produces essentially zero or negative median MAE-gap reduction:

```text
Seattle: -0.10402258952364463%
Parkinglot: -2.1951923116722116%
Jogging: 0.20329469100371367%
```

Even on rows where both learned and K6 branch composition are defined, the effect remains small.

Archived: `research/sessions/2026-09-16-step18c3.md`.

## Step 18C4 shoulder mechanism synthesis FROZEN

Drive artifact:

`experiments/08-second-joint-generalization/18C4_shoulder_mechanism_synthesis.json`

Archived session:

`research/sessions/2026-09-16-step18c4.md`

Frozen exploratory mechanism claims:

- confirmatory shoulder status: `FAIL_UNCHANGED`
- branch-mediated causality: `SUPPORTED_IN_FROZEN_TEST`
- support topology and magnitude: `DOMINANT_EXPLORATORY_FACTOR`
- within-branch composition: `SMALL_EFFECT_ON_DEFINED_OVERLAP`
- pose geometry: `RESIDUAL_MODULATOR_PLAUSIBLE`
- kinematic depth: `HYPOTHESIS_ONLY`

The strongest bounded shoulder interpretation is that the learned-vs-K6 difference is primarily explained by **whether each contralateral Gaussian receives shoulder-descendant support and how much total support it receives**. Matching that per-Gaussian branch mass removes at least `83.85%` of the median field MAE gap in every checkpoint, while replacing only within-branch composition changes the median field MAE gap by at most about `2.20%` in absolute value.

This mechanism synthesis remains exploratory/post-hoc and does not rescue the failed predeclared shoulder generalization.

## Exact next action

Before designing a corrective method, run one non-perturbative **arm-chain branch-support topology synthesis** across left wrist, left elbow, and left shoulder using the same frozen learned/K6 weights and contralateral masks.

The goal is to test whether the wrist/elbow/shoulder difference is structurally aligned with how subject-specific K6 support topology expands from the distal wrist branch `[20,22]` to elbow `[18,20,22]` to shoulder `[16,18,20,22]`.

Do not compute new deformations. Report, per checkpoint and joint:

- learned positive-support fraction
- K6 positive-support fraction
- learned-positive/K6-zero fraction
- both-positive fraction
- aggregate learned/K6 branch-support ratio
- support-mass summaries on both-positive rows

This is descriptive/exploratory and must not establish kinematic depth as causal.

## Research-record rule

Preserve the failed shoulder generalization. Exploratory mechanism work after Step 18C0 cannot change predeclared pass/fail outcomes. Do not tune shoulder thresholds or add joints merely to seek a passing result.