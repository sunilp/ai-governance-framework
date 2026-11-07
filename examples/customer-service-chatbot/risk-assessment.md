# Risk Assessment: Retail Banking Customer Service Assistant

## System Overview

| Field | Value |
|-------|-------|
| System Name | Retail Banking Customer Service Assistant |
| System ID | cs-assistant-retail-v1.2 |
| Business Unit | Retail Banking Digital |
| Assessment Date | 2025-07-18 |
| Prepared by | Product Owner, Retail Banking Digital (with AI Risk Analyst support) |
| Approved by | AI Risk Committee, 2025-07-29 |
| Last Re-assessment | 2026-03-10 (Q1 2026 governance review): tier unchanged |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect information about account balances, fees, or product terms could cause customer harm. However, the system does not make decisions — it provides information. |
| Data Exposure Risk | **Critical (4)** | Customer PII (names, account details, transaction history) flows through the LLM pipeline. PII redaction is applied pre-API but residual risk exists. |
| Prompt Injection Susceptibility | **High (3)** | Customer-facing with unrestricted text input. Input validation and injection detection are in place but cannot guarantee 100% coverage. |
| Output Controllability | **High (3)** | Outputs are delivered to customers after automated guardrail checks but without individual human review. Guardrails catch known patterns but not novel failure modes. |
| Third-Party Model Dependency | **High (3)** | Primary model is Anthropic Claude, served through Vertex AI in the EU region. Fallback to Gemini 2.5 Pro on Vertex AI is validated. Single-vendor dependency for primary path. |

**Aggregate Score: 16** (recorded for context; it does not set the tier)
**Highest Dimension: Critical (4)**, so the scored tier is T1

### Risk Tier Determination

**Tier: T1 (Critical)**

