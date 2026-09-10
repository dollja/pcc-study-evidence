# Episode-history benchmark development registration

This supplementary activity records the requested local development run and separates four evidence sets. It does not replace workflow/ACTIVE_BATCH (REV-003), close Weeks 1–3, change the Master Specification, or authorize stronger scientific claims.

## Records

- `acs_construction.json`: historical ACS construction; the reported 30 cases are not recounted or rerun here. Exact submitted PDF and source package remain unidentified in this activity.
- `actor_state_construction.json`: separate historical supplied-actor-state construction; reported 36 cases; no new execution or inference claim.
- `independent_pilot.json`: planned independent episode/annotation pilot; no episodes or ratings collected.
- `main_evaluation.json`: planned held-out evaluation; no sample-size freeze, data, execution or findings.
- `development_example.json`: one AI-assisted development source family and 22 passing local checks; never included in pilot or main evaluation.

The manifest schema is proposed. These records are auditable metadata, not an implemented global dataset loader or enforced cross-repository leakage firewall. Unknown historical membership is null rather than fabricated empty membership. Counts are not additive across constructions, prefixes, variants, or tests.

`data/prototype_evidence.csv` adds PEV-0016 and PEV-0017 as recorded_unverified: local commands actually ran, but not from a Git checkout of the imported source commit. PEV-0018 and PEV-0019 remain planned, with empty execution/result/commit fields. No claim-prototype link is added: this activity does not revise the claims or their wording ceilings. Existing PEV records are preserved.

Code and the machine-readable local-run summary are in prototype PR #17, source commit `4f550a323ac30da1c603fcc5264b98d08b157dc3`. No prototype implementation or test data is copied into this evidence repository. Raw execution logs and full replay JSON are retained in the user-delivered execution packet. Artifact checksums and proposed-document statuses are in `artifact_inventory.json`.

## Reproduction and review gates

1. Check out the exact prototype source commit and run the example commands; retain raw outputs, environment, source hashes, limitations and actual checkout state in a new run directory. Run the complete prototype test suite.
2. Only then may PEV-0016/0017 advance to reproduced. A passing development test never advances pilot/main status or proves construct validity.
3. Run `python scripts/render_system_status.py`, `python scripts/validate_registers.py`, and `python -m unittest discover -s tests -v` in the evidence checkout. Do not relabel the whole workflow blocked merely because these supplementary changes await review.
4. Keep both PRs draft until required validation succeeds. Verified status additionally requires the appropriate review. Record a merge SHA only after an actual merge. Preserve prior runs and raw imports.

This registration is not evidence of PCC accuracy, automatic interpretation extraction, private-state recovery, comparative advantage, novelty, or generalization.

## 2026-09-10 evidence-checkout validation

The evidence checkout state and required validation commands were rerun at
`e6f9faf60408100dc811876be764c31884ee74fb`. Their raw stdout, stderr, exit
codes, UTC bounds, environment details, and SHA-256 inventory are retained in
`reports/evidence_validation_20260910/`. This validates the registration's
structure only; it does not reproduce the prototype. The prototype repository
was not present in this environment and its HTTPS connection required
credentials that were unavailable, so PEV-0016 and PEV-0017 remain
`recorded_unverified`; PEV-0018 and PEV-0019 remain `planned`.
