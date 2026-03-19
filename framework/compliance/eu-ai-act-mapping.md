# EU AI Act — Framework Mapping

## Overview

The EU AI Act (Regulation 2024/1689) establishes a risk-based regulatory framework for AI systems. This document maps our governance framework controls to the Act's requirements, with a focus on high-risk AI systems (Title III, Chapter 2) which are most relevant to financial services.

## Risk Classification Alignment

| EU AI Act Category | Framework Tier | Examples in Financial Services |
|-------------------|---------------|-------------------------------|
| Unacceptable Risk (Art. 5) | Prohibited | Social scoring, real-time biometric identification (unless exempted) |
| High Risk (Art. 6, Annex III) | T1, T2 | Creditworthiness assessment, insurance pricing, fraud detection used for law enforcement cooperation |
| Limited Risk (Art. 50) | T3 | Customer-facing chatbots (transparency obligation), emotion recognition |
| Minimal Risk | T4 | Internal analytics, spam filters, search ranking |

## High-Risk System Requirements Mapping

### Article 9 — Risk Management System

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Continuous iterative risk management process | Risk classification matrix + quarterly reviews | [Risk Matrix](../risk-classification/risk-matrix.md) |
| Identification and analysis of known and foreseeable risks | Risk assessment template — 5 dimension scoring | [Assessment Template](../risk-classification/assessment-template.yaml) |
| Estimation and evaluation of risks from intended use and misuse | Impact assessment template | [Impact Assessment](../../templates/impact-assessment-template.md) |
| Adoption of risk management measures | Tiered governance controls proportional to risk | [Risk Matrix — Governance Intensity](../risk-classification/risk-matrix.md) |
| Testing to identify appropriate risk management measures | Validation requirements — robustness and stress testing | [Validation](../model-lifecycle/validation.md) |

### Article 10 — Data and Data Governance

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Training data subject to appropriate data governance | Development standards — data quality and governance requirements | [Development](../model-lifecycle/development.md) |
| Data quality criteria (relevance, representativeness, completeness) | Data quality assessment in development standards | [Development](../model-lifecycle/development.md) |
| Examination for possible biases | Bias and fairness testing requirements | [Development](../model-lifecycle/development.md) |

### Article 11 — Technical Documentation

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Technical documentation drawn up before placing on market | Model development document + model card | [Model Card Template](../../templates/model-card-template.yaml) |
| Kept up to date | Version control and quarterly review requirements | [Monitoring](../model-lifecycle/monitoring.md) |

### Article 12 — Record-Keeping

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Automatic logging of events | Audit trail requirements — prediction logging, decision recording | [Audit Trail](audit-trail-requirements.md) |
| Logging capabilities commensurate with intended purpose | Tiered logging requirements by risk tier | [Audit Trail](audit-trail-requirements.md) |
| Traceability throughout lifecycle | Data lineage + model versioning requirements | [Development](../model-lifecycle/development.md) |

### Article 13 — Transparency and Information to Deployers

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Designed to allow deployers to interpret output | Explainability requirements in validation | [Validation](../model-lifecycle/validation.md) |
| Instructions for use | Operational runbook and model documentation | Model card + deployment documentation |
| Human oversight measures | Human oversight levels defined in risk assessment | [Assessment Template](../risk-classification/assessment-template.yaml) |

### Article 14 — Human Oversight

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Designed to be effectively overseen by natural persons | Human oversight levels (in-the-loop, on-the-loop) defined per tier | [Assessment Template](../risk-classification/assessment-template.yaml) |
| Enable individuals to understand capabilities and limitations | Model card includes limitations section | [Model Card Template](../../templates/model-card-template.yaml) |
| Enable override or reversal of output | Rollback procedures and override mechanisms | [Deployment](../model-lifecycle/deployment.md) |

### Article 15 — Accuracy, Robustness, and Cybersecurity

| EU AI Act Requirement | Framework Control | Reference |
|----------------------|-------------------|-----------|
| Appropriate levels of accuracy | Performance validation with defined thresholds | [Validation](../model-lifecycle/validation.md) |
| Resilient to errors, faults, inconsistencies | Robustness testing, stress testing requirements | [Validation](../model-lifecycle/validation.md) |
| Resilient to unauthorized third-party manipulation | Security review in deployment gates, adversarial testing | [Deployment](../model-lifecycle/deployment.md) |

## Transparency Obligations (Article 50)

For AI systems that interact directly with people (e.g., chatbots):
- Users must be informed they are interacting with an AI system
- This applies to T3 systems in our framework
- Implementation: Clear disclosure at point of interaction

## Conformity Assessment

For high-risk AI systems (T1 in our framework):
1. Framework controls satisfy the internal conformity assessment procedure (Annex VI)
2. The validation report serves as evidence of conformity with Articles 9–15
3. The model card + development document + validation report together constitute the required technical documentation
4. Quarterly reviews provide ongoing conformity monitoring

## Implementation Notes

- The EU AI Act applies to AI systems placed on the market or put into service in the EU, regardless of where the provider is established
- Financial services AI systems may also be subject to sector-specific requirements (CRD, Solvency II, MiFID II) that complement the AI Act
- This mapping should be reviewed whenever the Act's delegated or implementing acts are published

---

## Enforcement Status (as of March 2026)

| Obligation | Effective Date | Status | Action Required |
|-----------|---------------|--------|----------------|
| Prohibited AI practices (Art. 5) | February 2025 | **In force** | Verify no prohibited AI practices in portfolio |
| GPAI model obligations (Art. 53–55) | August 2025 | **In force** | Verify model provider compliance; see [GenAI mapping](eu-ai-act-genai-mapping.md) |
| Transparency obligations (Art. 50) | August 2025 | **In force** | Ensure AI disclosure on all customer-facing systems |
| High-risk AI system requirements (Art. 6–15) | August 2026 | **5 months to compliance** | Finalize conformity assessment for all T1 systems |
| Annex I high-risk (regulated products) | August 2027 | Coming | Monitor and prepare |

---

## Compliance Evidence Requirements

What auditors and regulators expect to see for each article:

| Article | Required Evidence | Framework Source |
|---------|------------------|-----------------|
| Art. 9 — Risk Management | Completed risk assessments; review meeting minutes; remediation tracking | Risk assessment templates; review cadence records |
| Art. 10 — Data Governance | Data quality reports; bias testing results; data lineage documentation | Development standards; evaluation records |
| Art. 11 — Technical Documentation | Model cards; architecture documents; change history | [Model Card Template](../../templates/model-card-template.yaml); audit trail |
| Art. 12 — Record-Keeping | Audit trail exports; log retention evidence | [Audit Trail Requirements](audit-trail-requirements.md) |
| Art. 13 — Transparency | User-facing AI disclosures; model documentation | [Transparency Standards](../responsible-ai/transparency-standards.md) |
| Art. 14 — Human Oversight | Oversight procedure documentation; override logs | [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md) |
| Art. 15 — Accuracy/Robustness | Validation reports; adversarial testing results; security assessments | [Validation](../model-lifecycle/validation.md); [Red-Teaming Protocol](../ai-security/red-teaming-protocol.md) |

