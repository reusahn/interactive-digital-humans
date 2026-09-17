# Master Research Context

Last updated: 2026-09-17

This file is the durable source of truth for continuing the Interactive Digital Humans research across new ChatGPT conversations.

## Research identity

The broader research program is **Interactive Digital Humans / Real-Time 4D Human Intelligence**.

The long-term goal is not Gaussian Splatting itself. Gaussian representations are currently useful because animatable Gaussian humans expose learned deformation structure in a form that can be experimentally diagnosed.

Long-term research identity:

> I study how learned digital-human representations maintain structural coherence and controllability under motion, how failures of those properties can be diagnosed, and how structural priors can be incorporated into real-time 4D human models.

Broad PhD-level question:

> What structural priors must learned human representations preserve to remain coherent, controllable, and interactive under novel motion?

Longer-term structural properties include anatomical locality, correspondence, topology, identity preservation, temporal consistency, physical plausibility, and controllability.

## Paper 1 scope

Current Paper 1 is a diagnosis and mechanism-characterization paper, not yet a corrective-method paper.

Primary research question:

> How do learned animatable-human deformation models violate anatomical locality, and which learned skinning structures causally mediate that failure?

Alternative wording:

> When and how does anatomical locality fail in learned animatable-human deformation, and what learned skinning structure mediates anatomically nonlocal motion?

Important scope boundary: Paper 1 does **not** yet explain why training learns the nonlocal support topology. Training-level causes remain unresolved hypotheses.

The paper currently addresses:

- where locality failure appears
- how nonlocal motion is transmitted
- which learned skinning structure mediates it
- where learned-vs-K6 amplification generalizes and where it fails
- which structural factor is most strongly implicated by counterfactual analysis

## Experimental system

Current case study: Apple HUGS on NeuMan pretrained checkpoints.

Independent model-level units:

- Seattle
- Parkinglot
- Jogging

Independent checkpoint count: `n=3`.

Pose/frame diagnostics are nested within checkpoints and must not be counted as independent model-level replications.

Current body-chain scope:

- left wrist
- left elbow
- left shoulder

## LBS framing

A Gaussian `g` under linear blend skinning can be summarized as:

`T_g = sum_j w_{g,j} A_j`

A Gaussian with positive support on a joint or descendant branch can therefore respond to that branch's transform even when the Gaussian is anatomically distant from the perturbed joint.

For the observed contralateral response, the opposite-side joint itself is not rotating. The contralateral Gaussian moves because learned HUGS assigns it positive support on the perturbed side's descendant branch, which enters its blended transform.

## Step 18 canonical scientific result

Step 18 is complete and frozen after canonical A100 reconciliation.

Final reconciliation session:

`research/sessions/2026-09-17-step18-a100-final-reconciliation.md`

Research progression:

`discovery -> replication -> K6 replacement -> selective causal ablation -> second-joint generalization -> third-joint preregistered negative result -> counterfactual mechanism decomposition -> arm-chain support-topology synthesis -> A100 provenance reconciliation -> final mechanism freeze`

### Wrist

Step 16E0 left wrist:

- 3/3 checkpoints pass
- 18 nested pose diagnostics
- global minimum K6 reduction: `99.708575087815%`
- global minimum selective-ablation reduction: `100.0%`
- global minimum removed-mass correlation: `0.9808287038512752`

### Elbow

Step 17C0 left elbow:

- 3/3 checkpoints pass
- 18 nested pose diagnostics
- global minimum K6 reduction: `99.81874059431833%`
- global minimum selective-ablation reduction: `100.0%`
- global minimum removed-mass correlation: `0.9688984153761956`

Combined wrist + elbow:

- 3 independent pretrained checkpoints
- 2 tested joints
- 36 nested pose diagnostics
- 6/6 joint x checkpoint cells pass

### Shoulder preregistered generalization — canonical A100 R2

Frozen setup:

- joint: SMPL 16
- perturbation: local `z +10 deg`
- descendant branch: `[16,18,20,22]`
- contralateral subset: `{14,17,19,21,23}`
- Seattle poses: `[2,7,12,17]`
- Parkinglot poses: `[2,7,12,17]`
- Jogging poses: `[2,7,12,17,22,27,32,37,42,47]`

Predeclared thresholds:

- K6 reduction `>=95%`
- selective-ablation reduction `>=99.999%`
- removed-mass/displacement-reduction correlation `>=0.90`
- max/summed ablated contralateral response `<=1e-8`

