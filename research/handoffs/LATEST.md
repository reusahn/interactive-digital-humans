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

## Step 18B1E backend provenance audit COMPLETE

Current runtime is CPU-only:

```text
Python 3.13.15
NumPy 2.1.3
PyTorch 2.11.0+cpu
torch.version.cuda: None
cuda_available: False
smplx: 0.1.28
torch_num_threads: 1
```

Persisted historical Step-17 artifacts provide no backend evidence:

```text
Step-17 text/metadata files inspected: 8
textual backend hints: 0
structured device/backend fields: 0
strong CUDA evidence: 0
strong CPU evidence: 0
HISTORICAL BACKEND CONCLUSION: UNKNOWN_FROM_PERSISTED_EVIDENCE
```

No CPU/CUDA claim is justified yet. No elbow recomputation, shoulder computation, or tolerance change occurred.

Archived: `research/sessions/2026-09-16-step18b1e.md`

Drive artifact: `experiments/08-second-joint-generalization/18B1E_backend_provenance_audit.json`

## Exact next action

Run **Step 18B1F historical execution-source recovery audit**, still without shoulder computation.

1. search persisted notebooks, Python/text files, and JSON under the project root for exact Step-17B1/B2 artifact names and code fragments
2. inspect current IPython history and `history.sqlite` for the exact Step-17 execution cell if still available
3. print matched source excerpts with file/session provenance
4. treat device-selection code as evidence only if it belongs to the exact historical Step-17 execution source
5. do not infer CUDA from generic HUGS support code
6. do not change the frozen `1e-5` regression tolerance
7. do not compute shoulder metrics yet

If exact historical execution code still cannot be recovered, backend provenance remains unknown and the next decision must distinguish reproducibility policy from scientific effect size rather than silently widening the historical gate.

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, accidental inspection leakage, and backend provenance uncertainty rather than rewriting history after later success.

Cumulative ledger: `research/methodology/assumption-failure-ledger.md`
