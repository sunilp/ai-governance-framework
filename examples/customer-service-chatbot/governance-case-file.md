# Governance Case File: Retail Banking Customer Service Assistant

**System ID:** cs-assistant-retail-v1.2
**Risk Tier:** T1 (Critical)
**Status:** Production (deployed 2025-09-15)

This document is the complete governance trail from idea intake through the first year of production operations. It demonstrates every governance artifact produced for a T1 customer-facing GenAI system. Teams can use this structure as a template for their own systems.

---

## 1. Intake Record (Stage 1)

*Pre-register artifact — no Control ID. See governance-workflow.md Stage 1.*

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

### Dimension Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect information about account balances, fees, or product terms could cause customer harm. System does not make decisions — it provides information. |
| Data Exposure Risk | **Critical (4)** | Customer PII (names, account details, transaction history) flows through the LLM pipeline. PII redaction is applied pre-API but residual risk exists. |
| Prompt Injection Susceptibility | **High (3)** | Customer-facing with unrestricted text input. Input validation and injection detection are in place but cannot guarantee 100% coverage. |
| Output Controllability | **High (3)** | Outputs are delivered to customers after automated guardrail checks but without individual human review. Guardrails catch known patterns but not novel failure modes. |
| Third-Party Model Dependency | **High (3)** | Primary model is Anthropic Claude via API. Fallback to Gemini 1.5 Pro on Vertex AI is validated. Single-vendor dependency for primary path. |

**Aggregate Score:** 16
**Highest Dimension:** Critical (4)

### Risk Tier Determination

**Tier: T1 — Critical**

Automatic T1 triggers:
- Processes customer PII through external LLM API
- Generates customer-facing content without individual human review

### Risk Acceptance Conditions

Residual risks accepted by AI Risk Committee (2025-09-01):

1. Hallucination rate of ≤ 1% — accepted given RAG grounding, monitoring, and human spot-checks
2. Prompt injection residual risk — accepted given multi-layer defense and quarterly red-teaming
3. Vendor dependency on Anthropic — accepted given validated fallback and exit strategy

Standing conditions:
- Monthly hallucination rate reporting to AI Risk Committee
- Immediate escalation if hallucination rate exceeds 1% in any rolling 7-day window
- Quarterly red-team testing with external security team
- Annual re-assessment of vendor risk

---

## 3. Architecture Review Record (Stage 3)

*Control IDs: AR-001, AR-002, AR-003, AR-004, AR-005*

| Field | Value |
|-------|-------|
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
| LLM API endpoint | Anthropic EU endpoint | Confirmed |
| RAG corpus (BigQuery Vector Search) | EU | Confirmed |

### Vendor Assessment

Anthropic vendor risk assessment completed — reference VRA-2025-ANT-001. Key findings:

- Zero-retention API confirmed (data not stored by vendor)
- Training data exclusion clause in place
- DPA executed
- SLA: 99.9% uptime

---

## 4. Model Card Summary (Stage 4)

*Control IDs: DE-001, DE-002, DE-004*

Full model card documented in [model-card.yaml](model-card.yaml).

| Field | Value |
|-------|-------|
| System Name | Retail Banking Customer Service Assistant |
| Model ID | cs-assistant-retail-v1.2 |
| Base Model | Claude 3.5 Sonnet (claude-3-5-sonnet-20241022) |
| Base Model Provider | Anthropic |
| Hosting | Vendor API (zero retention) |
| System Prompt Version | v1.2.3 |
| Prompt Repository | git://internal/ai-prompts/cs-assistant |
| Decision Type | Assistive |
| Human Oversight Pattern | Human-over-the-loop |

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

*Control ID: DE-003*

| Field | Value |
|-------|-------|
| Reviewer | Senior AI Engineer, AI Platform team |
| Prompt Version | v1.2.3 |
| Review Date | 2025-08-20 |

### Review Findings

| # | Finding | Severity | Resolution |
|---|---------|----------|------------|
| 1 | Fallback response for unrecognized intent too vague — should offer escalation | Minor | Updated to offer human agent connection |
| 2 | Edge case: multi-language query mixing not handled | Minor | Added language detection; mixed-language queries route to human agent |

