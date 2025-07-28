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

The model is not directly subject to SR 11-7 unless the regulator specifically designates it, though best practice suggests applying similar standards.

**Score: Medium**

### 4. Reversibility — Medium

Blocked transactions can be released after fraud analyst review (typically within 2 hours). False positives cause customer friction but no lasting financial harm — the customer can retry the transaction or contact support. The impact is temporary inconvenience rather than permanent consequence.

**Score: Medium**

### 5. Scale of Impact — High

- 25 million transactions per day
- ~75,000 transactions blocked or stepped up daily
- Protects approximately $2B in daily transaction volume
- System failure would expose the organization to significant fraud losses

**Score: High**

## Overall Risk Tier: T2 — High

**Justification:** Decision autonomy and scale of impact score High, but reversibility is Medium (blocked transactions can be quickly released), and regulatory exposure is Medium compared to credit models. The system is critical for fraud prevention but decisions are more easily reversible than credit decisions. T2 governance provides appropriate oversight without the full T1 burden.

## Governance Requirements (per T2 classification)

| Requirement | Status |
|-------------|--------|
| MRM review + senior DS validation | Completed — validation report approved |
| Full model card | Completed — see model-card.yaml |
| Impact assessment | Completed |
| Challenger model | Baseline maintained (previous version v6.x) |
| Daily monitoring | Configured — detection rate, FPR, latency |
| Quarterly review | Scheduled |
| Senior management sign-off | Approved by Head of Financial Crime |
| Pre-deployment: 4 gates | All gates passed |
| Incident response SLA | 4 hours |

## Key Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Novel fraud pattern not detected | High | High | Monthly incremental retraining, rule engine overlay for known patterns, analyst feedback loop for labeling |
| High false positive rate causing customer friction | Medium | Medium | FPR monitoring with 5% hard cap, customer complaint tracking, friction-aware threshold tuning |
| System latency degradation affecting authorization | Low | Critical | Dedicated infrastructure, auto-scaling, sub-50ms SLA, automatic fallback to rules |
| Adversarial attack (fraudsters gaming the model) | Medium | High | Feature diversification, ensemble approach, regular feature rotation, adversarial testing |
| Model drift due to seasonal spending patterns | Medium | Medium | Hourly feature distribution monitoring, seasonal model variants considered |
