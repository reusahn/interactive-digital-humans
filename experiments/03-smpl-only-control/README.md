# Experiment 03 — SMPL-Only Control

## Question

Does the non-local wrist response observed in the HUGS Gaussian representation already exist in the underlying SMPL deformation, or is it amplified after mapping deformation to Gaussians?

## Setup

- NeuMan Seattle, frame 0
- SMPL neutral model, cleaned from the licensed legacy PKL for modern loading
- Seattle SMPL parameters from `smpl_optimized_aligned_scale.npz`
- left wrist z perturbation at ±10°
- vertex groups defined from the true SMPL LBS weights by dominant joint
- high-confidence condition: dominant LBS weight >= 0.9
- hierarchy: `intended = left_wrist + left_hand`, `local_chain = left_elbow + left_shoulder + left_collar`, `nonlocal = remainder`

Large vertex NPZ outputs remain in Google Drive under:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/03-smpl-only-control/
```

## Step 12G result

At +10°:

- SMPL high-confidence intended: **96.60%** of total displacement
- SMPL high-confidence local chain: **0.93%**
- SMPL high-confidence nonlocal: **2.47%**
- SMPL high-confidence contralateral arm: **0.89%**

At -10° the result is nearly sign-symmetric:

- intended: **96.56%**
- local chain: **0.91%**
- nonlocal: **2.53%**
- contralateral arm: **0.89%**

The high-confidence SMPL nonlocal residual is therefore real but substantially smaller than the HUGS Gaussian residual measured under the corresponding hierarchical grouping.

Using the exact HUGS Step 10 totals, the derived high-confidence HUGS values are approximately:

- intended: **87.73%**
- local chain: **6.69%**
- nonlocal: **5.58%**
- contralateral arm: **5.03%**

Thus, for ±10° wrist-z perturbations, the HUGS Gaussian representation shows roughly **2.2x** the normalized nonlocal share and roughly **5.7x** the normalized contralateral-arm share of the SMPL-only vertex control.

## Nonlocal anatomy in SMPL

The SMPL-only residual is not zero. At confidence >= 0.9, the largest nonlocal source is the head (~35% of the small residual). Contralateral right-arm assignments also appear, including right hand, wrist, elbow, and shoulder.

This means cross-body coupling is not exclusively introduced by HUGS. However, its normalized contribution is much smaller in SMPL than in the observed HUGS Gaussian response.

## Interpretation

This is evidence of **amplification**, not yet proof of a HUGS representation failure.

The comparison is not perfectly support-matched:

- SMPL uses 6,890 mesh vertices,
- HUGS uses ~473k Gaussians,
- Gaussian density is spatially nonuniform,
- HUGS applies K=6 blended SMPL/LBS transforms to Gaussian points,
- dominant-joint labels are diagnostic groupings rather than the actual HUGS deformation rule.

Therefore normalized displacement shares can be compared as a useful control, but absolute displacement sums and element counts should not be directly compared across the two representations.

## Artifacts

- `analysis/12G_wrist_z_smpl_only_hierarchical.csv`
- `analysis/12G_wrist_z_smpl_only_nonlocal_top12.csv`
- `analysis/12G_hugs_vs_smpl_wrist_comparison.csv`

The complete SMPL-only vertex arrays and full joint CSV remain in Google Drive.

## Next step

Run the SMPL-only wrist magnitude sweep at ±5°, ±10°, ±20°, and ±30° to match the existing HUGS sweep. If the HUGS-to-SMPL amplification ratio remains stable across magnitude and sign, proceed to a support-matched control using HUGS's actual K=6 blended LBS mapping for Gaussian points.
