# Step 19C — Quality, Baseline, and Held-Out Protocol Freeze

Date: 2026-09-17
Status: `PREREGISTRATION_IN_PROGRESS`

No method implementation, model training, or Step-19 outcome observation occurred in this step.

## Input preregistration state

Private draft:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19_preregistration_draft.md`

Input SHA256 from frozen Step 19B state:

`a547ede1e8db66aa5d2d38c2d23a23452521ff52b8d75825ecd34734c9b43b99`

## Frozen NeuMan split membership

Split artifact:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19_frozen_neuman_splits.json`

SHA256:

`d3a37090f14a25c31ca7b99c11cf6e586a21eef843124140408d28a5a05ed743`

### Seattle

- scene length: 41
- train: 33 frames
- validation: `[22,27,32,37]`
- test: `[2,7,12,17]`

### Parkinglot

- scene length: 42
- train: 34 frames
- validation: `[22,27,32,37]`
- test: `[2,7,12,17]`

### Jogging

- scene length: 102
- train: 82 frames
- validation: `[52,57,62,67,72,77,82,87,92,97]`
- test: `[2,7,12,17,22,27,32,37,42,47]`

These memberships reproduce the released HUGS/NeuMan split rule and are frozen before Step-19 training.

## Experimental roles

Development sequence:

`Seattle`

Confirmatory held-out sequences:

- `Parkinglot`
- `Jogging`

Seattle may be used for implementation debugging and preregistered lambda selection. Parkinglot/Jogging validation and test outcomes must not be used to redesign the method or tune hyperparameters.

## Reconstruction-quality metrics

Primary quality metrics on the human tight rectangular crop:

- PSNR, higher is better
- SSIM, higher is better
- LPIPS, lower is better

Secondary diagnostics:

- full-frame PSNR
- full-frame SSIM
- full-frame LPIPS

Do not combine the three quality metrics into one synthetic image-quality score.

## Primary comparison conditions

### A. HUGS-BASELINE

- original matched HUGS training condition
- `lambda_local = 0`

### B. HUGS-LOCALITY

- identical data membership, initialization procedure, optimization length, rendering losses, optimizer settings, and densification schedule
- only intended scientific method difference is addition of `lambda_local * L_local`

Paired training seeds:

`[0,1,2]`

Final checkpoint:

`30000`

No early stopping and no held-out-performance checkpoint selection.

## Locality evaluation protocol

Frozen perturbations:

- left shoulder: SMPL joint 16, local z +10 degrees
- left elbow: SMPL joint 18, local z +10 degrees
- left wrist: SMPL joint 20, local z +10 degrees

Transform semantics remain identical to Step 18.

For each perturbation and frozen evaluation frame, compute the Step-19B frozen `IRDR`.

Aggregation:

- per sequence/joint: median IRDR across frozen evaluation frames
- per sequence: arithmetic mean of shoulder/elbow/wrist joint-level median IRDR values (`macro_IRDR`)
- retain individual seed values and report mean/std across seeds

Frames and seeds are nested/repeated diagnostics, not independent model-level replications.

## Generalization scope

Primary Step-19 generalization scope, if supported:

- method development on Seattle
- frozen-method transfer to separately trained Parkinglot and Jogging sequences/subjects
- evaluation on held-out observed frames
- same three left-arm perturbation types

No held-out-joint, right-arm, lower-body, cross-dataset, or cross-method claim is preregistered here.

## Output preregistration state

Updated private draft SHA256:

`4b94556faaad4a37b73a1065291e8126efba8a76968672b37e2078c78d2b8088`

Still not frozen after Step 19C:

- success/failure thresholds
- lambda-local candidate/search rule
- final selected lambda-local
- ablation plan
- exact loss-code implementation

## Integrity guardrail

No method implementation, training, or Step-19 outcome was observed before this protocol freeze.
