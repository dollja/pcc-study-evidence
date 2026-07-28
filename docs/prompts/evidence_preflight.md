# PCC Evidence Preflight

## Recommended Codex mode

**Ask mode.** This task is read-only. It must not edit files, create a branch,
commit changes, or open a pull request.

## Purpose

Adjudicate the exact current proposal text against the canonical PCC claims,
decisions, scholarly evidence, novelty audit, and prototype-evidence records
before any proposal prose is revised.

This prompt is reusable across proposal stages. The launcher must supply the
current revision batch, immutable baselines, files in scope, and the exact
proposal source or an equivalent read-only source packet.

## Required launcher fields

```text
REVISION BATCH:
REV-XXX

EVIDENCE BASELINE:
<full immutable commit SHA>

TARGET PROPOSAL REPOSITORY:
dollja/pcc-proposal-latex

TARGET PROPOSAL COMMIT:
<full immutable commit SHA>

TARGET FILES AND SECTIONS:
- <path and section>
- <path and section>

SOURCE MODE:
exact_source_packet | local_proposal_checkout | pinned_read_only_clone

EXACT SOURCE:
<literal LaTeX source or exact load-bearing paragraphs, with file markers>
```

Optional fields:

```text
STAGE PROMPT:
<proposal stage prompt path>

KNOWN CLAIMS:
<CLM IDs>

KNOWN PROTOTYPE EVIDENCE:
<PEV IDs or none>

AUTHOR-CONFIRMED DECISIONS FOR THIS BATCH:
<exact decisions or none>
```

## Exact-source gate

Before adjudicating any claim, verify that the exact proposal language is
available.

Acceptable source modes:

1. `exact_source_packet`
   - The launcher contains literal source between markers such as:

     ```text
     BEGIN FILE: chapters/01_introduction.tex
     ...
     END FILE: chapters/01_introduction.tex
     ```

   - The packet must include the proposal repository and full proposal commit.
   - Paraphrases, summaries, prior chat descriptions, and compiled-PDF
     recollections are not exact source.

2. `local_proposal_checkout`
   - The selected Codex workspace actually contains the proposal files.
   - Verify each path and run `git rev-parse HEAD`.

3. `pinned_read_only_clone`
   - A proposal checkout is supplied through an explicitly configured,
     read-only mechanism.
   - Verify that its checked-out commit equals `TARGET PROPOSAL COMMIT`.

If exact source is unavailable, return only:

```text
PREFLIGHT STATUS: BLOCKED_MISSING_EXACT_SOURCE

Missing:
- <specific file, section, source marker, or commit>

Recovery:
- <exact information the launcher must provide>
```

Do not continue with sentence-level mapping. Do not claim that proposal files
are absent merely because they are not in this repository when a literal
source packet has been supplied in the task context.

If the source arrives in multiple messages, do not analyze until the launcher
provides:

```text
END REVISION SOURCE
```

## Read before analysis

Read the applicable files, including:

```text
AGENTS.md
docs/MASTER_SPECIFICATION.md
docs/REGISTER_GUIDE.md
docs/PROTOTYPE_EVIDENCE_GUIDE.md
schema/registers.json
data/components.csv
data/claims.csv
data/claim_source_links.csv
data/claim_decision_links.csv
data/component_provenance.csv
data/decisions.csv
data/novelty_propositions.csv
data/novelty_source_links.csv
data/prototype_evidence.csv
data/claim_prototype_links.csv
proposal/section_claim_map.csv
```

Also read any source, import, search, or decision records directly named by
the launcher.

## Authority and evidence rules

1. The PCC Dissertation Master Specification and subsequent
   author-confirmed decisions govern the dissertation's chosen definitions,
   architecture, scope, and terminology.

2. An author decision may define the dissertation. It does not establish what
   prior literature has demonstrated.

3. A literature-dependent statement requires a source link and its recorded
   verification status.

4. `imported_unverified`, abstract-only, or locator-pending evidence supports
   only provisional wording. Do not silently label it full-text verified.

5. A prototype record shows what a specified code revision implemented,
   executed, measured, or failed to do. It is not scholarly evidence and is
   never novelty evidence.

6. Implementation is distinct from demonstration. A controlled synthetic
   demonstration is distinct from comparative evaluation, validation,
   naturalistic generalization, or deployment readiness.

7. A novelty claim cannot exceed the novelty register. A missing keyword,
   missing abstract statement, or unreviewed mechanism is not evidence of
   absence.

8. Do not use personal reviewer or committee identifiers. Use role-based
   provenance only where the canonical register requires it.

9. Do not infer a new decision, source finding, prototype result, or claim
   status merely because it would make the proposal internally consistent.

## Wording ceilings

Assign exactly one primary ceiling to each atomic claim:

```text
author_defined
literature_supported
provisional_literature_support
planned_method
implementation_only
controlled_synthetic_demonstration
current_benchmark_result
limitation_only
future_work_only
unsupported
```

Interpret them as follows:

- `author_defined`: permitted as the dissertation's selected definition,
  architecture, scope, or theoretical commitment; not a literature finding.
