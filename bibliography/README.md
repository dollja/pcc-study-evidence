# Bibliography workflow

Authority chain:

```text
Zotero canonical collection
        -> Better BibTeX automatic export
        -> bibliography/references.bib
        -> Overleaf proposal
```

Rules:

- Correct metadata in Zotero, not in the exported `.bib`.
- Use stable Better BibTeX citation keys.
- Do not hand-merge Elicit BibTeX into the authoritative export.
- Keep Elicit and pre-export `.bib` fragments under `imports/raw/` for provenance.
- Review duplicates in Zotero by DOI, normalized title, and version relationship.
- Validate that every active LaTeX citation key exists after the proposal source is converted.
- Commit `references.bib` only when it is exported from the canonical Zotero collection.

Current status:

- the proposal source is checksum-frozen and inventoried;
- its manual bibliography contains all 33 citation keys currently used in prose;
- the supplied `sample.bib` covers only 8 of those keys and is identical to the copy embedded in the proposal export;
- the capability-matrix BibTeX fragment contains 10 Elicit-keyed entries and overlaps the previously imported starter corpus; and
- `bibliography/references.bib` remains a placeholder because a complete, deduplicated Better BibTeX export has not yet been supplied.

See `bibliography/IMPORT_STATUS.md` and `imports/normalized/bibliography/dedup_report.csv`.
