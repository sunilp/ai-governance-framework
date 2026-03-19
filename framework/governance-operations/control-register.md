# Control Register

This register maps every governance control in the framework to its evidence, owner, and escalation path. It is the single source of truth for what evidence an auditor, regulator, or compliance team should expect. Controls are organized by lifecycle stage — the way audits are structured.

For the end-to-end process connecting these stages, see [governance-workflow.md](governance-workflow.md). For a complete worked example showing every control's evidence for a T1 system, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md).

## Stage 1: Intake & Risk Assessment

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RA-001 | Risk assessment completed using framework matrices | All AI systems | Product owner | Signed risk assessment with dimension scoring + tier determination | Before development begins | Cannot proceed to development |
| RA-002 | Tier override review for auto-T1 triggers | Systems matching any auto-T1 criterion | AI Risk | Override decision document | At assessment | Escalate to AI Risk Committee |
| RA-003 | Impact assessment completed | T1/T2 systems | Product owner | Completed impact assessment template | Before development | Cannot proceed to development |
| RA-004 | Risk assessment reviewed by appropriate authority | All AI systems | AI Risk (T1/T2) / Team lead (T3/T4) | Review record with sign-off | Before development | Block progression |
| RA-005 | DPIA filed (if PII processed) | Systems processing PII | DPO | Filed DPIA with DPO sign-off | Before development | Cannot proceed; escalate to DPO |

## Stage 2: Architecture & Design Review

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| AR-001 | System architecture documented | All AI systems | Technical owner | Architecture document with component diagram and data flows | Before development | Block development |
| AR-002 | Architecture review board sign-off | T1/T2 systems | Architecture review board | Review meeting record with decision and conditions | Before development | Cannot proceed without sign-off |
| AR-003 | Data residency confirmed | Systems with external data flows | Technical owner | Data flow map with residency confirmation per jurisdiction | Before development | Escalate to compliance |
| AR-004 | Vendor/model selection justified | Systems using external models | AI lead | Model selection document with evaluation results and rationale | Before development | Block development |
| AR-005 | Third-party model risk assessment completed | Systems using external vendor APIs | AI Risk | Completed vendor risk assessment | Before development; annually thereafter | Block deployment; procurement escalation |

## Stage 3: Development & Prompt Engineering

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DE-001 | Model card created and version-controlled | All AI systems | AI lead | Model card in version control (YAML/markdown) | Before validation | Block validation gate |
| DE-002 | Prompts version-controlled | All GenAI systems | AI lead | Prompt files in git repository with commit history | Continuous | Block deployment |
| DE-003 | Prompt peer review completed | T1/T2 GenAI | Product owner | Signed prompt review checklist + prompt version link | Before release | Block deployment |
| DE-004 | Guardrails implemented and configured | T1/T2 GenAI (mandatory); T3/T4 (per tier standard) | Technical owner | Guardrail configuration document + test results | Before deployment | Block deployment |
| DE-005 | Data governance controls applied to training/fine-tuning data | Systems using fine-tuned models | AI lead | Data governance checklist with provenance documentation | Before training | Block training |

## Stage 4: Evaluation & Testing

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| EV-001 | Pre-release evaluation suite executed | All AI systems | AI lead | Evaluation report with pass/fail per metric | Before every deployment | Block deployment |
| EV-002 | Safety evaluation passed | All GenAI systems | AI lead | Safety eval results meeting tier thresholds | Before every deployment | Block deployment |
| EV-003 | Regression evaluation passed | T1/T2 on model/prompt change | AI lead | Regression report comparing current vs. previous version | On change | Block deployment if regression detected |
| EV-004 | RAG retrieval quality evaluated | RAG-based systems | AI lead | Retrieval precision/recall/relevance metrics | Before deployment + per tier cadence | Block deployment (pre-release); investigate (production) |
| EV-005 | Bias evaluation completed | T1/T2 systems | Responsible AI lead | Counterfactual test results with demographic parity metrics | Before deployment + quarterly (T1) | Block deployment; escalate to Responsible AI |
| EV-006 | Eval dataset integrity verified | All AI systems | AI lead | Confirmation of no overlap with training data; dataset version recorded | Before each eval run | Invalidate eval results; re-run |
| EV-007 | LLM-as-judge calibrated against human evaluators | T1/T2 using automated eval | AI lead | Calibration report with correlation scores | Quarterly (T1); semi-annually (T2) | Pause automated eval; revert to human eval |

