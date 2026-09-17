# Research Claim Ledger

Last updated: 2026-09-17

This file records the current scientific status of major claims. It is intentionally conservative.

| ID | Claim | Evidence class | Status | Scope / notes |
|---|---|---|---|---|
| CL-01 | Contralateral deformation can occur under local left-arm joint perturbation in learned HUGS deformation. | Confirmatory observation | SUPPORTED | Current evidence is HUGS / NeuMan checkpoints only. |
| CL-02 | Contralateral deformation is mediated through learned support assigned to the changed descendant branch. | Confirmatory intervention + replication | SUPPORTED_FOR_ALL_THREE_TESTED_JOINTS | Wrist, elbow, shoulder. Selective branch ablation removes the response in frozen tests. |
| CL-03 | Learned HUGS shows strong learned-vs-K6 contralateral amplification for the tested wrist perturbation. | Confirmatory | SUPPORTED | 3/3 checkpoints, nested poses. |
| CL-04 | Wrist amplification generalizes to the tested elbow perturbation. | Confirmatory generalization | SUPPORTED | 3/3 checkpoints. |
| CL-05 | Wrist/elbow learned-vs-K6 amplification generalizes unchanged to shoulder. | Confirmatory generalization | FAILED | Predeclared shoulder protocol, 0/18 K6-threshold passes. Failure must remain preserved. |
| CL-06 | Learned-vs-K6 amplification is joint-dependent rather than universal across the tested arm chain. | Frozen synthesis | SUPPORTED | Wrist/elbow supported, shoulder failed. |
| CL-07 | Per-Gaussian descendant-branch support topology and total magnitude explain most of the shoulder learned-vs-K6 field difference. | Exploratory counterfactual | STRONGLY_IMPLICATED | C2 median full-field MAE-gap reduction 83.85% to 94.50% across checkpoints. Not a training-level causal claim. |
| CL-08 | Within-branch joint composition is the dominant explanation for shoulder learned-vs-K6 field difference. | Exploratory counterfactual | NOT_SUPPORTED | C3 composition-only matching has near-zero or negative median improvement. |
| CL-09 | K6 contralateral descendant-branch support is nearly absent for wrist/elbow and expands sharply at shoulder. | Exploratory descriptive | CONSISTENT_ACROSS_ALL_THREE_CHECKPOINTS | Structural alignment with deformation behavior. |
| CL-10 | Kinematic depth itself causes the distal-to-proximal pattern. | Unresolved hypothesis | NOT_ESTABLISHED_AS_CAUSAL | Confounded with nested branch-support topology. |
| CL-11 | Photometric reconstruction loss causes anatomical nonlocality. | Unresolved training-origin hypothesis | UNTESTED | Do not present as result. |
| CL-12 | Learned digital-human models generally suffer from anatomical locality failure. | Cross-method generalization | UNTESTED | Current evidence is HUGS only. |
| CL-13 | Anatomical locality can be enforced without sacrificing reconstruction quality. | Future method hypothesis | UNTESTED | Step 19. Protocol must be frozen before implementation. |

## Frozen numeric anchors

Wrist global minimum K6 reduction: `99.708575087815%`

Elbow global minimum K6 reduction: `99.81874059431833%`

Shoulder K6 reduction range: `-77.671145% to 76.389818%`

Shoulder K6 pass count: `0/18`

Shoulder C2 mass-match median MAE-gap reductions:

- Seattle `94.49547062277841%`
- Parkinglot `83.84695205957038%`
- Jogging `93.51712996485506%`

Shoulder C3 composition-match median MAE-gap reductions:

- Seattle `-0.10402258952364463%`
- Parkinglot `-2.1951923116722116%`
- Jogging `0.20329469100371367%`

## Writing rule

Before introducing or strengthening a paper claim, locate it in this ledger. If it is not listed, treat it as unreviewed until its evidence class, scope, and status are explicitly assigned.
