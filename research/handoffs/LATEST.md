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
- Step 16C3 parkinglot independent causal counterfactual

Current independent-sequence result: **Parkinglot successfully reproduces the Seattle causal mechanism.**

Parkinglot uses an official checkpoint distinct from Seattle, with SHA256 `f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c`, 614,157 Gaussians, a subject-specific K=6 target, and a fixed pre-displacement high-confidence contralateral subset of 77,622 Gaussians.

Step 16C3 applied the same `left_wrist z +10 deg` perturbation at raw frame 2. Kinematic auditing showed that only SMPL joints 20 and 22, left wrist and descendant left hand, changed transforms. No contralateral joint transform changed.

Primary result:

```text
learned contralateral displacement: 5.416987895965576
K6 contralateral displacement:      0.01578645221889019
selective-ablation contralateral:    0.0

K6 reduction vs learned:             99.70857508781499%
selective-ablation reduction:        100.0%
learned-to-K6 gap closed:            1.0029227667924083
```

Selective intervention changed no learned weights outside the fixed contralateral subset. Removed left-wrist/hand learned mass was strongly associated with displacement reduction:

```text
removed-mass vs reduction correlation: 0.9975359387446432
removed-mass vs learned displacement:   0.9975359387446432
```

The fixed contralateral subset had almost no SMPL-derived wrist/hand support but much larger learned HUGS support:

```text
K6 wrist+hand mean:      2.161917080911735e-07
learned wrist+hand mean: 8.741816418478265e-05
```

Strongest current claim:

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement under a left-wrist z perturbation relative to the corresponding SMPL-derived K=6 target.

Do not generalize this yet to all joints, axes, NeuMan sequences, or Gaussian-human methods. The exact-zero selective-ablation result is structurally expected under pure LBS because the perturbation changes only left-wrist and left-hand transforms. The important evidence is that HUGS learned cross-joint support absent from the target and that this support accounts for the amplified cross-body response in two independent checkpoints.

Authoritative Drive files:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1B_fullbatch_numerical_audit.json
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_manifest.json
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_summary.csv
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_metadata.json
```

Immediate next action: **repeat the same Parkinglot counterfactual at raw evaluation frames `[2, 7, 12, 17]` using the same fixed K=6 anatomical mask.** This tests pose stability inside the second independent checkpoint before moving to a third sequence.

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16C1B full-batch validation](../sessions/2026-09-15-step16c1b.md)
- [Step 16C2 Parkinglot K=6 reconstruction](../sessions/2026-09-15-step16c2.md)
- [Step 16C3 Parkinglot causal replication](../sessions/2026-09-15-step16c3.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [daily research log](../logs/2026-09-15.md)
