# Experiment 01 — Reproduce and Probe a Gaussian Human Baseline

## Objective

Establish a working animatable Gaussian-human baseline and test one specific research question:

> **How local is local control in an existing avatar representation?**

Before introducing a new model, we need to measure how much a targeted body-region change propagates into unrelated parts of the avatar.

## Preferred baseline

Start with **HUGS (Human Gaussian Splats, CVPR 2024)** because the official implementation is available and already includes evaluation for PSNR, SSIM, and LPIPS.

Paper:
https://openaccess.thecvf.com/content/CVPR2024/html/Kocabas_HUGS_Human_Gaussian_Splats_CVPR_2024_paper.html

Code:
https://github.com/apple/ml-hugs

Alternative if HUGS installation becomes a blocker:

GaussianAvatar:
https://github.com/aipixel/GaussianAvatar

## Experiment stages

### E1.1 — Reproduce pretrained output

Goal: verify the software stack and renderer.

Record:
- GPU
- CUDA version
- PyTorch version
- dataset/sequence
- checkpoint
- render resolution
- FPS
- VRAM
- PSNR
- SSIM
- LPIPS

Success condition:
- reproduce visually plausible output,
- metrics are in the approximate range expected by the original implementation,
- render/evaluation scripts run without manual intervention.

### E1.2 — Inspect representation structure

For each Gaussian, determine what information is available or derivable:

- canonical position,
- current posed position,
- scale,
- rotation,
- opacity,
- appearance coefficients/features,
- skinning weights,
- nearest SMPL vertex/face,
- body-part label.

Output a diagnostic file or visualization where Gaussians are colored by body region.

Suggested coarse labels:

```text
head
left_arm
right_arm
torso
left_leg
right_leg
left_hand
right_hand
```

If hands cannot be separated reliably from the SMPL representation, document that limitation rather than hiding it.

### E1.3 — Semantic selection test

Implement functions equivalent to:

```python
select_gaussians(region="left_hand")
select_gaussians(region="head")
```

This is not yet a machine-learning contribution. It is instrumentation needed for the research.

Record:
- number of Gaussians per region,
- boundary ambiguity,
- whether Gaussians move between semantic regions under pose changes.

### E1.4 — Controlled local perturbation

Apply a deliberately small synthetic perturbation to one semantic region, for example left forearm/hand.

Candidate perturbations:
- translation,
- rotation,
- scale,
- position offset field.

Render before/after from multiple views.

We are not trying to make the perturbation realistic. We are measuring representation coupling.

### E1.5 — Leakage measurement

Define target region `T` and non-target region `N`.

For a representation-space change magnitude `Δg_i`, compute:

```text
TargetChange = sum(Δg_i for i in T)
OutsideChange = sum(Δg_i for i in N)
LeakageRatio = OutsideChange / (TargetChange + OutsideChange)
```

Also calculate an image-space version using masks:

```text
ImageLeakage = changed pixels outside target mask / all changed pixels
```

These metrics are prototypes and may be replaced after inspecting failure modes.

### E1.6 — Pose generalization check

Repeat the same local control operation under:
- one training-like pose,
- one moderately novel pose,
- one extreme novel pose.

Question:

Does semantic locality remain stable as articulation changes?

## Why this experiment matters

If current representations already allow robust, clean local control, the proposed research gap becomes weaker and we should move toward social/physical interaction modeling instead.

If local control causes significant leakage, instability, or semantic drift, we have an experimentally grounded problem to work on.

## Files to produce

```text
experiments/01-baseline/
├── README.md
├── environment.md
├── results.md
├── metrics.json
├── figures/
└── notes/
```

Do not commit large pretrained weights or licensed datasets to this repository.

## First decision gate

Proceed to a new semantically anchored representation only if at least one reproducible limitation appears in:

- local edit leakage,
- semantic correspondence across poses,
- contact-region control,
- temporal stability,
- end-to-end response latency.

The experiment is allowed to invalidate the proposed research direction. That is a valid research result at this stage.
