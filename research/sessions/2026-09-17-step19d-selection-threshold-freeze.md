# Step 19D — Lambda Search and Success/Failure Threshold Freeze

Date: 2026-09-17
Status: `FROZEN_BEFORE_METHOD_IMPLEMENTATION`

## Purpose

Freeze the Step-19 development-search rule, reconstruction-quality non-inferiority margins, locality success threshold, held-out confirmatory rule, and anti-retuning rules before any locality-method implementation or training.

No model implementation, model training, or Step-19 method outcome was observed before this freeze.

## Input preregistration state

Private draft:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19_preregistration_draft.md`

Input Step-19C SHA256:

`4b94556faaad4a37b73a1065291e8126efba8a76968672b37e2078c78d2b8088`

## Frozen lambda search

Development sequence: Seattle

Development split: frozen Seattle validation split

Paired seeds:

`[0,1,2]`

Nonzero candidate grid:

`[1e-4, 1e-3, 1e-2, 1e-1, 1.0]`

Baseline:

`lambda_local = 0`

Selection rule:

> Select the smallest nonzero lambda satisfying all frozen reconstruction-quality and locality criteria.

No additional lambda may be introduced after development outcomes are observed within this preregistered experiment.

## Reconstruction-quality non-inferiority

Paired convention:

- `delta_PSNR = LOCALITY - BASELINE`
- `delta_SSIM = LOCALITY - BASELINE`
- `delta_LPIPS = LOCALITY - BASELINE`

Development and held-out quality criteria:

- mean paired `delta_PSNR >= -0.5 dB`
- mean paired `delta_SSIM >= -0.01`
- mean paired `delta_LPIPS <= +0.02`

All three must pass.

These are preregistered study margins, not claimed as universal field standards.

## Locality success

For paired seed `r`:

`relative_macro_IRDR_reduction_r = (macro_IRDR_baseline_r - macro_IRDR_locality_r) / max(macro_IRDR_baseline_r, 1e-8)`

Primary locality requirement:

`median_r(relative_macro_IRDR_reduction_r) >= 0.50`

Joint guardrail:

For shoulder, elbow, and wrist separately:

`median_r(joint_IRDR_locality_r - joint_IRDR_baseline_r) <= 0`

Thus macro improvement cannot hide worsening of one tested joint.

## Development failure rule

If no candidate lambda satisfies every quality and locality criterion:

- no lambda is selected;
- the current support-envelope formulation fails the preregistered development stage;
- the lambda grid is not expanded;
- thresholds are not relaxed;
- Parkinglot/Jogging confirmatory outcomes are not used to rescue the formulation.

Seattle test remains locked during lambda selection.

## Held-out confirmatory rule

Held-out sequences:

- Parkinglot
- Jogging

The exact Seattle-selected lambda is transferred without per-sequence retuning.

Each held-out sequence independently must satisfy:

### Locality

- median paired relative macro-IRDR reduction `>= 0.50`
- shoulder median paired IRDR difference `<= 0`
- elbow median paired IRDR difference `<= 0`
- wrist median paired IRDR difference `<= 0`

### Reconstruction quality

- mean paired `delta_PSNR >= -0.5 dB`
- mean paired `delta_SSIM >= -0.01`
- mean paired `delta_LPIPS <= +0.02`

Primary Step-19 success requires BOTH Parkinglot AND Jogging to pass all criteria.

If only one passes, report mixed / non-generalizing evidence and do not classify the primary Step-19 hypothesis as supported.

## Frozen anti-retuning rules

- no lambda-grid expansion after results
- no threshold relaxation after results
- no sequence-specific lambda
- no best-seed-only primary reporting
- no checkpoint selection from held-out test
- no Parkinglot/Jogging tuning
- negative result remains valid
- individual seed results remain visible

## Frozen artifacts

Threshold protocol:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19_frozen_selection_thresholds.json`

Protocol SHA256:

`2c27de339f2df46da3342c9b223c130f3ffc6173563a3338c34b2a1f871cb822`

Updated private preregistration draft SHA256:

`30bd3f223f4913259e0b3224c7fedf1174596f2e0459200ab4c3254677f81606`

## Still unfrozen after Step 19D

- ablation plan
- exact locality-loss implementation contract
- exact code-level integration point in HUGS

The next action must audit the actual local HUGS source before freezing the implementation contract. Do not infer a source path or tensor name from memory.