# ISO/IEC 42001 — AI Management System Mapping

## Overview

ISO/IEC 42001:2023 is the international standard for AI Management Systems (AIMS). It defines requirements for establishing, implementing, maintaining, and continually improving an AI management system within an organization.

Organizations pursuing ISO 42001 certification can use this governance framework as their implementation backbone. This document maps the standard's clauses and Annex A controls to specific framework components.

---

## Clause Mapping

### Clause 4 — Context of the Organization

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 4.1 Understanding the organization and its context | Risk classification matrices define AI risk context; regulatory alignment maps external requirements | [Risk Matrix](../risk-classification/risk-matrix.md), [Multi-Jurisdictional Guide](multi-jurisdictional-guide.md) |
| 4.2 Understanding needs and expectations of interested parties | Impact assessment template identifies stakeholders and their requirements; model cards document intended users | [Impact Assessment](../../templates/impact-assessment-template.md), [Model Card Template](../../templates/model-card-template.yaml) |
| 4.3 Determining the scope of the AIMS | Portfolio KPIs define the AI system inventory; tier classification determines governance scope | [Governance Metrics](../operating-model/governance-metrics.md) |
| 4.4 AI management system | This framework constitutes the AIMS: risk classification, lifecycle standards, compliance mapping, operating model, responsible AI standards | This framework |

### Clause 5 — Leadership

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 5.1 Leadership and commitment | Board-level AI risk reporting; AI risk appetite statement; AI Risk Committee charter | [Board Reporting](../operating-model/board-reporting.md) |
| 5.2 AI policy | Risk classification, lifecycle standards, and responsible AI standards constitute the AI policy | [Responsible AI Checklist](responsible-ai-checklist.md), [Transparency Standards](../responsible-ai/transparency-standards.md) |
| 5.3 Organizational roles, responsibilities, and authorities | RACI matrices for traditional ML and GenAI; named roles with defined responsibilities | [Roles & Responsibilities](../operating-model/roles-responsibilities.md), [GenAI Roles](../operating-model/roles-genai.md) |

### Clause 6 — Planning

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 6.1 Actions to address risks and opportunities | Risk assessment template with dimension scoring; tiered governance controls; GenAI, multimodal, and agentic risk matrices | [Assessment Template](../risk-classification/assessment-template.yaml), [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md) |
| 6.2 AI objectives and planning to achieve them | Governance health KPIs define measurable objectives; adoption approach defines phased implementation | [Governance Metrics](../operating-model/governance-metrics.md) |

### Clause 7 — Support

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 7.1 Resources | Cost governance defines budgeting and resource allocation for AI systems | [Cost Governance](../operating-model/cost-governance.md) |
| 7.2 Competence | Governance training completion KPI; review cadence includes annual training program | [Governance Metrics](../operating-model/governance-metrics.md) |
| 7.3 Awareness | Escalation paths and review cadence ensure organizational awareness of AI governance requirements | [Escalation Paths](../operating-model/escalation-paths.md) |
| 7.4 Communication | Board reporting, escalation communication templates, stakeholder notification protocols | [Board Reporting](../operating-model/board-reporting.md), [Escalation Paths](../operating-model/escalation-paths.md) |
| 7.5 Documented information | Model cards, risk assessments, audit trails, incident reports — documented at every lifecycle stage | [Audit Trail](audit-trail-requirements.md), [Model Card Template](../../templates/model-card-template.yaml) |

### Clause 8 — Operation

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 8.1 Operational planning and control | Lifecycle standards (development, validation, deployment, monitoring) define operational controls | [Development](../model-lifecycle/development.md), [Deployment](../model-lifecycle/deployment.md) |
| 8.2 AI risk assessment | Risk assessment template; tier determination process; GenAI and multimodal risk matrices | [Assessment Template](../risk-classification/assessment-template.yaml) |
| 8.3 AI risk treatment | Tiered governance controls; deployment gates; guardrails; human oversight patterns | [Deployment Gates](../llm-lifecycle/deployment-gates.md), [Human-in-the-Loop](../responsible-ai/human-in-loop-patterns.md) |
| 8.4 AI system impact assessment | Impact assessment template; responsible AI checklist | [Impact Assessment](../../templates/impact-assessment-template.md), [Responsible AI Checklist](responsible-ai-checklist.md) |

### Clause 9 — Performance Evaluation

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 9.1 Monitoring, measurement, analysis, and evaluation | Governance metrics and KPIs; production monitoring; LLM monitoring | [Governance Metrics](../operating-model/governance-metrics.md), [LLM Monitoring](../llm-lifecycle/monitoring.md) |
| 9.2 Internal audit | GRC integration defines AI audit universe and procedures; three lines of defense model | [GRC Integration](../operating-model/grc-integration.md) |
| 9.3 Management review | Review cadence (quarterly AI Risk Committee, monthly model review, weekly ops standup) | [Review Cadence](../operating-model/review-cadence.md) |

