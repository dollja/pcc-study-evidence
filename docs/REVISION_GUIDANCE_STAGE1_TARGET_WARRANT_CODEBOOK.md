# Revision Guidance Stage 1: Observable Target, Warrant Conditions, and Annotation Codebook

Status: **author-confirmed scope amendment; implementation/evaluation consequences pending later stages**  
Effective date: **2026-09-14**

## 1. Purpose

This stage narrows the dissertation's computational target without discarding its cognitive motivation.

The primary empirical target is now an **interpretation-dependent operational action that lacks the support required by the documented task rules at a specified observation time**.

Actual latent pragmatic misalignment (LPM) remains a separate, stronger claim. The dissertation should test the relationship between the observable operational target and LPM rather than define them as equivalent.

This change is intended to make the benchmark independently annotatable, reduce dependence on inferred private state, and support credible comparisons with workflow/authorization checking while preserving the Theory-of-Mind and pragmatic motivation for why such failures may arise.

## 2. Claim hierarchy

### 2.1 Primary computational claim

At observation time `t`, given only the evidence visible by `t` and the applicable documented task rules, PCC should identify whether an interpretation-dependent operational event is sufficiently supported to proceed.

The core positive case is:

1. an operational event has occurred or is represented as having entered executable/committed task state;
2. the event depends on selecting one interpretation or task-state value rather than another;
3. materially different plausible interpretations imply different downstream actions, permissions, schedules, responsibilities, resources, artifact states, or completion criteria; and
4. the visible record does not contain the support required by the applicable documented task rules for the selected interpretation/value.

This target is **record-relative and time-indexed**. It does not assert that support never existed outside the observation boundary.

### 2.2 Stronger LPM claim

LPM remains the dissertation's cognitive phenomenon of interest: a task-relevant divergence in interpretation, standard, or commitment that remains unrepaired while interaction appears locally coherent.

However, an unsupported operational action is **not sufficient evidence of LPM**. The same operational failure can arise from missing authorization, incomplete documentation, stale context, policy violation, or ordinary process error even when collaborators share the same interpretation.

A stronger LPM annotation therefore requires additional evidence bearing on differing actor interpretations or commitments. The operational target and LPM should be represented with separate labels and evaluated for overlap/association.

### 2.3 Relationship claim to test

The empirical question is whether, and under what conditions, unsupported interpretation-dependent operational actions are associated with independently recognizable LPM.

Possible outcomes include:

- unsupported operational action + LPM evidence;
- unsupported operational action without LPM evidence;
- LPM evidence before any operational action;
- warranted operational action despite lexical/pragmatic ambiguity;
- insufficient evidence to determine either claim.

The dissertation should not force these conditions into a single label.

## 3. Preserve the cognitive motivation

The computational target is deliberately more observable than LPM, but the cognitive framing remains relevant.

Theory of Mind continues to motivate actor-indexed hypotheses about what collaborators appear to understand, expect, or treat as settled. Grounding/common-ground theory continues to motivate the distinction between private inference and public evidence. PCC continues to ask when an interpretation is sufficiently warranted to govern coordinated action.

The key methodological boundary is:

> Actor-indexed or second-order states may help explain or diagnose an operational failure, but they are not required to establish the primary benchmark label unless independently observable evidence supports them.

Thus the dissertation can test whether second-order representation adds diagnostic value without making private-state recovery a prerequisite for the core computational study.

## 4. Observation model

Each episode must define an explicit observation cutoff `t_obs`.

Only evidence available at or before `t_obs` may be used for the primary judgment. Later correction, repair, authorization, or artifact updates must not be back-projected into the earlier state.

Required episode inputs are:

- dialogue/history visible by `t_obs`;
- documented task rules applicable by `t_obs`;
- roles/authority information visible by `t_obs`;
- timestamped artifact/workflow events visible by `t_obs`;
- an explicit operational event, if one has occurred;
- the observation cutoff.

Unknown or unavailable context must remain unknown. Absence of observed support is not automatically evidence that support never existed.

## 5. Warrant conditions

### 5.1 Warrant object

Warrant is evaluated for a specific tuple:

`<episode, operational_event, selected_interpretation_or_value, task_rule, observation_time>`.

A warrant judgment is therefore not a global statement about the conversation.

### 5.2 Warrant labels

Use the following mutually exclusive primary labels:

- `SUPPORTED`: the visible record contains the evidence required by the applicable documented task rules for the selected interpretation/value at `t_obs`.
- `UNSUPPORTED`: an operational event exists, an applicable rule requires support, and the visible record positively shows that the required support is absent, contradicted, insufficient, expired, or supplied by an actor/artifact without the required authority/status.
- `CANNOT_DETERMINE`: the visible record is insufficient to decide whether the required support exists or whether the relevant rule applies. This is epistemic uncertainty, not a negative judgment.
- `NO_OPERATIONAL_EVENT`: no action/artifact/state promotion requiring the warrant judgment has occurred by `t_obs`.
- `OUT_OF_SCOPE`: the episode does not contain an interpretation-dependent operational decision within the benchmark definition.

### 5.3 Conditions for `SUPPORTED`