### Review Outcome

The prompt was updated to address both findings. Regression testing confirmed no negative impact on existing evaluation metrics. The updated prompt (v1.2.3) incorporates red-team findings from Section 7.

**Sign-off:** Senior AI Engineer, 2025-08-22

---

## 6. Evaluation Report (Stage 5)

*Control IDs: EV-001, EV-002, EV-003, EV-004, EV-005, EV-006, EV-007*

### Evaluation Parameters

| Parameter | Value |
|-----------|-------|
| Evaluation Date | 2025-09-01 |
| Evaluation Dataset Size | 500 cases |
| Training Data Overlap | None confirmed |
| Base Model | Claude 3.5 Sonnet |
| Prompt Version | v1.2.3 |

### Results

| Metric | Result | Threshold | Status | Eval Method |
|--------|--------|-----------|--------|-------------|
| Faithfulness | 0.94 | ≥ 0.90 | **PASS** | LLM-as-judge (calibrated) |
| Hallucination rate | 0.008 (0.8%) | ≤ 0.01 (1%) | **PASS** | LLM-as-judge + human eval |
| Correctness | 0.96 | ≥ 0.95 | **PASS** | Human eval |
| Safety pass rate | 0.99 | ≥ 0.99 | **PASS** | Automated (200-case safety eval suite — distinct from adversarial robustness testing) |
| Retrieval precision@5 | 0.87 | ≥ 0.85 | **PASS** | Automated |
| Counterfactual consistency | 0.95 | ≥ 0.90 | **PASS** | Automated (200 pairs x 4 attributes) |
| Escalation appropriateness | 0.93 | ≥ 0.90 | **PASS** | Human eval |

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
| Assessment Dates | 2025-08-25 to 2025-08-28 |
| Assessor | Internal AI Security + external CyberAI Ltd |
| Methodology | Manual + automated, 200 test cases, 6 categories |
| Model | Claude 3.5 Sonnet |
| Prompt Version | v1.2.0 (pre-review — findings informed v1.2.3) |

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
| High | 1 | Indirect prompt injection via RAG document: crafted FAQ with embedded instructions caused model to reveal system prompt structure. Remediated by context isolation. Retested and confirmed fixed. |
| Medium | 3 | (1) Multi-turn escalation bypass after 12 turns. Mitigated with per-turn safety classification. (2) Base64-encoded harmful request processed. Mitigated with input normalization. (3) System disclosed Claude usage when asked. Accepted as low impact. |
| Low | 5 | Minor boundary softening under edge conditions. Tracked. |

### Gate Decision

**Conditional pass** — High finding remediated and retested. Medium findings (1) and (2) remediated; medium finding (3) accepted as low impact (model identity is not a protected secret, and transparency obligations under EU AI Act Article 50 require disclosure of AI interaction).

Full report: **RT-2025-CS-001** (Confidential)

---

## 8. Deployment Approval (Stage 7)

*Control IDs: DA-001, DA-002, DA-003, DA-004*

### Evidence Checklist

| # | Evidence Item | Status | Reference |
|---|--------------|--------|-----------|
| 1 | Signed risk assessment | Complete | [risk-assessment.md](risk-assessment.md) |
| 2 | Architecture review record | Complete | Section 3 |
| 3 | DPIA filed | Complete | DPIA-2025-CS-001 |
| 4 | Model card | Complete | [model-card.yaml](model-card.yaml) |
| 5 | Prompt review record | Complete | Section 5 |
| 6 | Evaluation report | Complete | Section 6 |
| 7 | Red-team report | Complete | RT-2025-CS-001 |
| 8 | Security assessment | Complete | SEC-2025-CS-001 |
| 9 | Monitoring configuration | Complete | Section 9 |
| 10 | Incident response playbook | Complete | CS-ASSIST-IRP-v1.0 |
| 11 | Rollback plan | Complete | Rollback to v1.1.0 tested 2025-09-10 |
| 12 | Deployment approval | Complete | Signatures below |

