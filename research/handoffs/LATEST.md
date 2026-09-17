# Latest Research Handoff

Current continuation date: **2026-09-17**.

## ACTIVE PRIORITY — finish A100 Step-18 canonical revalidation

Canonical continuation runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

User-supplied project provenance states that the intended runtime through Step 17 was A100. Historical Step-17 archives establish CUDA use but do not independently identify the GPU model. Preserve this distinction.

Historical Step-18 T4 artifacts remain preserved and must never be overwritten. The active A100 sequence is provenance reconciliation, not threshold tuning or hypothesis rescue.

SMPL fingerprint:

```text
SHA256: f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints
- wrist, elbow, shoulder are repeated joint diagnostics within the same checkpoints

Never count nested poses as independent replications.

## Frozen distal benchmark

Left wrist Step 16E0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.708575087815%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9808287038512752
```

Left elbow Step 17C0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.81874059431833%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9688984153761956
```

Combined wrist + elbow: `6/6` joint x checkpoint cells pass across `36` nested pose diagnostics.

Historical Step-17 exact-number reconstruction recovered 5/6 aggregates within the old `1e-5` scalar gate on tested replacement runtimes; field correlations remained essentially 1.0. The gate was not widened.

## Step 18R0A / R0B — environment and input recovery COMPLETE

The exact pinned A100 legacy stack was rebuilt in `/content/hugs_legacy_torch113_py38`; Drive inputs and the SMPL pickle were verified. No scientific deformation computation occurred in R0A/R0B.

## Step 18R1 — A100 frame-2 shoulder rerun COMPLETE

Frozen Step 18B1H protocol and thresholds unchanged.

```text
Seattle:    K6 reduction 38.89052698499022%  FAIL | ablation 100% PASS | corr 0.9616730744322076 PASS
Parkinglot: K6 reduction -49.15654343505103% FAIL | ablation 100% PASS | corr 0.9769195553081134 PASS
Jogging:    K6 reduction 59.774070438714524% FAIL | ablation 100% PASS | corr 0.8946040920942271 FAIL
```

All three checkpoints reproduced changed transforms `[16,18,20,22]`. Threshold-level status matched historical T4 exactly.

Archive: `research/sessions/2026-09-17-step18r1-a100-frame2-rerun.md`

Drive:
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_displacements.npz`

## Step 18R2 — A100 full 18-pose shoulder rerun COMPLETE

Frozen pose schedule:

```text
Seattle:    [2,7,12,17]
Parkinglot: [2,7,12,17]
Jogging:    [2,7,12,17,22,27,32,37,42,47]
```

Global A100 result:

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
correlation passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction range: -77.67225758078598% to 76.3901059303657%
K6 reduction median: 42.390431156682965%
correlation range: 0.7985822327394099 to 0.9812400880684837
correlation median: 0.9436557686954412
```

Reproducibility:

```text
FRAME-2 THRESHOLD STATUS SAME AS R1: True
AGGREGATE THRESHOLD COUNTS SAME AS HISTORICAL T4: True
PER-POSE THRESHOLD STATUS SAME AS HISTORICAL T4: True
```

The preregistered shoulder generalization remains **FAIL** on canonical A100. The historical T4 shoulder result is not a hardware-specific scientific artifact.

Archive: `research/sessions/2026-09-17-step18r2-a100-full-pose-rerun.md`

Drive:
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_metadata.json`
- `experiments/08-second-joint-generalization/18R2_A100_left_shoulder_full_pose_displacements.npz`

## Current confirmatory three-joint interpretation

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification |
|---|---|---|---|
| wrist | PASS | supported | supported |
| elbow | PASS | supported | supported |
| shoulder | FAIL | supported | not supported |

Bounded claims remain:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

## Step 18R3 — A100 C1 support-mass reconciliation COMPLETE

Analysis class: `EXPLORATORY_POST_HOC`.

A100 support values are exactly unchanged because weight fields/masks are unchanged:

```text
Seattle:    learned/K6 support ratio 1.5764279015288012 | support learned | majority displacement learned | matches 3/4
Parkinglot: learned/K6 support ratio 0.8379048191221863 | support K6     | majority displacement K6     | matches 4/4
Jogging:    learned/K6 support ratio 5.5557058081619255 | support learned | majority displacement learned | matches 10/10
```

A100/T4 conclusion reconciliation:

```text
checkpoint support-majority direction matches: 3/3 on A100 and T4
checkpoint-level C1 conclusion same: True
all checkpoint directions same A100 vs T4: True
all per-pose displacement/support-match directions same A100 vs T4: True
```

Archive: `research/sessions/2026-09-17-step18r3-a100-c1-reconciliation.md`

