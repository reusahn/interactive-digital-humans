# Research Session Checkpoint — 2026-09-16 Step 18B1A key-resolution blocker

## Purpose

Localize the Step-18B1 elbow regression mismatch by comparing the current per-Gaussian elbow frame-2 displacement arrays against the archived Step-17B1 and Step-17B2 arrays before any shoulder computation is accepted.

## Partial numerical findings before the implementation error

Seattle and Parkinglot comparisons completed successfully.

For both checkpoints, the current manual reconstruction is extremely close to the archived arrays at the per-Gaussian level but is not elementwise identical.

### Seattle

Learned current vs Step-17B1:

- whole-array sum difference: `-0.0060625748367`
- relative sum error: `-0.000575924729%`
- mean absolute per-Gaussian difference: `7.884706e-08`
- p99 absolute difference: `4.362020e-07`
- max absolute difference: `7.179369e-07`
- Pearson: `0.9999999999284204`
- best global scale archived/current: `1.0000002678063693`
- scaled residual L2 fraction: `1.1782757e-05`

K6 current vs Step-17B1:

- whole-array sum difference: `-0.0004717237252`
- relative sum error: `-4.506242e-05%`
- mean absolute difference: `1.441314e-08`
- Pearson: `0.9999999999866134`

Step-17B1 vs Step-17B2 frame-2 arrays are effectively identical. Their Seattle learned whole-array sum differs by only `-1.5322639e-06`, mean absolute difference `2.966686e-10`, Pearson `0.9999999999996216`.

### Parkinglot

Learned current vs Step-17B1:

- whole-array sum difference: `-0.0115207754993`
- relative sum error: `-0.000344996869%`
- mean absolute per-Gaussian difference: `1.124316e-07`
- p99 absolute difference: `5.091006e-07`
- max absolute difference: `1.308632e-06`
- Pearson: `0.9999999999793191`
- best global scale archived/current: `1.000000288787473`
- scaled residual L2 fraction: `6.333825e-06`

K6 current vs Step-17B1:

- whole-array sum difference: `-0.0019553406673`
- relative sum error: `-5.899678e-05%`
- mean absolute difference: `1.721608e-08`
- Pearson: `0.9999999999966894`

Step-17B1 and Step-17B2 Parkinglot frame-2 arrays are exactly equal for learned and K6 in this audit.

## Interpretation of the partial audit

The Step-18B1 discrepancy is not a gross scientific mismatch. Seattle and Parkinglot show virtually identical spatial displacement fields, with Pearson agreement effectively 1.0 and sub-micro-unit per-Gaussian differences. However, the accumulated learned displacement sum still exceeds the frozen `1e-5` regression tolerance, so the original blocker remains valid. The tolerance must not be widened after observing the discrepancy.

The partial results suggest a very small numerical/source-path difference distributed over many Gaussians rather than a different anatomical or causal pattern. Exact cause remains unresolved until the Jogging audit is completed and the manual path is compared more precisely with the archived generator path.

## Implementation failure

The Step-18B1A audit stopped while resolving the Jogging Step-17B2 frame-2 key.

The generic resolver tested substring token `frame2`. That token also matched:

- `jogging_frame22_learned`
- `jogging_frame27_learned`

in addition to the intended `jogging_frame02_learned`.

The resulting candidate set was non-unique and raised a `RuntimeError` before Jogging comparisons or final audit JSON were saved.

This is a key-parsing bug only. It is not a scientific failure and does not alter any archived displacement array.

## Shoulder status

No shoulder causal computation was performed in Step 18B1A. The frozen third-joint protocol remains unchanged and no shoulder result is accepted yet.

## Exact next action

Rerun the per-Gaussian elbow audit with exact Step-17B2 frame-2 key construction, for example `f"{sequence}_frame02_{condition}"`, instead of substring matching. Complete all three checkpoints and save the compact audit JSON before changing or rerunning the shoulder computation.
