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

The next build reached graph construction but failed with `TypeLoadException: UnityEditor.VFX.VFXQuadOutput`, showing that the user's installed VFX Graph 17.3.x patch did not expose that class under the assumed namespace even though the output model exists in older VFX Graph code.

**Corrected interpretation**

Patch-level editor-internal namespace placement is not stable enough to hard-code. PATCH2 resolved exact type names first, then scanned loaded assemblies by short class name and preferred `UnityEditor.VFX*` namespaces.

**Impact**

This is a visualization implementation compatibility failure only. It does not modify any research result or causal interpretation.

**Follow-up**

Continue testing the visualization builder against the user's exact Unity 6000.3.x / VFX Graph 17.3.x installation and record further compatibility assumptions separately if they fail.

---

### A008 — `VFXQuadOutput` was not merely namespaced differently; the installed VFX Graph uses the modern composed particle output model

**Assumption before test**

PATCH2 assumed the installed package still contained a class whose short name was `VFXQuadOutput`, and that only its namespace had changed.

**Contradicting observation**

PATCH2 still failed with `TypeLoadException: UnityEditor.VFX.VFXQuadOutput` after scanning loaded assemblies by short name. Inspection of the current Unity Graphics source showed that modern VFX Graph registers `VFXComposedParticleOutput` through `VFXLibrary`; its Quad variant initializes a `ParticleTopologyPlanarPrimitive(VFXPrimitiveType.Quad)` and the default VFX shader. Current editor tests also create output contexts from the registered `VFXComposedParticleOutput` variant rather than an old `VFXQuadOutput` class.

**Corrected interpretation**

The visualization builder should not search for a legacy quad-output class at all on current 17.3.x. PATCH3 creates the particle output through the package's own `VFXLibrary.GetContexts()` registry, selects the `VFXComposedParticleOutput` Quad variant, and calls the variant's `CreateInstance()` so topology and default shader initialization follow the package's native path. A legacy `VFXQuadOutput` fallback remains only for older package snapshots.

**Impact**

This affects only Unity visualization authoring compatibility. It has no effect on any frozen HUGS deformation-locality result, benchmark statistic, or causal interpretation.

**Follow-up**

Prefer VFX Graph's registered context variants over direct construction of deprecated editor model classes when generating graphs programmatically.

---

### A009 — First Unity visualization passed technical generation but failed the intended visual/art direction

**Assumption before test**

The first generated `Paper_LeakageAtlas` scene was treated as an acceptable first visual prototype once the VFX Graph generation path compiled and rendered.

**Contradicting observation**

The rendered scene was technically functional but visually unsuitable: the body read as a rigid T-pose mannequin assembled from generic point volumes, the intended cyan/red semantic separation was weak, world-space typography was oversized and clipped by the camera frame, and the composition looked like a debug visualization rather than the desired artistic/scientific image.

**Corrected interpretation**

Successful VFX Graph generation is only a technical milestone, not evidence that the visualization language is acceptable. The first scene should be classified as a compatibility/debug scaffold. ART V2 was redesigned around a relaxed A-pose, dark holographic body core, emissive cyan perturbed branch, red contralateral ghost echo, HDRP bloom/ACES/vignette, screen-space typography, and tighter cinematic framing.

**Impact**

No scientific result changes. The failure concerns only the translation of the validated research into visual form.

**Follow-up**

Use `Tools > Research VFX > Build ART V2 Scenes` to generate the redesigned scenes. Continue treating the procedural body as illustrative until the saved Seattle per-Gaussian coordinates and displacement arrays are bound directly into the visualization.

---

### A010 — Step 18B1 manual SMPL/LBS reconstruction did not reproduce the frozen Step-17B1 elbow aggregate within tolerance

**Assumption before test**

The Step-18B1 manual CPU reconstruction of the released HUGS/SMPL pure-LBS path was expected to reproduce the archived Step-17B1 elbow frame-2 aggregate displacement values within the frozen `1e-5` regression tolerance before shoulder metrics were inspected.

**Contradicting observation**

