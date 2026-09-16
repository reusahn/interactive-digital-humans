# Assumption and Failure Ledger

This file preserves failed assumptions, disproven hypotheses, implementation misunderstandings, and corrections that materially affected or could have affected the research trajectory.

The purpose is not only to record final successful results. The research record should retain the reasoning path, especially where an assumption was contradicted by evidence.

## Recording rule

For every meaningful failed assumption, preserve:

1. **Assumption before test**
2. **Observation that contradicted it**
3. **Corrected interpretation**
4. **Impact on prior results**
5. **Follow-up action or audit**

Do not silently rewrite history after a later explanation is found. A corrected explanation should be added alongside the original failed assumption.

---

## Ledger entries

### A001 — Seattle HUGS validation-frame mapping

**Assumption before test**

The working interpretation initially treated `val_dataset[0]` as raw NeuMan frame 22.

**Contradicting observation**

Independent reconstruction of the HUGS data split showed that the dataset assignment uses the helper's third split output as `self.val_split`, making Seattle evaluation raw frames `[2,7,12,17]`. Direct raw-frame reconstruction verified frame 2 with approximately `2.36e-7` mean xyz error.

**Corrected interpretation**

`val_dataset[0]` corresponds to raw NeuMan frame 2, not 22.

**Impact**

Any earlier wording attaching the baseline probe to raw frame 22 was incorrect and was retired. The actual deformation measurements remain usable once associated with raw frame 2.

**Follow-up**

All later Seattle counterfactual and frame-replication work uses raw frame 2 as the first evaluation frame.

---

### A002 — Left-ankle locality target was initially too narrow

**Assumption before test**

An early leakage interpretation treated same-leg upstream knee/hip propagation as outside-target leakage for the left ankle and suggested a distal-greater-than-proximal pattern.

**Contradicting observation**

After correcting the anatomical target to include the full same-side local kinematic chain, the ankle nonlocal fraction dropped substantially. The earlier distal-greater-than-proximal narrative depended on counting expected same-leg propagation as leakage.

**Corrected interpretation**

The appropriate hierarchy is:

`intended part -> same-side local kinematic chain -> nonlocal remainder`.

The wrist remains the clearest high-confidence nonlocal case.

**Impact**

The earlier broad claim that distal joints necessarily leak more than proximal joints was retired/qualified.

**Follow-up**

All later masks explicitly separate intended, same-side local chain, and nonlocal/contralateral subsets.

---

### A003 — Seattle HC-count discrepancy was initially suspected to be `>=0.9` vs `>0.9`

**Assumption before test**

When Step 17A recomputation produced Seattle HC `197781` / contra `33074` instead of the frozen `197778` / `33072`, the leading hypothesis was a threshold-comparator difference between `>=0.9` and `>0.9`.

**Contradicting observation**

Step 17A1 found zero exact confidence values at `0.9`. Both comparators produced the same counts. The discrepancy came from using recomputed `argmax/max(effective_lbs)` rather than the historical `saved_dominant/saved_confidence` anatomy stored in the Step-13A artifact.

**Corrected interpretation**

The frozen Seattle benchmark anatomy source is `saved_dominant + saved_confidence`; `effective_lbs` remains the deformation-weight source.

**Impact**

No threshold was changed. Two additional recomputed contralateral rows were excluded by restoring the benchmark-consistent saved anatomy. The elbow precursor ordering changed negligibly and remained learned > K6.

**Follow-up**

Step 17A2 froze one canonical anatomy source per checkpoint before elbow causal perturbation.

---

### A004 — Assumed `hugs_triplane -> HUGS_TRIMLP` alias in released source

**Assumption before test**

After Step 17B1A, the working provenance hypothesis was that the pretrained packaged config literal `human.name: hugs_triplane` must resolve through an alias, registry, or factory branch to `HUGS_TRIMLP`.

**Contradicting observation**

Step 17B1B found zero tracked Python-source occurrences of `hugs_triplane` in exact HUGS commit `86ebe5522a384fc553f07f090b63a76dd4af8d33`. The audit failed because the expected alias did not exist.

