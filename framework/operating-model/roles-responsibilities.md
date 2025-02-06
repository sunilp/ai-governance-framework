# Roles and Responsibilities — RACI Matrix

## Purpose

Clear accountability is the foundation of effective AI governance. This document defines who is Responsible, Accountable, Consulted, and Informed for each governance activity.

## Key Roles

| Role | Description |
|------|-------------|
| **AI Risk Committee** | Senior leadership forum that oversees AI risk across the organization. Meets quarterly. |
| **Model Risk Management (MRM)** | Second-line function responsible for independent model validation and risk oversight. |
| **Business Owner** | Senior business stakeholder who owns the use case and accepts the risk. |
| **Data Science Lead** | Technical lead responsible for model development and performance. |
| **MLOps / Platform Engineering** | Responsible for model deployment, serving infrastructure, and monitoring. |
| **Compliance** | Ensures regulatory requirements are identified and met. |
| **Data Protection Officer (DPO)** | Oversees data privacy requirements and DPIAs. |
| **Internal Audit** | Provides independent assurance over the governance framework. |
| **Security** | Reviews security posture of AI systems and infrastructure. |

## RACI Matrix

### Model Development Phase

| Activity | Business Owner | DS Lead | MRM | Compliance | MLOps | AI Risk Committee |
|----------|---------------|---------|-----|------------|-------|-------------------|
| Define business requirements | **A** | C | I | C | I | I |
| Risk assessment and tiering | C | **R** | **A** | C | I | I (T1: **A**) |
| Data sourcing and quality | I | **R/A** | C | C | I | I |
| Model development | I | **R/A** | I | I | I | I |
| Bias and fairness testing | C | **R** | **A** (T1/T2) | C | I | I |
| Model documentation | I | **R/A** | C | I | I | I |

### Model Validation Phase

| Activity | Business Owner | DS Lead | MRM | Compliance | MLOps | AI Risk Committee |
|----------|---------------|---------|-----|------------|-------|-------------------|
| Independent validation | I | C | **R/A** | I | I | I |
| Challenger model development | I | **R** | **A** | I | I | I |
| Validation report review | C | C | **R/A** | C | I | I (T1) |

### Deployment Phase

| Activity | Business Owner | DS Lead | MRM | Compliance | MLOps | AI Risk Committee |
|----------|---------------|---------|-----|------------|-------|-------------------|
| Security review | I | C | I | I | **R** | I |
| Deployment approval (T1) | C | C | **R** | **R** | C | **A** |
| Deployment approval (T2) | **A** | **R** | C | C | C | I |
| Deployment execution | I | C | I | I | **R/A** | I |
| Post-deployment verification | C | **R** | C | I | **R** | I |

### Production Phase

| Activity | Business Owner | DS Lead | MRM | Compliance | MLOps | AI Risk Committee |
|----------|---------------|---------|-----|------------|-------|-------------------|
| Ongoing monitoring | I | C | I | I | **R/A** | I |
| Performance review (quarterly) | C | **R** | **A** (T1) | C | C | I (T1: **A**) |
| Incident response | C | **R** | C | C | **R** | I (P1: **A**) |
| Retraining decision | C | **R** | **A** (T1/T2) | I | C | I |
| Model retirement | **A** | **R** | C | C | **R** | I (T1) |

## Accountability Principles

1. **Single accountability:** Every AI system has exactly one Business Owner and one Data Science Lead. No shared accountability.
2. **Separation of duties:** The team that develops a model cannot independently validate it (T1/T2).
3. **Escalation obligation:** Any role holder who identifies a material risk is obligated to escalate, regardless of tier.
4. **Documentation duty:** Decisions must be documented. Verbal approvals are not sufficient for T1/T2 systems.
5. **Regulatory representation:** Compliance must be consulted on all T1/T2 systems and any system processing customer data.

## Onboarding New AI Systems

When a new AI system is proposed:

1. **Business Owner** submits a use case proposal with preliminary risk assessment
2. **Data Science Lead** is assigned and refines the risk assessment
3. **MRM** reviews and confirms the risk tier (T1/T2)
4. **Compliance** confirms regulatory requirements
5. **AI Risk Committee** approves initiation (T1) or is informed (T2/T3/T4)
6. All roles are documented in the AI system inventory
