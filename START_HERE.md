# Start here

Use this authority order: the [Master Specification](docs/MASTER_SPECIFICATION.md)
and author-confirmed decisions; this evidence repository; Zotero metadata; Overleaf
proposal prose; the prototype repository; then chat history. Chat history is
exploratory and is never current-state authority.

- [Current status](STATUS.md)
- [Evidence-system usage guide](docs/EVIDENCE_SYSTEM_USAGE_GUIDE.md)
- [Register guide](docs/REGISTER_GUIDE.md)
- [Master Specification](docs/MASTER_SPECIFICATION.md)
- [Active batch manifest](workflow/batches/REV-003.json)
- [Latest handoff](workflow/handoffs/REV-003B_fulltext_audit.md)

Validate with:

```bash
python scripts/render_system_status.py
python scripts/validate_registers.py
python -m unittest discover -s tests -v
```

Record an actual merge SHA only after merge. Raw imports are append-only. Novelty
language must never exceed the status and wording supported by the novelty register.
