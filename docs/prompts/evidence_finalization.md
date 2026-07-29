# PCC Evidence Finalization

## Recommended Codex mode

**Code mode.** This task updates canonical evidence registers, runs validation,
and opens a draft pull request.

## Purpose

Convert an approved evidence preflight and any completed prototype-evidence
closure into canonical claims, links, section mappings, and evidence records.

This prompt never writes proposal prose and never modifies prototype code.

## Required launcher fields

```text
REVISION BATCH:
REV-XXX

FINALIZATION MODE:
pre_revision | prototype_evidence_update | post_proposal_closure

EVIDENCE BASELINE:
<full immutable commit SHA>

TARGET BRANCH:
codex/<bounded-branch-name>

APPROVED EVIDENCE PREFLIGHT:
<paste the approved final handoff and required claim-level details>

AUTHOR CONFIRMATIONS:
<exact confirmed decisions and claim wording, or none>

PROTOTYPE EVIDENCE CLOSURE:
<approved closure handoff and immutable prototype commit, or none>

PROPOSAL MERGE:
<repository, full merge/head commit, and paths, or none>
```

## Read before editing

Read:

```text
AGENTS.md
README.md
docs/MASTER_SPECIFICATION.md
docs/REGISTER_GUIDE.md
docs/PROTOTYPE_EVIDENCE_GUIDE.md
schema/registers.json
scripts/validate_registers.py
data/components.csv
data/claims.csv
data/claim_source_links.csv
data/claim_decision_links.csv
data/component_provenance.csv
data/sources.csv
data/decisions.csv
data/novelty_propositions.csv
data/novelty_source_links.csv
data/prototype_evidence.csv
data/claim_prototype_links.csv
proposal/section_claim_map.csv
```

Read the exact source, search, import, or decision records named in the approved
preflight.

Confirm:

```text
git status --short
git rev-parse HEAD
```

Do not edit if the checked-out baseline differs from `EVIDENCE BASELINE`
without first reporting the mismatch.

## Non-negotiable rules

1. Do not invent claims, decisions, scholarly findings, prototype results,
   locators, or statuses.

2. Add a new `DEC` record only when the launcher contains an explicit
   author-confirmed decision. Do not convert a Codex recommendation into a
   decision.

3. Preserve stable IDs. Never reuse, renumber, or delete an ID. Retain
   superseded and retired rows with explicit status.

4. Preserve existing source verification status. Do not promote
   `imported_unverified`, abstract-only, or locator-pending evidence.

5. Prototype evidence is operational evidence, not scholarly evidence and
   never novelty evidence.

6. `verified` prototype status requires the repository's explicit review
   decision. A successful run alone normally supports `reproduced`, not
   `verified`.

7. Do not strengthen `NOV` status or priority wording unless a separately
   completed novelty audit and explicit decision authorize it.

8. Do not include personal reviewer or committee identifiers.

9. Do not modify files under `imports/raw`.

10. Do not modify proposal prose, prototype source, or bibliographic metadata.

## Mode-specific behavior

### Mode: `pre_revision`

Use this before Prompt D.

- Add only approved atomic claims.
- Add explicit author decisions supplied in the launcher.
- Add required claim-source and claim-decision links.
- Add claim-prototype links only when a completed, approved prototype closure
  is supplied.
- Create section-map rows with `traceability_status=planned`.
- Use the current source proposal commit supplied by the preflight as the
  baseline locator when appropriate.
- Do not invent the future revised proposal commit.

### Mode: `prototype_evidence_update`

Use this after Prompt B when prototype evidence must be registered before
proposal revision.

- Create or update `PEV` rows from the exact closure handoff.
- Create `CPE` links with a permitted relation and wording ceiling.
- Update claim status or implication only as authorized by the preflight.
- Do not modify theoretical, construct, boundary, or novelty support solely
  because a prototype run succeeded.
- Add section mappings only if the preflight approved them.

### Mode: `post_proposal_closure`

Use this after the proposal PR has merged.

- Modify only the relevant `proposal/section_claim_map.csv` rows unless the
  launcher explicitly authorizes another bounded correction.
- Record:
  - proposal repository;
  - full immutable proposal commit;
  - actual path;
  - actual section anchor;
  - `traceability_status=comment_inserted` or `reviewed`;
  - review date;
  - remaining provisional limitations.
- Do not change claim wording, evidence status, prototype evidence, novelty,
  or decisions during a traceability-only closure.

## Atomic claim handling

For each approved new claim:

