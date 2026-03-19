# NIST AI Risk Management Framework — Mapping

## Overview

The NIST AI Risk Management Framework (AI RMF 1.0, January 2023) provides a voluntary framework for managing AI risks throughout the AI lifecycle. It is widely adopted in US-regulated industries and increasingly referenced globally.

This document maps our governance framework controls to the AI RMF's four core functions: Govern, Map, Measure, and Manage. Organizations seeking NIST AI RMF alignment can use this mapping to demonstrate how their AI governance satisfies the framework's expectations.

---

## Core Functions Alignment

| NIST AI RMF Function | Purpose | Framework Equivalent | Key References |
|---------------------|---------|---------------------|----------------|
| **Govern** | Establish organizational governance, culture, and accountability for AI risk | Operating model (roles, review cadence, escalation, board reporting) | [operating-model/](../operating-model/) |
| **Map** | Identify and contextualize AI risks through stakeholder engagement and risk framing | Risk classification (matrices, assessment templates, tier determination) | [risk-classification/](../risk-classification/) |
| **Measure** | Assess, analyze, and monitor AI risks through testing and evaluation | Lifecycle standards (validation, evaluation, monitoring) | [model-lifecycle/](../model-lifecycle/), [llm-lifecycle/](../llm-lifecycle/) |
| **Manage** | Prioritize, respond to, and communicate AI risks | Compliance, incident response, escalation, board reporting | [compliance/](./), [operating-model/](../operating-model/) |

---

## Govern Function Mapping

The Govern function establishes the organizational structures and culture for responsible AI.

| NIST Category | Description | Framework Control | Reference |
|--------------|-------------|-------------------|-----------|
| GV.1 — Policies | Organizational policies for AI risk management | Risk classification matrices define governance intensity; lifecycle standards define policies per tier; responsible AI standards define ethical policies | [Risk Matrix](../risk-classification/risk-matrix.md), [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md) |
| GV.2 — Accountability | Defined roles and responsibilities for AI risk | RACI matrices for traditional ML and GenAI; named roles (AI Risk Analyst, Prompt Engineer, LLMOps, Responsible AI Lead) | [Roles & Responsibilities](../operating-model/roles-responsibilities.md), [GenAI Roles](../operating-model/roles-genai.md) |
| GV.3 — Workforce | Workforce diversity and AI literacy | Governance training completion KPI tracked; training referenced in review cadence | [Governance Metrics](../operating-model/governance-metrics.md), [Review Cadence](../operating-model/review-cadence.md) |
| GV.4 — Organizational Context | Organizational risk culture and risk tolerance | AI risk appetite statement defined and board-approved; tiered governance reflects risk tolerance | [Board Reporting](../operating-model/board-reporting.md) |
| GV.5 — Processes | Risk management processes integrated into organizational functions | Review cadence (quarterly/monthly/weekly); deployment gates; GRC integration | [Review Cadence](../operating-model/review-cadence.md), [GRC Integration](../operating-model/grc-integration.md) |
| GV.6 — Stakeholder Engagement | Engagement with affected stakeholders | Escalation paths define communication; board reporting covers stakeholder communication; impact assessments consider stakeholders | [Escalation Paths](../operating-model/escalation-paths.md), [Board Reporting](../operating-model/board-reporting.md) |

---

## Map Function Mapping

The Map function identifies AI risks in context.

| NIST Category | Description | Framework Control | Reference |
|--------------|-------------|-------------------|-----------|
| MP.1 — Context | Intended purpose, context of use, and deployment environment | Risk assessment template captures use case, users, decision type, regulatory context; GenAI risk dimensions capture additional context | [Assessment Template](../risk-classification/assessment-template.yaml), [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md) |
| MP.2 — Categorization | AI system categorization and classification | Four-tier risk classification (T1–T4); GenAI, multimodal, and agentic-specific matrices provide comprehensive categorization | [Risk Matrix](../risk-classification/risk-matrix.md), [Multimodal Risk Matrix](../risk-classification/multimodal-risk-matrix.md) |
| MP.3 — Stakeholders | Stakeholder identification and engagement | Impact assessment template identifies affected stakeholders; model cards document intended users and out-of-scope uses | [Impact Assessment](../../templates/impact-assessment-template.md) |
| MP.4 — Risks | Risk identification and documentation | Risk assessment template with dimension scoring; agentic AI risk taxonomy; third-party model risk categories | [Agentic AI Risk](../risk-classification/agentic-ai-risk.md), [Third-Party Model Risk](third-party-model-risk.md) |
| MP.5 — Impacts | Impact assessment | Impact assessment template; escalation criteria define material impact thresholds; board reporting covers organizational impact | [Impact Assessment](../../templates/impact-assessment-template.md) |

