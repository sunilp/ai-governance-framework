# Model Development Standards

## Scope

These standards apply to all AI/ML models developed for use in production systems. The depth of compliance is proportional to the system's risk tier (see [Risk Matrix](../risk-classification/risk-matrix.md)).

## Data Requirements

### Data Quality
- **Source documentation:** Every dataset must have a documented source, extraction method, and known limitations.
- **Quality assessment:** Data profiling must be completed before model training — null rates, cardinality, distribution analysis, temporal coverage.
- **Representativeness:** Training data must be assessed for representativeness against the target population. Document any known gaps.
- **Labeling standards:** For supervised learning, labeling methodology must be documented. Inter-annotator agreement must be measured for manually labeled data.

### Data Governance
- **Lineage:** Full lineage from source system to training dataset must be traceable.
- **Access controls:** Training data access must follow the principle of least privilege. Access logs must be retained.
- **Privacy:** PII must be identified, and usage must comply with applicable data protection regulations. Anonymization or pseudonymization must be applied where feasible.
- **Retention:** Training datasets must be retained for the lifecycle of the model plus the regulatory retention period.

## Development Practices

### Experiment Tracking
All model development must use an experiment tracking system (e.g., MLflow, Vertex AI Experiments). Every experiment must record:
- Hypothesis being tested
- Dataset version used
- Feature set
- Hyperparameters
- Evaluation metrics
- Hardware/compute environment

### Feature Engineering
- **Feature documentation:** Every feature must be documented with its business meaning, source, and transformation logic.
- **Prohibited features:** Features that directly encode protected attributes (race, gender, religion, etc.) are prohibited unless legally required and approved by compliance.
- **Proxy analysis:** Features that may serve as proxies for protected attributes must be identified and assessed.
- **Feature stability:** Features must be assessed for temporal stability. Features that degrade over time must have monitoring in place.

### Model Selection
- **Baseline:** Every model must be benchmarked against a simple baseline (e.g., logistic regression, business rules).
- **Interpretability trade-off:** For T1/T2 systems, the incremental performance gain of complex models over interpretable alternatives must be documented and justified.
- **Methodology documentation:** The rationale for algorithm selection must be documented, including alternatives considered.

## Bias and Fairness Testing

### Requirements by Tier
| Tier | Requirement |
|------|-------------|
| T1 | Full bias audit across all protected attributes, disparate impact analysis, fairness metric selection and thresholds |
| T2 | Bias testing across primary protected attributes, fairness metric reporting |
| T3 | Basic demographic analysis of model performance |
| T4 | Not required |

### Testing Standards
- Test model performance across demographic subgroups (where data is available and legally permissible).
- Document chosen fairness metrics and thresholds with justification.
- If disparate impact is detected, document the business justification and any mitigations applied.

## Documentation Standards

### Model Development Document
Every model must have a development document covering:
1. Business context and objectives
2. Data description and quality assessment
3. Feature engineering approach
4. Model methodology and selection rationale
5. Training procedure and hyperparameter tuning
6. Evaluation results (accuracy, fairness, robustness)
7. Known limitations and failure modes
8. Recommendations for deployment

### Model Card
A [model card](../../templates/model-card-template.yaml) must be completed before the model can proceed to validation.

## Peer Review

- **T1/T2 models:** Require peer review by at least one data scientist not involved in development, plus a review by the model risk management function.
- **T3 models:** Require peer review by at least one data scientist not involved in development.
- **T4 models:** Standard code review practices apply.

Peer review must assess: methodology soundness, code quality, test coverage, documentation completeness, and reproducibility.

## Version Control

- All model code must be in version control (Git).
- Model artifacts (weights, configs) must be versioned in an artifact registry.
- Dataset versions must be tracked and linked to model versions.
- Changes to production models require a new version — no in-place modifications.
