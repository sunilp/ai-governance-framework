# GenAI Use Case Assessment Template

## Instructions

Complete this assessment before initiating development of any GenAI use case. The product owner prepares it and submits it to the approver for the resulting risk tier (see section 8). Start with section 0: if the use case fails it, stop before spending time on the rest.

---

## 0. Should This Use GenAI at All?

Answer these before scoring anything. Each question maps to a position in [when to say no](../framework/governance-operations/when-to-say-no.md). A "Yes" means stop or redesign, and the approver reviews these answers with the rest of the assessment.

| # | Question | Yes / No | If yes |
|---|----------|----------|--------|
| 0.1 | Does the use case fall under EU AI Act Art. 5 or the internal prohibited-use policy? Run the [Step 0 prohibited-use screen](../framework/risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen) | | Rejected. Not tiered, cannot be excepted ([position 6](../framework/governance-operations/when-to-say-no.md#6-prohibited-practices-are-rejected-at-step-0)) |
| 0.2 | Would the model generate a fee, rate, balance, limit, eligibility outcome or regulatory figure, instead of taking it from a system of record? | | Redesign ([position 1](../framework/governance-operations/when-to-say-no.md#1-figures-with-legal-or-contractual-effect-come-from-a-system-of-record)) |
| 0.3 | Would GenAI make an adverse regulated decision without a qualified human deciding? | | Redesign ([position 2](../framework/governance-operations/when-to-say-no.md#2-genai-never-makes-an-adverse-regulated-decision-on-its-own)) |
| 0.4 | Would an agent take a write action that cannot be reversed, or cannot be rate-limited and capped, without human confirmation? | | Redesign ([position 3](../framework/governance-operations/when-to-say-no.md#3-no-autonomous-write-that-cannot-be-undone-or-capped)) |
| 0.5 | Would customer personal data, MNPI or regulated data go to an external model API without evidenced residency, zero retention and a signed DPA? | | Redesign ([position 4](../framework/governance-operations/when-to-say-no.md#4-no-external-model-api-without-evidenced-residency-and-zero-retention)) |
| 0.6 | Is there no agreed definition of a correct answer, or no way to build evaluation suites of the tier size? | | Not ready ([position 5](../framework/governance-operations/when-to-say-no.md#5-no-launch-when-the-evaluation-cannot-show-the-threshold-is-met)) |
| 0.7 | Would search, a rules engine or a conventional model meet the need? | | Use the simpler method ([position 7](../framework/governance-operations/when-to-say-no.md#7-no-genai-where-a-simpler-method-meets-the-need)) |
| 0.8 | Would a business-critical process depend on one vendor model with no validated fallback? | | Redesign ([position 8](../framework/governance-operations/when-to-say-no.md#8-no-business-critical-process-on-a-model-you-cannot-replace)) |

| Field | Response |
|-------|----------|
| Step 0 prohibited-use screen result (recorded under RA-001) | Pass / Rejected |
| Positions triggered and redesign made | |
| If proceeding despite a "Yes" (not possible for 0.1): reasoning, and the approver's recorded decision | |

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

Score each dimension: Critical (4), High (3), Medium (2), Low (1). Refer to [genai-risk-matrix.md](../framework/risk-classification/genai-risk-matrix.md#risk-tier-determination-for-genai) for definitions.

The highest-scoring dimension sets the tier: any Critical gives T1; otherwise any High gives T2; otherwise any Medium gives T3; all Low gives T4. The aggregate score is recorded for context only and does not set the tier.

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination severity | | |
| Data exposure risk | | |
| Prompt injection susceptibility | | |
| Output controllability | | |
| Third-party model dependency | | |
| **Highest dimension score** | | |
| **Aggregate score** (informational only) | | |
| **Tier from scoring** | | |

### Tier Override Check

Check every item in the [canonical override list](../framework/risk-classification/genai-risk-matrix.md#tier-override-rules). Overrides can raise the tier, never lower it.

**Automatic T1:**

- [ ] 1. Makes or directly influences regulated decisions (credit, insurance underwriting or pricing, AML/sanctions, employment)
- [ ] 2. Generates customer-facing content delivered without per-output human review
- [ ] 3. Processes customer personal data through an external LLM API without all four safeguards (zero vendor data retention, a regional endpoint that meets data residency requirements, a signed DPA, PII redaction or minimisation before the call)
- [ ] 4. Agentic behaviour with write access to production systems or data stores, or with authority to move money, communicate with customers, or change identity and access
- [ ] 5. Biometric identification or categorisation; synthetic media that can depict real people (deepfake-capable); voice cloning; medical imagery

**Minimum T2:**

- [ ] 6. Any agentic system, including read-only tool use, and any multi-agent system
- [ ] 7. Synthetic media generation not covered by item 5
- [ ] 8. Customer personal data through an external LLM API with all four safeguards in place
- [ ] 9. Personal data in visual content

If any of items 1 to 5 is checked, the use case is **T1**. If any of items 6 to 9 is checked, it is **at least T2**.

| Field | Response |
|-------|----------|
| Override items applied | |
| **Resulting risk tier** | |

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
| What HITL pattern applies? | Pattern 1 human-in-the-loop / Pattern 2 human-on-the-loop / Pattern 3 human-over-the-loop / Pattern 4 human-out-of-the-loop |
| T1 customer-facing using Pattern 3: are all five safeguards in place and evidenced? (see [pattern selection matrix](../framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix)) | Yes / No / N/A |
| Who reviews AI outputs? | |
| What is the review process? | |
| Can the user override or reject AI output? | Yes / No |

### Regulatory Applicability

| Regulation | Applicable? | Notes |
|-----------|------------|-------|
| EU AI Act | Yes / No | |
| GDPR | Yes / No | |
| SR 26-2 (US model risk guidance, replaced SR 11-7 in April 2026; covers traditional and non-generative AI model components only, GenAI and agentic AI are out of scope) | Yes / No | |
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

| Tier | Risk assessment approver |
|------|-------------------|
| T1 | AI Risk Committee |
| T2 | AI Risk (second line) |
| T3 | Team lead |
| T4 | Team lead (acknowledges the self-assessment) |

Deployment approval is a separate step: see [Stage 7 of the governance workflow](../framework/governance-operations/governance-workflow.md#stage-7-deployment-approval).

---

## 9. Next Steps

After approval, proceed to:

1. [ ] Model selection evaluation (if not finalized)
2. [ ] Prompt development per [prompt-engineering-standards.md](../framework/llm-lifecycle/prompt-engineering-standards.md)
3. [ ] RAG pipeline development (if applicable) per [rag-governance.md](../framework/llm-lifecycle/rag-governance.md)
4. [ ] Evaluation suite development
5. [ ] Security review scheduling
6. [ ] Deployment gate planning per [deployment-gates.md](../framework/llm-lifecycle/deployment-gates.md)
