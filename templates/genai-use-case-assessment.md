# GenAI Use Case Assessment Template

## Instructions

Complete this assessment before initiating development of any GenAI use case. Submit to the appropriate approver based on the resulting risk tier.

---

## 1. Use Case Overview

| Field | Response |
|-------|----------|
| Use case name | |
| Requesting business unit | |
| Business sponsor | |
| Technical lead | |
| Date submitted | |
| Target go-live date | |

### Business Justification

**What problem does this solve?**

> [Describe the business problem in 2-3 sentences]

**What is the current process?**

> [How is this done today, without AI?]

**What is the expected business value?**

> [Quantify where possible: time savings, cost reduction, quality improvement, revenue impact]

**Who are the end users?**

> [Internal employees, customers, partners, regulators?]

---

## 2. Technical Design

### AI System Type

- [ ] Conversational AI (chatbot, Q&A)
- [ ] Content generation (drafting, summarization)
- [ ] Classification / extraction
- [ ] Code generation / assistance
- [ ] Decision support
- [ ] Agentic AI (autonomous task execution)
- [ ] Other: _______________

### Architecture

**Foundation model:**

> [Which model? OpenAI GPT-4, Anthropic Claude, Google Gemini, open-source, etc.]

**Hosting:**

- [ ] Vendor API
- [ ] Self-hosted
- [ ] VPC / private endpoint
- [ ] Hybrid

**RAG (Retrieval-Augmented Generation):**

- [ ] Yes → complete RAG section below
- [ ] No

**If RAG:**

| Field | Response |
|-------|----------|
| Document sources | |
| Vector store | |
| Chunking strategy | |
| Number of documents | |
| Update frequency | |
| Access controls on documents | |

**Fine-tuning:**

- [ ] Yes → complete fine-tuning justification
- [ ] No

---

## 3. Risk Assessment

### GenAI Risk Dimensions

Score each dimension: Critical (4), High (3), Medium (2), Low (1). Refer to [genai-risk-matrix.md](../framework/risk-classification/genai-risk-matrix.md) for definitions.

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination severity | | |
| Data exposure risk | | |
| Prompt injection susceptibility | | |
| Output controllability | | |
| Third-party model dependency | | |
| **Aggregate score** | | |
| **Resulting risk tier** | | |

### Tier Override Check

Does this use case meet any automatic T1 criteria?

- [ ] Processes customer PII through external LLM API
- [ ] Generates customer-facing content without human review
- [ ] Makes or influences regulated decisions
- [ ] Involves agentic behavior with production system access

If any box is checked → **automatic T1 classification**.

---

## 4. Data Assessment

| Question | Response |
|----------|----------|
| What data enters the LLM prompt? | |
| Data classification of prompt content | Public / Internal / Confidential / PII / Regulated |
| Does the system process customer PII? | Yes / No |
| If yes, is PII redacted before LLM processing? | Yes / No / N/A |
| Where is data processed geographically? | |
| Does data cross jurisdictional boundaries? | Yes / No |
| Data retention requirements | |
| Has the data owner approved this use? | Yes / No |

---

## 5. Safety and Compliance

### Hallucination

| Question | Response |
|----------|----------|
| What is the acceptable hallucination rate? | |
| What happens if the system hallucinates? | |
| How will hallucination be measured? | |
| What mitigation is in place? | |

### Human Oversight

| Question | Response |
|----------|----------|
| What HITL pattern applies? | Full review / Sampling / Exception / Autonomous |
| Who reviews AI outputs? | |
| What is the review process? | |
| Can the user override or reject AI output? | Yes / No |

### Regulatory Applicability

| Regulation | Applicable? | Notes |
|-----------|------------|-------|
| EU AI Act | Yes / No | |
| GDPR | Yes / No | |
| SR 11-7 | Yes / No | |
| Consumer Duty (FCA) | Yes / No | |
| BCBS 239 | Yes / No | |
| DORA | Yes / No | |
| Other: _________ | Yes / No | |

### Transparency

| Question | Response |
|----------|----------|
| How will users know they're interacting with AI? | |
| How will AI-generated content be labeled? | |
| What limitations will be disclosed to users? | |

---

## 6. Vendor Assessment (If Using External Model)

| Question | Response |
|----------|----------|
| Vendor name | |
| Is a DPA in place? | Yes / No / In progress |
| Does the vendor retain your data? | Yes / No / Contractually excluded |
| Does the vendor use your data for training? | Yes / No / Contractually excluded |
| Vendor security certifications | |
| Fallback model identified? | Yes / No (required for T1/T2) |
| Exit strategy documented? | Yes / No (required for T1/T2) |

---

## 7. Operational Readiness

| Question | Response |
|----------|----------|
| Monitoring plan defined? | Yes / No |
| Alerting configured? | Yes / No |
| Incident response playbook? | Yes / No |
| On-call team identified? | Yes / No |
| Rollback procedure documented? | Yes / No |
| Cost budget approved? | Yes / No |
| Estimated monthly cost | |

---

## 8. Assessment Decision

| Field | Response |
|-------|----------|
| Risk tier | T1 / T2 / T3 / T4 |
| Decision | Approved / Approved with conditions / Rejected / Needs more information |
| Conditions (if any) | |
| Approver name | |
| Approver role | |
| Approval date | |

### Required Approvals by Tier

| Tier | Required Approvals |
|------|-------------------|
| T1 | AI Risk Committee + CISO + Business Unit Head |
| T2 | Head of AI + Security Review |
| T3 | Team Lead + Business Owner |
| T4 | Team Lead |

---

## 9. Next Steps

After approval, proceed to:

1. [ ] Model selection evaluation (if not finalized)
2. [ ] Prompt development per [prompt-engineering-standards.md](../framework/llm-lifecycle/prompt-engineering-standards.md)
3. [ ] RAG pipeline development (if applicable) per [rag-governance.md](../framework/llm-lifecycle/rag-governance.md)
4. [ ] Evaluation suite development
5. [ ] Security review scheduling
6. [ ] Deployment gate planning per [deployment-gates.md](../framework/llm-lifecycle/deployment-gates.md)
