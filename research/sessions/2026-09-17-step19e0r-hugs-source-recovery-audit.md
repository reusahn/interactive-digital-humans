# Step 19E0R — Exact HUGS Source Recovery + Read-Only Audit

Date: 2026-09-17
Status: COMPLETE — READ-ONLY SOURCE AUDIT

## Purpose

Recover the exact HUGS source revision previously audited during Step 18 and identify the code path needed to freeze the Step-19 locality-regularizer implementation contract. No source modification, method implementation, training, or Step-19 outcome observation occurred.

## Source provenance

Official repository:

`https://github.com/apple/ml-hugs.git`

Isolated audit checkout:

`/content/ml-hugs-audit-86ebe552`

Expected and recovered HEAD:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Working tree: clean.

Recovery audit artifact:

`/content/drive/MyDrive/interactive-digital-humans/private_research/2026-09-17_step19e0r_hugs_source_recovery_audit.json`

SHA256:

`1f81177e924b956e6c8455faad8a0e386d3dcba8ceeee5d1b2fffcfd47725dbb`

The earlier failed E0 audit remains preserved separately.

## Learned LBS production

Primary HUGS TRIMLP source:

`hugs/models/hugs_trimlp.py`

File SHA256:

`c64a0ac266dc1b9946d88231c44ae50ed85d0d2556392285f4ee18eb49a9ffff`

Canonical learned LBS path:

```text
deformation_out = self.deformation_dec(tri_feats)
lbs_weights = deformation_out['lbs_weights']
lbs_weights = F.softmax(lbs_weights/0.1, dim=-1)
```

The normalized learned weights are therefore available immediately after the frozen temperature-softmax and are returned in the canonical-forward output as `lbs_weights`.

## Deformation consumption

The normalized learned weights are passed to `lbs_extra` in `hugs/models/hugs_trimlp.py` and contribute to the LBS transform used to deform Gaussian positions and rotations.

Relevant audited path:

```text
A_t2pose = smpl_output.A[0]
A_vitruvian2pose = A_t2pose @ self.inv_A_t2vitruvian
deformed_xyz, _, lbs_T, _, _ = lbs_extra(
    A_vitruvian2pose[None], gs_xyz[None], posedirs, lbs_weights,
    smpl_output.full_pose, ...
)
```

This matches the deformation semantics audited during Step 18.

## Existing anatomical reference path

The HUGS forward path already computes an SMPL-derived LBS reference under `torch.no_grad()` via `smpl_lbsweight_top_k`, using canonical Gaussian locations and the vitruvian SMPL template. Step 19 must explicitly request `K=6` when constructing the frozen locality reference so it matches the Step-18 K6 definition rather than relying on an implicit default.

## Existing LBS loss hook

`hugs/losses/loss.py`

File SHA256:

`deb6ead8c77b93649d6ae325b08c2f5b1a8a2c6c8b0a23b21156ae86c989737f`

The current loss function already receives `human_gs_out['lbs_weights']` and optionally compares it to `human_gs_out['gt_lbs_weights']` through an MSE LBS loss. The global loss is assembled by summing `loss_dict` entries.

Relevant existing path:

```text
if self.l_lbs_w > 0.0 and human_gs_out['lbs_weights'] is not None ...:
    ...
    loss_dict['lbs'] = self.l_lbs_w * loss_lbs

loss = 0.0
for k, v in loss_dict.items():
    loss += v
```

This provides a natural loss-level integration point for the new locality term without modifying the renderer or LBS deformation equation.

## Trainer / gradient path

`hugs/trainer/gs_trainer.py`

File SHA256:

`11004cff2d8c962fda48d46d512f987b3fd0a28cfc1671020723d2167aebd6a8`

The trainer obtains the total loss from `self.loss_fn(...)`, executes `loss.backward()`, and then steps the human optimizer:

```text
loss, loss_dict, loss_extras = self.loss_fn(...)
loss.backward()
...
self.human_gs.optimizer.step()
self.human_gs.optimizer.zero_grad(set_to_none=True)
```

Therefore a locality loss built directly from the normalized `human_gs_out['lbs_weights']` tensor can propagate gradient to the learned deformation predictor through the existing training graph.

## Evaluation path confirmation

The audited trainer computes human-region PSNR, SSIM, and LPIPS on the rectangular human crop using `data['bbox']`, consistent with the Step-19C frozen evaluation protocol.

## Step-19 implication

The final implementation contract should:

1. leave the frozen temperature-softmax and deformation semantics unchanged;
2. derive the anatomical reference independently under `torch.no_grad()` from the canonical geometry and explicit K6 SMPL mapping;
3. create a 99%-mass support-envelope mask from that reference;
4. apply the locality penalty to normalized learned LBS mass outside that mask;
5. add the weighted locality term through the existing loss dictionary before the unchanged `loss.backward()` call;
6. keep the baseline condition exactly equivalent to the original source when `lambda_local = 0`.

## Integrity statement

No HUGS source modification performed.
No method implemented.
No model training performed.
No Step-19 method outcome observed.