Canonical A100 shoulder result:

- 18 nested poses
- kinematic pass: 18/18
- K6 pass: 0/18
- selective ablation pass: 18/18
- correlation pass: 14/18
- overall pass: 0/18
- negative K6 reductions: 5
- K6 reduction min/median/max: `-77.67225758078598 / 42.390431156682965 / 76.3901059303657%`
- correlation min/median/max: `0.7985822327394099 / 0.9436557686954412 / 0.9812400880684837`

Every corresponding A100 pose retained the same threshold-level classification as historical T4 Step 18B2.

Therefore the preregistered shoulder generalization is **FAIL** and remains unchanged.

Three-joint conclusion:

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Official bounded claims:

- branch-mediated causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

## Shoulder exploratory mechanism decomposition — canonical A100

All analyses after the preregistered shoulder result are exploratory/post-hoc and cannot rescue or alter the confirmatory failure.

### C1 / R3 support-mass analysis

Learned/K6 aggregate shoulder branch-support ratio:

- Seattle: `1.5764279015288012`
- Parkinglot: `0.8379048191221863`
- Jogging: `5.5557058081619255`

Checkpoint-level aggregate support direction and majority displacement direction agree in 3/3 checkpoints on A100, identical to historical T4.

A100 delta-support/delta-displacement correlation min/median/max:

```text
Seattle:    0.9362278422766451 / 0.9664406965256402 / 0.9672864525651061
Parkinglot: 0.9497614357282316 / 0.9738199257592272 / 0.9816398111085524
Jogging:    0.802178029451637  / 0.9193445080163702 / 0.9743405354392872
```

### C2 / R4 total branch-mass matching counterfactual

Counterfactual:

- preserve learned within-branch composition
- replace total shoulder-descendant branch mass per contralateral Gaussian with K6 mass
- rescale learned nonbranch weights proportionally to preserve row sum

All checkpoints had zero fallback rows; pure learned-composition fraction was `1.0`.

Canonical A100 median full-field MAE-gap reduction:

- Seattle: `94.49566207250349%`
- Parkinglot: `83.84751353605428%`
- Jogging: `93.51752945582919%`

Historical T4 medians were `94.49547062277841%`, `83.84695205957038%`, and `93.51712996485506%`; A100 differences are sub-0.001 percentage point.

Interpretation: per-Gaussian branch-support existence/topology and total amount explain most of the shoulder learned-vs-K6 field difference under this exploratory counterfactual.

### C3 / R5 within-branch composition matching counterfactual

Counterfactual:

- preserve learned total shoulder-branch mass
- replace only within-branch allocation with K6 composition where K6 branch mass is positive
- when K6 branch mass is zero, composition is undefined and learned composition remains unchanged

Canonical A100 composition-defined coverage:

- Seattle: `7196 / 33072 = 0.21758587324625062`
- Parkinglot: `20300 / 77622 = 0.2615237948004432`
- Jogging: `1785 / 20887 = 0.08545985541245751`

Thus K6 shoulder-branch mass is zero on about:

- Seattle: `78.24%`
- Parkinglot: `73.85%`
- Jogging: `91.45%`

Learned HUGS has positive shoulder-branch support on all tested contralateral rows in all three checkpoints.

Canonical A100 median full-field MAE-gap reduction:

- Seattle: `-0.10397201493190789%`
- Parkinglot: `-2.195179260385338%`
- Jogging: `0.20347135731436095%`

Effect is essentially zero or slightly negative.

Canonical A100 C2 minus C3 median contrasts:

- Seattle: `94.5996340874354` percentage points
- Parkinglot: `86.04269279643962` percentage points
- Jogging: `93.31405809851483` percentage points

Composition-matched counterfactual-vs-K6 field correlations remain near zero.

### Reconciled C4 mechanism synthesis

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

Frozen exploratory mechanism label:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

Safe wording:

> Exploratory counterfactual analysis strongly implicates per-Gaussian descendant-branch support topology and magnitude as the dominant mechanism underlying the observed shoulder learned-vs-K6 field difference.

Do not call this the training-level cause.

## Arm-chain support-topology synthesis

D0 is a frozen weight-topology analysis and is independent of the deformation GPU rerun.

Nested branches:

- wrist `[20,22]`
- elbow `[18,20,22]`
- shoulder `[16,18,20,22]`

Learned HUGS positive-support fraction on frozen contralateral rows is `1.0` for every tested checkpoint and joint.

K6 positive-support fractions:

