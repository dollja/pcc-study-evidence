# PCC Dissertation Master Specification

Status: **canonical author-confirmed specification**  
Effective date: **2026-07-24**  
Latest author-confirmed amendment: **2026-09-14**

## Title

**Pragmatic Commitment Control: Making Latent Pragmatic Misalignments Observable in Collaborative Work**

## Primary empirical substrate

Synthetic human-human-like workplace coordination.

## Theoretical structure

- Theory of Mind is the actor-indexed representational foundation.
- Grounding and common ground provide the public-evidence background.
- PCC addresses public warrant and promotion into coordination commitment.
- Action sensitivity identifies which interpretations have materially different downstream consequences.
- CSCW supplies the situated organizational, artifact, role, authorization, and workflow context.
- Observability, abstention, and contestability govern diagnostic output.

## 2026-09-14 observable-target amendment

The **primary computational target** is an interpretation-dependent operational action that lacks the support required by the documented task rules at a specified observation time.

The target is evidence-relative and time-indexed. The system must distinguish positive evidence of insufficient support from an incomplete record. Primary task-level labels therefore include `SUPPORTED`, `UNSUPPORTED`, `CANNOT_DETERMINE`, `NO_OPERATIONAL_EVENT`, and `OUT_OF_SCOPE`.

**Latent pragmatic misalignment (LPM) remains a separate, stronger cognitive claim.** An unsupported operational action does not by itself establish LPM: the same operational failure may arise from missing authorization, incomplete documentation, stale context, or ordinary process error even when collaborators share the same interpretation.

LPM is therefore annotated separately from the primary operational target. Evidence of actor-indexed interpretive divergence, apparent uptake/second-order assumptions, and repair status may be used to test the relationship between the two claims rather than to define them as equivalent.

The cognitive motivation is preserved: bounded actor-indexed and second-order representations remain candidate explanatory/diagnostic mechanisms. Their incremental value must be tested empirically rather than assumed to be necessary for establishing the primary operational label.

Detailed warrant and annotation rules are recorded in `docs/REVISION_GUIDANCE_STAGE1_TARGET_WARRANT_CODEBOOK.md`.

## Canonical authority order

1. This master specification and subsequent author-confirmed decisions.
2. The PCC Evidence and Provenance GitHub repository for claims, sources, provenance, novelty audits, searches, and decisions.
3. Zotero for bibliographic metadata and the authoritative BibTeX export.
4. Overleaf for proposal prose and final LaTeX organization.
5. The prototype GitHub repository for code, benchmark data, tests, outputs, and study materials.
6. Dissertation Project chats are exploratory and are not canonical unless their conclusions are entered into the decision log or saved as a canonical project source.

## Initial implementation tasks

1. Freeze and document the current proposal and prototype baseline.
2. Create and validate the linked evidence registers.
3. Import existing bibliography and Elicit outputs without silently overwriting raw data.
4. Assign stable IDs to PCC components, claims, novelty propositions, sources, searches, and decisions.
5. Add traceability comments to the LaTeX source.
6. Replace the manual proposal bibliography with an authoritative BibTeX workflow.
7. Revise the proposal in small, reviewable stages.
8. Do not strengthen novelty language unless the novelty register and closest-prior-work audit support it.

## Scope boundary

PCC diagnostic records represent bounded, evidence-backed hypotheses about apparent task interpretations and commitments. They do not claim direct access to private mental states, do not decide who is right, and do not authorize autonomous repair.
