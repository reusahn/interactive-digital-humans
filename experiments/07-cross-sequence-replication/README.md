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

This is a pragmatic first replication choice, not evidence that parkinglot is intrinsically more representative than the other NeuMan sequences. Additional sequences should be tested after the mechanism pipeline is validated independently once.

## Next step

Step 16B3:

1. selectively extract only `parkinglot/human_final.pth` and `parkinglot/config_train.yaml` from the already-persisted official pretrained-model ZIP,
2. compute checkpoint SHA256 and inspect checkpoint tensor structure,
3. verify the packaged sequence/config settings,
4. verify Gaussian count,
5. stop before learned-LBS reconstruction if any architecture or config mismatch appears.

After that, reconstruct parkinglot learned LBS and K=6 target before running the learned-vs-K6-vs-selective-ablation comparison.

Do not generalize the Seattle result to HUGS as a method until this independent-sequence test is completed.
