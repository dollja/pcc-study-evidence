# Import REV-003B raw full texts and Piwek proxy

Run this only after the raw-PDF staging pull request has been reviewed and
merged into `main`.

Use the Codex environment connected to:

```text
dollja/pcc-study-evidence
```

Use **Code mode** from:

```text
main
```

Codex should create the bounded work branch:

```text
codex/import-rev003b-fulltexts-with-piwek-proxy
```

## Critical source rule

Use the raw PDF files committed to this repository. Do **not** use `curl`,
browser retrieval, agent internet, arXiv downloads, DOI redirects, or Elicit
summaries.

The required repository paths are:

```text
imports/raw/literature/REV-003B/
  SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf
  SRC-0021_she_liang_kang_2026_arxiv_v1.pdf
  SRC-0036_piwek_2000_imperatives_commitment_action.pdf
```

Before doing any register work, run:

```bash
set -euo pipefail

for file in \
  imports/raw/literature/REV-003B/SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf \
  imports/raw/literature/REV-003B/SRC-0021_she_liang_kang_2026_arxiv_v1.pdf \
  imports/raw/literature/REV-003B/SRC-0036_piwek_2000_imperatives_commitment_action.pdf

do
  test -f "$file"
done

file imports/raw/literature/REV-003B/*.pdf
sha256sum imports/raw/literature/REV-003B/*.pdf
```

If any file is missing, stop with:

```text
BLOCKED_RAW_PDF_NOT_COMMITTED
```

List the exact missing repository path. Do not attempt a network download and
do not substitute an abstract or metadata record.

## Revision control

```text
PARENT BATCH:
REV-003

SOURCE-INTAKE SUBTASK:
REV-003B-FULLTEXT-INTAKE

HISTORICAL PRE-INTAKE BASELINE:
bb4788ed2065a531ca165bf7ef3c0bdbb92ad912

TARGET WORK BRANCH:
codex/import-rev003b-fulltexts-with-piwek-proxy
```

Before editing, run:

```bash
git status --short
git rev-parse HEAD
```

The tree must be clean. Record the actual current `main` SHA as the source
intake baseline. It will be newer than the historical baseline after the
raw-PDF staging PR merges. Do not reset or discard newer reviewed work.

## Verify the exact source files

Expected file controls:

```text
SRC-0007
canonical path:
imports/raw/literature/REV-003B/SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf

title:
Act or Clarify? Modeling Sensitivity to Uncertainty and Cost in Communication

authors:
Polina Tsvilodub; Karl Mulligan; Todd Snider; Robert D. Hawkins; Michael Franke

version:
arXiv:2602.02843v3

pages:
8

sha256:
324b61fb388af4db1de1449fda5308df55d069de4ec1548c4e28370264621a44

size_bytes:
1049305

SRC-0021
canonical path:
imports/raw/literature/REV-003B/SRC-0021_she_liang_kang_2026_arxiv_v1.pdf

title:
Safeguarding LLM Agents from Misalignment through Provenance Analysis

authors:
Yining She; Yiliang Liang; Eunsuk Kang

version:
arXiv:2607.01236v1

pages:
12

sha256:
66ddafe54cae7a4f1e13e72ba77068eeb6ebc09cbd5e191a6752fbd226ae7968

size_bytes:
1017348

PIWEK PROXY
canonical path:
imports/raw/literature/REV-003B/SRC-0036_piwek_2000_imperatives_commitment_action.pdf

title:
Imperatives, Commitment and Action: Towards a Constraint-based Model

author:
Paul Piwek

year:
2000

version:
ITRI-00-14 technical report; also published in LDV Forum

pages:
16

sha256:
b9c15c9b63318ac82efcf5c30ff89f4e994ab09d13f8676d5ade9c8d6a786ff2

size_bytes:
187110
```

Verify:

1. each file is a readable PDF;
2. page 1 title and author identity;
3. page count;
4. byte size;
5. SHA-256 checksum.

Stop if any identity or checksum differs. Do not silently normalize or replace
a source.

## Non-substitution rule

The Piwek 2000 report is **not** `SRC-0004`, *Situated Action and Commitment
in Dialogue* (1997).

Do not:

- rename the 2000 report as `SRC-0004`;
- overwrite `SRC-0004`;
- claim that the exact 1997 source was reviewed;
- transfer mechanisms attributed to the 1997 source to the 2000 report.

Use a new stable source ID. At the historical baseline the next unused source
ID appeared to be `SRC-0036`; verify this against the current
`data/sources.csv` before assigning it. If that ID is no longer unused, use the
next unused source ID and rename the committed file consistently in the same
PR.

`SRC-0004` must remain an exact-source access gap and be coded
`not_assessable` for mechanisms that require its full text.

## Read before editing

Read:

```text
AGENTS.md
README.md
docs/REGISTER_GUIDE.md
schema/registers.json
data/sources.csv
imports/manifest.csv
data/decisions.csv
workflow/batches/REV-003.json
workflow/handoffs/REV-003_scope.md
```

## Register and provenance tasks

1. Add import-manifest rows for the three committed PDFs using the next unused
   `IMP-####` IDs.
2. Record original filename, canonical stored path, SHA-256, size,
   `application/pdf`, import status, authority role, and limitations.
3. Use `full_text_audit_source` or the repository's closest permitted authority
   role.
4. Do not mark a paper `fulltext_verified` merely because its PDF is present.
5. For `SRC-0007` and `SRC-0021`, update retrieval notes to record exact raw
   full-text availability and canonical stored path while preserving Zotero as
   bibliographic metadata authority.
6. Add the Piwek 2000 report as a new source row using the next unused stable
   source ID. Record it as a proxy/companion comparator pending Zotero
   reconciliation.
7. Keep `SRC-0004` as an exact-source access gap. Its note may point to the new
   proxy source, but the two records must remain distinct.
8. Record the author's temporary proxy decision in a role-based decision row
   only if the decision schema supports an operational audit decision.
   Otherwise create:

   ```text
   workflow/handoffs/REV-003B_piwek_proxy_decision.md
   ```

9. Create:

   ```text
   workflow/handoffs/REV-003B_fulltext_intake.md
   ```

   Include exact versions, paths, checksums, page conventions, readiness, and
   the outstanding `SRC-0004` access gap.
10. Do not edit proposal prose, prototype code, claims, novelty status, or raw
    Elicit imports.

## Batch-state rule

Do not mark the six-source Tier 1 audit complete during intake.

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

Confirm:

- the three PDF checksums match;
- no network access was used;
- no raw import was overwritten;
- no source was marked full-text verified before the audit;
- `SRC-0004` remains distinct and not assessable;
- no claim, novelty proposition, proposal file, or prototype file changed;
- no personal advisor or committee identifier was introduced.

## Deliverable

Report:

- actual starting `main` SHA;
- exact files changed;
- source and import IDs assigned;
- all three paths, checksums, sizes, and page counts;
- source-status changes;
- validation results;
- the remaining `SRC-0004` access gap.

Open a draft pull request titled:

```text
Import REV-003B raw full texts and Piwek proxy comparator
```

Do not merge automatically.
