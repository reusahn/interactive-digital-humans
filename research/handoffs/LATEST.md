# Latest Research Handoff

Current continuation date: **2026-09-17**.

## ACTIVE PRIORITY — A100 Step-18 canonical revalidation

The user clarified that the intended canonical research runtime through Step 17 was A100 and requested that the scientific Step-18 work performed after the T4 hardware-sensitivity diagnostic be re-run on A100 rather than treating T4 as the continuing primary runtime.

Canonical revalidation runtime:

```text
GPU: NVIDIA A100-SXM4-40GB
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

Important provenance distinction:

- archival Step-17 files explicitly establish CUDA use but did not themselves identify the GPU model;
- the A100-through-Step-17 provenance is user-supplied project provenance and is now being preserved explicitly;
- the prior T4 Step-18 files must remain preserved as historical hardware-sensitivity/scientific artifacts and must not be overwritten.

### Step 18R0A/R0B environment and input recovery

A fresh Colab A100 session was rebuilt and verified at the exact pinned legacy stack above. Google Drive was mounted, all frozen Step-18 inputs were found, and `SMPL_NEUTRAL_clean.pkl` loaded successfully under NumPy 1.24 compatibility aliases.

SMPL fingerprint:

```text
SHA256: f12586bb4b97761b1d401996832a3eb5f8e28f99d0ddb108d58dad5ae82f2fc0
```

No scientific computation occurred during R0A/R0B.

### Step 18R1 A100 frame-2 shoulder rerun COMPLETE

Frozen scientific protocol and thresholds were unchanged from historical Step 18B1H.

A100 results:

```text
Seattle
K6 reduction: 38.89052698499022%      FAIL
selective ablation: 100.0%            PASS
correlation: 0.9616730744322076       PASS
overall: False

Parkinglot
K6 reduction: -49.15654343505103%     FAIL
selective ablation: 100.0%             PASS
correlation: 0.9769195553081134        PASS
overall: False

Jogging
K6 reduction: 59.774070438714524%     FAIL
selective ablation: 100.0%             PASS
correlation: 0.8946040920942271        FAIL
overall: False
```

All 3 checkpoints reproduced changed transforms `[16,18,20,22]` exactly.

Cross-checkpoint R1 synthesis:

```text
all kinematic pass: True
all K6 pass: False
all selective-ablation pass: True
all correlation pass: False
all three frame-2 shoulder cells pass: False
threshold-level status same as historical T4: True
```

A100-vs-T4 scalar changes were small and changed no threshold-level classification. Thus the frame-2 shoulder failure is not a T4 artifact.

Archived session:

`research/sessions/2026-09-17-step18r1-a100-frame2-rerun.md`

Session commit:

`73800170c03d5c9065fbeeaa713534038b84f8d6`

Drive artifacts:

- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_cross_checkpoint.json`
- `experiments/08-second-joint-generalization/18R1_A100_left_shoulder_frame2_displacements.npz`

### Exact next action

Run Step 18R2: the complete frozen 18-pose shoulder schedule on the same A100 legacy runtime, using new A100-specific filenames and preserving historical T4 Step 18B2 artifacts.

Only after R2 should the exploratory C1/C2/C3 synthesis be recomputed on A100. Step 19 remains paused until the Step-18 A100 revalidation and continuity reconciliation are complete.

## Statistical hierarchy

- independent pretrained model unit: checkpoint, `n=3`
- checkpoints: Seattle, Parkinglot, Jogging
- pose/frame diagnostics are nested within checkpoints
- wrist, elbow, shoulder are repeated joint diagnostics within the same checkpoints

## Frozen distal benchmark

