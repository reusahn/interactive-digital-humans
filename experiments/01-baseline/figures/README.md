# Baseline v1 Figures

These figures are compact, GitHub-native SVG records regenerated from the measured Baseline v1 tables. The original Colab PNG figures are also preserved in the Google Drive experiment archive described in `../DATA_MANIFEST.md`.

## 1. Joint × axis leakage

![Joint-axis leakage](01_joint_axis_leakage.svg)

Main observation: the strongest leakage in Seattle/frame 0 occurs at the distal ankle and wrist conditions, while the shoulder is much lower under the kinematic-subtree metric.

## 2. High-confidence subset

![High-confidence leakage](02_high_confidence_leakage.svg)

The main ankle/wrist versus shoulder pattern remains visible when only Gaussians with joint-assignment confidence ≥ 0.9 are retained.

## 3. Confidence sensitivity

![Confidence sensitivity](03_confidence_sensitivity.svg)

This is a sensitivity analysis, not a direct apples-to-apples benchmark across thresholds, because increasing the confidence threshold changes the evaluated Gaussian population.

## 4. Wrist displacement response

![Wrist displacement response](04_wrist_displacement_response.svg)

For signed left-wrist z perturbations from ±5° to ±30°, target displacement grows approximately with magnitude. Outside mean displacement is much smaller on the same scale.

## 5. Bidirectional wrist leakage

![Bidirectional wrist leakage](05_wrist_bidirectional_leakage.svg)

The z-axis wrist leakage ratio remains close to 11.21% across the tested signed magnitudes, showing near sign symmetry and approximate magnitude invariance of the leakage proportion in this single condition.

## Source tables

- `../analysis/joint_axis_leakage.csv`
- `../analysis/confidence_sensitivity.csv`
- `../analysis/joint_assignment_counts.csv`
- authoritative 36-run summary and raw NPZ arrays: Google Drive archive in `../DATA_MANIFEST.md`
