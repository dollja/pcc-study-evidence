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
- Keep Elicit `.bib` snapshots under `imports/raw/` for provenance.
- Validate that every active LaTeX citation key exists after the proposal source is imported.
- Commit the generated `references.bib` only when it is exported from the canonical Zotero collection.

The current `references.bib` is a placeholder because the Zotero export was not supplied.
