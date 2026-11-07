# Risk Assessment — Real-Time Transaction Fraud Detection

## System Overview

The Real-Time Transaction Fraud Detection system (MDL-FD-007) scores every card transaction in real time to identify potential fraud. It processes approximately 25 million transactions per day with a p99 latency requirement of 50ms. High-risk transactions are either blocked outright or stepped up for additional customer authentication.

## Risk Dimension Scoring

### 1. Decision Autonomy — High

The model automatically blocks high-confidence fraud transactions and triggers step-up authentication for medium-confidence scores. Approximately 0.3% of transactions are blocked or stepped up. While this is automated, the scope is narrower than credit decisioning — the model flags rather than makes final determinations for most cases, and fraud analysts review blocked transactions within hours.

**Score: High**

### 2. Data Sensitivity — High

The model processes transaction data including:
- Transaction amount, merchant, location, timestamp
- Card and device identifiers
- Customer behavioral profiles (aggregated spending patterns)
- Channel and authentication signals

Transaction data is classified as Restricted. The model does not process full PII (name, address) but card identifiers and behavioral profiles are sensitive.

**Score: High**

### 3. Regulatory Exposure — Medium

The model supports fraud prevention obligations but is not itself subject to specific model risk regulations in the same way as credit models:
- **PSD2** — Supports Strong Customer Authentication decisions
- **PCI-DSS** — Transaction data handling requirements
- **General supervisory expectations** for fraud prevention effectiveness

SR 26-2, which replaced SR 11-7 in April 2026, covers non-generative AI models such as this one. Its approach is risk-based: the bank scales model risk management to the model's materiality (exposure and purpose).

**Score: Medium**

### 4. Reversibility — Medium

Blocked transactions can be released after fraud analyst review (typically within 2 hours). False positives cause customer friction but no lasting financial harm — the customer can retry the transaction or contact support. The impact is temporary inconvenience rather than permanent consequence.

**Score: Medium**

### 5. Scale of Impact: Critical

- 25 million transactions per day
- ~75,000 transactions blocked or stepped up daily
- Protects approximately $2B in daily transaction volume
- System failure would expose the organization to significant fraud losses

This is far above the [risk matrix](../../framework/risk-classification/risk-matrix.md#5-scale-of-impact) Critical threshold (>100,000 customers or >$100M in exposure).

**Score: Critical**

## Overall Risk Tier: T1 (Critical)

**Justification:** Scale of Impact scores Critical. Under the framework rule the highest-scoring dimension sets the tier, so the system is T1. The Medium scores for reversibility and regulatory exposure do not lower it. No override applies (fraud blocking is not a regulated decision on the override list, and there is no GenAI or agentic component), and none is needed. Aggregate score: 14 of 20 (High 3 + High 3 + Medium 2 + Medium 2 + Critical 4), recorded for context only.

**Human oversight:** Transaction blocks are temporary and are released after fraud analyst review or customer contact, typically within 2 hours. Analysts review blocked transactions after the decision (human-on-the-loop), and customers can reach a human through support.

## Governance Requirements (per T1 classification)

| Requirement | Status |
|-------------|--------|
| Independent validation by Model Risk Management | Completed for v7.0.0 and v7.2.0; the development team does not validate its own model |
| Full model card | Completed: see model-card.yaml |
| Impact assessment | Completed |
| DPIA | Completed (card identifiers and behavioural profiles are personal data) |
| Challenger model | Active: previous version (v6.x) scored in shadow as challenger |
| Metrics review | Daily dashboard check by AI Operations (detection rate, FPR, latency); monthly system-owner review |
| Formal governance review | Quarterly, scheduled |
| Independent revalidation | Annual and on material change |
| Board reporting | Included in quarterly risk report |
| Risk assessment approval | AI Risk Committee |
| Deployment approval | AI Risk Committee + CISO + DPO (personal data processed) |
| Pre-deployment evidence | Full T1 evidence pack per [governance workflow](../../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier) (GenAI-only items not applicable) |
| Incident response | Response SLAs by severity per [escalation paths](../../framework/operating-model/escalation-paths.md#severity-classification) |

## Key Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Novel fraud pattern not detected | High | High | Monthly incremental retraining, rule engine overlay for known patterns, analyst feedback loop for labeling |
| High false positive rate causing customer friction | Medium | Medium | FPR monitoring with 5% hard cap, customer complaint tracking, friction-aware threshold tuning |
| System latency degradation affecting authorization | Low | Critical | Dedicated infrastructure, auto-scaling, sub-50ms SLA, automatic fallback to rules |
| Adversarial attack (fraudsters gaming the model) | Medium | High | Feature diversification, ensemble approach, regular feature rotation, adversarial testing |
| Model drift due to seasonal spending patterns | Medium | Medium | Hourly feature distribution monitoring, seasonal model variants considered |
