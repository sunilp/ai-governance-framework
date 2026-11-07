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
| 4.3 Determining the scope of the AI management system | Tier classification sets governance scope per system. Annex A of the AI policy template holds the AIMS scope statement, which the organization completes and the board approves with the policy | RA-001, GV-001 | [Risk Matrix](../risk-classification/risk-matrix.md), [AI Policy Template, Annex A](../../templates/ai-policy.md#annex-a-ai-management-system-items-isoiec-42001) |
| 4.4 AI management system | The governance workflow, control register and supporting standards supply AIMS processes; the organization must establish and maintain the AIMS itself | All register controls | [Governance Workflow](../governance-operations/governance-workflow.md), [Control Register](../governance-operations/control-register.md) |

### Clause 5: Leadership

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 5.1 Leadership and commitment | Board-level AI risk reporting; board-approved AI risk appetite statement and AI policy; AI Risk Committee membership and agenda, and a charter setting its authority, quorum, decision rights, delegation and escalation to the board | GV-001, GV-005, RA-004, DA-002 (AI Risk Committee approves T1) | [Board Reporting](../operating-model/board-reporting.md), [Review Cadence](../operating-model/review-cadence.md), [AI Risk Committee Charter](../../templates/ai-risk-committee-charter.md) |
| 5.2 AI policy | Board-approved AI policy, reviewed annually. The template covers fit with the organization's purpose, a framework for AI objectives, commitments to meet applicable requirements and to continual improvement, and communication to staff | GV-001 | [AI Policy Template](../../templates/ai-policy.md), [Responsible AI Checklist](responsible-ai-checklist.md), [Transparency Standards](../responsible-ai/transparency-standards.md) |
| 5.3 Roles, responsibilities and authorities | RACI matrices for traditional ML and GenAI; named control owners; tiered approvers; committee decision rights in the charter | RA-004, DA-002, GV-005 | [Roles & Responsibilities](../operating-model/roles-responsibilities.md), [GenAI Roles](../operating-model/roles-genai.md) |

### Clause 6: Planning

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 6.1.1 General (actions to address risks and opportunities) | Tiered governance; risk appetite; GenAI, multimodal and agentic risk matrices | RA-001 | [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md), [Board Reporting](../operating-model/board-reporting.md) |
| 6.1.2 AI risk assessment | Risk assessment template with dimension scoring and the override list | RA-001, RA-002, RA-004 | [Assessment Template](../risk-classification/assessment-template.yaml) |
| 6.1.3 AI risk treatment (including the Statement of Applicability) | Register controls by tier; exceptions with risk acceptance, recorded in the exception register and reviewed monthly. No Statement of Applicability template (the AI policy template only references one) | Stage 3 to 8 controls, GV-004. Statement of Applicability: No control yet (gap) | [Control Register](../governance-operations/control-register.md), [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance), [Exception Register](../../templates/exception-register.md) |
| 6.1.4 AI system impact assessment | Impact assessment template; DPIA | RA-003, RA-005 | [Impact Assessment](../../templates/impact-assessment-template.md) |
| 6.2 AI objectives and planning to achieve them | Governance health KPIs and targets; Annex A of the AI policy template sets measurable AI objectives with owners, target dates, resources and measures, approved with the policy | GV-001 | [Governance Metrics](../operating-model/governance-metrics.md), [AI Policy Template, Annex A](../../templates/ai-policy.md#annex-a-ai-management-system-items-isoiec-42001) |
| 6.3 Planning of changes | Annual framework review (Head of MRM, Q1); regulatory change impact assessment; annual policy review. Annex A of the AI policy template records how changes to the AIMS are proposed, assessed and approved | RV-004, GV-001 | [Review Cadence](../operating-model/review-cadence.md#annual-activities), [Regulatory Change Monitoring](regulatory-change-monitoring.md), [AI Policy Template, Annex A](../../templates/ai-policy.md#annex-a-ai-management-system-items-isoiec-42001) |

### Clause 7: Support

| ISO 42001 Requirement | Framework Implementation | Controls | Reference |
|----------------------|--------------------------|----------|-----------|
| 7.1 Resources | Cost governance; resource documentation in the AI-BOM and architecture document | AR-001, SR-004, PM-005 | [Cost Governance](../operating-model/cost-governance.md), [Supply Chain Security](../ai-security/supply-chain-security.md#ai-bill-of-materials-ai-bom) |
| 7.2 Competence | Role-based AI literacy measures for the board, executives, all staff, AI builders, human oversight reviewers and the second line; completion records by audience; knowledge checks for T1 and T2 system training; reviewer training for human oversight | GV-002 | [AI Literacy](../operating-model/ai-literacy.md), [Governance Metrics](../operating-model/governance-metrics.md), [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md) |
| 7.3 Awareness | AI policy communicated to staff; all-staff literacy module with annual attestation to the acceptable use standard; escalation paths and review cadence make governance duties visible | GV-001, GV-002, GV-003 | [AI Literacy](../operating-model/ai-literacy.md), [Acceptable Use](../operating-model/acceptable-use.md), [Escalation Paths](../operating-model/escalation-paths.md) |
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
| A.2 Policies related to AI | Board-approved AI policy (see clause 5.2), with the acceptable use standard for staff use of AI tools and the framework standards beneath it | GV-001, GV-003 | [AI Policy Template](../../templates/ai-policy.md), [Acceptable Use](../operating-model/acceptable-use.md), [responsible-ai/](../responsible-ai/), [risk-classification/](../risk-classification/) |
| A.3 Internal organization | Roles and RACI; tiered approvers; AI Risk Committee charter. No process for staff to report concerns about AI systems (the AI policy template only has a placeholder for one) | RA-004, DA-002, GV-005. Reporting of concerns: No control yet (gap) | [Roles](../operating-model/roles-responsibilities.md), [Escalation Paths](../operating-model/escalation-paths.md) |
| A.4 Resources for AI systems | Resource documentation: AI inventory (models, vendors, hosting and data per system), AI-BOM (models, data, tooling), architecture document, cost governance, roles | GV-006, AR-001, SR-004, PM-005 | [AI Inventory](../governance-operations/ai-inventory.md), [Supply Chain Security](../ai-security/supply-chain-security.md#ai-bill-of-materials-ai-bom), [Cost Governance](../operating-model/cost-governance.md) |
| A.5 Assessing impacts of AI systems | Impact assessment; DPIA; bias evaluation | RA-003, RA-005, EV-005 | [Impact Assessment](../../templates/impact-assessment-template.md) |
| A.6 AI system life cycle | Lifecycle standards from design to retirement: development, evaluation, deployment gates, monitoring, technical documentation, deprecation | DE-001 to DE-005, EV-001 to EV-009, DA-001 to DA-004, PM-001 to PM-005, DR-001 to DR-004 | [model-lifecycle/](../model-lifecycle/), [llm-lifecycle/](../llm-lifecycle/) |
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
| AI policy and leadership | AI policy template (GV-001); AI Risk Committee charter template (GV-005) |
| AIMS scope, objectives and change planning | Annex A of the AI policy template (GV-001) |
| Competence and awareness | AI literacy standard (GV-002); acceptable use standard (GV-003) |
| AI system inventory | Inventory standard, entry template and schema (GV-006) |

### Gaps a Certification Audit Will Find

The AI policy (with its AIMS annex), the committee charter and the literacy programme now have templates and controls (GV-001, GV-002, GV-005); the organization still has to complete and approve them. These remain missing from the framework. Each is a document or process the organization must write and approve.

| ISO 42001 Requirement | What Is Missing |
|---------------|--------------------------------------|
| 6.1.3 Statement of Applicability | Statement of Applicability with justification for each included or excluded Annex A control |
| A.3 Internal organization | Process for staff to report concerns about AI systems |
| A.8 External reporting | Channel for interested parties to report adverse impacts |

### What Organizations Must Produce From Operating the AIMS

| ISO 42001 Area | Organization-Specific Evidence Needed |
|---------------|--------------------------------------|
| Risk treatment plan | Risk treatment decisions for each AI system |
| Training records | Completion and competence records by audience ([AI literacy](../operating-model/ai-literacy.md#evidence-gv-002)) |
| Internal audit reports | Audit reports for AI systems and the AIMS |
| Management review minutes | AI Risk Committee minutes under its charter |
| Incident records | Incident reports |
| Corrective action records | Evidence of remediation completion |
| AI system inventory | Inventory populated to the [inventory standard](../governance-operations/ai-inventory.md), with quarterly reconciliation records |

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