Override check against the canonical list in the [GenAI risk matrix](../../framework/risk-classification/genai-risk-matrix.md#risk-tier-determination-for-genai):

Automatic T1:
- [ ] 1. Makes or directly influences regulated decisions: *No. Informational only; no credit, insurance, AML/sanctions or employment decisions.*
- [x] 2. Generates customer-facing content delivered without per-output human review: *Yes. This trigger makes the system T1.*
- [ ] 3. Processes customer personal data through an external LLM API without all four safeguards: *No. All four safeguards are in place (see below), so item 8 applies instead.*
- [ ] 4. Agentic behaviour with write access to production systems or data stores, or authority to move money, communicate with customers, or change identity and access: *No. Not agentic; the account API is read-only.*
- [ ] 5. Biometric identification or categorisation, deepfake-capable synthetic media, voice cloning, or medical imagery: *No.*

Minimum T2:
- [ ] 6. Any agentic or multi-agent system, including read-only tool use: *No. Fixed orchestration; the model does not call tools. The application fetches account context through a read-only API.*
- [ ] 7. Synthetic media generation: *No. Text only.*
- [x] 8. Customer personal data through an external LLM API with all four safeguards in place: *Yes. Minimum T2.*
- [ ] 9. Personal data in visual content: *No. Text only.*

Safeguards in place for item 3 (all four required to stay out of automatic T1):

| Safeguard | Status | Evidence |
|-----------|--------|----------|
| Zero data retention by the vendor | In place | Zero-retention API terms, VRA-2025-ANT-001 |
| Regional endpoint that meets data residency requirements | In place | Vertex AI EU region, confirmed at architecture review 2025-08-05 |
| Signed DPA | In place | DPA covering Vertex AI processing executed with Google Cloud |
| PII redaction or minimisation before the call | In place | Input guardrails redact PII in free text; account context is limited to the fields needed for the answer |

**Result:** T1. The scored tier is T1 (Data Exposure is Critical), and override trigger 2 also requires T1. Under the [pattern selection matrix](../../framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix), the system uses Pattern 3 (human-over-the-loop) with all five T1 safeguards in place; see the [case file](governance-case-file.md), Section 10.

### Re-assessment History

| Date | Trigger | Result |
|------|---------|--------|
| 2025-12-10 | Q4 2025 governance review | Tier unchanged (T1) |
| 2025-12-17 | Material change: base model migration for v1.2.0 | Tier unchanged (T1) |
| 2026-03-10 | Q1 2026 governance review | Tier unchanged (T1) |

---

## Detailed Risk Analysis

### Hallucination Risk

**Scenario:** System provides incorrect fee information, leading customer to make financial decision based on wrong data.

**Likelihood:** Low (RAG-grounded with verified document corpus; hallucination rate measured at 0.2% before release, 1 of 500 cases with a 95% upper bound of 0.95%)
**Impact:** Medium-High (potential financial loss to customer; regulatory complaint)
**Residual risk after mitigation:** Medium

**Mitigations:**
1. RAG retrieval from verified, version-controlled document corpus
2. System prompt instructs "only answer based on provided documents; say 'I don't have that information' otherwise"
3. Automated faithfulness evaluation on every response (async)
4. Daily sampled human review of 5% of responses (never fewer than 50 a day)
5. Financial figures sourced from account API, not generated by LLM
6. Refresh pipeline health monitoring with P2 alert on failure (added after incident GEN-2026-042)

### Prompt Injection Risk

**Scenario:** Malicious customer crafts input that causes system to reveal system prompt, other customers' data, or behave outside intended scope.

**Likelihood:** Medium (publicly accessible; sophisticated attacks possible)
**Impact:** High (data leakage, reputational damage, regulatory consequences)
**Residual risk after mitigation:** Medium-Low

**Mitigations:**
1. Input validation layer with injection pattern detection
2. System prompt isolation (not in user-accessible context)
3. Output guardrails filter for sensitive data patterns
4. PII redaction applied to both input and output
5. Regular red-team testing (quarterly)
6. Rate limiting per customer session

### Data Leakage Risk

**Scenario:** LLM response inadvertently includes PII from other customers (cross-contamination) or reveals internal system details.

**Likelihood:** Very Low (session isolation; no persistent memory across customers)
**Impact:** Critical (GDPR breach, regulatory consequences)
**Residual risk after mitigation:** Low

**Mitigations:**
1. Session isolation — no shared context between customers
2. No persistent memory across sessions
3. PII redaction on output
4. Customer data retrieved via authenticated API scoped to requesting customer
5. RAG corpus contains no customer-specific data
6. Zero data retention configured for model inference (prompts and responses not stored by the provider)

### Bias Risk

**Scenario:** System provides different quality of service or different tone based on customer demographics (inferred from name, language, query patterns).

**Likelihood:** Low (base model has residual biases; prompt design mitigates)
**Impact:** Medium (regulatory complaint, discrimination claim)
**Residual risk after mitigation:** Low

**Mitigations:**
1. Counterfactual testing across gender, age, nationality, language (200 pairs per attribute)
2. Sentiment parity monitoring in production
3. System prompt emphasizes equal, respectful treatment
4. Formal bias evaluation quarterly; production counterfactual spot-checks weekly (since v1.2.0)

---

## Governance Requirements (T1)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| AI Risk Committee approval | Complete | Risk assessment approved 2025-07-29; deployment approved 2025-09-10 |
| CISO sign-off | Complete | Deployment sign-off 2025-09-09; security assessment SEC-2025-CS-001 |
| DPO sign-off | Complete | DPIA-2025-CS-001 filed 2025-07-25; deployment sign-off 2025-09-09 (with conditions) |
| Independent validation | Complete | Validation report MRM-2025-CS-001 (2025-09-03) |
| Deployment evidence pack | Complete | Gate evidence package GEP-2025-CS-001, against the T1 [minimum evidence pack](../../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier) |
| Full prompt/response audit logging | Active | 7-year retention (T1 interaction logs, [retention requirements](../../framework/compliance/prompt-audit-trail.md#retention-requirements)), append-only |
| Governance record retention | Set | Life of the system plus 7 years after retirement ([retention periods](../../framework/compliance/audit-trail-requirements.md#retention-periods)) |
| Real-time quality monitoring | Active | Faithfulness eval on every response |
| Human oversight (Pattern 3 with all five T1 safeguards) | Active | Case file Section 10; last kill switch test 2026-03-04 |
| Fallback model validated | Complete | Gemini 2.5 Pro tested and validated |
| Incident response playbook | Published | Runbook CS-ASSIST-IRP-v1.0 |
| Monthly metrics review; quarterly governance review | Active | Next governance review: 2026-06-10 |
| Independent revalidation (annual and on material change) | Scheduled | Last: 2026-01-09 for the v1.2.0 material change (MRM-2025-CS-001-A1). Next annual revalidation due by 2026-09-03 |

---

## Risk Acceptance

**Residual risks accepted by AI Risk Committee (2025-09-10):**

1. Hallucination rate of ≤ 1% — accepted given RAG grounding, monitoring, and human spot-checks
2. Prompt injection residual risk — accepted given multi-layer defense and quarterly red-teaming
3. Vendor dependency on Anthropic — accepted given validated fallback and exit strategy

**Conditions:**
- Monthly hallucination rate reporting to AI Risk Committee
- P2 alert to on-call and AI Risk if the rolling 7-day hallucination rate exceeds 1%; P1 alert if the rolling 24-hour rate exceeds 2%
- Quarterly red-team testing with external security team
- Annual re-assessment of vendor risk
