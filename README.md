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
- **Board members** who need to understand AI risk posture without operational detail

## Framework Components

### Risk Classification
Define how AI systems are tiered by risk and what governance intensity each tier requires.
- [Risk Matrix (Traditional ML)](framework/risk-classification/risk-matrix.md) — tiering criteria for classical ML models
- [GenAI Risk Matrix](framework/risk-classification/genai-risk-matrix.md) — risk dimensions specific to LLMs and generative AI
- [Agentic AI Risk](framework/risk-classification/agentic-ai-risk.md) — risk taxonomy for autonomous AI agents (single and multi-agent)
- [Multimodal AI Risk Matrix](framework/risk-classification/multimodal-risk-matrix.md) — risk dimensions for vision, audio, video, and mixed-modality systems
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
- [Evaluation Governance](framework/llm-lifecycle/evaluation-governance.md) — what to evaluate, thresholds by tier, release criteria, dataset governance
- [Multimodal Governance](framework/llm-lifecycle/multimodal-governance.md) — input/output governance for non-text modalities
- [Multi-Agent Governance](framework/llm-lifecycle/multi-agent-governance.md) — orchestration, coordination, and accountability for multi-agent systems
- [Open-Source Model Governance](framework/llm-lifecycle/open-source-model-governance.md) — evaluation, licensing, and maintenance for open-weight models
- [Model Deprecation Governance](framework/llm-lifecycle/model-deprecation-governance.md) — sunsetting, migration, and archival

### AI Security
Standards for securing AI systems against adversarial threats.
- [Red-Teaming Protocol](framework/ai-security/red-teaming-protocol.md) — structured adversarial testing methodology
- [Adversarial Robustness](framework/ai-security/adversarial-robustness.md) — defenses against jailbreaking, prompt injection, model extraction, data poisoning
- [Supply Chain Security](framework/ai-security/supply-chain-security.md) — model provenance, open-source risk, AI bill of materials

### Compliance Mapping
How framework controls map to specific regulatory requirements.
- [EU AI Act Mapping](framework/compliance/eu-ai-act-mapping.md) — traditional AI system requirements (with enforcement status)
- [EU AI Act — GenAI Mapping](framework/compliance/eu-ai-act-genai-mapping.md) — GPAI model obligations, Article 50 transparency
- [NIST AI RMF Mapping](framework/compliance/nist-ai-rmf-mapping.md) — Govern, Map, Measure, Manage function alignment
- [ISO/IEC 42001 Mapping](framework/compliance/iso-42001-mapping.md) — AI management system certification backbone
- [Multi-Jurisdictional Guide](framework/compliance/multi-jurisdictional-guide.md) — EU, US, Singapore, UAE, Brazil, Canada, Australia, Japan
- [Cross-Border Data Governance](framework/compliance/cross-border-data-governance.md) — data flows, sovereignty, conflict resolution
- [Regulatory Change Monitoring](framework/compliance/regulatory-change-monitoring.md) — horizon scanning and impact assessment
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
- [Board Reporting](framework/operating-model/board-reporting.md) — quarterly risk report structure, material incident criteria, risk appetite
- [Governance Metrics & KPIs](framework/operating-model/governance-metrics.md) — measuring governance program health
- [Cost Governance](framework/operating-model/cost-governance.md) — budgeting, attribution, optimization governance
- [GRC Integration](framework/operating-model/grc-integration.md) — COSO, ISO 31000, three lines of defense
- [Incident Forensics](framework/operating-model/incident-forensics.md) — post-incident investigation and evidence preservation

### Governance Operations
The operational backbone — controls, evidence, and the end-to-end process.
- [Control Register](framework/governance-operations/control-register.md) — master mapping of every control to its evidence, owner, and escalation
- [Governance Workflow](framework/governance-operations/governance-workflow.md) — end-to-end process from idea intake to retirement, with gates and evidence packs

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
- [Board AI Risk Report](templates/board-ai-risk-report.md) — quarterly board reporting template
- [Red-Team Report](templates/red-team-report.md) — adversarial testing findings template

## Worked Examples
See the framework applied to real-world use cases:

**Traditional ML:**
- [Credit Scoring Model](examples/credit-scoring-model/) — T1 (Critical), heavily regulated, full validation
- [Fraud Detection System](examples/fraud-detection/) — T2 (High), real-time, high-autonomy

