# AI Governance Framework

**Practical governance patterns for AI and GenAI systems in regulated industries**

---

## Philosophy

Governance is enablement, not gatekeeping. The goal is not to slow down AI adoption — it is to make AI adoption durable, defensible, and scalable across a regulated organization.

This framework provides opinionated, field-tested patterns for governing both traditional ML and GenAI/LLM systems in financial services, healthcare, and other industries where model risk, data privacy, and regulatory compliance are non-negotiable.

## Who This Is For

- **Chief Risk Officers** who need confidence that AI systems meet regulatory expectations
- **CTOs and Engineering VPs** who need repeatable standards for AI productionization
- **AI/ML leads** who need clear guardrails without bureaucratic overhead
- **Compliance teams** who need to map AI controls to regulatory requirements
- **CISOs** who need to assess the security surface of LLM and agentic AI systems

## Framework Components

### Risk Classification
Define how AI systems are tiered by risk and what governance intensity each tier requires.
- [Risk Matrix (Traditional ML)](framework/risk-classification/risk-matrix.md) — tiering criteria for classical ML models
- [GenAI Risk Matrix](framework/risk-classification/genai-risk-matrix.md) — risk dimensions specific to LLMs and generative AI
- [Agentic AI Risk](framework/risk-classification/agentic-ai-risk.md) — risk taxonomy for autonomous AI agents
- [Assessment Template](framework/risk-classification/assessment-template.yaml) — structured risk assessment

### Model Lifecycle (Traditional ML)
Standards and gates across the full model lifecycle — from development through production monitoring.
- [Development Standards](framework/model-lifecycle/development.md)
- [Validation Requirements](framework/model-lifecycle/validation.md)
- [Deployment Gates](framework/model-lifecycle/deployment.md)
- [Production Monitoring](framework/model-lifecycle/monitoring.md)

### LLM Lifecycle (GenAI)
Governance standards specific to large language models and generative AI systems.
- [Foundation Model Selection](framework/llm-lifecycle/model-selection.md) — evaluation criteria for choosing LLMs
- [Prompt Engineering Standards](framework/llm-lifecycle/prompt-engineering-standards.md) — version control, review, testing
- [Fine-Tuning Governance](framework/llm-lifecycle/fine-tuning-governance.md) — when and how to fine-tune safely
- [RAG Governance](framework/llm-lifecycle/rag-governance.md) — retrieval quality, access controls, document lifecycle
- [GenAI Deployment Gates](framework/llm-lifecycle/deployment-gates.md) — what must pass before GenAI goes live
- [LLM Production Monitoring](framework/llm-lifecycle/monitoring.md) — output quality, drift, cost, safety

### Compliance Mapping
How framework controls map to specific regulatory requirements.
- [EU AI Act Mapping](framework/compliance/eu-ai-act-mapping.md) — traditional AI system requirements
- [EU AI Act — GenAI Mapping](framework/compliance/eu-ai-act-genai-mapping.md) — GPAI model obligations, Article 50 transparency
- [Prompt Audit Trail](framework/compliance/prompt-audit-trail.md) — logging, retention, reconstruction
- [Data Residency for LLMs](framework/compliance/data-residency-llm.md) — data flows in LLM architectures
- [Third-Party Model Risk](framework/compliance/third-party-model-risk.md) — vendor assessment and ongoing monitoring
- [Responsible AI Checklist](framework/compliance/responsible-ai-checklist.md)
- [Audit Trail Requirements](framework/compliance/audit-trail-requirements.md)

### Responsible AI
Standards for ethical and responsible deployment of AI systems.
- [Bias Detection for LLMs](framework/responsible-ai/bias-detection-llm.md) — counterfactual testing, metrics, monitoring
- [Hallucination Policy](framework/responsible-ai/hallucination-policy.md) — tolerance levels, measurement, mitigation
- [Transparency Standards](framework/responsible-ai/transparency-standards.md) — disclosure, labeling, explainability
- [Human-in-the-Loop Patterns](framework/responsible-ai/human-in-loop-patterns.md) — when and how humans review AI output

