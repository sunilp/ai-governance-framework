# Risk Assessment — Retail Credit Scoring Model

## System Overview

The Retail Credit Scoring Model (MDL-CS-003) predicts the probability of default for unsecured retail credit applications. It processes approximately 15,000 applications per day. About 60% of applications are approved automatically within approved credit policy. The other 40% (every proposed decline or other adverse outcome, such as a lower limit or higher price than applied for, plus cases near the decision boundary) go to a human underwriter, who decides before anything is issued. Any applicant can ask for human review of an automated decision.

Human oversight follows the T1 rule for regulated decisions in [human-in-loop-patterns.md](../../framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix): Pattern 1 (human-in-the-loop) for adverse and non-standard outcomes, automated favourable outcomes within approved policy, and a route to human review on request.

## Risk Dimension Scoring

### 1. Decision Autonomy — Critical

The model makes binding approval decisions for about 60% of applications with no human review. Proposed declines and other adverse outcomes are decided by an underwriter, but the model score is the main input to that decision. Binding automated decisions at this volume are the highest level of decision autonomy.

**Score: Critical**

### 2. Data Sensitivity — Critical

The model processes highly restricted PII including:
- Full name, address, date of birth
- Income and employment details
- Complete credit bureau records (payment history, outstanding debts, enquiries)
- Bank account information

All data is classified as Highly Restricted under the organization's data classification policy.

**Score: Critical**

### 3. Regulatory Exposure — Critical

The model is directly in scope for:
- **SR 11-7** — Federal Reserve / OCC model risk management guidance
- **EU AI Act** — Classified as high-risk AI system (Annex III, paragraph 5(b): creditworthiness assessment)
- **ECOA / Regulation B** — Fair lending requirements, adverse action notice obligations
- **GDPR** — Automated decision-making provisions (Article 22)
- **BCBS 239** — Risk data aggregation (model outputs feed risk reporting)

**Score: Critical**

### 4. Reversibility — High

Incorrect credit decisions can be reversed (approved applications can be monitored, declined applications can be reconsidered), but:
- A wrongful decline causes immediate customer frustration and potential financial harm
- A wrongful approval creates credit exposure that cannot be fully recovered
- Historical decisions affect the customer's interaction record

**Score: High**

### 5. Scale of Impact — Critical

- ~15,000 decisions per day across retail banking
- Affects 5.5M applications annually
- Total credit exposure influenced by the model: ~$12B outstanding
- Incorrect calibration could materially affect the bank's credit loss provisions

**Score: Critical**

## Overall Risk Tier: T1 — Critical

**Justification:** Decision autonomy, data sensitivity, regulatory exposure and scale of impact all score Critical, and any Critical dimension sets T1. Override item 1 (regulated credit decisions) in the [canonical override list](../../framework/risk-classification/genai-risk-matrix.md#tier-override-rules) also makes it T1 automatically. Aggregate score: 19 of 20, recorded for context only.

## Governance Requirements (per T1 classification)

| Requirement | Status |
|-------------|--------|
| Independent validation by MRM | Completed — validation report approved 2024-11-15 |
| Full model card | Completed — see model-card.yaml |
| Impact assessment | Completed — reviewed by compliance |
| Challenger model | Active — logistic regression v2.x maintained as challenger |
| Metrics review | Configured: daily dashboard check by AI Operations (PSI, approval rate); monthly system-owner review (AUC, fairness) |
| Human oversight | Pattern 1 for every proposed decline or adverse outcome; automated approvals within policy; human review on request |
| Quarterly review | Scheduled — next review 2025-Q1 |
| Board reporting | Included in quarterly risk report |
| Deployment approval | AI Risk Committee, CISO and DPO approved 2024-11-22 |
| Pre-deployment evidence | Full T1 evidence pack per [governance workflow](../../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier) (GenAI-only items not applicable) |
| Incident response | Response SLAs by severity per [escalation paths](../../framework/operating-model/escalation-paths.md#severity-classification); on-call rotation established |

## Key Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Model drift due to economic cycle change | Medium | High | Daily PSI monitoring, semi-annual retraining, stress testing against downturn scenarios |
| Discriminatory outcomes for protected groups | Low | Critical | Monthly fairness monitoring, proxy analysis, equalized odds thresholds |
| Data feed interruption (credit bureau) | Low | High | OOD detection routes affected applications to manual review, fallback scoring rules |
| Adversarial manipulation (synthetic applications) | Low | Medium | Input validation, fraud model upstream, velocity checks |
| Regulatory examination finding | Medium | High | Comprehensive documentation, quarterly self-assessment, mock examination annually |
