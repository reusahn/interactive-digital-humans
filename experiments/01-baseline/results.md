# Experiment 01 Results

_Status: implementation ready, measurements not yet run._

This file intentionally contains no fabricated benchmark values. Results are added only after running the probe on an actual HUGS checkpoint.

## Baseline verification

| Item | Value |
| --- | --- |
| HUGS commit | pending |
| GPU | pending |
| CUDA | pending |
| PyTorch | pending |
| NeuMan sequence | pending |
| Human checkpoint | pending |
| PSNR | pending |
| SSIM | pending |
| LPIPS | pending |
| Rendering FPS | pending |

## Locality sweep

The first sweep should cover multiple frames, joints, axes, and perturbation magnitudes. Do not report only the best or cleanest examples.

| Frame | Joint | Axis | Degrees | Target change | Outside change | Leakage ratio | Outside active fraction |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| pending | pending | pending | pending | pending | pending | pending | pending |

## Semantic assignment diagnostics

Record:

- number of Gaussians assigned to each coarse region,
- mean dominant-joint confidence,
- low-confidence boundary regions,
- visible failure cases around loose clothing, hair, hands, and joint boundaries.

## Interpretation

We will distinguish three outcomes.

### Outcome A — Locality is already robust

If HUGS remains semantically local across poses and body regions, the representation-side hypothesis is weakened. Project 001 should move toward contact dynamics, behavior generation, or social interaction instead of inventing a semantic representation layer unnecessarily.

### Outcome B — Locality fails mainly at semantic boundaries

If leakage concentrates near wrists, shoulders, garment boundaries, or other articulation boundaries, the next hypothesis is a topology/anchor-aware boundary model rather than a wholesale new avatar representation.

### Outcome C — Locality degrades broadly under novel articulation

If unrelated regions move substantially or semantic attachment becomes unstable across pose changes, a more structured interaction-ready representation becomes justified.

## Statistical reporting plan

For the baseline probe, report distributions rather than a single mean:

- median and interquartile range of leakage ratio,
- per-joint distributions,
- leakage versus perturbation angle,
- leakage versus semantic-assignment confidence,
- representative best, median, and worst cases.

No significance test is preselected until a competing method exists. Once a proposed method is implemented, compare baseline and proposed method on matched frames/perturbations with paired statistics and effect sizes.
