# Contribution workflow

1. Create a review branch for one bounded change.
2. Add or update raw inputs only through a new dated import path.
3. Update the linked registers in the same pull request.
4. Add LaTeX traceability comments only after the canonical proposal source is present.
5. Run `python scripts/validate_registers.py`.
6. Run `python -m unittest discover -s tests -v`.
7. Summarize evidence added, decisions changed, novelty impact, and unresolved gaps in the pull request.

Do not silently rewrite source descriptions, overwrite raw files, or strengthen novelty wording as part of a prose-only edit.
