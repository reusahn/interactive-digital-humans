# Research Session Checkpoint — 2026-09-16 Step 18B1G0

## Purpose

Switch the regression audit from the CPU-only Colab runtime to a real CUDA runtime without yet computing any shoulder result.

## Runtime

- Python: `3.13.15`
- PyTorch: `2.11.0+cu128`
- CUDA build: `12.8`
- CUDA available: `True`
- GPU: `NVIDIA A100-SXM4-40GB`
- compute capability: `8.0`
- GPU memory: approximately `39.49 GiB`
- NumPy: `2.1.3`
- SMPLX: `0.1.28`

All required persistent assets passed existence checks: clean SMPL, frozen Step-17 B1/B2 arrays, frozen anatomy masks, all three NeuMan pose files, and all three pretrained HUGS checkpoints.

The frozen Step-17B1 learned/K6/ablated arrays were finite float32 arrays with the expected Gaussian counts for Seattle, Parkinglot, and Jogging.

## Interpretation

CUDA execution is now available for a direct elbow regression audit. This does not establish that Step 17 historically ran on CUDA. No elbow causal result was recomputed in this bootstrap and no shoulder computation or tolerance change occurred.

## Next action

Run the source-equivalent elbow frame-2 regression on CUDA and compare directly against the archived Step-17B1 arrays before any shoulder computation.