### Operating Model
Who does what, when, and how decisions escalate.
- [AI CoE Design & Evolution](framework/operating-model/ai-coe-design.md) — from centralized CoE to distributed operating model
- [GenAI Roles & Responsibilities](framework/operating-model/roles-genai.md) — prompt engineers, AI risk analysts, LLMOps
- [Roles & Responsibilities (RACI)](framework/operating-model/roles-responsibilities.md)
- [Review Cadence](framework/operating-model/review-cadence.md)
- [Escalation Paths](framework/operating-model/escalation-paths.md)

## Templates
Ready-to-use templates for immediate adoption:

**Traditional ML:**
- [Model Card Template](templates/model-card-template.yaml)
- [Impact Assessment Template](templates/impact-assessment-template.md)
- [Incident Report Template](templates/incident-report-template.md)

**GenAI / LLM:**
- [LLM Model Card Template](templates/llm-model-card.yaml) — model card for LLM-based systems
- [GenAI Use Case Assessment](templates/genai-use-case-assessment.md) — risk assessment for new GenAI projects
- [Prompt Review Checklist](templates/prompt-review-checklist.md) — pre-deployment prompt review
- [GenAI Incident Report](templates/incident-report-genai.md) — GenAI-specific incident template

## Worked Examples
See the framework applied to real-world use cases:

**Traditional ML:**
- [Credit Scoring Model](examples/credit-scoring-model/) — T1 (Critical), heavily regulated, full validation
- [Fraud Detection System](examples/fraud-detection/) — T2 (High), real-time, high-autonomy

**GenAI / LLM:**
- [Customer Service Chatbot](examples/customer-service-chatbot/) — T1 (Critical), customer-facing, RAG-based
- [Document Summarization](examples/document-summarization/) — T2 (High), compliance docs, human-reviewed
- [Agentic Research Assistant](examples/agentic-research-assistant/) — T1 (Critical), agentic AI with tool access

## Adoption Approach

This framework is designed for phased rollout:

1. **Phase 1 (Week 1–2):** Adopt the risk classification matrix. Tier your existing AI and GenAI systems.
2. **Phase 2 (Month 1):** Apply lifecycle standards to one high-risk system as a pilot.
3. **Phase 3 (Month 2–3):** Roll out templates (model cards, impact assessments, prompt review checklists) org-wide.
4. **Phase 4 (Ongoing):** Establish the operating model — governance cadence, escalation paths, RACI.
5. **Phase 5 (GenAI):** Apply LLM lifecycle standards — model selection, prompt governance, RAG governance, deployment gates.

Start where the risk is highest. Expand as the organization builds muscle memory.

## Regulatory Alignment

This framework has been designed with explicit alignment to:

| Regulation | Coverage |
|---|---|
| **EU AI Act** | High-risk system requirements (Articles 6–15), GPAI model obligations (Articles 53–55), transparency (Article 50) |
| **SR 11-7 (Fed/OCC)** | Model risk management — development, validation, governance |
| **MAS FEAT** | Fairness, Ethics, Accountability, Transparency principles for AI in financial services |
| **BCBS 239** | Risk data aggregation and reporting — data lineage, quality, timeliness |
| **DORA** | Digital operational resilience — ICT risk management for AI systems |
| **GDPR** | Data protection, automated decision-making (Article 22), right to explanation |
| **MiFID II** | Investment research requirements, communication recording |
| **Consumer Duty (FCA)** | Fair customer outcomes, clear AI communications |

## Contributing

Contributions are welcome. If you work in regulated industries and have governance patterns worth sharing, open a PR. Practical experience matters more than theoretical frameworks.

## License

Apache 2.0 — see [LICENSE](LICENSE).
