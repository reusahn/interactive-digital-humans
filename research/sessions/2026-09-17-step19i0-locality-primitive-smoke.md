# Step 19I0 — Locality Primitive Implementation + Synthetic Smoke Test

Date: 2026-09-17

Status: `PASS`

Scientific training performed: `NO`

Scientific outcome observed: `NO`

## Frozen provenance

Audited Apple HUGS base commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`

Implementation branch:

`step19-locality-impl`

Implementation commit:

`f6065a9ca07a3dac2133f14d9e7f135e7a2c3f87`

Only changed source file:

`hugs/losses/locality.py`

Locality module SHA256:

`b811d2473cff99b56d596e525363f9f95a253bc2bf73da2ad855154273e18caf`

Drive patch:

`private_research/2026-09-17_step19i0_locality_primitive.patch`

Patch SHA256:

`5d341b3f77ae36afc107a749ea823ed16eb7a7a98655451af26823bf2ebee274`

Drive metadata:

`private_research/2026-09-17_step19i0_locality_primitive_smoke.json`

Metadata SHA256:

`25f0b0ce93fe1095f03708c528a3e1e09b9d0236935aeb3ed8afae71066a4745`

## Implemented primitive

Frozen primary method primitive:

`L_local = mean_g sum_j w[g,j] * (1 - M[g,j])`

where:

- `w` is post-softmax normalized learned HUGS LBS weight
- support envelope threshold `rho = 0.99`
- exact ties are resolved by lower SMPL joint index
- `M` is detached/non-differentiable envelope membership
- no gradient flows through `q_K6` or `M`
- no hard clipping or post-softmax weight modification occurs

## Synthetic smoke-test result

Runtime:

`torch 1.13.1+cu117`

Observed synthetic locality loss:

`0.44640886783599854`

Observed synthetic NSM per Gaussian:

`[0.013333775103092194, 0.7705470323562622, 1.0, 0.00175461545586586]`

Learned-logit gradient absolute sum:

`0.9585590958595276`

`q_K6` gradient:

`None`

`lambda_local = 0` weighted locality contribution:

`0.0`

## Smoke checks

All passed:

1. envelope rows nonempty
2. mask bool/binary
3. reference rows required normalized
4. learned rows required normalized
5. `L_local >= 0`
6. `lambda_local = 0` contributes exactly zero
7. no gradient to K6 reference/mask
8. nonzero finite gradient to learned logits
9. locality primitive does not alter learned normalized weights
10. no scientific validation/test metric inspected

## Interpretation

The frozen mathematical locality primitive is implemented and internally consistent on synthetic data. This is implementation validation only and is not scientific evidence for the Step-19 hypothesis.

## Next action

Proceed to Step 19I1 integration smoke testing only:

- integrate locality metadata/reference into HUGS forward/loss path
- preserve original deformation equation and renderer
- verify `lambda_local=0` baseline equivalence
- verify locality gradients reach actual deformation-decoder parameters
- do not inspect Seattle validation/test or Parkinglot/Jogging outcomes
