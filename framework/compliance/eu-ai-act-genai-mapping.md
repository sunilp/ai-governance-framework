# EU AI Act — GenAI-Specific Compliance Mapping

## Overview

The EU AI Act (Regulation 2024/1689) introduces specific obligations for General-Purpose AI (GPAI) models and systems that extend beyond the risk-based requirements applicable to all AI systems. This document maps those GenAI-specific obligations to framework controls.

For the broader EU AI Act mapping covering all AI system types, see [eu-ai-act-mapping.md](eu-ai-act-mapping.md).

---

## GPAI Model Obligations (Article 53)

These obligations apply to providers of GPAI models — the foundation model vendors (OpenAI, Anthropic, Google, Meta, Mistral, etc.). As a deployer, you must verify that your chosen model provider meets these obligations.

| Obligation | Article | What Providers Must Do | What Deployers Must Verify |
|-----------|---------|----------------------|---------------------------|
| Technical documentation | 53(1)(a) | Maintain and make available technical documentation of the model | Request and review model documentation; file with risk assessment |
| Information for downstream providers | 53(1)(b) | Provide information to downstream deployers to comply with the Act | Obtain model cards, safety reports, usage guidelines |
| Copyright compliance | 53(1)(c) | Implement a policy to comply with copyright law (text and data mining opt-outs) | Confirm provider's copyright compliance policy; assess IP risk |
| Training data summary | 53(1)(d) | Publish a sufficiently detailed summary of training data | Review training data summary; assess relevance and bias risks |

### Verification Checklist for Deployers

- [ ] Model provider has published technical documentation
- [ ] Model card with capabilities, limitations, and intended use is available
- [ ] Provider's copyright compliance policy reviewed and filed
- [ ] Training data summary reviewed for bias, geographic, and demographic considerations
- [ ] Provider's terms of service reviewed for data usage, retention, and processing terms
- [ ] Provider's security certifications verified (SOC 2, ISO 27001)

---

## Systemic Risk GPAI Models (Article 55)

Models with systemic risk (high-impact GPAI models) face additional obligations. A model is classified as systemic risk if it has high-impact capabilities or if the cumulative compute used for training exceeds 10^25 FLOP.

Currently this applies to models like GPT-4, Claude 3.5/4, Gemini Ultra. As a deployer using these models:

| Additional Obligation | Deployer Impact |
|----------------------|-----------------|
| Model evaluation against state-of-the-art benchmarks | Review provider's published evaluations; supplement with domain-specific evaluation |
| Adversarial testing (red-teaming) | Conduct your own adversarial testing for your specific use case |
| Incident reporting | Establish incident identification and reporting procedures; coordinate with provider |
| Cybersecurity protections | Verify provider's cybersecurity posture; implement your own application-layer security |

---

## Transparency Obligations for AI-Generated Content (Article 50)

| Obligation | Application | Framework Control |
|-----------|-------------|-------------------|
| AI disclosure — direct interaction | Users must be informed they are interacting with AI (unless obvious from context) | All customer-facing GenAI systems must clearly disclose AI involvement |
| AI disclosure — synthetic content | Content generated or manipulated by AI must be machine-readable as such (watermarking, metadata) | Generated text, images, or audio must be labeled as AI-generated |
| AI disclosure — deep fakes | Synthetic audio, image, or video must be disclosed | Not typically applicable in financial services; policy documented nonetheless |
| Emotion recognition / biometric categorization | Prohibited in certain contexts; notification required in others | Policy: no emotion recognition or biometric AI without explicit legal basis and approval |

### Implementation Requirements

For each GenAI use case, document:
1. **How users are informed** that they are interacting with AI
2. **How AI-generated content is labeled** in outputs and downstream systems
3. **Where AI-generated content enters human workflows** and how attribution is maintained

---

## High-Risk AI System Requirements Applied to GenAI (Articles 9–15)

When a GenAI system is used in a high-risk context (Annex III — credit scoring, insurance, employment, etc.), the full high-risk AI system requirements apply. Key GenAI-specific considerations:

### Risk Management System (Article 9)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Model validation against test data | Evaluation suite for hallucination, faithfulness, safety |
| Performance monitoring | Output quality monitoring, drift detection, adversarial testing |
| Risk identification | Prompt injection, data leakage, uncontrolled generation, vendor dependency |