Seattle:
- wrist `0.004626269956458636`
- elbow `0.006259071117561683`
- shoulder `0.21758587324625062`

Parkinglot:
- wrist `0.0022287495813042694`
- elbow `0.0022287495813042694`
- shoulder `0.2615237948004432`

Jogging:
- wrist `0.0019629434576530855`
- elbow `0.0019629434576530855`
- shoulder `0.08545985541245751`

Shoulder / elbow K6-support expansion:

- Seattle `34.76328502415459x`
- Parkinglot `117.34104046242776x`
- Jogging `43.53658536585366x`

Learned-positive/K6-zero topology-gap fractions:

Seattle:
- wrist `0.9953737300435413`
- elbow `0.9937409288824384`
- shoulder `0.7824141267537494`

Parkinglot:
- wrist `0.9977712504186957`
- elbow `0.9977712504186957`
- shoulder `0.7384762051995568`

Jogging:
- wrist `0.9980370565423469`
- elbow `0.9980370565423469`
- shoulder `0.9145401445875425`

Aggregate learned/K6 support ratios:

Seattle:
- wrist `650.2177430271481`
- elbow `708.9307441125728`
- shoulder `1.5764279015288012`

Parkinglot:
- wrist `404.35482465513775`
- elbow `1108.6841037038305`
- shoulder `0.8379048191221863`

Jogging:
- wrist `725.5585181759392`
- elbow `1355.289424308762`
- shoulder `5.5557058081619255`

Bounded interpretation: distal wrist/elbow K6 support is nearly absent on frozen contralateral rows, while shoulder support expands sharply. This structural transition aligns with the deformation results. Do not convert this into a causal claim about kinematic depth because depth and nested branch topology are confounded.

## Evidence classes

1. Branch-mediated causality
   - Evidence class: `CONFIRMATORY_PLUS_REPLICATION`
   - Status: `SUPPORTED_FOR_ALL_THREE_TESTED_JOINTS`

2. Learned-vs-K6 amplification
   - Evidence class: `CONFIRMATORY_GENERALIZATION_TEST`
   - Status: `JOINT_DEPENDENT_NOT_UNIVERSAL`

3. K6 support-topology transition
   - Evidence class: `EXPLORATORY_DESCRIPTIVE`
   - Status: `CONSISTENT_ACROSS_ALL_THREE_CHECKPOINTS`

4. Support topology + magnitude mechanism
   - Evidence class: `EXPLORATORY_COUNTERFACTUAL`
   - Status: `STRONGLY_IMPLICATED`

5. Within-branch composition
   - Evidence class: `EXPLORATORY_COUNTERFACTUAL`
   - Status: `SMALL_EFFECT_ON_DEFINED_OVERLAP`

6. Kinematic depth
   - Evidence class: `UNRESOLVED_HYPOTHESIS`
   - Status: `NOT_ESTABLISHED_AS_CAUSAL`

7. Scope
   - HUGS
   - NeuMan 3 pretrained checkpoints
   - one left-arm chain
   - frozen perturbations
   - nested pose diagnostics

## What is still unknown

The direct deformation transmission pathway is substantially characterized. The training-level origin of anatomically nonlocal support remains unknown.

Unverified hypotheses include:

- photometric reconstruction objectives do not enforce anatomical locality
- learned weights compensate pose or geometry error
- learned weights absorb canonical Gaussian placement error
- learned skinning compensates SMPL/model mismatch
- optimization ambiguity allows distant support to act as a surrogate variable

These are hypotheses only.

## Paper 1 working contributions

1. `We introduce an intervention-based diagnostic for anatomical locality in learned animatable-human deformation.`

2. `We show that contralateral deformation is causally mediated by learned support assigned to the perturbed joint's descendant branch, with strong distal-joint amplification that does not generalize unchanged to the shoulder.`

3. `Exploratory counterfactual analysis implicates per-Gaussian descendant-support topology and magnitude, rather than within-branch joint allocation, as the dominant mechanism underlying the observed joint-dependent behavior.`

These are working contribution statements and should still be reviewed for novelty and reviewer vulnerability.

## Claims that are currently prohibited

Do not write these as established findings:

- `Neural digital humans generally suffer from anatomical leakage.`
- `Photometric reconstruction loss causes anatomical leakage.`
- `Distal joints intrinsically leak more than proximal joints.`
- `Our method solves anatomical leakage.`
- `The effect is universal.`
- `We explain why HUGS learns nonlocal weights.`

## Step 19 direction