Annotate `SUPPORTED` only when all required conditions are met:

1. the applicable task rule is identifiable;
2. the operational event and selected task-state value are identifiable;
3. the required supporting evidence is visible by `t_obs`;
4. the evidence comes from a source/actor/artifact recognized as sufficient by the rule;
5. temporal validity, role/authority, artifact status, and required prerequisites are satisfied where applicable.

### 5.4 Conditions for `UNSUPPORTED`

Annotate `UNSUPPORTED` only when all of the following are true:

1. an operational event exists by `t_obs`;
2. an applicable documented rule identifies a support/prerequisite requirement;
3. the event depends on a selected interpretation/value;
4. at least one reasonable alternative interpretation/value would materially change the downstream action, permission, schedule, responsibility, resource use, artifact status, or completion criterion;
5. the visible record shows that the selected value lacks the required support, conflicts with the rule, uses invalid/expired support, or relies on a source without the required authority/status.

Do not use `UNSUPPORTED` solely because the annotator cannot find confirming evidence in an incomplete record.

### 5.5 Conditions for `CANNOT_DETERMINE`

Use `CANNOT_DETERMINE` when any essential adjudication input is unresolved, including:

- missing or ambiguous task rule;
- unclear observation boundary;
- missing role/authority information;
- operational event cannot be located confidently;
- the record may be incomplete and absence cannot be distinguished from nonoccurrence;
- competing interpretations are plausible but their downstream consequences cannot be established;
- evidence is contradictory without a rule for precedence.

### 5.6 Repair timing

Repair must be indexed to the operational event.

Code separately:

- `REPAIR_BEFORE_EVENT`: clarification/correction occurs before the operational event and prevents the unsupported promotion/action.
- `REPAIR_AFTER_EVENT`: clarification/correction occurs after the operational event. The current state may become corrected, but the historical unsupported event remains countable.
- `NO_REPAIR_OBSERVED`: no relevant repair is visible by `t_obs`.
- `REPAIR_STATUS_UNKNOWN`: evidence is insufficient.

A repair of one variable does not automatically clear other warrant failures.

## 6. Annotation order

Annotators should judge task evidence before making cognitive/LPM judgments.

### Pass A: task-level observable judgment

Annotate:

1. `observation_cutoff`
2. `operational_event`
3. `task_variable`
4. `selected_value_or_interpretation`
5. `plausible_alternatives`
6. `material_consequence_difference`
7. `applicable_task_rule`
8. `required_support`
9. `visible_support_evidence`
10. `warrant_label`
11. `warrant_reason_code`
12. `repair_timing`
13. `remaining_uncertainty`

### Pass B: LPM relationship judgment

Only after Pass A, annotate:

1. `lpm_evidence_status`
2. `actor_A_apparent_interpretation`
3. `actor_B_apparent_interpretation`
4. `evidence_for_interpretation_difference`
5. `evidence_of_apparent_uptake_or_second_order_assumption`
6. `surface_coherence_or_local_success`
7. `lpm_relation_to_event`
8. `lpm_confidence`

Annotators must be able to complete Pass A without assigning actor mental states.

## 7. LPM codebook

Use these values for `lpm_evidence_status`:

- `LPM_SUPPORTED`: visible evidence supports materially different task-relevant interpretations/commitments across actors, and the divergence remains unrepaired through the relevant observation window.
- `LPM_POSSIBLE`: evidence suggests divergence but is insufficient to establish materially different actor interpretations/commitments.
- `LPM_NOT_SUPPORTED`: the available evidence supports shared interpretation/commitment or the event is better explained by a non-interpretive process failure.
- `LPM_CANNOT_DETERMINE`: actor-indexed interpretation evidence is insufficient or unavailable.
- `LPM_NOT_APPLICABLE`: no relevant multi-actor interpretive question exists.

Do not infer `LPM_SUPPORTED` from `UNSUPPORTED` alone.

### 7.1 Minimum evidence for `LPM_SUPPORTED`

Require:

1. at least two actor-indexed interpretation/commitment values that are materially incompatible for the task variable;
2. public or artifact evidence supporting each attribution;
3. evidence that the divergence is present before or at the relevant operational event/cutoff;
4. no repair that resolves the divergence before the relevant event when the claim concerns an event caused under divergence.

Second-order evidence such as one actor apparently assuming the other shares an interpretation may strengthen the LPM account but should be coded separately rather than assumed.

## 8. Reason codes

### 8.1 Warrant reason codes

Use one or more:

- `MISSING_REQUIRED_APPROVAL`
- `WRONG_APPROVER_OR_AUTHORITY`
- `REVIEW_NOT_EQUIVALENT_TO_AUTHORIZATION`
- `MISSING_REQUIRED_ARTIFACT_STATE`
- `TEMPORAL_RULE_NOT_SATISFIED`
- `RESOURCE_PRECONDITION_NOT_SATISFIED`
- `COMPLETION_CRITERIA_NOT_SATISFIED`
- `INTERPRETATION_VALUE_NOT_GROUNDED`
- `CONTRADICTORY_VISIBLE_EVIDENCE`
- `STALE_OR_EXPIRED_SUPPORT`
- `RULE_APPLICABILITY_UNKNOWN`
- `RECORD_INCOMPLETE`
- `NO_MATERIAL_ACTION_DIFFERENCE`
- `OTHER_DOCUMENTED_REASON`

