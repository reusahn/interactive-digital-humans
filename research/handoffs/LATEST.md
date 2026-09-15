# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Research-record rule: preserve failed assumptions

Failed assumptions, disproven hypotheses, and implementation misunderstandings are first-class research records. Do not keep only the final successful interpretation.

For each meaningful failure, preserve:

1. assumption before test,
2. observation that contradicted it,
3. corrected interpretation,
4. impact on prior results,
5. follow-up audit/action.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`

The Step-17B1B alias failure is separately archived in:

`research/sessions/2026-09-15-step17b1b-assumption-failure.md`

## Frozen left-wrist benchmark

The completed left-wrist causal finding is frozen across **three independently pretrained HUGS NeuMan checkpoints**.

Independent unit: pretrained checkpoint, `n = 3`.

Within-checkpoint pose diagnostics: `18` total, nested within those three checkpoints and not to be counted as 18 independent replications.

```text
checkpoint causal passes: 3 / 3
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9808287038512752
global maximum ablated contralateral sum: 0.0
LEFT-WRIST CROSS-CHECKPOINT BENCHMARK FROZEN: True
```

Frozen primary claim:

> In three independently pretrained HUGS NeuMan checkpoints, Seattle, Parkinglot, and Jogging, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding subject-specific SMPL-derived K6 target under the tested left-wrist perturbation. The causal pattern is stable across the tested base poses within each checkpoint.

Do not pool raw displacement across sequences because sequence scale differs. Do not describe the 18 frame tests as independent replications.

## Predeclared second-joint protocol

Frozen before any left-elbow displacement was inspected:

- joint: `left_elbow` (`SMPL 18`)
- axis: `z`
- perturbation: `+10 deg`
- checkpoints: Seattle, Parkinglot, Jogging
- pose schedules: Seattle `[2,7,12,17]`, Parkinglot `[2,7,12,17]`, Jogging `[2,7,12,17,22,27,32,37,42,47]`
- confidence threshold: `>=0.9`
- contralateral anatomy: `{14,17,19,21,23}`
- perturbed branch channels: `{18,20,22}`
- expected changed transforms: exactly `[18,20,22]`

Frozen diagnostic thresholds:

```text
K6 reduction vs learned >= 95%
selective-ablation reduction >= 99.999%
removed-mass vs displacement-reduction correlation >= 0.90
maximum ablated contralateral displacement <= 1e-8
changed transforms exactly [18,20,22]
```

Failures remain results. Do not change joint, axis, angle, mask, or thresholds in response to outcome.

## Canonical anatomy sources frozen at Step 17A2

- Seattle masks: `saved_dominant` + `saved_confidence` from Step 13A
- Parkinglot masks: stored `dominant_joint` + `joint_confidence` from Step 16C2
- Jogging masks: stored `dominant_joint` + `joint_confidence` from Step 16D3
- K6 deformation condition: checkpoint-specific `effective_lbs`

```text
Seattle    HC 197778  contra 33072
Parkinglot HC 292095  contra 77622
Jogging    HC 148392  contra 20887
CANONICAL ANATOMY SOURCES FROZEN: True
```

Seattle's saved/recomputed anatomy discrepancy remains a historical provenance issue, but the benchmark-consistent mask source was frozen before elbow causal testing.

## Step 17B1 - left-elbow raw-frame-2 causal result

The predeclared left-elbow `z +10 deg` causal test passed in all three independently pretrained checkpoints on common raw frame 2.

| Checkpoint | Learned contra | K6 contra | Ablated contra | Learned contra % HC | K6 reduction | Ablation reduction | Removed-mass corr | Changed transforms | Pass |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| Seattle | 2.6505639553 | 0.0048044017 | 0.0 | 0.5360253% | 99.8187404% | 100.0% | 0.9708237 | `[18,20,22]` | True |
| Parkinglot | 11.0941810608 | 0.0116030509 | 0.0 | 0.5745978% | 99.8954132% | 100.0% | 0.9958911 | `[18,20,22]` | True |
| Jogging | 1.2263532877 | 0.0009509723 | 0.0 | 0.6924628% | 99.9224553% | 100.0% | 0.9863545 | `[18,20,22]` | True |

```text
checkpoint frame-2 passes: 3 / 3
minimum K6 reduction: 99.81874039866663%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation: 0.9708236964422226
maximum ablated contralateral displacement: 0.0
ALL THREE FRAME-2 ELBOW CAUSAL PASSES: True
```

Interpretation: strong second-joint causal evidence at one common base pose per checkpoint. Full elbow pose robustness is not yet established.

## Step 17B1A - exact source-semantics audit

Exact HUGS source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

The located released implementation is `hugs/models/hugs_trimlp.py`, class `HUGS_TRIMLP`.

Its constructor does not pass activation into `GeometryDecoder` or `DeformationDecoder`; both decoder classes default to `act='gelu'`.

The audit directly confirmed:

- `softmax(lbs_weights / 0.1)`
- canonical xyz = checkpoint xyz + geometry xyz offset
- `A_vitruvian2pose = A_t2pose @ inv_A_t2vitruvian`
- `disable_posedirs=True` zeroes pose offsets and uses `v_posed = v_shaped`

Numeric source-exact reconstruction matched stored experimental arrays exactly:

```text
Seattle    LBS all differences 0.0, dominant mismatch 0
Parkinglot LBS all differences 0.0, XYZ all differences 0.0
Jogging    LBS all differences 0.0, XYZ all differences 0.0
SOURCE SEMANTICS EXACT: True
```

No reconstruction rerun is indicated by the activation/forward-semantics audit.

## Step 17B1B - failed alias assumption

Pre-audit assumption:

> packaged `human.name: hugs_triplane` should resolve through an explicit alias/registry/factory mapping to `HUGS_TRIMLP`.

Observed result:

```text
HUGS_TRIMLP definition confirmed: True
literal `hugs_triplane` Python-source hit count: 0
RuntimeError: No official Python source contains literal hugs_triplane.
```

This is preserved as a failed provenance assumption, not deleted from the research history.

## Step 17B1C - packaged-config naming drift resolved

Exact commit string audit:

```text
tracked `hugs_triplane` hits: 0
tracked `hugs_trimlp` hits: 8
```

Official release config:

```text
human.name: hugs_trimlp
human.activation: relu
```

Official trainer:

```text
imports HUGS_TRIMLP: True
checks human.name == hugs_trimlp: True
constructs HUGS_TRIMLP: True
checks human.name == hugs_triplane: False
RELEASED TRAINER hugs_trimlp -> HUGS_TRIMLP: True
```

Downloaded pretrained package configs:

```text
Seattle    human.name = hugs_triplane
Parkinglot human.name = hugs_triplane
Jogging    human.name = hugs_triplane
```

Decision:

```text
released source contains hugs_trimlp: True
released source contains hugs_triplane: False
official release config uses hugs_trimlp: True
packaged configs all use hugs_triplane: True
trainer exact hugs_trimlp -> HUGS_TRIMLP: True
no released hugs_triplane alias: True
Step 17B1A source semantics exact: True
Step 17B1A numeric match: True
PACKAGED CONFIG LABEL DRIFT RESOLVED: True
```

Correct wording: the pretrained package config naming differs from the released implementation/config naming. Do **not** claim an executable alias exists. The historical cause of the naming mismatch is not established by this audit, so do not call it legacy/stale packaging as a fact without further evidence.

No reconstruction rerun is required because the checkpoint outputs numerically match released HUGS_TRIMLP semantics exactly.

## Immediate next action

Run the **full predeclared left-elbow pose robustness schedule** with frozen masks and unchanged thresholds:

- Seattle `[2,7,12,17]`
- Parkinglot `[2,7,12,17]`
- Jogging `[2,7,12,17,22,27,32,37,42,47]`

Require raw frame 2 to regress exactly to Step 17B1 before interpreting the remaining frames.

## Continuity files

- `research/methodology/assumption-failure-ledger.md`
- `research/sessions/2026-09-15-step17b1b-assumption-failure.md`
- `research/sessions/2026-09-15-step17b1c.md`
- `experiments/08-second-joint-generalization/analysis/17B1C_packaged_config_label_drift_audit.json`
- `research/sessions/2026-09-15-step17b1a.md`
- `experiments/08-second-joint-generalization/analysis/17B1A_exact_hugs_source_semantics_audit.json`
- `research/sessions/2026-09-15-step17b1.md`
- `experiments/08-second-joint-generalization/analysis/17B1_left_elbow_frame2_cross_checkpoint.csv`
- `research/sessions/2026-09-15-step17a2.md`
- `experiments/08-second-joint-generalization/analysis/17A2_left_elbow_canonical_precursor.csv`
- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/protocols/2026-09-15-second-joint-generalization-implementation-note.md`
