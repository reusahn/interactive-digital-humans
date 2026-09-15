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

The HUGS project README documents the official NeuMan data archive `neuman_data.zip`, which contains the required NeuMan sequences.

## Next step

Acquire and persist at least one additional official NeuMan sequence dataset. Then verify:

1. `4d_humans/smpl_optimized_aligned_scale.npz`,
2. matching official HUGS human checkpoint,
3. matching packaged HUGS config,
4. canonical Gaussian count and learned-LBS export,
5. K=6 target reconstruction.

After validation, repeat the Seattle mechanism diagnostic on the independent model:

- left-wrist z +10 degrees,
- original learned LBS,
- reconstructed K=6 target LBS,
- selective learned left-wrist/hand channel ablation on the high-confidence contralateral upper-body subset.

Do not generalize the Seattle result to HUGS as a method until this independent-sequence test is completed.
