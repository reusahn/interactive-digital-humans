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

Key scientific interpretation:

- The predeclared `>=95%` K6-reduction criterion fails in all three checkpoints.
- Parkinglot K6 produces **more** contralateral shoulder displacement than learned LBS.
- Selective removal of learned shoulder-branch weights produces exactly zero contralateral response in all three checkpoints.
- Thus shoulder response is mediated through the changed branch, but the distal wrist/elbow result that K6 almost eliminates contralateral response does not generalize to shoulder at frame 2.
- Jogging also narrowly fails the predeclared correlation threshold (`0.8946 < 0.90`).

This is a genuine shoulder scientific result, not the earlier runtime-regression blocker.

Archived:

- `research/sessions/2026-09-16-step18b1h.md`
- Drive `experiments/08-second-joint-generalization/18B1H_left_shoulder_frame2_cross_checkpoint.json`
- Drive `experiments/08-second-joint-generalization/18B1H_left_shoulder_frame2_displacements.npz`

## Interpretation boundary

Frame 2 already prevents a universal third-joint pass under the predeclared protocol. Later poses cannot rescue that confirmatory criterion. The remaining frozen pose schedule is still scientifically useful to characterize whether the shoulder failure is stable or pose-dependent.

A plausible but not yet established explanation is **kinematic-depth dependence**: learned-vs-SMPL locality amplification may be strong for distal wrist/elbow perturbations but weaker or qualitatively different for proximal shoulder perturbations, where standard SMPL K6 already carries substantial arm-branch influence.

## Exact next action

Run **Step 18B2 — Frozen left-shoulder full-pose failure characterization** under the same T4 legacy runtime and unchanged protocol.

Pinned script:

`research/scripts/step18b2_shoulder_full_pose_legacy.py`

Commit containing script: `b20fe372ea77628ebbb964d4fbdaaff43d459491`

It runs all predeclared schedules, including frame 2 as a deterministic regression anchor, and reports per-pose:

- changed transforms
- learned/K6/ablated contralateral sums
- K6 reduction
- selective-ablation reduction
- removed-mass/displacement-reduction correlation
- original pass/fail flags

Interpret all 18 pose diagnostics as nested within 3 pretrained checkpoints, not as 18 independent model replicates.

## Research-record rule

Preserve failures, reversals, and negative generalization results. Do not tune the shoulder protocol or widen thresholds after seeing Step 18B1H.
