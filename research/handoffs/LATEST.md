# Latest Research Handoff

Current continuation date: **2026-09-17**.

## CURRENT STATE — Step 19 preregistration FROZEN

Step 18 remains closed after canonical A100 reconciliation.

Step 19 protocol design is now complete. Corrective-method scientific training has **not** started and no Step-19 method outcome has been observed.

The next allowed phase is implementation smoke/unit validation only.

## Canonical Step-18 result retained

Independent pretrained model unit: checkpoint, `n=3`.

Checkpoints:

- Seattle
- Parkinglot
- Jogging

Pose/frame diagnostics remain nested within checkpoints.

Three-joint frozen interpretation:

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Final bounded Step-18 mechanism label:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

Shoulder confirmatory failure remains `FAIL_UNCHANGED`.

Canonical A100 shoulder R2:

- K6 pass `0/18`
- selective-ablation pass `18/18`
- correlation pass `14/18`
- K6 reduction min/median/max `-77.67225758078598 / 42.390431156682965 / 76.3901059303657%`

Canonical A100 C2 median MAE-gap reduction:

- Seattle `94.49566207250349%`
- Parkinglot `83.84751353605428%`
- Jogging `93.51752945582919%`

Canonical A100 C3 median MAE-gap reduction:

- Seattle `-0.10397201493190789%`
- Parkinglot `-2.195179260385338%`
- Jogging `0.20347135731436095%`

Do not reinterpret these exploratory analyses as a training-level cause.

## Step 19 research question

> Can anatomical locality be enforced without sacrificing reconstruction quality?

## Frozen Step-19 source provenance

Official HUGS source:

`https://github.com/apple/ml-hugs.git`

Exact audited source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Step 19E0 initially found no local HUGS checkout and is preserved as a failed source-discovery audit.

Step 19E0R recovered the exact audited commit from the official repository with a clean working tree and confirmed the integration path.

E0R audit Drive artifact:

`private_research/2026-09-17_step19e0r_hugs_source_recovery_audit.json`

SHA256:

`1f81177e924b956e6c8455faad8a0e386d3dcba8ceeee5d1b2fffcfd47725dbb`

## Frozen primary method — A1

Method label:

`99%-support-envelope locality regularizer`

Reference:

- subject-specific canonical SMPL-derived K6 effective mapping
- explicit `K = 6`
- support-envelope threshold `rho = 0.99`
- K6 reference and envelope built under `torch.no_grad()`
- no gradient through reference or envelope membership

Learned quantity:

- post-softmax normalized HUGS LBS weights
- original softmax temperature remains `0.1`

For Gaussian `g`, let detached binary mask `M[g,j]` indicate the smallest K6-reference joint set whose cumulative reference mass reaches 99%.

Per-Gaussian nonlocal support mass:

`NSM_g = sum_j w[g,j] * (1 - M[g,j])`

Primary locality loss:

`L_local = mean_g NSM_g`

Training objective:

`L_total = L_original_HUGS + lambda_local * L_local`

IRDR is not optimized directly. It remains the primary behavioral locality evaluation metric.

Original HUGS full-vector LBS MSE remains OFF in primary A1 (`lbs_w = 0`).

## Frozen development protocol

Development sequence: `Seattle` only.

Frozen split:

- train count `33`
- val `[22,27,32,37]`
- test `[2,7,12,17]`

Lambda candidates:

`[1e-4, 1e-3, 1e-2, 1e-1, 1.0]`

Paired seeds:

`[0,1,2]`

Select the **smallest** nonzero lambda passing every frozen Seattle-validation criterion.

Locality criteria:

- median paired relative macro-IRDR reduction `>= 50%`
- median paired IRDR difference `<= 0` separately for shoulder, elbow, wrist

Human-crop reconstruction non-inferiority:

- mean paired delta PSNR `>= -0.5 dB`
- mean paired delta SSIM `>= -0.01`
- mean paired delta LPIPS `<= +0.02`

