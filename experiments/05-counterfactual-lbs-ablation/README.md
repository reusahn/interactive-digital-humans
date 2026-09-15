# Experiment 05 - Counterfactual LBS Ablation

## Question

Does the high-confidence contralateral upper-body response observed under a local left-wrist perturbation depend on small learned HUGS cross-joint wrist/hand LBS components?

## Setup

- pretrained HUGS on NeuMan Seattle
- probe frame index 0, corrected raw NeuMan frame 2
- left-wrist z +10 degree perturbation
- 472,958 Gaussians
- confidence threshold >= 0.9
- corrected contralateral subset includes right collar, shoulder, elbow, wrist, and hand
- N = 33,072 contralateral Gaussians

## Counterfactual conditions

1. original learned HUGS LBS,
2. reconstructed SMPL-derived K=6 target LBS,
3. learned LBS with only left-wrist and left-hand channels removed on the corrected contralateral subset and rows renormalized.

All canonical Gaussians, pose transforms, geometry, shape, scale, translation, and weights outside the intervention subset are held fixed.

## Validation

An independent reconstruction of the original learned-LBS HUGS deformation reproduced the saved probe with displacement correlation `0.9999999992187057`. Mean before/after xyz errors were approximately `2.36e-7`.

## Result

| Condition | HC total displacement | Intended % | Local chain % | Nonlocal % | Contralateral sum | Contralateral % |
|---|---:|---:|---:|---:|---:|---:|
| learned | 82.779138 | 87.735388 | 6.688420 | 5.576191 | 4.163577 | 5.029741 |
| K6 target | 79.344404 | 91.804267 | 7.888879 | 0.306854 | 0.007556 | 0.009523 |
| wrist/hand ablated | 78.615561 | 92.381962 | 7.042647 | 0.575391 | 0.000000 | 0.000000 |

Primary effect:

- K6 target reduces contralateral displacement by **99.8185%** relative to learned LBS.
- Selectively removing learned left-wrist/hand channels from the contralateral subset reduces measured contralateral displacement by **100%** in this fixed perturbation.
- All 33,072 contralateral Gaussians show reduced displacement.
- Removed learned wrist/hand mass correlates with displacement reduction at **r = 0.981289**.

## Interpretation

This is direct causal evidence within this Seattle/raw-frame-2 counterfactual that the learned cross-joint wrist/hand LBS component mediates the amplified contralateral response. It is not yet evidence that the same mechanism generalizes across all HUGS frames, sequences, joints, or Gaussian-human methods.

The zero residual under selective ablation is consistent with the LBS structure: once the only channels whose transforms change under the perturbation are removed for a Gaussian, that perturbation pathway is eliminated. The scientifically important result is that HUGS learned those unexpected cross-joint channels despite the corresponding K=6 target being essentially zero, and that those channels quantitatively account for the observed cross-body motion.

## Data

Compact summary:

- [`analysis/14E_corrected_counterfactual_summary.csv`](analysis/14E_corrected_counterfactual_summary.csv)

Large/raw arrays remain in Google Drive:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/05-counterfactual-lbs-ablation/14E_corrected_counterfactual_displacements.npz
/content/drive/MyDrive/interactive-digital-humans/experiments/05-counterfactual-lbs-ablation/14E_metadata.json
```

## Next step

Replicate the same counterfactual across raw Seattle evaluation frames `[2, 7, 12, 17]` before designing a locality-preserving regularizer.
