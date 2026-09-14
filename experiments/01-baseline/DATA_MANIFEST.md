# Experiment 01 Data Manifest

This file records where the full Baseline v1 data are stored and which artifacts belong in GitHub versus Google Drive.

## Storage policy

GitHub stores reproducible code, compact tables, figures, and written analysis.

Large raw probe arrays (`*.npz`) stay in Google Drive only. Do not delete or move these raw files without updating this manifest.

## Authoritative Google Drive location

Colab-mounted path used during the experiment:

```text
/content/drive/MyDrive/interactive-digital-humans/experiments/01-baseline/
```

Expected archived contents:

```text
01-baseline/
├── hugs_locality_probe.py
├── config_train_seattle.yaml
├── baseline_summary.csv
├── experiment_metadata.json
├── figures/
│   ├── 01_joint_axis_leakage.png
│   ├── 02_high_confidence_leakage.png
│   └── 03_confidence_robustness.png
└── probe_results/
    ├── semantic_assignment.json
    ├── frame000_*_*.json
    └── frame000_*_*.npz
```

The Colab archive step reported `Total experiments: 36` and successfully saved the summary and metadata to this Drive directory.

## Raw NPZ contents

Probe NPZ files contain per-Gaussian arrays used for later re-analysis without rerunning HUGS:

```text
xyz_before       (N, 3)
xyz_after        (N, 3)
xyz_canon        (N, 3)
region_id        (N,)
dominant_joint   (N,)
joint_confidence (N,)
nearest_vertex   (N,)
```

For the Seattle frame-0 baseline, `N = 472,958` Gaussians.

These arrays are the authoritative source for any future locality metric, kinematic-subtree remapping, confidence sensitivity analysis, or spatial leakage visualization.

## Baseline v1 experiment coverage

The 36 saved probe measurements include:

- left-wrist magnitude sweep at ±5°, ±10°, ±20°, ±30° about z,
- left-wrist x/y/z axis tests at ±10°,
- five-joint sweep at ±10° over x/y/z for left wrist, elbow, shoulder, knee, and ankle,
- semantic assignment metadata used to map Gaussians to SMPL joints and coarse regions.

## GitHub copies

GitHub intentionally contains only compact/reproducible derivatives of the Drive archive:

- probe and metric code,
- experiment description and environment notes,
- aggregate CSV tables,
- figures,
- written results and caveats,
- this manifest.

Raw `*.npz` outputs are intentionally excluded because of size.

## Important provenance note

Do not treat reconstructed aggregate tables as a substitute for the Drive NPZ files. If a future analysis changes the definition of target region, kinematic descendants, confidence filtering, or leakage, recompute from the Drive NPZ arrays rather than from screenshots or rounded tables.
