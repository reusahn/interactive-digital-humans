# Research Session Checkpoint - 2026-09-15 Step 16C1 Numerical Audit

## Context

Parkinglot checkpoint provenance and architecture were already validated. The official HUGS source at `/content/ml-hugs` was restored at commit `86ebe5522a384fc553f07f090b63a76dd4af8d33`, and a lightweight loader successfully imported only `activation.py`, `triplane.py`, and `decoders.py` without the renderer stack.

## Step 16C1 first reconstruction attempt

The official Parkinglot checkpoint strict-loaded successfully into the reconstructed `TriPlane`, `GeometryDecoder`, and `DeformationDecoder` modules.

Checkpoint Gaussian count:

```text
614,157
```

Chunked canonical forward completed over all Gaussians using chunk size 65,536.

Core numerical checks were healthy:

```text
xyz_canon shape: (614157, 3)
learned_lbs shape: (614157, 24)
xyz NaN: 0
LBS NaN: 0
xyz Inf: 0
LBS Inf: 0
max LBS row-sum error: 3.5762786865234375e-07
mean LBS row-sum error: 5.003608194442677e-08
min learned weight: 2.385790847616443e-23
max learned weight: 0.9999994039535522
```

Canonical geometry ranges:

```text
x: -0.8510141373 to 0.8847273588
y: -0.7996198535 to 0.5584751368
z: -0.2463577390 to 0.2806299329
```

Geometry-offset norm quantiles:

```text
min:    0.0004350696
median: 0.0382876620
p90:    0.0682295099
p99:    0.1231123710
max:    0.3769477308
```

The only failed validation criterion was a deliberately strict chunk-reproducibility test. The first 4,096 Gaussians were rerun as a different CUDA batch size and compared with their values from the 65,536-sized chunked pass:

```text
canonical XYZ max difference: 5.960464477539063e-08
learned LBS max difference:   3.904104232788086e-06
```

The validation threshold had required learned-LBS max difference below `1e-7`, so `FORWARD VALID` returned `False` and the raw NPZ was intentionally not saved. The compact manifest was saved in Drive.

## Diagnosis

This is currently treated as a numerical-reproducibility audit issue, not evidence of an incorrect checkpoint reconstruction. All state dicts strict-loaded, all outputs are finite, and LBS rows sum to one to float32 precision. The discrepancy appears only when comparing forward passes using different CUDA batch shapes. The HUGS deformation logits are subsequently passed through `softmax(logits / 0.1)`, which can amplify small floating-point differences.

Importantly, the actual HUGS `canon_forward()` processes the full Gaussian tensor in one call rather than in 65,536-point chunks. Therefore the next validation should use a full-batch Parkinglot canonical forward, if GPU memory permits, as the authoritative reconstruction and compare that output against the chunked approximation.

## Exact next action

Run Step 16C1B only:

1. execute the Parkinglot canonical forward on all 614,157 Gaussians in one batch, matching the HUGS call shape,
2. compare full-batch and prior chunked canonical xyz and learned LBS,
3. report absolute-error quantiles, per-row L1 differences, dominant-joint agreement, and confidence-mask agreement,
4. if the full-batch forward is finite with valid row sums, save the full-batch outputs as authoritative,
5. do not construct the Parkinglot K=6 target until this audit is reviewed.
