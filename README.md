# PCC Evidence and Provenance System

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

The repository was initialized from an empty baseline on 2026-07-24. This first review stage:

- freezes the available repository, prototype, proposal, bibliography, and Elicit-input baselines;
- assigns stable IDs to PCC components, claims, sources, novelty propositions, searches, and decisions;
- records immutable checksums for all Elicit outputs, imports the raw BibTeX snapshot, and commits normalized CSV derivatives;
- creates linked evidence and provenance registers;
- adds validation and novelty-language guards;
- defines the LaTeX traceability-comment convention;
- establishes the Zotero -> Better BibTeX -> Overleaf workflow.

The current Overleaf/LaTeX source and authoritative Zotero export were not present in the workspace, so proposal traceability insertion and bibliography replacement remain pending rather than being reconstructed from incomplete artifacts.

## Repository map

```text
data/
  components.csv
  claims.csv
  sources.csv
  claim_source_links.csv
  claim_decision_links.csv
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
docs/
  MASTER_SPECIFICATION.md
  BASELINE_2026-07-24.md
  REGISTER_GUIDE.md
proposal/
  TRACEABILITY_CONVENTION.md
schema/
  registers.json
scripts/
  validate_registers.py
tests/
```

## Stable-ID policy

IDs are immutable and never reused:

- `PCC-C##` - PCC components
- `CLM-####` - claims
- `SRC-####` - sources
- `NOV-####` - novelty propositions
- `SEA-####` - searches
- `DEC-####` - decisions
- `IMP-####` - imports

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

## Working rule

Raw inputs are append-only. Never overwrite a raw import. Add a dated snapshot, record its hash in `imports/manifest.csv`, and create or update normalized records in a separate commit.
