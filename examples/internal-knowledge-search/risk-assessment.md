# Risk Assessment: Internal Knowledge Search

## System Overview

| Field | Value |
|-------|-------|
| System Name | Internal Knowledge Search |
| System ID | knowledge-search-v1.0 |
| Business Unit | IT Services |
| Assessment Date | 2026-02-10 |
| Assessor | AI Operations Analyst |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **Medium (2)** | Incorrect answers about internal policies cause confusion but no financial, legal, or safety harm. Users can verify via source documents. |
| Data Exposure Risk | **Medium (2)** | Internal documents only — no customer PII, no MNPI, no regulated data in knowledge base. Employee queries may contain internal context. |
| Prompt Injection Susceptibility | **Low (1)** | Internal users only with controlled access. No connection to external systems. Basic input validation in place. |
| Output Controllability | **Low (1)** | Output is informational only. Users make their own decisions. No downstream system consumes outputs. |
| Third-Party Model Dependency | **Medium (2)** | Anthropic Claude API. Service degradation is acceptable — employees can search documents manually. No business-critical dependency. |

**Aggregate Score: 8**
**Highest Dimension: Medium (2)**

### Risk Tier Determination

**Tier: T3 — Medium**

Automatic T1 trigger check:
- [ ] Processes customer PII through external LLM API — *No*
- [ ] Generates customer-facing content without human review — *No*
- [ ] Makes or influences regulated decisions — *No*
- [ ] Involves agentic behavior with production system access — *No*

No automatic tier overrides apply. System remains at T3 based on aggregate score.

---

## Risk Analysis

### Hallucination Risk

**Scenario:** System provides incorrect policy information (e.g., wrong number of vacation days, incorrect IT security procedure).

**Likelihood:** Medium (RAG reduces but does not eliminate hallucination)
**Impact:** Low (users can verify; no regulated decision; no customer impact)
**Residual risk after mitigation:** Low

**Mitigations:**
1. All answers include source document citation — user can click through to verify
2. Disclaimer on every response: search assistant, not authoritative source
3. Hallucination rate monitored monthly; threshold set at ≤ 5%
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
3. No tool access or action capability — read-only information retrieval
4. Automated adversarial scan completed pre-deployment (30 test cases)

---

## T3 Governance Requirements

This system demonstrates proportional governance — T3 controls are lighter than T1/T2.

| Requirement | T3 Standard | This System |
|-------------|------------|-------------|
| Model selection | Approved vendor list | Anthropic (approved vendor) |
| Prompt governance | Prompts stored in version control | Git repository |
| Guardrails | Basic input validation | Input validation active |
| Evaluation | Pre-deployment eval; monthly spot checks | 50-case eval suite; monthly spot-check of 50 responses |
| Monitoring | Weekly metrics review | Weekly usage metrics; monthly quality spot-check |
| Human oversight | Appropriate to use case | Human-on-the-loop (users evaluate answers themselves) |
| Audit trail | Summary logging; 3-year retention | Query/response logging; 3-year retention |
| Review cadence | Semi-annual review | Next review: 2026-08-15 |
| Red-teaming | Automated scan | Automated adversarial scan completed |
| Board reporting | Not required | Not included in board pack |
| Independent validation | Not required | Not performed |

### Comparison with T1 Governance

For context, here is what a T1 system (e.g., the [agentic research assistant](../agentic-research-assistant)) requires that this T3 system does not:

| T1 Requirement | T3 Equivalent |
|---------------|---------------|
| AI Risk Committee approval | Team lead approval |
| Full adversarial red-team (200+ cases) | Automated scan (30 cases) |
| Monthly review | Semi-annual review |
| Independent validation | Not required |
| Board-level reporting | Not required |
| Quarterly red-team retesting | Annual automated rescan |
| Real-time quality monitoring (every response) | Monthly spot-check |
| 7-year audit trail retention | 3-year retention |
| Mandatory fallback model | Not required (degradation acceptable) |

This is governance scaling as intended. Not every AI system needs T1 treatment.

---

## Conditions of Approval

1. Knowledge base must not contain customer PII, MNPI, or regulated data
2. System must display disclaimer that it is a search assistant, not an authoritative source
3. Monthly quality spot-check of 50 responses
4. Semi-annual review (next: 2026-08-15)
5. If scope expands to customer-facing or regulated content, re-assess and expect tier upgrade
