# Governance Case File: Retail Banking Customer Service Assistant

**System ID:** cs-assistant-retail-v1.2
**Risk Tier:** T1 (Critical)
**Status:** Production (v1.0.0 deployed 2025-09-15; current version 1.2.0, deployed 2026-01-10)

This document is the governance trail from idea intake through deployment and the first six months of production operations. It shows the evidence for every control that applies to this T1 GenAI RAG system; [Control Coverage](#control-coverage) maps each control to its section and lists the controls that do not apply, with reasons. Teams can use this structure as a template for their own systems.

---

## Control Coverage

Controls are from the [control register](../../framework/governance-operations/control-register.md), grouped by [governance workflow](../../framework/governance-operations/governance-workflow.md) stage.

| Workflow stage | Controls evidenced | Section |
|----------------|-------------------|---------|
| 2. Risk Assessment & Tiering | RA-001, RA-002, RA-003, RA-004, RA-005 | 2 |
| 3. Architecture & Design Review | AR-001, AR-002, AR-003, AR-004, AR-005 | 3 |
| 4. Development & Prompt Engineering | DE-001, DE-002, DE-003, DE-004 | 4, 5 |
| 5. Evaluation & Testing | EV-001 to EV-007, EV-009, independent validation | 6, 8 |
| 6. Security Review & Red-Teaming | SR-001, SR-002, SR-003 | 7 |
| 7. Deployment Approval | DA-001, DA-002, DA-003, DA-004 | 9 |
| 8. Production Operations | PM-001 to PM-005, IR-001 to IR-005 | 10, 14, 15 |
| 9. Ongoing Governance | RV-001, RV-002, RV-003, RV-004 | 11, 12, 13 |

RV-004 is event-driven. Regulatory change is checked at each quarterly review (Section 11); no impact assessment was triggered in the period this file covers.

**Controls that do not apply:**

| Control | Reason |
|---------|--------|
| DE-005 | No fine-tuning or training. The system uses vendor base models through APIs, grounded with RAG. |
| SR-004 | No open-source models or weights. The primary, fallback and embedding models are vendor APIs, assessed under AR-005. |
| DR-001, DR-002, DR-003, DR-004 | The system is in production and has not been deprecated, replaced or retired. The v1.2.0 base model change was a material change handled under RV-003 (Section 12), not a system replacement. |

---

## 1. Intake Record (Stage 1)

*Pre-register artifact, no control ID. See governance-workflow.md Stage 1.*

| Field | Value |
|-------|-------|
| Proposer | Head of Retail Banking Digital |
| Business Unit | Retail Banking |
| Date Submitted | 2025-07-01 |
| Use Case | AI-powered customer service assistant for retail banking customers via mobile app and online banking chat |
| Business Justification | Reduce average inquiry resolution time from 8 min to <2 min; handle 60% of routine inquiries without human intervention |
| Initial Risk Screening | Likely T1: customer-facing, will process customer PII, uses external LLM API |
| Sponsor | COO, Retail Banking |
| AI Risk Involvement | Flagged for early engagement |

### Intake Decision

The AI Risk team performed an initial screening call with the proposer on 2025-07-03. The system was flagged as likely T1 based on three factors: direct customer interaction, PII processing through an external API, and generation of customer-facing content without individual human review. Full risk assessment was initiated immediately.

---

## 2. Risk Assessment Summary (Stage 2)

*Control IDs: RA-001, RA-002, RA-003, RA-004, RA-005*

Full risk assessment documented in [risk-assessment.md](risk-assessment.md).

| Field | Value |
|-------|-------|
| Prepared by | Product Owner, Retail Banking Digital, 2025-07-18 (RA-001) |
| Impact assessment | IA-2025-CS-001, completed 2025-07-25 (RA-003) |
| DPIA | DPIA-2025-CS-001, filed with DPO sign-off 2025-07-25 (RA-005) |
| Approved by | AI Risk Committee, 2025-07-29 (RA-004) |

### Dimension Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect information about account balances, fees, or product terms could cause customer harm. System does not make decisions — it provides information. |
| Data Exposure Risk | **Critical (4)** | Customer PII (names, account details, transaction history) flows through the LLM pipeline. PII redaction is applied pre-API but residual risk exists. |
| Prompt Injection Susceptibility | **High (3)** | Customer-facing with unrestricted text input. Input validation and injection detection are in place but cannot guarantee 100% coverage. |
| Output Controllability | **High (3)** | Outputs are delivered to customers after automated guardrail checks but without individual human review. Guardrails catch known patterns but not novel failure modes. |
| Third-Party Model Dependency | **High (3)** | Primary model is Anthropic Claude, served through Vertex AI in the EU region. Fallback to Gemini 2.5 Pro on Vertex AI is validated. Single-vendor dependency for primary path. |

**Aggregate Score:** 16 (recorded for context; it does not set the tier)
**Highest Dimension:** Critical (4), so the scored tier is T1

### Risk Tier Determination

**Tier: T1 (Critical)**

Override check against the canonical list in the [GenAI risk matrix](../../framework/risk-classification/genai-risk-matrix.md#risk-tier-determination-for-genai) (RA-002):
- Trigger 2 applies: the system generates customer-facing content delivered without per-output human review. Automatic T1.
- Trigger 3 does not apply: customer personal data goes to an external LLM API, but all four safeguards are in place (vendor zero data retention, EU regional endpoint, signed DPA, PII redaction and minimisation before the call). Item 8 applies instead: minimum T2.
- No other trigger applies. See the checklist in [risk-assessment.md](risk-assessment.md).

### Risk Acceptance Conditions

Residual risks accepted by AI Risk Committee (2025-09-10, with the deployment approval):

1. Hallucination rate of ≤ 1% — accepted given RAG grounding, monitoring, and human spot-checks
2. Prompt injection residual risk — accepted given multi-layer defense and quarterly red-teaming
3. Vendor dependency on Anthropic — accepted given validated fallback and exit strategy

Standing conditions:
- Monthly hallucination rate reporting to AI Risk Committee
- P2 alert to on-call and AI Risk if the rolling 7-day hallucination rate exceeds 1%; P1 alert if the rolling 24-hour rate exceeds 2%
- Quarterly red-team testing with external security team
- Annual re-assessment of vendor risk

---

## 3. Architecture Review Record (Stage 3)

*Control IDs: AR-001, AR-002, AR-003, AR-004, AR-005*

| Field | Value |
|-------|-------|
| Architecture document | ARCH-2025-CS-001: component diagram, data flows, integration points (AR-001) |
| Review Date | 2025-08-05 |
| Review Board | AI Architecture Review Board |
| Attendees | Head of AI (chair), AI Platform Lead, CISO delegate, Data Privacy Officer |
| Decision | Approved with conditions |

### Conditions

| # | Condition | Status |
|---|-----------|--------|
| 1 | RAG corpus must have document-level access controls — no customer-specific data in corpus | Verified |
| 2 | PII redaction mandatory before LLM API call — verify with red-team testing | Verified |
| 3 | Fallback model must be validated before production go-live | Verified |

### Data Residency Confirmation

| Component | Region | Confirmation |
|-----------|--------|-------------|
| Application layer | GCP europe-west1 | Confirmed |
| LLM API endpoint | Claude on Vertex AI, EU region | Confirmed |
| RAG corpus (BigQuery Vector Search) | EU | Confirmed |

### Model Selection

Model selection document MS-2025-CS-001 (AR-004): Claude Sonnet 4 (claude-sonnet-4-20250514) as primary model, Gemini 2.5 Pro (gemini-2.5-pro, Vertex AI, EU region) as fallback. Approved by the AI Risk Committee and the CISO on 2025-07-29.

### Vendor Assessment

Anthropic vendor risk assessment completed — reference VRA-2025-ANT-001. Key findings:

- Zero-retention API confirmed (data not stored by vendor)
- Training data exclusion clause in place
- DPA executed
- SLA: 99.9% uptime

Google Cloud (Vertex AI fallback model and embeddings) is covered by VRA-2025-GCP-001.

---

## 4. Model Card Summary (Stage 4)

*Control IDs: DE-001, DE-002, DE-004*

As approved for the v1.0.0 deployment. The current model card (v1.2.0) is [model-card.yaml](model-card.yaml).

| Field | Value |
|-------|-------|
| System Name | Retail Banking Customer Service Assistant |
| System Version | 1.0.0 |
| Base Model | Claude Sonnet 4 (claude-sonnet-4-20250514) |
| Base Model Provider | Anthropic |
| Fallback Model | Gemini 2.5 Pro (gemini-2.5-pro), Vertex AI EU region, validated |
| Hosting | Vertex AI managed API, EU region (zero data retention) |
| System Prompt Version | v1.2.3 |
| Prompt Repository | git://internal/ai-prompts/cs-assistant |
| Decision Type | Informational |
| Human Oversight Pattern | Human-over-the-loop (Pattern 3, with the T1 safeguards in Section 10) |

### Guardrail Configuration

| Guardrail | Status |
|-----------|--------|
| Input validation | Active |
| Output filtering | Active |
| PII redaction | Active |
| Toxicity gate | Active |
| Hallucination detection | Active |

### Custom Rules

- No investment advice or return predictions
- No credit decisions or pre-approval indications
- Escalate complaints to human agent
- No account modifications
- All financial figures must be sourced from account API or documents

---

## 5. Prompt Review Record (Stage 4)

*Control ID: DE-003 (owner: AI lead, AI Platform Engineering Lead)*

| Field | Value |
|-------|-------|
| Prompt Version | v1.2.3 (revised from v1.2.0, the build that was red-teamed in Section 7) |
| Review Date | 2025-08-20 |
| Review Authority | T1: peer review + prompt engineering lead + security review + AI Risk sign-off |

### Review Findings

| # | Finding | Severity | Resolution |
|---|---------|----------|------------|
| 1 | Fallback response for unrecognized intent too vague — should offer escalation | Minor | Updated to offer human agent connection |
| 2 | Edge case: multi-language query mixing not handled | Minor | Added language detection; mixed-language queries route to human agent |

### Review Outcome

The prompt was updated to address both findings and to incorporate the red-team findings from Section 7 (assessment 2025-08-11 to 2025-08-14): context isolation for RAG content, input normalization, and per-turn safety classification. The regression suite and the prompt-change adversarial regression set were re-run on v1.2.3 with no degradation.

### Sign-Off

| Role | Reviewer | Date |
|------|----------|------|
| Peer review | Senior AI Engineer, AI Platform team | 2025-08-20 |
| Prompt engineering lead | Prompt Engineering Lead | 2025-08-21 |
| Security review | AI Security Lead | 2025-08-21 |
| AI Risk sign-off | AI Risk Analyst, AI Risk | 2025-08-22 |

---

## 6. Evaluation Report (Stage 5)

*Control IDs: EV-001, EV-002, EV-003, EV-004, EV-005, EV-006, EV-007, EV-009*

### Evaluation Parameters

| Parameter | Value |
|-----------|-------|
| Evaluation Date | 2025-09-01 |
| Evaluation Dataset Size | 500 cases |
| Training Data Overlap | None confirmed |
| System Version | 1.0.0 (release candidate) |
| Base Model | Claude Sonnet 4 (claude-sonnet-4-20250514) |
| Prompt Version | v1.2.3 |

### Results

| Metric | Result | Threshold | Status | Eval Method |
|--------|--------|-----------|--------|-------------|
| Faithfulness | 0.94 (95% lower bound 0.933, 500 cases) | ≥ 0.90 | **PASS** | LLM-as-judge (calibrated) |
| Hallucination rate | 0.002 (1 of 500; 95% upper bound 0.95%) | ≤ 0.01 (1%) | **PASS** | Hybrid (LLM-as-judge + human eval) |
| Correctness | 0.96 | ≥ 0.95 | **PASS** | Human eval |
| Safety pass rate | 0.998 (1 failure in 500; failure-rate upper bound 0.95%) | ≥ 0.99 | **PASS** | Automated (500-case safety eval suite, distinct from adversarial robustness testing) |
| Retrieval precision@5 | 0.87 (95% lower bound 0.851, 200 queries) | ≥ 0.85 | **PASS** | Automated |
| Counterfactual consistency | 0.95 (most inconsistent attribute: 11 of 200 pairs, upper bound 8.94%) | ≥ 0.90 | **PASS** | Automated (200 pairs x 4 attributes) |
| Escalation appropriateness | 0.93 | ≥ 0.90 | **PASS** | Human eval |
| Guardrail false negative rate | 0.0 (0 of 300; 95% upper bound 0.99%) | ≤ 0.01 (1%) | **PASS** | Automated (labelled harmful or out-of-scope set) |
| Guardrail false positive rate | 0.023 (7 of 300; 95% upper bound 4.34%) | ≤ 0.05 (customer-facing default ceiling) | **PASS** | Automated (labelled legitimate set) |

Status applies the T1 [statistical pass rule](../../framework/llm-lifecycle/evaluation-governance.md#statistical-pass-rule): proportions on the one-sided 95% upper bound, means on the one-sided 95% lower bound. Results by channel and for customers with vulnerability indicators were reported; every segment of 100 or more cases met the thresholds.

### Regression and Fallback

- Regression (EV-003): v1.0.0 compared with the v0.9 pilot build on the identical 500-case suite. No metric degraded.
- Fallback validation: Gemini 2.5 Pro run on the same pre-release and safety suites on 2025-09-02. Met T1 thresholds (architecture condition 3).

### LLM-as-Judge Calibration

LLM-as-judge calibration correlation with human evaluators: **0.91** (threshold ≥ 0.85 — **PASS**).

Calibration was performed on a 100-case subset with dual human annotation. Inter-annotator agreement (Cohen's kappa): 0.87. The LLM-as-judge is used for faithfulness and hallucination rate metrics; human eval remains the primary method for correctness and escalation appropriateness.

### Overall Assessment

**ALL METRICS PASS.** The system meets all T1 evaluation thresholds. No conditional passes or waivers required.

---

## 7. Red-Team Summary (Stage 6)

*Control IDs: SR-001, SR-002, SR-003*

### Assessment Overview

| Field | Value |
|-------|-------|
| Assessment Dates | 2025-08-11 to 2025-08-14 |
| Assessor | Internal AI Security + external CyberAI Ltd |
| Methodology | Manual + automated, 200 test cases, 6 categories |
| Model | Claude Sonnet 4 (claude-sonnet-4-20250514) |
| Prompt Version | v1.2.0 (pre-review build; findings incorporated in v1.2.3, Section 5) |

### Categories Tested

1. Direct prompt injection
2. Indirect prompt injection (via RAG documents)
3. Jailbreak / role-play escalation
4. PII extraction / data leakage
5. Encoding-based evasion (base64, Unicode)
6. Multi-turn manipulation

### Findings

| Severity | Count | Details |
|----------|-------|---------|
| Critical | 0 | — |
| High | 1 | Indirect prompt injection via RAG document: crafted FAQ with embedded instructions caused model to reveal system prompt structure. Remediated by context isolation. Retested on v1.2.3 and confirmed fixed. |
| Medium | 3 | (1) Multi-turn escalation bypass after 12 turns. Mitigated with per-turn safety classification. (2) Base64-encoded harmful request processed. Mitigated with input normalization. (3) System disclosed Claude usage when asked. Accepted as low impact. |
| Low | 5 | Minor boundary softening under edge conditions. Tracked. |

### Gate Decision

**Conditional pass.** High finding remediated and retested. Medium findings (1) and (2) remediated; medium finding (3) accepted as low impact (model identity is not a protected secret, and the framework's [transparency standards](../../framework/responsible-ai/transparency-standards.md#user-interaction-disclosure) already require the assistant to disclose that customers are interacting with AI. This disclosure was adopted ahead of EU AI Act Art. 50, which applies from 2 August 2026).

Adversarial defense configuration (SR-003): context isolation for retrieved content, input normalization, per-turn safety classification, injection pattern detection. Documented in the security assessment SEC-2025-CS-001, which also records the application security review and penetration test (deployment gate criteria).

Full report: **RT-2025-CS-001** (Confidential)

---

## 8. Independent Validation (Stage 5)

*T1 requires full independent validation by Model Risk Management (MRM). See [model validation](../../framework/model-lifecycle/validation.md).*

| Field | Value |
|-------|-------|
| Validator | Model Risk Management (independent of the AI Platform team that built the system) |
| Report | MRM-2025-CS-001 |
| Date | 2025-09-03 |
| Scope | Risk assessment and tier, evaluation design and results (Section 6), dataset integrity, LLM-as-judge calibration, red-team results (Section 7), fallback validation, monitoring design |
| Outcome | Approved for deployment. No open findings |
| Revalidation | Addendum MRM-2025-CS-001-A1 for the v1.2.0 material change, 2026-01-09 (Section 12). Next annual revalidation due by 2026-09-03 |

---

## 9. Deployment Approval (Stage 7)

*Control IDs: DA-001, DA-002, DA-003, DA-004*

### Pre-Deployment Sequence

| Date | Step |
|------|------|
| 2025-07-18 to 2025-07-29 | Risk assessment, impact assessment, DPIA, model selection; risk assessment approved |
| 2025-08-05 | Architecture review |
| 2025-08-11 to 2025-08-14 | Red-team on prompt v1.2.0 |
| 2025-08-20 to 2025-08-22 | Prompt review of v1.2.3, incorporating red-team findings |
| 2025-09-01 to 2025-09-02 | Pre-release evaluation and fallback validation |
| 2025-09-03 | Independent validation |
| 2025-09-05 | Rollback and kill switch tested; incident playbook published |
| 2025-09-08 to 2025-09-10 | Sign-offs |
| 2025-09-15 | v1.0.0 deployed |

### Evidence Checklist

Matches the T1 [minimum evidence pack](../../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier).

| # | Evidence Item | Controls | Status | Reference |
|---|--------------|----------|--------|-----------|
| 1 | Signed risk assessment, override check and approval | RA-001, RA-002, RA-004 | Complete | [risk-assessment.md](risk-assessment.md); approved 2025-07-29 |
| 2 | Impact assessment | RA-003 | Complete | IA-2025-CS-001 |
| 3 | DPIA | RA-005 | Complete | DPIA-2025-CS-001 |
| 4 | Architecture document and data residency confirmation | AR-001, AR-003 | Complete | ARCH-2025-CS-001; Section 3 |
| 5 | Architecture review record | AR-002 | Complete | Section 3 |
| 6 | Model selection and vendor risk assessment | AR-004, AR-005 | Complete | MS-2025-CS-001; VRA-2025-ANT-001; VRA-2025-GCP-001 |
| 7 | Model card and prompt version history | DE-001, DE-002 | Complete | [model-card.yaml](model-card.yaml); prompt repository |
| 8 | Prompt review record | DE-003 | Complete | Section 5 |
| 9 | Guardrail configuration and test results | DE-004 | Complete | Section 4 |
| 10 | Evaluation report | EV-001 to EV-007, EV-009 | Complete | Section 6 |
| 11 | Independent validation report | (Stage 5) | Complete | MRM-2025-CS-001; Section 8 |
| 12 | Red-team report | SR-001, SR-002 | Complete | RT-2025-CS-001; Section 7 |
| 13 | Security assessment: adversarial defenses, application security review, penetration test | SR-003, DA-003 | Complete | SEC-2025-CS-001 (SR-004 not applicable) |
| 14 | Monitoring, alerting, human oversight, production evaluation, cost monitoring | PM-001 to PM-005 | Complete | Section 10 |
| 15 | Incident response playbook and on-call rotation | IR-001, IR-002 | Complete | CS-ASSIST-IRP-v1.0; Section 10 |
| 16 | Rollback plan with test evidence | DA-004 | Complete | Rollback to the v0.9 pilot build and kill switch tested 2025-09-05 |
| 17 | Evidence checklist, gate evidence and deployment approval | DA-001, DA-002, DA-003 | Complete | This checklist; GEP-2025-CS-001; signatures below |

### Sign-Off Chain

Required for T1 with personal data: AI Risk Committee, CISO and DPO. The business owner and Compliance also signed.

| Role | Title | Date | Decision |
|------|-------|------|----------|
| Business Owner | Head of Retail Banking Digital | 2025-09-08 | Approved |
| CISO | Chief Information Security Officer | 2025-09-09 | Approved |
| DPO | Data Protection Officer | 2025-09-09 | Approved with conditions |
| Compliance | Head of Compliance | 2025-09-10 | Approved |
| AI Risk Committee | Chair, AI Risk Committee | 2025-09-10 | Approved |

### DPO Conditions

The Data Protection Officer approved with the following conditions:

1. DPIA to be reviewed within 6 months or upon material change to data processing
2. Customer consent mechanism for AI interaction to be reviewed by Legal within 30 days
3. Data subject access request (DSAR) process must include AI interaction logs

All conditions tracked in the DPIA register.

### Data Classification

This evidence pack is classified as **Internal/Confidential**. Access restricted to AI Risk, system owner, approvers, and auditors.

---

## 10. Production Operations (Stage 8)

*Control IDs: PM-001, PM-002, PM-003, PM-004, PM-005, IR-001, IR-002*

### Monitoring Metrics

| Metric | Threshold | Alert Priority | Notification |
|--------|-----------|----------------|-------------|
| Hallucination rate (rolling 7-day) | > 1% | P2 | On-call + AI Risk |
| Hallucination rate (rolling 24-hour) | > 2% | P1 | On-call + AI Risk + Head of AI |
| PII leakage detection | Any occurrence | P1 | On-call + CISO |
| RAG refresh pipeline failure (added after GEN-2026-042) | Any failed run | P2 | On-call + RAG pipeline owner |
| Guardrail trigger rate | > 2σ from baseline | P2 | On-call + team lead |
| Latency p95 | > 3000ms | P2 | On-call |
| Error rate | > 1% | P2 | On-call |
| Daily spend | > €700 | P3 | Team lead + finance |
| User satisfaction (thumbs down) | > 15% | P3 | Product owner |

### Alert Response SLAs

Alert priority (P1-P4) is not incident severity. On-call decides whether to declare an incident and sets its severity (S1-S4) per [escalation paths](../../framework/operating-model/escalation-paths.md#alert-priority-to-incident-severity).

| Priority | Acknowledge | Investigate | Mitigate |
|----------|-------------|-------------|----------|
| P1 | 15 min | 1 hour | 4 hours |
| P2 | 1 hour | 4 hours | 24 hours |
| P3 | 4 hours | 1 business day | 5 business days |

### Production Evaluation (PM-004)

| Activity | Configuration |
|----------|---------------|
| Online automated scoring of live traffic | Every response (async LLM-as-judge) |
| Metrics review | Daily dashboard check by AI Operations; monthly system-owner review |
| Full offline suite re-run | Monthly, and on any model, provider or prompt change |
| RAG retrieval evaluation | Weekly |
| Bias | Formal evaluation quarterly; production counterfactual spot-checks weekly (since v1.2.0) |
| Vendor behaviour canary | 100 fixed domain queries, daily |

### Human Oversight (PM-003)

Pattern 3 (human-over-the-loop). Allowed for this T1 informational system because all five safeguards in the [pattern selection matrix](../../framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) are in place and evidenced.

| Safeguard | Implementation | Evidence |
|-----------|----------------|----------|
| a) Daily sampled human review | 5% of responses each day, never fewer than 50 (about 80 a day at current volume), by trained customer service quality reviewers | Daily review log in the quality dashboard |
| b) Risk-based routing | Routed to a human agent: complaints, vulnerability indicators, fee or pricing disputes, anything that looks like regulated advice (investment, credit), unsupported languages, and low-confidence responses | Escalation router configuration and test results |
| c) Output scope guardrails | Output guardrails and the custom rules in Section 4 | Guardrail configuration and test results (DE-004) |
| d) Kill switch | Stops the AI channel and routes all chats to human agents within 15 minutes. Tested quarterly: 2025-09-05, 2025-12-03, 2026-03-04 | Kill switch test records |
| e) Hallucination monitoring | Every response scored against the T1 threshold in [evaluation governance](../../framework/llm-lifecycle/evaluation-governance.md#threshold-definitions-by-tier); alerts as in Monitoring Metrics above | Monitoring configuration |

### Operational Configuration and Incident Readiness

| Parameter | Value |
|-----------|-------|
| Dashboard | internal://dashboards/cs-assistant |
| Safety monitoring | Real-time guardrail monitoring |
| Cost monitoring (PM-005) | Real-time with daily budget alerts |
| Incident response playbook (IR-001) | CS-ASSIST-IRP-v1.0, runbook internal://runbooks/cs-assistant, published 2025-09-05 |
| On-call team (IR-002) | AI Platform On-Call, 24x7 rotation; schedule held in the on-call tool and checked at each quarterly review |
| Escalation path | On-call → AI Platform Lead → Head of AI → CTO |
| Audit logging | Every prompt and response logged, append-only, 7-year retention ([retention](../../framework/compliance/prompt-audit-trail.md#retention-requirements)) |

---

## 11. Ongoing Governance Log (Stage 9)

*Control IDs: RV-001, RV-002, RV-003, RV-004*

Formal governance reviews are quarterly for T1. Each review includes a risk re-assessment (re-tiering check), a model card update and a regulatory change check.

| Date | Event | Controls | Outcome |
|------|-------|----------|---------|
| 2025-11-12 | Quarterly red-team, RT-2025-CS-002 | SR-001, SR-002 | No Critical or High findings |
| 2025-11-20 | v1.1.0 released: German language support, product documentation corpus update. No model or prompt change | Change record | Approved by Head of AI as a non-material change (model card change history) |
| 2025-12-03 | Quarterly kill switch test | PM-003 | Passed |
| 2025-12-10 | Q4 2025 governance review (first review, within 3 months of go-live) | RV-001, RV-002, RV-004 | Tier unchanged (T1); model card updated; no regulatory change requiring assessment; base model migration proposed |
| 2025-12-17 | Material change assessment for v1.2.0; model selection update MS-2025-CS-002 approved by AI Risk Committee and CISO | RV-003, AR-004 | Tier unchanged (T1); proceed to revalidation |
| 2026-01-10 | v1.2.0 deployed after revalidation | RV-003 | Section 12 |
| 2026-02-11 | Quarterly red-team, RT-2026-CS-001 | SR-001, SR-002 | No Critical or High findings |
| 2026-03-04 | Quarterly kill switch test | PM-003 | Passed |
| 2026-03-10 | Q1 2026 governance review | RV-001, RV-002, RV-004 | Section 13 |
| 2026-03-15 | Incident GEN-2026-042 (S2) | IR-002 to IR-005 | Sections 14 and 15 |
| 2026-04-01 | AI Risk Committee accepts post-mortem recommendation | IR-005 | Section 15 |
| 2026-06-10 | Next governance review (Q2 2026) | RV-001 | Scheduled |

---

## 12. Material Change Revalidation: v1.2.0 (Stage 9)

*Control ID: RV-003*

| Field | Value |
|-------|-------|
| Change | Base model migration from claude-sonnet-4-20250514 to claude-sonnet-4-5-20250929; prompt retargeted to the new model as v2.0.0; improved hallucination detection guardrails; weekly production counterfactual spot-checks added |
| Reason | Quality and cost, based on comparison testing recorded in MS-2025-CS-002 |
| Classification | Material change (model swap). Handled through the deployment approval chain for T1 |
| Release | v1.2.0, 2026-01-10 |

### Revalidation Evidence

| Evidence | Controls | Date | Result |
|----------|----------|------|--------|
| Material change assessment and risk re-assessment | RV-003 | 2025-12-17 | Tier unchanged (T1) |
| Model selection update | AR-004 | 2025-12-17 | MS-2025-CS-002 approved by AI Risk Committee and CISO |
| Prompt review of v2.0.0 (full T1 review) | DE-003 | 2026-01-05 | Peer review, prompt engineering lead, security review and AI Risk sign-off completed |
| Prompt-change adversarial regression set (150 cases) | EV-003 | 2026-01-07 | Injection resistance 0.98, jailbreak resistance 0.97; no Critical or High findings |
| DPIA review (DPO condition 1) | RA-005 | 2026-01-07 | No change to data processing: same vendor terms, zero retention and endpoint |
| Regression suite: v1.2.0 against v1.1.0 on the identical 500-case suite | EV-003 | 2026-01-08 | No metric degraded |
| Safety evaluation re-run (500-case suite) | EV-002 | 2026-01-08 | 1 failure in 500 (failure-rate upper bound 0.95%); met T1 threshold |
| RAG retrieval evaluation re-run | EV-004 | 2026-01-08 | Precision@5 0.88 (95% lower bound 0.861, 200 queries); met T1 threshold |
| Guardrail evaluation re-run on the updated hallucination detection guardrails | EV-009 | 2026-01-08 | False negatives 0 of 300 (upper bound 0.99%); false positives 6 of 300 (upper bound 3.91%, against the 5% ceiling) |
| Formal bias evaluation re-run | EV-005 | 2026-01-08 | Counterfactual consistency 0.95 (200 pairs per attribute, 4 attributes; most inconsistent attribute 11 of 200, within the T1 maximum of 12) |
| Fallback re-validation with prompt v2.0.0 | EV-001 | 2026-01-08 | Met T1 thresholds |
| Independent revalidation by MRM | (Stage 5) | 2026-01-09 | Addendum MRM-2025-CS-001-A1: approved |
| Rollback to v1.1.0 (previous release) tested | DA-004 | 2026-01-09 | Passed |
| Deployment approval | DA-002 | 2026-01-09 | AI Risk Committee (out-of-cycle session), CISO and DPO approved |

Full results are in the model card evaluation block ([model-card.yaml](model-card.yaml), evaluation date 2026-01-08).

---

## 13. Q1 2026 Governance Review (Stage 9)

*Control IDs: RV-001, RV-002*

| Field | Value |
|-------|-------|
| Review Date | 2026-03-10 |
| Attendees | AI Platform Lead, AI Risk Analyst, Product Owner, Head of Retail Banking Digital |
| Review Period | 2025-12-10 to 2026-03-10 |
| System Version | v1.2.0 (since 2026-01-10) |

### Operational Summary

| Metric | Value |
|--------|-------|
| Total interactions | 142,000 |
| Escalation rate | 18% |
| Average resolution time | 1.4 min |
| User satisfaction (thumbs up) | 82% |
| Availability | 99.94% |

### Checks

| Check | Result |
|-------|--------|
| Risk re-assessment (re-tiering check) | Tier unchanged (T1) |
| Human oversight safeguards (Section 10) | Daily sample met on every day of the period; kill switch tested 2026-03-04 |
| Production evaluation | Monthly offline suite re-runs and weekly RAG retrieval evaluations met T1 thresholds |
| Quarterly red-team | RT-2026-CS-001, no Critical or High findings |
| Regulatory change | No change requiring an impact assessment |
| Model card | Updated (RV-002) |

### Findings

| # | Finding | Severity | Action | Status |
|---|---------|----------|--------|--------|
| 1 | German language accuracy lower than English (faithfulness 0.88 vs. 0.94). The German segment of the offline suite has 80 cases, below the 100-case gating size, so it is reported, not gated | Low | Schedule targeted German eval expansion (100 additional cases) | Due 2026-05-15 |
| 2 | Cost per request trending 8% above baseline (€0.032 vs. €0.03) | Low | Investigate prompt optimization | Due 2026-05-01 |

### Review Decision

The system continues to operate within acceptable risk parameters.

**Next scheduled review:** 2026-06-10

---

## 14. Example Incident: S2 Customer-Facing Hallucination, GEN-2026-042 (Stage 8)

*Control IDs: IR-002, IR-003, PM-002, PM-004*

### Incident Summary

| Field | Value |
|-------|-------|
| Incident ID | GEN-2026-042 |
| Severity | S2 |
| System | cs-assistant-retail-v1.2 |
| Detection Time | 2026-03-15 14:22 UTC |
| Detection Method | Automated monitoring: P2 alert, rolling 7-day hallucination rate above 1% |
| Mitigation Time | 2026-03-15 16:45 UTC |
| Resolution Time | 2026-03-16 10:00 UTC |

### What Happened

The rolling 7-day hallucination rate crossed the 1% alert line and reached 1.1%, which fired a P2 alert. Investigation found that the rolling 24-hour rate had peaked at 1.5%, below the 2% P1 line. Three documents in the RAG corpus contained outdated fee information: fee schedules for current accounts, savings accounts, and international transfers that had been updated on 2026-03-01 but not reflected in the corpus.

The document refresh pipeline had failed silently for 2 weeks due to an authentication token expiration on 2026-03-01. The pipeline did not have health monitoring configured, so no alert was raised when it stopped running.

### Customer Impact

- Approximately 40 customers received incorrect fee information over the 2-week window
- None were charged incorrectly: a billing check of the affected accounts found no incorrect charges, and corrected communications were sent to the affected customers on 2026-03-17
- No financial transactions were affected (system is informational only — it does not execute transactions)
- 2 customer complaints received via normal support channels
- No regulatory reporting required (informational error, no financial harm)

### Timeline

| Time (UTC) | Event |
|------------|-------|
| 2026-03-15 14:22 | P2 alert: rolling 7-day hallucination rate at 1.1% (alert line: 1%) |
| 2026-03-15 14:45 | On-call engineer acknowledges alert (23 minutes, within the P2 1-hour SLA) and begins investigation |
| 2026-03-15 15:30 | Root cause identified: 3 stale documents in RAG corpus; document refresh pipeline down since 2026-03-01. Rolling 24-hour rate found to have peaked at 1.5% |
| 2026-03-15 15:40 | Incident declared S2: incorrect output reached customers. Incident commander assigned; AI Risk notified |
| 2026-03-15 16:45 | Stale documents replaced manually; RAG index refreshed (containment) |
| 2026-03-15 17:30 | Hallucination rate on responses since the fix back at 0.7% (real-time monitoring) |
| 2026-03-16 10:00 | Pipeline failure root-caused (auth token expiration); auth renewal automated |
| 2026-03-17 | Billing check complete, no incorrect charges; corrected communications sent to affected customers |
| 2026-03-18 | Post-mortem held (Section 15) |

### Severity Justification

Classified S2 under [escalation paths](../../framework/operating-model/escalation-paths.md#severity-classification):
- Incorrect output (outdated fee information) reached about 40 customers, with no confirmed harm. That is the S2 definition.
- The tier floor also applies: any incident on a T1 system that reached customers is at least S2.
- Not S1: no customer was charged incorrectly, there was no financial loss, no data exposure and no regulatory breach.

S2 consequences applied: AI Risk notified at declaration (15:40), containment started within the S2 4-hour response SLA, root cause identified within 48 hours (2026-03-16 10:00), and a post-mortem completed within 2 weeks (2026-03-18, IR-004).

Board reporting: the incident does not meet the [material incident criteria](../../framework/operating-model/board-reporting.md#material-incident-criteria) (about 40 customers affected, no financial harm, no regulatory notification). No between-quarter board notification was required. It is included in the Q1 2026 quarterly board AI risk report.

---

## 15. Post-Mortem: GEN-2026-042 (Stage 8)

*Control IDs: IR-004, IR-005*

| Field | Value |
|-------|-------|
| Post-Mortem Date | 2026-03-18 |
| Facilitator | AI Platform Lead |
| Attendees | On-call engineer, AI Risk Analyst, RAG pipeline owner, Product Owner |

### Root Cause

The document refresh pipeline authentication token expired on 2026-03-01. The token had been manually provisioned with a 90-day expiry during initial setup and was not included in the automated credential rotation process. When the token expired, the pipeline failed silently — no error alerting had been configured on the pipeline itself.

The stale documents persisted for 2 weeks. The rolling 7-day hallucination rate rose gradually, from 0.8% to 1.1%, and crossed the 1% alert line on 2026-03-15. The 24-hour rate peaked at 1.5%, below the 2% P1 line. The rate crept upward as more customer queries hit the outdated fee information.

### Contributing Factors

1. **No monitoring on document refresh pipeline health.** Output quality monitoring caught the downstream effect but not the upstream cause.
2. **Auth token manually provisioned with 90-day expiry.** Not included in automated credential rotation.
3. **Gradual drift pattern.** The threshold breach took approximately 2 weeks to manifest, as only a subset of queries were affected by the stale documents.

### What Went Well

- Automated hallucination rate monitoring caught the breach before it became severe
- On-call engineer acknowledged the alert within 23 minutes (SLA: 1 hour for P2)
- Root cause identified 68 minutes after the alert
- Stale documents replaced 2 hours 23 minutes after the alert; hallucination rate on new traffic back at baseline by 17:30, about 3 hours after the alert
- No customer escalation beyond the 2 existing complaints

### What Did Not Go Well

- The pipeline had been failing silently for 2 weeks before detection
- Auth token provisioning was a manual process with no renewal alerting
- No integration test existed to verify document freshness

### Systemic Improvements

| # | Improvement | Owner | Due Date | Status |
|---|------------|-------|----------|--------|
| 1 | Add health monitoring to document refresh pipeline | RAG pipeline owner | 2026-04-01 | Complete |
| 2 | Automate auth token renewal for RAG service accounts | Platform engineering | 2026-04-15 | Complete |
| 3 | Add document freshness check to weekly metrics | AI Operations | 2026-04-01 | Complete |
| 4 | Review all T1 RAG pipelines for similar silent failure risks | AI Operations | 2026-05-01 | In progress |

### Control Gap Assessment

Monitoring standards (PM-004) cover output quality metrics but did not require upstream data pipeline health monitoring. This incident exposed a gap: a RAG system's output quality is a lagging indicator of data pipeline health. By the time hallucination rates breach thresholds, stale data may have been served for days or weeks.

**Recommendation:** Add pipeline health monitoring as a standard requirement for all RAG-based systems. Specifically:

1. All document refresh pipelines must have health checks with P2 alerting on failure
2. Document freshness (last successful refresh timestamp) must be included in the system dashboard
3. Auth credentials for pipeline service accounts must be managed through the automated credential rotation system

This recommendation was accepted by the AI Risk Committee on 2026-04-01 and has been incorporated into the LLM monitoring standard: see [RAG Pipeline Health](../../framework/llm-lifecycle/monitoring.md#rag-pipeline-health).

---

## Document Control

| Field | Value |
|-------|-------|
| Document ID | GCF-2025-CS-001 |
| Classification | Internal / Confidential |
| Created | 2025-09-15 |
| Last Updated | 2026-04-01 |
| Owner | AI Platform Engineering Lead |
| Review Cycle | Quarterly (aligned with system review) |
| Next Review | 2026-06-10 |
| Retention | Governance record: life of the system plus 7 years after retirement ([retention periods](../../framework/compliance/audit-trail-requirements.md#retention-periods)) |

### Related Documents

| Document | Reference |
|----------|-----------|
| Risk Assessment | [risk-assessment.md](risk-assessment.md) |
| Impact Assessment | IA-2025-CS-001 |
| Model Card | [model-card.yaml](model-card.yaml) |
| DPIA | DPIA-2025-CS-001 |
| Architecture Document | ARCH-2025-CS-001 |
| Model Selection | MS-2025-CS-001, MS-2025-CS-002 |
| Red-Team Reports | RT-2025-CS-001, RT-2025-CS-002, RT-2026-CS-001 (Confidential) |
| Security Assessment | SEC-2025-CS-001 |
| Gate Evidence Package | GEP-2025-CS-001 |
| Incident Response Playbook | CS-ASSIST-IRP-v1.0 |
| Vendor Risk Assessments | VRA-2025-ANT-001, VRA-2025-GCP-001 |
| Validation Report | MRM-2025-CS-001 (addendum MRM-2025-CS-001-A1) |
