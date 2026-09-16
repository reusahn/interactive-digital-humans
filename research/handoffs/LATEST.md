# Latest Research Handoff

Current continuation date: **2026-09-16**.

## Frozen prior benchmark

Step 17C0 established the learned cross-joint LBS causal mechanism for two tested distal joints, left wrist and predeclared left elbow, across three independently pretrained HUGS NeuMan checkpoints.

```text
independent pretrained checkpoints: 3
tested joints: 2
nested pose diagnostics: 36
joint x checkpoint cells passing: 6 / 6
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral response: 0.0
```

Independent model-level unit remains checkpoint, `n=3`.

## Step 18 frozen third-joint protocol

Frozen before shoulder causal output:

- joint: `left_shoulder`, SMPL 16
- perturbation: local `z +10°`
- branch: `[16,18,20,22]`
- expected changed transforms: `[16,18,20,22]`
- frozen contralateral subset: `{14,17,19,21,23}`
- Seattle poses: `[2,7,12,17]`
- Parkinglot poses: `[2,7,12,17]`
- Jogging poses: `[2,7,12,17,22,27,32,37,42,47]`
- K6 reduction threshold: `>=95%`
- selective-ablation reduction threshold: `>=99.999%`
- max/summed ablated contralateral response: `<=1e-8`
- removed-mass/displacement-reduction correlation: `>=0.90`

Protocol: `research/protocols/2026-09-16-third-joint-generalization.md`

No shoulder parameter or threshold may be tuned after inspection.

## Historical numerical-reproduction audit

The old Step-17 elbow archive is scientifically stable but cannot be reproduced bit-for-bit under newly reconstructed runtimes within the frozen `1e-5` aggregate gate for Parkinglot learned displacement.

Ruled out as primary explanations:

- wrong canonical xyz
- archive instability
- manual vs official SMPLX transform implementation
- chunked vs one-shot
- HUGS batched-rank vs flat matmul
- displacement norm placement
- TF32

Historical Step-17 output confirms `deformation device: cuda` but not GPU model.

Current reproducibility observations:

- modern A100, PyTorch 2.11/CUDA 12.8: `5/6`
- A100, official legacy stack PyTorch 1.13.1/CUDA 11.7: `5/6`
- T4, official legacy stack PyTorch 1.13.1/CUDA 11.7: `5/6`

The Parkinglot learned error changes magnitude and sign across runtimes while field Pearson correlations remain effectively 1.0. This is classified as historical float32/runtime numerical sensitivity, not disappearance of the causal field.

The frozen `1e-5` historical gate was **not** widened.

## Frozen primary Step-18 runtime

For continuation, freeze:

```text
GPU: Tesla T4
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

This is a continuation runtime choice, not a claim that historical Step 17 used T4.

## Step 18B1H shoulder frame-2 causal test COMPLETE

All checkpoints reproduced the expected changed transforms `[16,18,20,22]`.

| Checkpoint | Learned contra | K6 contra | K6 reduction | Ablation reduction | Corr | Overall |
|---|---:|---:|---:|---:|---:|---|
| Seattle | `3.5090098206` | `2.1443378665` | `38.8905%` | `100%` | `0.961674` | FAIL |
| Parkinglot | `9.6190783830` | `14.3472676853` | `-49.1543%` | `100%` | `0.976920` | FAIL |
| Jogging | `1.1837988005` | `0.4761869365` | `59.7747%` | `100%` | `0.894603` | FAIL |

```text
ALL THREE FRAME-2 SHOULDER CELLS PASS: False
```

## Step 18B2 full-pose shoulder characterization COMPLETE

The frame-2 values reproduced Step 18B1H exactly in all three checkpoints, confirming deterministic continuation under the frozen runtime.

### Seattle

```text
poses: 4
kinematic passes: 4/4
K6 passes: 0/4
selective-ablation passes: 4/4
corr passes: 4/4
overall passes: 0/4
negative K6 reductions: 1
K6 reduction min/median/max: -32.350004161443465 / 29.517250805666034 / 38.89051396025266
corr min/median/max: 0.9458241700212214 / 0.9593022501720412 / 0.9616736739083002
```

### Parkinglot

```text
poses: 4
kinematic passes: 4/4
K6 passes: 0/4
selective-ablation passes: 4/4
corr passes: 4/4
overall passes: 0/4
negative K6 reductions: 4
K6 reduction min/median/max: -77.67114518499558 / -52.50598349082395 / -44.71030074854638
corr min/median/max: 0.9486500565287279 / 0.9732314511023251 / 0.9812400568052309
```

### Jogging

```text
poses: 10
kinematic passes: 10/10
K6 passes: 0/10
selective-ablation passes: 10/10
corr passes: 6/10
overall passes: 0/10
negative K6 reductions: 0
K6 reduction min/median/max: 42.273608581426544 / 71.45910159816793 / 76.38981785068806
corr min/median/max: 0.7985830691231263 / 0.9085679698778099 / 0.9759407417520358
```

### Global shoulder synthesis

```text
nested_pose_count: 18
kinematic_pass_count: 18
k6_pass_count: 0
selective_ablation_pass_count: 18
corr_pass_count: 14
overall_pass_count: 0
negative_k6_reduction_count: 5
global_k6_reduction_min: -77.67114518499558
global_k6_reduction_max: 76.38981785068806
global_corr_min: 0.7985830691231263
global_corr_max: 0.9812400568052309
predeclared_third_joint_universal_pass: False
```

The 18 pose diagnostics are nested within 3 pretrained checkpoints and are not independent model-level replications.

## Current scientific interpretation

The third-joint universal generalization hypothesis is rejected under its frozen shoulder protocol.

The result is not that contralateral shoulder response disappears. Rather:

1. The shoulder perturbation always changes the expected branch `[16,18,20,22]`.
2. Selective removal of learned shoulder-descendant branch mass from frozen contralateral rows eliminates the tested contralateral response in all 18 poses.
3. Therefore branch-mediated causality persists through the shoulder.
4. However, the wrist/elbow result that SMPL K6 nearly abolishes learned contralateral response does not generalize proximally. K6 reduction is below 95% in all 18 shoulder poses.
5. Parkinglot reverses the comparison in all four shoulder poses, with K6 producing more contralateral displacement than learned LBS.
6. Seattle is mixed, while Jogging retains learned > K6 but only at 42.3% to 76.4% reduction.
7. Removed-mass/displacement-reduction correlation is strong in Seattle and Parkinglot but less pose-stable in Jogging, with 4/10 poses below the frozen 0.90 threshold.

The strongest bounded claim is therefore **joint-dependent cross-body LBS behavior**: branch-mediated causality is robust across wrist, elbow, and shoulder, but learned-vs-K6 amplification is robust only for the tested distal wrist/elbow perturbations and fails for the proximal shoulder.

A kinematic-depth explanation is plausible but remains a hypothesis, not an established mechanism.

Archived:

- `research/sessions/2026-09-16-step18b2.md`
- Drive `experiments/08-second-joint-generalization/18B2_left_shoulder_full_pose_metadata.json`
- Drive `experiments/08-second-joint-generalization/18B2_left_shoulder_full_pose_displacements.npz`

## Exact next action

Freeze a three-joint synthesis before any new perturbation or corrective-method design.

The next step should compare wrist, elbow, and shoulder at the correct checkpoint-level nesting and explicitly separate:

- branch-mediated causality
- learned-vs-K6 amplification
- pose stability of removed-mass correlation

Do not add another joint simply to seek a passing result and do not alter the frozen shoulder thresholds.

## Research-record rule

Preserve failures, reversals, and negative generalization results. Do not tune the shoulder protocol after seeing Step 18B1H/B2.