### Data Governance (Article 10)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Training data quality and representativeness | RAG corpus governance — freshness, accuracy, access controls |
| Bias in training data | Bias in retrieved context; bias in foundation model training data (assess via model card) |
| Data lineage | Prompt version control; context document provenance; full query-to-response traceability |

### Technical Documentation (Article 11)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Model architecture and training details | Foundation model selection rationale; prompt architecture; RAG pipeline design |
| Performance metrics | GenAI-specific metrics: hallucination rate, faithfulness, safety scores |
| Limitations | LLM-specific limitations: context window constraints, language biases, knowledge cutoff |

### Record-Keeping (Article 12)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Prediction logs | Full prompt/response logging with context documents |
| Model version history | Prompt version history, model version tracking, guardrail configuration history |
| Incident records | GenAI-specific incident taxonomy (hallucination, prompt injection, data leakage) |

### Transparency and User Information (Article 13)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Model explainability | Provide attribution to source documents (RAG); explain confidence/uncertainty |
| User instructions | Clear guidance on what the AI can/cannot do; how to interpret outputs; how to provide feedback |
| Limitation disclosure | Explicit disclosure of hallucination risk, knowledge cutoff, and scope boundaries |

### Human Oversight (Article 14)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Human-in-the-loop for decisions | Human review of GenAI outputs before consequential use |
| Override capability | Ability to override, correct, or reject AI-generated content |
| Monitoring capability | Real-time dashboards for output quality, safety metrics, user feedback |

### Accuracy, Robustness, Cybersecurity (Article 15)

| Traditional ML Approach | GenAI Extension |
|------------------------|-----------------|
| Model accuracy metrics | Hallucination rate, faithfulness score, correctness on domain tasks |
| Robustness testing | Adversarial prompt testing, edge case evaluation, input fuzzing |
| Cybersecurity | Prompt injection defense, guardrail integrity, API security, data exfiltration prevention |

---

## Compliance Timeline

| Deadline | Obligation |
|----------|-----------|
| February 2025 | Prohibited AI practices apply |
| August 2025 | GPAI model obligations apply (Articles 53–55) |
| August 2026 | Full Act applies including high-risk AI system requirements |
| August 2027 | High-risk AI systems in Annex I (regulated products) |

### Action Items for Enterprise GenAI Programs

1. **Now:** Inventory all GenAI use cases; classify by risk tier and EU AI Act applicability
2. **Now:** Verify GPAI model provider compliance (Article 53 obligations)
3. **Now:** Implement transparency measures for all customer-facing AI (Article 50)
4. **By August 2026:** Full compliance for high-risk GenAI systems (Articles 9–15)
5. **Ongoing:** Monitor regulatory guidance and standards from the AI Office

---

## Enforcement Status (as of March 2026)

| Obligation | Status | Practical Impact |
|-----------|--------|-----------------|
| GPAI model obligations (Art. 53) | **In force since August 2025** | Your model providers must already be compliant. If they are not providing technical documentation and training data summaries, escalate to procurement. |
| Systemic risk GPAI obligations (Art. 55) | **In force since August 2025** | If you use GPT-4, Claude, Gemini Ultra, or similar high-capability models — verify the provider has completed model evaluations and adversarial testing per Article 55. |
| Transparency (Art. 50) | **In force since August 2025** | All customer-facing GenAI systems must disclose AI involvement NOW. Audit all customer-facing systems for compliance. |
| High-risk GenAI systems (Art. 6–15) | **August 2026** | T1 GenAI systems must have full conformity evidence in 5 months. Prioritize conformity assessment for highest-risk systems. |

---

## Practical Compliance Evidence for Deployers

For organizations deploying (not developing) GPAI models — what you need in your compliance files:

| Requirement | Evidence to Maintain |
|-------------|---------------------|
| Provider technical documentation (Art. 53(1)(a)) | Filed copy of provider's system card or model card; date obtained; review notes |
| Copyright compliance (Art. 53(1)(c)) | Provider's published copyright policy + your internal assessment of IP risk |
| Training data summary (Art. 53(1)(d)) | Provider's training data disclosure + your bias assessment based on it |
| Deployment transparency (Art. 50) | Screenshots or logs of AI disclosure implementation in your systems |
| Adversarial testing (Art. 55) | Your own red-team report for your specific use case — not just the provider's general testing |
| Incident reporting | Incident report template ready; records of any incidents reported to the AI Office |
| Conformity evidence (Art. 6–15, for high-risk) | Complete package: risk assessment, model card, validation report, audit trail, monitoring evidence |
