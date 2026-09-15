# Research Session Checkpoint - 2026-09-15 Step 17B1B Assumption Failure

## Purpose

Record a failed provenance assumption discovered while trying to close the HUGS config-to-class provenance chain.

## Pre-audit assumption

Before running Step 17B1B, the working assumption was that the packaged pretrained config literal:

`human.name: hugs_triplane`

would resolve through an explicit alias, registry, factory branch, or equivalent source mapping to:

`HUGS_TRIMLP`

in exact HUGS source commit:

`86ebe5522a384fc553f07f090b63a76dd4af8d33`.

This was a hypothesis about provenance, not an observed fact.

## Observed result

The Step 17B1B audit found:

```text
HUGS_TRIMLP definition confirmed: True
literal `hugs_triplane` Python-source hit count: 0
```

The cell then raised:

```text
RuntimeError: No official Python source contains literal hugs_triplane.
```

The runtime error reflects a failed audit assumption, not a failure of the reconstruction or causal experiment.

## Corrected interpretation

Inspection of the exact released source shows that the official release configuration uses:

`human.name: hugs_trimlp`

and the trainer directly executes the branch:

`cfg.human.name == 'hugs_trimlp'`

which constructs:

`HUGS_TRIMLP(...)`.

No executable `hugs_triplane` alias has been established in the released commit. The pretrained package configs instead contain the different literal `hugs_triplane`.

Therefore the prior statement that there should be a `hugs_triplane -> HUGS_TRIMLP` alias was incorrect. The current hypothesis is that this is packaged-config naming drift or a legacy/stale package label rather than an alias in the released source. This hypothesis must itself be audited and recorded rather than silently substituted as fact.

## Downstream impact

This failed provenance assumption does not by itself invalidate the numerical experiments because Step 17B1A independently established exact numeric equivalence between stored learned-LBS arrays and reconstruction under the located HUGS_TRIMLP semantics for Seattle, Parkinglot, and Jogging.

No decoder, mask, threshold, perturbation, endpoint, or stored causal result is changed by this correction.

## Research-integrity rule reinforced

For this project, assumption failures are first-class results and must be preserved in the record. Each such event should distinguish:

1. the assumption made before the test,
2. the observation that contradicted it,
3. the corrected interpretation or new hypothesis,
4. whether prior experimental results are affected,
5. the exact follow-up audit needed.

Do not overwrite or hide a failed assumption after a later explanation is found.

## Exact next action

Run Step 17B1C only to test the new provenance hypothesis:

- released source uses `hugs_trimlp -> HUGS_TRIMLP`,
- packaged pretrained configs use `hugs_triplane`,
- released commit contains no executable `hugs_triplane` alias,
- Step 17B1A numeric equivalence remains exact.

Only after that audit should the provenance issue be considered resolved enough to proceed to the full predeclared elbow pose schedule.
