# GenAI Deployment Gates

## Overview

No GenAI system enters production without meeting defined deployment criteria. This document is not a separate gate model: the [governance workflow](../governance-operations/governance-workflow.md) is the only process, and the criteria sets below are the detailed checks for GenAI systems at its stages. Control DA-003 (deployment gates passed) means the criteria that apply to the system's tier are met.

Each criterion has explicit pass/fail evidence. A failure blocks deployment until remediated, unless an exception is approved under [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance).

---

## How the Criteria Apply by Tier

Which evidence each tier must produce is set by the [minimum evidence pack by tier](../governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier). The table shows which criteria sets apply.

| Criteria set | Workflow stages | T1 | T2 | T3 | T4 |
|--------------|-----------------|----|----|----|----|
| 1. Use case and risk assessment | 1, 2 (model selection at 3) | Required | Required | Required | Required (self-assessment) |
| 2. Development and evaluation | 4, 5 | Required | Required | Required | Required |
| 3. Security and compliance | 3, 6 | Required | Required | Required | Data residency only; approved vendor; red-team scan recommended |
| 4. Independent validation | 5 | Full independent validation by MRM | Reduced-scope independent validation by a qualified reviewer outside the development team | Peer review | Self-test |
| 5. Operational readiness and approval | 7, 8 | Required | Required | Required (reduced evidence pack) | Required (reduced evidence pack) |

Within criteria set 2, which evaluation types must pass at each tier is set in [Release Criteria by Tier](evaluation-governance.md#release-criteria-by-tier); rows for evaluations a tier does not require do not apply.

---

## Criteria Details

### 1. Use Case and Risk Assessment (Stages 1 and 2)

**Purpose:** Confirm the use case is understood, justified, and properly classified.

| Criterion | Evidence Required |
|-----------|------------------|
| Use case documented | Business justification, expected users, data flows, decision impact |
| Risk tier assigned | Completed GenAI risk assessment per [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md) |
| Data classification | All data in the pipeline classified per data governance policy |
| Model selected | Foundation model evaluated per [model-selection.md](model-selection.md) |
| Regulatory applicability | Applicable regulations identified; compliance approach documented |
| Stakeholder sign-off | Business owner, data owner, risk owner identified and committed |

**Owner:** Product owner prepares the risk assessment. Approved by the AI Risk Committee (T1), AI Risk (T2) or the team lead (T3/T4).

### 2. Development and Evaluation (Stages 4 and 5)

**Purpose:** Confirm the system works correctly, safely, and within defined quality thresholds.

| Criterion | Evidence Required |
|-----------|------------------|
| Functional testing | System produces correct outputs for representative test cases |
| Evaluation suite | Automated eval suite passes the tier thresholds in [evaluation-governance.md](evaluation-governance.md#threshold-definitions-by-tier) (accuracy, faithfulness, relevance) |
| Safety testing | Adversarial test suite passes (prompt injection, jailbreaking, toxicity) |
| Bias evaluation | Bias testing completed on relevant protected attributes; results documented |
| Hallucination rate | Measured and within the [tier threshold](evaluation-governance.md#threshold-definitions-by-tier), or a stricter use-case tolerance |
| Prompt review | All prompts reviewed per [prompt-engineering-standards.md](prompt-engineering-standards.md) |
| RAG quality (if applicable) | Retrieval metrics meet the [tier thresholds](evaluation-governance.md#threshold-definitions-by-tier); see also [rag-governance.md](rag-governance.md) |
| Code review | Application code peer-reviewed and merged |
| Documentation | Model card, architecture diagram, data flow diagram completed |

**Owner:** AI lead certifies that evaluations pass (Stage 5). Prompt review depth per tier is set in [prompt-engineering-standards.md](prompt-engineering-standards.md).

### 3. Security and Compliance (Stages 3 and 6)

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
| Penetration testing | Prompt injection and application security testing completed. Required for T1/T2 systems that are customer-facing or internet-exposed; recommended for T3 |

**Owner:** Security signs off the security review and red-team results (Stage 6). Compliance confirms the regulatory mapping.

### 4. Independent Validation (Stage 5)

**Purpose:** Independent assurance that the system is fit for purpose. T1 gets full independent validation by Model Risk Management. T2 gets independent validation with reduced scope by a qualified reviewer outside the development team (MRM or another second-line reviewer). T3 uses peer review and T4 a self-test. The team that builds a T1/T2 system never validates it.

| Criterion | Evidence Required |
|-----------|------------------|
| Independent evaluation | Validation team runs evaluation suite independently; results consistent |
| Conceptual soundness | System architecture and approach reviewed for soundness |
| Limitations review | Known limitations assessed for business impact |
| Stress testing | System tested under edge cases, adversarial conditions, and load |
| Challenger assessment | Alternative approaches considered and compared (where applicable) |
| Validation report | Independent validation report issued with findings and recommendations |

**Owner:** Model Risk Management (T1); MRM or another second-line reviewer (T2).

### 5. Operational Readiness and Approval (Stages 7 and 8)

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

**Owner:** AI Operations confirms operational readiness (DA-003); the approvers below sign off (DA-002).

---

## Approval Authority

| Tier | Final Approver |
|------|---------------|
| T1 | AI Risk Committee + CISO (+ DPO if personal data is processed) |
| T2 | Head of AI + Business Unit Head |
| T3 | Team Lead + Business Owner |
| T4 | Team Lead |

See [Approvals by Tier](../operating-model/roles-responsibilities.md#approvals-by-tier) for who is Accountable when more than one role signs.

---

## Post-Deployment Requirements

Passing deployment gates is not the end. Post-deployment obligations:

| Requirement | Cadence |
|-------------|---------|
| Online automated scoring | Every response (T1), 20% sample (T2), 5% sample (T3), weekly batch sample (T4); see [monitoring.md](monitoring.md#production-evaluation) |
| Metrics review | Daily dashboard check by AI Operations plus a monthly system-owner review (T1), Weekly (T2), Monthly (T3), Quarterly (T4) |
| Full offline evaluation re-run | Monthly (T1), Quarterly (T2), Semi-annually (T3/T4), and on every model, provider or prompt change |
| Model/prompt version review | Every change triggers re-evaluation |
| Incident follow-up | By severity: root cause within 48 hours and post-mortem within 1 week (S1) or 2 weeks (S2); root cause documented within 10 business days (S3); tracked in backlog (S4). See [escalation-paths.md](../operating-model/escalation-paths.md#severity-classification) |
| Formal governance review (RV-001) | Quarterly (T1), Semi-annually (T2), Annually (T3), Annual self-assessment (T4); risk re-assessment at each review and on material change |
| Independent revalidation | Annually (T1), every 24 months (T2), and on material change; T3/T4 peer re-review on material change |

---

## Gate Failure and Remediation

When a criterion is not met:

1. **Document the failure** — what criterion was not met, with evidence
2. **Assess severity** — is this a blocking issue or a risk to be accepted?
3. **Remediate** — fix the issue and re-submit evidence
4. **Exception (not routine):** if remediation is not feasible, request an exception with compensating controls under [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance), which sets the approvers, maximum duration and the controls that cannot be excepted
