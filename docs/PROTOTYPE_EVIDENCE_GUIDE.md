# Prototype evidence guide

## Purpose and boundaries

Prototype-evidence (`PEV`) records make a particular prototype revision, execution,
and observed result traceable without turning this repository into a copy of the
prototype. Prototype code, tests, benchmark inputs, and generated artifacts remain
in the prototype repository. This repository records references to them.

An immutable, full-length commit SHA fixes the exact code revision used by an
execution. A branch name, live deployment, or abbreviated hash can move or be
ambiguous, so a `reproduced` or `verified` record requires a lowercase 40-character
Git SHA (and the validator also permits a 64-character immutable hash). Validation
is deliberately offline: it checks the record, not the remote repository.

## Evidence types

- `implementation` identifies code that implements a capability. It does not show
  that the capability ran successfully.
- `test` identifies an executable check and its observed outcome.
- `machine_readable_output` identifies a retained output artifact from an execution.
- `metric` records a defined measurement produced by a run. A current benchmark
  result is not evidence of generalization.
- `limitation` records an observed or established operational boundary.

A demonstration is expressed by the `DEMONSTRATES` relation rather than by an
evidence type. In particular, implementation is distinct from demonstration, and a
controlled synthetic demonstration is distinct from evaluation, validation, or
generalization.

## Claim links and wording ceilings

`data/claim_prototype_links.csv` connects `CLM` claims to `PEV` records with one of:

- `IMPLEMENTS`
- `DEMONSTRATES`
- `TESTS`
- `PARTIALLY_OPERATIONALIZES`
- `ESTABLISHES_LIMITATION`
- `DOES_NOT_YET_EVALUATE`

Every link also limits permissible prose with one of these wording ceilings:

- `implementation_only`
- `controlled_synthetic_demonstration`
- `current_benchmark_result`
- `limitation_only`
- `future_work_only`

The ceiling prevents evidence from being restated more strongly than the recorded
run warrants. Prototype-only support can satisfy the linkage requirement only for
implementation, methodological, empirical, scope, or limitation claims.
Theoretical, boundary, construct, and novelty claims still require scholarly source
or author-decision linkage.

Prototype evidence is operational evidence, not scholarly evidence: it shows what
a specified revision did, not what the literature establishes. It is also never
novelty evidence. A prototype link cannot promote a novelty proposition or claim to
supported status; novelty remains governed by the novelty audit and decisions.

## Proposal-section traceability

`proposal/section_claim_map.csv` maps stable `CLM` IDs to proposal repository paths
and LaTeX `section_anchor` locations. Once a traceability comment is inserted or
reviewed, the map must identify the proposal repository, immutable proposal commit,
path, and anchor. This maps claims to prose without making this repository
authoritative for proposal prose.

## Lifecycle

The normal lifecycle is:

`planned -> recorded_unverified -> reproduced -> verified -> superseded`

- `planned`: intended evidence, with no claimed execution.
- `recorded_unverified`: an execution has been reported but not reproduced from the
  recorded command.
- `reproduced`: the exact command was rerun at the immutable commit and its result
  and limitations were recorded.
- `verified`: the reproduced evidence received the repository's required review.
- `superseded`: retained for history after a newer record replaces its use.

A live Streamlit screenshot is supplementary because it can document presentation
at a moment in time but does not identify the executable revision, exact command,
machine-readable result, or limitations. The primary evidence is the reproducible
record tied to code and retained output; screenshots may be referenced as an
additional artifact.

## Illustrative records

The following examples are documentation only and are not canonical register rows:

```csv
prototype_evidence_id,prototype_repository,commit_sha,evidence_type,verification_status
PEV-9999,example/prototype,aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,implementation,planned
```

```csv
link_id,claim_id,prototype_evidence_id,relation,wording_ceiling
CPE-9999,CLM-9999,PEV-9999,DEMONSTRATES,controlled_synthetic_demonstration
```

```csv
map_id,proposal_path,section_anchor,claim_id,claim_role,traceability_status
SCM-9999,proposal.tex,sec:placeholder,CLM-9999,method,planned
```
