# Latest Research Handoff

Current continuation date: **2026-09-16**.

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints
- wrist, elbow, shoulder are repeated joint diagnostics within the same checkpoints

## Frozen distal benchmark

Left wrist Step 16E0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.708575087815%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9808287038512752
```

Predeclared left elbow Step 17C0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.81874059431833%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9688984153761956
```

Combined wrist + elbow: `6/6` joint x checkpoint cells pass across `36` nested pose diagnostics.

Historical elbow exact-number reproduction under reconstructed runtimes is `5/6` within the old `1e-5` aggregate gate on modern A100, legacy-stack A100, and legacy-stack T4. Field correlations remain effectively `1.0`; the historical gate was not widened.

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

## Frozen shoulder protocol and negative result

Protocol: `research/protocols/2026-09-16-third-joint-generalization.md`

```text
joint: left shoulder, SMPL 16
perturbation: local z +10°
descendant branch: [16,18,20,22]
contralateral subset: {14,17,19,21,23}
K6 reduction threshold: >=95%
selective-ablation threshold: >=99.999%
correlation threshold: >=0.90
```

Step 18B2 full schedule:

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
corr passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction range: -77.671145% to 76.389818%
```

The predeclared shoulder universal generalization is **FAIL** and remains unchanged.

## Step 18C0 three-joint synthesis FROZEN

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification | Global min K6 reduction |
|---|---|---|---|---:|
| wrist | PASS | supported | supported | `99.708575%` |
| elbow | PASS | supported | supported | `99.818741%` |
| shoulder | FAIL | supported | not supported | `-77.671145%` |

Frozen claims:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

Drive: `experiments/08-second-joint-generalization/18C0_three_joint_synthesis.json`

## Step 18C1-C4 exploratory shoulder mechanism decomposition

C1: aggregate shoulder branch-support direction matches majority displacement direction in `3/3` checkpoints. Per-Gaussian delta-support/delta-displacement correlation is high overall.

C2: match each learned contralateral row's total shoulder-descendant branch mass to K6 while preserving learned within-branch composition.

Median full-field MAE-gap reduction:

```text
Seattle:    94.495471%
Parkinglot: 83.846952%
Jogging:    93.517130%
```

C3: preserve learned total branch mass and replace only within-branch allocation with K6 composition where defined.

Median full-field MAE-gap reduction:

```text
Seattle:    -0.104023%
Parkinglot: -2.195192%
Jogging:     0.203295%
```

K6 shoulder-branch mass is zero on most contralateral rows:

```text
Seattle:    78.24%
Parkinglot: 73.85%
Jogging:    91.45%
```

Step 18C4 therefore freezes the exploratory shoulder mechanism as:

- support topology + per-row magnitude: `DOMINANT_EXPLORATORY_FACTOR`
- within-branch composition: `SMALL_EFFECT_ON_DEFINED_OVERLAP`
- pose geometry: `RESIDUAL_MODULATOR_PLAUSIBLE`
- kinematic depth: `HYPOTHESIS_ONLY`

Archived through `research/sessions/2026-09-16-step18c4.md`.

## Step 18D0 arm-chain branch-support topology COMPLETE

No new perturbation or deformation was computed. Existing learned/K6 weights and frozen contralateral masks were compared for nested descendant branches:

```text
wrist    [20,22]
elbow    [18,20,22]
shoulder [16,18,20,22]
```

Learned support is positive on `100%` of frozen contralateral rows for every tested joint/checkpoint.

K6 positive-support fractions:

```text
Seattle:    wrist 0.0046263 | elbow 0.0062591 | shoulder 0.2175859
Parkinglot: wrist 0.0022287 | elbow 0.0022287 | shoulder 0.2615238
Jogging:    wrist 0.0019629 | elbow 0.0019629 | shoulder 0.0854599
```

Learned-positive/K6-zero topology-gap fractions:

```text
Seattle:    wrist 0.9953737 | elbow 0.9937409 | shoulder 0.7824141
Parkinglot: wrist 0.9977713 | elbow 0.9977713 | shoulder 0.7384762
Jogging:    wrist 0.9980371 | elbow 0.9980371 | shoulder 0.9145401
```

Aggregate learned/K6 branch-support ratios:

```text
Seattle:    wrist 650.22 | elbow 708.93  | shoulder 1.5764
Parkinglot: wrist 404.35 | elbow 1108.68 | shoulder 0.8379
Jogging:    wrist 725.56 | elbow 1355.29 | shoulder 5.5557
```

All `3/3` checkpoints satisfy:

- K6 support sets are nested along wrist -> elbow -> shoulder
- K6 positive-support fraction is nondecreasing distally to proximally
- learned-positive/K6-zero topology mismatch is nonincreasing

The structural transition is concentrated at the shoulder: K6 support exists on only about `0.20%-0.63%` of frozen contralateral rows for wrist/elbow but expands to about `8.55%-26.15%` at shoulder.

### Bounded interpretation

This topology transition is strongly aligned with the deformation results. Distal K6 support is nearly absent where K6 replacement suppresses learned contralateral response by roughly `99.7%+`; proximal shoulder K6 support becomes much more available where that suppression disappears or reverses.

Together with C2, the best bounded mechanism description is **branch-support topology plus per-row support magnitude**. Do not replace this with a claim that kinematic depth itself has been proven causal. Branch nesting and LBS support mechanically participate in the response.

Artifacts:

- `research/sessions/2026-09-16-step18d0.md`
- Drive `experiments/08-second-joint-generalization/18D0_arm_chain_support_topology.json`
- Drive `experiments/08-second-joint-generalization/18D0_arm_chain_support_topology.csv`

## Exact next action

Run **Step 18D1 — arm-chain mechanism synthesis freeze** using only C0, C4, and D0 artifacts. No new perturbation or deformation.

D1 should freeze the final bounded evidence chain before method design:

1. branch-mediated causality is supported across wrist/elbow/shoulder
2. learned-vs-K6 amplification is distal-joint specific in the tested arm chain
3. K6 contralateral branch-support topology is almost absent distally and expands sharply at shoulder
4. shoulder counterfactual evidence identifies per-row support topology/magnitude as the dominant exploratory explanation
5. within-branch composition has a small effect on defined overlap rows
6. kinematic depth remains hypothesis-only

After D1, corrective-method design may begin under a separately frozen protocol.

## Research-record rule

Preserve the failed shoulder generalization. C1-D1 are exploratory synthesis and cannot alter predeclared pass/fail outcomes. Do not add joints merely to seek a passing result or retune thresholds after inspection.
