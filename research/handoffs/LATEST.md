# Latest Research Handoff

Current continuation date: **2026-09-17**.

## ACTIVE PRIORITY — complete A100 Step-18 canonical revalidation

Canonical continuation runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

Historical Step-18 scientific artifacts produced on Tesla T4 remain preserved and must not be overwritten. The A100 sequence is a provenance reconciliation, not an attempt to retune thresholds or rescue failed hypotheses.

User-supplied project provenance states that the intended runtime through Step 17 was A100. Archival Step-17 files themselves establish CUDA use but do not independently identify the historical GPU model. Preserve this distinction.

SMPL fingerprint used by the active rerun:

```text
SHA256: f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

## Step 18R0A / R0B — environment and input recovery COMPLETE

The exact pinned A100 legacy stack was rebuilt in `/content/hugs_legacy_torch113_py38`; Drive inputs and the SMPL pickle were verified. No scientific deformation computation occurred in R0A/R0B.

## Step 18R1 — A100 frame-2 shoulder rerun COMPLETE

Frozen Step 18B1H protocol and thresholds were unchanged.

```text
Seattle:    K6 reduction 38.89052698499022%  FAIL | ablation 100% PASS | corr 0.9616730744322076 PASS
Parkinglot: K6 reduction -49.15654343505103% FAIL | ablation 100% PASS | corr 0.9769195553081134 PASS
Jogging:    K6 reduction 59.774070438714524% FAIL | ablation 100% PASS | corr 0.8946040920942271 FAIL
```

All three checkpoints reproduced changed transforms `[16,18,20,22]`. Threshold-level status matched historical T4 exactly.

Archive:
`research/sessions/2026-09-17-step18r1-a100-frame2-rerun.md`

Drive:
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

Reproducibility:

```text
FRAME-2 THRESHOLD STATUS SAME AS R1: True
AGGREGATE THRESHOLD COUNTS SAME AS HISTORICAL T4: True
PER-POSE THRESHOLD STATUS SAME AS HISTORICAL T4: True
```

Thus the preregistered shoulder generalization remains **FAIL** on canonical A100; the T4 result was not a hardware-specific scientific artifact.

Archive:
`research/sessions/2026-09-17-step18r2-a100-full-pose-rerun.md`

Drive:
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_displacements.npz`

## Step 18R3 — A100 C1 support-mass reconciliation COMPLETE

Analysis class: `EXPLORATORY_POST_HOC`.

The historical Step 18C1 definition was unchanged: compare learned vs K6 total support on shoulder descendant branch `[16,18,20,22]`, then relate checkpoint/pose support direction to learned-vs-K6 displacement direction and per-Gaussian delta-support/delta-displacement correlation.

A100 support results are exactly unchanged because weights/masks are unchanged:

```text
Seattle
learned support sum: 14.713887457148648
K6 support sum:      9.33368880548187
learned/K6 ratio:    1.5764279015288012
support favors: learned
majority displacement favors: learned
support-direction matches: 3/4
corr min/median/max: 0.9362278422766451 / 0.9664406965256402 / 0.9672864525651061

Parkinglot
learned support sum: 25.7759453917906
K6 support sum:      30.762378737473114
learned/K6 ratio:    0.8379048191221863
support favors: K6
majority displacement favors: K6
support-direction matches: 4/4
corr min/median/max: 0.9497614357282316 / 0.9738199257592272 / 0.9816398111085524

Jogging
learned support sum: 14.840888978197778
K6 support sum:      2.671287769844639
learned/K6 ratio:    5.5557058081619255
support favors: learned
majority displacement favors: learned
support-direction matches: 10/10
corr min/median/max: 0.802178029451637 / 0.9193445080163702 / 0.9743405354392872
```

A100/T4 reconciliation:

```text
A100 checkpoint support-majority direction matches: 3/3
T4 recomputed checkpoint support-majority direction matches: 3/3
checkpoint-level C1 conclusion same: True
all checkpoint directions same A100 vs T4: True
all per-pose displacement/support-match directions same A100 vs T4: True
```

Therefore the exploratory C1 interpretation survives A100 reconciliation unchanged at the conclusion level. Seattle frame 7 remains the one per-pose direction mismatch. C1 remains exploratory and cannot alter the confirmatory shoulder FAIL.

Archive:
`research/sessions/2026-09-17-step18r3-a100-c1-reconciliation.md`

R3 session commit:
`d16333c48a33178aeb616e48b3068282d773d853`

Drive:
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.json`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.csv`

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints
- wrist, elbow, shoulder are repeated joint diagnostics within the same checkpoints

Do not call the pose diagnostics independent replications.

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

Historical Step-17 exact-number reconstruction recovered only 5/6 aggregates within the old `1e-5` scalar gate on tested replacement runtimes; field correlations remained essentially 1.0. The gate was not widened.

## Current confirmatory three-joint interpretation

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Bounded claims remain:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

## Historical exploratory C2/C3 values pending A100 reconciliation

Historical T4 C2 total branch-mass matching median full-field MAE-gap reduction:

```text
Seattle:    94.49547062277841%
Parkinglot: 83.84695205957038%
Jogging:    93.51712996485506%
```

Historical T4 C3 within-branch composition matching median full-field MAE-gap reduction:

```text
Seattle:    -0.10402258952364463%
Parkinglot: -2.1951923116722116%
Jogging:     0.20329469100371367%
```

These remain historical T4 values until R4/R5 finish.

## Step 18D0 structural topology analysis

D0 is based on frozen weight topology, not newly computed deformation fields, so it does not require GPU recomputation merely because the historical B1H/B2 deformation calculations were run on T4.

Historical exploratory mechanism label remains provisional until R4/R5 reconciliation is complete:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

## Exact next action

Run **Step 18R4**, the A100 canonical reconciliation of historical Step 18C2.

Counterfactual definition must remain unchanged:

> For each frozen contralateral Gaussian, set total shoulder-descendant branch mass to the corresponding K6 branch mass while preserving learned within-branch proportions where defined. Rescale learned non-branch weights proportionally to preserve row sum. Rows with undefined learned composition are explicitly counted and use K6 composition only as fallback.

Use A100 R2 learned/K6 displacement fields for the original gap, recompute only the counterfactual deformation on the same A100 legacy runtime, write new A100-specific R4 artifacts, and preserve historical C2 artifacts.

Primary reconciliation quantity:

- full-field MAE-gap reduction, especially checkpoint median across frozen poses

Historical T4 medians for direct comparison:

```text
Seattle:    94.49547062277841%
Parkinglot: 83.84695205957038%
Jogging:    93.51712996485506%
```

After R4, run R5 for historical C3 composition matching. Only after R4/R5 should C0/C4/D synthesis and `MASTER_CONTEXT.md` / `CLAIM_LEDGER.md` be finalized. Step 19 remains paused.

Current sequence:

`R0A/R0B complete -> R1 complete -> R2 complete -> R3 complete -> R4 C2 next -> R5 C3 -> reconcile C0/C4/D -> finalize continuity -> Step 19 preregistration`

## Research-record rule

Preserve both historical T4 artifacts and new A100 artifacts. Never overwrite failed results, never widen historical thresholds, never silently replace old numbers without runtime provenance, and never use exploratory analyses to rewrite the failed confirmatory shoulder outcome.