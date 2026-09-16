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

Step 18A inspected only frozen contralateral branch-support mass. It did **not** compute shoulder perturbed displacement and therefore is not the causal result.

| Checkpoint | Learned branch mean | K6 branch mean | Learned/K6 ratio | Fraction rows learned>K6 | Mean ordering |
|---|---:|---:|---:|---:|---|
| Seattle | 0.000444904676 | 0.000282223295 | 1.576427900 | 0.801463474 | learned>K6 |
| Parkinglot | 0.000332070101 | 0.000396310050 | 0.837904818 | 0.763121280 | **learned<K6** |
| Jogging | 0.000710532339 | 0.000127892362 | 5.555705804 | 0.920668358 | learned>K6 |

Parkinglot reverses the mean support ordering. This remains part of the record and is not grounds for changing the frozen shoulder protocol.

## Step 18B0 artifact/key inventory COMPLETE

Step 18B0 established the exact learned-LBS, K6, mask, pose, and prior causal artifact locations for Seattle, Parkinglot, and Jogging.

Important asymmetry:

- Parkinglot and Jogging learned-LBS artifacts contain `xyz_canon`
- Seattle `13E_learned_lbs_weights.npz` does not

Corrected historical Drive directories:

- `experiments/05-counterfactual-lbs-ablation`
- `experiments/06-frame-replication`

Archived record:

`research/sessions/2026-09-16-step18b0.md`

## Step 18B0A Seattle canonical-XYZ provenance recovery COMPLETE

The corrected provenance search found the original Seattle baseline probe artifact family under `experiments/01-baseline/probe_results/` and the historical duplicate under `experiment-01/20260914_003959/`.

B0A also unintentionally printed aggregate summaries for `xyz_after`, including an already-existing shoulder probe. It did not compute the frozen Step-18 causal endpoints. This inspection leakage is preserved in the record and the protocol remains unchanged.

Archived record:

`research/sessions/2026-09-16-step18b0a.md`

## Step 18B0B exact Seattle canonical-XYZ identity validation COMPLETE

Authoritative Seattle reference fixed to:

`experiments/01-baseline/probe_results/frame000_left_wrist_z_10deg.npz`

Thirty-seven persistent copies were validated: all 36 current baseline probes plus the historical duplicate.

```text
xyz_canon shape: (472958,3)
xyz_canon dtype: float32
xyz_canon SHA256: 61a633d5b2c1fb353d7790cdd176919f17c3f1000ce7e9cb5d03e2751b51d314
xyz_before SHA256: 291a1fcb5818b35ed0ecf6acdb461d2532fd4ce0323be3b10e3d12f67c075c73
all shape OK: True
all dtype OK: True
all finite: True
all xyz_canon elementwise exact: True
all xyz_canon SHA256 match: True
all xyz_before elementwise exact: True
all xyz_before SHA256 match: True
SEATTLE CANONICAL XYZ EXACTLY VALIDATED: True
```

Every candidate had maximum absolute difference `0.0` from the reference for both `xyz_canon` and `xyz_before`.

Archived record:

`research/sessions/2026-09-16-step18b0b.md`

Drive artifact:

`experiments/08-second-joint-generalization/18B0B_seattle_xyz_exact_validation.json`

## Exact next action

Run **Step 18B1** on CPU using the frozen third-joint protocol.

Guardrail before shoulder interpretation:

1. reconstruct the source-exact SMPL/HUGS pure-LBS frame-2 computation
2. first reproduce the archived Step-17 elbow frame-2 aggregate results across Seattle, Parkinglot, and Jogging within the frozen numerical tolerance
3. if that regression fails, stop before interpreting shoulder output
4. if it passes, evaluate left shoulder SMPL 16, z +10 degrees, branch `[16,18,20,22]`
5. evaluate learned, K6, and frozen-contralateral selective branch ablation conditions
6. preserve the Parkinglot Step-18A mean-support reversal regardless of causal outcome
7. save raw per-Gaussian arrays only to Drive and archive compact results to GitHub after review

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, and accidental inspection leakage rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
