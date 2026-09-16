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

The initial B0 search also guessed two old directory names incorrectly. The corrected names are:

- `experiments/05-counterfactual-lbs-ablation`
- `experiments/06-frame-replication`

Archived record:

`research/sessions/2026-09-16-step18b0.md`

## Step 18B0A Seattle canonical-XYZ provenance recovery COMPLETE

The corrected provenance search found the original Seattle baseline probe artifact family under

`experiments/01-baseline/probe_results/`

with exact `(472958,3)` float32 arrays:

- `xyz_before`
- `xyz_after`
- `xyz_canon`

A historical duplicate also exists under

`experiment-01/20260914_003959/frame000_left_wrist_z_10deg.npz`.

All reported `xyz_canon` candidates shared the same summary statistics:

```text
min:      -0.8927599191665649
max:       0.8819881677627563
mean xyz: [-0.023014819249510765,
           -0.12770146131515503,
            0.013593386858701706]
```

This resolves the source family, but summary equality is not yet elementwise proof. Fix one authoritative Seattle source only after exact equality validation.

### Methodological note

B0A was intended as provenance-only inspection, but the generic candidate printer also emitted aggregate min/max/mean summaries for `xyz_after`, including the already-existing Seattle `left_shoulder z +10°` probe. It did **not** compute or display the frozen Step-18 causal metrics such as contralateral displacement, K6 reduction, selective-ablation reduction, removed-mass correlation, or pass/fail status.

The shoulder protocol remains frozen and unchanged. No tuning is permitted.

Archived record:

`research/sessions/2026-09-16-step18b0a.md`

Drive artifact:

`experiments/08-second-joint-generalization/18B0A_seattle_xyz_source_inventory.json`

## Exact next action

Run **Step 18B0B** on CPU only.

Purpose:

1. choose the Seattle baseline wrist-z +10 probe as the provisional canonical-source reference
2. verify `xyz_canon` elementwise across all baseline probe copies and the historical duplicate
3. verify the common `xyz_before` base state elementwise across baseline probes
4. do not read or summarize `xyz_after`
5. save a compact validation JSON

If exact equality passes, fix the Seattle canonical source path and immediately proceed next to Step 18B1 with the frozen shoulder protocol and an explicit regression against the Step-17 elbow frame-2 computation.

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, and accidental inspection leakage rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
