# Hallucination Policy

## Overview

Hallucination — the generation of plausible-sounding but factually incorrect, unsupported, or fabricated content — is an inherent characteristic of large language models. It cannot be eliminated, only managed.

This policy defines organizational tolerance for hallucination, measurement standards, mitigation requirements, and disclosure obligations.

---

## Definitions

| Term | Definition |
|------|-----------|
| Hallucination | Model output that is not grounded in the provided context, training data, or factual reality |
| Intrinsic hallucination | Output that contradicts the provided source material |
| Extrinsic hallucination | Output that introduces claims not present in or verifiable from the provided source material |
| Confabulation | Model generates fictional details (names, dates, citations, statistics) that appear authoritative |
| Faithfulness | Degree to which output is grounded in and supported by provided context |

---

## Hallucination Tolerance by Tier and Use Case

| Tier | Maximum Hallucination Rate | Rationale |
|------|---------------------------|-----------|
| T1 — Critical | ≤ 1% (measured by faithfulness evaluation) | Outputs directly influence regulated decisions or customer communications |
| T2 — High | ≤ 3% | Outputs reviewed by qualified human before use; limited direct impact |
| T3 — Medium | ≤ 5% | Internal use; errors caught in normal workflow |
| T4 — Low | ≤ 10% | Advisory or brainstorming; user expected to verify independently |

### Use Case-Specific Overrides

| Use Case Category | Maximum Rate | Override Rationale |
|------------------|-------------|-------------------|
| Regulatory reporting or disclosure | 0% (human verification required for all outputs) | Zero tolerance for regulatory submissions |
| Customer-facing communications | ≤ 1% | Reputational and regulatory risk |
| Financial analysis and credit memos | ≤ 2% | Consequential decision support |
| Internal knowledge Q&A | ≤ 5% | Users expected to verify; low consequence |
| Content drafting (non-customer) | ≤ 8% | Human editing expected |
| Code generation | ≤ 5% (measured by functional correctness) | Code review and testing expected |

---

## Measurement Standards

### Hallucination Evaluation Methods

| Method | Description | Use When |
|--------|-------------|----------|
| LLM-as-judge (faithfulness) | A separate LLM evaluates whether the output is supported by the provided context | RAG systems; scalable automated evaluation |
| Human evaluation | Subject matter experts evaluate factual accuracy | T1 use cases; ground truth validation |
| Citation verification | Verify that cited sources exist and support the claims made | Any system that produces citations |
| Factual accuracy check | Compare claims against authoritative data sources | Systems that generate factual statements |
| Consistency testing | Run the same query multiple times; flag inconsistent answers | Detect unreliable outputs |

### Evaluation Protocol

1. **Baseline measurement:** Before deployment, measure hallucination rate on a representative test set (minimum 200 queries for T1, 100 for T2)
2. **Production monitoring:** Ongoing automated evaluation on sampled production queries
3. **Periodic human evaluation:** Scheduled human review to calibrate automated metrics
4. **Trend tracking:** Monitor hallucination rate over time; alert on degradation

---

## Mitigation Requirements

### Mandatory Mitigations (All Tiers)

| Mitigation | Description |
|-----------|-------------|
| Grounding instruction | System prompts must instruct the model to base answers on provided context and acknowledge uncertainty |
| "I don't know" enablement | The system must be able to decline to answer when confidence is low |
| Source attribution | Where applicable, outputs must cite the source material used |

### Tier-Specific Mitigations

| Mitigation | T1 | T2 | T3 | T4 |
|-----------|----|----|----|----|
| RAG with verified sources | Required | Required | Recommended | Optional |
| Automated faithfulness evaluation on every response | Required | Recommended | Optional | — |
| Human review of all outputs | Required for customer-facing | Required for external outputs | — | — |
| Confidence scoring | Required | Recommended | Optional | — |
| Output cross-verification against structured data | Required for factual claims | Recommended | — | — |
| Guardrail-based hallucination detection | Required | Required | Recommended | Optional |

### Retrieval-Augmented Generation (RAG) Requirements

For systems using RAG to reduce hallucination:

| Requirement | Standard |
|-------------|---------|
| Retrieval quality | Faithfulness score ≥ 0.9 for T1; ≥ 0.85 for T2 |
| Source currency | Retrieved documents must meet freshness requirements |
| Context sufficiency | System must detect when retrieved context is insufficient and decline to answer |
| Attribution | Every claim in the output should be traceable to a retrieved source |

---

## Disclosure Requirements

### Internal Use Cases

- System documentation must state the hallucination rate and measurement methodology
- Users must be informed that outputs may contain errors and should be verified
- Training materials must cover hallucination risk and verification procedures

### Customer-Facing Use Cases

- Customers must be informed that they are interacting with an AI system
- Outputs must include appropriate caveats (e.g., "This information is AI-generated and should be verified")
- Critical outputs (financial, legal, medical) must not be presented as authoritative without human verification
- Feedback mechanism must be available for users to report inaccurate outputs

### Regulatory and Compliance Context

- AI-generated content used in regulatory reporting must be verified by a qualified human
- Hallucination rate and mitigation measures must be documented in model risk assessments
- Audit trail must capture both the AI output and any human verification or correction

---

## Incident Response

### Hallucination Incident Classification

| Severity | Criteria | Response |
|----------|----------|----------|
| S1 — Critical | Hallucinated output caused customer harm, financial loss, or regulatory issue | Immediate system pause; incident commander assigned; root cause analysis; regulatory notification if required |
| S2 — High | Hallucinated output reached customer but was caught before causing harm | System review; enhanced monitoring; root cause analysis within 48 hours |
| S3 — Medium | Hallucinated output detected internally before external delivery | Root cause documented; prompt/guardrail adjustment; retest |
| S4 — Low | Hallucination detected in monitoring/evaluation but within tolerance | Logged; reviewed at next scheduled assessment |

### Post-Incident Actions

1. Preserve the full audit trail (prompt, context, output, detection method)
2. Determine root cause (insufficient context, model limitation, prompt issue, data quality)
3. Implement remediation (prompt update, guardrail addition, context improvement)
4. Verify remediation effectiveness
5. Update hallucination rate measurement
6. Review whether tolerance thresholds remain appropriate