### 8.2 LPM relation codes

Use one:

- `LPM_PRECEDES_EVENT`
- `LPM_CONCURRENT_WITH_EVENT`
- `LPM_OBSERVED_WITHOUT_EVENT`
- `EVENT_WITHOUT_LPM_EVIDENCE`
- `LPM_RELATION_UNKNOWN`
- `NOT_APPLICABLE`

## 9. Positive and negative examples

### 9.1 Scheduling: unsupported + possible LPM

Task rule: fiscal-quarter convention governs finance reviews.  
Dialogue: one actor says "Q3"; another schedules September.  
Event: calendar invitation entered for September.  
Visible rule/evidence: fiscal Q3 dates are documented and differ materially from September.

Primary label: `UNSUPPORTED` if the selected September value conflicts with the documented rule and the event is already operational.  
LPM label: only `LPM_SUPPORTED` if actor-indexed evidence shows one actor intended fiscal Q3 and the other acted under calendar Q3; otherwise `LPM_POSSIBLE` or `LPM_CANNOT_DETERMINE`.

### 9.2 Release authorization: unsupported without LPM

Task rule: release requires final sign-off from role R2.  
Both actors agree the release is ready, but actor R1 mistakenly performs release after technical review.

Primary label: `UNSUPPORTED`.  
LPM label: `LPM_NOT_SUPPORTED` if evidence indicates shared interpretation and the failure is authorization/process compliance rather than interpretive divergence.

### 9.3 Completion/handoff: LPM before event

Actor A uses "done" to mean draft complete; Actor B treats it as stakeholder accepted. No handoff or closure event has yet occurred.

Primary label: `NO_OPERATIONAL_EVENT`.  
LPM label: `LPM_SUPPORTED` if the differing completion criteria are evidenced and unrepaired.

### 9.4 Harmless ambiguity

"Schedule the meeting with Finance." Alternatives such as meeting/sync/call do not change the applicable rules or downstream action materially.

Primary label: `OUT_OF_SCOPE` or no candidate after screening.  
LPM label: `LPM_NOT_APPLICABLE` unless independent evidence shows a consequential interpretive divergence.

### 9.5 Missing context

An artifact shows "approved" but the episode omits the authority matrix and there is no reliable rule identifying who can approve.

Primary label: `CANNOT_DETERMINE`.  
Do not convert lack of visible authorization into `UNSUPPORTED` without a documented rule/evidence boundary.

## 10. Consequences for hypotheses and evaluation

The benchmark should support at least two separable outcome families.

### H-core: observable operational target

A detector using explicit consequence and warrant reasoning should identify unsupported interpretation-dependent operational actions under fixed task schemas better than weaker baselines on target-event precision/recall and false alarms on warranted/repaired controls.

This remains a hypothesis until independently authored/annotated evaluation is run.

### H-LPM: relationship to cognitive misalignment

Unsupported operational actions should not be assumed to equal LPM. The study should estimate the association/conditional overlap between the primary warrant label and independently annotated LPM evidence status.

A useful result may show that PCC's operational target is narrower, broader, or only partially overlapping with LPM.

### H-second-order: incremental diagnostic value

Second-order actor-state representation should be tested as an ablation/addition: does it improve LPM discrimination, evidence localization, or diagnostic usefulness beyond task-level warrant checking and first-order state?

This hypothesis preserves the Theory-of-Mind motivation while allowing the dissertation to succeed even if the primary operational detector does not require general second-order state construction.

## 11. Minimum independent benchmark implications

The independently authored pilot should preserve the three current task structures:

- scheduling;
- release authorization;
- completion/handoff.

It must deliberately include:

- `SUPPORTED` operational events;
- `UNSUPPORTED` events;
- `CANNOT_DETERMINE` cases;
- `NO_OPERATIONAL_EVENT` cases with genuine interpretive divergence;
- negative controls with ambiguity but no material action difference;
- repair before event;
- repair after event;
- event-without-LPM cases;
- LPM-without-event cases.

This prevents the benchmark from mechanically equating ambiguity, unsupported action, and LPM.

## 12. Scope ceiling for this stage

This stage does **not** establish:

- that the automatic-state constructor can recover the necessary records from unrestricted natural language;
- that PCC outperforms a workflow/authorization checker or direct classifier;
- that second-order ToM is necessary for the core operational task;
- the prevalence or causal role of LPM in real workplaces;
- human diagnostic benefit;
- novelty or generalization.

Those claims require later stages and independent evidence.

## 13. Stage-1 completion criterion

Stage 1 is complete when the project consistently distinguishes:

1. the **primary observable label**: support status of an interpretation-dependent operational event at a specified observation time;
2. the **warrant basis**: documented task rules plus evidence visible by the cutoff;
3. the **secondary cognitive label**: independently evidenced LPM status;
4. the **testable relationship** between those labels;
5. the **annotation order** that allows the primary benchmark to be judged without private-state inference.
