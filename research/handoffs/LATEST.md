# Latest Research Handoff

Current continuation date: **2026-09-16**.

## Active Colab

`https://colab.research.google.com/github/reusahn/interactive-digital-humans/blob/main/notebooks/daily/2026-09-16_research.ipynb`

Notebook-link registry: `research/notebook-links.md`

## Frozen prior benchmark

Step 17C0 established the same learned cross-joint LBS causal mechanism for two tested joints, left wrist and predeclared left elbow, across three independently pretrained HUGS NeuMan checkpoints.

```text
independent pretrained checkpoints: 3
tested joints: 2
nested pose diagnostics: 36
joint x checkpoint cells passing: 6 / 6
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral response: 0.0
TWO-JOINT CROSS-CHECKPOINT BENCHMARK FROZEN: True
```

Independent model-level unit remains checkpoint, `n=3`.

## Step 18 predeclared third-joint protocol

Frozen before shoulder causal displacement inspection:

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

No joint, branch, mask, threshold, pose schedule, axis, or perturbation angle may be tuned after inspecting shoulder-related results.

## Step 18A descriptive precursor COMPLETE

Step 18A measured only frozen contralateral shoulder-branch support mass. Parkinglot reverses the mean support ordering (`learned/K6 = 0.837904818`). No shoulder causal displacement was computed.

## Step 18B0 / B0A / B0B provenance block COMPLETE

Seattle canonical source was recovered and exactly validated across 37 persistent copies.

Authoritative Seattle canonical reference:

`experiments/01-baseline/probe_results/frame000_left_wrist_z_10deg.npz`

`xyz_canon` SHA256: `61a633d5b2c1fb353d7790cdd176919f17c3f1000ce7e9cb5d03e2751b51d314`

## Step 18B1 historical elbow gate BLOCKED

The newly written reconstruction does not reproduce the frozen Step-17B1 elbow learned contralateral sums within the frozen `1e-5` aggregate tolerance across all checkpoints, so shoulder causal metrics remain blocked. No tolerance has been widened.

## Step 18B1A-R / B1B audits

Current versus archived Step-17 elbow fields are spatially nearly identical. Learned Pearson values are `>=0.999999999839`. Full before/after float32 evaluation reduces the learned aggregate mismatch but does not eliminate it. All K6 conditions pass the frozen gate.

## Step 18B1C-R source-exact transform audit COMPLETE

The manual Step-18 transform path is bitwise identical to official `smplx==0.1.28` transforms for all three checkpoints before and after elbow perturbation. Chunked versus one-shot CPU evaluation is also not the cause.

Archived: `research/sessions/2026-09-16-step18b1c-r.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1C_R_namespace_isolated_smplx_audit.json`

## Step 18B1D exact HUGS batched-rank audit COMPLETE

The exact HUGS `lbs_extra` tensor ranks were reproduced on CPU. Batched `[1,G,24] @ [1,24,16]` and flat `[G,24] @ [24,16]` paths were bitwise identical for tested positions/displacements.

| Checkpoint | Learned contra error | Learned gate | K6 contra error | K6 gate |
|---|---:|---|---:|---|
| Seattle | `-2.92805305548427e-05` | FAIL | `+4.982352947990876e-07` | PASS |
| Parkinglot | `+4.781559425737214e-05` | FAIL | `+2.246013536932878e-06` | PASS |
| Jogging | `+1.115696863962512e-05` | FAIL | `+4.4823536882176995e-08` | PASS |

Therefore tensor rank is not the source of the historical mismatch.

Archived: `research/sessions/2026-09-16-step18b1d.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1D_exact_hugs_batched_lbs_rank_audit.json`

## Step 18B1E backend provenance audit COMPLETE, later corrected by recovered prior output

The Experiment-08 persisted metadata itself contained no CPU/CUDA field, so Step 18B1E correctly classified the backend as unknown **from those persisted artifacts alone**.

A prior saved Step-17B1 execution output was subsequently recovered and explicitly states:

```text
deformation device: cuda
```

Therefore historical Step-17B1 execution is known to have used CUDA. The exact historical GPU, PyTorch, CUDA and cuBLAS versions remain unresolved.

