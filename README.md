# PCC Evidence and Provenance System

> **Start here**
> - [`START_HERE.md`](START_HERE.md)
> - [`STATUS.md`](STATUS.md)
> - [`docs/EVIDENCE_SYSTEM_USAGE_GUIDE.md`](docs/EVIDENCE_SYSTEM_USAGE_GUIDE.md)
> - [Active batch manifest](workflow/batches/REV-003.json)
> - [Latest handoff](workflow/handoffs/REV-003_evidence_finalization.md)

Canonical evidence, provenance, novelty-audit, search, and decision records for:

**Pragmatic Commitment Control: Making Latent Pragmatic Misalignments Observable in Collaborative Work**

This repository is the canonical implementation record for dissertation claims and their evidence. It is not the authority for bibliographic metadata or proposal prose: Zotero remains authoritative for metadata and BibTeX, while Overleaf remains authoritative for the RPI LaTeX proposal.

## Authority order

1. PCC Dissertation Master Specification and subsequent author-confirmed decisions.
2. This repository for claims, sources, provenance, novelty audits, searches, and decisions.
3. Zotero for bibliographic metadata and the authoritative Better BibTeX export.
4. Overleaf for proposal prose and final LaTeX organization.
5. The prototype GitHub repository for code, benchmark data, tests, outputs, and study materials.
6. Dissertation Project chats as exploratory material unless entered into `data/decisions.csv` or imported as a canonical project source.

See `docs/MASTER_SPECIFICATION.md`.

## Current status

See the generated [`STATUS.md`](STATUS.md). It is rendered from the active batch
pointer and manifest rather than maintained independently in this README.

## Repository map

```text
data/
  components.csv
  claims.csv
  sources.csv
  claim_source_links.csv
  claim_decision_links.csv
  prototype_evidence.csv
  claim_prototype_links.csv
  component_provenance.csv
  novelty_propositions.csv
  novelty_source_links.csv
  searches.csv
  decisions.csv
imports/
  manifest.csv
  raw/
  normalized/
bibliography/
  references.bib
  IMPORT_STATUS.md
docs/
  MASTER_SPECIFICATION.md
  BASELINE_2026-07-24.md
  PROTOTYPE_REFERENCE.md
  PROTOTYPE_EVIDENCE_GUIDE.md
  REGISTER_GUIDE.md
proposal/
  TRACEABILITY_CONVENTION.md
  section_claim_map.csv
schema/
  registers.json
scripts/
  validate_registers.py
tests/
workflow/
  batches/
  handoffs/
```

## Cross-repository revision batches

`workflow/batches/REV-###.json` is the canonical cross-repository revision
control record. Generated launchers are derived artifacts: the batch manifest,
not conversation history or a generated prompt, is authoritative for commit
SHAs and stage state. A future merge SHA may be recorded only after the
corresponding pull request has been reviewed and merged.

The commit `3f27be060438a4d01433ac12bcf037b4767431e0` is retained as a
remediation baseline and audit trail. It is not canonical reproduced PEV
evidence and must not be used as novelty proof.

## Stable-ID policy

IDs are immutable and never reused:

- `PCC-C##` - PCC components
- `CLM-####` - claims
- `SRC-####` - sources
- `NOV-####` - novelty propositions
- `SEA-####` - searches
- `DEC-####` - decisions
- `IMP-####` - imports
- `PEV-####` - prototype evidence
- `CPE-####` - claim–prototype links
- `SCM-####` - proposal section–claim mappings

Changes to wording do not change the ID. Superseded records remain in the register with an explicit status and pointer.

## Novelty policy

A candidate novelty proposition may not be rendered as “first,” “unprecedented,” or an equivalent priority claim until:

1. the closest sources have been reviewed in full text;
2. equivalent terminology has been searched;
3. backward and forward citation chains have been examined;
4. a deliberate disconfirmation search has been logged;
5. the residual difference is stated at the same unit of analysis as PCC; and
6. the novelty register status is changed to `supported` through an author-confirmed decision.

The validator rejects strong priority wording for unsupported novelty records.

## Validation

```bash
python scripts/validate_registers.py
python -m unittest discover -s tests -v
```

GitHub Actions runs the same checks on every pull request.

## Prototype evidence

The prototype repository is referenced at an immutable commit; its source code is
not copied into this evidence repository. PEV records are populated only after a
reproducible prototype run can be tied to an exact command, observed result,
limitations, and full commit SHA. Implementation remains distinct from
demonstration, and prototype evidence neither establishes scholarly claims nor
proves novelty. See `docs/PROTOTYPE_EVIDENCE_GUIDE.md`.

## Working rule

Raw inputs are append-only. Never overwrite a raw import. Add a dated snapshot, record its hash in `imports/manifest.csv`, and create or update normalized records in a separate commit. Personal committee identifiers are not stored in repository content; role-based provenance and logged repository-safe derivatives are used instead.
