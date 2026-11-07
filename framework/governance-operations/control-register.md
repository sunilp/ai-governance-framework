# Control Register

This register maps every governance control in the framework to its evidence, owner, and escalation path. It is the single source of truth for what evidence an auditor, regulator, or compliance team should expect. Controls are grouped by the stages of the [governance workflow](governance-workflow.md), using the same stage numbers and names. "Applies To" names the tiers explicitly and matches the workflow's tier tables.

A control can only be bypassed through an approved exception: see [Exceptions and Risk Acceptance](governance-workflow.md#exceptions-and-risk-acceptance). Some controls are non-waivable.

For the end-to-end process connecting these stages, see [governance-workflow.md](governance-workflow.md). For a worked example, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md#control-coverage). It shows the evidence for every control that applies to that T1 GenAI RAG system and lists the controls that do not apply, with reasons.

## Stage 1: Idea Intake

No register controls. Intake produces pre-register artifacts only (intake form and initial risk screening); see workflow Stage 1.

## Stage 2: Risk Assessment & Tiering

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RA-001 | Risk assessment completed using framework matrices | T1-T4 | Product owner | Signed risk assessment with dimension scoring + tier determination | Before development begins | Cannot proceed to development |
| RA-002 | Tier override review against the canonical override list | T1-T4 (any system matching an override trigger, automatic T1 or minimum T2) | AI Risk | Override decision document | At assessment | Escalate to AI Risk Committee |
| RA-003 | Impact assessment completed | T1-T2 (T3: recommended) | Product owner | Completed impact assessment template | Before development | Cannot proceed to development |
| RA-004 | Risk assessment approved by appropriate authority | T1-T4 | AI Risk Committee (T1) / AI Risk, second line (T2) / Team lead (T3, T4: acknowledges self-assessment) | Approval record with sign-off | Before development | Block progression |
| RA-005 | DPIA screening and, where required, full DPIA | T1-T4 processing personal data: screening for all; full DPIA always for T1-T2 and wherever screening indicates high risk | DPO | DPIA screening record; filed DPIA with DPO sign-off where required | Before development | Cannot proceed; escalate to DPO |

## Stage 3: Architecture & Design Review

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| AR-001 | System architecture documented | T1-T4 | Technical owner | Architecture document with component diagram and data flows | Before development | Block development |
| AR-002 | Architecture review sign-off | T1 (review board); T2 (team-level design review) | Architecture review board (T1) / Head of AI or delegate (T2) | T1: review board meeting record with decision and conditions. T2: recorded team-level design review approved by the Head of AI or delegate | Before development | Cannot proceed without sign-off |
| AR-003 | Data residency confirmed | T1-T4 with external data flows | Technical owner | Data flow map with residency confirmation per jurisdiction | Before development | Escalate to compliance |
| AR-004 | Vendor/model selection justified and approved | T1-T4 using external models | AI lead | Model selection document with evaluation results and rationale; approval by AI Risk Committee + CISO (T1), Head of AI (T2), team lead from the approved vendor list (T3/T4) | Before development | Block development |
| AR-005 | Third-party model risk assessment completed | T1-T3 using external vendor APIs (T4: approved vendors only, no separate assessment) | AI Risk | Completed vendor risk assessment | Before development; annually thereafter | Block deployment; procurement escalation |

## Stage 4: Development & Prompt Engineering

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DE-001 | Model card created and version-controlled | T1-T4 | AI lead | Model card in version control ([LLM model card](../../templates/llm-model-card.yaml) for GenAI) | Before validation | Block validation gate |
| DE-002 | Prompts version-controlled | T1-T4 GenAI | AI lead | Prompt files in git repository with commit history | Continuous | Block deployment |
| DE-003 | Prompt review completed per tier | T1-T3 GenAI (T3: peer review only; T4: self-review) | AI lead | Signed prompt review checklist + prompt version link. Reviewers: T1 peer review + prompt engineering lead + security review + AI Risk sign-off; T2 peer review + prompt engineering lead; T3 peer review | Before release | Block deployment |
| DE-004 | Guardrails implemented and configured | T1-T2 GenAI (T3: recommended) | Technical owner | Guardrail configuration document + test results | Before deployment | Block deployment |
| DE-005 | Data governance controls applied to training/fine-tuning data | T1-T3 using fine-tuned models (T4: recommended) | AI lead | Data governance checklist with provenance documentation | Before training | Block training |

## Stage 5: Evaluation & Testing

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| EV-001 | Pre-release evaluation suite executed | T1-T4 | AI lead | Evaluation report with pass/fail per metric | Before every deployment | Block deployment |
| EV-002 | Safety evaluation passed | T1-T4 GenAI (T4: automated, 20+ cases) | AI lead | Safety eval results meeting tier thresholds | Before every deployment | Block deployment |
| EV-003 | Regression evaluation passed | T1-T2 on model/prompt change (T3: recommended) | AI lead | Regression report comparing current vs. previous version | On change | Block deployment if regression detected |
| EV-004 | RAG retrieval quality evaluated | T1-T3 RAG systems (T4: recommended) | AI lead | Retrieval precision/recall/relevance metrics | Before deployment; then weekly (T1), monthly (T2), quarterly (T3) | Block deployment (pre-release); investigate (production) |
| EV-005 | Bias evaluation completed | T1-T2 (T3: recommended) | Responsible AI lead | Counterfactual test results with demographic parity metrics | Formal evaluation before deployment, then quarterly (T1) or semi-annual (T2); production counterfactual spot-checks weekly (T1) or monthly (T2) | Block deployment; escalate to Responsible AI |
| EV-006 | Eval dataset integrity verified | T1-T4 | AI lead | Confirmation of no overlap with training data; dataset version recorded | Before each eval run | Invalidate eval results; re-run |
| EV-007 | LLM-as-judge calibrated against human evaluators | T1-T2 using automated eval | AI lead | Calibration report with correlation scores | Quarterly (T1); semi-annually (T2) | Pause automated eval; revert to human eval |

## Stage 6: Security Review & Red-Teaming

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| SR-001 | Red-team testing completed per tier depth | T1-T3 GenAI (T4: automated scan recommended) | Security / AI Risk | Red-team report. Depth: T1 200+ cases including manual testing; T2 100+; T3 automated scan + 50 manual cases | Pre-deployment; per [red-teaming protocol](../ai-security/red-teaming-protocol.md) cadence | Block deployment |
| SR-002 | No unresolved Critical or High findings | T1-T2: 0 Critical, 0 unaddressed High. T3-T4: 0 Critical (High needs recorded risk acceptance) | System owner | Red-team report showing 0 Critical and, for T1-T2, 0 unaddressed High | Before deployment | Block deployment. Unresolved Critical findings cannot be excepted |
| SR-003 | Adversarial robustness defenses implemented | T1-T2 GenAI (T3: recommended) | Technical owner | Defense configuration documentation | Before deployment | Block deployment |
| SR-004 | Supply chain security verified | T1-T3 using open-source models (T4: recommended) | Security | AI-BOM + provenance verification | Before deployment; on model change | Block deployment |

## Stage 7: Deployment Approval

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DA-001 | Evidence pack assembled and complete | T1-T4 | Product owner | Evidence checklist against the [minimum evidence pack](governance-workflow.md#minimum-evidence-pack-by-tier) | Before deployment | Block deployment |
| DA-002 | Sign-off chain completed per tier | T1-T4 | Product owner | Signed deployment approval record. Approvers: T1 AI Risk Committee + CISO (+ DPO if personal data is processed); T2 Head of AI + Business Unit Head; T3 team lead + business owner; T4 team lead | Before deployment | Block deployment |
| DA-003 | Deployment gates passed | T1-T4 | AI Operations | Gate evidence package | Before deployment | Block deployment |
| DA-004 | Rollback plan documented and tested | T1-T2 | Technical owner | Rollback procedure + test evidence | Before deployment | Block deployment |

## Stage 8: Production Operations

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| PM-001 | Monitoring configured per tier requirements | T1-T4 (T4: basic usage and error monitoring) | AI Operations | Monitoring configuration + dashboard reference | Before traffic enabled | Block go-live |
| PM-002 | Alerting active with defined thresholds | T1-T3 (T4: covered by platform-level budget alerts) | AI Operations | Alert configuration evidence | Before traffic enabled | Block go-live |
| PM-003 | Human oversight operational | T1-T2 | Product owner | Oversight process document per the [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) + staffing confirmation | Before traffic enabled | Block go-live |
| PM-004 | Production evaluation running per cadence | T1-T4 | AI Operations | Schedule and latest results for online automated scoring, metrics review and full offline suite re-run | Per tier cadence (workflow Stage 8) | Escalate to AI Risk; increase monitoring |
| PM-005 | Cost monitoring active | T1-T3 (T4: covered by platform-level budget alerts) | AI Operations | Cost dashboard + alert configuration | Before traffic enabled | Block go-live |

### Stage 8 sub-group: Incident Response

Severity, response SLAs and notifications: [escalation paths](../operating-model/escalation-paths.md#severity-classification).

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| IR-001 | Incident response playbook documented | T1-T2 | AI Operations | Published runbook accessible to on-call | Before deployment | Block deployment |
| IR-002 | On-call team assigned | T1-T2 | AI Operations | On-call rotation schedule | Continuous | Escalate to AI Platform Lead |
| IR-003 | Incident reported and handled per severity SLA | T1-T4 (on incident) | Incident commander | Incident report per template, with root cause: S1/S2 within 48 hours, S3 within 10 business days | Per incident. Response SLA by severity: S1 15 minutes, S2 4 hours, S3 24 hours, S4 next business day | Escalate per escalation paths |
| IR-004 | Post-mortem completed for S1/S2 incidents | T1-T4 (S1 and S2 incidents) | Incident commander | Post-mortem report | Within 1 week (S1) / 2 weeks (S2) | Escalate to AI Risk Committee |
| IR-005 | Remediation actions tracked to completion | T1-T4 (incidents with remediation actions) | System owner | Remediation tracker with status; S4 items tracked in the backlog | Until complete | Escalate to AI Risk |

## Stage 9: Ongoing Governance

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RV-001 | Formal governance review completed | T1-T4 | System owner | Review record with findings, actions and risk re-assessment (re-tiering check) | Quarterly (T1); semi-annual (T2); annual (T3); annual self-assessment (T4) | Overdue review flagged in governance metrics; escalate after 30 days |
| RV-002 | Model card updated | T1-T4 | AI lead | Updated model card with current information | At each review | Block until updated |
| RV-003 | Revalidation on material change | T1-T4 | AI lead | Revalidation assessment + eval results | On model change, provider update, prompt change, or regulatory change. Independent revalidation also annual (T1) and every 24 months (T2) | Re-enter deployment gates |
| RV-004 | Regulatory change impact assessed | T1-T3 (T4: recommended) | Compliance | Regulatory change impact assessment | On regulatory change | Escalate to AI Risk Committee |

## Stage 10: Deprecation & Retirement

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DR-001 | Deprecation impact assessment completed | T1-T4 systems being deprecated | System owner | Impact assessment with affected systems and migration plan | At deprecation trigger | Block deprecation without assessment |
| DR-002 | Migration governance followed | T1-T2 systems being replaced (T3: recommended) | AI lead | Migration assessment + parallel running evidence + cutover approval | During migration | Block cutover |
| DR-003 | Evidence archived per retention policy | T1-T4 deprecated systems | AI Operations | Archival confirmation with artifact inventory | At retirement | Compliance escalation |
| DR-004 | System decommissioned cleanly | T1-T3 retired systems (T4: recommended) | Technical owner | Decommission record (monitoring removed, access revoked, documentation archived) | At retirement | Track until complete |

---

## Summary

This register contains 48 controls, grouped under the 10 stages of the governance workflow (Stage 1, Idea Intake, has no register controls). For the full governance workflow describing how systems progress through these stages, see [governance-workflow.md](governance-workflow.md). For a worked example, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md#control-coverage): it shows the evidence for every control that applies to that T1 GenAI RAG system and lists the controls that do not apply, with reasons.
