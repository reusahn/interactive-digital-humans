# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Research-record rule

Preserve failed assumptions, disproven hypotheses, implementation misunderstandings, and code-delivery failures rather than rewriting history after correction.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`

Structured chat continuity:

`research/sessions/2026-09-15-chat-continuity.md`

Recent recorded failures/corrections include:

- Seattle validation-frame mapping correction
- ankle locality-target correction
- Seattle `>=0.9` vs `>0.9` hypothesis disproved
- nonexistent `hugs_triplane -> HUGS_TRIMLP` alias assumption disproved
- Step 17B2 truncated-cell syntax failure, followed by successful rerun

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

## Predeclared left-elbow generalization

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

Canonical anatomy sources were frozen before causal testing:

```text
Seattle    saved_dominant + saved_confidence    HC 197778  contra 33072
Parkinglot dominant_joint + joint_confidence    HC 292095  contra 77622
Jogging    dominant_joint + joint_confidence    HC 148392  contra 20887
```

## Source/provenance status

Exact HUGS source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Step 17B1A established exact released HUGS_TRIMLP reconstruction semantics and zero numerical difference from stored learned-LBS arrays across Seattle, Parkinglot, and Jogging.

Step 17B1B disproved the assumption that an executable `hugs_triplane -> HUGS_TRIMLP` alias exists.

Step 17B1C established the correct provenance statement:

- released source/config name: `hugs_trimlp`
- released trainer directly constructs `HUGS_TRIMLP`
- downloaded pretrained package configs contain `hugs_triplane`
- released commit contains no executable `hugs_triplane` alias
- historical cause of the naming mismatch is unknown
- exact numeric reconstruction means no reconstruction rerun is required

## Frozen left-elbow pose-robust result

All 18 predeclared elbow pose diagnostics passed.

```text
ALL FRAME-2 REGRESSIONS PASS: True
checkpoint pose-robust passes: 3 / 3
global minimum K6 reduction: 99.81874059431833%
global minimum ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral: 0.0
ALL THREE CHECKPOINTS ELBOW POSE ROBUST: True
```

## Step 17C0 — frozen two-joint cross-checkpoint benchmark

The completed wrist and elbow results were synthesized without changing any endpoint or perturbation.

```text
independent pretrained checkpoints: 3
tested joints: 2
nested pose diagnostics: 36
joint x checkpoint diagnostic cells passing: 6 / 6
checkpoints where both joints pass: 3 / 3
global minimum K6 reduction: 99.708575087815%
global minimum selective-ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral: 0.0
TWO-JOINT CROSS-CHECKPOINT BENCHMARK FROZEN: True
```

### Current strongest bounded result

Across three independently pretrained HUGS NeuMan checkpoints, the same learned cross-joint LBS causal mechanism is demonstrated for two tested joints, left wrist and the predeclared left elbow, with robust behavior across all tested base poses. Replacing learned deformation weights with the subject-specific SMPL-derived K6 target removes at least 99.708575% of the tested contralateral response, while selective ablation of the learned perturbed-branch components eliminates the tested contralateral response under all 36 nested pose diagnostics.

### Statistical guardrails

- Independent model-level unit is checkpoint, `n=3`.
- Two joints are repeated diagnostics within the same checkpoints, not six independent models.
- Thirty-six pose tests are nested robustness diagnostics, not 36 independent replications.
- Raw displacement magnitudes are sequence-scale dependent and are not pooled.

## Public portfolio action

Add the completed diagnostic result to the portfolio submitted for Netflix Video Algorithms Intern, Video Coding (Gaussian Splatting), Fall 2026, JR40251:

`https://jonghoonahn.com/Video_Algorithms.html`

Repository file:

`reusahn/Portfolio/Video_Algorithms.html`

Public wording may report the validated HUGS / 4D-human deformation-locality benchmark and link to the public `interactive-digital-humans` repository. Do not disclose any future novel locality-preserving method/loss/architecture before publication/IP decisions.

## End-of-day decision

The planned research block is complete at Step 17C0.

Do **not** automatically start a third joint today. Next research session should decide whether another joint adds meaningful evidence or whether the evidence is sufficient to move into locality-preserving method/loss design.

## Continuity files

- `research/sessions/2026-09-15-chat-continuity.md`
- `research/sessions/2026-09-15-step17c0.md`
- `experiments/08-second-joint-generalization/analysis/17C0_two_joint_cross_checkpoint_benchmark.csv`
- `experiments/08-second-joint-generalization/analysis/17C0_two_joint_cross_checkpoint_benchmark.json`
- `research/methodology/assumption-failure-ledger.md`
- `research/sessions/2026-09-15-step17b2.md`
- `research/sessions/2026-09-15-step17b1c.md`
- `research/sessions/2026-09-15-step17b1b-assumption-failure.md`
