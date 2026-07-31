# REV-003B raw full-text intake

Upload the three exact PDF files to this directory on branch
`codex/stage-rev003b-fulltext-intake-package` using these canonical names:

```text
SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf
SRC-0021_she_liang_kang_2026_arxiv_v1.pdf
SRC-0036_piwek_2000_imperatives_commitment_action.pdf
```

Expected controls:

| File | Pages | Size (bytes) | SHA-256 |
|---|---:|---:|---|
| `SRC-0007_tsvilodub_et_al_2026_arxiv_v3.pdf` | 8 | 1049305 | `324b61fb388af4db1de1449fda5308df55d069de4ec1548c4e28370264621a44` |
| `SRC-0021_she_liang_kang_2026_arxiv_v1.pdf` | 12 | 1017348 | `66ddafe54cae7a4f1e13e72ba77068eeb6ebc09cbd5e191a6752fbd226ae7968` |
| `SRC-0036_piwek_2000_imperatives_commitment_action.pdf` | 16 | 187110 | `b9c15c9b63318ac82efcf5c30ff89f4e994ab09d13f8676d5ade9c8d6a786ff2` |

The Piwek 2000 report is a proxy/companion comparator. It is not `SRC-0004`,
and it must not be used to claim that the exact 1997 paper was reviewed.

After all three files are present, run the repository-local prompt:

```text
workflow/prompts/REV-003B/01_PREFILLED_IMPORT_PROMPT.md
```

That prompt prohibits network downloads and requires Codex to inspect these
committed raw PDFs.
