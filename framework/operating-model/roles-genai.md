# GenAI-Specific Roles and Responsibilities

## Overview

GenAI introduces roles that did not exist in traditional ML operating models. These roles may be net-new hires, extensions of existing roles, or temporary responsibilities assigned to existing team members as the organization scales.

This document defines GenAI-specific roles, their responsibilities, required skills, and how they integrate with the existing organizational structure.

---

## New Roles for GenAI

### Prompt Engineer

**Purpose:** Design, test, version, and maintain prompts that drive LLM system behavior.

| Aspect | Description |
|--------|-------------|
| Core responsibilities | Prompt design and optimization; evaluation suite development; prompt versioning and lifecycle management; adversarial testing |
| Required skills | Strong writing and analytical skills; understanding of LLM behavior; evaluation methodology; domain knowledge for the target use case |
| Reports to | AI/ML Engineering Lead or Product Manager |
| Interacts with | Data scientists, domain experts, QA, compliance |
| Career path | Senior Prompt Engineer → AI Product Lead or AI Engineering Lead |

**Note:** In many organizations, prompt engineering is a skill rather than a dedicated role. The decision to create a dedicated role depends on the volume and complexity of GenAI use cases.

### AI Risk Analyst (GenAI-Focused)

**Purpose:** Assess, monitor, and report on risks specific to GenAI systems.

| Aspect | Description |
|--------|-------------|
| Core responsibilities | GenAI risk assessments; hallucination and bias monitoring; incident investigation; regulatory compliance mapping; vendor model risk assessment |
| Required skills | Model risk management; understanding of LLM systems; regulatory knowledge (EU AI Act; US model risk guidance SR 26-2, which replaced SR 11-7 in April 2026 and leaves GenAI and agentic AI out of scope); quantitative analysis |
| Reports to | Head of AI Risk or Chief Risk Officer |
| Interacts with | AI engineering, compliance, legal, business stakeholders |
| Career path | Senior AI Risk Analyst → Head of AI Risk → CRO (AI) |

### LLM Operations Engineer (LLMOps)

**Purpose:** Operate and maintain LLM systems in production.

| Aspect | Description |
|--------|-------------|
| Core responsibilities | Model serving and scaling; monitoring and alerting; cost optimization; vendor API management; guardrail infrastructure; incident response |
| Required skills | Infrastructure engineering; monitoring and observability; API management; understanding of LLM inference characteristics |
| Reports to | AI Platform Lead or Head of MLOps |
| Interacts with | AI engineering, security, SRE, vendor management |
| Career path | Senior LLMOps → AI Platform Lead |

### AI Ethics and Responsible AI Lead

**Purpose:** Ensure GenAI systems meet ethical standards and responsible AI principles.

| Aspect | Description |
|--------|-------------|
| Core responsibilities | Bias evaluation design; fairness monitoring; transparency standards; human oversight design; stakeholder engagement on AI ethics |
| Required skills | AI ethics; bias detection methodologies; communication; stakeholder management; regulatory awareness |
| Reports to | Head of AI or Chief Ethics Officer |
| Interacts with | AI engineering, legal, compliance, business, customers |
| Career path | Senior Responsible AI Lead → Head of Responsible AI |

---

## Extended Responsibilities for Existing Roles

### Data Scientist / ML Engineer

| Existing Responsibility | GenAI Extension |
|------------------------|-----------------|
| Model development and training | LLM evaluation, fine-tuning, RAG pipeline development |
| Feature engineering | Context engineering, chunking strategy, retrieval optimization |
| Model evaluation | Hallucination testing, faithfulness evaluation, adversarial testing |
| A/B testing | Prompt A/B testing, model comparison |

### Solution Architect

| Existing Responsibility | GenAI Extension |
|------------------------|-----------------|
| System design | LLM integration architecture, guardrail design, RAG architecture |
| Vendor evaluation | Foundation model evaluation, vendor risk assessment |
| Non-functional requirements | Latency budgets for LLM calls, token cost estimation, data residency design |

