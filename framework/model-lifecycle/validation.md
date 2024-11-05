# Model Validation Requirements

## Purpose

Model validation provides independent assurance that a model is fit for purpose, performs as expected, and meets regulatory and organizational standards. For T1 systems, validation must be performed by a function independent of the development team.

## Validation Independence

| Tier | Validator | Independence Requirement |
|------|-----------|------------------------|
| T1 | Model Risk Management (2nd line) | Fully independent — no involvement in development |
| T2 | Senior data scientist + MRM review | Reviewer must not have contributed to development |
| T3 | Peer review within the team | Different individual from the developer |
| T4 | Standard code review | No additional validation required |

## Validation Scope

### 1. Conceptual Soundness
- Is the methodology appropriate for the problem?
- Are assumptions clearly stated and reasonable?
- Is the model complexity justified relative to interpretable alternatives?
- Are known theoretical limitations documented?

### 2. Data Integrity
- Is the training data representative and of sufficient quality?
- Are data transformations correct and documented?
- Is there data leakage between training and evaluation sets?
- Are feature definitions consistent between training and inference?

### 3. Discriminatory Performance
Evaluate the model on held-out test data across multiple metrics:

| Metric Category | Examples | Required For |
|----------------|----------|-------------|
| Accuracy | AUC-ROC, precision, recall, F1, RMSE | All tiers |
| Calibration | Brier score, calibration curves | T1, T2 |
| Stability | Performance across time periods | T1, T2 |
| Segmentation | Performance by key business segments | T1, T2, T3 |

### 4. Fairness Assessment
- Performance parity across protected attribute subgroups
- Disparate impact ratios (four-fifths rule where applicable)
- Selected fairness metrics with documented thresholds
- Required for T1 and T2; recommended for T3

### 5. Robustness Testing
- **Stress testing:** Model performance under extreme but plausible input distributions
- **Sensitivity analysis:** Impact of small perturbations to key inputs
- **Out-of-distribution detection:** Model behavior on inputs outside the training distribution
- **Adversarial testing:** For models exposed to external inputs (T1/T2)

### 6. Explainability Review
- Can individual predictions be explained to the appropriate audience?
- Are global feature importances reasonable and aligned with domain knowledge?
- Do explanations reveal concerning patterns (e.g., reliance on proxy features)?

## Challenger Models

### T1 Systems (Required)
A challenger model must be developed and maintained alongside the primary model. The challenger:
- Uses a different methodology or feature set
- Is evaluated on the same test data with the same metrics
- Provides a performance benchmark for the primary model
- Must be refreshed at least annually

### T2 Systems (Recommended)
A challenger or benchmark comparison is recommended but not mandated. At minimum, performance must be benchmarked against a simple baseline model.

## Validation Report

The validation report must include:

1. **Executive summary** — Pass/fail recommendation with key findings
2. **Scope and methodology** — What was validated and how
3. **Findings** — Categorized as:
   - **Critical:** Must be resolved before production deployment
   - **Major:** Must be resolved within 90 days of deployment
   - **Minor:** Tracked for future improvement
4. **Performance results** — All metrics with benchmarks
5. **Limitations and conditions** — Under what conditions is the model approved?
6. **Recommendations** — Specific monitoring requirements, revalidation triggers

## Revalidation Triggers

A model must be revalidated when:
- Material change to training data or feature set
- Performance degradation beyond defined thresholds
- Change in business use or scope expansion
- Regulatory requirement or audit finding
- Annual cycle (T1) or biannual cycle (T2)
