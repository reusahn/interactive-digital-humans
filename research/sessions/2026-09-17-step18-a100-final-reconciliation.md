# Step 18 — Final A100 Canonical Reconciliation

Date: 2026-09-17
Status: `FINAL_STEP18_A100_RECONCILIATION_FROZEN`

## Purpose

Reconcile the complete Step-18 shoulder confirmatory and exploratory evidence chain onto the intended canonical A100 legacy runtime while preserving all historical Tesla T4 artifacts and pass/fail outcomes.

No threshold was changed. No failed result was rescued. No new joint perturbation was introduced during the reconciliation.

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

`f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0`

User-supplied project provenance states that the intended runtime through Step 17 was A100. Historical Step-17 archives themselves establish CUDA use but do not independently identify the GPU model. Historical T4 Step-18 artifacts remain preserved as provenance/sensitivity artifacts.

## Confirmatory shoulder result — A100 R2

Frozen protocol remained:

- joint: SMPL 16 left shoulder
- local `z +10 deg`
- descendant branch `[16,18,20,22]`
- Seattle frames `[2,7,12,17]`
- Parkinglot frames `[2,7,12,17]`
- Jogging frames `[2,7,12,17,22,27,32,37,42,47]`
- K6 reduction threshold `>=95%`
- selective ablation reduction `>=99.999%`
- correlation `>=0.90`
- max/summed ablated contralateral response `<=1e-8`

A100 result:

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
correlation passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction min/median/max:
-77.67225758078598 / 42.390431156682965 / 76.3901059303657 %
correlation min/median/max:
0.7985822327394099 / 0.9436557686954412 / 0.9812400880684837
```

Every one of the 18 A100 pose diagnostics retained the same threshold-level classification as the corresponding historical T4 pose.

Therefore:

`SHOULDER_PREDECLARED_GENERALIZATION = FAIL_UNCHANGED`

The historical T4 shoulder failure is not a hardware-specific scientific artifact.

## C1 support-mass reconciliation — A100 R3

Aggregate learned/K6 shoulder branch-support ratios are unchanged because weights/masks are unchanged:

```text
Seattle:    1.5764279015288012
Parkinglot: 0.8379048191221863
Jogging:    5.5557058081619255
```

Checkpoint support direction matches majority learned-vs-K6 displacement direction in `3/3` checkpoints on A100, exactly as on T4.

All per-pose displacement/support-match directions also remain unchanged A100 vs T4.

## C2 total branch-mass matching — A100 R4

Counterfactual: preserve learned within-branch composition, replace total shoulder-descendant branch mass per contralateral Gaussian with K6 mass, and proportionally rescale learned nonbranch mass.

All checkpoints had zero fallback rows and pure learned-composition fraction `1.0`.

Canonical A100 median full-field MAE-gap reductions:

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

A100 minus T4 median differences are only about `0.00019`, `0.00056`, and `0.00040` percentage points respectively.

## C3 within-branch composition matching — A100 R5

Counterfactual: preserve learned total shoulder-branch mass, replace only allocation over `[16,18,20,22]` with K6 composition where K6 branch mass is positive.

Composition-defined coverage reproduced historical topology exactly:

```text
Seattle:    7196 / 33072 = 0.21758587324625062
Parkinglot: 20300 / 77622 = 0.2615237948004432
Jogging:    1785 / 20887 = 0.08545985541245751
```

Canonical A100 median full-field MAE-gap reductions:

```text
Seattle:    -0.10397201493190789%
Parkinglot: -2.195179260385338%
Jogging:     0.20347135731436095%
```

Historical T4 medians:

```text
Seattle:    -0.10402258952364463%
Parkinglot: -2.1951923116722116%
Jogging:     0.20329469100371367%
```

A100 C2 minus C3 median contrasts:

```text
Seattle:    94.5996340874354 percentage points
Parkinglot: 86.04269279643962 percentage points
Jogging:    93.31405809851483 percentage points
```

A100 composition-matched CF-vs-K6 correlations remain near zero, reproducing historical qualitative behavior.

## Reconciled C4 mechanism synthesis

Confirmatory shoulder status:

`FAIL_UNCHANGED`

Branch-mediated causality:

`SUPPORTED_IN_FROZEN_TEST`

Support topology and magnitude:

`DOMINANT_EXPLORATORY_FACTOR`

Within-branch composition:

`SMALL_EFFECT_ON_DEFINED_OVERLAP`

Pose geometry:

`RESIDUAL_MODULATOR_PLAUSIBLE`

Kinematic depth:

`HYPOTHESIS_ONLY`

The A100 reconciliation therefore leaves the historical C4 evidence classes unchanged. Only canonical numeric anchors are updated to R2/R4/R5 A100 values.

## D0 structural topology

D0 is based on frozen weight topology and does not depend on the deformation GPU runtime. It remains valid without numerical recomputation.

K6 positive descendant-support fractions:

```text
Seattle:    wrist 0.004626269956458636 | elbow 0.006259071117561683 | shoulder 0.21758587324625062
Parkinglot: wrist 0.0022287495813042694 | elbow 0.0022287495813042694 | shoulder 0.2615237948004432
Jogging:    wrist 0.0019629434576530855 | elbow 0.0019629434576530855 | shoulder 0.08545985541245751
```

Learned support remains positive on 100% of frozen contralateral rows for every tested joint/checkpoint cell.

## Final three-joint synthesis

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Final bounded claims remain:

1. `SUPPORTED_FOR_ALL_THREE_TESTED_JOINTS`
   - For the tested left-arm perturbations, contralateral deformation is mediated through weights assigned to the changed descendant branch.

2. `JOINT_DEPENDENT_NOT_UNIVERSAL`
   - Strong learned-HUGS versus subject-specific SMPL-K6 amplification is robust for tested wrist and elbow perturbations but does not generalize unchanged to the tested shoulder perturbation.

3. `CONSISTENT_ACROSS_ALL_THREE_CHECKPOINTS`
   - K6 descendant-branch support is nearly absent on contralateral rows for tested wrist/elbow branches and expands sharply at shoulder.

4. `STRONGLY_IMPLICATED`
   - For the tested shoulder perturbation, per-Gaussian descendant-branch support existence/topology and total magnitude explain most of the learned-vs-K6 displacement-field difference under the support-matching counterfactual.

5. `SMALL_EFFECT_ON_DEFINED_OVERLAP`
   - Redistributing a fixed learned shoulder-branch mass according to K6 within-branch composition produces little improvement toward the K6 displacement field where K6 composition is defined.

6. `NOT_ESTABLISHED_AS_CAUSAL`
   - Kinematic depth remains unresolved because depth is confounded with nested branch-support topology.

## Final mechanism statement

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

This remains the strongest bounded deformation-mechanism description after canonical A100 reconciliation.

It is not a statement about why HUGS training learns the nonlocal support structure.

## Scope / statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- one tested left-arm chain
- pose/frame diagnostics are nested within checkpoints
- wrist/elbow/shoulder are repeated diagnostics within the same checkpoints
- current evidence is HUGS / NeuMan only

## Step 18 closure

Step 18 is now closed again under canonical A100 reconciliation.

No further Step-18 deformation rerun is required unless a new provenance issue is discovered.

Step 19 may proceed only through a separately frozen preregistration/evaluation protocol before corrective-method implementation.