# Foundation Model Selection Criteria

## Overview

Selecting a foundation model for enterprise use is not a benchmarks exercise. It is a risk, capability, and operational fitness assessment that must account for regulatory constraints, data residency requirements, vendor stability, and total cost of ownership.

This document defines the evaluation framework for selecting large language models (LLMs) and other foundation models for enterprise deployment.

---

## Evaluation Dimensions

### 1. Capability Fit

Assess whether the model can perform the required task at the required quality level.

| Criterion | Assessment Method |
|-----------|------------------|
| Task performance | Run domain-specific evaluation suite; do not rely on public benchmarks alone |
| Domain knowledge | Test with representative enterprise queries; measure accuracy against ground truth |
| Language support | Validate performance in all required languages |
| Context window | Verify sufficient context for the use case (document length, conversation history) |
| Output format compliance | Test structured output generation (JSON, tables, specific formats) |
| Instruction following | Measure adherence to complex, multi-constraint prompts |
| Reasoning capability | Test multi-step reasoning chains relevant to the use case |

**Minimum requirement:** The model must demonstrate acceptable performance on a domain-specific evaluation suite before proceeding to other assessments. Generic benchmark scores (MMLU, HumanEval) are insufficient for enterprise use case approval.

### 2. Data Residency and Privacy

Assess where inference runs and data is stored, retention, training use, sub-processors, encryption and certifications with the [vendor assessment checklist](../compliance/cross-border-data-governance.md#vendor-assessment-checklist). Check that the data classes the use case sends are permitted for the hosting option ([residency by data classification](../compliance/cross-border-data-governance.md#residency-requirements-by-data-classification)).

**For regulated financial services:** Any model processing customer data, MNPI, or regulated information must have a data processing agreement (DPA) that satisfies GDPR, local data protection laws, and sectoral regulations (e.g., banking secrecy, MiFID II data requirements).

### 3. Vendor Risk

Score this dimension from the [third-party model risk assessment](../compliance/third-party-model-risk.md) (AR-005), which covers model behaviour changes and deprecation, operational and availability risk (SLAs, API changes, rate limits), vendor viability and pricing, [exit strategy](../compliance/third-party-model-risk.md#exit-strategy-requirements) and [concentration risk](../compliance/third-party-model-risk.md#concentration-risk). Open-weight models are assessed under [open-source model governance](open-source-model-governance.md) instead.

**Vendor lock-in mitigation:** For T1 and T2 use cases, maintain a validated fallback model served by a different vendor from the primary, or self-hosted. The vendor that counts is the one serving the model, not the company that trained it (see [Dimension 5](../risk-classification/genai-risk-matrix.md#dimension-5-third-party-model-dependency)). Document the performance delta and switchover procedure.

### 4. Safety and Alignment

| Criterion | Assessment |
|-----------|------------|
| Hallucination rate | Measure on domain-specific tasks; compare across candidate models |
| Toxicity and bias | Test with adversarial prompts and bias evaluation suites |
| Refusal behavior | Assess over-refusal rate on legitimate enterprise queries |
| Prompt injection resistance | Red-team with standard injection attacks; measure success rate |
| Content policy alignment | Does the model's content policy align with enterprise use case requirements? |
| Safety documentation | Transparency of model card, safety reports, known limitations |

### 5. Operational Characteristics

| Criterion | Assessment |
|-----------|------------|
| Latency (p50, p95, p99) | Measure under expected load; validate against use case SLA |
| Throughput | Tokens per second; concurrent request handling |
| Rate limits | API rate limits vs. expected traffic volume |
| Availability | Historical uptime; incident frequency and duration |
| Scalability | Can the service handle traffic spikes (10x, 100x)? |
| Cost per token | Input/output token pricing; cost projection for expected volume |
| Fine-tuning support | Availability, cost, and data requirements for fine-tuning |
| Self-hosting option | Can the model be deployed on-premises or in your cloud tenancy? |

### 6. Cost and Total Cost of Ownership

| Cost Component | Considerations |
|----------------|---------------|
| API/inference cost | Token pricing at expected volume |
| Fine-tuning cost | Training compute, data preparation effort |
| Infrastructure cost | Self-hosting compute, storage, networking |
| Integration cost | Engineering effort to integrate, build guardrails, evaluation pipelines |
| Operational cost | Monitoring, incident response, ongoing evaluation |
| Migration cost | Cost to switch if vendor relationship changes |
| Compliance cost | Audit, assessment, and documentation overhead |

---

## Model Selection Decision Matrix

Use this matrix to score candidate models. Score each dimension 1–5 (5 = best fit).

| Dimension | Weight (T1) | Weight (T2) | Weight (T3/T4) |
|-----------|-------------|-------------|-----------------|
| Capability fit | 20% | 25% | 30% |
| Data residency & privacy | 25% | 20% | 15% |
| Vendor risk | 20% | 15% | 10% |
| Safety & alignment | 20% | 20% | 15% |
| Operational characteristics | 10% | 15% | 20% |
| Cost/TCO | 5% | 5% | 10% |

**Note:** For T1 use cases, data residency and safety carry the highest combined weight. For T3/T4, capability and operational fit dominate.

---

## Model Categories and Considerations

### Commercial API and Open-Weight Models

Choose between a commercial API (OpenAI, Anthropic, Google) and an open-weight model (Llama, Mistral, Gemma) with the [open-source vs. commercial API decision framework](open-source-model-governance.md#decision-framework-open-source-vs-commercial-api).

### Fine-Tuned Models

**Advantages:** Domain specialization, consistent behavior, potentially lower inference cost (smaller models).
**Risks:** Training data governance, evaluation overhead, drift over time, maintenance burden.
**Best for:** Specialized tasks with stable requirements and sufficient high-quality training data.

---

## Approval Process

| Tier | Approval Authority |
|------|-------------------|
| T1 | AI Risk Committee + CISO |
| T2 | Head of AI |
| T3 | Team lead, choosing from the approved vendor list |
| T4 | Team lead, choosing from the approved vendor list |

### Required Documentation for Model Approval

1. Completed model evaluation report (all dimensions above)
2. Data flow diagram showing where data traverses
3. Vendor risk assessment (for commercial APIs)
4. Security review sign-off
5. Cost projection (12-month)
6. Fallback plan (T1/T2)
7. Exit strategy (T1/T2)
