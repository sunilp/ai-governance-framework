# Risk Assessment — Retail Credit Scoring Model

## System Overview

The Retail Credit Scoring Model (MDL-CS-003) predicts the probability of default for unsecured retail credit applications. It processes approximately 15,000 applications per day and directly determines automated approve/decline decisions for 85% of applications. The remaining 15% (near decision boundary) are routed to human underwriters.

## Risk Dimension Scoring

### 1. Decision Autonomy — Critical

The model makes binding credit decisions (approve/decline) for 85% of applications without human review. Declined applicants receive an adverse action notice but the initial decision is fully automated. This is the highest level of decision autonomy.

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

**Justification:** Four of five dimensions score at Critical level. The model makes autonomous decisions affecting millions of customers, processes highly restricted data, is subject to multiple regulatory frameworks, and influences billions in credit exposure. This is unambiguously a T1 system requiring the highest level of governance.

## Governance Requirements (per T1 classification)

| Requirement | Status |
|-------------|--------|
| Independent validation by MRM | Completed — validation report approved 2024-11-15 |
| Full model card | Completed — see model-card.yaml |
| Impact assessment | Completed — reviewed by compliance |
| Challenger model | Active — logistic regression v2.x maintained as challenger |
| Real-time + daily monitoring | Configured — PSI daily, AUC monthly, fairness monthly |
| Quarterly review | Scheduled — next review 2025-Q1 |
| Board reporting | Included in quarterly risk report |
| AI Risk Committee approval | Approved — 2024-11-22 |
| Pre-deployment: 5 gates | All gates passed |
| Incident response SLA | 1 hour — on-call rotation established |

## Key Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Model drift due to economic cycle change | Medium | High | Daily PSI monitoring, semi-annual retraining, stress testing against downturn scenarios |
| Discriminatory outcomes for protected groups | Low | Critical | Monthly fairness monitoring, proxy analysis, equalized odds thresholds |
| Data feed interruption (credit bureau) | Low | High | OOD detection routes affected applications to manual review, fallback scoring rules |
| Adversarial manipulation (synthetic applications) | Low | Medium | Input validation, fraud model upstream, velocity checks |
| Regulatory examination finding | Medium | High | Comprehensive documentation, quarterly self-assessment, mock examination annually |