## Step 18B1G1 direct CUDA elbow regression COMPLETE

Current CUDA runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
PyTorch: 2.11.0+cu128
CUDA: 12.8
smplx: 0.1.28
```

Strict FP32 CUDA produced `5/6` frozen gate passes. Seattle and Jogging learned passed, all K6 conditions passed, but Parkinglot learned remained outside tolerance at `+1.104918433156854e-04`. TF32 was much worse and is ruled out.

Archived: `research/sessions/2026-09-16-step18b1g1.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1G1_cuda_elbow_regression.json`

## Step 18B1G2 CUDA evaluation-placement audit COMPLETE

The same strict-FP32 CUDA before/after positions were evaluated with six norm/subtraction placements:

- CUDA `torch.linalg.vector_norm`
- CUDA `torch.norm`
- CUDA `sqrt(sum(delta^2))`
- CUDA subtraction then NumPy norm
- CUDA positions then NumPy subtraction + norm
- CUDA positions then CPU-Torch subtraction + norm

All six produce the same gate outcome:

```text
Seattle learned: PASS, error about +6.60e-06
Seattle K6: PASS, error about +1.51e-06
Parkinglot learned: FAIL, error about +1.1049e-04
Parkinglot K6: PASS, error about +2.40e-06
Jogging learned: PASS, error about -3.93e-06
Jogging K6: PASS, error about +3.70e-07

total gate passes: 5/6
EVALUATION-PLACEMENT RECOVERY: False
```

GPU-native norm variants are bitwise identical. CPU/NumPy placement changes fields only at roughly `1e-11` mean absolute scale. Therefore final displacement norm placement is not the source of the Parkinglot mismatch.

A useful consistency check emerged: summing each archived Step-17B1 displacement field with float32 reduction reproduces the historical printed contralateral scalar exactly. The archive and historical printed result are therefore internally consistent, and the remaining mismatch occurs upstream of the final reduction.

Archived: `research/sessions/2026-09-16-step18b1g2.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1G2_cuda_norm_placement_audit.json`

## Official HUGS environment target

The exact released HUGS setup script at commit `86ebe5522a384fc553f07f090b63a76dd4af8d33` specifies Python 3.8, PyTorch `1.13.1`, torchvision `0.14.1`, torchaudio `0.13.1`, and `pytorch-cuda=11.7`. The README states the system was tested on Ubuntu 22.04.3 with a CUDA 11.7-compatible GPU.

This does **not** prove the custom Step-17 diagnostic used that exact package stack, but it gives a concrete source-declared legacy environment to test before changing any frozen regression criterion.

## Step 18B1G3 legacy-environment bootstrap BLOCKED before science

The isolated legacy environment itself successfully initializes:

```text
Python: 3.8.20
Torch: 1.13.1+cu117
Torch CUDA build: 11.7
CUDA available: True
GPU: NVIDIA A100-SXM4-40GB
NumPy: 1.24.4
SciPy: 1.10.1
SMPLX import: OK
```

The regression subprocess then fails before any elbow computation while loading `SMPL_NEUTRAL_clean.pkl`:

```text
ModuleNotFoundError: No module named 'numpy._core'
```

This is a pickle serialization compatibility issue. The cleaned SMPL pickle was regenerated under NumPy 2.x and references `numpy._core`, while the legacy NumPy 1.24 runtime exposes the corresponding modules under `numpy.core`.

No elbow displacement, shoulder displacement, or scientific metric was produced by this failed G3 attempt. No tolerance changed.

Archived: `research/sessions/2026-09-16-step18b1g3-diagnostic-blocker.md`

## Exact next action

Patch only the isolated legacy subprocess loader with temporary NumPy module aliases so the NumPy-2-generated clean SMPL pickle can be loaded under NumPy 1.24.4. Validate the loaded SMPL structure before any regression computation. If the compatibility load succeeds, immediately rerun the same Step 18B1G3 elbow frame-2 regression under PyTorch `1.13.1+cu117`.

- keep TF32 disabled
- preserve the exact frozen `1e-5` gate
- do not compute shoulder metrics
- do not rewrite or replace the licensed original SMPL file

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, accidental inspection leakage, and backend provenance uncertainty rather than rewriting history after later success.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
