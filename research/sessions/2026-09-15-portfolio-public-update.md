# Public Portfolio Update — 2026-09-15

## Target

Updated the portfolio previously submitted for Netflix Video Algorithms Intern, Video Coding (Gaussian Splatting), Fall 2026, JR40251.

Live portfolio URL:

`https://jonghoonahn.com/Video_Algorithms.html`

Portfolio repository:

`reusahn/Portfolio`

## Changes made

Updated `Video_Algorithms.html` so the research narrative now has five stages:

1. Representation
2. Training
3. Delivery
4. Execution
5. Control

Added a new fifth research stage, **4D Human Deformation Locality**, describing the completed HUGS deformation-locality benchmark.

Added dedicated detail page:

`Projects29/human-deformation-locality.html`

## Public metrics disclosed

- 3 independently pretrained HUGS NeuMan checkpoints
- 2 tested joints: left wrist and predeclared left elbow
- 36 nested pose diagnostics
- 6/6 joint × checkpoint diagnostic cells passed
- global minimum K6 reduction: 99.708575%
- selective learned-branch ablation: 100% reduction of tested contralateral response in every nested pose diagnostic
- global minimum removed-mass / displacement-reduction correlation: 0.968898
- maximum ablated contralateral displacement: 0.0

## Statistical wording preserved

The portfolio explicitly states that the independent model-level unit is checkpoint, `n=3`. The two joints and 36 pose diagnostics are repeated/nested diagnostics and are not presented as independent replications.

## Failure-aware research process disclosed

The detail page also publicly notes selected corrected assumptions and implementation failures, including:

- Seattle mask-threshold hypothesis disproved
- `hugs_triplane -> HUGS_TRIMLP` alias hypothesis disproved
- earlier locality-target correction
- Step 17B2 truncated-cell syntax failure logged separately from scientific results

## Information intentionally not disclosed

No future novel locality-preserving correction method, loss, architecture, or unpublished intervention design was disclosed. The public portfolio contains only the validated diagnostic result on existing HUGS behavior and the reproducibility/failure-aware research process.

## Portfolio commits

- new detail page commit: `b25d22d07c7d6f50c6c36f4953a14c7cca62ba2c`
- updated Video Algorithms portfolio commit: `e0f4fb7ceab6d02b134196041f17daa486d4d399`

GitHub Pages may require a short deployment/cache interval before the live custom-domain page reflects the commit.
