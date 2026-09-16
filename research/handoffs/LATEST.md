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

Step 18A inspected only frozen contralateral branch-support mass. It did not compute shoulder causal displacement.

Parkinglot reverses the mean learned/K6 branch-support ordering (`0.8379x`) and that reversal remains part of the record.

## Step 18B0 / B0A / B0B provenance block COMPLETE

Seattle canonical source was recovered and exactly validated across 37 persistent copies.

Authoritative Seattle canonical reference:

`experiments/01-baseline/probe_results/frame000_left_wrist_z_10deg.npz`

`xyz_canon` SHA256:

`61a633d5b2c1fb353d7790cdd176919f17c3f1000ce7e9cb5d03e2751b51d314`

## Step 18B1 historical elbow gate BLOCKED

The newly written CPU/manual SMPL-LBS reconstruction did not reproduce the frozen Step-17B1 elbow contralateral learned sums within the frozen `1e-5` aggregate tolerance, so execution stopped before shoulder causal metrics were accepted.

This remains a pipeline/source-equivalence blocker, not a shoulder result.

## Step 18B1A-R completed per-Gaussian audit

Across all three checkpoints, current versus archived Step-17 elbow fields are spatially nearly identical:

- learned Pearson values: `>= 0.999999999839`
- learned mean per-Gaussian absolute differences: about `7e-8` to `1.1e-7`
- K6 agreement is even closer
- Step-17B1 and Step-17B2 frame-2 arrays are exact for Parkinglot/Jogging and near-exact for Seattle

No tolerance was changed.

Archived:

`research/sessions/2026-09-16-step18b1a-r.md`

## Step 18B1B evaluation-order audit COMPLETE

The hypothesis that displacement evaluation order alone caused the blocker was disproved.

Switching from direct `delta-A` displacement to full float32 before/after position evaluation greatly reduces learned-condition contralateral-sum error, but learned still fails the frozen `1e-5` regression gate in all three checkpoints:

| Checkpoint | direct delta-A learned error | best full-position learned error | gate |
|---|---:|---:|---|
| Seattle | `-3.667395e-4` | `-2.927389e-5` | FAIL |
| Parkinglot | `-1.622576e-3` | `+4.781559e-5` | FAIL |
| Jogging | `-7.595423e-5` | `+1.115697e-5` | FAIL |

K6 passes the aggregate `1e-5` gate in all three checkpoints.

Seattle historical elbow before/after positions are also only slightly different from the current reconstruction at float32 scale:

- before mean abs: `5.063156e-08`
- before max abs: `9.536743e-07`
- after mean abs: `4.979415e-08`
- after max abs: `9.536743e-07`

Interpretation: evaluation order contributes but does not fully explain the mismatch. The next likely source is manual versus source-exact SMPL transform construction and/or backend floating-point execution order.

Archived:

- `research/sessions/2026-09-16-step18b1b.md`
- failure ledger `A012`

Drive artifact:

`experiments/08-second-joint-generalization/18B1B_elbow_evaluation_order_audit.json`

## Step 18B1C dependency recovery COMPLETE

The HUGS-pinned dependency `smplx==0.1.28` is installed and importable in the current CPU runtime.

## Step 18B1C namespace blocker

The first post-install rerun of Step 18B1C stopped before any scientific audit result with:

```text
TypeError: blend_shapes() missing 1 required positional argument: 'shape_disps'
```

Cause: the dependency-verification cell imported SMPLX helpers into the global notebook namespace without aliases. Step 18B1's pre-existing `compute_A` resolves `blend_shapes` dynamically and therefore began calling `smplx.lbs.blend_shapes` instead of the local one-argument helper.

This is namespace pollution only. No shoulder computation ran and no transform/backend conclusion can be drawn from this failed attempt.

Archived:

- `research/sessions/2026-09-16-step18b1c-namespace-blocker.md`
- failure ledger `A013`

## Exact next action

Run a patched **Step 18B1C-R** that is self-contained with isolated names:

1. import SMPLX functions only as `sx_*`
2. define the manual comparison path under `manual_*` names
3. do not call the mutated global `compute_A`
4. compare manual versus SMPLX `A` transforms
5. test source-exact chunked and one-shot elbow frame-2 displacement against archived Step-17B1 arrays
6. preserve the frozen `1e-5` regression tolerance
7. do not compute shoulder metrics yet

## Research-record rule

Preserve failures, reversals, disproven assumptions, implementation problems, and accidental inspection leakage rather than rewriting history after later success.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`
