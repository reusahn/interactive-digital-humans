# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Completed state

The learned cross-joint left-wrist/left-hand LBS mechanism has now been causally reproduced in **three independently pretrained HUGS NeuMan checkpoints: Seattle, Parkinglot, and Jogging**.

All three use the same bounded diagnostic: subject-specific K6-derived anatomy, `left_wrist z +10 deg`, comparison of original learned LBS vs subject-specific SMPL-derived K6 target, plus selective removal of only learned left-wrist/left-hand channels on the fixed high-confidence contralateral subset.

### Seattle

Raw evaluation frames `[2,7,12,17]`:

```text
mean K6 reduction:             99.8184408838516%
minimum K6 reduction:          99.81753724223914%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9811488931072522
learned contra % HC range:     4.930677% to 5.034862%
```

### Parkinglot

Raw evaluation frames `[2,7,12,17]`:

```text
mean K6 reduction:             99.70879580221536%
minimum K6 reduction:          99.70857508781499%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9975337157455157
learned contra % HC range:     3.3925969009792323 to 3.3971048755337407
```

Parkinglot raw frame 2 also passed the tested `x/y/z × {-10,+10} deg` direction/sign robustness control:

```text
minimum K6 reduction:                 98.7997086031298%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation:     0.9664424743486758
maximum ablated contralateral sum:    0.0
maximum +/- sign asymmetry:           0.5583232093225667%
AXIS/SIGN ROBUST:                     True
```

The pathway is direction robust in Parkinglot, but effect magnitude is anisotropic. Do not claim axis-invariant magnitude.

### Jogging

Checkpoint provenance:

```text
checkpoint SHA256: 7a056fd6ba8ee9f5cc640eac43666e9ab57de33db2062a8ca379d1daa3afa769
Gaussian count:    311723
pose frames:       102
```

Step 16D3 precursor on the fixed K6-derived contralateral subset (`20887` Gaussians):

```text
K6 left-wrist+hand mean:      2.763716224762902e-07
learned left-wrist+hand mean: 0.00020052377658430487
learned/K6 mean ratio:        725.5584881964779x
```

Step 16D4 raw-frame-2 causal replication:

```text
learned contralateral:            1.2177642583847046
K6 contralateral:                 0.0021828871686011553
selective-ablation contralateral: 0.0
K6 reduction vs learned:          99.82074632642802%
selective-ablation reduction:     100.0%
removed-mass vs reduction r:      0.9901018350101268
```

Step 16D5 then repeated the same frozen causal test across all 10 effective Jogging evaluation poses `[2,7,12,17,22,27,32,37,42,47]`.

```text
FRAME2 REGRESSION PASS:                 True
learned contralateral range:            1.1079813241958618 to 1.2177642583847046
learned contra % HC range:              8.343904716882907 to 8.673447072624047
mean K6 reduction:                      99.8193166019593%
minimum K6 reduction:                   99.817790981312%
mean selective-ablation reduction:      100.0%
minimum selective-ablation reduction:   100.0%
mean removed-mass correlation:          0.9900301470766584
minimum removed-mass correlation:       0.9899109845297344
maximum ablated contralateral sum:      0.0
JOGGING 10-FRAME POSE ROBUST:           True
```

At every tested Jogging frame, only SMPL transforms `[20,22]` changed. The selective intervention changed no weights outside the fixed contralateral subset.

## Strongest defensible claim

> In three independently pretrained HUGS NeuMan checkpoints, Seattle, Parkinglot, and Jogging, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding subject-specific SMPL-derived K6 target under the tested left-wrist perturbation. Selectively removing only those learned wrist/hand channels on the fixed contralateral subset eliminates the tested contralateral response. The mechanism is stable across four tested evaluation poses in Seattle, four in Parkinglot, and all ten effective evaluation poses in Jogging. Parkinglot additionally shows robustness to the tested rotation axis and sign, with anisotropic response magnitude.

These are **three independent checkpoint-level replications**, not 18 independent replications. Within-sequence frame tests share checkpoint, learned field, Gaussian population, K6 target, and mask.

Do not yet generalize to other joints, all HUGS checkpoints, all perturbation magnitudes, or other Gaussian-human methods.

## Authoritative recent artifacts

- `research/sessions/2026-09-15-step16d5.md`
- `experiments/07-cross-sequence-replication/analysis/16D5_jogging_frame_replication.csv`
- Drive: `experiments/07-cross-sequence-replication/16D5_jogging_frame_replication_displacements.npz`
- Drive: `experiments/07-cross-sequence-replication/16D5_jogging_frame_replication_metadata.json`

## Immediate next action

Before starting a second joint, freeze the completed left-wrist finding into one cross-checkpoint synthesis artifact. Read the already-saved Seattle, Parkinglot, and Jogging frame-replication CSVs, keep checkpoint as the independent unit, and produce a compact checkpoint-level table with normalized contralateral fraction, minimum/mean K6 suppression, selective-ablation suppression, removed-mass correlation, and number of tested poses. Do not pool individual frames as independent samples.

After that synthesis is reviewed, choose the second-joint generalization test with an explicitly pre-declared causal channel set and anatomical endpoint.
