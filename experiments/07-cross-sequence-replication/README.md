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

## Step 16B3 - Parkinglot checkpoint provenance

The official Parkinglot checkpoint and packaged config were selectively extracted from the persisted official pretrained-model ZIP.

```text
checkpoint SHA256: f864f0fc3f4a9e6248fcd3ed0964b02967d7552825d6ff9993a149823204d76c
Gaussian count: 614157
pose frames: 42
```

The checkpoint is different from Seattle but uses the same core triplane/deformation architecture and 24-channel learned skinning output.

Compact manifest: [16B3 checkpoint manifest](analysis/16B3_parkinglot_checkpoint_manifest.json).

## Steps 16C0-16C1B - source restoration and learned-LBS reconstruction

The official Apple HUGS source was restored at commit:

```text
86ebe5522a384fc553f07f090b63a76dd4af8d33
```

A lightweight loader imported the exact HUGS `activation.py`, `triplane.py`, and `decoders.py` modules without renderer-specific dependencies.

Parkinglot checkpoint states strict-loaded successfully. Canonical Gaussian positions and learned 24-channel LBS weights were reconstructed through the checkpoint forward path.

Step 16C1B matched the HUGS all-Gaussian forward shape and compared it to the 65,536-chunk pass.

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

Authoritative large arrays:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1_parkinglot_learned_lbs.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C1B_fullbatch_numerical_audit.json
```

## Step 16C2 - Parkinglot-specific K=6 target

A subject-specific SMPL Vitruvian template was reconstructed from Parkinglot betas and the HUGS top-K target rule was applied to all 614,157 canonical Gaussians.

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

Pre-perturbation precursor on the fixed contralateral subset:

```text
K6 contralateral wrist+hand mean:      2.161917080911735e-07
learned contralateral wrist+hand mean: 8.741816418478265e-05
learned/K6 mean ratio:                 404.3548430077448x
```

Compact summary: [16C2 key summary](analysis/16C2_parkinglot_k6_key_summary.csv).

Authoritative K=6 mapping:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_effective_mapping.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C2_parkinglot_k6_manifest.json
```

## Step 16C3 - independent Parkinglot causal replication

The fixed K=6-derived anatomical masks were frozen before displacement. The same Seattle diagnostic was then applied to Parkinglot raw frame 2:

```text
left_wrist z +10 deg
```

Kinematic auditing confirmed that only left wrist and descendant left hand transforms changed:

```text
changed SMPL transforms: [20, 22]
unexpected changed transforms: []
```

Three conditions were compared:

1. original learned Parkinglot LBS,
2. Parkinglot SMPL-derived K=6 target,
3. learned Parkinglot LBS with left-wrist/left-hand channels removed only on the fixed 77,622-Gaussian high-confidence contralateral subset.

The selective intervention changed no weights outside that subset.

### High-confidence hierarchical result

| Condition | HC total | Intended % | Local-chain % | Nonlocal % | Contralateral sum | Contralateral % |
|---|---:|---:|---:|---:|---:|---:|
| learned | 159.458954 | 82.896408 | 12.284736 | 4.818841 | 5.416988 | 3.397105 |
| K6 target | 155.191818 | 85.765297 | 13.843283 | 0.391409 | 0.015786 | 0.010172 |
| wrist/hand ablated | 154.041946 | 85.811526 | 12.716738 | 1.471733 | 0.000000 | 0.000000 |

Primary result:

```text
learned contralateral:             5.416987895965576
K6 contralateral:                  0.01578645221889019
selective-ablation contralateral:  0.0
K6 reduction vs learned:           99.70857508781499%
selective-ablation reduction:      100.0%
learned-to-K6 gap closed:          1.0029227667924083
```

Per-Gaussian association:

```text
fraction displacement reduced:       0.8418103115096236
removed-mass vs reduction r:         0.9975359387446432
removed-mass vs learned displacement r: 0.9975359387446432
```

Compact result: [16C3 counterfactual summary](analysis/16C3_parkinglot_counterfactual_summary.csv).

Authoritative Drive outputs:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_summary.csv
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/07-cross-sequence-replication/16C3_parkinglot_counterfactual_metadata.json
```

## Current interpretation

The Seattle mechanism has now been causally reproduced in a second independently pretrained HUGS checkpoint.

The strongest defensible claim is:

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement under a left-wrist z perturbation relative to the corresponding SMPL-derived K=6 target.

The exact zero produced by selective ablation is expected from the LBS structure once the only changed wrist/hand channels are removed. The important result is that HUGS learns cross-joint support largely absent from the target and that this learned support accounts for the amplified contralateral response in both independently trained models.

This result is still bounded to two checkpoints and the tested left-wrist z perturbation. It does not yet establish that all HUGS joints, axes, sequences, or Gaussian-human methods behave this way.

## Next step

Repeat the Parkinglot causal diagnostic at raw evaluation frames `[2, 7, 12, 17]` using the same fixed K=6-derived anatomical mask and the same `left_wrist z +10 deg` perturbation. If the mechanism is stable across these poses, then proceed to a third independently pretrained sequence.
