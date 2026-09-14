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

The reconstructed K=6 support interpolation does **not** explain the observed contralateral response through direct left-wrist / left-hand LBS influence. The contralateral subset is overwhelmingly supported by right-upper-limb SMPL weights while still moving under a left-wrist perturbation.

This rules out a simple mechanism in which Gaussian K=6 support accidentally assigns substantial left-wrist skinning weight to the right arm.

However, this is not yet a causal explanation of the HUGS response.

Under `use_deformer: true`, HUGS uses deformation-decoder **learned LBS weights** for the actual Gaussian deformation path. The SMPL-derived K=6 weights are computed as a target for LBS regularization. Step 13A is therefore a support-target diagnostic, not the model's actual learned deformation-weight path.

## Steps 13B–13C — Exact checkpoint provenance recovered

The original probe metadata records the checkpoint that produced the baseline NPZ files as:

```text
/content/ml-hugs/output/pretrained_models/seattle/human_final.pth
```

with:

```text
dataset: neuman
sequence: seattle
frame_index: 0
joint: left_wrist
axis: z
degrees: 10.0
num_gaussians: 472958
```

The original runtime path no longer existed after the Colab reset, so the official Apple pretrained archive was downloaded once and stored persistently in Google Drive. Persistent copies now live at:

```text
/content/drive/MyDrive/interactive-digital-humans/assets/hugs/pretrained_models/seattle/human_final.pth
/content/drive/MyDrive/interactive-digital-humans/assets/hugs/pretrained_models/seattle/config_train.yaml
```

The exact `human_final.pth` is **96.5905657 MiB** and has SHA256:

```text
e64d0cab44e8f5b0e0ca2fa4a1e45de2c15deee1fe322839d1da36bf3fb8d8f1
```

The complete official pretrained ZIP is retained in Drive for reproducibility but is not committed to GitHub.

## Step 13D — Exact saved config and checkpoint structure

Artifact:

- `analysis/13D_checkpoint_manifest_summary.json`

The exact packaged Seattle `config_train.yaml` reports:

```text
mode: human_scene
human.name: hugs_triplane
human.use_deformer: true
human.disable_posedirs: true
human.n_subdivision: 2
human.triplane_res: 256
human.canon_pose_type: da_pose
human.optim_betas: false
human.optim_pose: true
human.optim_trans: true
human.loss.lbs_w: 1000.0
```

This corrects the earlier assumption that the exact saved config used the current source-tree name `hugs_trimlp`. The packaged checkpoint/config uses the legacy name **`hugs_triplane`**.

The current HUGS source tree no longer contains a `hugs_triplane.py` model file, but the checkpoint itself contains the expected triplane and deformation-decoder state:

- `xyz`: **472,958 × 3**, exactly matching the original probe Gaussian count
- triplane tensors: three **1 × 32 × 256 × 256** planes
- deformation decoder: **48,664 parameters**
- output skinning layer: **24 channels**

The deformation-decoder tensor layout matches the current triplane/deformer architecture closely enough that the learned LBS weights can be reconstructed directly from the checkpoint state without relying on current trainer model-name aliases. This direct reconstruction is preferable because feeding the legacy `human.name: hugs_triplane` config to the current trainer may not reproduce the historical name mapping.

## Next step

Reconstruct the triplane and deformation decoder directly from `human_final.pth` and export the **actual learned per-Gaussian LBS weights** for all 472,958 Gaussians.

The primary comparison is learned LBS versus the Step 13A K=6 target in the high-confidence contralateral residual subset. If those right-arm Gaussians carry anomalous learned left-wrist / left-hand influence despite near-zero K=6 target influence, the learned deformer provides a direct candidate mechanism for the cross-body amplification. If they do not, proceed to the full learned transform construction.
