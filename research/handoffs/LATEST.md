# Latest Research Handoff

Current continuation date: **2026-09-17**.

## ACTIVE PRIORITY — complete A100 Step-18 canonical revalidation

The intended canonical continuation runtime is:

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

Historical Step-18 scientific artifacts produced on Tesla T4 remain preserved and must not be overwritten. The A100 rerun is a provenance reconciliation, not an attempt to retune thresholds or rescue failed hypotheses.

User-supplied provenance states that the intended runtime through Step 17 was A100. Archival Step-17 outputs themselves establish CUDA use but do not independently identify the historical GPU model. Preserve this distinction.

## Step 18R0A / R0B — environment and input recovery COMPLETE

A fresh A100 Colab environment was rebuilt and verified at the exact pinned legacy stack above. Google Drive was mounted, frozen Step-18 inputs were found, and the SMPL pickle loaded under NumPy 1.24 compatibility aliases.

SMPL fingerprint:

```text
SHA256: f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

No scientific deformation computation occurred during R0A/R0B.

## Step 18R1 — A100 frame-2 shoulder rerun COMPLETE

Frozen Step 18B1H protocol and thresholds were unchanged.

```text
Seattle
K6 reduction: 38.89052698499022%      FAIL
selective ablation: 100.0%            PASS
correlation: 0.9616730744322076       PASS
overall: False

Parkinglot
K6 reduction: -49.15654343505103%     FAIL
selective ablation: 100.0%             PASS
correlation: 0.9769195553081134        PASS
overall: False

Jogging
K6 reduction: 59.774070438714524%     FAIL
selective ablation: 100.0%             PASS
correlation: 0.8946040920942271        FAIL
overall: False
```

All three checkpoints reproduced changed transforms `[16,18,20,22]` exactly. Threshold-level status was identical to historical T4 B1H for every checkpoint.

Archived session:

`research/sessions/2026-09-17-step18r1-a100-frame2-rerun.md`

Drive artifacts:

- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_displacements.npz`

## Step 18R2 — A100 full 18-pose shoulder rerun COMPLETE

Frozen pose schedule:

```text
Seattle:    [2,7,12,17]
Parkinglot: [2,7,12,17]
Jogging:    [2,7,12,17,22,27,32,37,42,47]
```

Global A100 result:

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
correlation passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction range: -77.67225758078598% to 76.3901059303657%
K6 reduction median: 42.390431156682965%
correlation range: 0.7985822327394099 to 0.9812400880684837
correlation median: 0.9436557686954412
```

Checkpoint summaries:

```text
Seattle
poses 4 | kinematic 4 | K6 0 | ablation 4 | corr 4 | overall 0
negative K6 reductions: 1
K6 min/median/max: -32.3484993441 / 29.5176443947 / 38.8905269850 %

Parkinglot
poses 4 | kinematic 4 | K6 0 | ablation 4 | corr 4 | overall 0
negative K6 reductions: 4
K6 min/median/max: -77.6722575808 / -52.5053105706 / -44.7084589224 %

Jogging
poses 10 | kinematic 10 | K6 0 | ablation 10 | corr 6 | overall 0
negative K6 reductions: 0
K6 min/median/max: 42.2754830946 / 71.4598668786 / 76.3901059304 %
```

Reproducibility comparison:

```text
FRAME-2 THRESHOLD STATUS SAME AS R1: True
AGGREGATE THRESHOLD COUNTS SAME AS HISTORICAL T4: True
PER-POSE THRESHOLD STATUS SAME AS HISTORICAL T4: True
```

All 18 historical T4 pose rows were recovered and every corresponding A100 pose retained the same kinematic/K6/ablation/correlation/overall threshold classification. Small FP32 scalar differences therefore do not alter the confirmatory shoulder conclusion.

The preregistered shoulder generalization remains **FAIL** on the intended A100 canonical runtime. The T4 shoulder failure is not a hardware-specific scientific artifact.

Archived session:

`research/sessions/2026-09-17-step18r2-a100-full-pose-rerun.md`

Session commit:

`cee40dd6b8cfaf15f0e1a35c88b92226ba8a2607`

Drive artifacts:

- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_displacements.npz`

Historical preserved T4 artifacts:

- `experiments/08-second-joint-generalization/18B2_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18B2_left_shoulder_full_pose_displacements.npz`

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints
- wrist, elbow, shoulder are repeated joint diagnostics within the same checkpoints

