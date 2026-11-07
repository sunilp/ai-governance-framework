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

The sensitivity of data that flows through the LLM pipeline: prompts, context windows, RAG retrieval, fine-tuning datasets, and outputs.

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

## Step 0: Prohibited-Use Screen

Before scoring, screen the use case against EU AI Act Art. 5 (prohibited AI practices) and the organisation's internal prohibited-use policy. Prohibited uses are not tiered. They are rejected at Stage 2 and do not proceed. Record the result in the risk assessment (RA-007). The check is non-waivable (see [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance)).

Art. 5 prohibits, among other practices:
- manipulative or deceptive techniques, or exploiting vulnerabilities, in ways that cause significant harm;
- social scoring;
- predicting that a person will commit a crime based solely on profiling or personality traits;
- untargeted scraping of facial images to build facial recognition databases;
- emotion recognition in the workplace and in education;
- biometric categorisation to infer sensitive characteristics.

From 2 December 2026 it also prohibits AI systems that generate non-consensual intimate imagery of identifiable people or child sexual abuse material. The full list, with notes for banking, is in the [EU AI Act mapping](../compliance/eu-ai-act-mapping.md#prohibited-practices-art-5).

---

## Risk Tier Determination for GenAI

Score each dimension as Critical (4), High (3), Medium (2), or Low (1). **The highest-scoring dimension sets the tier.** Then apply the override rules below. Overrides can raise the tier, never lower it. The approver may raise a tier with a recorded rationale (for example, a pilot with an unusual exposure profile). Nobody can lower a tier below what the scoring and overrides give.

| Highest dimension score | Tier | Governance Intensity |
|-------------------------|------|---------------------|
| Any dimension Critical | T1 Critical | Full independent validation, continuous monitoring, board-level reporting |
| Any dimension High, none Critical | T2 High | Independent validation (reduced scope), semi-annual review, senior management reporting |
| Any dimension Medium, none High or Critical | T3 Medium | Peer review, annual review |
| All dimensions Low | T4 Low | Self-test, annual self-assessment |

Record the aggregate score (the sum of the five scores, 5 to 20) for context and comparison across systems. It does not set the tier. The same rule applies in [risk-matrix.md](risk-matrix.md), [multimodal-risk-matrix.md](multimodal-risk-matrix.md) and [agentic-ai-risk.md](agentic-ai-risk.md).

### Tier Override Rules

This is the canonical override list. [risk-matrix.md](risk-matrix.md), [multimodal-risk-matrix.md](multimodal-risk-matrix.md) and [agentic-ai-risk.md](agentic-ai-risk.md) use the same list. Overrides can raise the tier, never lower it.

**Automatic T1:**

1. Makes or directly influences regulated decisions (credit, insurance underwriting or pricing, AML/sanctions, employment).
2. Generates customer-facing content delivered without per-output human review.
3. Processes customer personal data through an external LLM API without **all** of these safeguards: zero data retention by the vendor, a regional endpoint that meets data residency requirements, a signed DPA, and PII redaction or minimisation before the call. (With all four safeguards in place: minimum T2, and normal scoring decides.)
4. Agentic behaviour with write access to production systems or data stores, or with authority to move money, communicate with customers, or change identity and access.
5. Biometric identification or categorisation; synthetic media that can depict real people (deepfake-capable); voice cloning; medical imagery.

**Minimum T2:**

6. Any agentic system, including read-only tool use, and any multi-agent system.
7. Synthetic media generation not covered by item 5.
8. Customer personal data through an external LLM API with all four safeguards in place.
9. Personal data in visual content.

---

## Governance Requirements by Tier (GenAI-Specific)

### T1: Critical GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Independent model evaluation; approved vendor list; model selection approved by AI Risk Committee + CISO; architecture review board sign-off |
| Prompt governance | All prompts version-controlled, reviewed, tested against adversarial inputs |
| Guardrails | Input validation, output filtering, PII redaction, toxicity gates: all mandatory |
| Evaluation | Automated eval suite (hallucination rate, faithfulness, relevance) run on every deployment |
| Monitoring | Real-time output quality monitoring; hallucination rate dashboards; cost tracking |
| Human oversight | Regulated decisions: Pattern 1 (human-in-the-loop) for adverse or non-standard outcomes; favourable outcomes within approved policy may be automated where the law permits, with a route to human review on request. Customer-facing informational systems: Pattern 1, or Pattern 3 (human-over-the-loop) only with all five safeguards in place and evidenced. See [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix). Escalation paths defined |
| Audit trail | Full prompt/response logging; 7-year retention (see [retention requirements](../compliance/prompt-audit-trail.md#retention-requirements)) |
| Vendor risk | Third-party model risk assessment; data processing agreements; exit strategy documented |
| Review cadence | Daily dashboard check by AI Operations and monthly system-owner metrics review; quarterly governance review; annual independent revalidation |
| Incident response | GenAI-specific incident playbook; response SLAs by severity (see [severity classification](../operating-model/escalation-paths.md#severity-classification)) |

### T2: High GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Approved vendor list; model selection approved by Head of AI; recorded team-level design review approved by the Head of AI or delegate |
| Prompt governance | Prompts version-controlled and peer-reviewed |
| Guardrails | Input validation and output filtering required; PII redaction where applicable |
| Evaluation | Automated eval suite run before deployment; production evaluation per [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md#evaluation-types) |
| Monitoring | Daily output quality metrics; weekly review |
| Human oversight | Outputs reaching external parties: Pattern 1, or Pattern 3 with sampled review, output scope guardrails and hallucination monitoring (see [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix)) |
| Audit trail | Prompt/response logging with 5-year retention |
| Vendor risk | Standard vendor assessment; data processing agreement |
| Review cadence | Semi-annual governance review |
| Incident response | Response SLAs by severity (see [severity classification](../operating-model/escalation-paths.md#severity-classification)) |

### T3: Medium GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Approved vendor list |
| Prompt governance | Prompts stored in version control |
| Guardrails | Basic input validation |
| Evaluation | Pre-deployment and safety eval; 5% sampled automated scoring in production |
| Monitoring | Monthly metrics review |
| Human oversight | Appropriate to use case |
| Audit trail | Summary logging; 3-year retention |
| Review cadence | Annual governance review |

### T4: Low GenAI Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Model selection | Any approved vendor |
| Prompt governance | Documented |
| Guardrails | Standard [acceptable use policy](../operating-model/acceptable-use.md) (GV-003) |
| Evaluation | Pre-deployment and safety eval (automated, 20+ cases each) |
| Monitoring | Quarterly metrics review |
| Audit trail | Usage logging; 1-year retention |
| Review cadence | Annual self-assessment |

---

## Integration with Traditional ML Risk Matrix

For use cases that combine traditional ML models with GenAI components (e.g., a fraud detection system enhanced with LLM-generated explanations), assess both matrices independently. The higher tier applies to the combined system.

Document the interaction between traditional and generative components in the risk assessment, paying particular attention to:
- How GenAI outputs influence traditional model behavior (if applicable)
- Whether the GenAI component introduces new data flows that affect the traditional model's risk profile
- Whether failure of the GenAI component can degrade the traditional model's operation
