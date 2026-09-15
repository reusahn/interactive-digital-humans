# Latest Research Handoff

Current continuation document:

- [2026-09-15](2026-09-15.md)

Completed today:

- Step 14 corrected Seattle counterfactual LBS ablation
- Step 15 Seattle within-sequence frame replication
- Step 16A cross-sequence asset inventory
- Step 16B1 official NeuMan archive range probe
- Step 16B2 selective extraction of candidate NeuMan pose assets
- Step 16B3 Parkinglot checkpoint/config provenance validation
- Step 16C0 / 16C0B HUGS source restoration and lightweight module loading
- Step 16C1 / 16C1B Parkinglot learned-LBS forward reconstruction and numerical audit
- Step 16C2 Parkinglot-specific SMPL K=6 target reconstruction
- Step 16C3 first independent Parkinglot causal counterfactual
- Step 16C4 Parkinglot within-checkpoint pose replication

## Current strongest result

The learned cross-joint left-wrist/left-hand LBS mechanism has now been causally reproduced and shown to be pose-stable in **two independently pretrained HUGS NeuMan checkpoints: Seattle and Parkinglot**.

### Seattle

Four tested raw evaluation frames: `[2, 7, 12, 17]`.

```text
learned contralateral range: 4.096565 to 4.272963
mean K6 reduction:           99.8184408838516%
minimum K6 reduction:        99.81753724223914%
mean selective reduction:    100.0%
minimum selective reduction: 100.0%
mean removed-mass correlation: 0.9811488931072522
```

### Parkinglot

Independent checkpoint SHA256:

```text
f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c
```

Parkinglot has 614,157 Gaussians and a separately reconstructed subject-specific SMPL-derived K=6 target. The fixed high-confidence contralateral upper-body subset contains 77,622 Gaussians.

Four tested raw evaluation frames: `[2, 7, 12, 17]`.

```text
learned contralateral range:       4.965871334075928 to 5.416987895965576
learned contralateral % HC range:  3.3925969009792323 to 3.3971048755337407
mean K6 reduction:                 99.70879580221536%
minimum K6 reduction:              99.70857508781499%
mean selective reduction:          100.0%
minimum selective reduction:       100.0%
mean removed-mass correlation:     0.9975337157455157
```

At every Parkinglot frame, the kinematic audit showed only SMPL transforms `[20, 22]` changed under the `left_wrist z +10 deg` perturbation, corresponding to left wrist and descendant left hand. No contralateral joint transform changed.

Selective removal of learned left-wrist/left-hand channels only on the pre-defined contralateral subset reduced contralateral displacement to exactly zero at all four Parkinglot frames. Replacing the learned field with the SMPL-derived K=6 target reduced that response by approximately 99.71% at every tested frame.

The `fraction displacement reduced` metric is below 1 in Parkinglot because it uses the strict criterion `delta > 0`; Gaussians that already had exactly zero learned displacement are not counted as reduced. This does not conflict with the ablated contralateral displacement sum being exactly zero.

## Strongest defensible claim

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement under a left-wrist z perturbation relative to the corresponding SMPL-derived K=6 target, and the mechanism remains stable across four tested evaluation poses in each checkpoint.

Do not yet describe this as a universal HUGS failure. Evidence remains bounded to two checkpoints, one joint, and the tested perturbation axis/family.

## Authoritative recent Drive outputs

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication.csv
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication_metadata.json
```

## Immediate next experiment

Run a Parkinglot perturbation-direction robustness test at raw frame 2 with the same fixed learned field, K=6 target, anatomical mask, and selective ablation. Compare `left_wrist +10 deg` around x, y, and z.

Reason: two independent checkpoints already support the z-axis mechanism. The highest-value next control is to rule out that the causal result is a peculiarity of the originally chosen z rotation before spending time reconstructing a third full checkpoint. If the mechanism is preserved across x/y/z, proceed to a third independent sequence such as `jogging`.

For continuity, read:

- [Step 16C3 independent causal replication](../sessions/2026-09-15-step16c3.md)
- [Step 16C4 Parkinglot pose replication](../sessions/2026-09-15-step16c4.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [daily research log](../logs/2026-09-15.md)