1. Select the next unused `CLM-####` ID.
2. Use the exact author-approved or preflight-approved wording.
3. Assign:
   - claim type;
   - claim strength;
   - status;
   - proposal location;
   - PCC components;
   - PCC relation;
   - implication;
   - novelty risk;
   - origin;
   - last-reviewed date.
4. Link the claim to at least one appropriate source, decision, or eligible
   prototype record.
5. Do not use prototype-only support for theoretical, boundary, construct, or
   novelty claims.
6. Preserve a clear distinction between:
   - dissertation definition;
   - literature-derived statement;
   - implementation statement;
   - reproduced demonstration;
   - planned empirical test.

## Decision handling

When an exact author confirmation is supplied:

1. Select the next unused `DEC-####` ID.
2. Record the decision neutrally and atomically.
3. Use role-based participants such as `Author` where appropriate.
4. Record affected claims and sections.
5. Link the decision through `data/claim_decision_links.csv`.
6. Do not include meeting narrative or personal reviewer attribution unless
   explicitly required by repository policy.

## Prototype-evidence handling

Create a `PEV` row only when all fields required by its status are available.

For `reproduced` or `verified`, require:

```text
prototype_repository
full immutable commit SHA
evidence_type
scenario_id or not_applicable
context_condition
code_path
symbol_or_test
exact execution_command
output_artifact when required
observed_result
limitations
verified_date
```

Use only the controlled evidence types:

```text
implementation
test
machine_readable_output
metric
limitation
```

Use only the controlled relations:

```text
IMPLEMENTS
DEMONSTRATES
TESTS
PARTIALLY_OPERATIONALIZES
ESTABLISHES_LIMITATION
DOES_NOT_YET_EVALUATE
```

Use only the controlled wording ceilings:

```text
implementation_only
controlled_synthetic_demonstration
current_benchmark_result
limitation_only
future_work_only
```

Status rules:

- `planned`: no execution is claimed.
- `recorded_unverified`: a run was reported but not reproduced from the
  recorded command.
- `reproduced`: the exact command ran against the recorded immutable revision,
  and result plus limitations are retained.
- `verified`: reproduced evidence received explicit required review.
- `superseded`: retained after replacement.

Do not create a metric record without its retained output artifact and raw
counts or denominators where applicable.

## Claim–prototype link handling

For each `CPE` row:

1. Confirm the `CLM` and `PEV` IDs exist.
2. Select the narrowest relation justified by the run.
3. Select the strongest permissible wording ceiling, not the strongest desired
   prose.
4. State what the evidence does not establish.
5. Never use a prototype link to promote novelty.

Examples of acceptable notes:

```text
Supports wording that the extractor produced a temporal candidate in the
specified controlled Q3 case; does not establish comparative advantage,
naturalistic reliability, or generalization.
```

```text
Records that the generic meeting control was rejected at the stated revision;
does not establish a general false-positive rate outside the current corpus.
```

## Section-map handling

For each mapping, use the current schema and controlled vocabulary.

Pre-revision mapping:

```text
traceability_status=planned
proposal_commit_sha=<current source commit if the row maps existing text,
                     otherwise blank when the revised location does not yet exist>
```

Post-revision mapping:

```text
proposal_repository=<repository>
proposal_commit_sha=<full immutable revision>
proposal_path=<actual path>
section_anchor=<actual stable anchor>
traceability_status=comment_inserted | reviewed
```

Do not mark a comment inserted until the referenced proposal revision actually
contains it.

## Validation

Run:

```bash
python scripts/validate_registers.py
python -m unittest discover -s tests -v
git diff --check
```

All checks must pass.

Confirm that:

- no existing stable ID was reused;
- no raw import changed;
- no personal identifier was introduced;
- no prototype evidence was invented;
- no novelty status was strengthened;
- every new foreign key resolves;
- every new reproduced record contains command, result, limitation, and full
  commit SHA.

## Deliverable

Report:

```text
# REV-XXX EVIDENCE FINALIZATION

## Mode

## Baseline and branch

## Files changed

## Claims added, revised, superseded, or retired

## Decisions added

## Scholarly links added or preserved as provisional

## Prototype evidence added

## Claim–prototype links and wording ceilings

## Section-map rows

## Novelty status

## Validation results

## Remaining gaps

## Exact handoff to proposal revision

REVISION_BATCH:
EVIDENCE_COMMIT:
APPROVED_CLAIMS:
APPROVED_DECISIONS:
APPROVED_SOURCE_LINKS:
APPROVED_PEV_IDS:
WORDING_CEILINGS:
NOVELTY_STATUS:
TARGET_PROPOSAL_FILES:
TRACEABILITY_ROWS:
```

Open a draft pull request with a bounded title appropriate to the revision
batch. Do not merge automatically.
