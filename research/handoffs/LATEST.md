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

## Step 18B provenance/regression chain

Seattle canonical xyz was exactly validated across 37 persistent copies. The historical Step-17 elbow archive is internally stable, but newly reconstructed elbow learned displacement fields differ from it at tiny distributed float32 scale.

Audits ruled out the following as the primary cause:

- wrong canonical xyz source
- Step-17 archive instability
- manual versus official `smplx==0.1.28` transform implementation
- chunked versus one-shot evaluation
- HUGS batched `[1,G,24] @ [1,24,16]` tensor rank versus flat matmul
- displacement norm implementation or CPU/GPU norm placement
- TF32

Historical Step-17B1 output explicitly records `deformation device: cuda`.

## Step 18B1G1 current CUDA result

A100 + PyTorch `2.11.0+cu128`, strict FP32:

```text
Seattle learned: PASS, +6.60e-06
Parkinglot learned: FAIL, +1.1049e-04
Jogging learned: PASS, -3.93e-06
all K6: PASS
5 / 6 total
```

TF32 was substantially worse.

Archived: `research/sessions/2026-09-16-step18b1g1.md`

## Step 18B1G2 norm-placement result

Six CUDA/CPU subtraction and norm placements all produced the same `5/6` outcome. Therefore final norm/reduction placement is not the Parkinglot blocker.

Archived: `research/sessions/2026-09-16-step18b1g2.md`

## Step 18B1G3 official legacy HUGS software stack COMPLETE

Isolated legacy runtime:

```text
Python 3.8.20
NumPy 1.24.4
PyTorch 1.13.1+cu117
CUDA build 11.7
SMPLX 0.1.28
GPU NVIDIA A100-SXM4-40GB
TF32 disabled
```

A temporary NumPy module alias was required only because the clean SMPL pickle was serialized under NumPy 2.x. The SMPL file was not rewritten.

Result:

| Checkpoint | Learned error | Learned gate | K6 error | K6 gate |
|---|---:|---|---:|---|
| Seattle | `+7.207062083125493e-06` | PASS | `-2.6971592888003215e-06` | PASS |
| Parkinglot | `-2.8671978441252577e-05` | FAIL | `+1.9417839212110266e-06` | PASS |
| Jogging | `+4.058430192799278e-06` | PASS | `-8.393908501602709e-08` | PASS |

```text
learned passes: 2/3
K6 passes: 3/3
total: 5/6
kinematics: 3/3
LEGACY ENV REGRESSION RECOVERY: False
```

The official legacy software stack materially changes the tiny mismatch and moves Parkinglot learned from about `+1.10e-4` to `-2.87e-5`, but it still does not restore the frozen `1e-5` gate on the current A100. Field correlations remain effectively `1.0`.

Archived: `research/sessions/2026-09-16-step18b1g3.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1G3_legacy_torch113_cuda117_regression.json`

## Current interpretation

This is a numerical runtime-equivalence problem, not evidence that the frozen elbow mechanism disappeared. CPU/CUDA selection, source semantics, norm placement, TF32, and software-stack version alone do not explain the remaining Parkinglot aggregate difference.

The strongest remaining provenance variable is GPU architecture / low-level CUDA kernel selection. The historical Step-17 log confirms CUDA but does not identify the GPU model. Therefore a second GPU architecture is the next controlled test. This must not be described as proof that historical Step 17 used that GPU.

## Exact next action

Switch Colab from A100 to a **T4 GPU** if available, then run the pinned Step 18B1G4 hardware-sensitivity runner. It recreates Python 3.8 + PyTorch 1.13.1+cu117 in an isolated environment and reruns only the frozen Step-17B1 elbow frame-2 learned/K6 conditions.

Pinned runner added at:

`research/scripts/step18b1g4_t4_legacy_runner.py`

Rules:

- keep TF32 disabled
- preserve frozen `1e-5` gate
- no shoulder computation yet
- if T4 restores 6/6, freeze that numerical path before Step 18 shoulder computation
- if T4 does not restore 6/6, stop treating exact historical bit-level reproduction as a source-code bug and explicitly separate runtime numerical sensitivity from the stable scientific effect before deciding the shoulder reproducibility policy

## Research-record rule

Preserve failures and disproven assumptions. Do not silently widen the historical gate.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