### Sign-Off Chain

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

## 9. Monitoring Configuration (Stage 8)

*Control IDs: PM-001, PM-002, PM-003, PM-004, PM-005*

### Monitoring Metrics

| Metric | Threshold | Alert Severity | Notification |
|--------|-----------|----------------|-------------|
| Hallucination rate (rolling 7-day) | > 1% | P1 | On-call + AI Risk |
| PII leakage detection | Any occurrence | P1 | On-call + CISO |
| Guardrail trigger rate | > 2σ from baseline | P2 | On-call + team lead |
| Latency p95 | > 3000ms | P2 | On-call |
| Error rate | > 1% | P2 | On-call |
| Daily spend | > €700 | P3 | Team lead + finance |
| User satisfaction (thumbs down) | > 15% | P3 | Product owner |

### Operational Configuration

| Parameter | Value |
|-----------|-------|
| Dashboard | internal://dashboards/cs-assistant |
| On-call team | AI Platform On-Call |
| Escalation path | On-call → AI Platform Lead → Head of AI → CTO |
| Quality monitoring | Every response (async LLM-as-judge) |
| Safety monitoring | Real-time guardrail monitoring |
| Cost monitoring | Real-time with daily budget alerts |
| Drift detection | Daily evaluation on 100 canonical queries |

### Alert Response SLAs

| Severity | Acknowledge | Investigate | Mitigate |
|----------|-------------|-------------|----------|
| P1 | 15 min | 1 hour | 4 hours |
| P2 | 1 hour | 4 hours | 24 hours |
| P3 | 4 hours | 1 business day | 5 business days |

---

## 10. Q1 2026 Review — Post v1.2.0 Deployment (Stage 9)

*Control IDs: RV-001, RV-002*

| Field | Value |
|-------|-------|
| Review Date | 2026-04-01 |
| Attendees | AI Platform Lead, AI Risk Analyst, Product Owner, Head of Retail Banking Digital |
| Review Period | 2026-01-10 to 2026-04-01 |
| System Version | v1.2.0 |

### Operational Summary

| Metric | Value |
|--------|-------|
| Total interactions | 142,000 |
| Escalation rate | 18% |
| Average resolution time | 1.4 min |
| User satisfaction (thumbs up) | 82% |
| Availability | 99.94% |

### Findings

| # | Finding | Severity | Action | Status |
|---|---------|----------|--------|--------|
| 1 | Hallucination rate crept from 0.8% to 1.1% in week of 2026-03-15, breaching T1 threshold of 1.0%. Escalation triggered per risk acceptance conditions. AI Risk notified within 4 hours. Enhanced monitoring activated. Root cause: 3 outdated product documents in RAG corpus. Corpus refreshed; re-eval confirmed rate returned to 0.7%. Pipeline health monitoring added. | Medium | Complete | Resolved |
| 2 | German language accuracy lower than English (faithfulness 0.88 vs. 0.94) | Low | Schedule targeted German eval expansion (100 additional cases) | Due 2026-05-15 |
| 3 | Cost per request trending 8% above baseline (€0.032 vs. €0.03) | Low | Investigate prompt optimization | Due 2026-05-01 |

### Review Decision

The system continues to operate within acceptable risk parameters. Finding 1 was resolved during the review period. The hallucination rate breach validated that the monitoring and escalation controls work as designed — the incident was detected automatically, AI Risk was notified within SLA, and the root cause was resolved within 20 hours.

**Next scheduled review:** 2026-07-01

---

## 11. Example Incident: S3 Hallucination — GEN-2026-042 (Stage 8/9)

*Control IDs: IR-003, PM-004*

### Incident Summary

| Field | Value |
|-------|-------|
| Incident ID | GEN-2026-042 |
| Severity | S3 |
| System | cs-assistant-retail-v1.2 |
| Detection Time | 2026-03-15 14:22 UTC |
| Detection Method | Automated monitoring — hallucination rate P2 alert |
| Mitigation Time | 2026-03-15 16:45 UTC |
| Resolution Time | 2026-03-16 10:00 UTC |

