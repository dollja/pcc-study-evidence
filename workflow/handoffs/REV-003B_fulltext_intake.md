# REV-003B full-text intake handoff

## Revision control

- Parent batch: `REV-003`
- Source-intake subtask: `REV-003B-FULLTEXT-INTAKE`
- Actual intake baseline: `a6578af627601b59e0913b2c0e60e8fa0efee6bf`
- Work branch: `codex/import-rev003b-fulltexts-with-piwek-proxy`

## Intake controls

The three append-only raw PDFs committed under `imports/raw/literature/REV-003B/` were used. No network retrieval, DOI redirect, arXiv download, browser retrieval, or Elicit summary was used. Readability, first-page title and author identity, page-object count, byte size, and SHA-256 were checked before register edits.

| Source | Exact version and role | Canonical path | PDF pages | Size (bytes) | SHA-256 |
|---|---|---|---:|---:|---|
| `SRC-0007` | `arXiv:2602.02843v3`; exact full text | `imports/raw/literature/REV-003B/SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf` | 8 | 1049305 | `324b61fb388af4db1de1449fda5308df55d069de4ec1548c4e28370264621a44` |
| `SRC-0021` | `arXiv:2607.01236v1`; exact full text | `imports/raw/literature/REV-003B/SRC-0021_she_liang_kang_2026_arxiv_v1.pdf` | 12 | 1017348 | `66ddafe54cae7a4f1e13e72ba77068eeb6ebc09cbd5e191a6752fbd226ae7968` |
| `SRC-0036` | `ITRI-00-14`; also published in *LDV Forum*; proxy/companion comparator | `imports/raw/literature/REV-003B/SRC-0036_piwek_2000_imperatives_commitment_action.pdf` | 16 | 187110 | `b9c15c9b63318ac82efcf5c30ff89f4e994ab09d13f8676d5ade9c8d6a786ff2` |

Page counts use PDF page objects, including title/front-matter pages, rather than printed page labels. The files were readable PDFs with complete headers/trailers and extractable first-page text matching the expected titles and authors.

## Register assignments and readiness

- `IMP-0016` records the `SRC-0007` PDF.
- `IMP-0017` records the `SRC-0021` PDF.
- `IMP-0018` records the `SRC-0036` PDF.
- `DEC-0018` records the role-based temporary proxy decision.
- `SRC-0007` and `SRC-0021` are exact raw full texts ready for the later bounded full-text audit.
- `SRC-0036` is a proxy raw full text ready for a separate comparator audit, pending Zotero reconciliation.
- PDF presence and intake identity checks do not make any source or finding `fulltext_verified`.

## Outstanding access gap and audit boundary

`SRC-0004` remains the exact 1997 *Situated Action and Commitment in Dialogue* record and is `not_assessable` because its exact full text has not been reviewed. `SRC-0036` is the separate 2000 *Imperatives, Commitment and Action* report; its mechanisms must not be transferred to `SRC-0004`.

The six-source Tier 1 audit remains incomplete. No claims, proposal prose, prototype records, or novelty proposition were changed. `NOV-0001` remains `candidate`.
