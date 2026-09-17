# Step 19B — Core Locality Definitions Freeze

Date: 2026-09-17
Status: `PREREGISTRATION_CORE_DEFINITIONS_FROZEN`

No model implementation, training, or Step-19 outcome observation occurred in this step.

## Private preregistration draft

Drive path:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19_preregistration_draft.md`

Pre-19B backup:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19_preregistration_draft_before_19B.md`

Post-19B draft SHA256:

`a547ede1e8db66aa5d2d38c2d23a23452521ff52b8d75825ecd34734c9b43b99`

## Frozen hypothesis

A mechanism-aware anatomical support-envelope regularizer applied to learned Gaussian LBS weights will reduce anatomically nonlocal deformation under local joint perturbations while preserving reconstruction quality.

The method hypothesis is intentionally weaker than direct K6 weight matching. Learned weights inside the anatomically admissible envelope remain free rather than being forced to reproduce the K6 distribution.

## Frozen anatomical reference

For each Gaussian `g`, use the subject-specific canonical SMPL-derived K6 effective mapping `q[g,j]` only to define anatomically admissible joint support.

The envelope mass level is frozen at:

`rho = 0.99`

Define `S_g` as the smallest set of joints, ordered by descending `q[g,j]`, whose cumulative K6 reference mass reaches at least `0.99`.

## Frozen regularized quantity

For learned normalized HUGS LBS weights `w[g,j]`, define nonlocal support mass:

`NSM_g = sum_(j not in S_g) w[g,j]`

Structural regularizer:

`L_local = mean_g NSM_g`

This penalizes learned support outside the K6-derived anatomical envelope without requiring learned within-envelope composition to equal K6 composition.

## Frozen anatomical-locality sets for perturbation j

Let `B_j` be the set of transforms that actually change under the frozen SMPL local-joint perturbation, including the perturbed joint and changed descendants.

Define:

- `Local_j = {g : S_g intersects B_j}`
- `Remote_j = {g : S_g does not intersect B_j}`

These sets are determined independently of the Step-19 learned output and must not be redefined after training.

## Frozen primary behavioral locality metric

For Gaussian displacement under joint `j`, pose `p`:

`d[g;j,p] = ||x_perturbed[g;j,p] - x_baseline[g;p]||_2`

Define Intervention Remote Deformation Ratio:

`IRDR(j,p) = sum_(g in Remote_j) d[g;j,p] / (sum_(all human g) d[g;j,p] + 1e-12)`

IRDR is the primary Step-19 locality outcome.

Structural `NSM` is secondary because it is directly optimized by the proposed regularizer; the primary behavioral endpoint must test actual deformation locality rather than only the training objective.

## Not yet frozen

- reconstruction-quality metrics
- baseline/comparison conditions
- held-out joint/pose/generalization protocol
- success/failure thresholds
- loss coefficient / training hyperparameter protocol
- ablation plan

These must be preregistered before implementation/training and must not be tuned after observing method outcomes.
