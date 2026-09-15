# Experiment 07 - Cross-Sequence Replication

## Goal

Test whether the learned cross-joint LBS mechanism identified in the pretrained HUGS NeuMan Seattle model also appears in independently pretrained HUGS sequences and remains robust across base pose and perturbation direction.

## Step 16A - persistent asset inventory

Official pretrained HUGS archive in Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/assets/hugs/downloads/hugs_pretrained_models.zip
```

Archive size: approximately `2094.11 MiB`.

The archive contains official pretrained `human_final.pth`, `config_train.yaml`, and `scene_final.pth` entries for `citron`, `parkinglot`, `jogging`, `lab`, and `bike`.

## Step 16B1 - official NeuMan archive probe

The official NeuMan archive supports HTTP byte ranges:

```text
HTTP status: 206
Content-Range: bytes 0-0/4513980377
Accept-Ranges: bytes
Archive size: 4.204 GiB
```

The full archive was not downloaded.

## Step 16B2 - selective pose extraction

Only the five candidate `smpl_optimized_aligned_scale.npz` files were selectively extracted from the remote archive. Parkinglot has 42 frames and evaluation raw-frame indices `[2, 7, 12, 17]`.

## Step 16B3 - Parkinglot checkpoint provenance

```text
checkpoint SHA256: f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c
Gaussian count: 614157
pose frames: 42
```

The Parkinglot checkpoint is independent from Seattle while using the same core triplane/deformation architecture and 24-channel learned skinning output.

## Steps 16C0-16C1B - learned-LBS reconstruction

Official Apple HUGS source commit:

```text
86ebe5522a384fc553f07f090b63a76dd4af8d33
```

Parkinglot checkpoint states strict-loaded successfully. Canonical Gaussian positions and learned 24-channel LBS were reconstructed through the checkpoint forward path.

```text
FULL-BATCH FORWARD VALID: True
CHUNK SEMANTIC STABILITY: True
STEP 16C1B AUDIT PASS: True
full vs chunk canonical xyz difference: 0
full vs chunk learned LBS difference: 0
```

## Step 16C2 - Parkinglot-specific K=6 target

The subject-specific SMPL Vitruvian template was reconstructed from Parkinglot betas and the exact HUGS top-K rule was applied:

```text
K = 6
LBS consistency gate: exp(-L1 / 0.02) > 0.9
spatial weighting: exp(-squared_distance)
```

Validation:

```text
K6 TARGET VALID: True
max row-sum error: 2.384185791015625e-07
nearest-neighbor exact audit: 1.0
K=6 neighbor-set exact audit: 1.0
```

At K=6 confidence >=0.9:

```text
high-confidence: 292095
intended left wrist + hand: 2946
same-side local chain: 33764
nonlocal: 255385
contralateral upper body: 77622
```

Pre-perturbation precursor on the fixed contralateral subset:

```text
K6 wrist+hand mean:      2.161917080911735e-07
learned wrist+hand mean: 8.741816418478265e-05
learned/K6 mean ratio:   404.3548430077448x
```

## Step 16C3 - independent Parkinglot causal replication

At raw frame 2, the same `left_wrist z +10 deg` diagnostic used for Seattle was applied with masks fixed before displacement.

Kinematic audit:

```text
changed SMPL transforms: [20, 22]
unexpected changed transforms: []
```

Primary result:

```text
learned contralateral:             5.416987895965576
K6 contralateral:                  0.01578645221889019
selective-ablation contralateral:  0.0
K6 reduction vs learned:           99.70857508781499%
selective-ablation reduction:      100.0%
removed-mass vs reduction r:       0.9975359387446432
```

This causally reproduced the Seattle mechanism in a second independently pretrained checkpoint.

## Step 16C4 - Parkinglot pose replication

The same causal test was repeated at Parkinglot raw frames `[2, 7, 12, 17]` with the learned field, K=6 target, masks, selective-ablation definition, and `left_wrist z +10 deg` perturbation fixed.

| Raw frame | Learned contra | K6 contra | Ablated contra | Learned contra % HC | K6 reduction | Ablation reduction | Removed-mass vs reduction r |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 5.416988 | 0.015786 | 0.0 | 3.397105 | 99.708575% | 100.0% | 0.997536 |
| 7 | 5.089294 | 0.014824 | 0.0 | 3.392597 | 99.708726% | 100.0% | 0.997517 |
| 12 | 4.965871 | 0.014452 | 0.0 | 3.393532 | 99.708968% | 100.0% | 0.997529 |
| 17 | 5.037852 | 0.014665 | 0.0 | 3.394680 | 99.708913% | 100.0% | 0.997552 |

Across-frame aggregate:

```text
learned contra % HC range:         3.3925969009792323 to 3.3971048755337407
mean K6 reduction:                 99.70879580221536%
minimum K6 reduction:              99.70857508781499%
mean selective reduction:          100.0%
minimum selective reduction:       100.0%
mean removed-mass correlation:     0.9975337157455157
```

Compact artifact: [16C4 frame replication CSV](analysis/16C4_parkinglot_frame_replication.csv).

## Step 16C5 - Parkinglot axis/sign robustness

At raw frame 2, the fixed Parkinglot learned field, K=6 target, anatomical mask, and selective ablation were tested with `left_wrist` rotations around x, y, and z at both `-10 deg` and `+10 deg`.

Every perturbation changed only SMPL transforms `[20, 22]`, left wrist and descendant left hand.

| Axis | Deg | Learned contra | K6 contra | Ablated contra | Learned contra % HC | K6 reduction | Ablation reduction | Removed-mass vs reduction r |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| x | -10 | 0.317063 | 0.003806 | 0.0 | 0.331653 | 98.799709% | 100.0% | 0.966442 |
| x | +10 | 0.315298 | 0.003772 | 0.0 | 0.330131 | 98.803607% | 100.0% | 0.967749 |
| y | -10 | 5.416648 | 0.015552 | 0.0 | 3.800179 | 99.712887% | 100.0% | 0.997633 |
| y | +10 | 5.416755 | 0.015529 | 0.0 | 3.805536 | 99.713318% | 100.0% | 0.997628 |
| z | -10 | 5.415346 | 0.015779 | 0.0 | 3.396430 | 99.708633% | 100.0% | 0.997528 |
| z | +10 | 5.416988 | 0.015786 | 0.0 | 3.397105 | 99.708575% | 100.0% | 0.997536 |

Aggregate:

```text
minimum K6 reduction:                 98.7997086031298%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation:     0.9664424743486758
maximum ablated contralateral sum:    0.0
maximum +/- sign asymmetry:           0.5583232093225667%
AXIS/SIGN ROBUST:                     True
```

The mechanism is therefore robust to the tested rotation axis and sign in Parkinglot, but the effect magnitude is anisotropic. The x-axis response is roughly an order of magnitude smaller than the y/z response. The correct claim is causal pathway robustness, not axis-invariant magnitude.

Compact artifact: [16C5 axis/sign robustness CSV](analysis/16C5_parkinglot_axis_sign_robustness.csv).

Authoritative large outputs remain in Drive under `experiments/07-cross-sequence-replication/`.

## Current interpretation

The same learned cross-joint left-wrist/hand LBS mechanism is causally observed and pose-stable in two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot. In Parkinglot, the pathway is also robust across x/y/z left-wrist rotations and both signs, although its magnitude is strongly axis-dependent.

Strongest defensible claim:

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding SMPL-derived K=6 target. The mechanism remains stable across four tested evaluation poses in each checkpoint, and in Parkinglot it persists across x/y/z wrist rotations and both perturbation signs.

Do not describe the effect as isotropic and do not yet generalize to all HUGS checkpoints, joints, axes, or Gaussian-human methods.

## Next step

Proceed to a third independent checkpoint. Use **jogging** as the next candidate because its 102-frame dynamic sequence provides stronger sequence/pose diversity than the short Citron sequence. First extract and verify only the official Jogging `human_final.pth` and `config_train.yaml`, checkpoint SHA256, Gaussian count, and architecture before reconstructing learned LBS or K=6 targets.
