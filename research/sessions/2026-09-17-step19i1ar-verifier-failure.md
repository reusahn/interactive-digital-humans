# Step 19I1A-R verifier failure

Date: 2026-09-17
Status: IMPLEMENTATION_SMOKE_VERIFIER_FAILURE — NO SCIENTIFIC OUTCOME

## Context

Step 19I1A-R was intended to recover the dirty integration state left by the prior package-import dependency failure and then directly test locality-gradient flow through the audited HUGS `DeformationDecoder`.

The worktree remained at I0 commit:

`f6065a9ca07a3dac2133f14d9e7f135e7a2c3f87`

Observed dirty tracked files were exactly the expected four I1A integration files:

- `hugs/cfg/config.py`
- `hugs/losses/loss.py`
- `hugs/models/hugs_trimlp.py`
- `hugs/trainer/gs_trainer.py`

The only untracked file was the previous failed smoke-test script:

`_step19i1a_decoder_gradient_test.py`

SHA256:

`80f91f98fa820a87db0b4483380e899f5384c98bbeabc3a3593e2704bd193d99`

## Failure

The recovery cell stopped at its explicit-K6 verification before any source commit or scientific computation.

Printed result:

`explicit K=6 reference-call count: 0`

The verifier then asserted `explicit_k6_count >= 2` and stopped.

## Diagnosis

This `0` count is a verifier artifact, not evidence that the source patch lacks `K=6`.

The verifier used:

```python
block.split(")", 1)[0]
```

after splitting on `smpl_lbsweight_top_k(`. The `smpl_lbsweight_top_k` call contains nested expressions such as `gs_xyz.unsqueeze(0)` and `self.vitruvian_verts.unsqueeze(0)`. Therefore the first `)` encountered belongs to an inner `unsqueeze(0)` call and occurs before the later `K=6` keyword. The verifier truncates the call body too early and can falsely report zero explicit-K6 calls.

The prior I1A patcher had already reported that it inserted explicit `K=6` into two `gt_lbs_weights` reference calls. This new failure does not contradict that result; it only shows the recovery verifier was malformed.

## Integrity status

- no new commit created
- dirty source state preserved
- no HUGS training performed
- no Seattle validation/test inspected
- no Parkinglot/Jogging inspected
- no Step-19 scientific outcome observed
- preregistered protocol unchanged

## Next action

Rerun recovery with a structurally correct verifier that parses the Python AST (or tracks parenthesis depth) and checks `smpl_lbsweight_top_k` call nodes assigned to `gt_lbs_weights` for keyword `K=6`.

Only after that verification passes should the direct audited `DeformationDecoder` gradient smoke run and the four-file integration patch be committed.
