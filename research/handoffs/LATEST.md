# Latest Research Handoff

Current continuation date: **2026-09-16**.

## Frozen benchmark before Step 18

Step 17C0 established the learned cross-joint LBS causal mechanism for two tested joints, left wrist and predeclared left elbow, across three independently pretrained HUGS NeuMan checkpoints.

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

- joint: `left_shoulder`, SMPL 16
- perturbation: `z +10 degrees`
- descendant branch: `[16,18,20,22]`
- expected changed transforms: `[16,18,20,22]`
- frozen contralateral subset: `{14,17,19,21,23}`
- Seattle poses: `[2,7,12,17]`
- Parkinglot poses: `[2,7,12,17]`
- Jogging poses: `[2,7,12,17,22,27,32,37,42,47]`
- K6 reduction threshold: `>=95%`
- selective-ablation reduction threshold: `>=99.999%`
- maximum/summed ablated contralateral response: `<=1e-8`
- removed-mass/displacement-reduction Pearson correlation: `>=0.90`

Protocol: `research/protocols/2026-09-16-third-joint-generalization.md`

No shoulder parameter or threshold may be tuned after inspecting shoulder-related output.

## Step 18A precursor

Descriptive support only. No shoulder displacement. Parkinglot reversed the learned/K6 mean branch-support ordering (`0.837904818`), so support mass alone is not the causal test.

## Step 18B historical elbow regression investigation

Seattle canonical xyz was exactly validated across 37 persistent copies. The historical Step-17 elbow archive is internally stable, but newly reconstructed elbow learned displacement fields differ at tiny distributed float32 scale.

Audits ruled out as primary causes:

- wrong canonical xyz source
- Step-17 archive instability
- manual versus official `smplx==0.1.28` transform semantics
- chunked versus one-shot evaluation
- HUGS batched tensor rank versus flat matmul
- displacement norm implementation / CPU-GPU norm placement
- TF32
- CPU versus CUDA alone
- official legacy HUGS software stack alone
- GPU architecture alone across tested A100/T4 runs

Historical Step-17B1 output explicitly records `deformation device: cuda`, but does not identify the historical GPU model.

## Current A100 CUDA result

A100 + PyTorch `2.11.0+cu128`, strict FP32:

```text
Seattle learned: PASS, +6.60e-06
Parkinglot learned: FAIL, +1.1049e-04
Jogging learned: PASS, -3.93e-06
all K6: PASS
5 / 6 total
```

TF32 was substantially worse.

## Official legacy stack on A100

Python `3.8.20`, NumPy `1.24.4`, PyTorch `1.13.1+cu117`, CUDA `11.7`, SMPLX `0.1.28`, TF32 disabled:

```text
Seattle learned: PASS, +7.2071e-06
Parkinglot learned: FAIL, -2.8672e-05
Jogging learned: PASS, +4.0584e-06
all K6: PASS
5 / 6 total
```

Archived: `research/sessions/2026-09-16-step18b1g3.md`

## Step 18B1G4 T4 hardware-sensitivity result COMPLETE

Same legacy software stack on Tesla T4:

| Checkpoint | Learned error | Learned gate | K6 error | K6 gate |
|---|---:|---|---:|---|
| Seattle | `-9.328914529760368e-08` | PASS | `+1.3674934962182306e-06` | PASS |
| Parkinglot | `+3.830264290627383e-05` | FAIL | `-1.8405622768113972e-06` | PASS |
| Jogging | `+1.361315298709087e-06` | PASS | `0.0` | PASS |

```text
learned passes: 2/3
K6 passes: 3/3
total passes: 5/6
kinematics: 3/3
T4 LEGACY ENV REGRESSION RECOVERY: False
```

The Parkinglot learned residual changes sign and magnitude between A100 legacy (`-2.87e-05`) and T4 legacy (`+3.83e-05`) while the learned fields retain Pearson correlation effectively `1.0`. This is strong evidence for low-level floating-point runtime sensitivity rather than a source-semantics or mechanism mismatch.

Archived: `research/sessions/2026-09-16-step18b1g4.md`

Important artifact note: the G4 runner reused the filename `experiments/08-second-joint-generalization/18B1G3_legacy_torch113_cuda117_regression.json`, so the current Drive copy now contains the T4 result. The A100 legacy numbers are preserved in the GitHub G3 session checkpoint.

## Historical gate status

The original elbow exact-reproduction gate remains unchanged at `1e-5`. It has **not** been widened and remains **FAILED for exact 6/6 recovery on available runtimes**.

Further GPU hunting is no longer the primary research path unless exact historical hardware provenance is recovered.

## Step 18 runtime continuation policy FROZEN

Before inspecting shoulder causal displacement, a separate runtime-specific continuation policy was frozen at:

`research/protocols/2026-09-16-step18-runtime-continuation-policy.md`

Primary Step-18 runtime:

```text
GPU: Tesla T4
Python: 3.8.20
PyTorch: 1.13.1+cu117
CUDA build: 11.7
NumPy: 1.24.4
SMPLX: 0.1.28
TF32: disabled
```

This is a reproducibility choice, not a claim that historical Step 17 used T4.

The already-frozen shoulder scientific thresholds, masks, joint, branch, pose schedules, axis and angle remain unchanged. After the complete primary shoulder experiment, threshold-level conclusions must later be checked on a second declared CUDA runtime without tuning.

## Exact next action

Proceed to the first causal left-shoulder test on raw frame 2 across Seattle, Parkinglot and Jogging using the frozen T4 legacy runtime and the predeclared shoulder protocol.

The first shoulder cell must compute learned, K6, and selective branch-ablation displacement for frame 2 only, verify changed transforms `[16,18,20,22]`, evaluate the already-frozen thresholds, save raw per-Gaussian arrays to Drive, and stop for review before running the full 18-pose schedule.

## Research-record rule

Preserve failed exact-reproduction results and runtime sensitivity. Do not silently widen the historical gate or claim historical bitwise reproduction.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
