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
| Required skills | Model risk management; understanding of LLM systems; regulatory knowledge (EU AI Act, SR 11-7); quantitative analysis |
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
| Incident response | GenAI-specific incident taxonomy and playbooks |

### Compliance Officer

| Existing Responsibility | GenAI Extension |
|------------------------|-----------------|
| Regulatory compliance | EU AI Act mapping, AI system inventory, transparency obligations |
| Risk assessment | GenAI risk classification, HITL requirement determination |
| Audit | Prompt audit trail review, AI system examination readiness |

---

## RACI for GenAI Governance Activities

| Activity | Business Owner | AI Engineering | Prompt Engineer | AI Risk | LLMOps | Compliance | Security |
|----------|---------------|---------------|----------------|---------|--------|-----------|----------|
| Use case identification | A | C | C | C | - | C | - |
| Risk assessment | I | C | C | A | C | R | C |
| Model selection | C | A | C | R | C | I | R |
| Prompt development | C | C | A | I | - | I | C |
| Evaluation & testing | I | R | A | R | C | I | C |
| Security review | I | C | C | C | C | I | A |
| Deployment approval | R | C | C | A | R | R | R |
| Production monitoring | I | C | C | R | A | I | C |
| Incident response | I | R | C | R | A | I | R |
| Periodic review | R | C | C | A | C | R | C |

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

---

## Organizational Scaling

| Organization Size | Approach |
|------------------|---------|
| < 5 GenAI use cases | Existing roles absorb GenAI responsibilities; 1–2 dedicated GenAI engineers |
| 5–20 GenAI use cases | Dedicated prompt engineering and LLMOps roles; AI risk analyst |
| 20+ GenAI use cases | Full GenAI team within the AI CoE or distributed across domain teams |
| Enterprise-wide GenAI adoption | All roles formalized; embedded in domain teams with central governance |
