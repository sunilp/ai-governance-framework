# Roles and Responsibilities — RACI Matrix

## Purpose

Clear accountability is the foundation of effective AI governance. This document defines who is Responsible, Accountable, Consulted, and Informed for each governance activity.

## Role Definitions

These are the owner labels used in the [control register](../governance-operations/control-register.md) and the [governance workflow](../governance-operations/governance-workflow.md). In the register, "Owner" is the role that produces and maintains the evidence. It is not always the Accountable role in the RACI below: for example, the Product owner owns the deployment approval record (DA-002), but the tier approver is accountable for the decision.

| Role | Definition | Line of defence |
|------|------------|-----------------|
| **Business owner** | Senior business stakeholder who owns the use case and its outcomes and accepts the residual risk. Exactly one per system. Co-signs T3 deployments. | First |
| **Business Unit Head** | Head of the business unit that uses the system. Co-signs T2 deployments. | First |
| **Product owner** | Owns delivery of the system before production: prepares the risk assessment and impact assessment (RA-001, RA-003), assembles the evidence pack and runs the sign-off chain (DA-001, DA-002), and sets up human oversight (PM-003). | First |
| **System owner** | Owns the system in production: scheduled reviews (RV-001), red-team finding closure before release (SR-002), remediation tracking (IR-005) and deprecation impact assessments (DR-001). | First |
| **Technical owner** | Engineer responsible for architecture, data residency, guardrails, adversarial defences, rollback and decommissioning (AR-001, AR-003, DE-004, SR-003, DA-004, DR-004). Documents the architecture for T3/T4 systems. | First |
| **AI lead** | Technical lead for model and prompt development and evaluation: model selection document, model card, prompt version control and review, evaluation evidence, revalidation (AR-004, DE-001 to DE-003, DE-005, EV controls, RV-002, RV-003). The Data Science Lead fills this role for traditional ML. | First |
| **AI Operations** | Runs AI systems in production: monitoring, alerting, production evaluation, cost monitoring, on-call and incident playbooks (DA-003, PM-001, PM-002, PM-004, PM-005, IR-001, IR-002). Covers MLOps and LLMOps. | First |
| **Team lead** | Leads the delivery team. Approves T3/T4 risk assessments, model selection from the approved vendor list and deployments, and T4 exceptions. | First |
| **Head of AI** | Senior technology leader for AI. Approves T2 deployments (with the Business Unit Head), T2 model selection, T2 design reviews (or a delegate) and T3 exceptions. | First |
| **Architecture review board** | Cross-functional technical forum that signs off T1 architecture (AR-002). | First |
| **Security** | Security engineering function. Runs security review and red-teaming and verifies supply chain provenance (SR-001, SR-004). | First |
| **CISO** | Senior security executive. Co-signs T1 deployments and T1 model selection; consulted on the security terms of open-source and model licences. | First (some organisations place this role in the second line) |
| **Responsible AI lead** | Designs and owns bias evaluation and fairness standards (EV-005). See [roles-genai.md](roles-genai.md#ai-ethics-and-responsible-ai-lead). | First or second, depending on reporting line |
| **AI Risk (second line)** | Independent AI risk function. Approves T2 risk assessments, reviews auto-T1 override decisions (RA-002), runs third-party model risk assessments (AR-005) and challenges tiering. The head of AI Risk approves T2 exceptions. May perform T2 independent validation. | Second |
| **Model Risk Management (MRM)** | Second-line function that performs independent validation: full validation for T1, reduced-scope validation for T2 (or another second-line reviewer does it). | Second |
| **DPO** | Data Protection Officer. Oversees DPIA screening and DPIAs (RA-005) and co-signs T1 deployments that process personal data. | Second |
| **Compliance** | Identifies applicable regulation, maps controls to it, assesses regulatory change (RV-004) and decides on regulatory notification with Legal. | Second |
| **Legal** | Approves open-source and model licences (AI Risk consulted; CISO consulted on security terms) and reviews regulatory notifications. | Second |
| **AI Risk Committee** | Senior forum chaired by the CRO. Approves T1 risk assessments, model selection, deployments and exceptions. Meets monthly, with a quarterly full-portfolio meeting ([review-cadence.md](review-cadence.md)). | Second (oversight forum) |
| **Incident commander** | Named for each incident. Leads the response, files the incident report (IR-003) and runs the post-mortem (IR-004). | First |
| **Internal Audit** | Independent assurance over the governance framework. | Third |

## Approvals by Tier

Each decision has exactly one Accountable approver per tier. Where more than one role signs, the first named is Accountable and the others co-sign. The process and evidence for each decision are in the [governance workflow](../governance-operations/governance-workflow.md).

| Decision | T1 | T2 | T3 | T4 |
|----------|----|----|----|----|
| Risk assessment (prepared by the Product owner) | AI Risk Committee | AI Risk (second line) | Team lead | Team lead (self-assessment acknowledged) |
| Architecture | Architecture review board | Head of AI or delegate (recorded team-level design review) | Documented by the technical owner | Documented by the technical owner |
| Independent validation | MRM (full scope) | MRM or another second-line reviewer outside the development team (reduced scope) | Peer review | Self-test |
| Model selection | AI Risk Committee; CISO co-signs | Head of AI | Team lead (approved vendor list) | Team lead (approved vendor list) |
| Deployment | AI Risk Committee; CISO co-signs, and the DPO if personal data is processed | Head of AI; Business Unit Head co-signs | Team lead; business owner co-signs | Team lead |
| Exception | AI Risk Committee | Head of AI Risk | Head of AI | Team lead |

Open-source and model licences are approved by Legal at every tier. Exceptions follow [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance).

## RACI Matrix

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed. Each row has exactly one A for any given tier. The "Tier approver" column is the approver named in [Approvals by Tier](#approvals-by-tier). The Product / system owner column covers the Product owner before production and the System owner after. For T2 validation, the MRM column also covers another second-line reviewer outside the development team.

### Model Development Phase

| Activity | Business owner | Product / system owner | AI lead | AI Operations | Security | MRM | AI Risk | Compliance | Tier approver |
|----------|---------------|-----------------------|---------|---------------|----------|-----|---------|------------|---------------|
| Define business requirements | **A** | R | C | I | I | I | I | C | I |
| Risk assessment and tiering | C | R | C | I | C | I | C | C | **A** |
| Data sourcing and quality | I | I | **R/A** | I | I | C | I | C | I |
| Model development | I | I | **R/A** | I | I | I | I | I | I |
| Bias and fairness testing | C | I | R (T3/T4: **R/A**) | I | I | **A** (T1/T2) | C | C | I |
| Model documentation | I | I | **R/A** | I | I | C | I | I | I |

### Model Validation Phase

| Activity | Business owner | Product / system owner | AI lead | AI Operations | Security | MRM | AI Risk | Compliance | Tier approver |
|----------|---------------|-----------------------|---------|---------------|----------|-----|---------|------------|---------------|
| Independent validation (T1/T2) | I | I | C | I | I | **R/A** | C | I | I |
| Peer review (T3) or self-test (T4) | I | I | **R/A** | I | I | I | I | I | I |
| Challenger model development | I | I | R | I | I | **A** | I | I | I |
| Validation report review | C | I | C | I | I | **R/A** | C | C | I |

### Deployment Phase

| Activity | Business owner | Product / system owner | AI lead | AI Operations | Security | MRM | AI Risk | Compliance | Tier approver |
|----------|---------------|-----------------------|---------|---------------|----------|-----|---------|------------|---------------|
| Security review | I | I | C | C | **R/A** | I | C | I | I |
| Deployment approval | C | R | C | C | C | C | C | C | **A** |
| Deployment execution | I | I | C | **R/A** | I | I | I | I | I |
| Post-deployment verification | C | I | R | **R/A** | I | C | I | I | I |

### Production Phase

| Activity | Business owner | Product / system owner | AI lead | AI Operations | Security | MRM | AI Risk | Compliance | Tier approver |
|----------|---------------|-----------------------|---------|---------------|----------|-----|---------|------------|---------------|
| Ongoing monitoring and metrics review | I | C | C | **R/A** | I | I | I | I | I |
| Formal governance review (RV-001) | C | **R/A** | R | C | I | C | C | C | I |
| Incident response | C | C | R | **R/A** | R (security incidents) | C | C | C | I |
| Retraining decision | C | C | R (T3/T4: **R/A**) | C | I | **A** (T1/T2) | I | I | I |
| Model retirement | **A** | R | R | R | I | C | C | C | I |

Incident response: AI Operations assigns the incident commander, who leads the response. Severity, follow-ups and notifications (including the AI Risk Committee chair within 1 hour for S1) are set in [escalation-paths.md](escalation-paths.md#severity-classification). Formal governance review cadence is in [review-cadence.md](review-cadence.md#cadence-by-tier); T1 reviews are presented to the AI Risk Committee. Model retirement: the Business owner decides to retire the use case; decommissioning then follows [Stage 10 of the governance workflow](../governance-operations/governance-workflow.md#stage-10-deprecation--retirement).

## Accountability Principles

1. **Single accountability:** Every AI system has exactly one Business owner, one Product owner (System owner in production) and one AI lead, recorded in the AI system inventory. Every activity has exactly one Accountable role per tier.
2. **Separation of duties:** The team that builds a T1/T2 model never validates it.
3. **Escalation obligation:** Any role holder who identifies a material risk is obligated to escalate, regardless of tier.
4. **Documentation duty:** Decisions must be documented. Verbal approvals are not sufficient for T1/T2 systems.
5. **Regulatory representation:** Compliance must be consulted on all T1/T2 systems and any system processing customer data.

## Onboarding New AI Systems

When a new AI system is proposed:

1. **Product owner** submits the intake form, with the Business owner named
2. **AI lead** is assigned and helps the Product owner prepare the risk assessment
3. **Risk assessment** is approved per tier: AI Risk Committee (T1), AI Risk (T2), team lead (T3/T4)
4. **Compliance** confirms regulatory requirements
5. All roles are documented in the AI system inventory
