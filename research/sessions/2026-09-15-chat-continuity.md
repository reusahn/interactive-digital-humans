# Chat Continuity Record — 2026-09-15

## Why this file exists

This is a structured continuity record of the research conversation, not a raw transcript. It preserves the decisions, corrections, failed assumptions, result interpretation, and exact continuation state so later sessions do not lose the reasoning path.

The user explicitly requested that chat-derived research context be preserved alongside code/results, including assumptions that later proved wrong.

## Interaction protocol used in this session

1. Provide one next Colab cell.
2. User runs it and returns the full output.
3. Diagnose that exact output.
4. Archive meaningful results to GitHub.
5. Only then provide the next cell.

Raw large arrays stay on Drive. Compact CSV/JSON/Markdown records are mirrored to GitHub.

## Research state entering the elbow-generalization phase

The left-wrist locality result had already been established across Seattle, Parkinglot, and Jogging HUGS NeuMan checkpoints. The central bounded mechanism was that small learned cross-joint wrist/hand LBS components on anatomically contralateral Gaussians causally mediated a much larger contralateral response than the subject-specific SMPL-derived K6 target.

The left-wrist benchmark was frozen at Step 16E0:

- independent checkpoint unit: n=3
- nested wrist pose diagnostics: 18
- 3/3 checkpoint passes
- global minimum K6 reduction: 99.708575087815%
- selective ablation reduction: 100%
- global minimum removed-mass correlation: 0.9808287038512752
- max ablated contralateral displacement: 0.0

## Second-joint generalization plan

Before inspecting elbow displacement results, the following protocol was frozen:

- joint: left_elbow, SMPL joint 18
- axis: z
- perturbation: +10 degrees
- perturbed branch channels: [18,20,22]
- expected changed transforms: [18,20,22]
- contralateral anatomy: [14,17,19,21,23]
- confidence threshold: >=0.9
- Seattle poses: [2,7,12,17]
- Parkinglot poses: [2,7,12,17]
- Jogging poses: [2,7,12,17,22,27,32,37,42,47]
- K6 reduction threshold: >=95%
- selective-ablation reduction threshold: >=99.999%
- removed-mass/reduction correlation threshold: >=0.90
- max ablated contra: <=1e-8

Failures were explicitly designated as results. No joint, threshold, mask, angle, or pose schedule was to be changed in response to outcome.

## Step 17A / 17A1 / 17A2: precursor and anatomy-source correction

Step 17A found learned left-elbow-branch support on the fixed contralateral subset was much larger than K6 in all three checkpoints.

A small Seattle mask-count discrepancy then appeared:

- recomputed from effective_lbs: HC 197781, contra 33074
- frozen historical benchmark: HC 197778, contra 33072

An initial hypothesis was that this came from `>=0.9` versus `>0.9`. Step 17A1 disproved that. There were no exact 0.9 boundary values. The actual difference was the anatomy source:

- historical Seattle benchmark used `saved_dominant + saved_confidence`
- recomputation used `argmax/max(effective_lbs)`

Step 17A2 froze canonical anatomy sources before any elbow causal perturbation:

- Seattle: saved_dominant + saved_confidence
- Parkinglot: dominant_joint + joint_confidence
- Jogging: dominant_joint + joint_confidence
- K6 deformation weights remain effective_lbs

Counts frozen:

- Seattle HC 197778, contra 33072
- Parkinglot HC 292095, contra 77622
- Jogging HC 148392, contra 20887

The Seattle precursor changed negligibly under the corrected mask source and remained learned > K6.

## Step 17B1: elbow causal test at raw frame 2

The predeclared left-elbow z +10 degree perturbation passed in all three checkpoints.

Changed transforms were exactly [18,20,22] in Seattle, Parkinglot, and Jogging.

Frame-2 causal results:

- Seattle: learned contra 2.6505639553, K6 contra 0.0048044017, ablated 0.0, K6 reduction 99.8187404%, correlation 0.9708237
- Parkinglot: learned contra 11.0941810608, K6 contra 0.0116030509, ablated 0.0, K6 reduction 99.8954132%, correlation 0.9958911
- Jogging: learned contra 1.2263532877, K6 contra 0.0009509723, ablated 0.0, K6 reduction 99.9224553%, correlation 0.9863545

Interpretation at this point was intentionally limited to one common tested base pose per checkpoint.

## Source-semantics audit and failed alias assumption

A foundational audit was then completed because pretrained configs contained `human.activation: relu` while earlier reconstruction instantiated decoder modules without explicitly passing activation.

Step 17B1A inspected exact HUGS source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Findings:

- located released implementation: `hugs/models/hugs_trimlp.py`, class `HUGS_TRIMLP`
- GeometryDecoder and DeformationDecoder default to GELU
- HUGS_TRIMLP does not pass the packaged config activation into those decoder constructors
- softmax temperature is 0.1
- canonical xyz uses checkpoint xyz + geometry xyz offset
- transform composition is `A_t2pose @ inv_A_t2vitruvian`
- `disable_posedirs=True` semantics were confirmed
- stored learned-LBS arrays numerically matched exact reconstruction with difference 0.0 for Seattle, Parkinglot, and Jogging
- stored canonical xyz matched exactly where present