All three checkpoints reproduced the correct changed transform set `[18,20,22]`, exact-zero selective-ablation contralateral response, and nearly identical removed-mass/reduction correlations, but learned contralateral sums differed from the archived values by approximately `3.67e-4` (Seattle), `1.62e-3` (Parkinglot), and `7.59e-5` (Jogging). The strict regression gate therefore failed in all three checkpoints and execution stopped before the shoulder causal section.

**Corrected interpretation**

The manual reimplementation is structurally close but not yet numerically identical to the computation that generated the frozen Step-17 artifacts. This is a pipeline-regression / source-equivalence problem, not a shoulder scientific result. The exact source of the discrepancy remains unresolved.

**Impact**

No Step-18B1 shoulder causal result is accepted. No shoulder thresholds, masks, joint, axis, angle, branch, or pose schedule are changed. The earlier frozen Step-17 benchmark remains unchanged.

**Follow-up**

Compare the newly recomputed elbow per-Gaussian learned/K6/ablated arrays directly against `17B1_left_elbow_frame2_displacements.npz` and the frame-2 slice of `17B2_left_elbow_full_pose_displacements.npz` to isolate whether the mismatch is a global numerical scaling effect or a spatially structured transform/source implementation difference. Do not widen the frozen tolerance after observing the failure.

---

### A011 — Step 18B1A frame-2 key resolver used substring matching and collided with Jogging frames 22/27

**Assumption before test**

The Step-18B1A audit assumed that checking whether a key contained the token `frame2` would uniquely identify the Step-17B2 frame-2 displacement array.

**Contradicting observation**

For Jogging learned displacement, the resolver returned `jogging_frame02_learned`, `jogging_frame22_learned`, and `jogging_frame27_learned` because the substring `frame2` occurs in all three names. The audit raised a `RuntimeError` before completing the Jogging comparison or saving its final JSON.

**Corrected interpretation**

Frame identifiers must be resolved by exact naming, e.g. `f"{sequence}_frame02_{condition}"`, or by an anchored regular expression. Generic substring matching is unsafe for multi-frame experiment keys.

**Impact**

This is an audit implementation failure only. Seattle and Parkinglot per-Gaussian comparisons completed and showed near-perfect agreement with the archived spatial fields. No shoulder causal computation was performed, no research threshold changed, and no archived Step-17 result changed.

**Follow-up**

Rerun Step 18B1A with exact Step-17B2 frame-2 keys and complete the three-checkpoint per-Gaussian audit before repairing or rerunning Step 18B1.

---

### A012 — Displacement evaluation order was not sufficient to explain the Step-18B1 elbow regression mismatch

**Assumption before test**

After Step 18B1A-R showed nearly perfect spatial agreement with archived Step-17 arrays, the leading hypothesis was that the remaining aggregate mismatch was caused primarily by computing displacement from `delta-A` directly instead of first computing full float32 before/after positions and subtracting them as in the historical workflow.

**Contradicting observation**

Step 18B1B substantially reduced the learned-condition contralateral-sum error when full before/after positions were used, but the learned condition still failed the frozen `1e-5` regression gate in all three checkpoints. Best full-position learned errors were approximately `2.93e-5` for Seattle, `4.78e-5` for Parkinglot, and `1.12e-5` for Jogging. K6 passed in all three checkpoints. Reconstructed Seattle historical before/after positions still differed from the saved probe at distributed float32 scale, with mean absolute errors around `5e-8` and maxima around `9.54e-7`.

**Corrected interpretation**

Evaluation order contributes materially to the mismatch but does not fully explain it. The remaining discrepancy lies earlier in the exact transform/backend path, likely in manual versus source-exact SMPL transform construction and/or floating-point backend execution order.

**Impact**

The frozen `1e-5` tolerance is not widened. No shoulder causal output is accepted. Step 17 remains unchanged.

**Follow-up**

Compare the current manual `A` transforms directly against transforms produced with the exact `smplx.lbs` functions used by HUGS, then test source-exact one-shot versus chunked float32 skinning before attempting shoulder computation.

---

## Status

This ledger is cumulative. Future failed assumptions and material implementation failures should be appended rather than replacing earlier entries.
