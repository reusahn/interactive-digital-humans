# Experiment 04 Figures

## Step 13E

- `13E_wrist_weight_target_vs_learned.svg` compares the K=6 regularization target against the checkpoint-reconstructed learned left-wrist + left-hand LBS influence for the high-confidence nonlocal, high-confidence contralateral, and top-5%-displacement nonlocal subsets. The vertical scale is logarithmic.
- `13E_displacement_supported_by_learned_wrist.svg` shows the fraction of subset displacement carried by Gaussians whose learned left-wrist + left-hand weight exceeds `1e-3` or `1e-2`. It also records the Spearman association between learned wrist influence and observed displacement.

These figures are compact GitHub-side visual summaries derived from the exact numerical outputs archived in `analysis/13E_learned_vs_k6_key_summary.csv`. The authoritative full learned-LBS array remains in Google Drive at:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/04-k6-support-mapping/13E_learned_lbs_weights.npz
```
