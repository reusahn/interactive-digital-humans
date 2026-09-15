# Latest Research Handoff

Current continuation date: **2026-09-15**.

## Research-record rule

Preserve failed assumptions, disproven hypotheses, implementation misunderstandings, and code-delivery failures rather than rewriting history after correction.

Cumulative ledger:

`research/methodology/assumption-failure-ledger.md`

Structured chat continuity:

`research/sessions/2026-09-15-chat-continuity.md`

Recent recorded failures/corrections include Seattle validation-frame mapping, ankle locality-target interpretation, the disproved Seattle threshold-comparator hypothesis, the disproved `hugs_triplane -> HUGS_TRIMLP` alias assumption, and the Step 17B2 truncated-cell syntax failure followed by a successful rerun.

## Frozen left-wrist benchmark

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

## Frozen left-elbow generalization

Predeclared before elbow displacement was inspected:

- left_elbow, SMPL 18
- z +10 degrees
- branch channels `[18,20,22]`
- expected changed transforms `[18,20,22]`
- Seattle poses `[2,7,12,17]`
- Parkinglot poses `[2,7,12,17]`
- Jogging poses `[2,7,12,17,22,27,32,37,42,47]`

Canonical anatomy sources were frozen before perturbation:

```text
Seattle    saved_dominant + saved_confidence    HC 197778  contra 33072
Parkinglot dominant_joint + joint_confidence    HC 292095  contra 77622
Jogging    dominant_joint + joint_confidence    HC 148392  contra 20887
```

All 18 predeclared elbow pose diagnostics passed:

```text
ALL FRAME-2 REGRESSIONS PASS: True
checkpoint pose-robust passes: 3 / 3
global minimum K6 reduction: 99.81874059431833%
global minimum ablation reduction: 100.0%
global minimum removed-mass correlation: 0.9688984153761956
global maximum ablated contralateral: 0.0
ALL THREE CHECKPOINTS ELBOW POSE ROBUST: True
```

## Source/provenance status

Exact HUGS source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Step 17B1A established exact released HUGS_TRIMLP reconstruction semantics and zero numerical difference from stored learned-LBS arrays across Seattle, Parkinglot, and Jogging.

Step 17B1B disproved the assumption that an executable `hugs_triplane -> HUGS_TRIMLP` alias exists.

Step 17B1C established:

- released source/config name: `hugs_trimlp`
- released trainer directly constructs `HUGS_TRIMLP`
- downloaded pretrained package configs contain `hugs_triplane`
- released commit contains no executable `hugs_triplane` alias
- historical cause of the naming mismatch is unknown
- exact numeric reconstruction means no reconstruction rerun is required

## Step 17C0 — frozen two-joint benchmark

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

## Public Netflix portfolio update completed

The portfolio previously submitted for Netflix Video Algorithms Intern, Video Coding (Gaussian Splatting), Fall 2026, JR40251 has been updated.

Live URL:

`https://jonghoonahn.com/Video_Algorithms.html`

Portfolio repository:

`reusahn/Portfolio`

Changes:

- updated `Video_Algorithms.html` from four to five research stages: Representation → Training → Delivery → Execution → Control
- added 4D Human Deformation Locality to hero metrics, research journey, results table, technical scope, and About section
- created `Projects29/human-deformation-locality.html`
- public page includes 3 checkpoints, 2 tested joints, 36 nested pose diagnostics, 6/6 joint × checkpoint cells passed, minimum K6 reduction 99.7086%, 100% selective-ablation reduction, minimum correlation 0.9689
- public wording explicitly preserves checkpoint `n=3` as the independent model-level unit
- selected failed assumptions/corrections are included as evidence of failure-aware research practice
- no future novel locality-preserving method/loss/architecture was disclosed

Portfolio commits:

- detail page: `b25d22d07c7d6f50c6c36f4953a14c7cca62ba2c`
- main submitted portfolio: `e0f4fb7ceab6d02b134196041f17daa486d4d399`

Disclosure record:

`research/sessions/2026-09-15-portfolio-public-update.md`

GitHub Pages/custom-domain deployment may lag the repository commit briefly.

## End-of-day decision

The planned research block is complete at Step 17C0.

Do **not** automatically start a third joint today. Next research session should decide whether another joint adds meaningful evidence or whether the project should transition into locality-preserving method/loss design.

## Continuity files

- `research/sessions/2026-09-15-chat-continuity.md`
- `research/sessions/2026-09-15-step17c0.md`
- `research/sessions/2026-09-15-portfolio-public-update.md`
- `experiments/08-second-joint-generalization/analysis/17C0_two_joint_cross_checkpoint_benchmark.csv`
- `experiments/08-second-joint-generalization/analysis/17C0_two_joint_cross_checkpoint_benchmark.json`
- `research/methodology/assumption-failure-ledger.md`
