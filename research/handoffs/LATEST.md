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

A prior saved Step-17B1 execution output was subsequently recovered from the user's research record and explicitly states:

```text
deformation device: cuda
```

Therefore historical Step-17B1 execution is now known to have used CUDA. The exact historical GPU, PyTorch, CUDA and cuBLAS versions remain unresolved.

## Step 18B1G1 direct CUDA elbow regression COMPLETE

Current CUDA runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
PyTorch: 2.11.0+cu128
CUDA: 12.8
smplx: 0.1.28
```

### strict FP32 CUDA

| Checkpoint | Learned error | Learned gate | K6 error | K6 gate |
|---|---:|---|---:|---|
| Seattle | `+6.595764716621488e-06` | PASS | `+1.512095877842512e-06` | PASS |
| Parkinglot | `+1.104918433156854e-04` | FAIL | `+2.3953416530275717e-06` | PASS |
| Jogging | `-3.9301583569795184e-06` | PASS | `+3.7044446798972785e-07` | PASS |

```text
learned passes: 2/3
K6 passes: 3/3
total gate passes: 5/6
kinematics: 3/3
CUDA REGRESSION RECOVERY: FALSE
```

Strict CUDA FP32 substantially improves Seattle/Jogging aggregate agreement but does not recover Parkinglot learned within `1e-5`. Per-Gaussian fields remain nearly identical to the archive, with Pearson correlations effectively `1.0`.

### TF32 CUDA

TF32 is decisively worse and is ruled out as the historical numerical path. Learned errors rise to approximately `6.63e-4`, `9.57e-3`, and `-4.28e-4` for Seattle, Parkinglot, and Jogging respectively.

Archived: `research/sessions/2026-09-16-step18b1g1.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1G1_cuda_elbow_regression.json`

## Exact next action

Run one CUDA-only **norm/evaluation-placement audit** while preserving strict FP32 transforms and matmul. Reuse the exact same CUDA before/after positions and compare several mathematically equivalent displacement evaluation paths against the frozen Step-17B1 arrays, especially:

1. `torch.linalg.vector_norm` on CUDA before transfer
2. transfer `delta_xyz` to CPU and run NumPy `linalg.norm`
3. transfer full before/after positions separately to CPU, subtract there, then run NumPy norm
4. preserve the frozen `1e-5` gate without changing any scientific protocol
5. do not compute shoulder metrics yet

If one historical-style placement restores Parkinglot while retaining Seattle/Jogging, freeze that exact numerical path for Step 18. Otherwise the unresolved factor is historical CUDA/PyTorch/cuBLAS version provenance rather than operation placement.

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, accidental inspection leakage, and backend provenance uncertainty rather than rewriting history after later success.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
