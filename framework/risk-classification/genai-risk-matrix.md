# GenAI Risk Classification Matrix

## Overview

Generative AI introduces risk categories that traditional ML risk frameworks do not adequately cover. This matrix extends the existing four-tier risk classification (T1–T4) with GenAI-specific assessment dimensions.

Traditional ML risks center on model accuracy, data drift, and discriminatory outcomes. GenAI risks additionally include hallucination, prompt injection, data leakage through prompts, uncontrolled content generation, intellectual property exposure, and the opacity of foundation models that the organization did not train.

This matrix should be used alongside the existing [risk-matrix.md](risk-matrix.md) for any use case that involves large language models, generative image/video models, or AI agents.

---

## GenAI-Specific Risk Dimensions

### Dimension 1: Hallucination Severity

The degree to which factually incorrect outputs could cause harm.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Incorrect output directly causes financial, legal, or safety harm | Regulatory reporting, medical guidance, legal contract analysis |
| High | Incorrect output influences consequential decisions | Credit memo generation, investment research summaries |
| Medium | Incorrect output causes operational inefficiency but is caught | Internal document summarization, meeting minutes |
| Low | Incorrect output has minimal consequence | Content ideation, brainstorming assistance |

### Dimension 2: Data Exposure Risk

The sensitivity of data that flows through the LLM pipeline — prompts, context windows, RAG retrieval, fine-tuning datasets, and outputs.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | PII, material non-public information (MNPI), or regulated data in prompts/context | Customer data processing, deal room summarization |
| High | Confidential business data in prompts/context | Internal strategy documents, financial projections |
| Medium | Internal but non-sensitive data | Process documentation, general knowledge base |
| Low | Public or non-sensitive data only | Public FAQ generation, marketing content |

### Dimension 3: Prompt Injection Susceptibility

The exposure surface for adversarial prompt manipulation.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | User-facing with unrestricted input, connected to downstream actions | Customer chatbot with transaction capabilities |
| High | User-facing with unrestricted input, read-only | Customer Q&A, public-facing assistants |
| Medium | Internal users with controlled input templates | Employee productivity tools with structured prompts |
| Low | No user input; fully automated prompts | Batch summarization, scheduled report generation |

### Dimension 4: Output Controllability

The degree to which the organization can constrain, validate, and correct generated outputs before they reach end users or downstream systems.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Output directly consumed by external parties or systems with no review | Auto-response customer service, automated report filing |
| High | Output consumed after minimal review | Draft communications, generated disclosures |
| Medium | Output reviewed by qualified human before use | Research summaries reviewed by analyst |
| Low | Output is advisory only; human makes all decisions | Coding assistants, brainstorming tools |

### Dimension 5: Third-Party Model Dependency

The degree of reliance on foundation models controlled by external vendors.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Single-vendor API dependency for business-critical process | Core customer service on GPT-4 API only |
| High | Vendor API with limited fallback options | Primary model is vendor-hosted; fallback is degraded |
| Medium | Self-hosted model with vendor training data | Fine-tuned open model (Llama, Mistral) on own infrastructure |
| Low | Fully self-hosted, self-trained | Custom model trained on internal data |

---

## Risk Tier Determination for GenAI

Score each dimension as Critical (4), High (3), Medium (2), or Low (1). The highest single dimension score determines the floor. The aggregate determines the tier.

| Aggregate Score | Tier | Governance Intensity |
|----------------|------|---------------------|
| Any dimension = Critical, or aggregate ≥ 16 | T1 — Critical | Full independent validation, continuous monitoring, board-level reporting |
| Aggregate 12–15, no Critical dimensions | T2 — High | Enhanced validation, quarterly review, senior management reporting |
| Aggregate 8–11 | T3 — Medium | Standard validation, semi-annual review |
| Aggregate ≤ 7 | T4 — Low | Self-assessment, annual review |

### Tier Override Rules

Regardless of aggregate score, a use case is automatically T1 if:
- It processes customer PII through an external LLM API
- It generates content that is distributed to customers without human review
- It makes or directly influences regulated decisions (credit, insurance, AML)
- It involves agentic behavior with access to production systems or data stores

---

## Governance Requirements by Tier (GenAI-Specific)

### T1 — Critical GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Independent model evaluation; approved vendor list; architecture review board sign-off |
| Prompt governance | All prompts version-controlled, reviewed, tested against adversarial inputs |
| Guardrails | Input validation, output filtering, PII redaction, toxicity gates — all mandatory |
| Evaluation | Automated eval suite (hallucination rate, faithfulness, relevance) run on every deployment |
| Monitoring | Real-time output quality monitoring; hallucination rate dashboards; cost tracking |
| Human oversight | Human-in-the-loop for all consequential outputs; escalation paths defined |
| Audit trail | Full prompt/response logging with retention per compliance requirements |
| Vendor risk | Third-party model risk assessment; data processing agreements; exit strategy documented |
| Review cadence | Monthly review; quarterly independent validation |
| Incident response | GenAI-specific incident playbook; 15-minute response SLA for S1 |

### T2 — High GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Approved vendor list; team-level architecture review |
| Prompt governance | Prompts version-controlled and peer-reviewed |
| Guardrails | Input validation and output filtering required; PII redaction where applicable |
| Evaluation | Automated eval suite run before deployment and weekly in production |
| Monitoring | Daily output quality metrics; weekly review |
| Human oversight | Human review for outputs reaching external parties |
| Audit trail | Prompt/response logging with 5-year retention |
| Vendor risk | Standard vendor assessment; data processing agreement |
| Review cadence | Quarterly review |
| Incident response | 4-hour response SLA for S2 |

### T3 — Medium GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Approved vendor list |
| Prompt governance | Prompts stored in version control |
| Guardrails | Basic input validation |
| Evaluation | Pre-deployment eval; monthly spot checks |
| Monitoring | Weekly metrics review |
| Human oversight | Appropriate to use case |
| Audit trail | Summary logging; 3-year retention |
| Review cadence | Semi-annual review |

### T4 — Low GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Any approved vendor |
| Prompt governance | Documented |
| Guardrails | Standard acceptable use policy |
| Evaluation | Pre-deployment validation |
| Monitoring | Monthly usage review |
| Audit trail | Usage logging; 1-year retention |
| Review cadence | Annual self-assessment |

---

## Integration with Traditional ML Risk Matrix

For use cases that combine traditional ML models with GenAI components (e.g., a fraud detection system enhanced with LLM-generated explanations), assess both matrices independently. The higher tier applies to the combined system.

Document the interaction between traditional and generative components in the risk assessment, paying particular attention to:
- How GenAI outputs influence traditional model behavior (if applicable)
- Whether the GenAI component introduces new data flows that affect the traditional model's risk profile
- Whether failure of the GenAI component can degrade the traditional model's operation
