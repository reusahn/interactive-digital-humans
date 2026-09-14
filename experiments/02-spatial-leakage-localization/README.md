# Experiment 02 — Spatial Leakage Localization

This experiment re-analyzes the archived HUGS Baseline v1 NPZ outputs to localize non-target deformation and test whether the observed leakage is dominated by isolated outliers or by structured anatomical regions.

## Step 7 — Leakage concentration and anatomical source analysis

Artifacts:

- `analysis/07_anatomical_leakage_groups.csv`
- `analysis/07_leakage_concentration.csv`
- `figures/07_leakage_concentration.png`

Main observation: outside displacement is strongly heavy-tailed but not reducible to a tiny handful of extreme points. Across ankle, wrist, and shoulder probes, the top 5% of non-target Gaussians account for roughly 83–85% of outside displacement, while the top 0.1% account for only roughly 6–13%. This supports a structured high-displacement subset rather than a single-outlier explanation.

Anatomically, ankle leakage is dominated by the upstream same-side leg, while wrist and shoulder probes show large same-side upstream components together with notable contralateral upper-limb components.

These observations are diagnostic only. They do not yet establish whether the pattern is expected from skinning weights or reflects representation-specific deformation error.
