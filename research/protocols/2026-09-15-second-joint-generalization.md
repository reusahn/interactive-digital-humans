# Predeclared Second-Joint Generalization Protocol

Date: 2026-09-15

This protocol is frozen **before inspecting second-joint learned-vs-K6 support or displacement results**. The previously completed left-wrist endpoint remains unchanged.

## Scientific question

Does the learned cross-joint LBS mechanism identified for the left wrist generalize to a second articulated joint under the same HUGS checkpoints, perturbation magnitude, anatomical-confidence rule, causal controls, and pose schedules?

## Predeclared second joint

- Joint: **left_elbow** (`SMPL joint 18`)
- Axis: **z**
- Perturbation: **+10 degrees**

Rationale: left elbow changes joint identity while retaining the same limb, side, axis, and angular magnitude as the frozen left-wrist benchmark. It is more proximal than the wrist and has a clear descendant chain, providing a direct joint-generalization test without simultaneously changing several design factors.

## Independent checkpoints

Exactly the same three independently pretrained HUGS NeuMan checkpoints used in the frozen wrist benchmark:

1. Seattle
2. Parkinglot
3. Jogging

Independent model-level unit: **checkpoint, n = 3**.

## Fixed within-checkpoint pose schedules

- Seattle: `[2,7,12,17]`
- Parkinglot: `[2,7,12,17]`
- Jogging: `[2,7,12,17,22,27,32,37,42,47]`

These pose tests are nested robustness tests and must not be counted as independent model replications.

## Fixed anatomical rule

For each checkpoint, use its already reconstructed subject-specific K=6 target.

- High confidence: K6 dominant-joint confidence `>= 0.9`
- Contralateral upper-body subset: K6 dominant joint in `{right_collar 14, right_shoulder 17, right_elbow 19, right_wrist 21, right_hand 23}`
- Masks are defined before any second-joint displacement is computed.

## Perturbed branch channels

A left-elbow local rotation changes the transforms of the left-elbow branch:

- `left_elbow = 18`
- `left_wrist = 20`
- `left_hand = 22`

Predeclared perturbed-branch channel set: **`{18,20,22}`**.

Every pose must pass a kinematic audit showing that the changed SMPL transforms are exactly `[18,20,22]`. Any different transform set is a diagnostic failure requiring review, not post-hoc redefinition.

## Three causal conditions

For the fixed K6-derived high-confidence contralateral subset:

1. **Learned**: original learned HUGS LBS.
2. **K6 target**: subject-specific reconstructed SMPL-derived K=6 LBS target.
3. **Selective branch ablation**: starting from learned LBS, set only channels `{18,20,22}` to zero on the fixed contralateral subset, then renormalize each modified row. No weights outside that subset may change.

## Pre-perturbation precursor audit

Before running pose perturbations, compare learned and K6 aggregate branch support

`w(left_elbow) + w(left_wrist) + w(left_hand)`

on the fixed contralateral subset for each checkpoint. This is descriptive precursor evidence only and is not itself a causal replication.

## Primary causal metrics

For each checkpoint and each predeclared pose:

- learned contralateral displacement sum
- K6 contralateral displacement sum
- selective-ablation contralateral displacement sum
- K6 reduction vs learned
- selective-ablation reduction vs learned
- correlation between removed learned branch mass and per-Gaussian displacement reduction

Cross-checkpoint raw displacement sums must not be pooled because sequence scales differ.

## Frozen diagnostic pass thresholds

Use the same operational thresholds already applied to the wrist benchmark. These are diagnostic decision rules, not universal scientific definitions:

- K6 reduction vs learned `>= 95%`
- selective-ablation reduction vs learned `>= 99.999%`
- removed-mass vs displacement-reduction correlation `>= 0.90`
- maximum selective-ablation contralateral displacement sum `<= 1e-8`
- exact kinematic changed-transform set `[18,20,22]`

A checkpoint-level second-joint causal replication requires all of these conditions across its predeclared pose schedule. Cross-checkpoint generalization requires all three checkpoints to satisfy the frozen checkpoint rule. Failures remain results and will not trigger threshold, mask, axis, angle, or joint changes.

## Interpretation guardrails

Passing this protocol would support generalization from the frozen left-wrist diagnostic to **one additional joint, left elbow**, within the tested HUGS NeuMan checkpoints. It would still not justify claims about all joints, all HUGS checkpoints, or other Gaussian-human methods.