**GenAI / LLM:**
- [Customer Service Chatbot](examples/customer-service-chatbot/) — T1 (Critical), customer-facing, RAG-based, [complete governance case file](examples/customer-service-chatbot/governance-case-file.md)
- [Document Summarization](examples/document-summarization/) — T2 (High), compliance docs, human-reviewed
- [Agentic Research Assistant](examples/agentic-research-assistant/) — T1 (Critical), agentic AI with tool access
- [Internal Knowledge Search](examples/internal-knowledge-search/) — T3 (Medium), internal RAG, lighter governance

## Adoption Approach

This framework is designed for phased rollout:

1. **Phase 1 (Week 1–2):** Adopt the risk classification matrix. Tier your existing AI and GenAI systems.
2. **Phase 2 (Month 1):** Apply lifecycle standards to one high-risk system as a pilot.
3. **Phase 3 (Month 2–3):** Roll out templates (model cards, impact assessments, prompt review checklists) org-wide.
4. **Phase 4 (Ongoing):** Establish the operating model — governance cadence, escalation paths, RACI.
5. **Phase 5 (GenAI):** Apply LLM lifecycle standards — model selection, prompt governance, RAG governance, deployment gates.
6. **Phase 6 (Security):** Establish red-teaming program, adversarial robustness standards, supply chain governance.
7. **Phase 7 (Global):** Extend compliance mapping to all operating jurisdictions; implement regulatory change monitoring.

Start where the risk is highest. Expand as the organization builds muscle memory.

## Regulatory Alignment

This framework has been designed with explicit alignment to:

| Regulation | Coverage |
|---|---|
| **EU AI Act** | High-risk system requirements (Articles 6–15), GPAI model obligations (Articles 53–55), transparency (Article 50), enforcement status tracking |
| **NIST AI RMF** | Govern, Map, Measure, Manage functions — full category-level mapping |
| **ISO/IEC 42001** | AI management system — clause-by-clause implementation mapping for certification |
| **SR 11-7 (Fed/OCC)** | Model risk management — development, validation, governance |
| **MAS FEAT** | Fairness, Ethics, Accountability, Transparency principles for AI in financial services |
| **MAS Model Governance Framework** | Singapore AI governance — model risk, fairness, explainability |
| **BCBS 239** | Risk data aggregation and reporting — data lineage, quality, timeliness |
| **DORA** | Digital operational resilience — ICT risk management for AI systems |
| **GDPR** | Data protection, automated decision-making (Article 22), right to explanation |
| **LGPD (Brazil)** | Data protection for AI systems — consent, data subject rights |
| **MiFID II** | Investment research requirements, communication recording |
| **Consumer Duty (FCA)** | Fair customer outcomes, clear AI communications |

## Contributing

Contributions are welcome. If you work in regulated industries and have governance patterns worth sharing, open a PR. Practical experience matters more than theoretical frameworks.

### Related Writing

- [Your ML Risk Framework Wasn't Built for GenAI](https://sunilprakash.com/writing/ai-governance-genai/)
- [The Year LLMs Met Compliance — And Compliance Wasn't Ready](https://sunilprakash.com/writing/llms-meet-compliance/)

## Changelog

### March 2026 — Comprehensive Update

- **AI Security:** Added red-teaming protocol, adversarial robustness standards, supply chain security
- **Regulatory breadth:** Added NIST AI RMF mapping, ISO/IEC 42001 mapping, multi-jurisdictional guide (8 jurisdictions), regulatory change monitoring, cross-border data governance
- **Frontier AI coverage:** Added multimodal AI risk matrix and governance, multi-agent governance, open-source model governance, model deprecation governance
- **Enterprise operations:** Added board reporting, governance metrics/KPIs, cost governance, GRC integration, incident forensics
- **Templates:** Added board risk report and red-team report templates
- **Examples:** Added T3 internal knowledge search (lighter governance demonstration)
- **Updated:** EU AI Act mappings with enforcement status and compliance evidence requirements; agentic AI risk taxonomy with multi-agent, persistent memory, and tool chain risk dimensions

## License

Apache 2.0 — see [LICENSE](LICENSE).
