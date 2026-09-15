# Experiment 06 - Seattle Frame Replication

## Question

Does the learned cross-joint wrist/hand LBS mechanism identified in the Seattle raw-frame-2 diagnostic remain stable across multiple base poses from the same pretrained HUGS sequence?

## Setup

- model: pretrained HUGS, NeuMan Seattle
- Gaussian count: 472,958
- perturbation: left wrist, z axis, +10 degrees
- raw NeuMan frames: 2, 7, 12, 17
- confidence threshold: >= 0.9
- high-confidence contralateral subset: 33,072 Gaussians
- contralateral definition: right collar + right shoulder + right elbow + right wrist + right hand
- conditions: learned HUGS LBS, reconstructed K=6 target LBS, corrected selective left-wrist/left-hand-channel ablation

Large per-Gaussian displacement arrays remain in Google Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/06-frame-replication/15A_seattle_frame_replication_displacements.npz
```

Compact summary:

- [15A Seattle frame replication CSV](analysis/15A_seattle_frame_replication.csv)

## Results

| Raw frame | Learned contralateral | K=6 contralateral | Selective ablation | K=6 reduction | Ablation reduction | Removed-mass vs reduction r |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 4.163577 | 0.007556 | 0.0 | 99.8185% | 100.0% | 0.981289 |
| 7 | 4.221095 | 0.007667 | 0.0 | 99.8184% | 100.0% | 0.981038 |
| 12 | 4.272963 | 0.007797 | 0.0 | 99.8175% | 100.0% | 0.980829 |
| 17 | 4.096565 | 0.007401 | 0.0 | 99.8193% | 100.0% | 0.981440 |

Across the four tested base poses:

```text
learned contralateral range: 4.096565 to 4.272963
mean K=6 reduction:          99.8184409%
minimum K=6 reduction:       99.8175372%
mean selective reduction:    100.0%
minimum selective reduction: 100.0%
mean removed-mass vs reduction correlation: 0.9811489
```

## Interpretation

The mechanism is highly stable across these four Seattle evaluation poses. The learned cross-joint component continues to produce approximately 4.1-4.27 units of high-confidence contralateral displacement, while the SMPL-derived K=6 target leaves only about 0.0074-0.0078. Removing the learned left-wrist/hand channels from the same contralateral subset eliminates the measured response in all four tested poses.

This is evidence of **within-sequence pose robustness**, not independent replication across subjects, checkpoints, or Gaussian-human methods. All four tests share the same pretrained Seattle model, learned weights, canonical Gaussian set, and anatomical mask.

## Defensible claim

> In the pretrained HUGS Seattle sequence, the learned cross-joint wrist/hand LBS mechanism that mediates contralateral upper-body displacement remains stable across four tested evaluation poses under the same left-wrist z +10 degree perturbation.

Do not generalize this result to other NeuMan sequences or HUGS models until cross-sequence replication is performed.

## Next step

Run the same mechanism test on at least one independently pretrained NeuMan HUGS sequence. The next operational step is to inventory which additional official pretrained sequence checkpoints and corresponding NeuMan pose assets are already available in persistent storage.
