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

The newly written CPU reconstruction did not reproduce the frozen Step-17B1 elbow learned contralateral sums within the frozen `1e-5` aggregate tolerance, so execution stopped before shoulder causal metrics were accepted. No tolerance was widened.

## Step 18B1A-R / B1B audits

Current versus archived Step-17 elbow fields are spatially nearly identical. Learned Pearson values are `>=0.999999999839`. Full before/after float32 evaluation reduces the learned aggregate mismatch but does not eliminate it. All K6 conditions pass the frozen gate.

## Step 18B1C-R namespace-isolated source-exact audit COMPLETE

The manual Step-18 transform path is bitwise identical to the official `smplx==0.1.28` transform path for all three checkpoints before and after elbow perturbation.

Chunked versus one-shot CPU evaluation is also not the cause. Source-exact CPU evaluation remains at `3/6` aggregate gate passes. Every K6 condition passes and every dense learned condition remains slightly outside `1e-5`.

Archived: `research/sessions/2026-09-16-step18b1c-r.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1C_R_namespace_isolated_smplx_audit.json`

## Step 18B1D exact HUGS batched-rank audit COMPLETE

The exact released-HUGS `lbs_extra` batch-rank structure was reproduced on CPU with `W=[1,G,24]`, `A=[1,24,16]`, and batched `torch.matmul`.

Result: the exact HUGS batched path is bitwise identical to the previous flat 2-D CPU path for every tested before position, after position, and displacement field.

| Checkpoint | Learned contra error | Learned gate | K6 contra error | K6 gate |
|---|---:|---|---:|---|
| Seattle | `-2.92805305548427e-05` | FAIL | `+4.982352947990876e-07` | PASS |
| Parkinglot | `+4.781559425737214e-05` | FAIL | `+2.246013536932878e-06` | PASS |
| Jogging | `+1.115696863962512e-05` | FAIL | `+4.4823536882176995e-08` | PASS |

```text
exact HUGS batched gate passes: 3/6
previous flat 2-D gate passes: 3/6
ALL THREE LEARNED CONDITIONS PASS WITH EXACT HUGS RANK: False
```

Therefore tensor rank / batched-versus-flat CPU matmul is not the source of the historical mismatch.

Archived: `research/sessions/2026-09-16-step18b1d.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1D_exact_hugs_batched_lbs_rank_audit.json`

## Exact next action

Run **Step 18B1E backend-provenance audit**, elbow only, before any shoulder computation.

1. record the current Python, Torch, CPU/CUDA environment
2. search persisted Experiment-08 and Step-17 metadata/text artifacts for backend evidence such as `cuda`, `device`, `torch`, GPU model, and version strings
3. inspect relevant JSON/MD/TXT metadata only, plus NPZ keys/dtypes where useful
4. conclude historical CPU or CUDA only if persisted evidence supports it
5. otherwise record backend provenance as unknown
6. preserve the frozen `1e-5` regression tolerance
7. do not compute shoulder metrics yet

If historical CUDA execution is positively established, reproduce the exact elbow path on CUDA in the next audit. If provenance is unknown, keep that uncertainty explicit rather than assuming CUDA.

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, accidental inspection leakage, and backend provenance uncertainty rather than rewriting history after later success.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
