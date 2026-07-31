# Import REV-003B exact full texts and Piwek proxy

Run in the Codex environment connected to:

```text
dollja/pcc-study-evidence
```

Use **Code mode** on branch:

```text
codex/stage-rev003b-fulltext-intake-package
```

This prompt is now stored inside the repository, so no chat attachment is
required. The task does require internet access for these domains:

```text
arxiv.org
jlcl.org
```

If agent internet access is disabled, stop with
`BLOCKED_SOURCE_DOWNLOAD_DISABLED` and identify the required setting. Do not
continue from abstracts or Elicit summaries.

## Revision control

```text
PARENT BATCH:
REV-003

SOURCE-INTAKE SUBTASK:
REV-003B-FULLTEXT-INTAKE

EXPECTED STARTING BASELINE:
bb4788ed2065a531ca165bf7ef3c0bdbb92ad912

STAGING BRANCH:
codex/stage-rev003b-fulltext-intake-package

TARGET WORK BRANCH:
codex/import-rev003b-fulltexts-with-piwek-proxy
```

Before editing, run:

```bash
git status --short
git rev-parse HEAD
```

The tree must be clean. If `main` has advanced beyond the expected baseline,
use the current reviewed `main` commit and report the actual SHA; do not reset
or discard newer canonical work.

## Source acquisition

Create a temporary acquisition directory and download the exact public source
versions:

```bash
set -euo pipefail
mkdir -p /tmp/rev003b-fulltext

curl -L --fail --retry 3 \
  https://arxiv.org/pdf/2602.02843v3 \
  -o /tmp/rev003b-fulltext/SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf

curl -L --fail --retry 3 \
  https://arxiv.org/pdf/2607.01236v1 \
  -o /tmp/rev003b-fulltext/SRC-0021_she_liang_kang_2026_arxiv_v1.pdf

curl -L --fail --retry 3 \
  https://jlcl.org/article/view/21/19 \
  -o /tmp/rev003b-fulltext/SRC-0036_piwek_2000_imperatives_commitment_action.pdf

file /tmp/rev003b-fulltext/*.pdf
sha256sum /tmp/rev003b-fulltext/*.pdf
```

Verify that every downloaded file is a PDF and inspect page 1 before copying
anything into the repository.

Expected identities:

```text
SRC-0007
title: Act or Clarify? Modeling Sensitivity to Uncertainty and Cost in Communication
authors: Polina Tsvilodub; Karl Mulligan; Todd Snider; Robert D. Hawkins; Michael Franke
version: arXiv:2602.02843v3
expected pages: 8
reference upload sha256: 324b61fb388af4db1de1449fda5308df55d069de4ec1548c4e28370264621a44
reference upload size_bytes: 1049305

SRC-0021
title: Safeguarding LLM Agents from Misalignment through Provenance Analysis
authors: Yining She; Yiliang Liang; Eunsuk Kang
version: arXiv:2607.01236v1
expected pages: 12
reference upload sha256: 66ddafe54cae7a4f1e13e72ba77068eeb6ebc09cbd5e191a6752fbd226ae7968
reference upload size_bytes: 1017348

PIWEK PROXY
title: Imperatives, Commitment and Action: Towards a Constraint-based Model
author: Paul Piwek
year: 2000
version: official JLCL/LDV Forum article or ITRI-00-14 author report
persistent identifier: https://doi.org/10.21248/jlcl.17.2000.21
reference technical-report pages: 16
reference technical-report sha256: b9c15c9b63318ac82efcf5c30ff89f4e994ab09d13f8676d5ade9c8d6a786ff2
reference technical-report size_bytes: 187110
```

For the two arXiv files, stop if the title or version differs. A byte checksum
difference must be investigated and documented before import.

For the Piwek source, the official JLCL article may have different pagination
or bytes from the uploaded ITRI technical report. That is acceptable only if:

- the title and author match;
- the DOI or publication record is verified;
- the exact reviewed version, page convention, checksum, size, and URL are
  recorded honestly;
- it remains a separate proxy/companion source rather than `SRC-0004`.

## Canonical destination paths

After verification, copy the files to:

```text
imports/raw/literature/REV-003B/
  SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf
  SRC-0021_she_liang_kang_2026_arxiv_v1.pdf
  SRC-0036_piwek_2000_imperatives_commitment_action.pdf
```

## Non-substitution rule

The Piwek 2000 report/article is **not** `SRC-0004`, *Situated Action and
Commitment in Dialogue* (1997).

Do not:

- rename the 2000 source as `SRC-0004`;
- overwrite `SRC-0004`;
- claim that the exact 1997 source was reviewed;
- transfer mechanisms from the 1997 citation to the 2000 source.

Use a new stable source ID. At the expected baseline the next unused source ID
appears to be `SRC-0036`; verify this against `data/sources.csv` before
assigning it. If another source has already taken that ID, use the next unused
ID and update the filename consistently.

## Register and provenance tasks

Read:

```text
AGENTS.md
docs/REGISTER_GUIDE.md
schema/registers.json
data/sources.csv
imports/manifest.csv
data/decisions.csv
workflow/batches/REV-003.json
workflow/handoffs/REV-003_scope.md
```

Then:

1. Add import-manifest rows for the three exact PDFs using the next unused
   `IMP-####` IDs.
2. Preserve the source filenames, canonical stored paths, actual SHA-256
   values, sizes, and `application/pdf` media type.
3. Use `full_text_audit_source` or the repository's closest permitted
   authority role.
4. Do not mark any paper `fulltext_verified` merely because the PDF exists.
5. For `SRC-0007` and `SRC-0021`, record exact-full-text availability and
   stored path while preserving Zotero as bibliographic metadata authority.
6. Add the Piwek 2000 source as a new source row using the next unused source
   ID. Record that it is a proxy/companion comparator pending Zotero
   reconciliation.
7. Keep `SRC-0004` as an exact-source access gap. Add a note pointing to the
   new proxy source, but do not change an unreviewed source into an absence
   finding.
8. Record the author's temporary proxy decision in a new role-based decision
   row only if the decision schema supports an operational audit decision.
   Otherwise retain the decision in:
   `workflow/handoffs/REV-003B_piwek_proxy_decision.md`.
9. Create:
   `workflow/handoffs/REV-003B_fulltext_intake.md`
   listing exact versions, URLs, paths, checksums, readiness, and the
   outstanding `SRC-0004` gap.
10. Do not edit proposal prose, prototype code, claims, novelty status, or raw
    Elicit imports.

## Batch-state rule

Do not mark the six-source Tier 1 audit complete.

The source-access state may become:

```text
REV-003B exact full text ready:
- SRC-0007
- SRC-0021

REV-003B proxy full text ready:
- Piwek 2000 new source ID

Still not assessable:
- SRC-0004 exact Piwek 1997 source
```

Preserve:

```text
NOV-0001:
candidate
```

## Validation

Run:

```bash
python scripts/validate_registers.py
python -m unittest discover -s tests -v
git diff --check
```

Report exact files changed, source/import IDs assigned, URLs, checksums,
status changes, validation results, and the remaining `SRC-0004` access gap.

Open a draft pull request titled:

```text
Import REV-003B full texts and Piwek proxy comparator
```

Do not merge automatically.
