# GRC Integration

## Overview

AI governance does not exist in a vacuum. Every regulated organization already has governance, risk, and compliance (GRC) functions — risk committees, control libraries, audit plans, and reporting frameworks. AI governance must plug into these existing structures, not create parallel bureaucracy.

This document maps AI governance controls to enterprise risk frameworks and defines how AI risk management integrates with first, second, and third lines of defense.

---

## COSO ERM Mapping

The Committee of Sponsoring Organizations (COSO) Enterprise Risk Management framework is widely adopted in financial services. Here is how AI governance maps to its five components.

| COSO Component | AI Governance Implementation | Framework Reference |
|---------------|------------------------------|-------------------|
| **Governance & Culture** | AI risk appetite defined and board-approved; AI-specific roles and responsibilities; governance training for AI practitioners | [Board Reporting](board-reporting.md), [Roles & Responsibilities](roles-responsibilities.md), [Roles — GenAI](roles-genai.md) |
| **Strategy & Objective Setting** | AI use case assessment against business strategy; risk tier determination aligns AI investment with risk tolerance | [Risk Matrix](../risk-classification/risk-matrix.md), [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md) |
| **Performance** | Production monitoring, governance metrics, responsible AI KPIs measure AI system performance against objectives | [Governance Metrics](governance-metrics.md), [LLM Monitoring](../llm-lifecycle/monitoring.md) |
| **Review & Revision** | Scheduled review cadence, incident-driven reviews, regulatory change assessments | [Review Cadence](review-cadence.md), [Regulatory Change Monitoring](../compliance/regulatory-change-monitoring.md) |
| **Information, Communication & Reporting** | Board reporting, escalation paths, incident communication templates | [Board Reporting](board-reporting.md), [Escalation Paths](escalation-paths.md) |

---

## ISO 31000 Mapping

ISO 31000 defines a generic risk management process. AI governance maps to each step.

| ISO 31000 Process Step | AI Governance Implementation | Framework Reference |
|------------------------|------------------------------|-------------------|
| Scope, context, criteria | Risk classification matrices define scope; regulatory context mapped | [Risk Matrix](../risk-classification/risk-matrix.md), [EU AI Act Mapping](../compliance/eu-ai-act-mapping.md) |
| Risk identification | Risk assessment template; GenAI and multimodal risk dimensions | [Assessment Template](../risk-classification/assessment-template.yaml), [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md) |
| Risk analysis | Tier determination (T1–T4); dimension scoring; impact assessment | [Impact Assessment Template](../../templates/impact-assessment-template.md) |
| Risk evaluation | Governance intensity mapped to tier; risk acceptance decisions | [Risk Matrix — Governance Intensity](../risk-classification/risk-matrix.md) |
| Risk treatment | Lifecycle controls, deployment gates, guardrails, human oversight | [Deployment Gates](../llm-lifecycle/deployment-gates.md), [Human-in-the-Loop](../responsible-ai/human-in-loop-patterns.md) |
| Monitoring and review | Production monitoring, review cadence, drift detection | [LLM Monitoring](../llm-lifecycle/monitoring.md), [Review Cadence](review-cadence.md) |
| Communication and consultation | Escalation paths, board reporting, incident communication | [Escalation Paths](escalation-paths.md), [Board Reporting](board-reporting.md) |
| Recording and reporting | Audit trail, model cards, incident reports | [Audit Trail](../compliance/audit-trail-requirements.md), [Model Card Template](../../templates/model-card-template.yaml) |

---

## Three Lines of Defense

| Line | AI Governance Role | Key Activities | Framework Files |
|------|-------------------|----------------|-----------------|
| **1st Line — AI Teams** | Build, test, deploy, and monitor AI systems per governance standards | Conduct risk assessments; follow lifecycle standards; maintain model cards; implement guardrails; respond to incidents | model-lifecycle/, llm-lifecycle/, templates/ |
| **2nd Line — AI Risk & Compliance** | Independent risk oversight, policy setting, challenge function | Define governance standards; review risk assessments; challenge tier assignments; monitor governance KPIs; regulatory mapping | risk-classification/, compliance/, operating-model/ |
| **3rd Line — Internal Audit** | Independent assurance of governance effectiveness | Audit AI governance framework application; test control effectiveness; report findings to audit committee | grc-integration (this file), [Audit Trail](../compliance/audit-trail-requirements.md) |

