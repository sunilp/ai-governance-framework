# AI Risk Classification Matrix

## Purpose

Every AI system in a regulated organization must be classified by risk tier before development begins. The tier determines the governance intensity — how much oversight, documentation, validation, and monitoring the system requires.

This is not a theoretical exercise. Regulators expect you to demonstrate that you understand the risk profile of every AI system in production and that governance controls are proportional to that risk.

## Risk Tiers

| Tier | Label | Governance Intensity | Examples |
|------|-------|---------------------|----------|
| **T1** | Critical | Full lifecycle governance, independent validation, board-level reporting | Credit decisioning, AML/CTF screening, capital adequacy models |
| **T2** | High | Model risk management review, quarterly monitoring, senior management sign-off | Fraud detection, customer segmentation for pricing, collections prioritization |
| **T3** | Medium | Documented development standards, automated monitoring, annual review | Chatbot routing, document classification, marketing propensity models |
| **T4** | Low | Lightweight documentation, standard deployment practices | Internal search ranking, log anomaly detection, test automation |

## Classification Criteria

Assess each AI system against five dimensions. The highest-scoring dimension determines the overall tier.

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

1. **System owner** completes the [assessment template](assessment-template.yaml) for each new AI system.
2. **AI Risk Committee** reviews assessments for T1 and T2 systems.
3. **Model Risk Management** validates the tier classification independently for T1 systems.
4. **Tier is recorded** in the AI system inventory and determines all downstream governance requirements.
5. **Re-classification** is triggered by material changes to scope, data, autonomy level, or regulatory environment.

## Governance Intensity by Tier

| Requirement | T1 Critical | T2 High | T3 Medium | T4 Low |
|-------------|-------------|---------|-----------|--------|
| Independent validation | Required | Required | Not required | Not required |
| Model card | Full | Full | Summary | Minimal |
| Impact assessment | Required | Required | Recommended | Not required |
| Challenger model | Required | Recommended | Not required | Not required |
| Monitoring frequency | Real-time + daily | Daily | Weekly | Monthly |
| Review cadence | Quarterly | Quarterly | Annually | Annually |
| Board reporting | Yes | Summarized | No | No |
| Incident response SLA | 1 hour | 4 hours | 24 hours | 72 hours |
| Pre-deployment gates | 5 gates | 4 gates | 2 gates | 1 gate |