### Product Manager

| Existing Responsibility | GenAI Extension |
|------------------------|-----------------|
| Requirements definition | AI use case assessment, hallucination tolerance definition, HITL pattern selection |
| User experience | AI disclosure design, feedback mechanisms, managing user expectations |
| Success metrics | GenAI-specific metrics (output quality, hallucination rate, user satisfaction) |

### Security Engineer

| Existing Responsibility | GenAI Extension |
|------------------------|-----------------|
| Application security | Prompt injection defense, input/output sanitization |
| Data security | PII redaction in prompts, data residency compliance, audit trail security |
| Vendor security | LLM vendor security assessment, API security |
| Incident response | GenAI incident playbooks; severity per [escalation-paths.md](escalation-paths.md#severity-classification) |

### Compliance Officer

| Existing Responsibility | GenAI Extension |
|------------------------|-----------------|
| Regulatory compliance | EU AI Act mapping, AI system inventory, transparency obligations |
| Risk assessment | Advises the Product owner on GenAI risk classification and HITL requirements |
| Audit | Prompt audit trail review, AI system examination readiness |

---

## GenAI RACI Supplement

The [RACI matrix and approvals by tier](roles-responsibilities.md#approvals-by-tier) in roles-responsibilities.md apply to GenAI systems unchanged: one Accountable role per activity per tier, risk assessments prepared by the Product owner and approved per tier, and deployment approved by the tier approver. This supplement maps the GenAI roles above onto that RACI and adds GenAI-specific activities.

| GenAI role | RACI column in roles-responsibilities.md |
|-----------|------------------------------------------|
| Prompt Engineer | Works under the AI lead |
| AI Risk Analyst | AI Risk (second line) |
| LLM Operations Engineer | AI Operations |
| AI Ethics and Responsible AI Lead | Responsible AI lead (see [Role Definitions](roles-responsibilities.md#role-definitions)) |
| Security Engineer | Security |

### GenAI-Specific Activities

| Activity | Prompt Engineer | AI lead | AI Operations | Security | AI Risk | Responsible AI lead | Tier approver |
|----------|----------------|---------|---------------|----------|---------|---------------------|---------------|
| Prompt development and version control (DE-002) | R | **A** | I | C | I | I | I |
| Prompt review (DE-003; depth per tier in [prompt-engineering-standards.md](../llm-lifecycle/prompt-engineering-standards.md)) | R | **A** | I | C (T1: R, security review) | C (T1: signs off) | I | I |
| Model selection (AR-004) | C | R | C | C | C (vendor risk, AR-005) | I | **A** |
| Evaluation and testing (EV-001 to EV-007) | R | **A** | C | I | C | R (bias evaluation, EV-005) | I |
| Red-teaming and security review (SR-001 to SR-004) | C | R | C | **R/A** | C | I | I |
| Production evaluation and vendor behaviour canary (PM-004) | C | R | **R/A** | I | I | I | I |
| Incident response | C | R | **R/A** | R (security incidents) | C | C | I |

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed. The tier approver for model selection is the AI Risk Committee with the CISO co-signing (T1), the Head of AI (T2) or the team lead from the approved vendor list (T3/T4). Incident severity, follow-ups and notifications are set in [escalation-paths.md](escalation-paths.md#severity-classification).

---

## Organizational Scaling

| Organization Size | Approach |
|------------------|---------|
| < 5 GenAI use cases | Existing roles absorb GenAI responsibilities; 1–2 dedicated GenAI engineers |
| 5–20 GenAI use cases | Dedicated prompt engineering and LLMOps roles; AI risk analyst |
| 20+ GenAI use cases | Full GenAI team within the AI CoE or distributed across domain teams |
| Enterprise-wide GenAI adoption | All roles formalized; embedded in domain teams with central governance |
