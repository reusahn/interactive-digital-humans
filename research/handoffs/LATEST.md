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

Continuation runtime:

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

## Step 18B2 full-pose shoulder characterization

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

Parkinglot has K6 > learned shoulder displacement in all four tested poses. Seattle is mixed. Jogging has learned > K6 in all ten poses but well below the frozen `95%` K6-reduction criterion.

Archived: `research/sessions/2026-09-16-step18b2.md`.

## Step 18C0 three-joint synthesis FROZEN

Drive artifact:

`experiments/08-second-joint-generalization/18C0_three_joint_synthesis.json`

Archived session:

`research/sessions/2026-09-16-step18c0.md`

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

## Step 18C1 exploratory shoulder support-mass decomposition COMPLETE

Status: exploratory/post-hoc. No new perturbation, threshold change, or confirmatory rescue.

Shoulder-descendant branch: `[16,18,20,22]`.

### Seattle

```text
learned branch-support sum: 14.713887457148648
K6 branch-support sum: 9.33368880548187
learned/K6 support ratio: 1.5764279015288012
support favors: learned
majority displacement favors: learned
support-direction matches: 3/4
per-Gaussian delta-support/delta-displacement corr range: 0.936228 to 0.967286
```

Seattle frame 7 is the one aggregate direction reversal: support favors learned but displacement favors K6.

### Parkinglot

```text
learned branch-support sum: 25.7759453917906
K6 branch-support sum: 30.762378737473114
learned/K6 support ratio: 0.8379048191221863
support favors: K6
majority displacement favors: K6
support-direction matches: 4/4
corr range: 0.949761 to 0.981640
```

This directly aligns the Parkinglot shoulder reversal with greater K6 shoulder-branch support.

### Jogging

```text
learned branch-support sum: 14.840888978197778
K6 branch-support sum: 2.671287769844639
learned/K6 support ratio: 5.5557058081619255
support favors: learned
majority displacement favors: learned
support-direction matches: 10/10
corr range: 0.802175 to 0.974340
```

Checkpoint-level support direction matches majority displacement direction in `3/3` independently pretrained checkpoints.

### C1 interpretation

Branch-support amount and spatial distribution are a major explanatory factor for the shoulder learned-vs-K6 behavior. The per-Gaussian association is strong and the checkpoint-level direction agrees in all three checkpoints.

However, support mass is not the whole explanation:

- Seattle frame 7 reverses the aggregate support direction despite high per-Gaussian correlation.
- displacement ratios vary by pose while branch weights are pose-independent.
- Jogging support ratio is about `5.56`, while learned/K6 displacement ratios vary only about `1.73` to `4.24`.

Therefore pose geometry and/or within-branch joint composition still modulate the conversion from branch support to displacement. Kinematic depth remains unproven.

Archived:

- `research/sessions/2026-09-16-step18c1.md`
- Drive `experiments/08-second-joint-generalization/18C1_shoulder_support_mass_exploratory.json`
- Drive `experiments/08-second-joint-generalization/18C1_shoulder_support_mass_exploratory.csv`

## Exact next action

Run **Step 18C2**, an exploratory support-matching counterfactual under the same frozen shoulder perturbation.

Counterfactual definition:

- use only frozen contralateral rows
- set each learned row's total shoulder-descendant branch mass to the corresponding K6 branch mass
- preserve learned within-branch proportions wherever they are defined
- proportionally rescale learned non-branch weights to preserve row sum
- explicitly count any rows where learned branch/non-branch composition is undefined and use K6 composition only as a reported fallback there
- do not alter the shoulder joint, perturbation, masks, pose schedules, or confirmatory criteria

Measure how much this support-mass match reduces the original learned-vs-K6 displacement-field MAE/RMSE gap across the already frozen 18 shoulder poses. This separates branch-support magnitude from residual within-branch composition / pose-geometry effects.

Pinned script:

`research/scripts/step18c2_shoulder_support_match_counterfactual.py`

Pinned script commit:

`a7d9e93b75a7a96ec9a3f16919458491bc306db0`

## Research-record rule

Preserve negative generalization results. Step 18C1/C2 are exploratory and cannot rescue the failed predeclared shoulder claim. Do not add joints merely to seek a passing result and do not tune shoulder thresholds.