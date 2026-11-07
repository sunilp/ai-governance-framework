# AI Risk Classification Matrix

## Purpose

Every AI system in a regulated organization must be classified by risk tier before development begins. The tier determines the governance intensity — how much oversight, documentation, validation, and monitoring the system requires.

This is not a theoretical exercise. Regulators expect you to demonstrate that you understand the risk profile of every AI system in production and that governance controls are proportional to that risk.

## Risk Tiers

| Tier | Label | Governance Intensity | Examples |
|------|-------|---------------------|----------|
| **T1** | Critical | Full lifecycle governance, independent validation, board-level reporting | Credit decisioning, AML/CTF screening, capital adequacy models, real-time card fraud blocking at retail scale |
| **T2** | High | Independent validation (reduced scope), weekly metrics review, semi-annual governance review, senior management sign-off | Fraud alert prioritization for analyst queues, customer segmentation for pricing, collections prioritization |
| **T3** | Medium | Documented development standards, automated monitoring, annual review | Chatbot routing, document classification, marketing propensity models |
| **T4** | Low | Lightweight documentation, standard deployment practices | Internal search ranking, log anomaly detection, test automation |

## Classification Criteria

Assess each AI system against five dimensions. Score each dimension Critical (4), High (3), Medium (2) or Low (1).

**The highest-scoring dimension sets the tier:** any Critical dimension gives T1; otherwise any High gives T2; otherwise any Medium gives T3; all Low gives T4. Then check the [canonical override list](genai-risk-matrix.md#tier-override-rules). Overrides can raise the tier, never lower it. The approver may raise a tier with a recorded rationale (for example, a pilot with an unusual exposure profile). Nobody can lower a tier below what the scoring and overrides give. Record the aggregate score (the sum of the five scores) for context and comparison only. It does not set the tier. The same rule applies in the [GenAI](genai-risk-matrix.md#risk-tier-determination-for-genai), [multimodal](multimodal-risk-matrix.md) and [agentic](agentic-ai-risk.md) matrices.

### 1. Decision Autonomy

How much does the system influence or make decisions without human intervention?

| Score | Description |
|-------|-------------|
| Critical | System makes binding decisions with no human review (e.g., auto-decline loan applications) |
| High | System makes recommendations that are followed >80% of the time |
| Medium | System provides inputs that inform human decisions |
| Low | System performs background tasks with no direct decision impact |

### 2. Data Sensitivity

What is the classification of data the system processes?

| Score | Description |
|-------|-------------|
| Critical | Highly restricted PII, financial records, health data, biometric data |
| High | PII, customer behavioral data, transaction histories |
| Medium | Aggregated or pseudonymized data, internal operational data |
| Low | Public data, synthetic data, non-sensitive metadata |

### 3. Regulatory Exposure

Is the system subject to specific regulatory requirements?

| Score | Description |
|-------|-------------|
| Critical | Directly in scope for SR 11-7, EU AI Act high-risk, BCBS 239, anti-discrimination laws |
| High | Subject to general supervisory expectations, data protection regulations |
| Medium | Indirectly supports regulated processes |
| Low | No regulatory nexus |

### 4. Reversibility

If the system makes an error, how easily can it be corrected?

| Score | Description |
|-------|-------------|
| Critical | Irreversible or extremely costly to reverse (e.g., denied credit affecting customer record) |
| High | Reversible but with significant customer or business impact |
| Medium | Reversible with moderate effort and limited impact |
| Low | Trivially reversible or self-correcting |

### 5. Scale of Impact

How many people or how much capital is affected by the system's outputs?

| Score | Description |
|-------|-------------|
| Critical | Affects >100,000 customers or >$100M in exposure |
| High | Affects >10,000 customers or >$10M in exposure |
| Medium | Affects >1,000 customers or >$1M in exposure |
| Low | Affects <1,000 customers or <$1M in exposure |

## Decision Process

1. **Product owner** prepares the risk assessment using the [assessment template](assessment-template.yaml) for each new AI system.
2. **Approval by tier:** T1 AI Risk Committee; T2 AI Risk (second line); T3 team lead; T4 team lead (acknowledges the self-assessment).
3. **Model Risk Management** validates the tier classification independently for T1 systems.
4. **Tier is recorded** in the AI system inventory and determines all downstream governance requirements.
5. **Re-assessment** (a re-tiering check) happens at every formal governance review and on material change to scope, data, autonomy level, or regulatory environment.

## Governance Intensity by Tier

| Requirement | T1 Critical | T2 High | T3 Medium | T4 Low |
|-------------|-------------|---------|-----------|--------|
| Independent validation | Full, by Model Risk Management | Reduced scope, by a qualified reviewer outside the development team (MRM or second line) | Peer review | Self-test |
| Independent revalidation | Annual and on material change | Every 24 months and on material change | On material change (peer re-review) | On material change (peer re-review) |
| Model card | Full | Full | Summary | Minimal |
| Impact assessment | Required | Required | Recommended | Not required |
| Challenger model | Required | Recommended | Not required | Not required |
| Metrics review | Daily dashboard check by AI Operations, plus monthly system-owner review | Weekly | Monthly | Quarterly |
| Formal governance review (RV-001) | Quarterly | Semi-annual | Annual | Annual self-assessment |
| Board reporting | Yes | Summarized | No | No |

The team that builds a T1 or T2 model never validates it.

Pre-deployment evidence by tier is set in the governance workflow: see [minimum evidence pack by tier](../governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier). Incident response times depend on severity, not tier: see [severity classification](../operating-model/escalation-paths.md#severity-classification).

