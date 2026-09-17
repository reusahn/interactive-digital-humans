# Step 18R5 — A100 Reconciliation of Exploratory Step 18C3

Date: 2026-09-17
Status: `EXPLORATORY_POST_HOC_RECONCILED_ON_A100`

## Purpose

Recompute the historical Step 18C3 within-branch composition counterfactual on the intended canonical A100 legacy runtime while preserving the original scientific definition and historical T4 artifacts.

This analysis is exploratory/post-hoc and does not alter the failed preregistered shoulder generalization.

## Canonical runtime

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

SMPL SHA256:

```text
f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

## Counterfactual definition

Preserve each learned row's total shoulder-descendant branch mass and replace only the within-branch allocation over `[16,18,20,22]` with K6 composition where K6 branch mass is positive.

If learned branch mass is positive but K6 branch mass is exactly zero, K6 within-branch composition is undefined. Those rows retain learned composition rather than inventing a K6 composition.

The original learned/K6 displacement gap is taken from canonical A100 Step 18R2. The composition-matched counterfactual deformation is recomputed on A100.

## Composition-support coverage

Coverage reproduced the historical C3 topology exactly.

```text
Seattle
contralateral rows: 33072
learned-positive branch rows: 33072
composition-defined rows: 7196
K6-composition undefined rows: 25876
defined fraction: 0.21758587324625062

Parkinglot
contralateral rows: 77622
learned-positive branch rows: 77622
composition-defined rows: 20300
K6-composition undefined rows: 57322
defined fraction: 0.2615237948004432

Jogging
contralateral rows: 20887
learned-positive branch rows: 20887
composition-defined rows: 1785
K6-composition undefined rows: 19102
defined fraction: 0.08545985541245751
```

All historical composition-coverage counts reproduced exactly: `True`.

## Counterfactual validation

```text
Seattle
row-sum max error: 2.384185791015625e-07
learned branch-mass preservation max error: 0.0
minimum weight: 0.0

Parkinglot
row-sum max error: 3.5762786865234375e-07
learned branch-mass preservation max error: 3.725290298461914e-09
minimum weight: 0.0

Jogging
row-sum max error: 3.5762786865234375e-07
learned branch-mass preservation max error: 0.0
minimum weight: 0.0
```

## A100 full-field MAE-gap reduction

### Seattle

```text
min/median/max:
-0.1874531024120163 / -0.10397201493190789 / 0.15788682448444336 %

historical T4 median:
-0.10402258952364463 %

A100 - T4 median delta:
+0.000050574591736740615 percentage points
```

Defined-overlap median: `-0.2396526479799821%`.

A100 C2 median: `94.49566207250349%`.

A100 C2 - C3 contrast: `94.5996340874354` percentage points.

### Parkinglot

```text
min/median/max:
-3.2820980213791318 / -2.195179260385338 / -1.9179318571641124 %

historical T4 median:
-2.1951923116722116 %

A100 - T4 median delta:
+0.000013051286873455581 percentage points
```

Defined-overlap median: `-3.1557424055567274%`.

A100 C2 median: `83.84751353605428%`.

A100 C2 - C3 contrast: `86.04269279643962` percentage points.

### Jogging

```text
min/median/max:
0.05404001102309319 / 0.20347135731436095 / 2.1119170563166922 %

historical T4 median:
0.20329469100371367 %

A100 - T4 median delta:
+0.00017666631064727767 percentage points
```

Defined-overlap median: `0.9510110139988537%`.

A100 C2 median: `93.51752945582919%`.

A100 C2 - C3 contrast: `93.31405809851483` percentage points.

## Correlation behavior

A100 composition-matched CF-vs-K6 field correlations remain near zero, reproducing the historical qualitative behavior.

```text
Seattle    min/median/max: -0.0404741883 / -0.0292717133 / 0.0340214830
Parkinglot min/median/max:  0.0177469906 /  0.0191368770 / 0.0225266327
Jogging    min/median/max: -0.0318786269 / -0.0179253463 / 0.0605150208
```

## Reconciliation result

```text
all historical composition-coverage counts reproduced exactly: True
all A100 C3 median signs same as historical T4: True
```

The historical C3 interpretation survives A100 reconciliation: within-branch composition matching has essentially zero or slightly negative median effect, in sharp contrast with the large C2 branch-mass matching effect.

## Scientific interpretation

The reciprocal A100 C2/C3 decomposition supports the same bounded exploratory mechanism statement as the historical T4 analysis:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

For the tested shoulder perturbation, the presence and total magnitude of per-Gaussian descendant-branch support are strongly implicated as the dominant source of the learned-vs-K6 field difference. Redistributing a fixed learned branch mass according to K6 within-branch composition has a small effect on rows where K6 composition is defined.

This is a deformation-mechanism statement, not a training-level causal explanation.

## Guardrails

- exploratory/post-hoc
- independent pretrained checkpoints: `n=3`
- pose diagnostics are nested within checkpoints
- no new threshold introduced
- preregistered shoulder result remains `FAIL`
- K6 composition is undefined on most contralateral rows
- kinematic depth remains unresolved
- no generalization beyond tested HUGS/NeuMan scope

## Drive artifacts

- `experiments/08-second-joint-generalization/18R5_A100_shoulder_composition_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R5_A100_shoulder_composition_match_counterfactual_displacements.npz`

Historical T4 C3 artifacts remain preserved.