Step 17B1B then tested an assumption that packaged `hugs_triplane` must be an alias for `HUGS_TRIMLP`. That assumption was wrong. Exact source contained zero `hugs_triplane` Python-source hits.

Step 17B1C resolved the provenance correctly:

- released config name: `hugs_trimlp`
- released trainer directly constructs HUGS_TRIMLP
- downloaded pretrained package configs use `hugs_triplane`
- no executable `hugs_triplane` alias exists in the released commit
- historical reason for the naming mismatch is unknown
- exact numeric reconstruction shows no rerun is required

Important conversation rule added here: failed assumptions should remain visible in the research record and should not be silently overwritten by the later correct explanation.

## Step 17B2: full elbow pose robustness

The first Step 17B2 cell failed before execution because the transferred code was truncated, producing an unterminated string SyntaxError. This was recorded as an implementation/delivery failure, not a scientific failure.

A shorter self-contained replacement cell was then run successfully.

All 18 predeclared elbow pose diagnostics passed:

- Seattle: 4/4
- Parkinglot: 4/4
- Jogging: 10/10

Global elbow robustness:

- minimum K6 reduction: 99.81874059431833%
- minimum selective-ablation reduction: 100%
- minimum removed-mass correlation: 0.9688984153761956
- maximum ablated contralateral displacement: 0.0

Frame-2 regressions back to Step 17B1 passed in all three checkpoints.

## Step 17C0: two-joint benchmark freeze

The user then ran the two-joint synthesis. It passed completely.

Frozen result:

- independent pretrained checkpoints: 3
- tested joints: 2
- nested pose diagnostics: 36
- joint x checkpoint diagnostic cells passing: 6/6
- checkpoints where both joints pass: 3/3
- global minimum K6 reduction: 99.708575087815%
- global minimum selective-ablation reduction: 100%
- global minimum removed-mass correlation: 0.9688984153761956
- global maximum ablated contralateral displacement: 0.0
- TWO-JOINT CROSS-CHECKPOINT BENCHMARK FROZEN: True

Strongest bounded current claim:

Across three independently pretrained HUGS NeuMan checkpoints, the same learned cross-joint LBS causal mechanism is demonstrated for two tested joints, left wrist and the predeclared left elbow, with robust behavior across all tested base poses. The two joints are repeated diagnostics within the same three pretrained models, and the 36 pose diagnostics are nested robustness tests rather than independent replications.

## Statistical and wording guardrails

Do not say:

- 6 independent replications
- n=36 independent samples
- raw displacement magnitudes are directly pooled across sequences
- the package/source naming difference has a known historical cause
- an executable hugs_triplane alias exists

Safe wording:

- 3 independently pretrained checkpoints
- 2 tested joints
- 36 nested pose diagnostics
- 6/6 joint × checkpoint diagnostic cells passed
- full predeclared pose robustness within each checkpoint

## Public portfolio decision

The user requested that this completed research be added to the portfolio submitted for Netflix Video Algorithms Intern, Video Coding (Gaussian Splatting), Fall 2026, JR40251.

Submitted portfolio URL:

`https://jonghoonahn.com/Video_Algorithms.html`

Repository file:

`reusahn/Portfolio/Video_Algorithms.html`

Public disclosure should include the validated diagnostic result and research process, but not expose any future novel locality-preserving method/loss/architecture before a publication/IP decision.

Recommended portfolio framing:

- new 4D human / deformation-locality research stage after representation, training, delivery, and execution
- diagnose controllability and deformation locality in learned Gaussian human representations
- three independently pretrained HUGS checkpoints
- two tested joints
- 36 nested pose diagnostics
- minimum K6 reduction 99.7086%
- selective branch ablation removes 100% of tested contralateral response
- minimum removed-mass correlation 0.9689
- explicit note that checkpoint n=3 is the independent model unit
- link to public `reusahn/interactive-digital-humans` repository

## End-of-day state

The planned research block for the day is complete at Step 17C0. Do not automatically start a third joint. Next session should first decide whether another joint adds meaningful evidence or whether the project should transition into novel locality-preserving method/loss design.

## Related records

- `research/methodology/assumption-failure-ledger.md`
- `research/sessions/2026-09-15-step17c0.md`
- `experiments/08-second-joint-generalization/analysis/17C0_two_joint_cross_checkpoint_benchmark.csv`
- `experiments/08-second-joint-generalization/analysis/17C0_two_joint_cross_checkpoint_benchmark.json`
- `research/sessions/2026-09-15-step17b2.md`
- `research/sessions/2026-09-15-step17b1c.md`
- `research/sessions/2026-09-15-step17b1b-assumption-failure.md`
