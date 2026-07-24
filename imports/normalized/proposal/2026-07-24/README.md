# Proposal source import - 2026-07-24

This directory freezes and inventories the author-supplied Overleaf/RPI LaTeX export without turning the evidence repository into the proposal authority or retaining personal committee identifiers.

## Source control

- Original import: `IMP-0011`
- Original filename: `rpi_pcc_LaTeX.zip`
- Original SHA-256: `52805ac4b32ece8f9bb19dac51e6976e13528fd7dbedc9fe43e45c5d0bcfac61`
- Original size: 1,927,622 bytes
- Original archive inventory: 35 entries, including 31 files and 4 directories
- Original embedded compiled PDF: 666,548 bytes; SHA-256 `354d77ee5ab43caca991fc91b0a744f3ee8602eb38fc0f3a80fc770fc3ea6c4a`

The unmodified archive is checksum-recorded but is not stored in this repository because its front matter contains a personal committee identifier. Overleaf remains authoritative for the source files, figures, and compiled PDF.

## Sanitized analytical derivatives

- `source_inventory.csv` records the path, size, and SHA-256 of every one of the 31 source-export files without storing their content.
- `citation_inventory.csv` records every citation key used by the proposal and every manual bibliography record.
- `IMP-0012` identifies the source inventory as the repository-safe baseline derivative.

A local privacy-sanitized compile test replaced the personal front-matter identifier with the role label `Dissertation Advisor`, reused the original figures, and completed two `pdflatex` passes successfully. The resulting proposal had 47 pages. Neither the sanitized source copy nor compiled derivative is committed here.

## Baseline findings

- The source title is `Pragmatic Commitment Control: Detecting Latent Interpretive Drift in Collaborative Work`.
- The author-confirmed title in the master specification is `Pragmatic Commitment Control: Making Latent Pragmatic Misalignments Observable in Collaborative Work`.
- The title difference is preserved as a baseline finding; the canonical title should be applied in the first controlled Overleaf revision.
- The proposal uses `pages/bib.tex` with a manual `thebibliography` block.
- Proposal prose uses 33 unique citation keys.
- The manual bibliography has 38 records, of which 5 are not currently cited.
- The embedded `sample.bib` has only 8 entries and is not sufficient to replace the manual bibliography.
- Traceability comments were not inserted during baseline import.