Drive:
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.json`
- `experiments/08-second-joint-generalization/18R3_A100_shoulder_support_mass_exploratory.csv`

## Step 18R4 — A100 C2 support-mass matching reconciliation COMPLETE

Analysis class: `EXPLORATORY_POST_HOC`.

Counterfactual definition unchanged from historical C2:

> Preserve learned within-branch composition, set each frozen contralateral Gaussian's total shoulder-descendant branch mass to its corresponding K6 mass, and proportionally rescale learned non-branch weights to preserve row sum.

All checkpoints had zero fallback rows and pure learned-composition fraction `1.0`.

A100 median full-field MAE-gap reduction:

```text
Seattle:    94.49566207250349%
Parkinglot: 83.84751353605428%
Jogging:    93.51752945582919%
```

Historical T4 medians:

```text
Seattle:    94.49547062277841%
Parkinglot: 83.84695205957038%
Jogging:    93.51712996485506%
```

A100 - T4 median differences:

```text
Seattle:    +0.00019144972507945113 percentage points
Parkinglot: +0.0005614764838952624 percentage points
Jogging:    +0.0003994909741322772 percentage points
```

A100 C2 medians therefore reproduce the historical large field-gap reduction essentially unchanged. The descriptive `>80%` flag is not a preregistered threshold.

Interpretation preserved: per-row descendant-branch support topology and total support magnitude remain strongly implicated as major explanatory factors for the shoulder learned-vs-K6 displacement-field difference. This does not establish a training-level cause and cannot alter the failed confirmatory shoulder result.

Archive: `research/sessions/2026-09-17-step18r4-a100-c2-reconciliation.md`

R4 session commit: `ae8e3b03436bbca9b3f69a10f631bb5885900ad1`

Drive:
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual.json`
- `experiments/08-second-joint-generalization/18R4_A100_shoulder_support_match_counterfactual_displacements.npz`

Historical T4 C2 artifacts remain preserved.

## Historical C3 target for A100 reconciliation

Historical Step 18C3 counterfactual:

- preserve learned total shoulder branch mass
- replace only within-branch joint allocation over `[16,18,20,22]` with K6 composition where K6 branch mass is positive
- when learned branch mass is positive but K6 branch mass is zero, K6 composition is undefined; leave learned composition unchanged and count these rows rather than inventing a composition

Historical K6 composition-defined coverage:

```text
Seattle:    7196 / 33072 = 0.21758587324625062
Parkinglot: 20300 / 77622 = 0.2615237948004432
Jogging:    1785 / 20887 = 0.08545985541245751
```

Historical T4 full-field MAE-gap reduction min/median/max:

```text
Seattle:    -0.18710644909942786 / -0.10402258952364463 / 0.15762290284524472 %
Parkinglot: -3.2815576226578935 / -2.1951923116722116 / -1.9180009113846097 %
Jogging:     0.054189093650924836 / 0.20329469100371367 / 2.111938172181793 %
```

Historical T4 defined-overlap-only median MAE-gap reduction:

```text
Seattle:    -0.23979397289649595%
Parkinglot: -3.1557623872811136%
Jogging:     0.951095835217225%
```

Historical C3 interpretation: within-branch composition matching produces essentially no field-gap reduction (and sometimes worsens it), in sharp contrast to C2 total branch-mass matching.

## Step 18D0 structural topology analysis

D0 uses frozen weight topology rather than newly computed deformation fields and does not require GPU rerun solely because historical B1H/B2 were run on T4.

Learned support is positive on 100% of frozen contralateral rows for all tested joint/checkpoint cells. K6 shoulder support coverage is the C3 composition-defined coverage above.

Historical mechanism label remains provisional until R5 reconciliation finishes:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

## Exact next action

Run **Step 18R5**, canonical A100 reconciliation of historical Step 18C3.

R5 must preserve learned total branch mass and replace only K6 within-branch composition on rows where K6 branch mass is positive. Use the canonical A100 R2 learned/K6 displacement fields as the original gap and recompute the C3 counterfactual deformation on A100. Preserve historical C3 artifacts and compare full-field and defined-overlap results with historical T4 values.

After R5, reconcile C0/C4/D synthesis, update `MASTER_CONTEXT.md` and `CLAIM_LEDGER.md` if the A100 evidence warrants it, then and only then unpause Step 19 preregistration.

Current sequence:

`R0A/R0B complete -> R1 complete -> R2 complete -> R3 complete -> R4 complete -> R5 C3 next -> reconcile C0/C4/D -> finalize continuity -> Step 19 preregistration`

## Research-record rule

Preserve both historical T4 artifacts and new A100 artifacts. Never overwrite failed results, never widen historical thresholds, never silently replace old numbers without runtime provenance, and never use exploratory analyses to rewrite the failed confirmatory shoulder outcome.
