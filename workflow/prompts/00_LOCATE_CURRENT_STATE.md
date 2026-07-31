# Locate the current PCC system state (read only)

Make **no edits**. Do not infer current state from conversation history.

1. Read `START_HERE.md` and `STATUS.md`.
2. Read `workflow/ACTIVE_BATCH` and resolve its value to
   `workflow/batches/<VALUE>.json`; read that manifest.
3. Read the latest handoff named in `STATUS.md`.
4. Run exactly:

   ```bash
   git status --short
   git branch --show-current
   git rev-parse HEAD
   ```

5. Compare the active batch, operation, stages, baselines, and latest handoff in
   `STATUS.md` with the resolved manifest. If they disagree, return
   `STALE_STATE_RECORD` and explain every mismatch. Do not guess which is newer.
6. Otherwise report: current batch; current repository SHA; evidence, proposal, and
   prototype baselines; completed stages; blocked stages; blockers; known
   limitations; next authorized task; and the exact files authorizing that task.

Report a dirty tree or unexpected branch as context, not as authorization to alter
files. A merge SHA may be treated as actual only when the repository records show
that its PR was merged.
