# Research Session Checkpoint — 2026-09-17 Step 18R4

## Purpose

Recompute the historical exploratory Step 18C2 shoulder support-mass matching counterfactual on the intended canonical A100 legacy runtime, while preserving the original T4 artifacts and scientific definition.

Analysis class: `EXPLORATORY_POST_HOC`.

Counterfactual definition unchanged from historical C2:

- frozen shoulder branch `[16,18,20,22]`
- preserve learned within-branch composition where defined
- replace total shoulder-descendant branch mass per frozen contralateral Gaussian with K6 branch mass
- proportionally rescale learned non-branch weights to preserve row sum
- undefined learned compositions use the same explicitly counted K6 fallback rule as historical C2
- original learned-vs-K6 displacement gap comes from canonical A100 Step 18R2
- counterfactual deformation recomputed on A100

No confirmatory threshold, joint, mask, perturbation, or pose schedule was changed.

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

## Structural invariants

All three checkpoints had:

- branch fallback rows: `0`
- outside fallback rows: `0`
- pure learned-composition fraction: `1.0`
- counterfactual row-sum max error: `2.384185791015625e-07`
- K6 branch-mass match max error below `7e-10`
- minimum counterfactual weight: `0.0`

Thus this rerun required no composition fallback rows.

## A100 results

### Seattle

```text
MAE gap reduction min/median/max:
68.34228988341695 / 94.49566207250349 / 96.3525229839263 %

historical T4 median:
94.49547062277841 %

A100 - T4 median delta:
+0.00019144972507945113 percentage points

RMSE gap reduction min/median/max:
66.82421377004563 / 94.2611542006636 / 95.8295116835092 %

fraction improved min/median/max:
0.8975266086115142 / 0.9300768021286889 / 0.9433659893565554

CF-vs-K6 corr min/median/max:
0.9932627312304395 / 0.9943957252549069 / 0.999782227288398
```

### Parkinglot

```text
MAE gap reduction min/median/max:
73.57855419879601 / 83.84751353605428 / 87.24532936182469 %

historical T4 median:
83.84695205957038 %

A100 - T4 median delta:
+0.0005614764838952624 percentage points

RMSE gap reduction min/median/max:
92.69185656161443 / 95.60646862961674 / 96.57166402420901 %

fraction improved min/median/max:
0.947476230965448 / 0.9498466929478756 / 0.9529514828270336

CF-vs-K6 corr min/median/max:
0.9892098218898479 / 0.9967494097391262 / 0.9985341347378197
```

### Jogging

```text
MAE gap reduction min/median/max:
71.24251382824997 / 93.51752945582919 / 96.92115170878516 %

historical T4 median:
93.51712996485506 %

A100 - T4 median delta:
+0.0003994909741322772 percentage points

RMSE gap reduction min/median/max:
52.19784154373719 / 88.83915268025706 / 94.90364998906612 %

fraction improved min/median/max:
0.9914300761239048 / 0.9962177430937904 / 0.9971273998180686

CF-vs-K6 corr min/median/max:
0.789517394976109 / 0.9587969077308451 / 0.9946555437734357
```

## Reconciliation

A100 median full-field MAE-gap reductions:

```text
Seattle:    94.49566207250349%
Parkinglot: 83.84751353605428%
Jogging:    93.51752945582919%
```

Historical T4 medians:

```text
Seattle:    94.49547062277841%
Parkinglot: 83.84695205957038%
Jogging:    93.51712996485506%
```

Median differences are less than `0.0006` percentage points in every checkpoint. Therefore the historical C2 exploratory interpretation is preserved under canonical A100 revalidation.

The descriptive flag `all A100 checkpoint medians >80%` is `True`, but this is **not** a preregistered threshold and must not be presented as confirmatory evidence.

## Interpretation

The A100 rerun strongly preserves the historical exploratory result: replacing the learned per-Gaussian total shoulder-descendant branch mass with the corresponding K6 mass, while preserving learned within-branch composition, removes most of the learned-vs-K6 displacement-field gap in all three independently pretrained checkpoints.

This continues to strongly implicate descendant-branch support topology and total per-row support magnitude as a major explanatory mechanism for the shoulder learned-vs-K6 difference.

This does **not** establish why training produced that support topology and does not alter the failed preregistered shoulder generalization.

## Drive artifacts

- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual_displacements.npz`

Historical T4 artifacts remain preserved:

- `experiments/08-second-joint-generalization/18C2_shoulder_support_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18C2_shoulder_support_match_counterfactual_displacements.npz`

## Exact next action

Run Step 18R5: canonical A100 reconciliation of historical Step 18C3 within-branch composition matching.

R5 must preserve learned total shoulder-branch mass and replace only within-branch composition with K6 composition where K6 branch composition is defined, using the same historical fallback/coverage definitions and pose schedule. Compare A100 results against historical T4 C3 without changing confirmatory conclusions.
