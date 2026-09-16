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

The newly written CPU reconstruction did not reproduce the frozen Step-17B1 elbow learned contralateral sums within the frozen `1e-5` aggregate tolerance, so execution stopped before shoulder causal metrics were accepted. No tolerance was widened.

## Step 18B1A-R / B1B audits

Current versus archived Step-17 elbow fields are spatially nearly identical. Learned Pearson values are `>=0.999999999839`. Full before/after float32 evaluation reduces the learned aggregate mismatch but does not eliminate it. All K6 conditions pass the frozen gate.

## Step 18B1C dependency / namespace blockers

`smplx==0.1.28` was installed successfully. One audit attempt then failed because unaliased SMPLX imports polluted notebook helper names. This was recorded separately. No shoulder computation ran.

## Step 18B1C-R namespace-isolated source-exact audit COMPLETE

The manual Step-18 transform path is bitwise identical to the official `smplx==0.1.28` transform path for all three checkpoints before and after elbow perturbation.

```text
Seattle manual A == smplx A: True
Parkinglot manual A == smplx A: True
Jogging manual A == smplx A: True
manual A bitwise exact vs smplx in all checkpoints: True
```

Chunked versus one-shot CPU evaluation is also not the cause under the current 2-D skinning implementation.

The source-exact transform + current CPU skinning path still yields `3/6` aggregate gate passes. Every K6 condition passes and every dense learned condition remains slightly outside `1e-5`:

| Checkpoint | Learned contra error | K6 contra error |
|---|---:|---:|
| Seattle | `-2.92805305548427e-05` | `+4.982352947990876e-07` |
| Parkinglot | `+4.781559425737214e-05` | `+2.246013536932878e-06` |
| Jogging | `+1.115696863962512e-05` | `+4.4823536882176995e-08` |

Archived: `research/sessions/2026-09-16-step18b1c-r.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1C_R_namespace_isolated_smplx_audit.json`

## Newly identified source-shape audit requirement

Inspection of the exact released HUGS `hugs/models/modules/lbs.py` shows that `lbs_extra` does not use the 2-D skinning matmul used by the current audit helper. HUGS constructs:

```text
W: [1, G, 24]
A.view: [1, 24, 16]
T = torch.matmul(W, A.view(...))
v_posed_homo: [1, G, 4]
v_homo = torch.matmul(T, v_posed_homo.unsqueeze(-1))
```

The current Step-18 audit instead used `W: [G,24] @ A: [24,16]`. Although mathematically equivalent, the tensor rank/kernel execution path can change float32 rounding. This source-level difference must be tested before attributing the residual to CPU-versus-CUDA backend provenance.

## Exact next action

Run **Step 18B1D exact-HUGS batched-LBS rank audit**, elbow frame 2 only, CPU only.

1. keep the already validated source-exact SMPLX `A` transforms
2. reproduce HUGS `lbs_extra` tensor ranks exactly with batch dimension 1
3. compute learned/K6 before and after positions with the exact batched `torch.matmul` sequence
4. compare displacement arrays and frozen contralateral sums to Step-17B1
5. compare the exact-HUGS batched path to the existing 2-D one-shot path
6. preserve the frozen `1e-5` regression tolerance
7. do not compute shoulder metrics yet

Only if this exact tensor-rank audit still fails should the next audit move to CPU-versus-CUDA runtime provenance.

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, accidental inspection leakage, and backend provenance uncertainty rather than rewriting history after later success.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
