# Experiment 04 — HUGS K=6 Support Mapping Diagnostic

## Question

Can the stable contralateral wrist response observed in the HUGS Gaussian representation be explained by the official K=6 Gaussian-to-SMPL support interpolation used by HUGS?

## Setup

- NeuMan Seattle, frame 0
- saved HUGS canonical Gaussian coordinates from the original `left_wrist z +10°` probe
- 472,958 Gaussians
- licensed SMPL neutral model, cleaned for modern loading
- Seattle shape parameters from `smpl_optimized_aligned_scale.npz`
- reconstructed HUGS Vitruvian SMPL template
- official HUGS K=6 neighbor weighting rule

The authoritative raw K=6 mapping remains in Google Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/04-k6-support-mapping/13A_k6_effective_mapping.npz
```

## Reconstruction validation

The reconstructed Vitruvian template reproduces the original saved diagnostic assignment extremely closely:

- nearest-vertex exact match: **0.9998583384**
- dominant-joint exact match: **1.0**
- maximum dominant-joint confidence error: **0.0**

This is strong evidence that the canonical SMPL geometry used for the support reconstruction matches the original probe geometry closely enough for this diagnostic.

## Step 13A result

Artifact:

- `analysis/13A_k6_support_summary.csv`

For high-confidence nonlocal Gaussians:

- mean effective left-wrist + left-hand weight: **4.27e-6**
- displacement-weighted effective left-wrist + left-hand weight: **5.44e-7**
- fraction of displacement from points with wrist/hand influence > 1e-3: **0.0**
- effective dominant-joint changed fraction: **0.0**

For high-confidence contralateral Gaussians:

- mean effective left-wrist + left-hand weight: **4.88e-7**
- displacement-weighted effective left-wrist + left-hand weight: **5.72e-7**
- fraction of displacement from points with wrist/hand influence > 1e-3: **0.0**
- mean effective right-upper-limb weight: **0.995266**
- effective dominant-joint changed fraction: **0.0**

The top 5% highest-displacement high-confidence nonlocal subset is similarly inconsistent with direct left-wrist influence under the reconstructed K=6 support map.

## Interpretation

The reconstructed K=6 support interpolation does **not** explain the observed contralateral response through direct left-wrist / left-hand LBS influence. The contralateral subset is overwhelmingly supported by right-upper-limb LBS weights while still moving under a left-wrist perturbation.

This rules out a simple mechanism in which Gaussian K=6 support accidentally assigns substantial left-wrist skinning weight to the right arm.

However, this is not yet a causal explanation of the HUGS response.

A critical implementation distinction must now be checked against the exact checkpoint configuration. The official NeuMan HUGS release configuration uses:

```text
human.name: hugs_trimlp
human.use_deformer: true
human.disable_posedirs: true
```

Under `use_deformer: true`, HUGS uses learned deformation-decoder LBS weights for the actual Gaussian deformation path. The K=6 SMPL-derived weights are used as a ground-truth/regularization target rather than as the actual deformation weights. Therefore Step 13A should be interpreted as a support-target diagnostic, not automatically as a reconstruction of the model's true deformation path unless the exact saved checkpoint configuration is verified to use the non-deformer path.

## Next step

Recover or re-download the exact pretrained Seattle HUGS checkpoint and its `config_train.yaml`, verify `use_deformer` and `disable_posedirs`, then export the **actual learned per-Gaussian LBS weights** from `canon_forward()`.

If the saved baseline uses the release `use_deformer: true` path, directly compare learned LBS weights against the reconstructed K=6 target for the high-confidence contralateral residual subset. The key test is whether those right-arm Gaussians carry anomalous learned left-wrist / left-hand influence even though their K=6 target does not.
