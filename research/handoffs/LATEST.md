# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Research-record rule

Preserve failed assumptions, disproven hypotheses, implementation misunderstandings, and code-delivery failures rather than rewriting history after correction.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`

Relevant recent failures already recorded include:

- Seattle frame mapping assumption
- ankle locality-target interpretation
- Seattle `>=0.9` vs `>0.9` hypothesis
- nonexistent `hugs_triplane -> HUGS_TRIMLP` alias assumption
- Step 17B2 truncated-cell syntax failure

## Frozen left-wrist benchmark

Completed across three independently pretrained HUGS NeuMan checkpoints.

```text
independent checkpoints: 3
nested wrist pose diagnostics: 18
checkpoint causal passes: 3 / 3
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9808287038512752
global maximum ablated contralateral sum: 0.0
LEFT-WRIST CROSS-CHECKPOINT BENCHMARK FROZEN: True
```

Do not treat 18 frames as 18 independent replications.

## Predeclared second-joint protocol

Frozen before elbow displacement was inspected:

- joint: left_elbow, SMPL 18
- axis: z
- angle: +10 deg
- branch channels: `[18,20,22]`
- expected changed transforms: `[18,20,22]`
- Seattle poses: `[2,7,12,17]`
- Parkinglot poses: `[2,7,12,17]`
- Jogging poses: `[2,7,12,17,22,27,32,37,42,47]`
- K6 reduction threshold: >=95%
- selective-ablation reduction threshold: >=99.999%
- removed-mass/reduction correlation threshold: >=0.90
- max ablated contralateral displacement: <=1e-8

## Canonical anatomy sources

Frozen before elbow causal testing:

```text
Seattle    saved_dominant + saved_confidence    HC 197778  contra 33072
Parkinglot dominant_joint + joint_confidence    HC 292095  contra 77622
Jogging    dominant_joint + joint_confidence    HC 148392  contra 20887
```

Seattle's saved/recomputed confidence discrepancy remains a historical provenance issue, but the benchmark-consistent source was frozen before perturbation.

## Source/provenance audits

Exact HUGS source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Step 17B1A established exact released HUGS_TRIMLP reconstruction semantics and zero numerical difference from stored learned-LBS arrays across Seattle, Parkinglot, and Jogging.

Step 17B1B disproved the assumption that an executable `hugs_triplane -> HUGS_TRIMLP` alias exists.

Step 17B1C established the correct provenance statement:

- released source/config name: `hugs_trimlp`
- trainer directly constructs `HUGS_TRIMLP`
- downloaded pretrained package configs contain `hugs_triplane`
- released commit contains no executable `hugs_triplane` alias
- historical cause of the naming mismatch is unknown
- exact numeric reconstruction means no experimental rerun is required

## Step 17B2 - full predeclared left-elbow pose robustness

All 18 predeclared elbow pose diagnostics passed. Independent model-level unit remains checkpoint, `n=3`.

| Checkpoint | Poses | Learned contra % HC range | Mean K6 reduction | Min K6 reduction | Min ablation reduction | Mean corr | Min corr | Max ablated contra | Pass |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Seattle | 4 | 0.515229-0.609622% | 99.825186% | 99.818741% | 100.0% | 0.973314 | 0.968898 | 0.0 | True |
| Parkinglot | 4 | 0.574598-0.579239% | 99.894670% | 99.891335% | 100.0% | 0.996069 | 0.995891 | 0.0 | True |
| Jogging | 10 | 0.535945-0.806519% | 99.907031% | 99.888116% | 100.0% | 0.989380 | 0.984624 | 0.0 | True |

```text
ALL FRAME-2 REGRESSIONS PASS: True
checkpoint pose-robust passes: 3 / 3
global minimum K6 reduction: 99.81874059431833%
global minimum ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral: 0.0
ALL THREE CHECKPOINTS ELBOW POSE ROBUST: True
```

Seattle frame-2 learned displacement differs from Step 17B1 by only `2.86102294921875e-06`, inside the frozen `1e-5` regression tolerance. Parkinglot and Jogging regress essentially exactly.

Current strongest bounded result: the same learned cross-joint LBS causal mechanism is demonstrated for **two tested joints, left wrist and left elbow, across three independently pretrained checkpoints**, with full predeclared pose robustness nested within each checkpoint.

Do not describe this as six independent replications. Joints are repeated diagnostics within the same three independently pretrained checkpoints.

## Immediate next action

Do **not** start a third joint yet.

First run a two-joint freeze/synthesis step that combines the already-frozen wrist benchmark and completed elbow benchmark into a single cross-joint, cross-checkpoint record without pooling raw displacement magnitudes or treating joint/frame observations as independent model replications.

## Continuity files

- `research/sessions/2026-09-15-step17b2.md`
- `experiments/08-second-joint-generalization/analysis/17B2_left_elbow_checkpoint_summary.csv`
- `research/methodology/assumption-failure-ledger.md`
- `research/sessions/2026-09-15-step17b1c.md`
- `experiments/08-second-joint-generalization/analysis/17B1C_packaged_config_label_drift_audit.json`
- `research/sessions/2026-09-15-step17b1b-assumption-failure.md`
- `research/sessions/2026-09-15-step17b1a.md`
- `experiments/08-second-joint-generalization/analysis/17B1A_exact_hugs_source_semantics_audit.json`
- `research/protocols/2026-09-15-second-joint-generalization.md`
- `research/protocols/2026-09-15-second-joint-generalization-implementation-note.md`
