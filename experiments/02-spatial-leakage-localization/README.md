# Experiment 02 — Spatial Leakage Localization

This experiment re-analyzes the archived HUGS Baseline v1 NPZ outputs to localize non-target deformation and test whether the observed leakage is dominated by isolated outliers, semantic assignment ambiguity, or structured anatomical coupling.

## Step 7 — Leakage concentration and anatomical source analysis

Artifacts:

- `analysis/07_anatomical_leakage_groups.csv`
- `analysis/07_leakage_concentration.csv`
- `figures/07_leakage_concentration.png`

Main observation: outside displacement is strongly heavy-tailed but not reducible to a tiny handful of extreme points. Across ankle, wrist, and shoulder probes, the top 5% of non-target Gaussians account for roughly 83–85% of outside displacement, while the top 0.1% account for only roughly 6–13%.

Anatomically, ankle leakage is dominated by the upstream same-side leg, while wrist and shoulder probes show large same-side upstream components together with notable contralateral upper-limb components.

## Step 8 — Confidence robustness

Dominant-joint confidence filtering reduces the apparent leakage substantially but does not eliminate it. At confidence >= 0.9, a meaningful residual remains, especially for wrist motion. This shows that nearest-vertex / dominant-joint ambiguity contributes to the diagnostic, but cannot explain all of the observed displacement.

## Step 9 — High-confidence anatomical residual

Artifact:

- `analysis/09_high_confidence_joint_breakdown.csv`

Key results at dominant-joint confidence >= 0.9:

- ankle z: left knee = **86.73%** of high-confidence outside displacement
- wrist z: left elbow = **39.04%**, with substantial contralateral upper-limb components
- shoulder z: the outside component is small in absolute terms but is dominated by contralateral upper-limb assignments

The ankle-to-knee and wrist-to-elbow patterns therefore survive strict confidence filtering and are not explained by low-confidence semantic assignment alone.

## Step 10 — Signed and magnitude response

Artifact:

- `analysis/10_signed_magnitude_high_confidence_response.csv`

The wrist probe was evaluated at ±5°, ±10°, ±20°, and ±30°. Its high-confidence outside-displacement sum is nearly proportional to perturbation magnitude and almost perfectly symmetric with respect to sign:

- 5°: ~5.083
- 10°: ~10.154
- 20°: ~20.23
- 30°: ~30.15

The high-confidence leakage ratio stays effectively constant at ~12.26% across this entire range. The anatomical composition is also extremely stable: upstream same-side share stays near 54.52% and contralateral share near 41.01%.

The ankle ±10° and shoulder ±10° probes are similarly sign-symmetric.

## Current interpretation

The residual deformation behaves like a deterministic, approximately linear coupling rather than random numerical noise or a few isolated outliers. However, this is **not yet evidence of a representation-specific HUGS failure**. HUGS deforms Gaussians using blended SMPL/LBS transformations rather than the single dominant-joint labels used by this diagnostic.

The next decisive experiment is therefore an **SMPL-only control**: apply the same joint perturbations directly to the underlying body model and compare the resulting vertex displacement structure against the HUGS Gaussian response. This will separate deformation already implied by the body/skinning model from additional representation-specific effects.
