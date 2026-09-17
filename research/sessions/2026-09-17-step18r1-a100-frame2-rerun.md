# Research Session Checkpoint — 2026-09-17 Step 18R1 A100 Frame-2 Rerun

## Purpose

Re-run the frozen Step 18B1H left-shoulder frame-2 causal test on the canonical A100 legacy runtime after the user clarified that the earlier research runtime through Step 17 was A100-based and requested the T4 scientific portion of Step 18 to be revalidated on A100.

This rerun does **not** alter the frozen shoulder scientific protocol or any threshold. Historical T4 artifacts remain preserved.

## Canonical runtime

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA build: 11.7
SMPLX: 0.1.28
TF32: off
compute capability: (8,0)
```

SMPL input fingerprint:

```text
private_assets/smpl/SMPL_NEUTRAL_clean.pkl
SHA256: f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

## Frozen protocol

- joint: left shoulder, SMPL 16
- frame: 2
- perturbation: local z +10°
- descendant branch: `[16,18,20,22]`
- expected changed transforms: `[16,18,20,22]`
- contralateral anatomy: frozen Step-17A2 masks
- K6 reduction threshold: `>=95%`
- selective-ablation reduction threshold: `>=99.999%`
- max/summed ablated contralateral displacement: `<=1e-8`
- removed-mass/displacement-reduction correlation threshold: `>=0.90`

## A100 results

All three checkpoints reproduced the expected changed transform set exactly:

```text
[16,18,20,22]
```

### Seattle

```text
learned contra sum: 3.5089943585666106
K6 contra sum: 2.1443279606464785
ablated contra sum: 0.0
ablated contra max: 0.0
K6 reduction: 38.89052698499022%      FAIL
selective-ablation reduction: 100.0%   PASS
removed-mass/reduction corr: 0.9616730744322076  PASS
overall frame-2 pass: False
```

A100 minus historical T4:

```text
learned contra sum delta: -1.546205368185838e-05
K6 contra sum delta: -9.90581884252606e-06
K6 reduction delta: +1.3024737555156207e-05 percentage points
corr delta: -5.994760925442932e-07
```

### Parkinglot

```text
learned contra sum: 9.618950167762762
K6 contra sum: 14.347293584974977
ablated contra sum: 0.0
ablated contra max: 0.0
K6 reduction: -49.15654343505103%     FAIL
selective-ablation reduction: 100.0%   PASS
removed-mass/reduction corr: 0.9769195553081134  PASS
overall frame-2 pass: False
```

A100 minus historical T4:

```text
learned contra sum delta: -0.0001282152745716303
K6 contra sum delta: +2.5899645663685078e-05
K6 reduction delta: -0.002257400436135981 percentage points
corr delta: -1.2528429804703478e-07
```

### Jogging

```text
learned contra sum: 1.183803335025459
K6 contra sum: 0.47619589569148957
ablated contra sum: 0.0
ablated contra max: 0.0
K6 reduction: 59.774070438714524%      FAIL
selective-ablation reduction: 100.0%   PASS
removed-mass/reduction corr: 0.8946040920942271  FAIL
overall frame-2 pass: False
```

A100 minus historical T4:

```text
learned contra sum delta: +4.534536230949016e-06
K6 contra sum delta: +8.959172191680409e-06
K6 reduction delta: -0.0006027301969240284 percentage points
corr delta: +1.3993545893153936e-06
```

## Cross-checkpoint result

```text
all kinematic pass: True
all K6 pass: False
all selective-ablation pass: True
all correlation pass: False
all three frame-2 shoulder cells pass: False
threshold-level status same as historical T4: True
```

## Interpretation

The shoulder frame-2 scientific conclusion is unchanged on A100. The numerical differences between A100 and T4 are small FP32/runtime-hardware sensitivity effects and do not change any threshold-level classification.

Therefore:

1. the Step-18 shoulder failure is **not an artifact of using T4**;
2. the K6 `>=95%` generalization criterion still fails in all 3 checkpoints;
3. selective removal of the shoulder descendant branch still eliminates contralateral displacement exactly in all 3 checkpoints;
4. Seattle and Parkinglot still pass the correlation threshold, while Jogging remains just below `0.90`;
5. no scientific threshold should be changed.

This validates continuing the Step-18 re-run program on the A100 legacy runtime.

## Drive artifacts

New A100 artifacts:

- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_displacements.npz`

Historical T4 artifacts remain preserved:

- `experiments/08-second-joint-generalization/18B1H_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18B1H_left_shoulder_frame2_displacements.npz`

## Exact next action

Run the complete frozen shoulder pose schedule on the same A100 legacy runtime:

- Seattle: `[2,7,12,17]`
- Parkinglot: `[2,7,12,17]`
- Jogging: `[2,7,12,17,22,27,32,37,42,47]`

Save under new A100-specific Step-18R2 artifact names and compare threshold-level results against historical T4 Step 18B2. Do not overwrite the historical T4 outputs.
