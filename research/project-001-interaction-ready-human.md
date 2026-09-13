# Project 001 — Interaction-Ready 4D Human Representation

_Status: research hypothesis / scoping stage_

## Working title

**Interaction-Ready 4D Humans: Semantically Anchored Real-Time Avatars for Social and Physical Response**

## Core question

> Can a real-time 4D human representation expose semantically meaningful, locally controllable interaction regions while preserving identity, temporal coherence, and rendering quality?

## Motivation

Real-time Gaussian avatars have become fast and visually strong, but most are optimized primarily for reconstruction, novel-view synthesis, or pose-driven animation. Meanwhile, recent social-avatar systems generate realistic conversational reactions, and recent physical-interaction systems model contact or object response.

The proposed project sits between these areas. Instead of treating the renderer as a passive final stage, we ask whether the **human representation itself can be designed as an interface for interaction**.

The initial representation should support explicit regions such as:

- gaze / head,
- face,
- left and right hand,
- torso,
- articulated limbs,
- garments,
- contact patches.

These regions should be addressable by a behavior or interaction controller without globally regenerating the avatar.

## Why this may matter

An interactive avatar needs more than photorealistic rendering. When a user looks at it, touches it, hands it an object, or changes position, the avatar must react while maintaining:

- who it is,
- where its body is,
- how its surface moves,
- what is in contact,
- and what parts should remain unchanged.

A representation without explicit interaction structure pushes all of this burden into a large downstream generator. A structured 4D representation may offer lower latency, stronger spatial consistency, and more interpretable control.

## Hypothesis

### H1 — Semantic anchors improve localized control

A body-anchored Gaussian representation augmented with semantic interaction anchors will allow local pose/deformation/appearance control with less unintended change outside the target region than an unstructured deformation model.

### H2 — Local response can preserve global identity

Local interaction updates can be applied while maintaining stable global identity and appearance, avoiding the drift that can occur in full-frame autoregressive/video generation.

### H3 — Hybrid structure will outperform a purely free Gaussian cloud for interaction

A hybrid representation using articulated body topology for transport and explicit/free Gaussians for appearance and non-rigid detail may provide a better trade-off between control, contact reasoning, and visual fidelity.

## Important caveat

These are hypotheses, not established facts. The first phase of the project is designed to falsify them if necessary.

## Phase 0 — Baseline reproduction

Before proposing a new method, reproduce at least two existing avatar families.

### Baseline A: HUGS

Why:
- official Apple implementation,
- monocular human + scene,
- SMPL initialization,
- real-time rendering,
- PSNR/SSIM/LPIPS evaluation scripts.

Paper:
https://openaccess.thecvf.com/content/CVPR2024/html/Kocabas_HUGS_Human_Gaussian_Splats_CVPR_2024_paper.html

Code:
https://github.com/apple/ml-hugs

### Baseline B: GaussianAvatar

Why:
- canonical animatable 3D Gaussian formulation,
- monocular human video,
- dynamic appearance conditioned by motion,
- accessible official implementation.

Paper:
https://openaccess.thecvf.com/content/CVPR2024/html/Hu_GaussianAvatar_Towards_Realistic_Human_Avatar_Modeling_from_a_Single_Video_CVPR_2024_paper.html

Code:
https://github.com/aipixel/GaussianAvatar

### Optional structured comparison: DAMA

Why:
- explicitly body-anchored Gaussians,
- garment semantics and layers,
- physical plausibility and controllability,
- code available.

Paper:
https://openaccess.thecvf.com/content/CVPR2026W/PhysHuman/html/Eskandar_DAMA_Disentangled_Body-Anchored_Gaussians_for_Controllable_Multi-Layered_Avatars_CVPRW_2026_paper.html

Code:
https://github.com/danieleskandar/DAMA-code

## Phase 1 — Build a semantic interaction layer

Start from a reproduced body-anchored avatar.

Each Gaussian or group of Gaussians receives, directly or through interpolation, structured metadata such as:

- body-part label,
- skeletal attachment,
- canonical-space coordinate,
- interaction-region membership,
- distance to surface/contact region,
- optional material/garment class.

Interaction anchors can initially be simple points or local frames attached to SMPL-X / MANO / face landmarks.

Candidate anchors:

- eyes / gaze origin,
- head orientation,
- palms,
- fingertips,
- chest,
- shoulders,
- garment regions,
- detected user-contact location.

## Phase 2 — Local response module

Given an interaction event, predict only local changes around relevant semantic regions.

Possible control input:

```text
interaction = {
  actor_signal,
  target_region,
  target_position,
  target_orientation,
  contact_state,
  temporal_context
}
```

Possible output:

```text
local_delta = {
  gaussian_position_delta,
  gaussian_rotation_delta,
  gaussian_scale_delta,
  opacity_delta,
  appearance_feature_delta
}
```

The first experiment should use deliberately simple interaction events before conversational AI:

1. gaze target following,
2. hand reaches a target point,
3. hand touches face or torso,
4. external object approaches a contact region.

## Phase 3 — Compare global vs local control

### Baseline control

Use the original pose/deformation pathway to produce the target action.

### Proposed control

Apply semantic-anchor-conditioned local deformation.

### Question

Does the proposed representation produce the requested local change with less degradation or drift elsewhere?

## Initial metrics

### Reconstruction / rendering
- PSNR
- SSIM
- LPIPS
- FPS
- VRAM

### Interaction controllability

**Target error**

Distance between requested and realized anchor/contact target.

**Locality / edit leakage**

Measure deformation or appearance change outside the intended semantic region.

One simple prototype metric:

```text
Leakage = change outside target region / total representation change
```

Lower is better.

**Identity preservation**

Compare image-embedding similarity before and after interaction while controlling for pose/view changes.

**Temporal stability**

Measure frame-to-frame changes in regions that should remain static.

**Latency**

Measure input event → updated rendered frame rather than rendering FPS alone.

## Minimal publishable contribution candidate

A plausible first contribution is not "a new complete digital human system."

It is narrower:

> A semantically anchored 4D human representation and evaluation protocol for low-latency localized interaction control, showing improved control locality and identity stability over conventional globally driven avatar deformation.

This contribution is only worth pursuing if the baseline experiments show a measurable problem with existing representations.

## Failure conditions

Abandon or reformulate this direction if:

1. existing avatar representations already provide equivalent semantic local control with no meaningful trade-off,
2. local control does not improve latency or stability,
3. semantic anchoring significantly harms novel-pose generalization,
4. evaluation cannot distinguish the proposed representation from a simple mask-based local deformation baseline.

## Next concrete action

Reproduce one established baseline before implementing any novel module.

Recommended order:

1. HUGS installation and pretrained demo,
2. HUGS evaluation pipeline,
3. own/small public sequence,
4. inspect Gaussian-to-SMPL attachment and deformation,
5. implement semantic body-part labels as a non-learning diagnostic layer,
6. visualize/select Gaussians by semantic region,
7. measure whether a controlled local perturbation remains local.

That last test is the first original experiment in this repository.
