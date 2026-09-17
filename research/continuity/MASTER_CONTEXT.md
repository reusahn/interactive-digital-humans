# Master Research Context

Last updated: 2026-09-17

This file is the durable source of truth for continuing the Interactive Digital Humans research across new ChatGPT conversations. Read this before answering research-continuity questions.

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

Important scope boundary: Paper 1 currently does **not** explain why training learns the nonlocal support topology. Training-level causes remain unresolved hypotheses.

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

## Step 18 frozen scientific result

Step 18 is complete and frozen at Step 18D1.

Research progression:

`discovery -> replication -> K6 replacement -> selective causal ablation -> second-joint generalization -> third-joint preregistered negative result -> counterfactual mechanism decomposition -> arm-chain support-topology synthesis -> final mechanism freeze`

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

### Shoulder preregistered generalization

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

Shoulder result:

- 18 nested poses
- kinematic pass: 18/18
- K6 pass: 0/18
- selective ablation pass: 18/18
- correlation pass: 14/18
- overall pass: 0/18
- negative K6 reductions: 5
- K6 reduction range: `-77.671145% to 76.389818%`

The preregistered shoulder generalization is **FAIL** and remains unchanged.

Three-joint frozen conclusion:

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Official frozen claims:

- branch-mediated causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

## Shoulder exploratory mechanism decomposition

All analyses after the preregistered shoulder result are exploratory/post-hoc and cannot rescue or alter the confirmatory failure.

### C1 support-mass analysis

Learned/K6 aggregate shoulder branch-support ratio:

- Seattle: `1.5764279015288012`
- Parkinglot: `0.8379048191221863`
- Jogging: `5.5557058081619255`

Checkpoint-level aggregate support direction and majority displacement direction agree in 3/3 checkpoints.

### C2 total branch-mass matching counterfactual

Counterfactual:

- preserve learned within-branch composition
- replace total shoulder-descendant branch mass per contralateral Gaussian with K6 mass

Median full-field MAE-gap reduction:

- Seattle: `94.49547062277841%`
- Parkinglot: `83.84695205957038%`
- Jogging: `93.51712996485506%`

Interpretation: per-Gaussian branch-support amount/topology explains most of the shoulder learned-vs-K6 field difference under this exploratory counterfactual.

### C3 within-branch composition matching counterfactual

Counterfactual:

- preserve learned total shoulder-branch mass
- replace only within-branch joint allocation with K6 composition where K6 composition is defined

Median full-field MAE-gap reduction:

- Seattle: `-0.10402258952364463%`
- Parkinglot: `-2.1951923116722116%`
- Jogging: `0.20329469100371367%`

Effect is essentially zero or slightly negative.

K6 shoulder-branch mass is exactly zero on most contralateral rows:

- Seattle: about `78.24%`
- Parkinglot: about `73.85%`
- Jogging: about `91.45%`

Learned HUGS has positive shoulder-branch support on all tested contralateral rows in all three checkpoints.

Frozen exploratory mechanism label:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

Safe wording:

> Exploratory counterfactual analysis strongly implicates per-Gaussian descendant-branch support topology and magnitude as the dominant mechanism underlying the observed shoulder learned-vs-K6 field difference.

Do not call this the training-level cause.

## Arm-chain support-topology synthesis

Nested branches:

- wrist `[20,22]`
- elbow `[18,20,22]`
- shoulder `[16,18,20,22]`

Learned HUGS positive-support fraction on frozen contralateral rows is `1.0` for every tested checkpoint and joint.

K6 positive-support fractions:

Seattle:
- wrist `0.0046263`
- elbow `0.0062591`
- shoulder `0.2175859`

Parkinglot:
- wrist `0.0022287`
- elbow `0.0022287`
- shoulder `0.2615238`

Jogging:
- wrist `0.0019629`
- elbow `0.0019629`
- shoulder `0.0854599`

Shoulder / elbow K6-support expansion:

- Seattle `34.7633x`
- Parkinglot `117.3410x`
- Jogging `43.5366x`

Learned-positive/K6-zero topology-gap fractions:

Seattle:
- wrist `0.9953737`
- elbow `0.9937409`
- shoulder `0.7824141`

Parkinglot:
- wrist `0.9977713`
- elbow `0.9977713`
- shoulder `0.7384762`

Jogging:
- wrist `0.9980371`
- elbow `0.9980371`
- shoulder `0.9145401`

Aggregate learned/K6 support ratios:

Seattle:
- wrist `650.22`
- elbow `708.93`
- shoulder `1.5764`

Parkinglot:
- wrist `404.35`
- elbow `1108.68`
- shoulder `0.8379`

Jogging:
- wrist `725.56`
- elbow `1355.29`
- shoulder `5.5557`

Bounded interpretation: distal wrist/elbow K6 support is nearly absent on frozen contralateral rows, while shoulder support expands sharply. This structural transition aligns strongly with the deformation results. Do not convert this into a causal claim about kinematic depth because depth and nested branch topology are confounded.

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

Step 18 is complete. Corrective-method implementation has not started.

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

Frozen primary Step-18 runtime:

- GPU: Tesla T4
- Python: 3.8.20
- NumPy: 1.24.4
- PyTorch: 1.13.1+cu117
- CUDA: 11.7
- SMPLX: 0.1.28
- TF32: off

This runtime is a continuation choice and is not proof that historical Step 17 used T4.

Historical exact-number reconstruction of the Step-17 elbow archive recovered only 5/6 within the original `1e-5` aggregate tolerance on tested modern/legacy replacement runtimes. Field correlations remained effectively 1.0. The historical gate was not widened.

## Key repository artifacts

Repository: `reusahn/interactive-digital-humans`

Primary continuity files:

- `research/continuity/MASTER_CONTEXT.md`
- `research/continuity/CLAIM_LEDGER.md`
- `research/continuity/BOOTSTRAP.md`
- `research/handoffs/LATEST.md`

Frozen Step-18 session records:

- `research/sessions/2026-09-16-step18c2.md`
- `research/sessions/2026-09-16-step18c3.md`
- `research/sessions/2026-09-16-step18c4.md`
- `research/sessions/2026-09-16-step18d0.md`
- `research/sessions/2026-09-16-step18d1.md`

Step 18D1 session commit: `3501a54805c6e59495289bd939873144c5f65704`

Latest end-of-Step-18 handoff commit: `8262228c2272808e9e257ae3ad38d869cff801e5`

Drive final Step-18 synthesis:

`experiments/08-second-joint-generalization/18D1_final_arm_chain_mechanism_synthesis.json`

## Continuity policy

This repository, not ChatGPT conversational memory, is the authoritative continuity source.

At the end of every substantial research session:

1. archive the session under `research/sessions/`
2. update `research/handoffs/LATEST.md`
3. update this `MASTER_CONTEXT.md` only when durable research understanding changes
4. update `CLAIM_LEDGER.md` when claim status changes
5. keep raw large arrays/checkpoints on Drive and store compact provenance/results in GitHub

If a future conversation lacks context, load `BOOTSTRAP.md`, `MASTER_CONTEXT.md`, `CLAIM_LEDGER.md`, and `LATEST.md` before doing research work.
