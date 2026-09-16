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

### Important observation

The descriptive expectation `mean learned branch support > mean K6 branch support` does not hold uniformly. Parkinglot reverses the mean ordering. This must be retained rather than tuned away.

The reversal does **not** itself fail the causal shoulder protocol because support mass is not the causal displacement metric. Notably, 76.31% of Parkinglot contralateral rows still have learned branch mass greater than K6, indicating a distributional/tail effect rather than majority-row reversal.

Integrity checks passed:

- frozen HC/contralateral counts exactly matched Step 17A2
- learned and K6 row sums within approximately `3e-7` of 1
- zero NaNs

Archived artifacts:

- `research/sessions/2026-09-16-step18a.md`
- `experiments/08-second-joint-generalization/analysis/18A_left_shoulder_branch_support_precursor.csv`
- `experiments/08-second-joint-generalization/analysis/18A_left_shoulder_branch_support_precursor.json`

Drive artifacts also saved by Colab:

- `experiments/08-second-joint-generalization/18A_left_shoulder_branch_support_precursor.csv`
- `experiments/08-second-joint-generalization/18A_left_shoulder_branch_support_precursor.json`

## Exact next action

Do **not** change the predeclared shoulder protocol.

Next run a CPU-only Step 18B0 artifact/key inventory to recover the exact stored Step-17 deformation inputs and pose/SMPL artifact keys before constructing the shoulder frame-2 causal test. This avoids guessing file names or array keys and does not inspect shoulder causal displacement.

After that inventory, run Step 18B1 shoulder frame-2 causal diagnostic unchanged across Seattle, Parkinglot, and Jogging.

## Research-record rule

Preserve failures, reversals, disproven assumptions, and implementation problems rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
