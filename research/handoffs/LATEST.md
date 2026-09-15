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
- Step 16C2 parkinglot-specific SMPL K=6 target reconstruction

Current independent-sequence choice: **parkinglot**.

Parkinglot uses an official checkpoint distinct from Seattle, with SHA256 `f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c`, 614,157 Gaussians, 42 NeuMan pose frames, and the same core learned deformation architecture.

Step 16C1B established an authoritative Parkinglot learned-LBS export. The all-Gaussian HUGS-style full-batch forward and the earlier 65,536-chunk pass were exactly identical for canonical xyz, learned LBS, geometry offsets, dominant joints, high-confidence masks, and left-wrist/hand channels.

Step 16C2 independently reconstructed the Parkinglot subject-specific SMPL-derived K=6 target using the HUGS top-K rule. It passed row-sum and independent brute-force KNN validation:

```text
K6 TARGET VALID: True
max row-sum error: 2.384185791015625e-07
nearest-neighbor exact fraction: 1.0
K=6 neighbor-set exact fraction: 1.0
```

At K=6 confidence >=0.9:

```text
high-confidence Gaussians: 292095
intended left wrist + hand: 2946
same-side local chain: 33764
nonlocal: 255385
contralateral upper body: 77622
```

Learned-vs-K6 anatomical agreement is high:

```text
overall dominant-joint agreement: 0.9888562696509199
K6-HC dominant-joint agreement: 0.9999315291257981
```

Most important pre-perturbation result on the fixed 77,622-Gaussian contralateral subset:

```text
K6 left-wrist+hand mean weight:      2.161917080911735e-07
learned left-wrist+hand mean weight: 8.741816418478265e-05
learned/K6 mean ratio:               404.3548430077448x
K6 max:                              0.00014079449465498328
learned max:                         0.248804971575737
```

Interpretation: a second independently pretrained HUGS checkpoint shows the same qualitative learned cross-joint support precursor identified in Seattle. This is not yet a causal replication because no Parkinglot wrist perturbation has been applied.

Authoritative Drive files:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1B_fullbatch_numerical_audit.json
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_manifest.json
```

Immediate next action: **run one Parkinglot raw-frame-2 `left_wrist z +10 deg` causal diagnostic using the fixed K=6-derived anatomical mask and compare learned LBS, K=6 target, and selective learned wrist/hand-channel ablation on the 77,622 high-confidence contralateral Gaussians.**

Do not generalize to HUGS as a method until the Parkinglot displacement/counterfactual result is known.

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16C1B full-batch validation](../sessions/2026-09-15-step16c1b.md)
- [Step 16C2 Parkinglot K=6 reconstruction](../sessions/2026-09-15-step16c2.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [daily research log](../logs/2026-09-15.md)
