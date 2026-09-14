# Experiment 01 Results

_Status: Baseline v1 completed on the pretrained HUGS Seattle sequence. Raw arrays are archived in Google Drive. Compact tables and figures are versioned here._

## Scope

- baseline: HUGS / Human Gaussian Splats
- dataset: NeuMan
- sequence: Seattle
- frame analyzed: 0
- number of human Gaussians: 472,958
- saved probe measurements: 36
- perturbation family: controlled SMPL joint rotations
- joints in the main joint sweep: left wrist, left elbow, left shoulder, left knee, left ankle
- axes: x, y, z
- signed perturbation for joint sweep: ±10°
- additional wrist magnitude sweep: ±5°, ±10°, ±20°, ±30° about z

The authoritative raw `*.npz` outputs remain in Google Drive. See `DATA_MANIFEST.md`.

## Main result

Within this Seattle/frame-0 baseline, HUGS deformation locality is strongly articulation-dependent. Distal articulations show substantially more non-target Gaussian displacement than the proximal shoulder under the current kinematic-subtree leakage metric.

The strongest observed condition is **left ankle z at 26.57% leakage**. Left wrist conditions are approximately **9.90%–11.21%**, while left shoulder conditions are approximately **0.58%–0.91%**.

These results are not yet a claim about HUGS in general because this baseline currently covers one sequence and one frame.

## Kinematic-subtree leakage

The initial coarse-region metric was refined so that descendants expected to move under a joint rotation count as target motion. For example:

- wrist target: wrist + hand
- elbow target: elbow + wrist + hand
- shoulder target: shoulder + elbow + wrist + hand
- ankle target: ankle + foot
- knee target: knee + ankle + foot

| Joint | Axis | Leakage | Target mean | Outside mean | Outside P99 | Outside max | Target Gaussians |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| left_ankle | z | 26.57% | 0.014321 | 0.000190 | 0.004731 | 0.442028 | 16,730 |
| left_ankle | x | 18.19% | 0.023556 | 0.000192 | 0.004858 | 0.377936 | 16,730 |
| left_wrist | z | 11.21% | 0.021561 | 0.000052 | 0.001291 | 0.036199 | 8,825 |
| left_ankle | y | 10.72% | 0.020328 | 0.000089 | 0.002792 | 0.229624 | 16,730 |
| left_wrist | y | 10.27% | 0.022988 | 0.000050 | 0.001285 | 0.036621 | 8,825 |
| left_wrist | x | 9.90% | 0.009780 | 0.000020 | 0.000350 | 0.029225 | 8,825 |
| left_knee | y | 8.39% | 0.014051 | 0.000198 | 0.005646 | 0.218718 | 62,984 |
| left_elbow | z | 3.05% | 0.042939 | 0.000072 | 0.001958 | 0.027016 | 24,065 |
| left_elbow | x | 2.60% | 0.039038 | 0.000056 | 0.001265 | 0.027707 | 24,065 |
| left_knee | z | 2.53% | 0.082265 | 0.000328 | 0.006907 | 0.349888 | 62,984 |
| left_elbow | y | 2.53% | 0.059189 | 0.000082 | 0.002067 | 0.027601 | 24,065 |
| left_knee | x | 2.28% | 0.082641 | 0.000297 | 0.006171 | 0.279244 | 62,984 |
| left_shoulder | x | 0.91% | 0.057910 | 0.000052 | 0.001173 | 0.038589 | 42,595 |
| left_shoulder | y | 0.66% | 0.064406 | 0.000042 | 0.000919 | 0.087770 | 42,595 |
| left_shoulder | z | 0.58% | 0.082392 | 0.000047 | 0.001051 | 0.095469 | 42,595 |

Exact compact values are stored in `analysis/joint_axis_leakage.csv`.

## Wrist magnitude and sign behavior

For left-wrist z perturbations, target and outside displacement increase almost proportionally with perturbation magnitude, while the leakage proportion remains almost constant around 11.21%.

