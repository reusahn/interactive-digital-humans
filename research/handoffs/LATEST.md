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

## Step 18B0 / B0A / B0B provenance block COMPLETE

Seattle canonical source was recovered and exactly validated.

Authoritative Seattle canonical reference:

`experiments/01-baseline/probe_results/frame000_left_wrist_z_10deg.npz`

Across 37 persistent baseline/historical copies:

```text
all shape OK: True
all dtype OK: True
all finite: True
all xyz_canon elementwise exact: True
all xyz_canon SHA256 match: True
all xyz_before elementwise exact: True
all xyz_before SHA256 match: True
SEATTLE CANONICAL XYZ EXACTLY VALIDATED: True
```

`xyz_canon` SHA256:

`61a633d5b2c1fb353d7790cdd176919f17c3f1000ce7e9cb5d03e2751b51d314`

`xyz_before` SHA256:

`291a1fcb5818b35ed0ecf6acdb461d2532fd4ce0323be3b10e3d12f67c075c73`

Archived records:

- `research/sessions/2026-09-16-step18b0.md`
- `research/sessions/2026-09-16-step18b0a.md`
- `research/sessions/2026-09-16-step18b0b.md`

## Step 18B1 BLOCKED by historical elbow regression gate

Step 18B1 was designed to reproduce Step-17B1 elbow frame-2 before interpreting any shoulder output.

The gate failed in all three checkpoints, so execution stopped before the shoulder causal section.

| Checkpoint | Current learned contra | Frozen learned contra | Learned abs diff | Current K6 contra | Frozen K6 contra | K6 abs diff | Current corr | Frozen corr | Regression pass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Seattle | 2.650197376676 | 2.650563955300 | 0.000366578624 | 0.004803800226 | 0.004804401660 | 0.000000601434 | 0.970826263032 | 0.970823696400 | False |
| Parkinglot | 11.092557772695 | 11.094181060800 | 0.001623288105 | 0.011602326001 | 0.011603050900 | 0.000000724899 | 0.995891130849 | 0.995891100000 | False |
| Jogging | 1.226277361622 | 1.226353287700 | 0.000075926078 | 0.000953316052 | 0.000950972300 | 0.000002343752 | 0.986356606925 | 0.986354500000 | False |

Still correct in all three checkpoints:

- changed transforms exactly `[18,20,22]`
- selective-ablation contralateral response exactly `0.0`
- correlation nearly identical to the frozen result

The frozen aggregate regression tolerance was `1e-5`, so the learned sums fail. Do **not** widen the tolerance after seeing this output.

Interpretation:

- pipeline/source-equivalence blocker only
- not a shoulder result
- not evidence against the frozen shoulder hypothesis
- no Step-18B1 shoulder causal metric is accepted
- prior Step-17 benchmark remains unchanged

Archived:

- `research/sessions/2026-09-16-step18b1-regression-blocker.md`
- failure ledger entry `A010`

## Step 18B1A key-resolution failure recorded

The first per-Gaussian audit completed Seattle and Parkinglot but the generic token `frame2` also matched Jogging `frame22` and `frame27`, causing a key-resolution error. This is an implementation bug only.

Archived:

- `research/sessions/2026-09-16-step18b1a-key-resolution-blocker.md`
- failure ledger entry `A011`

## Step 18B1A-R exact-key per-Gaussian audit COMPLETE

Exact Step-17B1 and Step-17B2 frame-02 keys were used across all three checkpoints.

The current manual Step-18B1 reconstruction is spatially almost identical to the historical Step-17 elbow fields:

| Checkpoint | Learned relative whole-array sum error | Learned mean abs per-Gaussian diff | Learned max abs diff | Learned Pearson | Optimal global scale | Scaled residual L2 fraction |
|---|---:|---:|---:|---:|---:|---:|
| Seattle | -0.000575924729% | 7.884706e-08 | 7.179369e-07 | 0.999999999928 | 1.000000267806 | 1.178276e-05 |
| Parkinglot | -0.000344996869% | 1.124316e-07 | 1.308632e-06 | 0.999999999979 | 1.000000288787 | 6.333825e-06 |
| Jogging | -0.000889985277% | 7.080164e-08 | 6.406544e-07 | 0.999999999839 | 1.000000071249 | 1.776511e-05 |

K6 differences are smaller still. Ablated fields show the same tiny distributed discrepancy pattern as learned fields.

Step-17 internal consistency is strong:

- Parkinglot B1 vs B2 frame-02 arrays: bitwise exact for learned/K6/ablated
- Jogging B1 vs B2 frame-02 arrays: bitwise exact for learned/K6/ablated
- Seattle B1 vs B2 frame-02 arrays: not bitwise exact but near-exact with mean abs differences <=1e-9

Interpretation: the Step-17 archive is internally consistent. The mismatch is specific to the new manual Step-18B1 reconstruction path. It is not a different spatial field, but the frozen aggregate tolerance still must not be widened.

Leading untested hypothesis: floating-point evaluation order. Step-18B1 currently computes displacement directly from `delta_A = A_after - A_before`; the historical pipeline may have generated full float32 before/after posed positions and then subtracted/normed them. Algebraic equivalence does not guarantee bitwise equality in float32.

Archived:

- `research/sessions/2026-09-16-step18b1a-r.md`

Drive artifact:

`experiments/08-second-joint-generalization/18B1A_R_elbow_per_gaussian_regression_audit.json`

No shoulder computation has been accepted or interpreted.

## Exact next action

Run **Step 18B1B**, elbow only.

1. reconstruct full float32 before and after posed positions with the current A matrices
2. compute displacement from posed-position subtraction using NumPy float32 and Torch float32 variants
3. compare those variants directly against archived Step-17B1 per-Gaussian arrays
4. test whether evaluation order explains the aggregate regression blocker
5. do not compute shoulder metrics
6. do not alter the frozen `1e-5` historical regression tolerance

Only after the historical elbow regression path is reproduced should Step 18B1 be repaired and rerun with the frozen shoulder protocol unchanged.

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, and accidental inspection leakage rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