---

## Measure Function Mapping

The Measure function assesses and monitors AI risks.

| NIST Category | Description | Framework Control | Reference |
|--------------|-------------|-------------------|-----------|
| MS.1 — Test and Evaluation | Appropriate methods for AI system testing | Validation requirements for traditional ML; evaluation suites for GenAI (hallucination, faithfulness, safety); red-teaming protocol for adversarial testing | [Validation](../model-lifecycle/validation.md), [Red-Teaming Protocol](../ai-security/red-teaming-protocol.md) |
| MS.2 — Metrics | AI system metrics and measurement | Governance metrics and KPIs; system-specific monitoring metrics; responsible AI KPIs | [Governance Metrics](../operating-model/governance-metrics.md) |
| MS.3 — Monitoring | Ongoing monitoring of AI systems | Production monitoring standards for traditional ML and LLMs; drift detection; alerting and escalation | [LLM Monitoring](../llm-lifecycle/monitoring.md), [ML Monitoring](../model-lifecycle/monitoring.md) |
| MS.4 — Feedback | Incorporating feedback into risk management | User feedback monitoring (thumbs up/down, escalation rate, regeneration rate); review cadence incorporates monitoring findings | [LLM Monitoring](../llm-lifecycle/monitoring.md), [Review Cadence](../operating-model/review-cadence.md) |

---

## Manage Function Mapping

The Manage function responds to and communicates about AI risks.

| NIST Category | Description | Framework Control | Reference |
|--------------|-------------|-------------------|-----------|
| MG.1 — Risk Treatment | Risk response and mitigation | Tiered governance controls; deployment gates enforce risk treatment; lifecycle standards define mandatory controls per tier | [Deployment Gates](../llm-lifecycle/deployment-gates.md), [Responsible AI Checklist](responsible-ai-checklist.md) |
| MG.2 — Incident Response | Response to AI-related incidents | Escalation paths with severity classification and response SLAs; incident report templates (traditional and GenAI); incident forensics protocol | [Escalation Paths](../operating-model/escalation-paths.md), [Incident Forensics](../operating-model/incident-forensics.md) |
| MG.3 — Risk Communication | Communication of AI risks to stakeholders | Board reporting structure; escalation communication templates; regulatory notification process | [Board Reporting](../operating-model/board-reporting.md), [Escalation Paths](../operating-model/escalation-paths.md) |
| MG.4 — Documentation | Documentation of AI risk management activities | Model cards, audit trails, risk assessments, incident reports — comprehensive documentation at every lifecycle stage | [Audit Trail](audit-trail-requirements.md), [Model Card Template](../../templates/model-card-template.yaml) |

---

## NIST AI RMF Profiles and Framework Tiers

The NIST AI RMF uses "profiles" to tailor risk management to organizational context. Our framework's tier system (T1–T4) serves a similar purpose:

| NIST Concept | Framework Equivalent |
|-------------|---------------------|
| Current Profile (where you are) | Current tier assignment for each AI system |
| Target Profile (where you want to be) | Governance requirements defined for each tier |
| Gap Analysis | Difference between current controls and tier requirements |
| Prioritization | Tier determines priority — T1 first, then T2, T3, T4 |

The framework's tiered approach inherently implements NIST's profile concept: every AI system is assessed, classified, and governed according to its risk profile.

---

## Gaps and Recommendations

| NIST Area | Current Coverage | Recommendation |
|-----------|-----------------|----------------|
| GV.3 — Workforce diversity and AI literacy | Training KPI tracked; no dedicated training program document | Consider adding an AI governance training program document |
| MP.3 — Broader stakeholder engagement | Impact assessment covers direct stakeholders; community impact less developed | Expand impact assessment to include broader societal impact for T1 systems |
| Cross-cutting — AI system inventory | Implied by portfolio KPIs and model cards | Consider maintaining a formal AI system registry as a standalone artifact |

---

## Implementation Notes

- NIST AI RMF is voluntary but increasingly referenced in US regulatory guidance (OCC, SEC, FTC)
- Organizations subject to both EU AI Act and NIST AI RMF can use this framework as a common implementation — the two frameworks are complementary, not contradictory
- NIST Companion Resource: the AI RMF Playbook provides additional guidance on implementing each subcategory — use it alongside this mapping for detailed implementation
