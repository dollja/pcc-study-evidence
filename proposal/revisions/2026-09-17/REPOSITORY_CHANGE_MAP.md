# Proposal formatting and repository change map

Date: 17 September 2026. Status: reviewable proposal revision and supplementary mapping; no approval, merge, benchmark result, or evidence-status promotion.

## Baselines checked

| Repository | Main commit | Relevant open drafts |
| --- | --- | --- |
| [Evidence](https://github.com/dollja/pcc-study-evidence) | `d5968b784ea7b52d258501d032d2684b6501ddb2` | #39 candidate acceptance; #40 and #41 overlapping Stage 1 records; #37 development registration |
| [Proposal](https://github.com/dollja/pcc-proposal-latex) | `a73275c9675eccf303d588229371a7d198b4a2e3` | #8 Related Work at `94c68bed550b98aa717ce35855a29f5959f32cb7` |
| [Prototype](https://github.com/dollja/interpretive-drift-protoype) | `a2a844a74a9bf0fcb0b8ddb0f4d1e2e84026418b` | #17 episode-history source at `4f550a323ac30da1c603fcc5264b98d08b157dc3`; #19 blocked reproduction record |

The evidence workflow remains REV-003. STATUS and the batch manifest agree that Chapter 2 revision is ready, while closure remains unstarted. The present user request authorizes a broader proposal repackaging and cross-repository map; it does not close or overwrite that existing batch. Direct Git checkout was unavailable; source and record inspection used commit-pinned GitHub connector snapshots. This is not a full checkout reproduction.

## Formatting applied

The supplied `Proposal_Jacky_v3 (2).zip` is the visual reference. The revised source restores its one-inch geometry, 12-point type, red chapter headings, dark section headings, blue subheadings, compact heading spacing, caption treatment, numbered references, gray/tan callout definitions, listing style, and running-header design. The current title, revised argument, draft date, and status boundaries are preserved. The legacy `thesis.cls` remains byte-identical to the attachment. Scalable Latin Modern fonts, URL wrapping, and revised-text macros are retained for reliable compilation. The running header is reapplied after front matter because the class resets the page style. Generic committee labels are placeholders, not confirmations of membership.

The downloadable title page keeps the supplied adviser information. The repository derivative uses role labels, as required by its AGENTS.md. No private front matter is committed.

## Mapping and ownership

| Change | Proposal location | Evidence repository responsibility | Prototype implication |
| --- | --- | --- | --- |
| Operational target versus actual LPM | Abstract; Chapters 1 and 3 | Resolve Stage 1 draft register dependencies; retain CLM-0024/0025 definitions | Separate observable warrant from actor-state hypotheses |
| Warrant, authority, version, cutoff, and repair | Chapter 3; Appendix A | Review rule/codebook specification; no empirical promotion | Replace or isolate heuristic gating for the evaluated path; retain event history |
| Grounding, planning, workflow and provenance comparison | Chapter 2; references | Reconcile source IDs/Zotero and PR #8; keep NOV-0001 candidate | Workflow checker must be a genuine comparator |
| Supplied-state and automatic-state conditions | Chapters 3–4 | Record scope decision once resolved; preserve planned PEV-0018/0019 | Inputs contain facts/evidence, not gold warrant; bounded extraction remains proposed |
| Independent pilot, three freezes, family splits | Chapter 4 | Keep AI authorship, author acceptance, independent review and annotations separate | Version evidence packets and withheld labels; implement declared metrics |
| Conditional human utility and Weeks 3–6 | Chapters 4–6 | Committee/institutional scope still pending | No measured human benefit is implied by an interface |
| Historical constructions and development example | Appendix A | Keep distinct source/evidence identities and status | Do not pool ACS30, actor-state36, AI candidate30, or the one development history |

`REPOSITORY_CHANGE_MAP.csv` provides 14 detailed rows. Identifiers in its `related_records` column identify related scope or provenance, not blanket proof for every sentence. `PARAGRAPH_TRACEABILITY.csv` ties individual prose anchors to proposed review categories. `CITATION_REGISTER_MAP.csv` exposes references that still lack a matching source-register record. Existing SCM rows remain untouched: changed source anchors require review before an immutable merged proposal commit can replace planned mappings.

## Draft-record collisions requiring reconciliation

1. Evidence PR #39 at `9f2fa2264247e524af156e3af2d5f2dddd4f92bd` uses DEC-0025 for author acceptance of the 30 AI-authored candidates.
2. PR #40 at `f78715031cdaa00ee26e768e7d8223fafab1fdd3` uses DEC-0025 for the core target, adds DEC-0026–0028, and uses CLM-0036 for five task-level warrant labels.
3. PR #41 at `c997a1212bb7523911d7ea5dc256b8e8d51ca0bc` uses DEC-0025 for the paired claim boundary and CLM-0036 for the stronger-LPM evidence requirement.

These are conflicting draft allocations, not interchangeable aliases. The proposal follows the delivered Stage 1 v0.1.0/PR #41 wording and qualifies those identifiers by commit. It does not renumber stable IDs, select a canonical merged winner, or close another draft. Reconcile the competing drafts with a retained alias/history record before merging them together. PR #39's author acceptance is not independent material approval.

## Relationship to proposal PR #8

The new whole-proposal draft overlaps PR #8 in Chapter 2 and bibliography. It is a candidate integration for review, not an automatic replacement of that PR. Its clearer explanatory order differs from CLM-0027's recorded seven-part chapter architecture; architecture retention or amendment must be resolved explicitly (the existing architecture claim is CLM-0027, with DEC-0022/0023 governing section boundaries). Retain the audited affirmative comparator overlap and the uncertainty/cost-sensitive clarification account during that review. No existing SCM-0022–0045 row is marked complete. The source-register wording ceiling and candidate novelty status continue to apply.

## Concrete prototype follow-up

The following locators were inspected at `a2a844a74a9bf0fcb0b8ddb0f4d1e2e84026418b`. They identify future implementation work, not modifications made by this formatting task.

- `schemas.py::ScenarioCase` contains `control` and desired-output fields; the evaluated input contract must exclude reference/control labels. `detector.py::_detect_commitment_control` and several baseline paths currently use `case.control` to suppress output.
- `commitment_gate.py::gate_recommendation` uses a weighted maxim/risk profile with allow/warn/clarify/hold recommendations. That computation does not implement the proposed rule-specific, three-valued warrant judgment. A new audit path needs explicit requirements, alternatives, authority, versions, and event deadlines.
- `extraction_schemas.py::VariableCandidate` and `variable_extractor.py` use Step 1 flag/reject/abstain decisions. Preserve these historical interfaces while clearly separating candidate selection from a final operational-event finding.
- `detector.py::detect_transcript_only_placeholder`, `detect_first_order`, and `detect_ambiguity_assessment` call the main detector and weaken its output. They do not supply the independently implemented workflow and consequence-only comparisons proposed here.
- `evaluator.py` needs a separate declared evaluation for target-event decisions, false alarms, uncertainty/coverage, source-family splits, and annotation disagreements before the main experiment. Existing metrics are not relabeled.
- PR #17's `research_examples/episode_history/` provides a separate supplied-state reference example. Its PEV-0016/0017 records remain `recorded_unverified`; source existence in an open branch is not main-branch reproduction.

No prototype source is changed, no new prototype PR is needed for a formatting/mapping task, and no prototype test run is claimed. These items are ready to guide a later implementation stage.

## Suggested integration sequence

1. Review the reformatted proposal and this map. Reconcile evidence #39/#40/#41 identifier collisions and the intended Chapter 2 integration with proposal #8.
2. Register any newly accepted claims/decisions and reconcile citation metadata before promoting draft traceability to canonical mappings. Preserve provenance and superseded records.
3. Merge only reviewed proposal content, then record its actual immutable merge commit in the evidence section map. An open draft commit is not a merge SHA.
4. Implement the agreed audit input contract and credible baselines in the prototype. Run its complete suite and record exact immutable execution evidence separately.
5. Collect independent pilot judgments, resolve scope, and freeze the protocol. Keep PEV-0018/0019 planned until real study evidence exists.
