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

Step 18B0 inspected persistent artifacts and array layouts only. **No shoulder perturbed displacement was computed.**

Confirmed:

- licensed original and cleaned SMPL assets exist
- Step 17A2 frozen masks exist
- Seattle, Parkinglot, and Jogging learned-LBS and K6 arrays exist with expected `(G,24)` shapes
- all three NeuMan pose assets exist
- prior Parkinglot/Jogging wrist counterfactual and frame-replication artifacts remain present
- Step 17B1 elbow frame-2 displacement artifact remains present with learned/K6/ablated/removed-branch arrays for all three sequences
- Step 17B2 full-pose elbow displacement artifact remains present for all 18 nested poses

### Important input asymmetry

Parkinglot and Jogging learned-LBS artifacts contain `xyz_canon` directly.

Seattle `13E_learned_lbs_weights.npz` does **not** contain canonical Gaussian XYZ. Seattle canonical positions must therefore be recovered from the earlier Seattle diagnostic/counterfactual artifacts before Step 18B1 is constructed.

### Step 18B0 path correction

The inventory cell guessed two historical Drive directory names incorrectly:

- guessed `experiments/05-causal-counterfactual`, actual `experiments/05-counterfactual-lbs-ablation`
- guessed `experiments/06-pose-robustness`, actual `experiments/06-frame-replication`

This affected only artifact discovery. It did not alter any scientific result, threshold, mask, pose, or perturbation. The corrected historical names are now fixed for the next inventory step.

Archived records:

- `research/sessions/2026-09-16-step18b0.md`
- `experiments/08-second-joint-generalization/analysis/18B0_artifact_inventory.json`

## Exact next action

Run **Step 18B0A** on CPU only.

Purpose:

1. search the corrected Seattle Experiment 01-06 persistent directories
2. identify the exact saved Seattle canonical Gaussian XYZ source used by prior causal work
3. inspect candidate NPZ/NPY keys and shapes only
4. do not run the shoulder perturbation yet

Only after Seattle canonical-XYZ provenance is recovered should Step 18B1 be constructed. Step 18B1 should include a regression against the frozen Step-17 elbow frame-2 computation before shoulder output is interpreted.

## Research-record rule

Preserve failures, reversals, disproven assumptions, and implementation problems rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
