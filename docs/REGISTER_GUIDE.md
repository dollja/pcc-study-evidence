# Register guide

## Separation of concerns

- `claims.csv` records atomic dissertation claims.
- `sources.csv` records source identity and metadata status.
- `claim_source_links.csv` records evidentiary and provenance relationships.
- `component_provenance.csv` records what a source contributes to a PCC component and what PCC adopts, changes, or extends.
- `novelty_propositions.csv` records precise proposed deltas.
- `novelty_source_links.csv` records the strongest equivalence threats.
- `searches.csv` records discovery, verification, and disconfirmation searches.
- `decisions.csv` records author/advisor/committee decisions. Decisions are not scholarly evidence.
- `claim_decision_links.csv` connects canonical framing claims to author decisions.
- `prototype_evidence.csv` records reproducible references to prototype revisions,
  commands, results, artifacts, and limitations; it never contains prototype code.
- `claim_prototype_links.csv` relates eligible claims to operational evidence while
  enforcing a wording ceiling.
- `proposal/section_claim_map.csv` maps stable claim IDs to proposal repository,
  LaTeX path, and section-anchor references.

## Record lifecycle

Claims:

`draft -> searched -> abstract_checked -> fulltext_verified -> closest_work_compared -> author_reviewed -> locked -> revised|retired`

Sources:

`discovered -> screened -> included -> coded -> verified -> active -> archived`

Novelty propositions:

`candidate -> provisionally_supported -> challenged -> supported|withdrawn`

Prototype evidence:

`planned -> recorded_unverified -> reproduced -> verified -> superseded`

## Evidence relations

- `DEFINES`
- `SUPPORTS`
- `QUALIFIES`
- `CONTRADICTS`
- `MOTIVATES`
- `SUPPLIES_METHOD`
- `SUPPLIES_MEASURE`
- `ESTABLISHES_BOUNDARY`

## Provenance relations

- `INHERITED`
- `ADAPTED`
- `NEAR_EQUIVALENT`
- `BOUNDARY_CONDITION`
- `METHOD_BORROWED`
- `MOTIVATING`
- `PERIPHERAL`
- `CANDIDATE_NEW_COMBINATION`
- `SUPPORTED_NEW_COMBINATION`

## Prototype-evidence relations and wording ceilings

Claim–prototype relations are `IMPLEMENTS`, `DEMONSTRATES`, `TESTS`,
`PARTIALLY_OPERATIONALIZES`, `ESTABLISHES_LIMITATION`, and
`DOES_NOT_YET_EVALUATE`.

The required wording ceiling is one of `implementation_only`,
`controlled_synthetic_demonstration`, `current_benchmark_result`,
`limitation_only`, or `future_work_only`. These ceilings keep implementation
distinct from demonstration and keep a controlled synthetic demonstration distinct
from evaluation, validation, or generalization. See
`docs/PROTOTYPE_EVIDENCE_GUIDE.md` for entry requirements and examples.

## Source-description rule

Keep two statements distinct:

1. what the source demonstrably says, implements, or evaluates;
2. how PCC interprets that contribution.

Do not translate motivation language into a mechanism claim. Do not code “absent” after a keyword search; use `not_located_after_scoped_review` or `not_assessable` as appropriate.
