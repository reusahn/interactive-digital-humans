# Latest Research Handoff

Current continuation document:

- [2026-09-15](2026-09-15.md)

Completed today:

- Step 14 corrected counterfactual LBS ablation
- Step 15 Seattle within-sequence pose replication
- Step 16A cross-sequence asset inventory
- Step 16B1 official NeuMan archive range probe
- Step 16B2 selective extraction of five candidate NeuMan SMPL pose assets

Current independent-sequence choice: **parkinglot**.

Reason: parkinglot has 42 frames and effective evaluation raw frames `[2, 7, 12, 17]`, matching the Seattle replication frame indices and giving a clean first cross-sequence comparison.

Next experiment: **Step 16B3 - extract and validate the official parkinglot `human_final.pth` and `config_train.yaml` from the already-persisted HUGS pretrained ZIP.** Verify checkpoint/config provenance and structure before reconstructing parkinglot learned LBS and K=6 target.

For full chat-session continuity, read:

- [main 2026-09-15 session record](../sessions/2026-09-15.md)
- [Step 16B2 session checkpoint](../sessions/2026-09-15-step16b2.md)
- [daily research log](../logs/2026-09-15.md)
