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

Only Seattle is currently extracted persistently under:

```text
/content/drive/MyDrive/interactive-digital-humans/assets/hugs/pretrained_models/
```

### Readiness table

| Sequence | HUGS checkpoint | HUGS config | NeuMan SMPL pose asset | Ready for mechanism replication |
|---|---|---|---|---|
| citron | available in official ZIP | available in official ZIP | missing | no |
| parkinglot | available in official ZIP | available in official ZIP | missing | no |
| jogging | available in official ZIP | available in official ZIP | missing | no |
| lab | available in official ZIP | available in official ZIP | missing | no |
| bike | available in official ZIP | available in official ZIP | missing | no |

The blocker is therefore the persistent NeuMan sequence data, not the pretrained HUGS models.

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

Random byte-range access is therefore available. The full archive has not been stored in Drive.

See [the Step 16B1 archive probe record](analysis/16B1_official_neuman_archive_probe.md).

## Current acquisition strategy

Do not download the entire 4.2 GiB NeuMan archive yet. First use a seekable HTTP range-backed ZIP reader to locate and selectively extract only:

```text
4d_humans/smpl_optimized_aligned_scale.npz
```

for `citron`, `parkinglot`, `jogging`, `lab`, and `bike`.

These pose files are sufficient to inspect candidate frame counts and shape parameters at negligible storage cost. Once a candidate is chosen, extract only its matching pretrained HUGS checkpoint/config from the already-persisted `hugs_pretrained_models.zip` and reconstruct that model's learned LBS field and K=6 target.

## Next step

Step 16B2:

1. open the official NeuMan ZIP through byte-range random access,
2. locate the five candidate `smpl_optimized_aligned_scale.npz` members,
3. persist only those small pose assets into Drive,
4. inspect keys, frame counts, betas, and scale arrays,
5. select the first independent sequence for the causal mechanism replication.

Do not generalize the Seattle result to HUGS as a method until this independent-sequence test is completed.
