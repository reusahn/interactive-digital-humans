# Latest Research Handoff

Current continuation document:

- [2026-09-15](2026-09-15.md)

Completed today:

- Step 14 corrected counterfactual LBS ablation
- Step 15 Seattle within-sequence pose replication
- Step 16A cross-sequence asset inventory
- Step 16B1 official NeuMan archive probe

Step 16B1 confirmed that the official `neuman_data.zip` is `4.204 GiB` and supports HTTP byte-range requests (`206`, `Accept-Ranges: bytes`). The full archive has **not** been downloaded.

Current strategy: avoid storing the full 4.2 GiB archive. Use a range-backed remote ZIP reader to selectively extract only the per-sequence `4d_humans/smpl_optimized_aligned_scale.npz` pose assets for the independent HUGS candidates, inspect their frame counts, then choose the first cross-sequence replication model.

Next experiment: **Step 16B2 - selectively extract and inspect candidate NeuMan SMPL pose NPZ files from the official remote ZIP.**

For full chat-session continuity, read [the structured 2026-09-15 session record](../sessions/2026-09-15.md), [the Step 16B1 session checkpoint](../sessions/2026-09-15-step16b1.md), and [the daily research log](../logs/2026-09-15.md).
