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

## Step 18B1H shoulder frame-2 result

All checkpoints had the correct changed branch `[16,18,20,22]`.

| Checkpoint | Learned contra | K6 contra | K6 reduction | Ablation reduction | Corr | Overall |
|---|---:|---:|---:|---:|---:|---|
| Seattle | `3.5090098206` | `2.1443378665` | `38.8905%` | `100%` | `0.961674` | FAIL |
| Parkinglot | `9.6190783830` | `14.3472676853` | `-49.1543%` | `100%` | `0.976920` | FAIL |
| Jogging | `1.1837988005` | `0.4761869365` | `59.7747%` | `100%` | `0.894603` | FAIL |

`ALL THREE FRAME-2 SHOULDER CELLS PASS: False`

## Step 18B2 full-pose shoulder characterization

Frame-2 values reproduced Step 18B1H exactly.

Seattle:

```text
poses: 4
K6 passes: 0/4
selective-ablation passes: 4/4
corr passes: 4/4
overall passes: 0/4
negative K6 reductions: 1
K6 reduction min/median/max: -32.350004 / 29.517251 / 38.890514
```

Parkinglot:

```text
poses: 4
K6 passes: 0/4
selective-ablation passes: 4/4
corr passes: 4/4
overall passes: 0/4
negative K6 reductions: 4
K6 reduction min/median/max: -77.671145 / -52.505983 / -44.710301
```

Jogging:

```text
poses: 10
K6 passes: 0/10
selective-ablation passes: 10/10
corr passes: 6/10
overall passes: 0/10
negative K6 reductions: 0
K6 reduction min/median/max: 42.273609 / 71.459102 / 76.389818
```

Global:

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

### Claim 1: branch-mediated contralateral causality

`SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`

For the tested perturbations, contralateral response is causally mediated through weights assigned to the changed kinematic descendant branch.

### Claim 2: learned-vs-K6 amplification

`JOINT_DEPENDENT_NOT_UNIVERSAL`

The strong learned-HUGS-versus-SMPL-K6 amplification found for wrist and elbow does not generalize unchanged to the proximal shoulder.

### Claim 3: kinematic depth

`HYPOTHESIS_ONLY`

A distal-to-proximal dependence is consistent with the observed pattern, but kinematic depth has not been established as the causal explanation.

## Exact next action

Before introducing another perturbation or a corrective method, run one **exploratory/post-hoc shoulder mechanism decomposition using existing frozen artifacts only**.

Question: can the shoulder learned-vs-K6 reversal/attenuation be substantially explained by the amount and spatial distribution of shoulder-descendant branch support already present in learned versus K6 weights?

Use only:

- frozen learned/K6 weights
- frozen contralateral masks
- completed Step 18B2 shoulder displacement fields

No new perturbation, threshold change, or confirmatory claim. Compare branch-support differences against learned-minus-K6 displacement differences per Gaussian and per pose. Treat checkpoint-level `n=3` correctly.

## Research-record rule

Preserve negative generalization results. Do not add joints merely to seek a passing result, do not tune shoulder thresholds, and label all mechanism decomposition after Step 18C0 as exploratory unless separately preregistered.