**Corrected interpretation**

Step 17B1C established that the released source and official release configs use `hugs_trimlp`, and the trainer directly maps `cfg.human.name == 'hugs_trimlp'` to `HUGS_TRIMLP`. The downloaded pretrained package configs instead contain `hugs_triplane`, for which no executable alias exists in the released commit. This is recorded as packaged-config naming/label drift, not an alias.

**Impact**

No reconstruction rerun is required because Step 17B1A already showed exact numerical equality between the stored Seattle, Parkinglot, and Jogging learned-LBS arrays and reconstruction under the released `HUGS_TRIMLP` semantics. LBS differences were exactly `0.0`; Parkinglot/Jogging canonical XYZ differences were also `0.0`.

**Follow-up**

Provenance statements must distinguish the packaged config label from the released implementation name. Do not claim an alias exists.

---

### A005 — Step 17B2 code cell was truncated during transfer

**Assumption before test**

The Step 17B2 full-pose cell was assumed to have been transferred into Colab as a complete executable cell.

**Contradicting observation**

Execution stopped before any scientific computation with `SyntaxError: unterminated string literal (detected at line 200)`. Inspection of the pasted cell showed that the code itself was cut off partway through the Jogging sequence definition, leaving an incomplete string / dictionary literal.

**Corrected interpretation**

This was a code-delivery/truncation failure, not an experimental result and not evidence against the elbow hypothesis.

**Impact**

No Step 17B2 scientific output exists from this run. No thresholds, masks, joint definitions, pose schedules, or prior results are changed.

**Follow-up**

Rerun Step 17B2 from a shorter, self-contained replacement cell. Record the syntax failure separately from the subsequent scientific result.

---

### A006 — Unity VFX 17.3 visualization builder assumed a `GetGraph` helper that was unavailable in the installed patch

**Assumption before test**

The first ResearchViz Unity builder assumed that the installed VFX Graph 17.3.x editor assembly exposed `UnityEditor.VFX.VisualEffectResourceExtensions.GetGraph` through reflection.

**Contradicting observation**

Running `Tools > Research VFX > Build / Repair Demo` failed before scene generation with `MissingMethodException: Method 'UnityEditor.VFX.VisualEffectResourceExtensions.GetGraph' not found.`

**Corrected interpretation**

The visualization toolchain must not rely on that editor-internal extension method as a stable 17.3.x API. PATCH1 changed graph discovery to locate the serialized `VFXGraph` subasset through `AssetDatabase`, with optional reflection fallbacks.

**Impact**

This affected only the experimental visualization bootstrap. It has no effect on HUGS research measurements, frozen masks, causal tests, or benchmark conclusions.

**Follow-up**

Treat VFX Graph editor-authoring APIs as patch-sensitive implementation details and keep compatibility failures separate from scientific failures.

---

### A007 — Unity VFX 17.3 visualization builder assumed `VFXQuadOutput` lived in a fixed namespace

**Assumption before test**

PATCH1 still resolved VFX editor model classes by exact fully qualified names, including `UnityEditor.VFX.VFXQuadOutput`.

**Contradicting observation**

The next build reached graph construction but failed with `TypeLoadException: UnityEditor.VFX.VFXQuadOutput`, showing that the user's installed VFX Graph 17.3.x patch did not expose that class under the assumed namespace even though the output model exists in the VFX Graph codebase.

**Corrected interpretation**

Patch-level editor-internal namespace placement is not stable enough to hard-code. PATCH2 resolves exact type names first, then scans loaded assemblies by short class name and prefers `UnityEditor.VFX*` namespaces.

**Impact**

Again, this is a visualization implementation compatibility failure only. It does not modify any research result or causal interpretation.

**Follow-up**

Continue testing the visualization builder against the user's exact Unity 6000.3.x / VFX Graph 17.3.x installation and record further compatibility assumptions separately if they fail.

---

## Status

This ledger is cumulative. Future failed assumptions and material implementation failures should be appended rather than replacing earlier entries.
