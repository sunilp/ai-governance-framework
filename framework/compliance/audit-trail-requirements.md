# Audit Trail Requirements

## Purpose

Every AI system in production must maintain an audit trail sufficient to reconstruct decisions, trace data lineage, and satisfy regulatory examination. The depth of logging is proportional to the system's risk tier.

An auditor — whether internal, external, or regulatory — should be able to answer: **"Why did this system make this decision, for this customer, at this point in time?"**

## What Must Be Logged

### Model Predictions (T1, T2, T3)

Every prediction must record:

| Field | Description | Required For |
|-------|-------------|-------------|
| `prediction_id` | Unique identifier for the prediction event | All |
| `timestamp` | UTC timestamp of the prediction | All |
| `model_id` | Model identifier (name + version) | All |
| `model_version` | Exact version of the model that produced the output | All |
| `input_hash` | Hash of the input features (for verification without storing raw PII) | T1, T2 |
| `input_features` | Full input feature vector (where legally and technically feasible) | T1 |
| `output` | Model prediction/score/classification | All |
| `confidence` | Prediction confidence or probability | T1, T2 |
| `explanation` | Feature contributions or explanation output | T1 |
| `decision` | Downstream decision taken based on the prediction | T1, T2 |
| `human_override` | Whether a human overrode the model's output | T1, T2 |
| `override_reason` | Reason for override (if applicable) | T1, T2 |
| `customer_id` | Pseudonymized customer identifier | T1, T2 |
| `request_source` | Which system or process triggered the prediction | All |

### Data Lineage (T1, T2)

For each model version in production, maintain records of:
- Training dataset identifier and version
- Data sources and extraction timestamps
- Transformation and feature engineering pipeline version
- Data quality assessment results at time of training
- Any data exclusions or filters applied, with justification

### Model Lifecycle Events (All Tiers)

| Event | Fields | Required For |
|-------|--------|-------------|
| Model registered | model_id, version, developer, timestamp | All |
| Validation completed | model_id, validator, result, report_link | T1, T2, T3 |
| Deployment approved | model_id, approver, gate_results, timestamp | T1, T2 |
| Deployed to production | model_id, version, environment, deployer, timestamp | All |
| Monitoring alert triggered | model_id, alert_type, severity, metric_values | All |
| Retraining initiated | model_id, trigger_reason, new_dataset_id | T1, T2 |
| Model retired | model_id, reason, replacement_model_id, timestamp | All |

### Access Logs (T1, T2)
- Who accessed the model's predictions, training data, or configuration
- Read vs. write access
- Timestamp and source system
- Anomalous access patterns flagged

## Retention Periods

| Data Type | Minimum Retention | Basis |
|-----------|------------------|-------|
| Interaction logs: model predictions, prompts, responses, agent actions | T1 7 years; T2 5 years; T3 3 years; T4 1 year | Set in [prompt-audit-trail.md](prompt-audit-trail.md#retention-requirements) |
| Governance records: risk assessments, approvals, validation and evaluation reports, red-team reports, incident reports, model cards, change history (including lifecycle events and training data lineage) | Life of the system plus the tier period after retirement: T1 7 years; T2 5 years; T3 3 years; T4 1 year | Framework default |
| Technical documentation of a high-risk AI system, where the organisation is its provider under the EU AI Act | 10 years after the system is placed on the market | EU AI Act Art. 18 |
| Access logs | 3 years | Security policy |

Tier periods are framework defaults. Set retention to the longest obligation that applies to you. Reference points: EU AI Act Art. 18 (provider technical documentation, 10 years), Art. 19 (provider-generated logs, at least 6 months), Art. 26(6) (deployer logs, at least 6 months); MiFID II Art. 16(7) (records of client communications, 5 years, up to 7 if the authority requests).

## Storage and Access Controls

### Storage Requirements
- Audit logs must be stored in append-only, tamper-evident storage
- Logs must be encrypted at rest and in transit
- Storage must be in a compliant region (no unauthorized cross-border transfer)
- Logs must be separable from operational data to support independent audit access

### Access Controls
- **Write access:** Only the model serving infrastructure and lifecycle management system
- **Read access:** Model owner, Model Risk Management, Internal Audit, Compliance, and authorized regulators
- **Admin access:** Platform team only, with dual-approval for configuration changes
- All access to audit logs must itself be logged

## Regulatory Examination Readiness

At any point, the organization must be able to produce:

1. **Model inventory:** Complete list of all AI systems in production with risk tiers, owners, and current versions
2. **Decision reconstruction:** For any specific prediction, retrieve the full context — inputs, model version, output, downstream decision, and any human override
3. **Performance history:** Trend data for model performance, drift metrics, and fairness indicators
4. **Governance evidence:** Validation reports, deployment approvals, review meeting minutes, incident reports
5. **Data lineage:** End-to-end lineage from source system to model prediction

### Examination Preparation
- Maintain a "regulatory examination pack" that can be assembled within 48 hours
- Designate a point person for AI-related regulatory inquiries
- Conduct annual mock examinations for T1 systems
