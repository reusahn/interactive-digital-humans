# Experiment 03 — SMPL-Only Control

## Question

Does the non-local wrist response observed in the HUGS Gaussian representation already exist in the underlying SMPL deformation, or is it amplified after mapping deformation to Gaussians?

## Setup

- NeuMan Seattle, frame 0
- SMPL neutral model, cleaned from the licensed legacy PKL for modern loading
- Seattle SMPL parameters from `smpl_optimized_aligned_scale.npz`
- left wrist z perturbations
- vertex groups defined from the true SMPL LBS weights by dominant joint
- high-confidence condition: dominant LBS weight >= 0.9
- hierarchy: `intended = left_wrist + left_hand`, `local_chain = left_elbow + left_shoulder + left_collar`, `nonlocal = remainder`

Large vertex NPZ outputs and plot files remain in Google Drive under:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/03-smpl-only-control/
```

## Step 12G — ±10° SMPL-only control

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

The SMPL-only residual is therefore real but substantially smaller than the corresponding HUGS Gaussian residual.

The SMPL high-confidence nonlocal residual is not empty. Its largest source is the head at roughly 35% of the small residual, and right-arm assignments also appear. Therefore cross-body coupling is not exclusively introduced by HUGS.

## Step 12H — Matched magnitude sweep

The SMPL-only control was extended to the same left-wrist z perturbation sweep used for HUGS:

```text
±5°, ±10°, ±20°, ±30°
```

### SMPL-only

Across the sweep, high-confidence SMPL nonlocal displacement changes gradually from **2.56% at -30°** to **2.39% at +30°**. The contralateral-arm share stays tightly clustered near **0.87–0.89%**.

### HUGS Gaussians

The corresponding HUGS values are almost invariant across magnitude and sign:

- nonlocal share: approximately **5.576–5.581%**
- contralateral-arm share: approximately **5.029–5.031%**

### Amplification ratio

Across all eight signed perturbations:

- HUGS / SMPL nonlocal amplification = **2.176x to 2.330x**, mean **2.240x**
- HUGS / SMPL contralateral-arm amplification = **5.652x to 5.773x**, mean **5.689x**

The amplification therefore survives both sign changes and a six-fold variation in perturbation magnitude.

This is stronger evidence that the HUGS Gaussian deformation pipeline preserves a systematically larger normalized nonlocal and cross-body response than the SMPL mesh control. It is still evidence of **amplification**, not proof that the Gaussian representation itself is the sole cause.

## Interpretation

The current result supports three statements:

1. SMPL itself is not perfectly local under this diagnostic, so some nonlocal response is inherited from the body model / skinning system.
2. HUGS exhibits a substantially larger normalized residual, especially in the contralateral arm.
3. The HUGS-to-SMPL gap is stable across perturbation magnitude and sign, making a random numerical artifact explanation unlikely.

The comparison is not yet perfectly support-matched:

- SMPL uses 6,890 mesh vertices,
- HUGS uses approximately 473k Gaussians,
- Gaussian density is spatially nonuniform,
- HUGS applies K=6 blended SMPL/LBS transforms to Gaussian points,
- dominant-joint labels are diagnostic groupings rather than HUGS's actual deformation rule.

Therefore normalized displacement shares are a useful control, but element counts and absolute displacement sums should not be compared directly between the two representations.

## Artifacts

- `analysis/12G_wrist_z_smpl_only_hierarchical.csv`
- `analysis/12G_wrist_z_smpl_only_nonlocal_top12.csv`
- `analysis/12G_hugs_vs_smpl_wrist_comparison.csv`
- `analysis/12H_wrist_z_smpl_magnitude_sweep.csv`
- `analysis/12H_wrist_z_hugs_vs_smpl_magnitude.csv`

Drive also contains:

- `12G_wrist_z_smpl_only_vertices.npz`
- `12H_nonlocal_hugs_vs_smpl.png/.svg`
- `12H_contralateral_hugs_vs_smpl.png/.svg`

## Next step

Move to a support-matched diagnostic using HUGS's actual K=6 Gaussian-to-SMPL mapping. Reconstruct the effective 24-dimensional LBS weight vector for every saved HUGS Gaussian from `xyz_canon`, the HUGS Vitruvian SMPL template, and the official K=6 weighting rule. Then test whether the Gaussians producing the contralateral residual receive unexpected left-wrist / left-arm influence through the mapping itself.
