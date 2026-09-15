# Experiment 07 - Cross-Sequence Replication

## Goal

Test whether the learned cross-joint LBS mechanism identified in the pretrained HUGS NeuMan Seattle model also appears in an independently pretrained HUGS sequence.

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

Authoritative arrays remain in Drive.

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

At all four frames, only SMPL transforms `[20, 22]` changed.

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

Authoritative large outputs:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication.csv
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C4_parkinglot_frame_replication_metadata.json
```

## Current interpretation

The same learned cross-joint left-wrist/hand LBS mechanism is now causally observed and pose-stable in two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, across four tested evaluation poses per checkpoint.

Strongest defensible claim:

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement under a left-wrist z perturbation relative to the corresponding SMPL-derived K=6 target, and the mechanism remains stable across four tested evaluation poses in each checkpoint.

This is not yet a universal claim about HUGS. Evidence remains bounded to two checkpoints, one joint, and the tested perturbation axis/family.

## Next step

Before reconstructing a third full checkpoint, run a perturbation-direction robustness control on Parkinglot raw frame 2 using the same fixed learned field, K=6 target, anatomical mask, and selective ablation. Compare left-wrist rotations about x, y, and z, ideally with both signs at the same magnitude. If the mechanism is direction/sign robust, proceed to a third independent sequence such as `jogging`.
