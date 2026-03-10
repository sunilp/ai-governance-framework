# Risk Assessment: Compliance Document Summarizer

## System Overview

| Field | Value |
|-------|-------|
| System Name | Compliance Document Summarizer |
| System ID | doc-summarizer-compliance-v1.0 |
| Business Unit | Compliance Operations |
| Assessment Date | 2025-10-10 |
| Assessor | AI Risk Analyst, Model Risk Management |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect summary of regulatory requirements could lead to compliance gaps. However, all outputs are reviewed by human compliance analysts before use. |
| Data Exposure Risk | **Medium (2)** | Documents are confidential but do not contain customer PII. Processed within GCP EU region on Vertex AI (VPC-hosted). |
| Prompt Injection Susceptibility | **Low (1)** | Internal users only; input is uploaded documents, not free-text queries. Limited attack surface. |
| Output Controllability | **Low (1)** | All outputs reviewed by qualified compliance analyst before use (Pattern 1: full human-in-the-loop). |
| Third-Party Model Dependency | **Medium (2)** | Hosted on Vertex AI (GCP); fallback to Claude 3.5 Sonnet validated. Data stays within organizational GCP tenancy. |

**Aggregate Score: 9**
**Highest Dimension: High (3)**

### Risk Tier Determination

**Tier: T2 — High**

Automatic T1 trigger check:
- [ ] Processes customer PII through external LLM API — *No*
- [ ] Generates customer-facing content without human review — *No: internal only, human-reviewed*
- [ ] Makes or influences regulated decisions — *Indirect: summaries inform compliance analysis*
- [ ] Involves agentic behavior with production system access — *No*

No automatic T1 triggers. Classified as T2 based on aggregate score and hallucination severity.

---

## Detailed Risk Analysis

### Hallucination Risk

**Scenario:** System omits a key regulatory deadline or mischaracterizes a compliance requirement, leading the analyst to overlook a material obligation.

**Likelihood:** Low (faithfulness score 0.96; human review catches errors)
**Impact:** High (missed regulatory deadline; potential enforcement action)
**Residual risk after mitigation:** Low

**Mitigations:**
1. Human-in-the-loop: every summary reviewed by qualified compliance analyst
2. Summary template requires explicit extraction of dates, deadlines, and affected entities
3. Faithfulness evaluation on every output
4. Confidence indicators for inferred vs. extracted content
5. Source document always available alongside summary for verification

### Data Exposure Risk

**Scenario:** Confidential regulatory correspondence or pre-publication policy documents are exposed through the processing pipeline.

**Likelihood:** Very Low (VPC-hosted on Vertex AI; no external API calls)
**Impact:** Medium (confidential document exposure)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. VPC-hosted model — no data leaves organizational infrastructure
2. Google contractual commitment: no data used for training
3. Document access controls enforced at application layer
4. Audit logging of all document processing

---

## Governance Requirements (T2)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Head of AI approval | Complete | Approval dated 2025-10-20 |
| Security review | Complete | Security review report 2025-10-18 |
| Deployment gates (4 of 5) | Passed | Gate evidence package |
| Prompt/response audit logging | Active | 5-year retention |
| Weekly quality monitoring | Active | 20% sample evaluation |
| Fallback model validated | Complete | Claude 3.5 Sonnet tested |
| Quarterly review cadence | Active | Next: 2026-05-15 |

---

## Risk Acceptance

**Residual risks accepted by Head of AI (2025-10-20):**

1. Hallucination rate of ≤ 3% — accepted given full human review of every output
2. Document length limitations — accepted with user warning for documents >80 pages

**No conditions or restrictions beyond standard T2 governance requirements.**
