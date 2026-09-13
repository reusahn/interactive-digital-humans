# HUGS Implementation Notes for Project 001

This note translates the first research question into a practical modification plan for the official HUGS implementation.

Official code:
https://github.com/apple/ml-hugs

## What the public implementation already exposes

The released HUGS configuration contains human-model controls for:

- Gaussian position, opacity, scale, rotation, and appearance learning rates,
- SMPL spatial parameters,
- pose / beta / translation optimization,
- LBS weight optimization,
- optional surface and deformer modes,
- canonical-pose settings,
- KNN neighborhood settings,
- densification and pruning.

Relevant public config:
https://github.com/apple/ml-hugs/blob/main/hugs/cfg/config.py

The NeuMan loader exposes SMPL parameters including body pose, global orientation, translation, scale, and betas, and loads segmentation masks used for separating the human from the scene.

Relevant loader:
https://github.com/apple/ml-hugs/blob/main/hugs/datasets/neuman.py

These properties make HUGS a reasonable diagnostic baseline for asking whether Gaussian primitives can be associated with stable semantic body regions.

## First modification should be non-learning

Do **not** begin by training a new network.

The first instrumentation layer should assign every canonical Gaussian a semantic body-region label derived from the nearest SMPL surface element or its dominant skinning influence.

Conceptually:

```text
canonical Gaussian
      ↓
nearest SMPL vertex / face
      ↓
SMPL body-region lookup
      ↓
semantic label
```

Initial labels can remain coarse:

```text
HEAD
TORSO
LEFT_UPPER_ARM
LEFT_LOWER_ARM
RIGHT_UPPER_ARM
RIGHT_LOWER_ARM
LEFT_UPPER_LEG
LEFT_LOWER_LEG
RIGHT_UPPER_LEG
RIGHT_LOWER_LEG
LEFT_HAND_REGION
RIGHT_HAND_REGION
```

HUGS uses standard SMPL rather than SMPL-X, so fine hand/finger and face semantics should **not** be assumed at this stage. That limitation is itself informative for the longer-term representation choice.

## Why canonical-space labeling

Labels should first be assigned in canonical space rather than independently for each posed frame.

Reason:

- the research question requires semantic identity of a region to persist across motion,
- per-frame nearest-neighbor labeling may silently reassign Gaussians after deformation,
- stable canonical labels let us explicitly measure when articulation breaks spatial correspondence.

## Diagnostic data to export

For every Gaussian, create an experiment-side table such as:

```text
gaussian_id
canonical_xyz
semantic_region
nearest_smpl_vertex
nearest_smpl_face
skinning_weight_vector
max_skinning_joint
```

If some fields are inaccessible in the implementation, record them as unavailable rather than reconstructing them from assumptions.

## Visualization 01 — semantic colors

Render the canonical and posed avatar with flat diagnostic colors by semantic region.

The goal is not visual quality. We want to inspect:

- whether clothing/hair Gaussians inherit plausible body labels,
- whether boundary regions flicker or become ambiguous,
- whether off-body Gaussians remain semantically attached under articulation.

## Visualization 02 — interaction neighborhood

Select a semantic region and define an interaction anchor.

First anchors:

```text
head center
left wrist / hand proxy
right wrist / hand proxy
chest
```

For each anchor, visualize Gaussian distance bands in canonical space and posed space.

This lets us see whether a fixed semantic neighborhood remains spatially coherent as the body articulates.

## Perturbation experiment

Start with a synthetic local change, not a learned behavior.

Example:

```text
Target: LEFT_LOWER_ARM + LEFT_HAND_REGION
Operation: small rigid rotation or position offset
```

Render multiple views and compare:

1. target-region change,
2. non-target change,
3. silhouette artifacts,
4. appearance discontinuity,
5. behavior under a novel body pose.

## First useful negative result

A useful finding would be something like:

> Canonical semantic assignments remain stable, but local geometric manipulation creates visible discontinuities at skinning/appearance boundaries.

or

> Gaussians representing loose clothing deviate sufficiently from SMPL that nearest-surface semantics become unreliable during novel poses.

Either result gives a concrete next problem. It is stronger than starting by claiming a new architecture without measuring an existing failure.

## Likely follow-up if HUGS semantics are insufficient

DAMA is a strong comparison because its public pipeline explicitly trains segmentation Gaussians, performs topology-aware label refinement, and constructs body-anchored, semantically separated garment layers.

Code:
https://github.com/danieleskandar/DAMA-code

This makes DAMA useful for testing whether structured semantic anchoring fixes the failure observed in HUGS, even though DAMA's original target is clothing rather than general human interaction.

## Decision logic

```text
HUGS semantic labeling works cleanly
    ↓
Test interaction locality directly

HUGS semantic labeling fails because of body-relative ambiguity
    ↓
Compare a structured/body-anchored representation such as DAMA

Both support clean locality
    ↓
Representation is not the main bottleneck; shift Project 001 toward behavior/contact dynamics

Structured model clearly improves locality or stability
    ↓
Investigate an interaction-specific semantic representation
```

This decision structure prevents the project from becoming attached to a preferred answer before the baseline is measured.