## Stage 5: Security & Red-Teaming

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| SR-001 | Red-team testing completed per tier depth | All GenAI systems | Security / AI Risk | Red-team report | Pre-deployment; per tier cadence | Block deployment (T1/T2); document risk acceptance (T3/T4) |
| SR-002 | No unresolved Critical or High findings | T1/T2 systems | System owner | Red-team report showing 0 Critical, 0 unaddressed High | Before deployment | Block deployment |
| SR-003 | Adversarial robustness defenses implemented | T1/T2 GenAI | Technical owner | Defense configuration documentation | Before deployment | Block deployment |
| SR-004 | Supply chain security verified | Systems using open-source models | Security | AI-BOM + provenance verification | Before deployment; on model change | Block deployment |

## Stage 6: Deployment Approval

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DA-001 | Evidence pack assembled and complete | All AI systems | Product owner | Evidence checklist with all required items present | Before deployment | Block deployment |
| DA-002 | Sign-off chain completed per tier | All AI systems | Product owner | Signed deployment approval record | Before deployment | Block deployment |
| DA-003 | Deployment gates passed | All AI systems | AI Operations | Gate evidence package | Before deployment | Block deployment |
| DA-004 | Rollback plan documented and tested | T1/T2 systems | Technical owner | Rollback procedure + test evidence | Before deployment | Block deployment |

## Stage 7: Production Monitoring

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| PM-001 | Monitoring configured per tier requirements | All production AI | AI Operations | Monitoring configuration + dashboard reference | Before traffic enabled | Block go-live |
| PM-002 | Alerting active with defined thresholds | All production AI | AI Operations | Alert configuration evidence | Before traffic enabled | Block go-live |
| PM-003 | Human oversight operational | T1/T2 systems | Product owner | Oversight process document + staffing confirmation | Before traffic enabled | Block go-live |
| PM-004 | Production evaluation running per cadence | All production AI | AI Operations | Eval schedule + latest eval results | Per tier cadence | Escalate to AI Risk; increase monitoring |
| PM-005 | Cost monitoring active | All production AI | AI Operations | Cost dashboard + alert configuration | Before traffic enabled | Block go-live |

## Stage 8: Incident Response

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| IR-001 | Incident response playbook documented | T1/T2 systems | AI Operations | Published runbook accessible to on-call | Before deployment | Block deployment |
| IR-002 | On-call team assigned | T1/T2 systems | AI Operations | On-call rotation schedule | Continuous | Escalate to AI Platform Lead |
| IR-003 | Incident reported per severity SLA | All production AI (on incident) | Incident commander | Incident report per template | Per incident | Escalate per escalation paths |
| IR-004 | Post-mortem completed for S1/S2 incidents | T1/T2 systems (on incident) | Incident commander | Post-mortem report | Within 1 week (S1) / 2 weeks (S2) | Escalate to AI Risk Committee |
| IR-005 | Remediation actions tracked to completion | All incidents with remediation | System owner | Remediation tracker with status | Until complete | Escalate to AI Risk |

## Stage 9: Review & Revalidation

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RV-001 | Scheduled review completed | All AI systems | System owner | Review record with findings and actions | Monthly (T1); Quarterly (T2); Semi-annual (T3); Annual (T4) | Overdue review flagged in governance metrics; escalate after 30 days |
| RV-002 | Model card updated | All AI systems | AI lead | Updated model card with current information | At each review | Block until updated |
| RV-003 | Revalidation on material change | All AI systems | AI lead | Revalidation assessment + eval results | On model change, provider update, or regulatory change | Re-enter deployment gates |
| RV-004 | Regulatory change impact assessed | All AI systems | Compliance | Regulatory change impact assessment | On regulatory change | Escalate to AI Risk Committee |

## Stage 10: Deprecation & Retirement

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DR-001 | Deprecation impact assessment completed | Systems being deprecated | System owner | Impact assessment with affected systems and migration plan | At deprecation trigger | Block deprecation without assessment |
| DR-002 | Migration governance followed | Systems being replaced | AI lead | Migration assessment + parallel running evidence + cutover approval | During migration | Block cutover |
| DR-003 | Evidence archived per retention policy | All deprecated systems | AI Operations | Archival confirmation with artifact inventory | At retirement | Compliance escalation |
| DR-004 | System decommissioned cleanly | All retired systems | Technical owner | Decommission record (monitoring removed, access revoked, documentation archived) | At retirement | Track until complete |

---

## Summary

This register contains 48 controls across 10 lifecycle stages. For the full governance workflow describing how systems progress through these stages, see [governance-workflow.md](governance-workflow.md). For a complete worked example showing every control's evidence for a T1 system, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md).