### Clause 10 — Improvement

| ISO 42001 Requirement | Framework Implementation | Reference |
|----------------------|--------------------------|-----------|
| 10.1 Continual improvement | Review cadence drives continuous improvement; post-mortem process identifies systemic improvements; regulatory change monitoring triggers framework updates | [Review Cadence](../operating-model/review-cadence.md), [Incident Forensics](../operating-model/incident-forensics.md) |
| 10.2 Nonconformity and corrective action | Incident response (escalation paths, incident reports, forensics); audit finding remediation tracking | [Escalation Paths](../operating-model/escalation-paths.md), [Incident Report — GenAI](../../templates/incident-report-genai.md) |

---

## Annex A Controls Mapping

ISO 42001 Annex A defines 38 controls organized across domains. Key controls mapped to our framework:

| Annex A Control | Description | Framework Implementation | Reference |
|----------------|-------------|--------------------------|-----------|
| A.2 — AI policy | Policy for responsible AI use | Responsible AI standards; risk classification | responsible-ai/, risk-classification/ |
| A.3 — AI system roles | Defined roles for AI system development and use | RACI matrices; GenAI-specific roles | [Roles](../operating-model/roles-responsibilities.md) |
| A.4 — AI resources | Resources for AI activities | Cost governance; infrastructure standards | [Cost Governance](../operating-model/cost-governance.md) |
| A.5 — AI impact assessment | Assessment of AI system impacts | Impact assessment template; risk assessment | [Impact Assessment](../../templates/impact-assessment-template.md) |
| A.6 — AI system lifecycle | Lifecycle processes for AI systems | Full lifecycle standards (development → monitoring) | model-lifecycle/, llm-lifecycle/ |
| A.7 — Data management | Data quality and governance | Development standards (data quality); RAG governance; data residency | [RAG Governance](../llm-lifecycle/rag-governance.md), [Data Residency](data-residency-llm.md) |
| A.8 — AI technology and model | Model development and selection | Model selection criteria; fine-tuning governance; open-source governance | [Model Selection](../llm-lifecycle/model-selection.md) |
| A.9 — Third-party | Third-party AI component management | Third-party model risk assessment; supply chain security | [Third-Party Risk](third-party-model-risk.md), [Supply Chain](../ai-security/supply-chain-security.md) |
| A.10 — AI system monitoring | Monitoring and measurement | Production monitoring (ML and LLM); drift detection; governance metrics | [LLM Monitoring](../llm-lifecycle/monitoring.md) |

---

## Certification Readiness

### What This Framework Provides

| ISO 42001 Area | Evidence From Framework |
|---------------|------------------------|
| AI management system documentation | This framework, README, all component documents |
| Risk assessment methodology | Risk matrices, assessment templates, tier determination |
| Lifecycle procedures | Development, validation, deployment, monitoring standards |
| Roles and responsibilities | RACI matrices, role descriptions |
| Monitoring and measurement | KPI framework, monitoring standards |
| Incident management | Escalation paths, incident templates, forensics protocol |
| Audit procedures | GRC integration, audit universe, audit procedures |

### What Organizations Must Produce Additionally

| ISO 42001 Area | Organization-Specific Evidence Needed |
|---------------|--------------------------------------|
| Statement of Applicability | Organization's specific scope and control selection |
| Risk treatment plan | Organization's specific risk treatment decisions for each AI system |
| Training records | Evidence of staff completing governance training |
| Internal audit reports | Actual audit reports for AI systems |
| Management review minutes | AI Risk Committee meeting minutes |
| Incident records | Actual incident reports |
| Corrective action records | Evidence of remediation completion |
| AI system inventory | Registry of all AI systems with tier classification |

---

## Integration with ISO 27001

Organizations already ISO 27001 certified benefit from significant overlap:

| Shared Area | ISO 27001 | ISO 42001 Extension |
|------------|-----------|-------------------|
| Risk management | ISMS risk assessment | Extend to AI-specific risks (hallucination, bias, prompt injection) |
| Access control | Information access controls | Extend to model access, prompt access, training data access |
| Incident management | Security incident process | Extend to AI incidents (hallucination, safety bypass, bias) |
| Supplier management | Supplier security assessment | Extend to AI model provider assessment |
| Asset management | Information asset register | Extend to AI system inventory |
| Internal audit | ISMS audit program | Extend to AI governance audit |

The AIMS can be integrated into the existing ISMS rather than managed as a separate system.

---

## Implementation Notes

- ISO 42001 certification audits examine evidence of implementation, not just documentation. Ensure controls are operating, not just written.
- The standard requires continual improvement — static governance that never changes will fail certification renewal.
- Certification timeline: typically 6–12 months from decision to certification, assuming the governance framework is already in place.
- Maintenance: surveillance audits annually; recertification every 3 years.