Do not call the 18 shoulder poses independent replications.

## Frozen distal benchmark

Left wrist Step 16E0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.708575087815%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9808287038512752
```

Predeclared left elbow Step 17C0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.81874059431833%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9688984153761956
```

Combined wrist + elbow: `6/6` joint x checkpoint cells pass across `36` nested pose diagnostics.

Historical exact-number reconstruction of Step-17 elbow recovered 5/6 aggregates within the old `1e-5` scalar gate on tested replacement runtimes, although displacement fields remained essentially perfectly correlated. The historical gate was not widened.

## Current confirmatory three-joint interpretation

The A100 R2 rerun does not change the threshold-level three-joint conclusion:

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Current bounded confirmatory claims remain:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

The canonical A100 shoulder numeric anchors are now the Step 18R2 values above. Historical T4 numeric anchors remain preserved in the original B1H/B2 artifacts and sessions.

## Historical exploratory Step 18C1-C4 status

Historical C1 used:

- frozen learned and K6 weights
- frozen contralateral masks
- historical T4 B2 displacement fields
- shoulder branch `[16,18,20,22]`

Historical C1 checkpoint support ratios:

```text
Seattle:    1.5764279015288012  support favors learned
Parkinglot: 0.8379048191221863  support favors K6
Jogging:    5.5557058081619255  support favors learned
```

Historical checkpoint support-majority displacement direction match: `3/3`.

Historical C2 mass-match counterfactual median full-field MAE-gap reduction:

```text
Seattle:    94.49547062277841%
Parkinglot: 83.84695205957038%
Jogging:    93.51712996485506%
```

Historical C3 composition-match median full-field MAE-gap reduction:

```text
Seattle:    -0.10402258952364463%
Parkinglot: -2.1951923116722116%
Jogging:     0.20329469100371367%
```

Historical exploratory mechanism label:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

These deformation-dependent exploratory values have not yet been reconciled on the new A100 R2 displacement fields. They remain historical T4 values until R3/R4/R5 are complete.

## Step 18D0 structural topology analysis

D0 is based on frozen weight topology rather than newly computed deformation fields and therefore does not require a GPU rerun merely because T4 was used for B1H/B2.

Nested descendant branches:

```text
wrist    [20,22]
elbow    [18,20,22]
shoulder [16,18,20,22]
```

Learned support is positive on 100% of frozen contralateral rows for every tested joint/checkpoint.

K6 positive-support fractions:

```text
Seattle:    wrist 0.0046263 | elbow 0.0062591 | shoulder 0.2175859
Parkinglot: wrist 0.0022287 | elbow 0.0022287 | shoulder 0.2615238
Jogging:    wrist 0.0019629 | elbow 0.0019629 | shoulder 0.0854599
```

D0 can remain as structural input while deformation-dependent C/D synthesis is reconciled.

## Exact next action

Run **Step 18R3**, the A100 reconciliation of historical exploratory Step 18C1 using the frozen learned/K6 weights, frozen masks, and the new `18R2_A100_left_shoulder_full_pose_displacements.npz` fields.

R3 must:

1. preserve the historical C1 artifacts;
2. write new A100-specific C1 output filenames;
3. keep the shoulder branch `[16,18,20,22]` unchanged;
4. compute the same support sums/ratios, per-pose learned/K6 displacement direction, and per-Gaussian delta-support/delta-displacement correlations;
5. compare A100 C1 threshold-free/descriptive conclusions against historical C1;
6. not reinterpret C1 as confirmatory evidence.

After R3, proceed separately to A100 C2 and C3. Only after C1/C2/C3 are reconciled should C0/C4/D synthesis and `MASTER_CONTEXT.md` / `CLAIM_LEDGER.md` be finalized. Step 19 remains paused.

Current sequence:

`R0A/R0B complete -> R1 complete -> R2 complete -> R3 C1 next -> R4 C2 -> R5 C3 -> reconcile C0/C4/D -> finalize continuity -> Step 19 preregistration`

## Research-record rule

Preserve both historical T4 artifacts and new A100 artifacts. Never overwrite failed results, never widen historical thresholds, and never silently replace old numbers without recording runtime provenance. Failed confirmatory outcomes remain failed regardless of exploratory follow-up.