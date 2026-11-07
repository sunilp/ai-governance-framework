# Risk Assessment: Internal Knowledge Search

## System Overview

| Field | Value |
|-------|-------|
| System Name | Internal Knowledge Search |
| System ID | knowledge-search-v1.0 |
| Business Unit | IT Services |
| Assessment Date | 2026-02-10 |
| Prepared by | Product Owner, IT Services |
| Risk assessment approved by | AI Platform Team Lead (team lead), 2026-02-11 |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **Medium (2)** | Incorrect answers about internal policies cause confusion but no financial, legal, or safety harm. Users can verify via source documents. |
| Data Exposure Risk | **Medium (2)** | Internal documents only: no customer PII, no MNPI, no regulated data in knowledge base. Employee queries may contain internal context. |
| Prompt Injection Susceptibility | **Low (1)** | Internal users only with controlled access. No connection to external systems. Basic input validation in place. |
| Output Controllability | **Low (1)** | Output is informational only. Users make their own decisions. No downstream system consumes outputs. |
| Third-Party Model Dependency | **Medium (2)** | Anthropic Claude API. Service degradation is acceptable: employees can search documents manually. No business-critical dependency. |

**Highest Dimension: Medium (2)**
**Aggregate Score: 8** (context only; does not set the tier)

### Risk Tier Determination

**Tier: T3 (Medium)**

Override check against the [canonical override list](../../framework/risk-classification/genai-risk-matrix.md#tier-override-rules):
- [ ] 1. Regulated decisions: *No. Employment decisions are out of scope.*
- [ ] 2. Customer-facing content without per-output review: *No. Employees only.*
- [ ] 3. Customer personal data through an external LLM API without all four safeguards: *No. No customer personal data. Employee queries go to the Anthropic API under a DPA with zero retention.*
- [ ] 4. Agentic write access or authority: *No. No tool access.*
- [ ] 5. Biometric, deepfake-capable media, voice cloning, medical imagery: *No.*
- [ ] 6 to 9 (minimum T2 items): *No.*

No override applies. The highest-scoring dimension is Medium, so the tier is T3.

---

## Risk Analysis

### Hallucination Risk

**Scenario:** System provides incorrect policy information (e.g., wrong number of vacation days, incorrect IT security procedure).

**Likelihood:** Medium (RAG reduces but does not eliminate hallucination)
**Impact:** Low (users can verify; no regulated decision; no customer impact)
**Residual risk after mitigation:** Low

**Mitigations:**
1. All answers include source document citation; user can click through to verify
2. Disclaimer on every response: search assistant, not authoritative source
3. Hallucination rate tracked through 5% sampled automated scoring and the monthly metrics review; T3 cap ≤ 5%
4. Knowledge base documents reviewed and refreshed weekly

### Data Leakage Risk

**Scenario:** System reveals internal policy information to unauthorized employee, or employee inputs sensitive information in queries.

**Likelihood:** Low (all employees are authorized users; knowledge base contains non-sensitive internal documents)
**Impact:** Low (internal information, not customer data or MNPI)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. Access restricted to authenticated employees only
2. Knowledge base contains non-sensitive operational documents only
3. Queries and responses logged per audit trail requirements (3-year retention for T3); PII-bearing fields (employee name, role) tokenized before storage; access to logs restricted to AI Operations and Compliance
4. No customer PII or MNPI in the knowledge base

### Prompt Injection Risk

**Scenario:** Employee attempts to manipulate the system via adversarial prompts.

**Likelihood:** Very Low (internal users with authenticated access; no external exposure; low motivation)
**Impact:** Low (system is informational only; no downstream actions; no customer impact)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. Basic input validation
2. System prompt instructs model to answer only from retrieved documents
3. No tool access or action capability: read-only information retrieval
4. Red-team completed pre-deployment: automated adversarial scan (200 generated prompts) plus 50 manual cases

---

## T3 Governance Requirements

This system demonstrates proportional governance: T3 controls are lighter than T1/T2.

| Requirement | T3 Standard | This System |
|-------------|------------|-------------|
| Model selection | Approved vendor list | Anthropic (approved vendor) |
| Prompt governance | Prompts stored in version control | Git repository |
| Guardrails | Basic input validation | Input validation active |
| Evaluation | Pre-deployment and safety eval; 5% sampled automated scoring in production | 50-case pre-release suite, 50-case safety suite, 50-query retrieval set; 5% of responses scored automatically |
| Monitoring | Monthly metrics review | Monthly metrics review (usage, quality, cost), including a human spot-check of 50 sampled responses |
| Human oversight | Appropriate to use case | Human-on-the-loop (Pattern 2): answers go straight to employees; a sample is reviewed monthly |
| Audit trail | Summary logging; 3-year retention | Query/response logging; 3-year retention |
| DPIA screening (RA-005) | Required where personal data is processed | Completed 2026-02-09: not high risk; full DPIA not required (see below) |
| Review cadence | Annual governance review | Next review: 2027-02-15 |
| Red-teaming | Automated adversarial scan + 50 manual cases | Completed 2026-02-12: 200-prompt automated scan plus 50 manual cases |
| Board reporting | Not required | Not included in board pack |
| Independent validation | Peer review | Peer review by an AI Platform engineer outside the build team |

### Comparison with T1 Governance

For context, here is what a T1 system (e.g., the [agentic research assistant](../agentic-research-assistant)) requires that this T3 system does not:

| T1 Requirement | T3 Equivalent |
|---------------|---------------|
| AI Risk Committee approval | Team lead approval |
| Full adversarial red-team (200+ cases, including manual testing) | Automated adversarial scan + 50 manual cases |
| Quarterly governance review | Annual governance review |
| Independent validation by Model Risk Management | Peer review |
| Board-level reporting | Not required |
| Quarterly red-team retesting | Annual automated rescan |
| Automated scoring of every response | 5% sampled automated scoring; monthly metrics review |
| 7-year audit trail retention | 3-year retention |
| Mandatory fallback model | Not required (degradation acceptable) |

This is governance scaling as intended. Not every AI system needs T1 treatment.

---

## Conditions of Approval

1. Knowledge base must not contain customer PII, MNPI, or regulated data
2. System must display disclaimer that it is a search assistant, not an authoritative source
3. Monthly metrics review, including a human spot-check of 50 sampled responses
4. Annual governance review (next: 2027-02-15)
5. If scope expands to customer-facing or regulated content, re-assess and expect tier upgrade
6. Re-run DPIA screening if query logs are used for anything beyond audit and service quality (for example, monitoring individual employees)

---

## DPIA Screening (RA-005)

Every system that processes personal data gets a DPIA screening. A full DPIA is needed only where screening indicates high risk (always for T1/T2).

| Field | Value |
|-------|-------|
| Screening date | 2026-02-09 |
| Screened by | Data Protection Office (DPO delegate) |
| Personal data | Employee name and role in query logs; incidental personal data employees may type into queries |
| Data subjects | Employees |
| Purpose | Audit trail and service quality |
| High-risk indicators | None: no profiling, no automated decisions about employees, no special-category data in the knowledge base, no systematic monitoring |
| Outcome | Not high risk. Full DPIA not required. |
| Conditions | Name and role tokenized before storage; log access limited to AI Operations and Compliance; 3-year retention (T3); queries sent to the Anthropic API under a DPA with zero retention |
