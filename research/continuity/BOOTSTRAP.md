# New Chat Bootstrap

Use this file when starting a new research conversation.

## Required loading order

Before proposing experiments, writing claims, or interpreting new results, read these files from `reusahn/interactive-digital-humans`:

1. `research/continuity/MASTER_CONTEXT.md`
2. `research/continuity/CLAIM_LEDGER.md`
3. `research/handoffs/LATEST.md`
4. the most recent relevant file under `research/sessions/`

If the task concerns a particular experiment, also load its protocol, script, and archived session record before making claims about it.

## Continuity rule

Treat GitHub as the authoritative research memory. Do not rely on conversational memory alone.

The current research program is Interactive Digital Humans / Real-Time 4D Human Intelligence. The active first-paper topic is anatomical locality in learned animatable-human deformation. Step 18 is frozen at 18D1. Corrective-method implementation has not started.

## Scientific integrity rules

- Preserve the preregistered shoulder failure.
- Do not retune thresholds after seeing results.
- Distinguish confirmatory, exploratory, and unresolved evidence.
- Do not count nested poses as independent replications.
- Do not claim kinematic depth is causal.
- Do not claim a training-level cause has been established.
- Do not generalize from HUGS to learned digital humans in general without additional cross-method evidence.
- Freeze Step 19 evaluation protocol before method implementation.

## Research workflow

For experiment-running conversations:

1. Give exactly one next executable Colab cell when a cell is needed.
2. Wait for the user's full output.
3. Diagnose the exact result.
4. Archive meaningful results to GitHub.
5. Update `LATEST.md` when the continuation state changes.
6. Update `MASTER_CONTEXT.md` and `CLAIM_LEDGER.md` only when durable scientific understanding changes.

Large raw arrays and checkpoints stay on Drive. Compact Markdown, JSON, CSV, scripts, protocols, and provenance records belong in GitHub.

## One-line instruction the user can paste in a fresh chat

`이전 연구 이어가자. GitHub reusahn/interactive-digital-humans의 research/continuity/BOOTSTRAP.md, MASTER_CONTEXT.md, CLAIM_LEDGER.md, research/handoffs/LATEST.md를 먼저 읽고 현재 frozen state를 확인한 다음에만 답해.`

## Exact-transcript limitation

These continuity files preserve the scientific state, decisions, metrics, failures, hypotheses, artifact paths, and next actions. They are not a guaranteed verbatim archive of every sentence exchanged in ChatGPT.

If an exact old conversation transcript matters, preserve/export that transcript separately and add it to the repository or provide it in the new conversation. Scientific continuity should not depend on exact transcript availability.
