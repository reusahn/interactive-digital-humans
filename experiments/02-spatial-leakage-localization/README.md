# Experiment 02 — Spatial Leakage Localization

This experiment re-analyzes archived HUGS probe outputs to localize non-target deformation and distinguish local kinematic propagation from genuinely non-local coupling.

## Metric definitions

Two locality scales are now reported separately.

### Fine joint-local target

For the ankle analysis, the strict target is:

```text
left_ankle + left_foot
```

Under this definition, knee/hip motion counts as outside displacement. The archived `joint_axis_leakage.csv` reports 26.57% ankle-z leakage with `num_target = 16730`, which matches the semantic-assignment counts `left_ankle = 13369` plus `left_foot = 3361`.

### Coarse regional target

The original probe code maps `left_ankle` to the entire semantic `left_leg` region:

```text
left_hip + left_knee + left_ankle + left_foot
```

Recomputing the same NPZ with this broader target gives only ~5.38% regional leakage at +10°, and ~3.13% after dominant-joint confidence >= 0.9 filtering.

These values are not contradictory. They measure different spatial scales of locality.

## Step 7 — Leakage concentration

Artifacts:

- `analysis/07_anatomical_leakage_groups.csv`
- `analysis/07_leakage_concentration.csv`

The displacement signal is heavy-tailed but not reducible to a few isolated points. Roughly the top 5% of non-target Gaussians account for about 83–85% of outside displacement.

## Step 8 — Confidence robustness

Dominant-joint confidence filtering substantially reduces apparent outside displacement, confirming that semantic boundary ambiguity contributes to the metric. A meaningful residual remains, especially for wrist motion.

## Step 9 — High-confidence residual anatomy

Artifact:

- `analysis/09_high_confidence_joint_breakdown.csv`

For wrist z at confidence >= 0.9:

- left elbow = 39.04%
- right shoulder = 16.10%
- left shoulder = 15.18%
- right elbow = 8.79%
- right hand = 8.53%
- right wrist = 7.57%

The same-side upstream elbow remains the largest component and substantial contralateral upper-limb structure survives strict filtering.

## Step 10 — Signed and magnitude response

Artifact:

- `analysis/10_signed_magnitude_high_confidence_response.csv`

The wrist probe at ±5°, ±10°, ±20°, and ±30° shows an approximately linear and sign-symmetric response. High-confidence outside displacement scales from ~5.08 at 5° to ~30.15 at 30°, while the leakage ratio remains near 12.26% and the contralateral share remains near 41%.

This behavior is consistent with deterministic coupling rather than random numerical noise.

## Step 10A — Coarse ankle regional control

Artifacts:

- `analysis/10A_corrected_ankle_summary.csv`
- `analysis/10A_corrected_ankle_joint_breakdown.csv`

At +10°:

- full-left-leg target displacement = 309.443726
- outside displacement = 17.596235
- coarse regional leakage = **5.380455%**
- high-confidence coarse leakage = **3.126863%**

At -10°, the corresponding values are 5.404658% and 3.135370%, showing strong sign symmetry.

The large difference between the strict 26.57% ankle/foot diagnostic and the ~5.38% full-leg diagnostic shows that much of the apparent ankle leakage is intra-limb coupling rather than cross-region motion.

## Current interpretation

The locality problem should be treated hierarchically:

1. intended joint/part,
2. same-side kinematic neighborhood,
3. non-local or cross-body remainder.

The wrist remains the strongest candidate for a non-local effect because it retains a stable contralateral component under high-confidence filtering and across perturbation magnitude.

This is not yet evidence of a HUGS-specific representation failure. HUGS uses blended SMPL/LBS transformations, so the next decisive comparison is against an SMPL-only control.

## Next step

Compute a hierarchical displacement decomposition for ankle, wrist, and shoulder using the existing NPZ arrays, then run an **SMPL-only control vs HUGS Gaussian response**.
