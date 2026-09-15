# Latest Research Handoff

Current continuation document:

- [2026-09-15](2026-09-15.md)

Completed today:

- Step 14 corrected Seattle counterfactual LBS ablation
- Step 15 Seattle within-sequence frame replication
- Step 16A cross-sequence asset inventory
- Step 16B1 official NeuMan archive range probe
- Step 16B2 selective extraction of candidate NeuMan pose assets
- Step 16B3 Parkinglot checkpoint/config provenance validation
- Step 16C0 / 16C0B HUGS source restoration and lightweight module loading
- Step 16C1 / 16C1B Parkinglot learned-LBS forward reconstruction and numerical audit
- Step 16C2 Parkinglot-specific SMPL K=6 target reconstruction
- Step 16C3 Parkinglot independent causal counterfactual
- Step 16C4 Parkinglot within-checkpoint pose replication
- Step 16C5 Parkinglot axis/sign robustness control
- Step 16D1 Jogging checkpoint/config provenance and architecture validation

## Current strongest result

The learned cross-joint left-wrist/left-hand LBS mechanism has been causally reproduced and shown to be pose-stable in **two independently pretrained HUGS NeuMan checkpoints: Seattle and Parkinglot**.

Seattle raw frames `[2,7,12,17]`, `left_wrist z +10 deg`:

```text
mean K6 reduction:             99.8184408838516%
minimum K6 reduction:          99.81753724223914%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9811488931072522
```

Parkinglot raw frames `[2,7,12,17]`, same perturbation:

```text
learned contra % HC range:     3.3925969009792323 to 3.3971048755337407
mean K6 reduction:             99.70879580221536%
minimum K6 reduction:          99.70857508781499%
mean selective reduction:      100.0%
mean removed-mass correlation: 0.9975337157455157
```

Parkinglot raw frame 2 additionally passed `x/y/z × {-10,+10} deg` direction/sign control:

```text
minimum K6 reduction:                 98.7997086031298%
minimum selective-ablation reduction: 100.0%
minimum removed-mass correlation:     0.9664424743486758
maximum ablated contralateral sum:    0.0
maximum +/- sign asymmetry:           0.5583232093225667%
AXIS/SIGN ROBUST:                     True
```

Important nuance: the causal pathway is direction robust, but effect magnitude is anisotropic. The x-axis response is much smaller than y/z. Do not claim axis-invariant magnitude.

## Step 16D1 - third candidate readiness

Third independent candidate: **Jogging**.

Official checkpoint/config and pose asset were verified:

```text
Jogging checkpoint SHA256: 7a056fd6ba8ee9f5cc640eac43666e9ab57de33db2062a8ca379d1daa3afa769
Jogging config SHA256:     7e854af5d7d0dd564f863de4aca2465b8268c1eb3c3b06a0618c66cea8a25e53
Gaussian count:            311723
pose frames:               102
beta drift:                0.0
eval raw frames:           [2,7,12,17,22,27,32,37,42,47]
```

The Jogging checkpoint is distinct from Parkinglot. Triplane, geometry-decoder, and deformation-decoder tensor signatures match Parkinglot exactly. Packaged architecture-related config fields also match, including `hugs_triplane`, `use_deformer=True`, `disable_posedirs=True`, `n_subdivision=2`, and `triplane_res=256`.

```text
independent checkpoint: True
core architecture match: True
config identity valid: True
pose asset valid: True
THIRD CHECKPOINT READY: True
```

Do **not** count Jogging as a third replication yet. No Jogging learned-LBS or causal result exists at this point.

## Strongest defensible claim

> In two independently pretrained HUGS NeuMan checkpoints, Seattle and Parkinglot, small learned cross-joint left-wrist/hand LBS components causally mediate an amplified contralateral upper-body displacement relative to the corresponding SMPL-derived K=6 target. The mechanism remains stable across four tested evaluation poses in each checkpoint, and in Parkinglot it persists across x/y/z wrist rotations and both perturbation signs.

Do not describe this as a universal HUGS failure, an isotropic effect, or a result generalized to all joints or Gaussian-human methods.

## Immediate next experiment

Run **Step 16D2: Jogging learned-LBS reconstruction**.

Use the already validated HUGS source commit and exact Parkinglot forward path:

```text
checkpoint xyz
 -> TriPlane
 -> GeometryDecoder -> canonical xyz
 -> DeformationDecoder
 -> softmax(lbs_logits / 0.1)
 -> learned 24-channel LBS
```

Validate strict state loading, finite outputs, row sums, and full-batch/chunk numerical consistency before building the Jogging K=6 target.

For continuity, read:

- [Step 16C5 Parkinglot axis/sign robustness](../sessions/2026-09-15-step16c5.md)
- [Step 16D1 Jogging checkpoint readiness](../sessions/2026-09-15-step16d1.md)
- [Experiment 07 README](../../experiments/07-cross-sequence-replication/README.md)
- [16D1 compact manifest](../../experiments/07-cross-sequence-replication/analysis/16D1_jogging_checkpoint_manifest.json)
