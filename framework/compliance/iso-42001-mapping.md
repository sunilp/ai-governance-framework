# ISO/IEC 42001 AI Management System Mapping

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

## Overview

ISO/IEC 42001:2023 (published 18 December 2023) specifies requirements for establishing, implementing, maintaining and continually improving an AI management system (AIMS). Clauses 4 to 10 are mandatory. Annex A lists 38 reference controls under nine control objectives (A.2 to A.10); an organization selects the controls it needs and records the selection in a Statement of Applicability.

This framework supplies much of the operational content an AIMS needs: risk and impact assessment, lifecycle controls, monitoring, incident handling and audit integration. It is not an AIMS on its own. A certification audit also needs organization-specific documents that the framework does not provide; they are listed under [Certification Readiness](#certification-readiness).

This document maps clauses 4 to 10 and the Annex A control objectives to framework documents and to control IDs in the [control register](../governance-operations/control-register.md).

---

## Clause Mapping

### Clause 4: Context of the organization

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 4.1 Understanding the organization and its context | Risk classification defines AI risk context; regulatory mappings capture external requirements; regulatory change monitoring keeps them current | RV-004 | [Risk Matrix](../risk-classification/risk-matrix.md), [Multi-Jurisdictional Guide](multi-jurisdictional-guide.md), [Regulatory Change Monitoring](regulatory-change-monitoring.md) |
| 4.2 Understanding the needs and expectations of interested parties | Impact assessment identifies affected stakeholders; model cards document intended users | RA-003, DE-001 | [Impact Assessment](../../templates/impact-assessment-template.md), [Model Card Template](../../templates/model-card-template.yaml) |
| 4.3 Determining the scope of the AI management system | Tier classification sets governance scope per system. No AIMS scope statement is provided; the organization must write one | RA-001. Scope statement: No control yet (gap) | [Risk Matrix](../risk-classification/risk-matrix.md), [Governance Metrics](../operating-model/governance-metrics.md) |
| 4.4 AI management system | The governance workflow, control register and supporting standards supply AIMS processes; the organization must establish and maintain the AIMS itself | All register controls | [Governance Workflow](../governance-operations/governance-workflow.md), [Control Register](../governance-operations/control-register.md) |

### Clause 5: Leadership

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 5.1 Leadership and commitment | Board-level AI risk reporting; board-approved AI risk appetite statement; AI Risk Committee membership and agenda. No AI Risk Committee charter document exists | RA-004, DA-002 (AI Risk Committee approves T1) | [Board Reporting](../operating-model/board-reporting.md), [Review Cadence](../operating-model/review-cadence.md) |
| 5.2 AI policy | The framework's standards can be the basis of an AI policy, but there is no top-management-approved AI policy document | No control yet (gap) | [Responsible AI Checklist](responsible-ai-checklist.md), [Transparency Standards](../responsible-ai/transparency-standards.md) |
| 5.3 Roles, responsibilities and authorities | RACI matrices for traditional ML and GenAI; named control owners; tiered approvers | RA-004, DA-002 | [Roles & Responsibilities](../operating-model/roles-responsibilities.md), [GenAI Roles](../operating-model/roles-genai.md) |

### Clause 6: Planning

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 6.1.1 General (actions to address risks and opportunities) | Tiered governance; risk appetite; GenAI, multimodal and agentic risk matrices | RA-001 | [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md), [Board Reporting](../operating-model/board-reporting.md) |
| 6.1.2 AI risk assessment | Risk assessment template with dimension scoring and the override list | RA-001, RA-002, RA-004 | [Assessment Template](../risk-classification/assessment-template.yaml) |
| 6.1.3 AI risk treatment (including the Statement of Applicability) | Register controls by tier; exceptions with risk acceptance. No Statement of Applicability template | Stage 3 to 8 controls. Statement of Applicability: No control yet (gap) | [Control Register](../governance-operations/control-register.md), [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance) |
| 6.1.4 AI system impact assessment | Impact assessment template; DPIA | RA-003, RA-005 | [Impact Assessment](../../templates/impact-assessment-template.md) |
| 6.2 AI objectives and planning to achieve them | Governance health KPIs and targets. These are not set out as AIMS objectives with plans to achieve them | No control yet (gap) | [Governance Metrics](../operating-model/governance-metrics.md) |
| 6.3 Planning of changes | Annual framework review (Head of MRM, Q1); regulatory change impact assessment. No documented procedure for planning changes to the AIMS itself | RV-004 (regulatory changes only). AIMS change planning: No control yet (gap) | [Review Cadence](../operating-model/review-cadence.md#annual-activities), [Regulatory Change Monitoring](regulatory-change-monitoring.md) |

### Clause 7: Support

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 7.1 Resources | Cost governance; resource documentation in the AI-BOM and architecture document | AR-001, SR-004, PM-005 | [Cost Governance](../operating-model/cost-governance.md), [Supply Chain Security](../ai-security/supply-chain-security.md#ai-bill-of-materials-ai-bom) |
| 7.2 Competence | Governance training completion KPI; ongoing training and awareness program listed as an annual activity; reviewer training for human oversight. No training program document | No control yet (gap) | [Governance Metrics](../operating-model/governance-metrics.md), [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md) |
| 7.3 Awareness | Escalation paths and review cadence make governance duties visible | No register control | [Escalation Paths](../operating-model/escalation-paths.md) |
| 7.4 Communication | Board reporting, escalation communication templates, regulatory notification | IR-003 | [Board Reporting](../operating-model/board-reporting.md), [Escalation Paths](../operating-model/escalation-paths.md#communication-templates) |
| 7.5 Documented information | Model cards, risk assessments, evidence packs, audit trails and incident reports; retention on retirement | DE-001, DA-001, DR-003 | [Audit Trail](audit-trail-requirements.md), [Prompt Audit Trail](prompt-audit-trail.md) |

### Clause 8: Operation

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 8.1 Operational planning and control | Lifecycle standards and the 10-stage governance workflow | DA-003, PM-001 | [Governance Workflow](../governance-operations/governance-workflow.md), [Development](../model-lifecycle/development.md), [Deployment](../model-lifecycle/deployment.md) |
| 8.2 AI risk assessment | Risk assessment at intake and re-tiering at each formal review and on material change | RA-001, RV-001, RV-003 | [Assessment Template](../risk-classification/assessment-template.yaml), [Review Cadence](../operating-model/review-cadence.md) |
| 8.3 AI risk treatment | Deployment gates; guardrails; adversarial defenses; human oversight | DA-003, DE-004, SR-003, PM-003 | [Deployment Gates](../llm-lifecycle/deployment-gates.md), [Human-in-the-Loop](../responsible-ai/human-in-loop-patterns.md) |
| 8.4 AI system impact assessment | Impact assessment, repeated on material change | RA-003, RV-003 | [Impact Assessment](../../templates/impact-assessment-template.md), [Responsible AI Checklist](responsible-ai-checklist.md) |

### Clause 9: Performance evaluation

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 9.1 Monitoring, measurement, analysis and evaluation | Governance metrics and KPIs; production monitoring and evaluation | PM-001, PM-002, PM-004 | [Governance Metrics](../operating-model/governance-metrics.md), [LLM Monitoring](../llm-lifecycle/monitoring.md) |
| 9.2 Internal audit | AI audit universe and audit procedures; annual internal audit of AI governance (Q2) | No register control (audit is a third-line activity) | [GRC Integration](../operating-model/grc-integration.md#audit-integration), [Review Cadence](../operating-model/review-cadence.md#annual-activities) |
| 9.3 Management review | Monthly AI Risk Committee, with a full-portfolio meeting each quarter; monthly Model Review Board; formal reviews per system | RV-001 | [Review Cadence](../operating-model/review-cadence.md) |

### Clause 10: Improvement

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 10.1 Continual improvement | Annual framework review; post-mortems identify systemic fixes; regulatory change monitoring triggers updates | IR-004, RV-004 | [Review Cadence](../operating-model/review-cadence.md), [Incident Forensics](../operating-model/incident-forensics.md) |
| 10.2 Nonconformity and corrective action | Incident handling, post-mortems and remediation tracking; failed controls escalate per the register | IR-003, IR-004, IR-005 | [Escalation Paths](../operating-model/escalation-paths.md), [GenAI Incident Report](../../templates/incident-report-genai.md) |

---

## Annex A Controls Mapping

Annex A has 38 controls under nine control objectives. Mapping at control-objective level:

| Annex A Control Objective | Framework Implementation | Controls | Reference |
|----------------|--------------------------|----------|-----------|
| A.2 Policies related to AI | Framework standards; no approved AI policy document (see clause 5.2) | No control yet (gap) | [responsible-ai/](../responsible-ai/), [risk-classification/](../risk-classification/) |
| A.3 Internal organization | Roles and RACI; tiered approvers. No process for staff to report concerns about AI systems | RA-004, DA-002. Reporting of concerns: No control yet (gap) | [Roles](../operating-model/roles-responsibilities.md), [Escalation Paths](../operating-model/escalation-paths.md) |
| A.4 Resources for AI systems | Resource documentation: AI-BOM (models, data, tooling), architecture document, cost governance, roles | AR-001, SR-004, PM-005 | [Supply Chain Security](../ai-security/supply-chain-security.md#ai-bill-of-materials-ai-bom), [Cost Governance](../operating-model/cost-governance.md) |
| A.5 Assessing impacts of AI systems | Impact assessment; DPIA; bias evaluation | RA-003, RA-005, EV-005 | [Impact Assessment](../../templates/impact-assessment-template.md) |
| A.6 AI system life cycle | Lifecycle standards from design to retirement: development, evaluation, deployment gates, monitoring, technical documentation, deprecation | DE-001 to DE-005, EV-001 to EV-007, DA-001 to DA-004, PM-001 to PM-005, DR-001 to DR-004 | [model-lifecycle/](../model-lifecycle/), [llm-lifecycle/](../llm-lifecycle/) |
| A.7 Data for AI systems | Data governance and provenance for training and fine-tuning data; RAG corpus integrity; eval dataset integrity; data residency | DE-005, EV-004, EV-006, AR-003 | [RAG Governance](../llm-lifecycle/rag-governance.md), [Fine-Tuning Governance](../llm-lifecycle/fine-tuning-governance.md), [Data Residency](data-residency-llm.md) |
| A.8 Information for interested parties of AI systems | AI disclosure and content labeling; model cards; incident communication and regulatory notification. No channel for external parties to report adverse impacts | DE-001, IR-003 | [Transparency Standards](../responsible-ai/transparency-standards.md), [Escalation Paths](../operating-model/escalation-paths.md#regulatory-notification) |
| A.9 Use of AI systems | Intended use and out-of-scope use in model cards; human oversight patterns; hallucination tolerance by use case | DE-001, PM-003 | [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md), [Hallucination Policy](../responsible-ai/hallucination-policy.md) |
| A.10 Third-party and customer relationships | Vendor selection and risk assessment; supply chain security; exit strategy. Obligations to the organization's own customers who use its AI systems are not covered | AR-004, AR-005, SR-004 | [Third-Party Risk](third-party-model-risk.md), [Supply Chain](../ai-security/supply-chain-security.md) |

---

## Certification Readiness

### What This Framework Provides

| ISO 42001 Area | Evidence From Framework |
|---------------|------------------------|
| Risk assessment and treatment methodology | Risk matrices, assessment template, tier determination, control register |
| Impact assessment | Impact assessment template, DPIA control |
| Lifecycle procedures | Development, validation, deployment, monitoring and deprecation standards |
| Roles and responsibilities | RACI matrices, role descriptions, named control owners |
| Monitoring and measurement | KPI framework, monitoring standards |
| Incident management | Escalation paths, incident templates, forensics protocol |
| Audit procedures | GRC integration, audit universe, audit procedures |

### Gaps a Certification Audit Will Find

These are missing from the framework. Each is a document the organization must write and approve.

| ISO 42001 Requirement | What Is Missing |
|---------------|--------------------------------------|
| 4.3 Scope of the AIMS | AIMS scope statement |
| 5.1 Leadership | AI Risk Committee charter (membership and agenda exist in review cadence; terms of reference, authority and quorum do not) |
| 5.2 and A.2 AI policy | AI policy approved by top management |
| 6.1.3 Statement of Applicability | Statement of Applicability with justification for each included or excluded Annex A control |
| 6.2 AI objectives | Documented, measurable AI objectives and plans to achieve them |
| 6.3 Planning of changes | Procedure for planning changes to the AIMS |
| 7.2 Competence | Training program and competence records |
| A.3 Internal organization | Process for staff to report concerns about AI systems |
| A.8 External reporting | Channel for interested parties to report adverse impacts |

### What Organizations Must Produce From Operating the AIMS

| ISO 42001 Area | Organization-Specific Evidence Needed |
|---------------|--------------------------------------|
| Risk treatment plan | Risk treatment decisions for each AI system |
| Training records | Evidence of staff completing governance training |
| Internal audit reports | Audit reports for AI systems and the AIMS |
| Management review minutes | AI Risk Committee meeting minutes |
| Incident records | Incident reports |
| Corrective action records | Evidence of remediation completion |
| AI system inventory | Registry of all AI systems with tier classification |

---

## Companion Standards

| Standard | Status | How it relates to 42001 and this framework |
|----------|--------|--------------------------------------------|
| ISO/IEC 42005:2025, AI system impact assessment | Published 28 May 2025. Guidance standard | Guidance for the impact assessment required by 6.1.4, 8.4 and A.5; use it to strengthen the [impact assessment template](../../templates/impact-assessment-template.md) (RA-003) |
| ISO/IEC 42006:2025, requirements for bodies providing audit and certification of AI management systems | Published 7 July 2025 | Sets requirements for certification bodies that audit against ISO/IEC 42001 |
| EN ISO/IEC 42001:2026 | European adoption of ISO/IEC 42001:2023, published in 2026 | Same requirements. It is not a harmonised standard under the EU AI Act, so certification gives no presumption of conformity with the Act |
| EN 18286:2026, Artificial intelligence: Quality management system for EU AI Act regulatory purposes | Harmonised standard. Its reference was published in the Official Journal on 14 October 2026 by Commission Implementing Decision (EU) 2026/2274 | Gives providers of high-risk AI systems a presumption of conformity with the Article 17 quality management system requirements it covers. Its informative annexes map its clauses to ISO 9001 and ISO/IEC 42001, so an existing 42001 AIMS can be extended rather than duplicated. The mapping shows clause correspondence, not equivalence: a 42001 certificate alone gives no presumption. High-risk obligations apply from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems; see [EU AI Act mapping](eu-ai-act-mapping.md) |
| ISO/IEC 27090:2026, addressing security threats and compromises to AI systems | Published October 2026. Guidance | Security guidance alongside ISO/IEC 27001 and 27002; relevant to [ai-security/](../ai-security/) and controls SR-001 to SR-004 |

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

---

## Sources

- EVS (Estonian Centre for Standardisation), ISO/IEC 42001:2023: https://www.evs.ee/en/iso-iec-42001-2023
- Advisera, ISO 42001 requirements: clauses and structure: https://advisera.com/articles/iso-42001-clauses-requirements/
- ISMS.online, ISO 42001 Annex A controls: https://www.isms.online/iso-42001/annex-a-controls/
- ISMS.online, ISO 42001 checklist (Statement of Applicability under 6.1.3): https://www.isms.online/iso-42001/checklist/
- Schellman, How ISO 42001 aims to promote trustworthy AI (Annex A areas, 38 controls): https://www.schellman.com/blog/iso-certifications/how-iso-42001-aims-to-promote-trustworthy-ai
- NIST AIRC, NIST AI RMF to ISO/IEC FDIS 42001 crosswalk: https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf
- EVS, ISO/IEC 42005:2025: https://www.evs.ee/en/iso-iec-42005-2025
- CMS, ISO/IEC 42005:2025 overview: https://cms.law/en/gbr/legal-updates/iso-iec-42005-2025-a-new-blueprint-for-legal-and-commercial-leaders-navigating-ai-risk-and-governance
- EVS, ISO/IEC 42006:2025: https://www.evs.ee/en/iso-iec-42006-2025
- NSAI Standards, EN ISO/IEC 42001:2026: https://shop.standards.ie/en-ie/standards/en-iso-iec-42001-2026-1497138_saig_cen_cen_3929071/
- EVS, EVS-EN ISO/IEC 42001:2026: https://www.evs.ee/en/evs-en-iso-iec-42001-2026
- CEN-CENELEC, EN 18286 in the spotlight: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-30-ai-quality-management/
- BSI, EN 18286:2026 harmonized: https://www.bsigroup.com/en-GB/insights-and-media/media-centre/press-releases/2026/october/en-18286-2026-harmonized-a-significant-milestone-for-ai-act-compliance/
- Nemko, EN 18286 cited as harmonized QMS standard: https://digital.nemko.com/news/en-18286-eu-ai-act-cites-new-harmonized-qms-standard
- Intertek, EN 18286 and existing management systems: https://www.intertek.com/blog/2026/10-01-en-18286-first-eu-ai-act-standards-puzzle-piece-is-on-the-table/
- Cloud Security Alliance, EN 18286 and the limits of AI Act presumption of conformity: https://labs.cloudsecurityalliance.org/research/csa-research-note-en18286-harmonised-standard-presumption-20/
- AFNOR, ISO/IEC 27090:2026: https://www.boutique.afnor.org/en-gb/standard/iso-iec-270902026/cybersecurity-artificial-intelligence-ai-addressing-security-threats-and-co/xs147261/606717
- Nemko, ISO/IEC 27090 published: https://digital.nemko.com/news/isoiec-27090-published-as-new-ai-cybersecurity-standard
