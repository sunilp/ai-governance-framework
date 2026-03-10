# GenAI Deployment Gates

## Overview

No GenAI system enters production without passing a defined set of gates. The gates are graduated by risk tier — higher-risk use cases require more gates and more rigorous evidence.

Each gate has explicit pass/fail criteria. A gate failure blocks deployment until remediated. There are no exceptions to gate requirements without documented risk acceptance from the appropriate authority.

---

## Gate Structure by Tier

### T1 — Critical GenAI Use Cases (5 Gates)

```
Gate 1: Use Case & Risk Assessment
    ↓
Gate 2: Development & Evaluation Complete
    ↓
Gate 3: Security & Compliance Review
    ↓
Gate 4: Independent Validation
    ↓
Gate 5: Operational Readiness & Approval
```

### T2 — High (4 Gates)

Gates 1, 2, 3, 5 (independent validation replaced by enhanced peer review)

### T3 — Medium (3 Gates)

Gates 1, 2, 5 (simplified)

### T4 — Low (2 Gates)

Gates 1, 2 (self-assessment)

---

## Gate Details

### Gate 1: Use Case & Risk Assessment

**Purpose:** Confirm the use case is understood, justified, and properly classified.

| Criterion | Evidence Required |
|-----------|------------------|
| Use case documented | Business justification, expected users, data flows, decision impact |
| Risk tier assigned | Completed GenAI risk assessment per [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md) |
| Data classification | All data in the pipeline classified per data governance policy |
| Model selected | Foundation model evaluated per [model-selection.md](model-selection.md) |
| Regulatory applicability | Applicable regulations identified; compliance approach documented |
| Stakeholder sign-off | Business owner, data owner, risk owner identified and committed |

**Gate owner:** Business Owner + AI Risk Analyst

### Gate 2: Development & Evaluation Complete

**Purpose:** Confirm the system works correctly, safely, and within defined quality thresholds.

| Criterion | Evidence Required |
|-----------|------------------|
| Functional testing | System produces correct outputs for representative test cases |
| Evaluation suite | Automated eval suite passes all thresholds (accuracy, faithfulness, relevance) |
| Safety testing | Adversarial test suite passes (prompt injection, jailbreaking, toxicity) |
| Bias evaluation | Bias testing completed on relevant protected attributes; results documented |
| Hallucination rate | Measured and within defined tolerance for the risk tier |
| Prompt review | All prompts reviewed per [prompt-engineering-standards.md](prompt-engineering-standards.md) |
| RAG quality (if applicable) | Retrieval metrics meet thresholds per [rag-governance.md](rag-governance.md) |
| Code review | Application code peer-reviewed and merged |
| Documentation | Model card, architecture diagram, data flow diagram completed |

**Gate owner:** Development Lead + Prompt Engineering Lead

### Gate 3: Security & Compliance Review

**Purpose:** Confirm the system meets security standards and regulatory requirements.

| Criterion | Evidence Required |
|-----------|------------------|
| Security review | Application security assessment completed |
| Data residency | Data flow validated against residency requirements |
| Access controls | Authentication, authorization, and audit logging verified |
| PII handling | PII detection, redaction, or exclusion validated |
| Vendor assessment | Third-party model risk assessment completed (if using external API) |
| DPA in place | Data processing agreement executed with model provider (if applicable) |
| Regulatory mapping | Controls mapped to applicable regulatory requirements |
| Penetration testing | Prompt injection and application security testing completed (T1/T2) |

**Gate owner:** CISO + Compliance Officer

### Gate 4: Independent Validation (T1 Only)

**Purpose:** Independent assurance that the system is fit for purpose.

| Criterion | Evidence Required |
|-----------|------------------|
| Independent evaluation | Validation team runs evaluation suite independently; results consistent |
| Conceptual soundness | System architecture and approach reviewed for soundness |
| Limitations review | Known limitations assessed for business impact |
| Stress testing | System tested under edge cases, adversarial conditions, and load |
| Challenger assessment | Alternative approaches considered and compared (where applicable) |
| Validation report | Independent validation report issued with findings and recommendations |

**Gate owner:** Model Risk Management / Independent Validation Team

### Gate 5: Operational Readiness & Approval

**Purpose:** Confirm the system can be operated safely in production.

| Criterion | Evidence Required |
|-----------|------------------|
| Monitoring configured | All required metrics instrumented and alerting configured |
| Runbook documented | Operational procedures, troubleshooting guides, escalation paths |
| Incident response | GenAI-specific incident playbook reviewed and tested |
| Rollback procedure | Tested rollback or fallback mechanism |
| On-call coverage | Team on-call rotation covering the system |
| Cost controls | Token budgets, rate limits, and cost alerts configured |
| Deployment plan | Deployment approach defined (canary, shadow, direct) with rollback criteria |
| User communication | End users informed of AI system capabilities, limitations, and feedback channels |
| Final approval | Tier-appropriate approval authority signs off |

**Gate owner:** Operations Lead + Final Approver (per tier)

---

## Approval Authority

| Tier | Final Approver |
|------|---------------|
| T1 | AI Risk Committee |
| T2 | Head of AI + Business Unit Head |
| T3 | Team Lead + Business Owner |
| T4 | Team Lead |

---

## Post-Deployment Requirements

Passing deployment gates is not the end. Post-deployment obligations:

| Requirement | Cadence |
|-------------|---------|
| Production monitoring review | Daily (T1), Weekly (T2), Monthly (T3/T4) |
| Full evaluation re-run | Monthly (T1), Quarterly (T2), Semi-annually (T3/T4) |
| Model/prompt version review | Every change triggers re-evaluation |
| Incident review | Within 24 hours of any incident |
| Scheduled re-assessment | Annually at minimum; triggered by material changes |

---

## Gate Failure and Remediation

When a gate fails:

1. **Document the failure** — what criterion was not met, with evidence
2. **Assess severity** — is this a blocking issue or a risk to be accepted?
3. **Remediate** — fix the issue and re-submit evidence
4. **Risk acceptance (exceptional)** — if remediation is not feasible, document a risk acceptance with compensating controls, approved by the tier-appropriate authority

Risk acceptance is not a routine path. It is an exception that must be justified, time-bounded, and reviewed at the next scheduled assessment.
