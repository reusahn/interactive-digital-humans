# Latest Research Handoff

Current continuation date: **2026-09-17**.

## CURRENT STATE — Step 19 implementation smoke validation in progress

Step 18 remains closed after canonical A100 reconciliation.

Step 19 preregistration is **FROZEN**. Scientific training has **not** started. No Step-19 method outcome has been observed.

Step 19I0 is complete and passed. The next allowed action is Step 19I1 integration smoke testing only.

## Canonical Step-18 result retained

Independent pretrained model unit: checkpoint, `n=3`.

Checkpoints: Seattle, Parkinglot, Jogging.

Pose/frame diagnostics remain nested within checkpoints.

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Frozen exploratory mechanism label:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

Shoulder confirmatory failure remains `FAIL_UNCHANGED`.

Do not reinterpret Step-18 exploratory mechanism analyses as training-level causes.

## Step 19 research question

> Can anatomical locality be enforced without sacrificing reconstruction quality?

## Frozen source provenance

Official HUGS source: `https://github.com/apple/ml-hugs.git`

Exact audited commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Step 19E0 failed because no local HUGS checkout was present; preserve that failed audit.

Step 19E0R recovered the exact audited commit from the official repository with a clean working tree.

E0R Drive audit:

`private_research/2026-09-17_step19e0r_hugs_source_recovery_audit.json`

SHA256:

`1f81177e924b956e6c8455faad8a0e386d3dcba8ceeee5d1b2fffcfd47725dbb`

## Frozen primary method — A1

Method: `99%-support-envelope locality regularizer`.

Reference:

- subject-specific canonical SMPL-derived K6 effective mapping
- explicit `K = 6`
- support-envelope threshold `rho = 0.99`
- reference and envelope under `torch.no_grad()`
- no gradient through K6 reference or envelope membership

Learned quantity:

- post-softmax normalized HUGS LBS weights
- original HUGS softmax temperature remains `0.1`

Per-Gaussian nonlocal support mass:

`NSM_g = sum_j w[g,j] * (1 - M[g,j])`

Primary locality loss:

`L_local = mean_g NSM_g`

Training objective:

`L_total = L_original_HUGS + lambda_local * L_local`

IRDR is not optimized directly. Original HUGS full-vector LBS MSE remains OFF in primary A1 (`lbs_w = 0`).

## Frozen development protocol

Development sequence: Seattle only.

Frozen Seattle split:

- train count `33`
- val `[22,27,32,37]`
- test `[2,7,12,17]`

Lambda candidates:

`[1e-4, 1e-3, 1e-2, 1e-1, 1.0]`

Paired seeds:

`[0,1,2]`

Select the smallest nonzero lambda passing every frozen Seattle-validation criterion.

Locality:

- median paired relative macro-IRDR reduction `>= 50%`
- median paired IRDR difference `<= 0` separately for shoulder, elbow, wrist

Human-crop reconstruction non-inferiority:

- mean paired delta PSNR `>= -0.5 dB`
- mean paired delta SSIM `>= -0.01`
- mean paired delta LPIPS `<= +0.02`

If none passes, A1 fails development. Do not expand grid or relax thresholds. Seattle test remains locked during lambda selection.

## Frozen confirmatory protocol

Held-out sequences: Parkinglot and Jogging.

Frozen tests:

- Parkinglot `[2,7,12,17]`
- Jogging `[2,7,12,17,22,27,32,37,42,47]`

Seattle-selected method/lambda transfer unchanged. No per-sequence tuning. Both held-out sequences must independently pass all locality and reconstruction criteria for primary Step-19 success.

## Frozen ablations

A0 — matched HUGS baseline (`lambda_local=0`, `lbs_w=0`)

A1 — 99%-support-envelope locality regularizer

A2 — direct full-vector K6 MSE matching, secondary only

## Frozen implementation contract

Audited path:

- `hugs/models/hugs_trimlp.py`: learned LBS logits -> `F.softmax(lbs_weights / 0.1, dim=-1)`
- existing deformation consumes those normalized weights
- `hugs/losses/loss.py` receives `human_gs_out['lbs_weights']`
- locality enters `loss_dict['locality'] = lambda_local * L_local`
- existing loss sum, `loss.backward()`, and human optimizer step remain unchanged

A1 must not change softmax temperature, SMPL kinematics, deformation transform semantics, or learned weights after softmax; must not optimize IRDR directly; and must not combine A1 with direct K6 full-vector MSE.

Lambda is constant for the full 30,000-step run; no warmup/annealing.

## Step 19I0 — locality primitive smoke PASS

Implementation worktree:

`/content/ml-hugs-step19-locality-impl`

Branch:

`step19-locality-impl`

Base commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Implementation commit:

`f6065a9ca07a3dac2133f14d9e7f135e7a2c3f87`

Only changed file:

`hugs/losses/locality.py`

Module SHA256:

`b811d2473cff99b56d596e525363f9f95a253bc2bf73da2ad855154273e18caf`

Drive patch:

`private_research/2026-09-17_step19i0_locality_primitive.patch`

Patch SHA256:

`5d341b3f77ae36afc107a749ea823ed16eb7a7a98655451af26823bf2ebee274`

Drive metadata:

`private_research/2026-09-17_step19i0_locality_primitive_smoke.json`

Metadata SHA256:

`25f0b0ce93fe1095f03708c528a3e1e09b9d0236935aeb3ed8afae71066a4745`

Synthetic smoke checks all passed:

1. support-envelope rows nonempty
2. envelope mask bool/binary
3. normalized K6 reference required
4. normalized learned LBS required
5. `L_local >= 0`
6. `lambda_local=0` contribution exactly zero
7. no gradient to K6 reference/mask
8. learned logits receive finite nonzero gradient
9. locality primitive does not modify learned normalized weights
10. no scientific validation/test metric inspected

Observed synthetic `L_local = 0.44640886783599854`; learned-logit gradient absolute sum `0.9585590958595276`; `q_K6.grad = None`.

GitHub session:

`research/sessions/2026-09-17-step19i0-locality-primitive-smoke.md`

Interpretation: implementation validation only, not scientific evidence.

## Frozen preregistration artifacts

Final preregistration Drive file:

`private_research/2026-09-17_step19_preregistration_draft.md`

SHA256:

`6c1f464f36dd3a567464fc091329abf605b2d37e12800a126a55ec35dd0a9b33`

Implementation contract:

`private_research/2026-09-17_step19_frozen_implementation_contract.json`

SHA256:

`255c216f5bc17d8efa0101e3b11fafe5562e2d4d1c18bcbb271fed953d23191c`

Freeze record:

`research/sessions/2026-09-17-step19e1-preregistration-frozen.md`

## Claim status

No scientific claim has changed.

`CL-13` remains `UNTESTED`:

> Anatomical locality can be enforced without sacrificing reconstruction quality.

Do not describe the method as successful before the frozen scientific protocol is executed.

## Exact next action — Step 19I1

Integrate the frozen locality primitive into the actual HUGS model/loss/config path on the isolated implementation branch and run non-scientific integration smoke checks only.

Required I1 checks include:

- K6 reference/envelope can be generated from current canonical Gaussian positions without gradient
- locality term enters existing loss aggregation without changing renderer/LBS transform semantics
- `lambda_local=0` preserves baseline forward/loss behavior
- nonzero locality term sends gradient into actual learned deformation-decoder parameters
- no gradient enters K6 reference/envelope
- do not inspect Seattle validation/test, Parkinglot, or Jogging scientific outcomes

Do not launch the 30,000-step development runs until I1 integration validation is archived as passing.

## Research-record rule

Repository is authoritative. Preserve all failed/successful audits, frozen hashes, implementation commits, and negative results. Never alter the frozen Step-19 thresholds or lambda grid after scientific outcomes are observed.