Step 18 is now closed again after A100 canonical reconciliation. Corrective-method implementation has not started.

Step 19 research question:

> Can anatomical locality be enforced without sacrificing reconstruction quality?

Before implementation, preregister:

- corrective-method hypothesis
- learned quantity to regularize or constrain
- locality metric
- reconstruction-quality metric
- baseline
- success threshold
- held-out/generalization protocol
- ablation plan
- datasets
- body regions
- cross-method generalization plan

Only after this protocol is frozen should implementation begin.

A later generalization question is:

> Is anatomical nonlocality specific to HUGS, or does it emerge across learned human deformation representations?

Future scope should include additional animatable Gaussian-human methods, datasets, subjects, body regions, and possibly non-Gaussian learned deformation representations.

## Research integrity rules

- Never retune thresholds after seeing results.
- Preserve negative results.
- Separate confirmatory, exploratory, and unresolved evidence.
- Do not count nested poses as independent replications.
- Do not generalize beyond tested scope.
- Separate deformation mechanism from training origin.
- Separate correlation, intervention, and descriptive evidence.
- Freeze Step 19 evaluation protocol before method implementation.
- Do not add joints merely to seek a passing result.

## Runtime and provenance

Canonical Step-18 reconciliation runtime:

- GPU: NVIDIA A100-SXM4-40GB
- Python: 3.8.20
- NumPy: 1.24.4
- PyTorch: 1.13.1+cu117
- CUDA: 11.7
- SMPLX: 0.1.28
- TF32: off

SMPL fingerprint:

`f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0`

User-supplied project provenance states that the intended runtime through Step 17 was A100. Historical Step-17 archives themselves establish CUDA use but do not independently identify the GPU model.

Historical Step-18 B1H/B2/C1/C2/C3/C4/D1 artifacts produced on Tesla T4 remain preserved as historical provenance. Their scientific threshold-level conclusions were not overwritten. A100 R1-R5 reconciled the deformation-dependent shoulder evidence and retained the same bounded conclusions.

Historical exact-number reconstruction of the Step-17 elbow archive recovered only 5/6 within the original `1e-5` aggregate tolerance on tested replacement runtimes. Field correlations remained effectively 1.0. The historical gate was not widened.

## Key repository artifacts

Repository: `reusahn/interactive-digital-humans`

Primary continuity files:

- `research/continuity/MASTER_CONTEXT.md`
- `research/continuity/CLAIM_LEDGER.md`
- `research/continuity/BOOTSTRAP.md`
- `research/handoffs/LATEST.md`

Historical Step-18 synthesis records:

- `research/sessions/2026-09-16-step18c2.md`
- `research/sessions/2026-09-16-step18c3.md`
- `research/sessions/2026-09-16-step18c4.md`
- `research/sessions/2026-09-16-step18d0.md`
- `research/sessions/2026-09-16-step18d1.md`

Canonical A100 reconciliation records:

- `research/sessions/2026-09-17-step18r1-a100-frame2-rerun.md`
- `research/sessions/2026-09-17-step18r2-a100-full-pose-rerun.md`
- `research/sessions/2026-09-17-step18r3-a100-c1-reconciliation.md`
- `research/sessions/2026-09-17-step18r4-a100-c2-reconciliation.md`
- `research/sessions/2026-09-17-step18r5-a100-c3-reconciliation.md`
- `research/sessions/2026-09-17-step18-a100-final-reconciliation.md`

Canonical Drive artifacts:

- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_displacements.npz`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_displacements.npz`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.json`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.csv`
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual_displacements.npz`
- `experiments/08-second-joint-generalization/18R5_A100_shoulder_composition_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R5_A100_shoulder_composition_match_counterfactual_displacements.npz`

Historical T4 artifacts remain preserved and must not be overwritten.

## Continuity policy

This repository, not ChatGPT conversational memory, is the authoritative continuity source.

At the end of every substantial research session:

1. archive the session under `research/sessions/`
2. update `research/handoffs/LATEST.md`
3. update this `MASTER_CONTEXT.md` only when durable research understanding changes
4. update `CLAIM_LEDGER.md` when claim status or canonical numeric anchors change
5. keep raw large arrays/checkpoints on Drive and store compact Markdown/CSV/JSON/scripts/provenance in GitHub

If a future conversation lacks context, load `BOOTSTRAP.md`, `MASTER_CONTEXT.md`, `CLAIM_LEDGER.md`, and `LATEST.md` before doing research work.