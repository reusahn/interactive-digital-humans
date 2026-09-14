# Experiment 04 - HUGS K=6 Support Mapping and Learned-LBS Mechanism

## Question

Can the stable contralateral wrist response observed in the HUGS Gaussian representation be explained by the SMPL-derived K=6 support target, or does the learned HUGS deformation field introduce additional cross-joint influence?

## Setup

- NeuMan Seattle, frame 0
- original HUGS `left_wrist z +10 deg` probe
- 472,958 Gaussians
- licensed SMPL neutral model, cleaned for modern loading
- Seattle shape parameters from `smpl_optimized_aligned_scale.npz`
- exact official Seattle `human_final.pth` checkpoint
- exact packaged `config_train.yaml`
- reconstructed K=6 SMPL support target
- directly reconstructed checkpoint triplane, geometry decoder, and deformation decoder

Large binary arrays and licensed/private assets remain in Google Drive. Compact tables, figures, manifests, and interpretation are archived here.

## Step 13A - K=6 support-target reconstruction

Artifacts:

- [K=6 support summary](analysis/13A_k6_support_summary.csv)
- authoritative raw mapping in Drive: `experiments/04-k6-support-mapping/13A_k6_effective_mapping.npz`

### Reconstruction validation

The reconstructed Vitruvian SMPL support geometry reproduces the original saved diagnostic assignment extremely closely:

- nearest-vertex exact match: **0.9998583384**
- dominant-joint exact match: **1.0**
- maximum dominant-joint confidence error: **0.0**

### High-confidence contralateral subset

- Gaussian count: **33,072**
- displacement sum: **4.163954**
- mean K=6 left-wrist + left-hand weight: **4.8793e-7**
- displacement-weighted K=6 wrist/hand weight: **5.7222e-7**
- displacement from points with K=6 wrist/hand influence > `1e-3`: **0.0**
- mean K=6 right-upper-limb weight: **0.995266**

The K=6 support target therefore does not explain the cross-body response through accidental direct left-wrist support on right-arm Gaussians.

## Steps 13B-13D - Exact checkpoint provenance and config

Artifact:

- [Checkpoint manifest](analysis/13D_checkpoint_manifest_summary.json)

The original baseline metadata records:

```text
checkpoint: /content/ml-hugs/output/pretrained_models/seattle/human_final.pth
dataset: neuman
sequence: seattle
num_gaussians: 472958
```

The official Apple pretrained archive was re-downloaded and stored persistently in Drive. The exact Seattle checkpoint is **96.5905657 MiB** with SHA256:

```text
e64d0cab44e8f5b0e0ca2fa4a1e45de2c15deee1fe322839d1da36bf3fb8d8f1
```

The checkpoint `xyz` tensor is **(472958, 3)**, exactly matching the original probe Gaussian count.

The packaged `config_train.yaml` reports:

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

This corrects the earlier assumption that the exact saved config used the current source-tree name `hugs_trimlp`. The packaged checkpoint/config uses the legacy name `hugs_triplane`.

Checkpoint structure:

- three triplane tensors: **1 x 32 x 256 x 256**
- deformation decoder: **48,664 parameters**
- skinning output: **24 channels**
- `use_deformer: true`
- `disable_posedirs: true`

Because the current source tree no longer exposes the legacy `hugs_triplane` name directly, the checkpoint forward path was reconstructed from the saved tensor states rather than through a current trainer alias.

## Step 13E - Actual learned per-Gaussian LBS weights

Artifacts:

- [Learned-vs-K6 key summary](analysis/13E_learned_vs_k6_key_summary.csv)
- [Forward-path validation](analysis/13E_forward_validation.csv)
- [Target vs learned wrist influence](figures/13E_wrist_weight_target_vs_learned.svg)
- [Displacement supported by learned wrist influence](figures/13E_displacement_supported_by_learned_wrist.svg)
- authoritative full learned weights in Drive: `experiments/04-k6-support-mapping/13E_learned_lbs_weights.npz`

### Forward-path validation

The checkpoint triplane and geometry decoder were reconstructed directly and tested against the original saved `xyz_canon` from the HUGS probe.

- mean canonical XYZ error: **2.1164e-8**
- p99 canonical XYZ error: **6.6744e-8**
- maximum canonical XYZ error: **1.3349e-7**
- learned LBS maximum row-sum error: **2.9802e-7**
- learned LBS NaN count: **0**
- forward validation: **PASS**