Left wrist Step 16E0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.708575087815%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9808287038512752
```

Predeclared left elbow Step 17C0:

```text
checkpoint passes: 3/3
nested poses: 18
global min K6 reduction: 99.81874059431833%
global min selective-ablation reduction: 100.0%
global min removed-mass correlation: 0.9688984153761956
```

Combined wrist + elbow: `6/6` joint x checkpoint cells pass across `36` nested pose diagnostics.

Historical elbow exact-number reproduction under reconstructed runtimes is `5/6` within the old `1e-5` aggregate gate on modern A100, legacy-stack A100, and legacy-stack T4. Field correlations remain effectively `1.0`; the historical gate was not widened.

## Historical Step-18 T4 continuation runtime

Historical Step-18 scientific artifacts from B1H onward were produced under:

```text
GPU: Tesla T4
Python: 3.8.20
NumPy: 1.24.4
PyTorch: 1.13.1+cu117
CUDA: 11.7
SMPLX: 0.1.28
TF32: off
```

These files remain preserved. T4 is no longer the intended canonical continuation runtime for the active revalidation.

## Frozen shoulder protocol and historical T4 negative result

Protocol: `research/protocols/2026-09-16-third-joint-generalization.md`

```text
joint: left shoulder, SMPL 16
perturbation: local z +10°
descendant branch: [16,18,20,22]
contralateral subset: {14,17,19,21,23}
K6 reduction threshold: >=95%
selective-ablation threshold: >=99.999%
correlation threshold: >=0.90
```

Historical T4 Step 18B2 full schedule:

```text
nested poses: 18
kinematic passes: 18/18
K6 passes: 0/18
selective-ablation passes: 18/18
corr passes: 14/18
overall passes: 0/18
negative K6 reductions: 5
K6 reduction range: -77.671145% to 76.389818%
```

The predeclared shoulder universal generalization is historically **FAIL**. A100 R1 already preserves the same frame-2 threshold classifications; R2 will determine the complete A100 full-schedule numbers.

## Historical Step 18C0 three-joint synthesis

| Joint | Predeclared status | Branch-mediated causality | Learned-vs-K6 amplification | Global min K6 reduction |
|---|---|---|---|---:|
| wrist | PASS | supported | supported | `99.708575%` |
| elbow | PASS | supported | supported | `99.818741%` |
| shoulder | FAIL | supported | not supported | `-77.671145%` |

Historical frozen claims pending A100 Step-18 numeric reconciliation:

- branch-mediated contralateral causality: `SUPPORTED_ACROSS_ALL_THREE_TESTED_JOINTS`
- learned-vs-K6 amplification: `JOINT_DEPENDENT_NOT_UNIVERSAL`
- kinematic-depth explanation: `HYPOTHESIS_ONLY`

Drive: `experiments/08-second-joint-generalization/18C0_three_joint_synthesis.json`

## Historical Step 18C1-C4 exploratory shoulder mechanism decomposition

C1: aggregate shoulder branch-support direction matches majority displacement direction in `3/3` checkpoints.

C2 per-row shoulder branch-mass matching median full-field MAE-gap reduction:

```text
Seattle:    94.495471%
Parkinglot: 83.846952%
Jogging:    93.517130%
```

C3 composition-only matching median full-field MAE-gap reduction:

```text
Seattle:    -0.104023%
Parkinglot: -2.195192%
Jogging:     0.203295%
```

K6 shoulder-branch mass is zero on most contralateral rows:

```text
Seattle:    78.24%
Parkinglot: 73.85%
Jogging:    91.45%
```

Historical Step 18C4 exploratory mechanism freeze:

- support topology + per-row magnitude: `DOMINANT_EXPLORATORY_FACTOR`
- within-branch composition: `SMALL_EFFECT_ON_DEFINED_OVERLAP`
- pose geometry: `RESIDUAL_MODULATOR_PLAUSIBLE`
- kinematic depth: `HYPOTHESIS_ONLY`

These exploratory deformation-dependent analyses must be recomputed/reconciled after A100 R2 rather than silently retained as canonical A100 numbers.

## Step 18D0 arm-chain branch-support topology

Nested descendant branches:

```text
wrist    [20,22]
elbow    [18,20,22]
shoulder [16,18,20,22]
```

Learned support is positive on `100%` of frozen contralateral rows for every tested joint/checkpoint.

K6 positive-support fractions:

```text
Seattle:    wrist 0.0046263 | elbow 0.0062591 | shoulder 0.2175859
Parkinglot: wrist 0.0022287 | elbow 0.0022287 | shoulder 0.2615238
Jogging:    wrist 0.0019629 | elbow 0.0019629 | shoulder 0.0854599
```

Learned-positive/K6-zero topology-gap fractions:

```text
Seattle:    wrist 0.9953737 | elbow 0.9937409 | shoulder 0.7824141
Parkinglot: wrist 0.9977713 | elbow 0.9977713 | shoulder 0.7384762
Jogging:    wrist 0.9980371 | elbow 0.9980371 | shoulder 0.9145401
```

Aggregate learned/K6 branch-support ratios:

```text
Seattle:    wrist 650.22 | elbow 708.93  | shoulder 1.5764
Parkinglot: wrist 404.35 | elbow 1108.68 | shoulder 0.8379
Jogging:    wrist 725.56 | elbow 1355.29 | shoulder 5.5557
```

D0 is weight-topology descriptive analysis and did not require new deformation computation. It can be retained as structural input while the deformation-dependent A100 synthesis is recomputed.

## Historical Step 18D1 arm-chain synthesis

Historical T4 synthesis described the bounded mechanism as:

`DESCENDANT_SUPPORT_TOPOLOGY_AND_PER_ROW_MAGNITUDE`

The scientific interpretation is not currently contradicted by A100 R1, but deformation-dependent C/D numbers should not be promoted as canonical A100 results until the active rerun sequence is complete.

## Current stop point

Do **not** begin Step 19 yet.

Current sequence:

`18R1 A100 frame2 complete -> 18R2 A100 full pose -> recompute A100 C1/C2/C3 -> reconcile C0/C4/D synthesis -> update MASTER_CONTEXT and CLAIM_LEDGER if needed -> only then Step 19 preregistration`

## Research-record rule

Preserve both historical T4 artifacts and new A100 artifacts. Never overwrite failed results, never widen historical thresholds, and never silently replace old numbers without recording runtime provenance. Nested poses remain diagnostics rather than independent model-level replications.
