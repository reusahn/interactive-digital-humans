# Experiment 02 — Spatial Leakage Localization

This experiment re-analyzes archived HUGS Baseline v1 NPZ outputs to localize non-target deformation and test whether the observed leakage is dominated by isolated outliers, semantic assignment ambiguity, or structured anatomical coupling.

## Methodology correction

Baseline v1 defines `left_ankle` against the coarse semantic region `left_leg`, which contains:

```text
left_hip + left_knee + left_ankle + left_foot
```

In the secondary Step 6–10 helper code, the ankle target was accidentally narrowed to only `left_ankle + left_foot`. This caused left-knee and left-hip displacement to be incorrectly counted as ankle outside displacement.

Therefore:

- wrist and shoulder Step 6–10 analyses remain valid,
- ankle Step 6–10 rows/plots are provisional and must be recomputed,
- Baseline v1's original ankle leakage ratio remains valid because it used the correct coarse `left_leg` region.

## Step 7 — Leakage concentration and anatomical source analysis

Artifacts:

- `analysis/07_anatomical_leakage_groups.csv`
- `analysis/07_leakage_concentration.csv`
- `figures/07_leakage_concentration.png`

For wrist and shoulder, outside displacement is strongly heavy-tailed but not reducible to a tiny handful of extreme points. The top 5% of non-target Gaussians account for roughly 84–85% of outside displacement.

## Step 8 — Confidence robustness

Dominant-joint confidence filtering reduces apparent leakage substantially but does not eliminate the wrist/shoulder signal. At confidence >= 0.9, a meaningful wrist residual remains.

## Step 9 — High-confidence anatomical residual

Artifact:

- `analysis/09_high_confidence_joint_breakdown.csv`

Valid wrist result at confidence >= 0.9:

- left elbow = **39.04%** of high-confidence outside displacement
- right shoulder = 16.10%
- left shoulder = 15.18%
- right elbow = 8.79%
- right hand = 8.53%
- right wrist = 7.57%

The wrist-to-elbow pattern and contralateral upper-limb structure survive strict confidence filtering.

The ankle rows in this artifact are superseded pending corrected recomputation.

## Step 10 — Signed and magnitude response

Artifact:

- `analysis/10_signed_magnitude_high_confidence_response.csv`

The wrist probe was evaluated at ±5°, ±10°, ±20°, and ±30°. Its high-confidence outside-displacement sum is nearly proportional to perturbation magnitude and almost perfectly symmetric with respect to sign:

- 5°: ~5.083
- 10°: ~10.154
- 20°: ~20.23
- 30°: ~30.15

The wrist high-confidence leakage ratio stays effectively constant at ~12.26% across this entire range. The anatomical composition is also extremely stable: upstream same-side share stays near 54.52% and contralateral share near 41.01%.

The shoulder ±10° response is similarly sign-symmetric. The ankle Step 10 rows are superseded pending target-mask correction.

## Current interpretation

The valid wrist residual behaves like a deterministic, approximately linear coupling rather than random numerical noise or a few isolated outliers. However, this is **not yet evidence of a representation-specific HUGS failure**. HUGS deforms Gaussians using blended SMPL/LBS transformations rather than the single dominant-joint labels used by this diagnostic.

## Next step

1. Recompute the ankle secondary analysis using the full `left_leg` target set.
2. Then run an **SMPL-only control** with the same perturbations and comparable anatomical groupings.

The SMPL-only control will test whether the cross-body / upstream structure is already implied by the body and skinning model or whether HUGS introduces additional representation-specific residuals.
