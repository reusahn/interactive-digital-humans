# Research Session Checkpoint — 2026-09-17 Step 18R2 A100 Full-Pose Rerun

## Purpose

Re-run the complete frozen Step 18B2 left-shoulder pose schedule on the intended canonical A100 legacy runtime, preserving all historical T4 artifacts and keeping the preregistered protocol and thresholds unchanged.

Canonical runtime:

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

Frozen protocol remained unchanged:

- joint: left shoulder, SMPL 16
- perturbation: local z +10°
- descendant branch: `[16,18,20,22]`
- contralateral anatomy: frozen Step-17A2 masks
- Seattle frames: `[2,7,12,17]`
- Parkinglot frames: `[2,7,12,17]`
- Jogging frames: `[2,7,12,17,22,27,32,37,42,47]`
- K6 reduction threshold: `>=95%`
- selective-ablation reduction threshold: `>=99.999%`
- maximum and summed ablated contralateral displacement: `<=1e-8`
- removed-mass/displacement-reduction correlation threshold: `>=0.90`

## A100 results

### Seattle

```text
pose count: 4
kinematic pass: 4/4
K6 pass: 0/4
selective-ablation pass: 4/4
correlation pass: 4/4
overall pass: 0/4
negative K6 reductions: 1
K6 reduction min/median/max:
-32.348499344094606 / 29.517644394732528 / 38.89052698499022 %
correlation min/median/max:
0.9458239695319512 / 0.959302486189516 / 0.9616730744322076
```

### Parkinglot

```text
pose count: 4
kinematic pass: 4/4
K6 pass: 0/4
selective-ablation pass: 4/4
correlation pass: 4/4
overall pass: 0/4
negative K6 reductions: 4
K6 reduction min/median/max:
-77.67225758078598 / -52.505310570558706 / -44.70845892237716 %
correlation min/median/max:
0.9486499616066566 / 0.9732313968381923 / 0.9812400880684837
```

### Jogging

```text
pose count: 10
kinematic pass: 10/10
K6 pass: 0/10
selective-ablation pass: 10/10
correlation pass: 6/10
overall pass: 0/10
negative K6 reductions: 0
K6 reduction min/median/max:
42.275483094568976 / 71.45986687855165 / 76.3901059303657 %
correlation min/median/max:
0.7985822327394099 / 0.9085684692341088 / 0.9759406006207797
```

## Global A100 synthesis

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

The preregistered shoulder generalization remains **FAIL** on the intended A100 canonical runtime.

## Reproducibility comparison

Frame-2 R2 values match Step 18R1 exactly for all three checkpoints.

Historical T4 B2 comparison recovered all 18 historical pose rows. Every A100 pose preserved the same threshold-level classification as the corresponding T4 pose:

```text
FRAME-2 THRESHOLD STATUS SAME AS R1: True
AGGREGATE THRESHOLD COUNTS SAME AS HISTORICAL T4: True
PER-POSE THRESHOLD STATUS SAME AS HISTORICAL T4: True
```

All A100-vs-T4 K6-reduction differences were small relative to the scientific thresholds. The largest observed K6-reduction scalar difference in the printed comparison was about `0.00361` percentage points. Correlation differences were on the order of roughly `1e-6` or smaller. No threshold crossing occurred.

Therefore the Step-18 shoulder negative result is not a T4-specific artifact. The hardware/runtime change introduces small floating-point numerical differences but does not alter the confirmatory scientific conclusion under the frozen protocol.

## Scientific interpretation

The intended canonical A100 rerun preserves the historical Step-18B2 evidence structure:

- expected changed transforms `[16,18,20,22]` reproduce on all 18 nested poses;
- K6 never reaches the preregistered `>=95%` reduction threshold;
- selective descendant-branch ablation eliminates the contralateral response under all 18 poses;
- the removed-mass/displacement-reduction correlation threshold passes 14/18 poses;
- no pose passes the full shoulder generalization criterion.

Thus the bounded confirmatory interpretation remains:

1. branch-mediated shoulder response is supported under the frozen intervention;
2. strong learned-vs-K6 amplification observed at wrist/elbow does not generalize unchanged to shoulder;
3. the preregistered shoulder generalization remains a negative result and must not be rescued by post-hoc exploratory analysis.

## Drive artifacts

New A100 artifacts:

- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_displacements.npz`

Preserved historical T4 artifacts:

- `experiments/08-second-joint-generalization/18B2_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18B2_left_shoulder_full_pose_displacements.npz`

## Exact next action

Proceed to A100 recomputation/reconciliation of exploratory Step 18C1, then C2 and C3, using the new R2 displacement fields where applicable. Preserve the historical T4 C-series artifacts rather than overwriting them. Only after C1/C2/C3 are reconciled should C0/C4/D synthesis and continuity files be finalized. Step 19 remains paused.
