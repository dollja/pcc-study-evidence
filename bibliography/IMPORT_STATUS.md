# Bibliography import status

The proposal source export is checksum-frozen and inventoried. Its current LaTeX source uses a manual `thebibliography` block in `pages/bib.tex`; it does not yet use the authoritative Better BibTeX workflow.

## Current inventory

- unique citation keys used in proposal prose: **33**
- manual `\bibitem` records: **38**
- cited keys missing from the manual bibliography: **0**
- manual records not currently cited: **5**
- citation keys covered by the supplied `sample.bib` fragment: **8/33**
- supplied capability-matrix fragment entries: **10**
- previously imported starter-corpus entries: **35**

The standalone `sample.bib` is byte-for-byte identical to the copy embedded in the proposal export. Cross-fragment DOI/title matches are recorded in `imports/normalized/bibliography/dedup_report.csv`.

## Authority decision

These files are import fragments, not yet the authoritative `bibliography/references.bib`. The capability-matrix and starter-corpus fragments use opaque Elicit keys, and `sample.bib` covers only part of the proposal. The controlled path remains:

```text
import fragments -> Zotero duplicate review and metadata correction
                 -> Better BibTeX export with stable keys
                 -> bibliography/references.bib
                 -> LaTeX conversion in a separate review stage
```

No raw fragment is silently overwritten, and no Elicit metadata is promoted to Zotero authority by this import.

## Current proposal-source note

The source still carries the pre-canonical title `Pragmatic Commitment Control: Detecting Latent Interpretive Drift in Collaborative Work`. The author-confirmed title in the master specification remains authoritative and should be applied in the first controlled proposal revision rather than during baseline import.
