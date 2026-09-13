# Experiment 01 — HUGS Semantic Locality Probe

## Research question

> **How local is local control in an existing real-time Gaussian human representation?**

The purpose of this experiment is not to claim a new method yet. It is to test whether the representation-side research gap actually exists.

Our first baseline is **HUGS: Human Gaussian Splats (CVPR 2024)**. HUGS initializes its human representation from SMPL and transports canonical Gaussians through pose-dependent skinning. That makes it a useful baseline for asking whether interaction-relevant body regions remain spatially and semantically local.

Official upstream implementation:
https://github.com/apple-aiml-research/ml-hugs

## Hypothesis under test

A representation designed mainly for reconstruction and pose-driven animation may not provide sufficiently stable local structure for interaction-specific control.

We test this with deliberately small joint perturbations before introducing any learned interaction module.

## Why the probe is semantic

We assign every canonical Gaussian to a coarse semantic region without training a segmentation network.

1. Find the nearest canonical SMPL vertex to each Gaussian.
2. Read that SMPL vertex's LBS weights.
3. Take the dominant SMPL joint.
4. Map the joint to a coarse region.

Current regions:

```text
torso
head
left_arm
right_arm
left_hand
right_hand
left_leg
right_leg
```

This layer is diagnostic instrumentation, not the proposed contribution.

## First perturbation

Default probe:

```text
joint: left_wrist
axis: z
angle: 10 degrees
```

We render/compute the avatar once with the original validation pose and once after adding the small wrist rotation. Canonical semantic labels stay fixed. We then measure how much posed Gaussian displacement occurs inside and outside the intended target region.

## Prototype locality metric

For per-Gaussian displacement magnitude `d_i`:

```text
TargetChange  = sum(d_i for i in target region)
OutsideChange = sum(d_i for i outside target region)

LeakageRatio = OutsideChange / (TargetChange + OutsideChange)
```

Lower leakage is not automatically better. A representation that fails to execute the target motion could also score low, so target displacement is always reported beside leakage.

Additional diagnostics:

- mean target displacement,
- mean outside displacement,
- maximum target/outside displacement,
- active fraction inside/outside the target region,
- dominant-joint confidence for semantic assignment.

## Implemented files

```text
experiments/01-baseline/
├── README.md
├── environment.md
├── semantic_regions.py
├── locality_metrics.py
├── hugs_locality_probe.py
└── results.md
```

### `semantic_regions.py`

Builds the non-learning Gaussian-to-SMPL semantic assignment using canonical positions and SMPL LBS weights.

### `locality_metrics.py`

Computes representation-space displacement and locality/leakage statistics.

### `hugs_locality_probe.py`

Loads an actual HUGS experiment/checkpoint through the upstream `GaussianTrainer`, takes a validation frame, applies a controlled SMPL joint perturbation, and saves JSON + NPZ outputs.

## Run

First reproduce the upstream HUGS evaluation in its own environment. Then:

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

## Minimum experiment sweep

A single clean example is not evidence. The initial study should include at least:

```text
joints: left_wrist, right_wrist, head, left_elbow, right_elbow
axes: x, y, z
angles: 5°, 10°, 20°
frames: >= 10 validation poses distributed across the sequence
```

Then examine:

1. whether leakage rises with articulation magnitude,
2. whether wrists/shoulders and other semantic boundaries fail more often,
3. whether low semantic-assignment confidence predicts leakage,
4. whether the behavior changes across training-like versus difficult poses.

## Decision gate

### If HUGS is already robust

Do **not** invent a new semantic Gaussian representation just because that was the original idea. Move Project 001 toward contact response, interaction behavior, or social/physical coupling.

### If failure is localized to boundaries

Investigate a smaller contribution: interaction anchors, topology-aware semantic boundaries, or local contact fields.

### If semantic/local control degrades broadly

Then a structured interaction-ready 4D human representation becomes a defensible research direction.

## What is not done yet

- no GPU measurements have been run from this repository yet,
- no benchmark values have been fabricated,
- no new model is claimed,
- image-space leakage and rendered before/after figures are still pending.

The next legitimate result is an actual locality sweep on a pretrained HUGS checkpoint.
