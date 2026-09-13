# Experiment 01 Environment

## Baseline

HUGS: Human Gaussian Splats, CVPR 2024.

Official repository:
https://github.com/apple-aiml-research/ml-hugs

The upstream README reports testing on Ubuntu 22.04.3 with a CUDA 11.7-compatible GPU. Treat that as the reference environment rather than assuming newer CUDA/PyTorch combinations are equivalent.

## Recommended directory layout

Keep the upstream baseline outside this repository so its license, history, and submodules remain intact.

```text
workspace/
├── interactive-digital-humans/
└── ml-hugs/
```

Clone HUGS with its submodules:

```bash
git clone --recursive https://github.com/apple-aiml-research/ml-hugs.git
cd ml-hugs
source scripts/conda_setup.sh
```

Follow the upstream instructions to obtain the SMPL model, NeuMan data, and HUGS pretrained models. Do not commit those licensed assets or checkpoints into this repository.

## Verify the upstream baseline first

From the HUGS repository:

```bash
python scripts/evaluate.py -o /path/to/HUGS_OUTPUT_DIR
```

The upstream evaluation reports PSNR, SSIM, and LPIPS and also exercises the pretrained human model before we add any probe code.

## Run our first locality probe

Activate the same HUGS conda environment, then run from this experiment directory:

```bash
cd /path/to/interactive-digital-humans/experiments/01-baseline
python hugs_locality_probe.py \
  --hugs-root /path/to/ml-hugs \
  --output-dir /path/to/HUGS_OUTPUT_DIR \
  --frame 0 \
  --joint left_wrist \
  --axis z \
  --degrees 10 \
  --save-dir probe_results
```

Expected outputs:

```text
probe_results/
├── semantic_assignment.json
├── frame000_left_wrist_z_10deg.json
└── frame000_left_wrist_z_10deg.npz
```

The JSON records the geometric locality metrics. The NPZ stores canonical and posed Gaussian positions plus semantic assignments so we can make figures without rerunning the model.

## Minimum sweep

Do not interpret a single perturbation as a result. Run at least:

```text
joints:   left_wrist, right_wrist, head, left_elbow, right_elbow
axes:     x, y, z
angles:   5°, 10°, 20°
frames:   >= 10 validation poses distributed through the sequence
```

For each run record:

- target change,
- outside change,
- leakage ratio,
- active fraction inside/outside the target region,
- semantic-assignment confidence.

## Important interpretation rule

A low leakage ratio is not automatically good. A system that barely moves anything can also have low leakage. Report locality together with target displacement or target error.

The first decision gate is whether locality degrades systematically under novel articulation or at semantic boundaries. If it does not, this research hypothesis should be weakened or abandoned rather than forcing a new representation.
