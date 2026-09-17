# Step 19E1 — Final Preregistration Freeze

Date: 2026-09-17
Status: `STEP_19_PREREGISTRATION_FROZEN`

No corrective-method implementation, model training, or Step-19 scientific outcome had occurred at freeze time.

## Frozen artifacts

Private Drive:

- `private_research/2026-09-17_step19_preregistration_draft.md`
  - final SHA256: `6c1f464f36dd3a567464fc091329abf605b2d37e12800a126a55ec35dd0a9b33`
- `private_research/2026-09-17_step19_frozen_implementation_contract.json`
  - SHA256: `255c216f5bc17d8efa0101e3b11fafe5562e2d4d1c18bcbb271fed953d23191c`
- source audit `private_research/2026-09-17_step19e0r_hugs_source_recovery_audit.json`
  - SHA256: `1f81177e924b956e6c8455faad8a0e386d3dcba8ceeee5d1b2fffcfd47725dbb`

## Source provenance

Official source: `https://github.com/apple/ml-hugs.git`

Exact audited HUGS commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

E0R recovered this exact commit with a clean working tree. The source audit confirmed:

- learned normalized LBS weights are produced by temperature-softmax with temperature `0.1`
- learned LBS weights are consumed by the existing HUGS deformation path
- the existing loss path receives `human_gs_out['lbs_weights']`
- the existing trainer performs `loss.backward()` and then the human optimizer step

## Primary Step-19 method

A1: `99%-support-envelope locality regularizer`

Reference:

- subject-specific canonical SMPL-derived K6 effective mapping
- explicit `K = 6`
- support-envelope threshold `rho = 0.99`
- reference construction under `torch.no_grad()`
- no gradient through K6 reference or envelope membership

Learned quantity:

- post-softmax normalized learned HUGS LBS weights
- HUGS softmax temperature remains `0.1`

For Gaussian `g`, let detached binary mask `M[g,j]` indicate joints in the smallest K6-reference joint set whose cumulative mass reaches 99%.

Per-Gaussian nonlocal support mass:

`NSM_g = sum_j w[g,j] * (1 - M[g,j])`

Primary locality loss:

`L_local = mean_g NSM_g`

Training objective:

`L_total = L_original_HUGS + lambda_local * L_local`

IRDR remains an independent behavioral evaluation metric and is not optimized directly.

## Development protocol

Development sequence: `Seattle`

Frozen NeuMan split:

- train: 33 frames
- val: `[22,27,32,37]`
- test: `[2,7,12,17]`

Lambda candidates:

`[1e-4, 1e-3, 1e-2, 1e-1, 1.0]`

Paired seeds:

`[0,1,2]`

Select the smallest nonzero lambda satisfying all frozen Seattle-validation criteria.

Development locality requirement:

- median paired relative macro-IRDR reduction `>= 50%`
- median IRDR difference `<= 0` separately for shoulder, elbow, wrist

Reconstruction-quality non-inferiority:

- mean paired delta PSNR `>= -0.5 dB`
- mean paired delta SSIM `>= -0.01`
- mean paired delta LPIPS `<= +0.02`

If no lambda passes, the current A1 formulation fails development. Do not expand the grid or relax thresholds within this protocol.

## Confirmatory protocol

Held-out sequences:

- Parkinglot
- Jogging

Frozen test frames:

- Parkinglot: `[2,7,12,17]`
- Jogging: `[2,7,12,17,22,27,32,37,42,47]`

No per-sequence lambda retuning.

Both held-out sequences must independently pass all locality and quality criteria for the preregistered primary Step-19 hypothesis to be classified as supported.

## Primary quality metrics

Human-crop:

- PSNR
- SSIM
- LPIPS

Full-frame versions are secondary diagnostics.

## Ablations

A0: matched HUGS baseline

- `lambda_local = 0`
- original HUGS `lbs_w = 0`

A1: proposed 99%-support-envelope locality regularizer

A2: direct full-vector K6 MSE matching

- own Seattle-only coefficient search over the same candidate grid
- same seeds and frozen selection criteria
- secondary ablation; does not determine primary Step-19 success

## Implementation contract

Primary A1 must not:

- modify LBS temperature
- modify SMPL kinematics
- modify transform semantics
- hard-zero learned weights
- renormalize weights after masking
- optimize IRDR directly
- use direct full-vector K6 MSE simultaneously
- tune on Parkinglot or Jogging

Loss integration is at the existing loss level using normalized `human_gs_out['lbs_weights']`; the existing trainer backward and optimizer path remains unchanged.

The locality term is active whenever the human model and learned LBS are available and is constant for the full 30,000-step run. No warmup or annealing.

## Required implementation smoke checks before scientific training

1. envelope rows nonempty
2. envelope mask binary
3. K6 reference rows sum approximately to 1
4. learned normalized LBS rows sum approximately to 1
5. `L_local >= 0`
6. `lambda_local = 0` contributes exactly zero locality loss
7. reference and mask require no gradient
8. locality loss produces gradient in learned deformation parameters
9. baseline forward outputs are unchanged when locality is disabled
10. no validation/test scientific metric is used during smoke checks

## Scientific state

No claim status changes occurred. `CL-13` remains `UNTESTED` until Step-19 scientific training/evaluation.

## Exact next action

Begin implementation on an isolated working copy/branch from HUGS commit `86ebe552...` and perform smoke/unit validation only. Do not inspect Seattle validation outcomes or any Parkinglot/Jogging scientific result until the implementation matches the frozen contract.
