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
- Step 16D1 Jogging checkpoint/config provenance and architecture validation
- Step 16D2 Jogging learned-LBS reconstruction and full-batch/chunk audit
- Step 16D3 Jogging subject-specific K=6 target reconstruction and precursor test

## Current strongest causal result

The learned cross-joint left-wrist/left-hand LBS mechanism has been causally reproduced and shown to be pose-stable in **two independently pretrained HUGS NeuMan checkpoints: Seattle and Parkinglot**.

Seattle raw frames `[2,7,12,17]`, `left_wrist z +10 deg`:

```text
mean K6 reduction:             99.8184408838516%
minimum K6 reduction:          99.81753724223914%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9811488931072522
```

Parkinglot raw frames `[2,7,12,17]`, same perturbation:

```text
learned contra % HC range:     3.3925969009792323 to 3.3971048755337407
mean K6 reduction:             99.70879580221536%
minimum K6 reduction:          99.70857508781499%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9975337157455157
```

Parkinglot raw frame 2 also passed the `x/y/z × {-10,+10} deg` direction/sign control:

```text
minimum K6 reduction:                 98.7997086031298%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation:     0.9664424743486758
maximum ablated contralateral sum:    0.0
maximum +/- sign asymmetry:           0.5583232093225667%
AXIS/SIGN ROBUST:                     True
```

Important nuance: the causal pathway is direction robust, but effect magnitude is anisotropic. Do not claim axis-invariant magnitude.

## Jogging status

Jogging is a distinct third independently pretrained checkpoint:

```text
checkpoint SHA256: 7a056fd6ba8ee9f5cc640eac43666e9ab57de33db2062a8ca379d1daa3afa769
Gaussian count:    311723
pose frames:       102
beta drift:        0.0
eval raw frames:   [2,7,12,17,22,27,32,37,42,47]
```

Step 16D2 reconstructed and numerically validated Jogging canonical xyz and learned 24-channel LBS. Full-batch and 65,536-chunk outputs matched exactly.

Step 16D3 reconstructed the Jogging subject-specific HUGS-style K=6 target and passed all numerical and independent-search checks:

```text
K6 TARGET VALID:                  True
max row-sum error:                2.384185791015625e-07
nearest-neighbor exact fraction:  1.0
K=6 neighbor-set exact fraction:  1.0
high-confidence >=0.9:           148392
contralateral HC subset:          20887
```

Learned-vs-K6 anatomy is strongly aligned on K6-HC Gaussians:

```text
overall dominant-joint agreement: 0.9710865094972139
K6-HC dominant-joint agreement:   0.9999258720146639
```

Most important pre-perturbation Jogging result on the fixed 20,887-Gaussian contralateral subset:

```text
K6 left-wrist+hand mean:      2.763716224762902e-07
learned left-wrist+hand mean: 0.00020052377658430487
learned/K6 mean ratio:        725.5584881964779x
K6 max:                       0.00014079449465498328
learned max:                  0.02658037841320038
fraction learned >1e-3:       0.02848661847081917
fraction K6 >1e-3:            0.0
```

This is the same qualitative pre-perturbation cross-joint-support precursor seen in Seattle and Parkinglot. **Jogging is still not a third causal replication** because no Jogging perturbation or selective intervention has been run yet.

## Strongest defensible claim

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding SMPL-derived K=6 target. The mechanism remains stable across four tested evaluation poses in each checkpoint, and in Parkinglot it persists across x/y/z wrist rotations and both perturbation signs. A third independent checkpoint, Jogging, independently exhibits the same pre-perturbation cross-joint support precursor but has not yet undergone the causal perturbation test.

Do not describe this as a universal HUGS failure, an isotropic effect, or a result generalized to all joints or Gaussian-human methods.

## Immediate next experiment

Run **Step 16D4: Jogging raw-frame-2 causal counterfactual**.

Freeze the Jogging K=6-derived masks from Step 16D3 and apply the same `left_wrist z +10 deg` diagnostic used for Seattle and Parkinglot. Compare:

1. original Jogging learned LBS,
2. Jogging subject-specific K=6 target,
3. learned Jogging LBS with only left-wrist/left-hand channels removed on the fixed 20,887-Gaussian high-confidence contralateral subset.

If K6 replacement strongly suppresses the contralateral response and the selective intervention removes it, the mechanism will have a third independent checkpoint-level causal replication.

For continuity, read:

- [Step 16C5 Parkinglot axis/sign robustness](../sessions/2026-09-15-step16c5.md)
- [Step 16D1 Jogging checkpoint readiness](../sessions/2026-09-15-step16d1.md)
- [Step 16D2 Jogging learned-LBS validation](../sessions/2026-09-15-step16d2.md)
- [Step 16D3 Jogging K=6 precursor](../sessions/2026-09-15-step16d3.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [16D3 compact summary](../../experiments/07-cross-sequence-replication/analysis/16D3_jogging_k6_key_summary.csv)
