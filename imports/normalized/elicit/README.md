# Normalized Elicit derivatives

These files are deterministic, reviewable derivatives of supplied Elicit workbooks. They are not raw inputs and do not replace the import manifest or the original workbook bytes.

Committed in the initialization stage:

- `claim_source_matrix.csv`
- `initial_full_text_extraction_audit.csv`

Pending a separate binary-capable import stage:

- lossless derivative of the combined Tier 1-Tier 2 capability matrix
- lossless derivative of the Tier 2 authority/workflow audit

The pending workbooks are already checksum-frozen in `imports/manifest.csv`, and their relevant judgments have been represented conservatively in the linked canonical registers. No missing binary content is treated as imported.
