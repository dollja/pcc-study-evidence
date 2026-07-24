# LaTeX traceability convention

The canonical proposal source has not yet been imported. When it is available, add non-rendering comments immediately before major claim-bearing prose:

```latex
% PCC-CLAIM: CLM-0019
% PCC-EVIDENCE: SRC-0002;SRC-0003
% PCC-DECISION: DEC-0006
% PCC-NOVELTY: NOV-0001
% PCC-STATUS: fulltext_verified
PCC addresses the warrant required to promote an attributed interpretation
into action-guiding coordination commitment.
```

Use only the identifiers that apply. A paragraph may reference multiple claims.

Rules:

1. Comments do not replace citations.
2. `PCC-EVIDENCE` must point to `data/sources.csv`.
3. Novelty-bearing prose must include a `PCC-NOVELTY` identifier.
4. Candidate novelty records may use only cautious wording.
5. When prose changes materially, update the claim register first or in the same pull request.
6. Do not insert traceability comments into generated bibliography files.
