# Step 19 — Pre-outcome release-config discrepancy discovered

Date: 2026-09-17

## Status

`BLOCKING PROTOCOL PROVENANCE ISSUE — NO SCIENTIFIC OUTCOME OBSERVED`

Step 19 scientific training has not started. No Seattle validation/test, Parkinglot, Jogging, PSNR/SSIM/LPIPS, or IRDR method outcome has been observed.

## Discovery

While preparing Step 19I1B baseline-equivalence testing against the exact audited HUGS source commit, the actual release NeuMan configuration was re-read from:

`cfg_files/release/neuman/hugs_human_scene.yaml`

at HUGS commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

The release file contains:

- `train.num_steps: 14998`
- `human.loss.lbs_w: 1000.0`

The previously frozen Step-19 preregistration instead described the released NeuMan configuration while simultaneously freezing:

- final checkpoint / training length `30000`
- primary matched baseline `lbs_w = 0`

These statements are inconsistent with the actual audited release configuration.

## Why this matters

The Step-18 diagnosis was performed on released pretrained HUGS/NeuMan checkpoints. The published/released NeuMan recipe already uses direct full-vector K6-style LBS MSE regularization with a large fixed coefficient (`lbs_w=1000`). Therefore a Step-19 comparison that calls `lbs_w=0` the released HUGS baseline would be factually incorrect.

The discrepancy was discovered before any Step-19 scientific model training or method outcome. It is therefore a protocol/provenance correction problem, not post-result retuning.

## Required action

Do not begin Step 19I1B scientific-frame equivalence or any 30k training under the inconsistent protocol.

Create a non-destructive pre-outcome preregistration erratum that preserves the original frozen file/hash and supersedes only the affected release-configuration/baseline/ablation fields. Thresholds, splits, lambda grid, held-out rules, and anti-retuning rules should remain unchanged unless independently required by the source correction.

A scientifically coherent corrected design should treat the actual released HUGS recipe as the primary A0 baseline and distinguish the mechanism-aware support-envelope replacement from a no-skinning-prior ablation.

## Claim status

No claim status changes.

`CL-13` remains `UNTESTED`.
