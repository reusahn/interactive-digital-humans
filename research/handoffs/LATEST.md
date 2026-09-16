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

Field MAE-gap reduction after per-row branch-mass matching:

```text
Seattle    min/median/max: 68.341709 / 94.495471 / 96.352339%
Parkinglot min/median/max: 73.579259 / 83.846952 / 87.244704%
Jogging    min/median/max: 71.242567 / 93.517130 / 96.921237%
```

Counterfactual-vs-K6 field correlations:

```text
Seattle    min/median/max: 0.993263 / 0.994395 / 0.999783
Parkinglot min/median/max: 0.989209 / 0.996750 / 0.998534
Jogging    min/median/max: 0.789515 / 0.958796 / 0.994655
```

Interpretation: per-row branch-support magnitude/topology is a dominant exploratory explanatory factor. C2 cannot change the failed confirmatory shoulder outcome.

Archived: `research/sessions/2026-09-16-step18c2.md`.

## Step 18C3 exploratory within-branch composition counterfactual COMPLETE

Counterfactual:

- preserve learned total branch mass on `[16,18,20,22]`
- replace only the within-branch allocation with K6 composition where K6 branch mass is positive
- leave the failed shoulder protocol unchanged

A key structural observation is that K6 shoulder-branch composition is undefined on most contralateral rows because K6 branch mass is exactly zero there, while learned branch mass is positive on every tested contralateral row.

```text
Seattle
composition-defined fraction: 0.217586
K6-zero shoulder-branch rows: 25876 / 33072 = about 78.24%

Parkinglot
composition-defined fraction: 0.261524
K6-zero shoulder-branch rows: 57322 / 77622 = about 73.85%

Jogging
composition-defined fraction: 0.085460
K6-zero shoulder-branch rows: 19102 / 20887 = about 91.45%
```

Full-field MAE-gap reduction from composition matching is essentially zero or negative:

```text
Seattle    min/median/max: -0.187106 / -0.104023 / 0.157623%
Parkinglot min/median/max: -3.281558 / -2.195192 / -1.918001%
Jogging    min/median/max:  0.054189 /  0.203295 / 2.111938%
```

Even on the rows where both learned and K6 branch composition are defined, composition matching produces little improvement:

```text
Seattle    defined-row median MAE-gap reduction: -0.239794%
Parkinglot defined-row median MAE-gap reduction: -3.155762%
Jogging    defined-row median MAE-gap reduction:  0.951096%
```

C2 vs C3 median full-field MAE-gap reduction:

```text
Seattle    mass match 94.495471% vs composition match -0.104023%
Parkinglot mass match 83.846952% vs composition match -2.195192%
Jogging    mass match 93.517130% vs composition match  0.203295%
```

Composition-matched counterfactual-vs-K6 field correlations remain near zero, unlike C2.

### Current exploratory mechanism interpretation

For the tested shoulder perturbation, the learned-vs-K6 cross-body difference is driven primarily by the **presence and magnitude of per-Gaussian shoulder-descendant support**, not by reallocating a fixed amount of shoulder-branch mass among joints 16/18/20/22.

This should be described as support **topology plus per-row magnitude**, not merely aggregate branch mass. K6 has zero shoulder-descendant support on most contralateral rows, whereas learned HUGS assigns positive support to all of them.

Residual pose dependence remains. Kinematic depth is still only a hypothesis.

Archived:

- `research/sessions/2026-09-16-step18c3.md`
- Drive `experiments/08-second-joint-generalization/18C3_shoulder_composition_match_counterfactual.json`
- Drive `experiments/08-second-joint-generalization/18C3_shoulder_composition_match_counterfactual_displacements.npz`

## Exact next action

Freeze **Step 18C4 shoulder mechanism synthesis** before any new perturbation or corrective-method design.

The synthesis should explicitly separate four levels:

1. support existence/topology
2. per-row total branch mass
3. within-branch joint composition
4. residual pose-geometry dependence

No new deformation computation is needed for C4. It should read the completed C1/C2/C3 artifacts, preserve the exploratory label, and freeze bounded mechanism claims without modifying the failed shoulder criterion.

## Research-record rule

Preserve the negative shoulder generalization result. Exploratory mechanism decomposition after Step 18C0 cannot change the predeclared pass/fail outcome. Do not tune shoulder thresholds or add joints merely to seek a passing result.