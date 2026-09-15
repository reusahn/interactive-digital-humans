# Experiment 07 - Cross-Sequence Replication

## Goal

Test whether the learned cross-joint LBS mechanism identified in the pretrained HUGS NeuMan Seattle model also appears in an independently pretrained HUGS sequence.

## Step 16A - persistent asset inventory

Official pretrained HUGS archive in Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/assets/hugs/downloads/hugs_pretrained_models.zip
```

Archive size: approximately `2094.11 MiB`.

The archive contains official pretrained `human_final.pth`, `config_train.yaml`, and `scene_final.pth` entries for:

- citron
- parkinglot
- jogging
- lab
- bike

Only Seattle was initially extracted persistently under:

```text
/content/drive/MyDrive/interactive-digital-humans/assets/hugs/pretrained_models/
```

### Readiness before NeuMan pose extraction

| Sequence | HUGS checkpoint | HUGS config | NeuMan SMPL pose asset | Ready for mechanism replication |
|---|---|---|---|---|
| citron | available in official ZIP | available in official ZIP | missing | no |
| parkinglot | available in official ZIP | available in official ZIP | missing | no |
| jogging | available in official ZIP | available in official ZIP | missing | no |
| lab | available in official ZIP | available in official ZIP | missing | no |
| bike | available in official ZIP | available in official ZIP | missing | no |

## Step 16B1 - official NeuMan archive probe

Official archive:

```text
https://docs-assets.developer.apple.com/ml-research/models/hugs/neuman_data.zip
```

The archive was probed without downloading it.

```text
HTTP status: 206
Content-Range: bytes 0-0/4513980377
Accept-Ranges: bytes
Content-Type: application/zip
Archive size: 4.204 GiB (4304.9 MiB)
```

Random byte-range access is available. The full archive was not stored in Drive.

See [the Step 16B1 archive probe record](analysis/16B1_official_neuman_archive_probe.md).

## Step 16B2 - selective NeuMan pose extraction

The official 4.2 GiB NeuMan archive was opened through a seekable HTTP range-backed reader. The archive contains 6,075 entries and exactly six matching optimized SMPL pose assets, one for each NeuMan sequence including Seattle.

Only the following five small files were extracted and persisted:

```text
/content/drive/MyDrive/interactive-digital-humans/datasets/neuman/citron/4d_humans/smpl_optimized_aligned_scale.npz
/content/drive/MyDrive/interactive-digital-humans/datasets/neuman/parkinglot/4d_humans/smpl_optimized_aligned_scale.npz
/content/drive/MyDrive/interactive-digital-humans/datasets/neuman/jogging/4d_humans/smpl_optimized_aligned_scale.npz
/content/drive/MyDrive/interactive-digital-humans/datasets/neuman/lab/4d_humans/smpl_optimized_aligned_scale.npz
/content/drive/MyDrive/interactive-digital-humans/datasets/neuman/bike/4d_humans/smpl_optimized_aligned_scale.npz
```

The full NeuMan ZIP was not downloaded.

Compact inventory: [16B2 pose asset inventory](analysis/16B2_pose_asset_inventory.csv).

### Candidate pose summary

| Sequence | Frames | Beta drift | Scale range | Effective evaluation raw frames |
|---|---:|---:|---|---|
| citron | 37 | 0 | 2.503076 to 3.338921 | `[2, 7, 12]` |
| parkinglot | 42 | 0 | 3.538034 to 4.013123 | `[2, 7, 12, 17]` |
| jogging | 102 | 0 | 1.441199 to 1.930032 | `[2, 7, 12, 17, 22, 27, 32, 37, 42, 47]` |
| lab | 103 | 0 | 8.232719 to 9.435638 | `[2, 7, 12, 17, 22, 27, 32, 37, 42, 47]` |
| bike | 104 | 0 | 1.459522 to 1.607994 | `[2, 7, 12, 17, 22, 27, 32, 37, 42, 47]` |

All five pose assets have constant betas across frames and the expected NeuMan keys: `global_orient`, `body_pose`, `betas`, `transl`, `scale`, `bbox`, and `vertex_colors`.

## First independent-sequence choice

Use **parkinglot** for the first independent pretrained-model replication.

Reason: it provides 42 pose frames and the same four effective evaluation raw-frame indices `[2, 7, 12, 17]` used in the Seattle frame-replication experiment. This gives the cleanest first cross-sequence comparison while changing the pretrained HUGS checkpoint, learned deformation field, shape parameters, canonical Gaussian set, and source sequence.

This is a pragmatic first replication choice, not evidence that parkinglot is intrinsically more representative than the other NeuMan sequences.

## Step 16B3 - Parkinglot checkpoint provenance

The official Parkinglot checkpoint and packaged config were selectively extracted from the persisted official pretrained-model ZIP.

Key facts:

```text
checkpoint SHA256: f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c
Gaussian count: 614157
pose frames: 42
```

The checkpoint is different from the Seattle checkpoint but uses the same core triplane/deformation architecture and 24-channel learned skinning output.

Compact manifest: [16B3 checkpoint manifest](analysis/16B3_parkinglot_checkpoint_manifest.json).

## Steps 16C0-16C1B - source restoration and learned-LBS reconstruction

The official Apple HUGS source was restored at commit:

```text
86ebe5522a384fc553f07f090b63a76dd4af8d33
```

A lightweight source loader was used so the exact `activation.py`, `triplane.py`, and `decoders.py` modules could be loaded without renderer-specific dependencies.

Parkinglot checkpoint states strict-loaded successfully. Canonical Gaussian positions and learned 24-channel LBS weights were reconstructed through the checkpoint forward path.

A temporary numerical audit failure occurred only when the first 4,096 Gaussians were rerun with a different CUDA batch shape. Step 16C1B then ran the actual all-Gaussian forward shape used by HUGS and compared it to the earlier 65,536-chunk pass.

Final result:

```text
FULL-BATCH FORWARD VALID: True
CHUNK SEMANTIC STABILITY: True
STEP 16C1B AUDIT PASS: True
full vs chunk canonical xyz difference: exactly 0
full vs chunk learned LBS difference: exactly 0
dominant-joint mismatch: 0
high-confidence-mask mismatch: 0
high-confidence learned-LBS count: 290822
```

Authoritative large arrays remain in Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1B_fullbatch_numerical_audit.json
```

