# Latest Research Handoff

Current continuation date: **2026-09-17**.

## CURRENT STATE — Step 18 A100 reconciliation COMPLETE

Step 18 is closed again after full canonical A100 provenance reconciliation.

No additional Step-18 deformation rerun is currently required unless a new provenance issue is discovered.

Historical Tesla T4 artifacts remain preserved. They are historical provenance/sensitivity records and must not be overwritten.

## Canonical runtime

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

SMPL fingerprint:

```text
SHA256: f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

User-supplied project provenance states that the intended runtime through Step 17 was A100. Historical Step-17 archives themselves establish CUDA use but do not independently identify the GPU model. Preserve this distinction.

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints
- wrist, elbow, shoulder are repeated joint diagnostics within the same checkpoints

Never count nested pose diagnostics as independent replications.

## Frozen distal benchmark

Left wrist Step 16E0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.708575087815%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9808287038512752
```

Left elbow Step 17C0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.81874059431833%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9688984153761956
```

Combined wrist + elbow: `6/6` joint x checkpoint cells pass across `36` nested pose diagnostics.

Historical Step-17 exact-number reconstruction recovered only 5/6 aggregates within the old `1e-5` scalar gate on tested replacement runtimes; displacement fields remained essentially perfectly correlated. The historical gate was not widened.

## Step 18R1 — A100 frame-2 shoulder rerun COMPLETE

All three checkpoints reproduced changed transforms `[16,18,20,22]` exactly.

```text
Seattle:    K6 reduction 38.89052698499022%  FAIL | ablation 100% PASS | corr 0.9616730744322076 PASS
Parkinglot: K6 reduction -49.15654343505103% FAIL | ablation 100% PASS | corr 0.9769195553081134 PASS
Jogging:    K6 reduction 59.774070438714524% FAIL | ablation 100% PASS | corr 0.8946040920942271 FAIL
```

Threshold-level status matched historical T4 B1H exactly.

## Step 18R2 — A100 full 18-pose shoulder rerun COMPLETE

Canonical A100 global result:

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
correlation passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction min/median/max:
-77.67225758078598 / 42.390431156682965 / 76.3901059303657 %
correlation min/median/max:
0.7985822327394099 / 0.9436557686954412 / 0.9812400880684837
```

Reproducibility:

```text
FRAME-2 THRESHOLD STATUS SAME AS R1: True
AGGREGATE THRESHOLD COUNTS SAME AS HISTORICAL T4: True
PER-POSE THRESHOLD STATUS SAME AS HISTORICAL T4: True
```

The preregistered shoulder generalization remains `FAIL_UNCHANGED`. The historical T4 failure is not a hardware-specific scientific artifact.

## Step 18R3 — A100 C1 support-mass reconciliation COMPLETE

Analysis class: `EXPLORATORY_POST_HOC`.

```text
Seattle:    learned/K6 support ratio 1.5764279015288012 | support learned | majority displacement learned | direction matches 3/4
Parkinglot: learned/K6 support ratio 0.8379048191221863 | support K6      | majority displacement K6      | direction matches 4/4
Jogging:    learned/K6 support ratio 5.5557058081619255 | support learned | majority displacement learned | direction matches 10/10
```

Checkpoint support-majority direction matches remain `3/3`; all A100/T4 direction classifications are unchanged.

## Step 18R4 — A100 C2 total branch-mass matching COMPLETE

Analysis class: `EXPLORATORY_POST_HOC`.

All checkpoints had zero fallback rows and pure learned-composition fraction `1.0`.

Canonical A100 median full-field MAE-gap reduction:

```text
Seattle:    94.49566207250349%
Parkinglot: 83.84751353605428%
Jogging:    93.51752945582919%
```

Historical T4 medians were `94.49547062277841%`, `83.84695205957038%`, and `93.51712996485506%`. Differences are sub-0.001 percentage point.

Interpretation preserved: per-row descendant-branch support existence/topology and total magnitude are strongly implicated as major explanatory factors for the shoulder learned-vs-K6 field difference.

## Step 18R5 — A100 C3 within-branch composition matching COMPLETE

