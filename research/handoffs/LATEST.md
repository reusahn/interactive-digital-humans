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
- Step 16C1 / 16C1B Parkinglot learned-LBS reconstruction and numerical audit
- Step 16C2 Parkinglot-specific SMPL K=6 target reconstruction
- Step 16C3 Parkinglot independent causal counterfactual
- Step 16C4 Parkinglot within-checkpoint pose replication
- Step 16C5 Parkinglot axis/sign robustness control
- Step 16D1 Jogging checkpoint/config provenance and architecture validation
- Step 16D2 Jogging learned-LBS reconstruction and full-batch/chunk audit
- Step 16D3 Jogging subject-specific K=6 target reconstruction and precursor test
- Step 16D4 Jogging third-checkpoint causal counterfactual

## Current strongest result

The learned cross-joint left-wrist/left-hand LBS mechanism has now been causally reproduced in **three independently pretrained HUGS NeuMan checkpoints: Seattle, Parkinglot, and Jogging**.

### Seattle

Four tested raw evaluation frames `[2,7,12,17]`, `left_wrist z +10 deg`:

```text
mean K6 reduction:             99.8184408838516%
minimum K6 reduction:          99.81753724223914%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9811488931072522
```

### Parkinglot

Four tested raw evaluation frames `[2,7,12,17]`:

```text
mean K6 reduction:             99.70879580221536%
minimum K6 reduction:          99.70857508781499%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9975337157455157
```

Parkinglot raw frame 2 additionally passed `x/y/z × {-10,+10} deg` direction/sign robustness:

```text
minimum K6 reduction:                 98.7997086031298%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation:     0.9664424743486758
maximum ablated contralateral sum:    0.0
maximum +/- sign asymmetry:           0.5583232093225667%
AXIS/SIGN ROBUST:                     True
```

The pathway is direction robust in Parkinglot, but effect magnitude is anisotropic. Do not claim axis-invariant magnitude.

### Jogging third independent causal replication

Jogging checkpoint:

```text
checkpoint SHA256: 7a056fd6ba8ee9f5cc640eac43666e9ab57de33db2062a8ca379d1daa3afa769
Gaussian count:    311723
pose frames:       102
```

Step 16D3 established the same pre-perturbation precursor on a fixed K6-derived 20,887-Gaussian high-confidence contralateral subset:

```text
K6 left-wrist+hand mean:      2.763716224762902e-07
learned left-wrist+hand mean: 0.00020052377658430487
learned/K6 mean ratio:        725.5584881964779x
```

Step 16D4 then applied `left_wrist z +10 deg` at raw frame 2. Kinematic auditing showed only SMPL transforms `[20,22]` changed. No contralateral transform changed.

```text
learned contralateral:            1.2177642583847046
K6 contralateral:                 0.0021828871686011553
selective-ablation contralateral: 0.0
K6 reduction vs learned:          99.82074632642802%
selective-ablation reduction:     100.0%
learned-to-K6 gap closed:         1.0017957556937693
removed-mass vs reduction r:      0.9901018350101268
THIRD CAUSAL REPLICATION CANDIDATE: True
```

Selective intervention changed no weights outside the fixed contralateral subset.

## Strongest defensible claim

> In three independently pretrained HUGS NeuMan checkpoints, Seattle, Parkinglot, and Jogging, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding subject-specific SMPL-derived K=6 target under the tested left-wrist perturbation. Selectively removing only those learned wrist/hand channels on the fixed contralateral subset eliminates the tested contralateral response.

Seattle and Parkinglot also have within-checkpoint pose replication. Parkinglot additionally has axis/sign robustness. Jogging has not yet undergone pose replication.

Do not describe this as a universal HUGS failure, an isotropic effect, or a result generalized to all joints or Gaussian-human methods.

## Immediate next experiment

Run **Step 16D5: Jogging within-checkpoint pose replication** across effective raw evaluation frames:

```text
[2,7,12,17,22,27,32,37,42,47]
```

Keep fixed:

- Jogging checkpoint and learned LBS
- Jogging subject-specific K6 target
- K6-derived anatomical masks
- fixed 20,887-Gaussian contralateral subset
- selective wrist/hand ablation definition
- `left_wrist z +10 deg`

If the causal suppression is stable across these 10 base poses, the third independent checkpoint will also have substantially stronger within-sequence pose robustness than the first two sequences.

For continuity, read:

- [Step 16D2 Jogging learned-LBS validation](../sessions/2026-09-15-step16d2.md)
- [Step 16D3 Jogging K=6 precursor](../sessions/2026-09-15-step16d3.md)
- [Step 16D4 Jogging third causal replication](../sessions/2026-09-15-step16d4.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [16D4 compact summary](../../experiments/07-cross-sequence-replication/analysis/16D4_jogging_counterfactual_summary.csv)