## Step 16C2 - Parkinglot-specific K=6 target

A subject-specific SMPL Vitruvian template was reconstructed from the Parkinglot betas. The exact HUGS-style top-K target rule was then applied to all 614,157 canonical Gaussians:

```text
K = 6
LBS consistency gate: exp(-L1 / 0.02) > 0.9
spatial weighting: exp(-squared_distance)
```

The K=6 target passed all numerical and independent-search checks:

```text
K6 TARGET VALID: True
max row-sum error: 2.384185791015625e-07
nearest-neighbor exact audit: 1.0
K=6 neighbor-set exact audit: 1.0
sample effective-LBS max abs difference: 1.7881393432617188e-07
```

High-confidence K=6 anatomical assignment at threshold `>=0.9`:

```text
high-confidence: 292095
intended left wrist + hand: 2946
same-side local chain including left collar: 33764
nonlocal: 255385
contralateral upper body including right collar: 77622
```

Learned and K=6 dominant anatomical labels are strongly aligned:

```text
overall dominant-joint agreement: 0.9888562696509199
agreement on K6 high-confidence subset: 0.9999315291257981
```

The key pre-perturbation observation is that the fixed high-confidence contralateral subset has nearly zero SMPL-derived left-wrist/hand support on average, while the learned Parkinglot field introduces substantially more:

```text
K6 contralateral wrist+hand mean:      2.161917080911735e-07
learned contralateral wrist+hand mean: 8.741816418478265e-05
learned/K6 mean ratio:                 404.3548430077448x
K6 max:                                0.00014079449465498328
learned max:                           0.248804971575737
```

Compact summary: [16C2 key summary](analysis/16C2_parkinglot_k6_key_summary.csv).

Authoritative large K=6 mapping remains in Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_manifest.json
```

## Current interpretation

Parkinglot independently reproduces the **pre-perturbation precursor** found in Seattle: a learned cross-joint left-wrist/hand LBS component appears on Gaussians anatomically assigned to the opposite upper body even though the SMPL-derived K=6 target assigns almost no such support on average.

This is not yet a causal cross-sequence replication. No Parkinglot wrist perturbation has been run yet.

## Next step

Run the first Parkinglot causal diagnostic at raw frame 2 with the same `left_wrist z +10 deg` perturbation as Seattle. Freeze the K=6-derived anatomical mask before observing displacement and compare:

1. original learned Parkinglot LBS,
2. Parkinglot K=6 target LBS,
3. learned Parkinglot LBS with only left-wrist/left-hand channels removed on the fixed 77,622-Gaussian high-confidence contralateral subset.

Do not generalize the Seattle causal result to HUGS as a method until this independent Parkinglot perturbation/counterfactual is completed.