Analysis class: `EXPLORATORY_POST_HOC`.

Composition-defined coverage reproduced historical topology exactly:

```text
Seattle:    7196 / 33072 = 0.21758587324625062
Parkinglot: 20300 / 77622 = 0.2615237948004432
Jogging:    1785 / 20887 = 0.08545985541245751
```

Canonical A100 median full-field MAE-gap reduction:

```text
Seattle:    -0.10397201493190789%
Parkinglot: -2.195179260385338%
Jogging:     0.20347135731436095%
```

Historical T4 medians were `-0.10402258952364463%`, `-2.1951923116722116%`, and `0.20329469100371367%`.

Canonical A100 C2 minus C3 median contrasts:

```text
Seattle:    94.5996340874354 percentage points
Parkinglot: 86.04269279643962 percentage points
Jogging:    93.31405809851483 percentage points
```

All historical composition-coverage counts reproduced exactly; all C3 median signs matched historical T4.

## Reconciled Step 18 synthesis

Three-joint confirmatory interpretation:

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Bounded claims:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- K6 arm-chain support-topology transition: `CONSISTENT_ACROSS_ALL_THREE_CHECKPOINTS`
- support topology + per-row total magnitude: `STRONGLY_IMPLICATED`
- within-branch composition: `SMALL_EFFECT_ON_DEFINED_OVERLAP`
- kinematic depth: `NOT_ESTABLISHED_AS_CAUSAL`

Final bounded deformation-mechanism label:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

This is not a training-level causal explanation.

## D0 structural topology remains valid

D0 uses frozen weights and masks, not newly computed deformation fields. No GPU-specific recomputation was needed.

K6 positive descendant-support fractions:

```text
Seattle:    wrist 0.004626269956458636 | elbow 0.006259071117561683 | shoulder 0.21758587324625062
Parkinglot: wrist 0.0022287495813042694 | elbow 0.0022287495813042694 | shoulder 0.2615237948004432
Jogging:    wrist 0.0019629434576530855 | elbow 0.0019629434576530855 | shoulder 0.08545985541245751
```

Learned support is positive on 100% of frozen contralateral rows in all tested joint/checkpoint cells.

## Canonical records

GitHub sessions:

- `research/sessions/2026-09-17-step18r1-a100-frame2-rerun.md`
- `research/sessions/2026-09-17-step18r2-a100-full-pose-rerun.md`
- `research/sessions/2026-09-17-step18r3-a100-c1-reconciliation.md`
- `research/sessions/2026-09-17-step18r4-a100-c2-reconciliation.md`
- `research/sessions/2026-09-17-step18r5-a100-c3-reconciliation.md`
- `research/sessions/2026-09-17-step18-a100-final-reconciliation.md`

Drive artifacts:

- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_displacements.npz`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_displacements.npz`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.json`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.csv`
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual_displacements.npz`
- `experiments/08-second-joint-generalization/18R5_A100_shoulder_composition_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R5_A100_shoulder_composition_match_counterfactual_displacements.npz`

Continuity files now use canonical A100 numeric anchors. Historical T4 files remain preserved.

## Exact next action — Step 19 preregistration

Step 19 is now **unpaused for protocol design only**. Corrective-method implementation must not begin until the evaluation protocol is frozen.

Step 19 research question:

> Can anatomical locality be enforced without sacrificing reconstruction quality?

Before implementation, freeze:

1. corrective-method hypothesis
2. exact learned quantity to regularize or constrain
3. anatomical-locality metric
4. reconstruction-quality metric
5. baseline and comparison conditions
6. success/failure thresholds
7. training/held-out/generalization protocol
8. ablation plan
9. datasets / subjects / body regions
10. cross-method generalization plan

Do not tune these criteria after observing method results.

A later cross-method question remains:

> Is anatomical nonlocality specific to HUGS, or does it emerge across learned human deformation representations?

## Research-record rule

Preserve both historical T4 artifacts and canonical A100 artifacts. Never overwrite failed results, never widen historical thresholds, never silently replace provenance, and never use exploratory analyses to rewrite confirmatory outcomes.