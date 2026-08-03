# Locate the current PCC system state (read only)

Make **no edits**. Do not infer current state from conversation history.

1. Read `START_HERE.md` and `STATUS.md`.
2. Read `workflow/ACTIVE_BATCH` and resolve its value to
   `workflow/batches/<VALUE>.json`; read that manifest.
3. Read the latest handoff named in `STATUS.md`.
4. Read the manifest's `next_task` object and every path listed under
   `next_task.authorization_files`.
5. Run exactly:

   ```bash
   git status --short
   git branch --show-current
   git rev-parse HEAD
   ```

6. Compare the active batch, current operation, current-task state, downstream
   stages, baselines, source-access controls, and latest handoff in `STATUS.md`
   with the resolved manifest. If they disagree, return `STALE_STATE_RECORD` and
   explain every mismatch. Do not guess which is newer.
7. Otherwise report separately:

   - current batch and repository SHA;
   - evidence, proposal, and prototype baselines;
   - completed operations;
   - **current authorized task and its state**;
   - exact files authorizing the current task;
   - downstream stage gates;
   - access gaps, if any;
   - known limitations.

A downstream stage such as Prompt C may remain gated while the current evidence
task is `ready`. Do not describe the whole workflow as blocked in that case. Use
`BLOCKED_CURRENT_TASK` only when `next_task.state` is explicitly `blocked` and
identify the missing input or unresolved dependency.

Report a dirty tree or unexpected branch as context, not as authorization to alter
files. A merge SHA may be treated as actual only when the repository records show
that its PR was merged.