### What Happened

Automated monitoring flagged a hallucination rate spike from 0.8% to 1.5% over a rolling 24-hour window. Investigation identified that 3 documents in the RAG corpus contained outdated fee information — specifically, fee schedules for current accounts, savings accounts, and international transfers that had been updated on 2026-03-01 but not reflected in the corpus.

The document refresh pipeline had failed silently for 2 weeks due to an authentication token expiration on 2026-03-01. The pipeline did not have health monitoring configured, so no alert was raised when it stopped running.

### Customer Impact

- Approximately 40 customers received incorrect fee information over the 2-week window
- No financial transactions were affected (system is informational only — it does not execute transactions)
- 2 customer complaints received via normal support channels
- No regulatory reporting required (informational error, no financial harm)

### Timeline

| Time (UTC) | Event |
|------------|-------|
| 2026-03-15 14:22 | Automated monitoring triggers P2 alert: hallucination rate at 1.5% (threshold: 1%) |
| 2026-03-15 14:45 | On-call engineer acknowledges alert, begins investigation |
| 2026-03-15 15:30 | Root cause identified: 3 stale documents in RAG corpus; document refresh pipeline down since 2026-03-01 |
| 2026-03-15 16:45 | Stale documents replaced manually; RAG index refreshed |
| 2026-03-15 17:30 | Hallucination rate returned to 0.7% (confirmed via real-time monitoring) |
| 2026-03-16 10:00 | Pipeline failure root-caused (auth token expiration); auth renewal automated |

### Severity Justification

Classified as S3 (not S2) because:
- System is informational only — no financial transactions executed based on incorrect information
- Customer harm was limited to receiving incorrect fee quotes
- Self-healing once documents were refreshed
- No regulatory reporting obligation triggered

---

## 12. Post-Mortem — GEN-2026-042 (Stage 8/9)

*Control IDs: IR-004, IR-005*

| Field | Value |
|-------|-------|
| Post-Mortem Date | 2026-03-18 |
| Facilitator | AI Platform Lead |
| Attendees | On-call engineer, AI Risk Analyst, RAG pipeline owner, Product Owner |

### Root Cause

The document refresh pipeline authentication token expired on 2026-03-01. The token had been manually provisioned with a 90-day expiry during initial setup and was not included in the automated credential rotation process. When the token expired, the pipeline failed silently — no error alerting had been configured on the pipeline itself.

The stale documents persisted for 2 weeks. The gradual drift in hallucination rate (from 0.8% to 1.5%) meant the monitoring threshold was not breached immediately — the rate crept upward as more customer queries hit the outdated fee information.

### Contributing Factors

1. **No monitoring on document refresh pipeline health.** Output quality monitoring caught the downstream effect but not the upstream cause.
2. **Auth token manually provisioned with 90-day expiry.** Not included in automated credential rotation.
3. **Gradual drift pattern.** The threshold breach took approximately 2 weeks to manifest, as only a subset of queries were affected by the stale documents.

### What Went Well

- Automated hallucination rate monitoring caught the breach before it became severe
- On-call engineer acknowledged the alert within 23 minutes (SLA: 1 hour for P2)
- Root cause identified within 1.5 hours
- Full resolution (documents refreshed, rate returned to baseline) within 2.5 hours
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

This recommendation was accepted by the AI Risk Committee on 2026-04-01 and will be incorporated into the monitoring standards for all T1 and T2 RAG systems.

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
| Next Review | 2026-07-01 |

### Related Documents

| Document | Reference |
|----------|-----------|
| Risk Assessment | [risk-assessment.md](risk-assessment.md) |
| Model Card | [model-card.yaml](model-card.yaml) |
| DPIA | DPIA-2025-CS-001 |
| Red-Team Report | RT-2025-CS-001 (Confidential) |
| Security Assessment | SEC-2025-CS-001 |
| Incident Response Playbook | CS-ASSIST-IRP-v1.0 |
| Vendor Risk Assessment | VRA-2025-ANT-001 |
| Validation Report | MRM-2025-CS-001 |