This makes the learned-LBS export a direct reconstruction of the checkpoint forward path rather than an architectural approximation.

### High-confidence nonlocal subset

- Gaussian count: **171,896**
- K=6 mean wrist/hand weight: **4.2667e-6**
- learned mean wrist/hand weight: **7.0759e-5**
- mean learned/K6 increase: **16.58x**
- K=6 displacement-weighted wrist/hand weight: **5.4439e-7**
- learned displacement-weighted wrist/hand weight: **0.004146**
- displacement-weighted increase: **7616.5x**
- displacement from Gaussians with learned wrist/hand weight > `1e-3`: **70.90%**
- displacement from Gaussians with learned wrist/hand weight > `1e-2`: **5.86%**
- Spearman learned wrist influence vs displacement: **0.8303**

### High-confidence contralateral subset

- Gaussian count: **33,072**
- displacement sum: **4.163954**
- K=6 mean wrist/hand weight: **4.8793e-7**
- learned mean wrist/hand weight: **0.000317262**
- mean learned/K6 increase: **650.22x**
- K=6 displacement-weighted wrist/hand weight: **5.7222e-7**
- learned displacement-weighted wrist/hand weight: **0.00425322**
- displacement-weighted increase: **7432.88x**
- displacement from Gaussians with learned wrist/hand weight > `1e-3`: **72.76%**
- displacement from Gaussians with learned wrist/hand weight > `1e-2`: **5.77%**
- learned right-upper-limb weight: **0.996699**
- K=6 right-upper-limb weight: **0.995266**
- learned-vs-target mean L1 distance: **0.0234233**
- learned-vs-target dominant-joint mismatch: **0.0**
- Spearman learned wrist influence vs displacement: **0.996939**

The striking point is that these Gaussians remain overwhelmingly right-arm weighted and retain the same dominant anatomical assignment, yet the learned model introduces a small left-wrist/hand component that is almost perfectly rank-correlated with the observed contralateral displacement.

### Highest-displacement nonlocal subset

For the top 5% of high-confidence nonlocal Gaussians by displacement:

- K=6 mean wrist/hand weight: **9.5728e-7**
- learned mean wrist/hand weight: **0.00128138**
- mean learned/K6 increase: **1338.56x**
- learned displacement-weighted wrist/hand weight: **0.00453406**
- displacement from Gaussians with learned wrist/hand weight > `1e-3`: **77.68%**
- Spearman learned wrist influence vs displacement: **0.973174**

## Current interpretation

Step 13E provides strong mechanism-level evidence that the learned deformation field is associated with the stable cross-body amplification observed in the wrist perturbation diagnostic.

The result is stronger than a simple dominant-joint misassignment explanation:

1. the K=6 target gives contralateral Gaussians essentially zero direct left-wrist/hand support,
2. the learned checkpoint introduces measurable left-wrist/hand weight on those same right-arm Gaussians,
3. the learned wrist influence is extremely strongly associated with observed contralateral displacement,
4. the learned and target dominant joints still agree for the contralateral subset,
5. the right-arm aggregate weight remains near 1.0.

The defensible statement at this stage is:

> In this Seattle/frame-0 wrist-z diagnostic, the pretrained HUGS learned deformation field introduces small cross-joint LBS components that are strongly associated with the amplified contralateral Gaussian response relative to the SMPL-derived K=6 target and SMPL-only control.

This is still an association plus a mechanistic candidate, not yet a causal ablation. A small learned wrist weight can produce visible displacement because the wrist transform acts at a large spatial lever arm on a distant right-arm Gaussian.

## Next step - causal counterfactual ablation

The next experiment should keep the same canonical Gaussians, pose transforms, and checkpoint geometry fixed, while changing only the LBS weights:

1. run the original learned-LBS deformation,
2. replace learned LBS with the reconstructed K=6 target,
3. optionally zero only the learned left-wrist + left-hand channels on contralateral Gaussians and renormalize,
4. compare contralateral displacement under the same `left_wrist z +10 deg` perturbation.

If the contralateral response collapses toward the K=6/SMPL control after this substitution, that will provide direct causal evidence that learned cross-joint skinning weights drive the observed amplification.
