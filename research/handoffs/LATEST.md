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

Next experiment: **Step 16C1 - reconstruct parkinglot canonical Gaussian positions and learned 24-channel LBS weights directly from the official checkpoint.** Validate finiteness, dimensions, and LBS row sums before constructing the parkinglot K=6 target or running any causal ablation.

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16B2 session checkpoint](../sessions/2026-09-15-step16b2.md)
- [Step 16B3 session checkpoint](../sessions/2026-09-15-step16b3.md)
- [daily research log](../logs/2026-09-15.md)
