# PCC Evidence and Provenance Repository Instructions

## Authority

This repository is authoritative for claims, sources, evidence links,
component provenance, novelty audits, searches, decisions, and
prototype-evidence references.

It is not authoritative for bibliographic metadata, proposal prose, or
prototype implementation.

## Non-negotiable rules

- Do not include personal advisor or committee identifiers.
- Use role-based provenance such as author_review, advisor_review,
  committee_review, or external_review.
- Do not overwrite files under imports/raw.
- Do not reuse or renumber stable IDs.
- Do not strengthen novelty wording unless the novelty register supports it.
- Do not convert an Elicit extraction into a full-text-verified finding.
- Separate scholarly evidence, author decisions, and prototype evidence.
- Preserve superseded and retired records rather than deleting them.

## Validation

Run:

python scripts/validate_registers.py
python -m unittest discover -s tests -v

Do not merge or mark a pull request ready without passing validation.
