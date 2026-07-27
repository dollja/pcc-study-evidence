# Import policy

Raw inputs are immutable and append-only.

1. Store a new dated snapshot under `imports/raw/<system>/<date>/`.
2. Record the original filename, repository path, SHA-256, size, media type, and authority role in `imports/manifest.csv`.
3. Never overwrite an existing raw path. A corrected or later export receives a new dated path and import ID.
4. Keep normalized CSV/text derivatives under `imports/normalized/`.
5. Record exact duplicates in the manifest using `duplicate_of`; do not store duplicate bytes.
6. Do not promote Elicit BibTeX into `bibliography/references.bib`. Zotero remains authoritative.
7. Do not treat abstract-only extraction as full-text verification.

The raw files in this import are literature-synthesis outputs, not copies of the underlying papers.

Binary PDFs and workbooks listed as `checksum_recorded_pending_binary_import` must be added in a later binary-capable import commit without changing their import IDs or hashes.