| Degrees | Target mean | Outside mean | Leakage ratio | Outside active fraction | Max target | Max outside |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| -30 | 0.064022 | 0.000154 | 11.2050% | 0.237548 | 0.170886 | 0.107502 |
| -20 | 0.042955 | 0.000103 | 11.2066% | 0.217410 | 0.114650 | 0.072124 |
| -10 | 0.021560 | 0.000052 | 11.2092% | 0.182437 | 0.057543 | 0.036199 |
| -5 | 0.010790 | 0.000026 | 11.2125% | 0.148520 | 0.028799 | 0.018117 |
| +5 | 0.010791 | 0.000026 | 11.2133% | 0.148498 | 0.028799 | 0.018117 |
| +10 | 0.021562 | 0.000052 | 11.2109% | 0.182471 | 0.057544 | 0.036199 |
| +20 | 0.042962 | 0.000103 | 11.2106% | 0.217535 | 0.114653 | 0.072123 |
| +30 | 0.064039 | 0.000154 | 11.2111% | 0.237557 | 0.170893 | 0.107500 |

This supports a narrow statement for this condition: wrist deformation is approximately sign-symmetric and magnitude-linear, while the leakage proportion is nearly invariant to signed magnitude.

## Wrist axis dependence at ±10°

Averaging the two signs for each axis:

| Axis | Leakage | Target mean | Outside mean | Outside active fraction | Max outside |
| --- | ---: | ---: | ---: | ---: | ---: |
| x | 9.90% | 0.009780 | 0.000020 | 0.101313 | 0.029225 |
| y | 10.27% | 0.022988 | 0.000050 | 0.166572 | 0.036621 |
| z | 11.21% | 0.021561 | 0.000052 | 0.182454 | 0.036199 |

So sign has little effect under this wrist test, but rotation axis does.

## Joint-assignment confidence sensitivity

Filtering to more confidently assigned Gaussians does not remove the main distal-versus-proximal pattern. In particular, at confidence ≥ 0.9:

- left ankle z remains 25.49%
- left ankle x remains 19.23%
- left wrist z remains 12.27%
- left wrist y remains 11.16%
- left shoulder x/y/z fall to 0.41% / 0.29% / 0.25%

This makes it less likely that the strongest ankle/wrist effects are explained solely by ambiguous hard joint assignment. However, confidence filtering changes the evaluated Gaussian population substantially, so this is a sensitivity check rather than a directly comparable absolute benchmark across thresholds.

Full values are stored in `analysis/confidence_sensitivity.csv`.

## Gaussian-to-SMPL joint assignment

The dominant-joint mapping is non-empty for all 24 SMPL joints. Relevant subtree counts match the analysis masks exactly:

```text
left_wrist target   = 6,501 wrist + 2,324 hand = 8,825
left_elbow target   = 15,240 elbow + 6,501 wrist + 2,324 hand = 24,065
left_shoulder target= 18,530 shoulder + 15,240 elbow + 6,501 wrist + 2,324 hand = 42,595
left_ankle target   = 13,369 ankle + 3,361 foot = 16,730
left_knee target    = 46,254 knee + 13,369 ankle + 3,361 foot = 62,984
```

All 24 counts are stored in `analysis/joint_assignment_counts.csv`.

## Figures

The baseline record includes:

1. joint × axis deformation leakage heatmap,
2. the same heatmap after filtering to joint-confidence ≥ 0.9,
3. confidence-threshold sensitivity curves,
4. wrist magnitude-response plot,
5. bidirectional wrist-locality plot.

## Current interpretation

The strongest defensible working hypothesis is:

> Distal articulations in this HUGS baseline exhibit substantially greater apparent non-local Gaussian deformation than proximal articulations, and the strongest effects persist after filtering by joint-assignment confidence.

A separate wrist result is:

> Wrist deformation is approximately sign-symmetric and magnitude-linear in this test, while locality is direction-dependent.

## What this does not establish

This Baseline v1 does **not** yet establish that distal-joint leakage is a universal property of HUGS. Current limitations include:

- one NeuMan sequence,
- one validation frame,
- only left-side joints in the full joint sweep,
- representation-space displacement rather than perceptual/image-space artifact measurement,
- hard dominant-joint assignment used for diagnostic grouping,
- no competing method yet.

The next analysis should spatially localize the highest outside-displacement Gaussians for representative conditions such as left ankle z +10° and left wrist z +10°, then compare observed displacement with expected LBS influence before proposing a new locality regularizer or representation change.
