# Risk Assessment: Compliance Document Summarizer

## System Overview

| Field | Value |
|-------|-------|
| System Name | Compliance Document Summarizer |
| System ID | doc-summarizer-compliance-v1.0 |
| Business Unit | Compliance Operations |
| Assessment Date | 2025-10-10 |
| Prepared by | Product Owner, Compliance Operations |
| Risk assessment approved by | AI Risk (second line), 2025-10-14 |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect summary of regulatory requirements could lead to compliance gaps. However, all outputs are reviewed by human compliance analysts before use. |
| Data Exposure Risk | **High (3)** | Documents are confidential business data (regulatory correspondence, pre-publication policy) but do not contain customer personal data. Primary processing on Vertex AI in the GCP EU region (VPC-hosted). During a primary outage only, documents go to the fallback model (Claude Sonnet 4.5), also served through Vertex AI in the EU region under the same Google Cloud agreement, with zero data retention. |
| Prompt Injection Susceptibility | **Medium (2)** | Internal users only, but the input is uploaded documents, which can carry instructions (indirect prompt injection). The system has no tools and every summary is reviewed before use, which limits what an injected instruction can do. |
| Output Controllability | **Low (1)** | All outputs reviewed by qualified compliance analyst before use (Pattern 1: full human-in-the-loop). |
| Third-Party Model Dependency | **High (3)** | Primary model hosted on Vertex AI (GCP). Validated fallback to Claude Sonnet 4.5 on Vertex AI (EU region), used only on primary outage. No switch to the fallback is recorded, so it is not a tested fallback and counts as degraded. No outage tolerance is recorded. |

**Highest Dimension: High (3)** (Hallucination Severity, Data Exposure Risk, Third-Party Model Dependency)
**Aggregate Score: 12** (context only; does not set the tier)

### Risk Tier Determination

**Tier: T2 (High)**

Override check against the [canonical override list](../../framework/risk-classification/genai-risk-matrix.md#tier-override-rules):
- [ ] 1. Regulated decisions: *No. Summaries inform compliance analysts; no credit, insurance, AML/sanctions or employment decision.*
- [ ] 2. Customer-facing content without per-output review: *No. Internal only; every summary is reviewed.*
- [ ] 3. Customer personal data through an external LLM API without all four safeguards: *No. Documents do not contain customer personal data, and the fallback is also served on Vertex AI in the EU region, under the same Google Cloud agreement, with zero data retention.*
- [ ] 4. Agentic write access or authority: *No.*
- [ ] 5. Biometric, deepfake-capable media, voice cloning, medical imagery: *No.*
- [ ] 6 to 9 (minimum T2 items): *No.*

No override applies. The highest-scoring dimension is High (Hallucination Severity, Data Exposure Risk and Third-Party Model Dependency), so the tier is T2.

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

**Likelihood:** Low (primary and fallback models are both served on Vertex AI in the EU region; no document goes to a vendor outside the Google Cloud agreement)
**Impact:** Medium (confidential document exposure)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. Primary model VPC-hosted on Vertex AI; the fallback is also served on Vertex AI in the EU region, so documents go to no other vendor
2. Fallback (Claude Sonnet 4.5 on Vertex AI): same Google Cloud agreement, zero data retention, EU region, contractual exclusion from training; every fallback activation is logged
3. Google contractual commitment: no data used for training
4. Document access controls enforced at application layer
5. Audit logging of all document processing

---

## Governance Requirements (T2)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| Risk assessment approval (AI Risk, second line) | Complete | Approval dated 2025-10-14 |
| Independent validation (reduced scope) | Complete | Model Risk Management, outside the development team; report 2025-10-17 |
| Deployment approval (Head of AI + Business Unit Head) | Complete | Head of AI 2025-10-20; Head of Compliance Operations 2025-10-15 |
| Security review | Complete | Security review report 2025-10-18 |
| Bias evaluation | Complete | 100 counterfactual pairs per attribute; consistency 0.91 against the T2 threshold of 0.85 |
| Red-team | Complete | 120 cases (T2 minimum 100) |
| Pre-deployment evidence | Complete | T2 evidence pack per [governance workflow](../../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier) |
| Prompt/response audit logging | Active | 5-year retention |
| Production evaluation | Active | 20% sampled automated scoring; weekly metrics review |
| Fallback model validated | Complete | Claude Sonnet 4.5 on Vertex AI (EU region) tested |
| Semi-annual governance review | Active | Next: 2026-08-15 |

---

## Risk Acceptance

**Residual risks accepted by the business owner (Head of Compliance Operations) and confirmed by AI Risk (second line) with the risk assessment approval (2025-10-14):**

1. Hallucination rate of ≤ 3%: accepted given full human review of every output
2. Document length limitations: accepted with user warning for documents >80 pages

**No conditions or restrictions beyond standard T2 governance requirements.**
