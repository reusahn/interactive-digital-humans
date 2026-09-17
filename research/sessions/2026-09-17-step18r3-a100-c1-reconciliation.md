# Research Session Checkpoint — 2026-09-17 Step 18R3

## Purpose

Recompute the historical exploratory Step 18C1 shoulder support-mass analysis using the canonical A100 Step 18R2 displacement fields, while preserving the historical T4 artifacts and all scientific definitions.

This analysis is exploratory/post-hoc. It does not alter the preregistered shoulder failure.

Canonical runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

Inputs:

- frozen learned LBS weights
- frozen K6 weights
- frozen Step 17A2 contralateral masks
- A100 Step 18R2 displacement fields
- historical T4 Step 18B2 displacement fields for same-code reconciliation
- shoulder-descendant branch `[16,18,20,22]`

## A100 results

### Seattle

```text
learned branch-support sum: 14.713887457148648
K6 branch-support sum: 9.33368880548187
learned/K6 support ratio: 1.5764279015288012
aggregate support favors: learned
majority displacement favors: learned
support-direction matches: 3/4
corr min/median/max:
0.9362278422766451 / 0.9664406965256402 / 0.9672864525651061
```

### Parkinglot

```text
learned branch-support sum: 25.7759453917906
K6 branch-support sum: 30.762378737473114
learned/K6 support ratio: 0.8379048191221863
aggregate support favors: K6
majority displacement favors: K6
support-direction matches: 4/4
corr min/median/max:
0.9497614357282316 / 0.9738199257592272 / 0.9816398111085524
```

### Jogging

```text
learned branch-support sum: 14.840888978197778
K6 branch-support sum: 2.671287769844639
learned/K6 support ratio: 5.5557058081619255
aggregate support favors: learned
majority displacement favors: learned
support-direction matches: 10/10
corr min/median/max:
0.802178029451637 / 0.9193445080163702 / 0.9743405354392872
```

## A100 versus historical T4 reconciliation

Support sums and support ratios are identical because the weight fields and masks are unchanged.

The A100 displacement-derived quantities differ only at small floating-point scale. The qualitative and directional outcomes are unchanged:

```text
A100 checkpoint support-majority direction matches: 3/3
T4 recomputed checkpoint support-majority direction matches: 3/3
checkpoint-level C1 conclusion same: True
all checkpoint directions same A100 vs T4: True
all per-pose displacement/support-match directions same A100 vs T4: True
```

Thus the historical C1 exploratory interpretation survives canonical A100 reconciliation unchanged at the conclusion level.

## Interpretation

The checkpoint-level direction of shoulder descendant-branch support still matches the majority learned-vs-K6 displacement direction in all three independently pretrained checkpoints. Seattle remains the only sequence with a single per-pose direction mismatch at frame 7; Parkinglot remains especially informative because K6 has more shoulder-branch support and produces greater displacement at all four frozen poses.

This remains exploratory evidence. It does not establish a training-level cause and does not rescue or modify the confirmatory shoulder generalization failure.

## Drive artifacts

- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.json`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.csv`

Historical C1 artifacts remain preserved.

## Exact next action

Run Step 18R4: the A100 canonical rerun of the historical Step 18C2 total shoulder-descendant branch-mass matching counterfactual, preserving learned within-branch composition while replacing each contralateral Gaussian's total branch mass with its K6 branch mass. Use new A100-specific artifacts and compare the resulting MAE-gap-reduction summaries against historical T4 C2.
