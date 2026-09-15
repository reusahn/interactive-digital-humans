# Latest Research Handoff

Current continuation document:

- [2026-09-15](2026-09-15.md)

Completed today:

- Step 14 corrected counterfactual LBS ablation
- Step 15 Seattle within-sequence pose replication
- Step 16A cross-sequence asset inventory
- Step 16B1 official NeuMan archive range probe
- Step 16B2 selective extraction of five candidate NeuMan SMPL pose assets
- Step 16B3 parkinglot checkpoint/config provenance and architecture validation

Current independent-sequence choice: **parkinglot**.

Parkinglot has an official independent checkpoint with SHA256 `f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c`, 614,157 Gaussians, the same core triplane/deformation architecture as Seattle, and a verified 42-frame NeuMan pose asset.

Step 16C1 was attempted but stopped before any reconstruction because the current Colab runtime no longer contains the HUGS source tree. `HUGS source root: None` was returned for both `/content/ml-hugs` and `/content/apple-ml-hugs`. This is an environment persistence issue, not a scientific/checkpoint failure.

Immediate next action: **restore the official Apple HUGS source tree at `/content/ml-hugs` and verify `hugs/models/modules/triplane.py` plus `hugs/models/modules/decoders.py` before rerunning Step 16C1.**

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16B2 session checkpoint](../sessions/2026-09-15-step16b2.md)
- [Step 16B3 session checkpoint](../sessions/2026-09-15-step16b3.md)
- [Step 16C1 source-tree blocker](../sessions/2026-09-15-step16c1-source-missing.md)
- [daily research log](../logs/2026-09-15.md)
