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
- Step 16C0B lightweight HUGS module loading validation

Current independent-sequence choice: **parkinglot**.

Parkinglot has an official independent checkpoint with SHA256 `f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c`, 614,157 Gaussians, the same core triplane/deformation architecture as Seattle, and a verified 42-frame NeuMan pose asset.

Step 16C1 strict-loaded all Parkinglot checkpoint states and completed a chunked canonical forward over all 614,157 Gaussians. Outputs were finite and learned LBS row sums were valid to float32 precision. The only failed criterion was an overly strict cross-batch CUDA reproducibility test: rerunning the first 4,096 points as a different batch size produced canonical-XYZ max difference `5.96e-8` and learned-LBS max difference `3.9041e-6`, exceeding the temporary `1e-7` LBS threshold. Raw arrays were therefore not yet archived as authoritative.

This is being treated as a numerical audit issue rather than a scientific/checkpoint failure. The actual HUGS `canon_forward()` processes the complete Gaussian tensor in one call, so the immediate next action is **Step 16C1B - run a full-batch Parkinglot canonical forward matching the original HUGS call shape, compare it with the chunked approximation, audit anatomical stability, and only then save authoritative learned-LBS arrays.**

Do not build the Parkinglot K=6 target until Step 16C1B is reviewed.

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16B2 session checkpoint](../sessions/2026-09-15-step16b2.md)
- [Step 16B3 session checkpoint](../sessions/2026-09-15-step16b3.md)
- [Step 16C1 source-tree blocker](../sessions/2026-09-15-step16c1-source-missing.md)
- [Step 16C0 import blocker](../sessions/2026-09-15-step16c0-import-blocker.md)
- [Step 16C0B lightweight loader validation](../sessions/2026-09-15-step16c0b.md)
- [Step 16C1 numerical audit](../sessions/2026-09-15-step16c1-numerical-audit.md)
- [daily research log](../logs/2026-09-15.md)
