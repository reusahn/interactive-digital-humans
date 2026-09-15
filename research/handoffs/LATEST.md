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
- Step 16C0 official Apple HUGS source restoration

Current independent-sequence choice: **parkinglot**.

Parkinglot has an official independent checkpoint with SHA256 `f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c`, 614,157 Gaussians, the same core triplane/deformation architecture as Seattle, and a verified 42-frame NeuMan pose asset.

Step 16C0 successfully restored the official source tree at `/content/ml-hugs` with HEAD `86ebe5522a384fc553f07f090b63a76dd4af8d33`. Required module files exist. The import test then stopped because `hugs.models.__init__` pulled in runtime dependencies and `loguru` was missing. No Parkinglot forward reconstruction was attempted.

Immediate next action: **load only `activation.py`, `triplane.py`, and `decoders.py` through a lightweight import path that bypasses `hugs.models.__init__`, verify the three required classes, then rerun Step 16C1.**

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16B2 session checkpoint](../sessions/2026-09-15-step16b2.md)
- [Step 16B3 session checkpoint](../sessions/2026-09-15-step16b3.md)
- [Step 16C1 source-tree blocker](../sessions/2026-09-15-step16c1-source-missing.md)
- [Step 16C0 import blocker](../sessions/2026-09-15-step16c0-import-blocker.md)
- [daily research log](../logs/2026-09-15.md)
