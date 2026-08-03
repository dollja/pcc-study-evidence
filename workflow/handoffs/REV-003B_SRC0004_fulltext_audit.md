# REV-003B SRC-0004 exact full-text audit handoff

## Revision control and source controls

- **Parent batch:** `REV-003`.
- **Audit task:** exact-source addendum to `REV-003B-AUDIT`.
- **Starting canonical evidence SHA:** `4f0cee14945929d195ced29daa9725e416d8b3be`.
- **Starting intake operation:** PR #22, merge `4f0cee14945929d195ced29daa9725e416d8b3be`.
- **Proposal baseline, unchanged:** `a73275c9675eccf303d588229371a7d198b4a2e3`.
- **Prototype baseline, unchanged; Prompt B skipped:** `c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4`.
- **Source:** `SRC-0004`, P.L.A. Piwek, *Situated action and commitment in dialogue*, *IPO Annual Progress Report 32* (1997), printed pp. 89-97.
- **Exact raw scan:** `imports/raw/literature/REV-003B/SRC-0004_piwek_1997_situated.pdf`.
- **Raw SHA-256:** `338b24096b8acf12d87e48a34fac3f3207b22799507e4efb4fcfe3a039a73a67`.
- **Reading aids:** searchable PDF SHA-256 `4fc392bce91a7e249b5ac27e7352c13f3cf214e8becca1f5612118252e602c34`; OCR text SHA-256 `6343b55bebc0c6006bcb3cb55de6063afcc653f2c058bbf384268c07c14fc859`.

The OCR derivatives were used only to navigate the scan. Every affirmative mechanism finding and locator in `audits/REV-003B/SRC-0004.md` was checked against the raw page image. Printed page numbers are authoritative; PDF page numbers may be added only as navigation aids.

## Audit completeness

All nine PDF pages / printed pp. 89-97 were reviewed. The mechanism audit covered:

- conditional relevance and context-dependent response sets;
- actor-associated dialogue state;
- commitments attributed to self and other;
- public and shared commitment sets;
- unsettled judgments;
- declarative, imperative, and interrogative update behavior;
- Transparency and Discussion rules;
- confirmation, denial, refusal, compliance, and default cancellation;
- linguistic and non-linguistic action constraints;
- multimodal evidence in the shared block workspace;
- expert-role asymmetry;
- inspectability and contestability;
- reported DenK implementation lineage;
- evaluation and limitations.

## Exact-source verdict

**SRC-0004 is a possible near-equivalent, with high confidence for the exact 1997 text, but is not novelty-defeating under the current PCC mechanism definition.**

Strongest overlap:

1. A dialogue state is associated with an actor and records commitments that actor ascribes to self and other.
2. Public and shared commitments are explicit formal state.
3. Assertions, requests, reception signals, confirmation, denial, presupposition, entailment, physical action, and expert acceptance provide update evidence.
4. Transparency and Discussion rules govern when commitments become public or shared.
5. Commitments constrain linguistic and physical action.
6. The block example connects request, physical execution, expert acceptance, shared commitment, and persistent object-state change.
7. The source reports that substantial parts of the information-state model were used in DenK.

The source therefore establishes that actor-indexed commitment state, public/shared uptake, response-governed commitment update, multimodal evidence, and commitment-to-action transitions are inherited mechanisms rather than PCC novelties.

## Residual PCC boundary

The following joint links were not located after scoped review:

- explicit extraction and comparison of competing values for an action-sensitive task variable;
- calibrated evidence sufficiency, confidence, cost, or abstention;
- formal organizational authority, entitlement, permission, or approval governance;
- durable workflow-artifact state, policy, approval chain, or handoff governance;
- a participant-facing diagnostic record exposing evidence, alternatives, authority basis, warrant, uncertainty, and consequences;
- a path to challenge or appeal the system's evidence attribution or promotion decision;
- empirical evaluation of diagnostic correctness, localization, calibration, false-positive burden, or contestability.

The task-expert asymmetry in the block example is meaningful situated context, but it is not a general formalization of organizational authorization. Denial, confirmation, refusal, and default cancellation are interactional challenge mechanisms, but they are not a contestation interface for a diagnostic system.

## Register and audit-artifact changes

- `audits/REV-003B/SRC-0004.md`: exact full-text mechanism card added.
- `audits/REV-003B/SRC-0004_access_gap.md`: retained as a historical record and marked superseded for current access status.
- `audits/REV-003B/cross_source_matrix.md`: exact SRC-0004 column replaces the access-gap column.
- `data/sources.csv`: `SRC-0004` advanced to `fulltext_verified` / `fulltext_audit_complete` with exact scope and residual limitations.
- `data/claim_source_links.csv`: `CE-0011` replaced with exact locator-backed support and boundary; `CE-0026` links the bounded finding to the candidate combination claim.
- `data/component_provenance.csv`: `CP-0015` verified and `CP-0049` through `CP-0053` record actor state, public evidence, promotion rules, consequence-bearing action, and contestability boundary.
- `data/novelty_source_links.csv`: `NS-0006` now records strongest overlap first and the exact residual second.
- `data/searches.csv`: `SEA-0005` records the exact-source scoped review.
- `workflow/handoffs/REV-003B_fulltext_audit.md`: updated to incorporate the addendum without treating REV-003 as complete.

## Novelty wording ceiling

`NOV-0001` remains `candidate`.

Permitted wording:

> The exact Piwek 1997 source already combines actor-associated own/other commitment state, public/shared commitment updates, multimodal evidence, and consequence-bearing action. PCC therefore treats these as inherited mechanisms. Its remaining proposed contribution is a more specific diagnostic combination centered on action-sensitive candidate interpretations, explicit evidence sufficiency under role/authority and artifact/workflow constraints, participant-facing contestability, and direct evaluation.

Not permitted:

- PCC is the first system to model situated commitments or shared commitments.
- Prior work lacks commitment-to-action transitions.
- The exact Piwek source lacks action, public evidence, role context, or multimodality.
- Novelty or priority is established.

## Exact next task

1. Merge this exact-source audit addendum after review and validation.
2. Synchronize the REV-003 workflow-control record and generated `STATUS.md` using the actual intake and audit PR numbers and merge SHAs.
3. Complete REV-003A exact full-text audits for `SRC-0002`, `SRC-0003`, and `SRC-0010`.
4. Perform a deliberate combined Tier 1 synthesis using exact `SRC-0004`; keep `SRC-0036` only as separate proxy/companion context.
5. Do not run Prompt C until REV-003A and the combined synthesis are reviewed. Do not run Prompt D until Prompt C merges. Do not mark closure or a final novelty conclusion.
