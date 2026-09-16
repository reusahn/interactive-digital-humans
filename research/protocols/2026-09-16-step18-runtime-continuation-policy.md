# Step 18 Runtime Continuation Policy — Frozen before shoulder causal displacement

Date metadata: 2026-09-16

## Why this policy exists

The frozen Step-17B1 elbow archive cannot be reproduced within the historical aggregate `1e-5` gate on the currently tested runtimes despite near-perfect per-Gaussian spatial agreement.

The following have been ruled out as primary causes: canonical-source mismatch, archive instability, manual-vs-SMPLX transform semantics, HUGS tensor rank, chunking, displacement norm placement, TF32, CPU-vs-CUDA alone, official legacy software stack alone, and GPU architecture alone across tested A100/T4 runs.

Under the same legacy software stack, the remaining Parkinglot learned aggregate error changes sign/magnitude between A100 and T4 while field Pearson remains effectively `1.0`. This is treated as historical low-level floating-point runtime sensitivity, not as disappearance of the causal deformation field.

## Historical gate status

The original elbow exact-reproduction gate remains unchanged:

`abs(candidate contralateral sum - archived contralateral sum) <= 1e-5`

It is **not widened**.

Status on available runtimes: **FAILED for exact 6/6 recovery**.

This historical regression gate is retained as a provenance criterion and is not reused as a post-hoc tunable scientific threshold.

## Primary Step-18 execution runtime

Frozen before shoulder causal displacement inspection:

- GPU: Tesla T4
- Python: 3.8.20
- PyTorch: 1.13.1+cu117
- CUDA build: 11.7
- NumPy: 1.24.4
- SMPLX: 0.1.28
- TF32: disabled
- released HUGS source semantics
- float32 deformation path

Reason for choosing this runtime: it is the currently active second-hardware environment and uses the source-declared HUGS legacy software stack. This is a reproducibility choice, **not** a claim that historical Step 17 used T4.

## Scientific protocol remains unchanged

The already-frozen third-joint protocol remains exactly:

- joint: left shoulder, SMPL 16
- perturbation: local z +10 degrees
- descendant branch: `[16,18,20,22]`
- expected changed transforms: `[16,18,20,22]`
- contralateral dominant-joint subset: `{14,17,19,21,23}`
- Seattle frames: `[2,7,12,17]`
- Parkinglot frames: `[2,7,12,17]`
- Jogging frames: `[2,7,12,17,22,27,32,37,42,47]`
- K6 contralateral reduction: `>=95%`
- selective-ablation reduction: `>=99.999%`
- maximum/summed ablated contralateral response: `<=1e-8`
- removed-mass/displacement-reduction Pearson correlation: `>=0.90`

No threshold, mask, joint, axis, angle, branch, or pose schedule may be changed after shoulder output is inspected.

## Runtime-sensitivity rule for Step 18

1. Run the primary shoulder experiment completely on the frozen T4 legacy runtime.
2. Do not tune anything based on the result.
3. If the primary protocol passes, later rerun the shoulder pass/fail metrics on a second declared CUDA runtime, preferably A100 + the same legacy software stack, as a numerical sensitivity check.
4. A scientific conclusion is considered runtime-robust only if the threshold-level conclusions are unchanged across the declared runtimes.
5. Exact per-Gaussian bitwise equality across GPU architectures is not required and is not claimed.

## Reporting language

Allowed:

- "The historical Step-17 archive showed runtime-sensitive float32 aggregate differences across modern/legacy CPU/CUDA and A100/T4 environments while preserving essentially identical spatial deformation fields."
- "Step 18 was therefore executed under a predeclared fixed runtime and later checked for threshold-level robustness on a second runtime."

Not allowed:

- claiming the historical Step-17 GPU was T4
- claiming exact historical numerical reproduction was achieved
- silently widening the frozen `1e-5` gate
- tuning shoulder thresholds after observing shoulder output
