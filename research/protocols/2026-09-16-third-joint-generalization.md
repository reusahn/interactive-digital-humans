# Predeclared Protocol — Third-Joint Generalization

Date frozen: 2026-09-16

## Motivation

The current frozen benchmark establishes the same learned cross-joint LBS causal mechanism for two tested joints, left wrist and predeclared left elbow, across three independently pretrained HUGS NeuMan checkpoints and 36 nested pose diagnostics.

Before moving into any novel corrective method, test one additional joint on the same left-arm kinematic branch to determine whether the mechanism also generalizes proximally rather than only to the distal wrist/elbow pair.

This third-joint test is frozen before inspecting the causal displacement result.

## Predeclared joint

- joint: `left_shoulder`
- SMPL joint index: `16`
- axis: `z`
- perturbation: `+10 degrees`
- perturbed descendant branch: `[16,18,20,22]`
- expected changed transforms: `[16,18,20,22]`

## Checkpoints

Independent pretrained model-level unit remains checkpoint, `n = 3`:

- Seattle
- Parkinglot
- Jogging

## Pose schedule

Use the exact same raw-frame schedules as the frozen wrist and elbow robustness benchmarks:

- Seattle: `[2,7,12,17]`
- Parkinglot: `[2,7,12,17]`
- Jogging: `[2,7,12,17,22,27,32,37,42,47]`

Total nested shoulder pose diagnostics: `18`.

## Anatomy source

Reuse the canonical anatomy sources already frozen before the elbow causal test:

- Seattle: `saved_dominant + saved_confidence`
- Parkinglot: `dominant_joint + joint_confidence`
- Jogging: `dominant_joint + joint_confidence`

Confidence threshold remains `>= 0.9`.

No anatomy source, confidence threshold, mask definition, checkpoint, pose, perturbation angle, or axis may be changed after inspecting shoulder displacement results.

## Contralateral diagnostic subset

Use the same frozen contralateral upper-body anatomy used by wrist and elbow:

`{14,17,19,21,23}`

This corresponds to the right collar/shoulder/elbow/wrist/hand side of the upper body under the established SMPL joint indexing.

## Conditions

For every predeclared pose evaluate exactly three conditions:

1. `learned`
   - released HUGS learned deformation field

2. `K6`
   - subject-specific SMPL-derived K=6 deformation target already used in the frozen benchmark

3. `selective branch ablation`
   - on the frozen contralateral subset only, zero learned weights for branch channels `[16,18,20,22]`
   - renormalize the remaining row weights
   - no changes outside the frozen contralateral subset

## Predeclared causal thresholds

A pose-level shoulder diagnostic passes only if all conditions hold:

- changed transforms exactly equal `[16,18,20,22]`
- K6 contralateral reduction relative to learned `>= 95%`
- selective-ablation contralateral reduction relative to learned `>= 99.999%`
- maximum/summed ablated contralateral response under the established metric `<= 1e-8`
- Pearson correlation between removed branch mass and displacement reduction `>= 0.90`

Failures remain results. No threshold tuning is permitted after inspection.

## Statistical hierarchy

- independent pretrained models: `n = 3`
- shoulder is a repeated diagnostic within those same models
- 18 shoulder pose tests are nested robustness diagnostics, not 18 independent replications
- after this test, the three joints must not be described as 9 independent pretrained models

## Interpretation boundary

If the shoulder passes, the bounded result becomes cross-joint generalization across three positions along one articulated branch: proximal shoulder, intermediate elbow, and distal wrist, within three independently pretrained checkpoints.

If the shoulder fails, retain the failure and interpret the mechanism as potentially stronger or more reliable distally rather than changing the joint or thresholds.

## Disclosure guardrail

This protocol tests existing HUGS behavior only. Do not publicly disclose any future novel locality-preserving loss, architecture, or correction method before publication/IP decisions.
