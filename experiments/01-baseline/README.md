# Experiment 01 — HUGS Deformation Locality Baseline

## Research question

> **How local is local control in an existing real-time Gaussian human representation?**

This experiment probes whether small, controlled SMPL joint rotations in HUGS remain anatomically local in Gaussian space or produce measurable non-target displacement.

The baseline is **HUGS: Human Gaussian Splats (CVPR 2024)** using the pretrained NeuMan **Seattle** sequence.

Official upstream implementation:
https://github.com/apple-aiml-research/ml-hugs

## Status

**Baseline v1 completed.**

- 36 saved probe measurements
- 472,958 human Gaussians in the analyzed Seattle frame
- left wrist magnitude/sign sweep
- x/y/z axis comparison
- joint sweep across left wrist, elbow, shoulder, knee, and ankle
- kinematic-subtree leakage re-analysis
- joint-assignment confidence sensitivity analysis
- raw NPZ outputs archived in Google Drive
- compact tables, figures, and interpretation versioned in this repository

See `results.md` for the measured values and `DATA_MANIFEST.md` for raw-data storage.

## Core probe

For a selected validation frame, the probe:

1. loads the pretrained HUGS human checkpoint,
2. evaluates the original pose,
3. perturbs one SMPL joint by a controlled signed angle around x, y, or z,
4. recomputes posed Gaussian locations,
5. stores per-Gaussian before/after positions and semantic/joint metadata,
6. measures displacement inside and outside an anatomically expected target subtree.

The raw NPZ record contains:

```text
xyz_before
xyz_after
xyz_canon
region_id
dominant_joint
joint_confidence
nearest_vertex
```

## Semantic / joint assignment

Each canonical Gaussian is associated with the nearest canonical SMPL vertex. The vertex's LBS weights provide a dominant SMPL joint and confidence score.

A coarse semantic mapping is retained for diagnostics, but the main joint comparison uses **kinematic descendants** rather than the original coarse body-region mask.

Examples:

```text
wrist    -> wrist + hand
elbow    -> elbow + wrist + hand
shoulder -> shoulder + elbow + wrist + hand
ankle    -> ankle + foot
knee     -> knee + ankle + foot
```

This prevents expected descendant motion from being misclassified as leakage.

## Leakage metric

For per-Gaussian displacement magnitude `d_i`:

```text
TargetChange  = sum(d_i for i in expected target subtree)
OutsideChange = sum(d_i for i outside the target subtree)

LeakageRatio = OutsideChange / (TargetChange + OutsideChange)
```

Lower leakage is not automatically better, so target displacement is always reported beside leakage.

Additional diagnostics include:

- mean target and outside displacement,
- outside P99 and maximum displacement,
- active fractions,
- dominant-joint confidence,
- confidence-threshold sensitivity.

## Baseline v1 findings

Within **Seattle / frame 0**, the strongest current pattern is articulation dependence.

- left ankle z: **26.57%** leakage
- left ankle x: **18.19%**
- left wrist z: **11.21%**
- left wrist y: **10.27%**
- left wrist x: **9.90%**
- left shoulder x/y/z: only **0.91% / 0.66% / 0.58%**

The distal-versus-proximal pattern remains visible after filtering to joint-assignment confidence ≥ 0.9.

The wrist-specific sweep also shows:

- approximately sign-symmetric behavior,
- approximately linear displacement growth with perturbation magnitude,
- nearly constant z-axis leakage ratio around 11.21% across ±5° to ±30°,
- measurable axis dependence at ±10°.

These are baseline observations, not yet a general claim about HUGS, because the current study covers one sequence and one frame.

## Repository structure

```text
experiments/01-baseline/
├── README.md
├── DATA_MANIFEST.md
├── environment.md
├── semantic_regions.py
├── locality_metrics.py
├── hugs_locality_probe.py
├── results.md
├── analysis/
│   ├── joint_axis_leakage.csv
│   ├── confidence_sensitivity.csv
│   └── joint_assignment_counts.csv
└── figures/
    └── baseline analysis figures
```

Raw `*.npz` outputs intentionally remain in Google Drive because they are large and are the authoritative source for later re-analysis.

## Run

```bash
cd experiments/01-baseline

python hugs_locality_probe.py \
  --hugs-root /path/to/ml-hugs \
  --output-dir /path/to/HUGS_OUTPUT_DIR \
  --frame 0 \
  --joint left_wrist \
  --axis z \
  --degrees 10 \
  --save-dir probe_results
```

See `environment.md` for setup details.

## Current research hypothesis

A defensible next question is:

> **Why do distal articulations in this HUGS baseline produce substantially greater non-local Gaussian displacement than proximal articulations, and can deformation be made more anatomically local without sacrificing rendering or animation quality?**

Before proposing a new method, the next analysis should spatially localize the highest-leakage Gaussians and compare their observed displacement with expected LBS influence.

## Limitations of Baseline v1

- one NeuMan sequence,
- one validation frame,
- left-side joints in the main joint comparison,
- representation-space displacement rather than perceptual/image-space artifacts,
- hard dominant-joint assignment used for diagnostic grouping,
- no competing method yet.

The raw Drive archive should be preserved so all metrics can be recomputed without rerunning the expensive HUGS probe.