If no lambda passes, A1 fails development. Do not expand the lambda grid or relax thresholds inside this protocol.

Seattle test is locked during lambda selection.

## Frozen confirmatory protocol

Held-out sequences:

- Parkinglot
- Jogging

Frozen test frames:

- Parkinglot `[2,7,12,17]`
- Jogging `[2,7,12,17,22,27,32,37,42,47]`

The Seattle-selected method and lambda transfer unchanged. No per-sequence tuning.

Both Parkinglot and Jogging must independently pass all locality and quality criteria for primary Step-19 success.

## Frozen quality metrics

Primary human-crop metrics:

- PSNR
- SSIM
- LPIPS

Full-frame versions are secondary.

## Frozen ablations

A0 — matched HUGS baseline

- `lambda_local = 0`
- `lbs_w = 0`

A1 — proposed 99%-support-envelope locality regularizer

A2 — direct full-vector K6 MSE matching

A2 uses the same Seattle-only coefficient grid and seeds as A1. It is secondary and does not determine primary Step-19 success.

## Frozen implementation contract

Audited integration path:

- normalized learned LBS is produced in `hugs/models/hugs_trimlp.py` by `F.softmax(lbs_weights / 0.1, dim=-1)`
- existing deformation path consumes these normalized weights
- existing `hugs/losses/loss.py` receives `human_gs_out['lbs_weights']`
- locality term is added as `loss_dict['locality'] = lambda_local * L_local`
- existing loss aggregation remains unchanged
- existing trainer `loss.backward()` and human optimizer step remain unchanged

Primary A1 must NOT:

- change softmax temperature
- modify SMPL kinematics or transform semantics
- hard-zero learned weights
- mask/renormalize learned LBS after softmax
- optimize IRDR directly
- combine A1 with direct K6 full-vector MSE
- tune using Parkinglot/Jogging

The selected lambda is constant for the full 30,000-step run. No warmup or annealing.

## Required smoke/unit checks before scientific training

1. envelope rows are nonempty
2. envelope mask is binary
3. K6 reference rows sum approximately to 1
4. learned normalized LBS rows sum approximately to 1
5. `L_local >= 0`
6. `lambda_local = 0` contributes exactly zero locality loss
7. K6 reference and mask require no gradient
8. locality loss produces gradient in learned deformation parameters
9. baseline forward outputs remain unchanged when locality is disabled
10. no Seattle validation/test or held-out scientific metric is used during smoke checks

## Frozen preregistration artifacts

Drive final preregistration:

`private_research/2026-09-17_step19_preregistration_draft.md`

SHA256:

`6c1f464f36dd3a567464fc091329abf605b2d37e12800a126a55ec35dd0a9b33`

Drive implementation contract:

`private_research/2026-09-17_step19_frozen_implementation_contract.json`

SHA256:

`255c216f5bc17d8efa0101e3b11fafe5562e2d4d1c18bcbb271fed953d23191c`

GitHub freeze record:

`research/sessions/2026-09-17-step19e1-preregistration-frozen.md`

## Claim status

No scientific claim status changed at preregistration freeze.

`CL-13` remains `UNTESTED`:

> Anatomical locality can be enforced without sacrificing reconstruction quality.

Do not describe the method as successful until the frozen Step-19 scientific protocol is executed.

## Exact next action

Create an isolated implementation working copy/branch from HUGS commit `86ebe552...` and implement only the frozen A1 locality primitive plus non-scientific smoke/unit tests.

Do not launch 30,000-step scientific training yet.

Do not inspect Seattle validation/test method outcomes, Parkinglot outcomes, or Jogging outcomes during implementation validation.

## Research-record rule

Preserve failed and successful audits, frozen protocol hashes, source provenance, and all negative scientific outcomes. Never alter the frozen Step-19 thresholds or lambda grid after method outcomes are observed.