- `literature_supported`: supported by appropriate verified scholarly
  evidence with a usable locator.
- `provisional_literature_support`: relevant evidence exists, but full-text
  verification, locator, or adjudication remains incomplete.
- `planned_method`: describes a study, comparison, or measure that has not
  yet produced a result.
- `implementation_only`: code or schema exists at an immutable revision.
- `controlled_synthetic_demonstration`: recorded behavior was reproduced in
  a bounded synthetic case.
- `current_benchmark_result`: a defined metric was reproduced on the stated
  current benchmark; no generalization is implied.
- `limitation_only`: supports only an operational or evidentiary boundary.
- `future_work_only`: states a planned extension or unresolved test.
- `unsupported`: the current records do not license the statement.

## Claim-by-claim procedure

For every load-bearing paragraph, display, definition, research question,
hypothesis, contribution sentence, or result statement in scope:

1. Record:
   - proposal repository;
   - full proposal commit;
   - proposal path;
   - line range if available;
   - section or subsection heading;
   - stable section-anchor suggestion;
   - a short exact excerpt sufficient to identify the text.

2. Split the text into atomic claims with distinct evidence burdens.

3. Map each atomic claim to an existing `CLM` ID where possible.

4. For a genuinely missing claim:
   - use a temporary label such as `PROPOSED-CLM-A`;
   - propose exact atomic wording;
   - propose claim type and components;
   - do not assign a canonical ID in this read-only task.

5. Identify applicable:
   - `DEC` records;
   - `SRC` records and verification status;
   - `NOV` records;
   - `PEV` records, if any.

6. Assign:
   - claim role;
   - wording ceiling;
   - retain, split, revise, weaken, defer, retire, or remove;
   - required evidence or author decision.

7. Identify outdated framing, including any statement that:
   - treats M-ToM plus a session knowledge graph as the current central
     novelty claim;
   - presents action-sensitive ambiguity as wholly new;
   - treats public commitment or common ground as new PCC primitives;
   - equates actor-indexed hypotheses with recovered private mental states;
   - presents planned evaluations as findings;
   - presents synthetic results as naturalistic generalization;
   - implies autonomous repair.

8. Determine whether prototype evidence is required.

Prompt B is required only when the intended proposal wording asserts or
strengthens something about:

```text
implementation
executed behavior
controlled demonstration
metric or benchmark result
leakage control
negative control
abstention behavior
context-conditioned behavior
operational limitation
```

Prompt B is normally skipped for purely author-defined construct, theoretical,
scope, or literature claims.

## Proposal-section map planning

Propose, but do not write, section-map rows containing:

```text
revision_batch
proposal_repository
proposal_commit_sha
proposal_path
section_anchor
claim_id or proposed claim label
claim_role
traceability_status
notes
```

For a pre-revision preflight, use `traceability_status=planned`. Do not invent
a future proposal commit.

## Output format

Return this structure exactly:

```text
# REV-XXX EVIDENCE PREFLIGHT

## Status

GO | CONDITIONAL GO | BLOCKED

## Source verification

- source mode:
- proposal repository:
- proposal commit:
- files and sections received:
- exact-source gate: passed | failed

## Paragraph-level claim disposition

<table or structured list>

## Approved existing claims

<CLM IDs, roles, ceilings, and restrictions>

## Proposed new atomic claims

<temporary labels and exact wording; no canonical IDs>

## Claims to split, revise, weaken, defer, retire, or remove

<claim-specific instructions>

## Scholarly-evidence gaps

<SRC IDs, missing locators, full-text work, or unresolved comparators>

## Author-decision gaps

<exact questions requiring explicit confirmation>

## Prototype-evidence requirement

RUN PROMPT B | SKIP PROMPT B

For each required prototype item:
- claim:
- exact behavior to establish:
- scenario:
- context condition:
- acceptable evidence type:
- minimum test or artifact:
- requested wording ceiling:
- what the evidence must not be used to claim:

## Novelty constraint

<NOV status and permitted wording>

## Proposed section-map rows

<planned mappings>

## Final handoff

REVISION_BATCH:
PREFLIGHT_STATUS:
EVIDENCE_BASELINE:
PROPOSAL_REPOSITORY:
PROPOSAL_COMMIT:
APPROVED_EXISTING_CLAIMS:
PROPOSED_NEW_CLAIMS:
AUTHOR_CONFIRMATIONS_REQUIRED:
PROMPT_B_STATUS:
PROTOTYPE_EVIDENCE_REQUESTS:
NOVELTY_STATUS:
TARGET_PROPOSAL_FILES:
```

## Stop conditions

Stop and return `BLOCKED` when:

- exact proposal text is missing;
- the proposal commit is unknown;
- the requested statement depends on evidence not present in any canonical
  register;
- an unresolved author decision changes the construct materially;
- the requested novelty wording exceeds the novelty register;
- a claimed prototype result lacks an immutable revision and reproducible
  record.

Do not block the entire revision merely because some scholarly links remain
provisional. Approve author-defined wording where appropriate, weaken
literature-dependent language, and identify the verification work that remains.
