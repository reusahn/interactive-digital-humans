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
- Step 16C3 Parkinglot independent causal counterfactual
- Step 16C4 Parkinglot within-checkpoint pose replication
- Step 16C5 Parkinglot axis/sign robustness control

## Current strongest result

The learned cross-joint left-wrist/left-hand LBS mechanism has been causally reproduced and shown to be pose-stable in **two independently pretrained HUGS NeuMan checkpoints: Seattle and Parkinglot**.

Seattle tested raw frames `[2, 7, 12, 17]` under `left_wrist z +10 deg`:

```text
mean K6 reduction:              99.8184408838516%
minimum K6 reduction:           99.81753724223914%
mean selective reduction:       100.0%
mean removed-mass correlation:  0.9811488931072522
```

Parkinglot tested raw frames `[2, 7, 12, 17]` under the same perturbation:

```text
learned contra % HC range:      3.3925969009792323 to 3.3971048755337407
mean K6 reduction:              99.70879580221536%
minimum K6 reduction:           99.70857508781499%
mean selective reduction:       100.0%
mean removed-mass correlation:  0.9975337157455157
```

Step 16C5 additionally tested Parkinglot raw frame 2 across `x/y/z × {-10,+10} deg` while keeping the learned field, K=6 target, anatomical masks, and selective intervention fixed.

```text
minimum K6 reduction:                 98.7997086031298%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation:     0.9664424743486758
maximum ablated contralateral sum:    0.0
maximum +/- sign asymmetry:           0.5583232093225667%
AXIS/SIGN ROBUST:                     True
```

Important nuance: the causal pathway is direction robust, but response magnitude is not isotropic. The x-axis learned contralateral response is much smaller (`~0.315-0.317`, about `0.33%` of HC displacement) than the y/z responses (`~5.415-5.417`, about `3.4-3.8%` of HC displacement). Do not claim axis-invariant magnitude.

At every Parkinglot perturbation tested so far, kinematic auditing shows only SMPL transforms `[20,22]` change, corresponding to left wrist and descendant left hand. No contralateral transform changes.

## Strongest defensible claim

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding SMPL-derived K=6 target. The mechanism remains stable across four tested evaluation poses in each checkpoint, and in Parkinglot it persists across x/y/z wrist rotations and both perturbation signs.

Do not describe this as a universal HUGS failure, an isotropic effect, or a result generalized to all joints or Gaussian-human methods.

## Authoritative recent Drive outputs

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C5_parkinglot_axis_sign_displacements.npz
```

## Immediate next experiment

Proceed to a third independently pretrained sequence: **Jogging**.

Reason: the 102-frame dynamic sequence provides more sequence/pose diversity than Citron while using a distinct pretrained HUGS model. First extract and verify only Jogging's official `human_final.pth` and `config_train.yaml`, checkpoint SHA256, Gaussian count, packaged config, and architecture. Stop before learned-LBS reconstruction if any provenance or architecture mismatch appears.

For continuity, read:

- [Step 16C4 Parkinglot pose replication](../sessions/2026-09-15-step16c4.md)
- [Step 16C5 Parkinglot axis/sign robustness](../sessions/2026-09-15-step16c5.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [16C5 compact CSV](../../experiments/07-cross-sequence-replication/analysis/16C5_parkinglot_axis_sign_robustness.csv)
- [daily research log](../logs/2026-09-15.md)
