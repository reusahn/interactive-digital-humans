# Research Claim Ledger

Last updated: 2026-09-17

This file records the current scientific status of major claims. It is intentionally conservative.

| ID | Claim | Evidence class | Status | Scope / notes |
|---|---|---|---|---|
| CL-01 | Contralateral deformation can occur under local left-arm joint perturbation in learned HUGS deformation. | Confirmatory observation | SUPPORTED | Current evidence is HUGS / NeuMan checkpoints only. |
| CL-02 | Contralateral deformation is mediated through learned support assigned to the changed descendant branch. | Confirmatory intervention + replication | SUPPORTED_FOR_ALL_THREE_TESTED_JOINTS | Wrist, elbow, shoulder. Selective branch ablation removes the response in frozen tests. |
| CL-03 | Learned HUGS shows strong learned-vs-K6 contralateral amplification for the tested wrist perturbation. | Confirmatory | SUPPORTED | 3/3 checkpoints, nested poses. |
| CL-04 | Wrist amplification generalizes to the tested elbow perturbation. | Confirmatory generalization | SUPPORTED | 3/3 checkpoints. |
| CL-05 | Wrist/elbow learned-vs-K6 amplification generalizes unchanged to shoulder. | Confirmatory generalization | FAILED | Predeclared shoulder protocol, 0/18 K6-threshold passes on canonical A100; every pose retained the same threshold classification as historical T4. Failure must remain preserved. |
| CL-06 | Learned-vs-K6 amplification is joint-dependent rather than universal across the tested arm chain. | Frozen synthesis | SUPPORTED | Wrist/elbow supported, shoulder failed. |
| CL-07 | Per-Gaussian descendant-branch support topology and total magnitude explain most of the shoulder learned-vs-K6 field difference. | Exploratory counterfactual | STRONGLY_IMPLICATED | Canonical A100 C2/R4 median full-field MAE-gap reduction 83.85% to 94.50% across checkpoints. Not a training-level causal claim. |
| CL-08 | Within-branch joint composition is the dominant explanation for shoulder learned-vs-K6 field difference. | Exploratory counterfactual | NOT_SUPPORTED | Canonical A100 C3/R5 composition-only matching has near-zero or negative median improvement; composition is defined on only ~8.5% to 26.2% of contralateral rows depending on checkpoint. |
| CL-09 | K6 contralateral descendant-branch support is nearly absent for wrist/elbow and expands sharply at shoulder. | Exploratory descriptive | CONSISTENT_ACROSS_ALL_THREE_CHECKPOINTS | Structural alignment with deformation behavior. D0 uses frozen weight topology. |
| CL-10 | Kinematic depth itself causes the distal-to-proximal pattern. | Unresolved hypothesis | NOT_ESTABLISHED_AS_CAUSAL | Confounded with nested branch-support topology. |
| CL-11 | Photometric reconstruction loss causes anatomical nonlocality. | Unresolved training-origin hypothesis | UNTESTED | Do not present as result. |
| CL-12 | Learned digital-human models generally suffer from anatomical locality failure. | Cross-method generalization | UNTESTED | Current evidence is HUGS only. |
| CL-13 | Anatomical locality can be enforced without sacrificing reconstruction quality. | Future method hypothesis | UNTESTED | Step 19. Protocol must be frozen before implementation. |

## Canonical numeric anchors

Canonical deformation-dependent Step-18 reconciliation runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

Wrist global minimum K6 reduction: `99.708575087815%`

Elbow global minimum K6 reduction: `99.81874059431833%`

Shoulder canonical A100 R2:

- K6 reduction min/median/max: `-77.67225758078598 / 42.390431156682965 / 76.3901059303657%`
- K6 pass count: `0/18`
- selective-ablation pass count: `18/18`
- correlation pass count: `14/18`
- overall pass count: `0/18`
- negative K6 reductions: `5`

Shoulder canonical A100 C2/R4 mass-match median MAE-gap reductions:

- Seattle `94.49566207250349%`
- Parkinglot `83.84751353605428%`
- Jogging `93.51752945582919%`

Shoulder canonical A100 C3/R5 composition-match median MAE-gap reductions:

- Seattle `-0.10397201493190789%`
- Parkinglot `-2.195179260385338%`
- Jogging `0.20347135731436095%`

Canonical A100 C2 minus C3 median contrasts:

- Seattle `94.5996340874354` percentage points
- Parkinglot `86.04269279643962` percentage points
- Jogging `93.31405809851483` percentage points

K6 shoulder composition-defined coverage:

- Seattle `7196 / 33072 = 0.21758587324625062`
- Parkinglot `20300 / 77622 = 0.2615237948004432`
- Jogging `1785 / 20887 = 0.08545985541245751`

## Historical T4 provenance

Historical Step-18 B1H/B2/C1/C2/C3/C4/D1 artifacts produced on Tesla T4 remain preserved. The canonical A100 R1-R5 reconciliation retained the same threshold-level confirmatory result and the same bounded exploratory mechanism interpretation. Historical numbers must not be deleted or silently overwritten.

## Writing rule

Before introducing or strengthening a paper claim, locate it in this ledger. If it is not listed, treat it as unreviewed until its evidence class, scope, and status are explicitly assigned.