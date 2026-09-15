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

## Current strongest result

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

Parkinglot raw frame 2 additionally passed `x/y/z × {-10,+10} deg` direction/sign control:

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

Step 16D2 reconstructed the Jogging canonical Gaussian positions and learned 24-channel LBS from the official checkpoint using HUGS source commit `86ebe5522a384fc553f07f090b63a76dd4af8d33`.

```text
xyz_canon shape:              (311723, 3)
learned_lbs shape:            (311723, 24)
max LBS row-sum error:        3.5762786865234375e-07
high-confidence >=0.9:       140755
high-confidence fraction:    0.4515387058381961
FULL-BATCH FORWARD VALID:     True
CHUNK SEMANTIC STABILITY:     True
STEP 16D2 AUDIT PASS:         True
```

The 65,536-point chunk reconstruction matched the full-batch result exactly. Dominant-joint mismatch and HC-mask mismatch counts were both zero.

Do **not** count Jogging as a third mechanism replication yet. No Jogging K=6 target or causal perturbation exists yet.

## Strongest defensible claim

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding SMPL-derived K=6 target. The mechanism remains stable across four tested evaluation poses in each checkpoint, and in Parkinglot it persists across x/y/z wrist rotations and both perturbation signs.

## Immediate next experiment

Run **Step 16D3: Jogging subject-specific SMPL K=6 target reconstruction**.

Use Jogging's constant betas and the authoritative `16D2_jogging_learned_lbs.npz`. Reconstruct the HUGS top-K target with:

```text
K = 6
LBS consistency gate = exp(-L1 / 0.02) > 0.9
spatial weight = exp(-squared_distance)
```

Validate K=6 row sums and an independent brute-force KNN audit, define the K=6 high-confidence anatomical masks, then inspect learned-vs-K=6 left-wrist/hand support on the fixed contralateral subset before applying any pose perturbation.

For continuity, read:

- [Step 16C5 Parkinglot axis/sign robustness](../sessions/2026-09-15-step16c5.md)
- [Step 16D1 Jogging checkpoint readiness](../sessions/2026-09-15-step16d1.md)
- [Step 16D2 Jogging learned-LBS validation](../sessions/2026-09-15-step16d2.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [16D2 compact audit](../../experiments/07-cross-sequence-replication/analysis/16D2_jogging_learned_lbs_audit.json)
