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
- Step 16C1 / 16C1B parkinglot canonical forward and learned-LBS validation

Current independent-sequence choice: **parkinglot**.

Parkinglot has an official independent checkpoint with SHA256 `f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c`, 614,157 Gaussians, the same core triplane/deformation architecture as Seattle, and a verified 42-frame NeuMan pose asset.

Step 16C1 strict-loaded all Parkinglot checkpoint states and reconstructed canonical xyz plus learned 24-channel LBS over all 614,157 Gaussians. A temporary cross-batch audit discrepancy appeared only when rerunning 4,096 points with a different CUDA batch shape.

Step 16C1B then executed the actual HUGS-style all-Gaussian forward in one batch. The full-batch result and the earlier 65,536-chunk pass were exactly identical for canonical xyz, learned LBS, geometry-offset norms, dominant joints, high-confidence masks, and left-wrist/hand channels. Full-batch outputs were finite and the maximum LBS row-sum error was `3.5762786865234375e-07`.

Final status:

```text
FULL-BATCH FORWARD VALID: True
CHUNK SEMANTIC STABILITY: True
STEP 16C1B AUDIT PASS: True
high-confidence count: 290822
dominant-joint mismatch: 0
high-confidence mask mismatch: 0
```

Authoritative Drive files:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1B_fullbatch_numerical_audit.json
```

Immediate next experiment: **construct the Parkinglot-specific SMPL-derived K=6 target using the Parkinglot shape parameters and the same HUGS top-K weighting rule used for Seattle. Validate K=6 row sums, nearest anatomical assignment, and target-vs-learned basic statistics before any perturbation or ablation.**

Do not generalize the Seattle causal result to Parkinglot or HUGS as a method until the independent Parkinglot perturbation/counterfactual is completed.

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16B2 session checkpoint](../sessions/2026-09-15-step16b2.md)
- [Step 16B3 session checkpoint](../sessions/2026-09-15-step16b3.md)
- [Step 16C0B lightweight loader validation](../sessions/2026-09-15-step16c0b.md)
- [Step 16C1 numerical audit](../sessions/2026-09-15-step16c1-numerical-audit.md)
- [Step 16C1B full-batch validation](../sessions/2026-09-15-step16c1b.md)
- [daily research log](../logs/2026-09-15.md)
