# Latest Research Handoff

Current continuation date: **2026-09-16**.

## Active Colab

`https://colab.research.google.com/github/reusahn/interactive-digital-humans/blob/main/notebooks/daily/2026-09-16_research.ipynb`

Notebook-link registry:

`research/notebook-links.md`

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

Independent model-level unit remains checkpoint, `n=3`. Joint and pose tests are repeated/nested diagnostics rather than additional independent models.

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

Protocol:

`research/protocols/2026-09-16-third-joint-generalization.md`

No joint, branch, mask, threshold, pose schedule, axis, or perturbation angle may be tuned after inspecting shoulder-related results.

## Step 18A descriptive precursor COMPLETE

Step 18A measured only frozen contralateral shoulder-branch support mass. It did not compute shoulder causal displacement.

Parkinglot reverses the mean support ordering (`learned/K6 = 0.837904818`) while Seattle and Jogging have learned>K6. This reversal remains part of the record and is not grounds for changing the frozen shoulder protocol.

## Step 18B0 / B0A / B0B provenance block COMPLETE

Seattle canonical source was recovered and exactly validated across 37 persistent copies.

Authoritative Seattle canonical reference:

`experiments/01-baseline/probe_results/frame000_left_wrist_z_10deg.npz`

`xyz_canon` SHA256:

`61a633d5b2c1fb353d7790cdd176919f17c3f1000ce7e9cb5d03e2751b51d314`

## Step 18B1 historical elbow gate BLOCKED

The newly written CPU reconstruction did not reproduce the frozen Step-17B1 elbow learned contralateral sums within the frozen `1e-5` aggregate tolerance, so execution stopped before shoulder causal metrics were accepted.

This is a pipeline/source-equivalence blocker, not a shoulder result. No threshold was widened.

## Step 18B1A-R per-Gaussian audit COMPLETE

Current versus archived Step-17 elbow displacement fields are spatially nearly identical across all three checkpoints:

- learned Pearson values `>= 0.999999999839`
- learned mean per-Gaussian absolute differences about `7e-8` to `1.1e-7`
- K6 agreement even closer
- Step-17B1 and Step-17B2 frame-2 arrays exact for Parkinglot/Jogging and near-exact for Seattle

## Step 18B1B evaluation-order audit COMPLETE

Direct delta-A evaluation was not the whole cause. Full before/after float32 position evaluation reduced learned contralateral-sum error to:

| Checkpoint | best full-position learned error | frozen `1e-5` gate |
|---|---:|---|
| Seattle | `-2.927389e-5` | FAIL |
| Parkinglot | `+4.781559e-5` | FAIL |
| Jogging | `+1.115697e-5` | FAIL |

All K6 conditions pass the same gate.

## Step 18B1C dependency / namespace blockers

`smplx==0.1.28` was installed successfully. A subsequent audit attempt failed because unaliased SMPLX imports polluted notebook helper names. This was recorded separately as an implementation failure. No shoulder computation ran.

## Step 18B1C-R namespace-isolated source-exact audit COMPLETE

The manual Step-18 transform path is **bitwise identical** to the official `smplx==0.1.28` transform path for all three checkpoints, both before and after the elbow perturbation.

```text
Seattle manual A == smplx A: True
Parkinglot manual A == smplx A: True
Jogging manual A == smplx A: True
manual A bitwise exact vs smplx in all checkpoints: True
```

Chunked versus one-shot CPU LBS evaluation is also not the cause. Parkinglot/Jogging are bitwise exact between chunked and one-shot for learned and K6. Seattle learned differs only at negligible floating-point scale (`mean abs ~1.35e-14`, `max abs ~6.37e-9`).

The source-exact CPU path still yields only `3/6` aggregate gate passes, because every K6 condition passes and every dense learned condition remains slightly outside the frozen `1e-5` tolerance:

| Checkpoint | Learned contra error | K6 contra error |
|---|---:|---:|
| Seattle | `-2.92805305548427e-05` | `+4.982352947990876e-07` |
| Parkinglot | `+4.781559425737214e-05` | `+2.246013536932878e-06` |
| Jogging | `+1.115696863962512e-05` | `+4.4823536882176995e-08` |

Per-Gaussian learned Pearson remains essentially 1.0 in every checkpoint.

Archived:

`research/sessions/2026-09-16-step18b1c-r.md`

Drive artifact:

`experiments/08-second-joint-generalization/18B1C_R_namespace_isolated_smplx_audit.json`

### Current interpretation

The remaining historical Step-17 versus current Step-18 discrepancy is **not** explained by:

1. manual versus official SMPLX transform construction
2. delta-A versus full-position evaluation alone
3. chunked versus one-shot CPU skinning

The remaining candidate is runtime/backend floating-point provenance, especially CPU versus CUDA execution. The learned LBS field is dense, so it accumulates more floating-point operations than sparse K6 and can expose backend-level rounding differences while retaining nearly perfect spatial agreement.

## Exact next action

Run **Step 18B1D runtime/backend provenance audit**, elbow only.

1. report PyTorch version, CUDA build, CUDA availability, device name, CPU thread counts, MKL/OpenMP backend status, and TF32 flags
2. if CUDA is unavailable, stop after provenance reporting without shoulder computation
3. if CUDA is available, recompute the same source-exact elbow frame-2 learned/K6 displacement on CUDA and compare CPU versus CUDA against the frozen Step-17B1 arrays
4. do not widen the frozen `1e-5` tolerance
5. do not compute shoulder causal metrics yet

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, accidental inspection leakage, and backend provenance uncertainty rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
