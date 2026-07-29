# REV-002 prototype-evidence archive

This directory contains an immutable, multipart base64 representation of:

```text
REV-002-evidence-c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4.zip
```

The archive was supplied for the guarded REV-002 prototype-evidence finalization task in `dollja/pcc-study-evidence`.

## Identity

- Prototype repository: `dollja/interpretive-drift-protoype`
- Prototype commit represented by the archive: `c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4`
- Prototype pull request: `#15`
- Decoded ZIP size: `40540` bytes
- Decoded ZIP SHA-256: `b13361c994ba522595f97a654e53ef08fb4bd66c7982503664fe14dd048f8d6c`
- ZIP entries: `65`
- Extracted regular files: `47`
- Content type: repository-owned Markdown, JSON, and CSV evidence artifacts only

No prototype source code is copied into this evidence repository.

## Reconstruct and verify in Codex

From the evidence-repository root, run:

```bash
bash imports/raw/prototype/2026-07-29/restore_rev002_evidence_archive.sh
```

The script:

1. concatenates parts `00` through `07` in lexical order;
2. base64-decodes the exact ZIP to `/tmp`;
3. verifies the supplied SHA-256;
4. tests the ZIP structure;
5. extracts the package to `/tmp/REV-002-evidence-c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4`.

The Prompt C task may then inspect:

```text
/tmp/REV-002-evidence-c9a38d833de1262cc2a8be0bdaaa1ee9ba777ed4/evidence/runs/REV-002/
```

## Evidence boundary

This import makes the exact prototype evidence package available to the evidence-repository task. It does not, by itself:

- assign `PEV` or `CPE` IDs;
- establish scholarly or theoretical support;
- prove novelty;
- authorize `verified` status;
- erase the recorded limitation concerning general second-order chronology for non-adjacent cues.

Prompt C must inspect the individual manifests, commands, results, and limitations before assigning `reproduced`, `recorded_unverified`, `limitation_only`, or other permitted statuses and wording ceilings.