### 1st Line Responsibilities

- Conduct initial risk assessment using framework templates
- Follow lifecycle standards (development, validation, deployment, monitoring)
- Maintain model cards and keep them current
- Implement and maintain guardrails, safety filters, and human oversight
- Respond to incidents per escalation paths
- Track and report system-level metrics

### 2nd Line Responsibilities

- Define and maintain governance standards (this framework)
- Challenge 1st line risk assessments — verify tier assignments are appropriate
- Monitor governance health KPIs across the portfolio
- Conduct independent model validation for T1 systems
- Map controls to regulatory requirements
- Report to AI Risk Committee and board

### 3rd Line Responsibilities

- Develop AI-specific audit universe and risk-based audit plan
- Test whether governance controls are operating effectively
- Verify that 1st and 2nd line activities are performed as documented
- Report findings to Audit Committee independently of management
- Follow up on remediation of audit findings

---

## Control Embedding

### Mapping AI Controls to Enterprise Control Libraries

Organizations with existing control frameworks (SOX, operational risk, IT general controls) should map AI governance controls to those frameworks rather than creating a separate AI control library.

| AI Governance Control | Enterprise Control Category | Integration Approach |
|----------------------|---------------------------|---------------------|
| Risk assessment completion | Operational risk | Add AI systems to operational risk register; link AI risk assessments |
| Deployment gate sign-off | Change management | Include AI deployment gates in existing change management process |
| Model card maintenance | IT asset management | Register AI systems as IT assets; link model cards |
| Audit trail and logging | IT general controls | Extend existing logging and retention controls to AI systems |
| Incident response | Operational resilience | Include AI incidents in existing incident management process |
| Vendor risk assessment | Third-party risk management | Include AI model providers in existing TPRM program |
| Data governance | Data management | Extend existing data governance to AI training data, prompts, and outputs |

### GRC Platform Integration

If the organization uses a GRC platform (ServiceNow GRC, Archer, LogicGate, etc.):
- Register AI systems as risk entities in the platform
- Map AI governance controls to the platform's control taxonomy
- Track AI risk assessments, findings, and remediation in the platform
- Generate AI governance reports from the platform for consistency with other risk domains

---

## Audit Integration

### AI Audit Universe

Internal audit should maintain an AI audit universe covering:

| Audit Area | Focus | Frequency |
|-----------|-------|-----------|
| AI governance framework effectiveness | Are standards applied consistently? Are reviews happening? | Annual |
| T1 system deep dive | Full audit of a specific T1 system: risk assessment, controls, monitoring | Annual (rotate systems) |
| Model validation independence | Is 2nd line challenge function operating? Are validations independent? | Annual |
| Data governance for AI | Training data quality, RAG corpus integrity, data lineage | Annual |
| AI vendor risk management | Are vendor assessments current? Exit strategies documented? | Annual |
| Incident response effectiveness | Are incidents detected, responded to, and learned from? | Biennial |
| Regulatory compliance | Are regulatory mapping and compliance evidence current? | Annual |

### AI-Specific Audit Procedures

In addition to standard audit techniques, AI audits should include:
- Re-execution of risk assessments to verify tier classification accuracy
- Sample testing of deployment gate evidence (were gates actually enforced?)
- Evaluation suite re-run on production systems (do current scores match documented scores?)
- Review of model card accuracy against observed system behavior
- Prompt audit — are production prompts consistent with reviewed and approved versions?
- Log completeness testing — are audit trails actually capturing what they claim to?

---

## Implementation Notes

- Start by mapping T1 systems into existing GRC structures. Expand to T2/T3/T4 as integration matures.
- Do not create parallel governance processes. If the organization already has change management, use it — add AI-specific gates, don't build a separate process.
- Audit integration is iterative. Year 1: framework effectiveness audit. Year 2: add system-specific deep dives. Year 3: full AI audit program.
