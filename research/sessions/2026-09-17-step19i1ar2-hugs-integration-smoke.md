# Step 19I1A-R2 — HUGS integration + actual decoder-gradient smoke

Date: 2026-09-17

## Status

`PASS — IMPLEMENTATION SMOKE ONLY`

No scientific training was performed. No Seattle validation/test frame, Parkinglot result, Jogging result, PSNR/SSIM/LPIPS result, or IRDR scientific outcome was inspected.

## Provenance

Frozen HUGS base commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Input Step-19I0 implementation commit:

`f6065a9ca07a3dac2133f14d9e7f135e7a2c3f87`

Output integration commit:

`e68b1b3eeca3cc2229dbc307ec37c78bbc7eb214`

Changed files from I0:

- `hugs/cfg/config.py`
- `hugs/losses/loss.py`
- `hugs/models/hugs_trimlp.py`
- `hugs/trainer/gs_trainer.py`

Frozen locality primitive remained unchanged:

`hugs/losses/locality.py`

SHA256:

`b811d2473cff99b56d596e525363f9f95a253bc2bf73da2ad855154273e18caf`

## Prior non-scientific failures preserved

### 19I1A

The first decoder-gradient smoke attempted normal package import and triggered `hugs.models.__init__ -> SceneGS`, which required unavailable `loguru` in the legacy environment. The locality gradient test had not run.

### 19I1A-R

The recovery verifier incorrectly counted explicit K6 calls as zero because it truncated the `smpl_lbsweight_top_k(...)` source at the first inner `)` from `unsqueeze(0)`.

Neither failure changed source claims or scientific outcomes.

## AST K6 verification

Python AST inspection found exactly two assignments of `gt_lbs_weights` from `smpl_lbsweight_top_k(...)`.

Both calls explicitly contain:

`K=6`

Locations after patch:

- line 318
- line 481

## Frozen source-contract checks

Passed:

- learned LBS normalization remains `F.softmax(lbs_weights/0.1, dim=-1)`
- original `lbs_extra` deformation path remains present
- config default `locality_w = 0.0`
- config default `lbs_w = 0.0`
- `HumanSceneLoss` receives `l_locality_w`
- locality reference uses detached `human_gs_out['gt_lbs_weights']`
- support envelope uses frozen `rho=0.99`
- locality term enters `loss_dict['locality']`
- original `loss.backward()` remains unchanged
- original human optimizer step remains unchanged
- source files compile under the legacy Python/Torch environment

## Actual audited DeformationDecoder gradient smoke

The exact audited `DeformationDecoder` source was loaded directly without executing the full `hugs.models` package initialization.

Synthetic detached K6-like reference was used only for gradient plumbing.

Observed smoke values:

- normalized learned LBS row-sum max error: `1.1920928955078125e-07`
- synthetic q row-sum max error: `0.0`
- allowed joints per row: `3` for all 16 synthetic rows
- `L_local = 0.8710632920265198`
- mean NSM `= 0.8710632920265198`

Nonzero gradients reached the actual audited deformation decoder:

- `net.0.weight = 0.9976804256439209`
- `net.0.bias = 0.030019471421837807`
- `net.2.weight = 1.8229739665985107`
- `net.2.bias = 0.06369362026453018`
- `skinning_linear.weight = 1.8181369304656982`
- `skinning_linear.bias = 0.16747578978538513`
- `skinning.weight = 1.4619622230529785`
- `skinning.bias = 0.3887782096862793`

Required gradient checks passed for `skinning.weight`, `skinning.bias`, and `skinning_linear.weight`.

K6 reference and envelope remained detached. `lambda_local=0` produced exactly zero weighted locality contribution.

## File fingerprints

- `hugs/models/hugs_trimlp.py`: `7e7b56787cc1f9bdc3987c5abec045e900e5c91356af49c3ce59ef3047c81898`
- `hugs/losses/loss.py`: `742adf2bb1a07b222e44e3090778ef053029225657322e3cd1834a5fd111c0d7`
- `hugs/cfg/config.py`: `f81304c17690d5322c625869bc5645e85fc063cf93ebf59726de333edea81a66`
- `hugs/trainer/gs_trainer.py`: `0a23ca8ace58df6f77374800547707a6bfc39869f491b1cff0846b941de989ac`

Drive patch:

`private_research/2026-09-17_step19i1ar2_hugs_integration.patch`

Patch SHA256:

`12299a33c2a3a202eb57d7692fb965b65b087596aa45a2e2c76a960183f31fb0`

Drive metadata:

`private_research/2026-09-17_step19i1ar2_hugs_integration_smoke.json`

Metadata SHA256:

`119816c77dec937fc68390c226d00635e40b4354a7984402e8896e8a41fafd9a`

## Interpretation

This is implementation validation only. It demonstrates that the frozen A1 locality objective can be integrated into the audited HUGS loss graph and that its gradient reaches the actual learned skinning predictor while the anatomical reference remains detached.

It does **not** show that the method reduces anatomical nonlocality, preserves reconstruction quality, or succeeds scientifically.

## Next allowed action

Step 19I1B:

Use exactly one frozen Seattle **training** frame to verify original-vs-patched baseline forward/loss equivalence with locality disabled, then run a locality-enabled graph smoke on that same training frame.

Seattle validation/test frames remain locked. Parkinglot and Jogging remain untouched.
