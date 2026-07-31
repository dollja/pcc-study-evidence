# PCC Evidence and Provenance System usage guide

## 1. Authority and repository responsibilities

Apply the canonical order in the [Master Specification](MASTER_SPECIFICATION.md):
author-confirmed specifications and decisions; this repository's evidence and
provenance records; Zotero bibliographic metadata and Better BibTeX; Overleaf
proposal prose; the prototype repository's code, tests, data, outputs, and study
materials; and finally exploratory chats. Conversation history never determines
current state.

The evidence repository links scholarly evidence, author decisions, and referenced
prototype evidence without conflating them. The proposal repository owns revisioned
LaTeX; the prototype repository owns implementation and executable artifacts;
Zotero owns metadata; and Overleaf owns final proposal organization and rendering.

## 2. Registers, IDs, and boundaries

Claims, sources, claim–source links, component provenance, novelty propositions and
links, searches, decisions, prototype-evidence references, and proposal mappings
are separate registers. See the [Register Guide](REGISTER_GUIDE.md) for lifecycles,
relations, and controlled terms, and the [Prototype Evidence Guide](PROTOTYPE_EVIDENCE_GUIDE.md)
for operational-evidence boundaries.

Stable IDs are immutable, never reused or renumbered, and remain present when a
record is superseded or retired. A wording revision does not create a new identity.
Raw imports are append-only and normalized derivatives remain separate.

## 3. Cross-repository revision sequence

1. **Preflight:** read [START_HERE](../START_HERE.md), generated
   [status](../STATUS.md), `workflow/ACTIVE_BATCH`, its manifest, and latest handoff;
   verify the working tree, branch, and HEAD; then confirm baselines and blockers.
2. **Prototype evidence, when required:** execute at an immutable prototype commit,
   retain the exact command, result, artifact, and limitation, then record only a
   reference here. Do not copy prototype code or use PEV evidence as novelty proof.
3. **Evidence finalization:** complete source verification, bounded coding,
   provenance, searches, novelty audit, and role-based review in this repository.
4. **Proposal revision:** revise the proposal only from finalized evidence and at
   the recorded proposal baseline; preserve traceability comments and mappings.
5. **Post-proposal closure:** record reviewed merge SHAs only after merge, reconcile
   mappings and decisions, validate every repository, and close the batch without
   deleting superseded records.

## 4. Literature full-text audit

Freeze the exact source version and checksum; confirm title, authorship, and readable
full text; distinguish exact text from proxy or companion material; inspect scoped
sections and record exact locators. State separately what the source establishes and
how PCC uses it. Record `not_assessable` or a bounded scoped-search result rather
than inferring absence. An abstract, Elicit extraction, title, or keyword miss is not
full-text verification. Log comparator, citation-chain, equivalent-term, and
disconfirmation searches before changing novelty status.

## 5. Prototype evidence and proposal traceability

For PEV work, follow the [entry and lifecycle requirements](PROTOTYPE_EVIDENCE_GUIDE.md):
an exact immutable commit, command, observed result, retained artifact where
required, limitation, and review are prerequisites for stronger statuses. Apply the
claim-link wording ceiling.

For proposal work, use stable claim IDs in traceability comments and maintain
`proposal/section_claim_map.csv` with repository, immutable proposal commit, path,
anchor, role, and review state. Proposal prose stays in the proposal repository; the
mapping stays here.

## 6. Codex findings and context recovery

Treat **P0** as an immediate correctness, safety, or authority-boundary blocker;
**P1** as a high-impact issue that blocks readiness; **P2** as a material but
non-blocking correction; and **P3** as minor cleanup. Verify every finding against
canonical files, resolve P0/P1 before readiness, and either fix or explicitly track
P2/P3. Severity is triage metadata, not evidence and not permission to exceed scope.

In every new Codex task, use the read-only
[current-state locator](../workflow/prompts/00_LOCATE_CURRENT_STATE.md). Do not rely
on conversation memory. If the pointer, manifest, status, handoff, or Git state
conflicts, stop and report the discrepancy rather than guessing.

## 7. Validation and review checklist

- Run the status renderer twice and confirm no second diff.
- Run `python scripts/validate_registers.py` and
  `python -m unittest discover -s tests -v`, then `git diff --check`.
- Review the diff for scope, stable IDs, append-only imports, role-based provenance,
  novelty ceiling, exact locators, immutable SHAs, and separation among scholarly,
  decision, prototype, and proposal records.
- Confirm every recorded merge SHA corresponds to an already merged change and that
  the manifest, generated status, latest handoff, and PR agree.

A revision batch is complete only when all required evidence and optional prototype
stages are reviewed and merged, proposal revision and traceability are merged,
post-proposal reconciliation is complete, all blockers are resolved or explicitly
accepted through an authorized decision, validation passes, closure is recorded,
and the generated status identifies the resulting immutable baselines.
