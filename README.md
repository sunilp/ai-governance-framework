# AI Governance Framework

**Practical governance patterns for AI and GenAI systems in regulated industries**

New here? Read [START-HERE.md](START-HERE.md) first: a short reading path for your role, a 30-day minimum setup, a 6-week path for one GenAI system, the fast lane for low-risk systems, and how small teams cover the roles.

---

## Philosophy

Governance is enablement, not gatekeeping. The goal is not to slow down AI adoption. It is to make AI adoption durable, defensible, and scalable across a regulated organization.

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
- [Risk Matrix (Traditional ML)](framework/risk-classification/risk-matrix.md): tiering criteria for classical ML models
- [GenAI Risk Matrix](framework/risk-classification/genai-risk-matrix.md): risk dimensions specific to LLMs and generative AI
- [Agentic AI Risk](framework/risk-classification/agentic-ai-risk.md): risk taxonomy for autonomous AI agents (single and multi-agent)
- [Multimodal AI Risk Matrix](framework/risk-classification/multimodal-risk-matrix.md): risk dimensions for vision, audio, video, and mixed-modality systems
- [Assessment Template](framework/risk-classification/assessment-template.yaml): structured risk assessment

### Model Lifecycle (Traditional ML)
Standards and gates across the full model lifecycle, from development through production monitoring.
- [Development Standards](framework/model-lifecycle/development.md)
- [Validation Requirements](framework/model-lifecycle/validation.md)
- [Deployment Gates](framework/model-lifecycle/deployment.md)
- [Production Monitoring](framework/model-lifecycle/monitoring.md)

### LLM Lifecycle (GenAI)
Governance standards specific to large language models and generative AI systems.
- [Foundation Model Selection](framework/llm-lifecycle/model-selection.md): evaluation criteria for choosing LLMs
- [Prompt Engineering Standards](framework/llm-lifecycle/prompt-engineering-standards.md): version control, review, testing
- [Fine-Tuning Governance](framework/llm-lifecycle/fine-tuning-governance.md): when and how to fine-tune safely
- [RAG Governance](framework/llm-lifecycle/rag-governance.md): retrieval quality, access controls, document lifecycle
- [GenAI Deployment Gates](framework/llm-lifecycle/deployment-gates.md): what must pass before GenAI goes live
- [LLM Production Monitoring](framework/llm-lifecycle/monitoring.md): output quality, drift, cost, safety
- [Evaluation Governance](framework/llm-lifecycle/evaluation-governance.md): what to evaluate, thresholds by tier, release criteria, dataset governance
- [Multimodal Governance](framework/llm-lifecycle/multimodal-governance.md): input/output governance for non-text modalities
- [Multi-Agent Governance](framework/llm-lifecycle/multi-agent-governance.md): orchestration, coordination, and accountability for multi-agent systems
- [Open-Source Model Governance](framework/llm-lifecycle/open-source-model-governance.md): evaluation, licensing, and maintenance for open-weight models
- [Model Deprecation Governance](framework/llm-lifecycle/model-deprecation-governance.md): sunsetting, migration, and archival
- [Agent Identity and Tool Governance](framework/llm-lifecycle/agent-identity-and-tool-governance.md): agent identities, delegation, tool and MCP/A2A allowlists, memory, kill switch, agent action audit

### AI Security
Standards for securing AI systems against adversarial threats.
- [Red-Teaming Protocol](framework/ai-security/red-teaming-protocol.md): structured adversarial testing methodology
- [Adversarial Robustness](framework/ai-security/adversarial-robustness.md): defenses against jailbreaking, prompt injection, model extraction, data poisoning
- [Supply Chain Security](framework/ai-security/supply-chain-security.md): model provenance, open-source risk, AI bill of materials

### Compliance Mapping
How framework controls map to specific regulatory requirements.
- [EU AI Act Mapping](framework/compliance/eu-ai-act-mapping.md): obligations by role (deployer, provider, GPAI downstream user), Art. 50 transparency, Arts. 4 and 5, application dates as amended in 2026
- [NIST AI RMF Mapping](framework/compliance/nist-ai-rmf-mapping.md): all 19 Core categories mapped to docs and control IDs, plus the Generative AI Profile (NIST AI 600-1)
- [ISO/IEC 42001 Mapping](framework/compliance/iso-42001-mapping.md): clauses 4 to 10 and Annex A mapped to docs and controls, with the gaps a certification audit will find
- [Multi-Jurisdictional Guide](framework/compliance/multi-jurisdictional-guide.md): EU, US, UK, Singapore, Canada, Australia, Japan, Brazil, UAE, South Korea, China, India
- [Cross-Border Data and LLM Data Residency](framework/compliance/cross-border-data-governance.md): data flows across jurisdictions and LLM architectures, residency by data class, sovereignty, conflict resolution
- [Regulatory Change Monitoring](framework/compliance/regulatory-change-monitoring.md): horizon scanning and impact assessment
- [Prompt Audit Trail](framework/compliance/prompt-audit-trail.md): logging, retention, reconstruction
- [Third-Party Model Risk](framework/compliance/third-party-model-risk.md): vendor assessment and ongoing monitoring
- [AI Procurement Clauses](framework/compliance/ai-procurement-clauses.md): contract clause set for AI vendors, including EU AI Act value-chain terms and DORA Art. 30
- [Responsible AI Checklist](framework/compliance/responsible-ai-checklist.md)
- [Audit Trail Requirements](framework/compliance/audit-trail-requirements.md)

### Responsible AI
Standards for ethical and responsible deployment of AI systems.
- [Bias Detection for LLMs](framework/responsible-ai/bias-detection-llm.md): counterfactual testing, metrics, monitoring
- [Hallucination Policy](framework/responsible-ai/hallucination-policy.md): tolerance levels, measurement, mitigation
- [Transparency Standards](framework/responsible-ai/transparency-standards.md): disclosure, labeling, explainability
- [Human-in-the-Loop Patterns](framework/responsible-ai/human-in-loop-patterns.md): when and how humans review AI output

### Operating Model
Who does what, when, and how decisions escalate.
- [AI CoE Design & Evolution](framework/operating-model/ai-coe-design.md): from centralized CoE to distributed operating model
- [GenAI Roles & Responsibilities](framework/operating-model/roles-genai.md): prompt engineers, AI risk analysts, LLMOps
- [Roles & Responsibilities (RACI)](framework/operating-model/roles-responsibilities.md)
- [Review Cadence](framework/operating-model/review-cadence.md)
- [Escalation Paths](framework/operating-model/escalation-paths.md)
- [Board Reporting](framework/operating-model/board-reporting.md): quarterly risk report structure, material incident criteria, risk appetite
- [Governance Metrics & KPIs](framework/operating-model/governance-metrics.md): measuring governance program health
- [Cost Governance](framework/operating-model/cost-governance.md): budgeting, attribution, optimization governance
- [GRC Integration](framework/operating-model/grc-integration.md): COSO, ISO 31000, three lines of defense
- [Incident Forensics](framework/operating-model/incident-forensics.md): post-incident investigation and evidence preservation
- [AI Literacy](framework/operating-model/ai-literacy.md): literacy measures by role (EU AI Act Art. 4)
- [Acceptable Use of AI Tools](framework/operating-model/acceptable-use.md): employee use of AI, coding assistants, AI embedded in SaaS, shadow AI

### Governance Operations
The operational backbone: controls, evidence, and the end-to-end process.
- [Control Register](framework/governance-operations/control-register.md): master mapping of every control to its evidence, owner, and escalation
- [Governance Workflow](framework/governance-operations/governance-workflow.md): end-to-end process from idea intake to retirement, with gates and evidence packs
- [AI Inventory](framework/governance-operations/ai-inventory.md): what to register, required fields, quarterly reconciliation
- [When to Say No](framework/governance-operations/when-to-say-no.md): when not to use GenAI or an agent, and when an external model API is unacceptable

## Machine-Readable Controls and Validation

The control register and the canonical policy tables are generated from YAML, so every rule has one source:

- [`controls/`](controls/): every control with owner, evidence, frequency, escalation, control type, the test an auditor runs, and the docs that define it
- [`policy/`](policy/): roles, tier parameters (cadences, approvers, retention), evaluation thresholds and pass rules, incident severity
- [`schemas/`](schemas/): JSON Schemas for controls, policy files, model cards and inventory entries

`python tools/build.py` regenerates the Markdown tables. `python tools/check.py` validates schemas, control references, links, generated-table drift, example conformance and the age of regulatory status lines. CI runs both on every push and pull request. See [tools/README.md](tools/README.md).

## Templates
Ready-to-use templates for immediate adoption:

**Traditional ML:**
- [Model Card Template](templates/model-card-template.yaml)
- [Impact Assessment Template](templates/impact-assessment-template.md) (includes the EU AI Act Art. 27 fundamental rights impact assessment)
- [Incident Report Template](templates/incident-report-template.md)

**GenAI / LLM:**
- [LLM Model Card Template](templates/llm-model-card.yaml): model card for LLM-based systems
- [GenAI Use Case Assessment](templates/genai-use-case-assessment.md): risk assessment for new GenAI projects
- [Prompt Review Checklist](templates/prompt-review-checklist.md): pre-deployment prompt review
- [GenAI Incident Report](templates/incident-report-genai.md): GenAI-specific incident template
- [Board AI Risk Report](templates/board-ai-risk-report.md): quarterly board reporting template
- [Red-Team Report](templates/red-team-report.md): adversarial testing findings template

**Programme:**
- [AI Policy](templates/ai-policy.md): board-approved AI policy skeleton
- [AI Risk Committee Charter](templates/ai-risk-committee-charter.md)
- [Exception Register](templates/exception-register.md)
- [AI Inventory Entry](templates/ai-inventory-entry.yaml)

## Worked Examples
See the framework applied to real-world use cases:

**Traditional ML:**
- [Credit Scoring Model](examples/credit-scoring-model/): T1 (Critical), heavily regulated, full validation
- [Fraud Detection System](examples/fraud-detection/): T1 (Critical), real-time automated blocking; Critical on scale (25M transactions a day)

**GenAI / LLM:**
- [Customer Service Chatbot](examples/customer-service-chatbot/): T1 (Critical), customer-facing, RAG-based, [complete governance case file](examples/customer-service-chatbot/governance-case-file.md)
- [Document Summarization](examples/document-summarization/): T2 (High), compliance docs, human-reviewed
- [Agentic Research Assistant](examples/agentic-research-assistant/): T1 (Critical), agentic AI with tool access
- [Internal Knowledge Search](examples/internal-knowledge-search/): T3 (Medium), internal RAG, lighter governance

## Adoption Approach

Roll out from the [governance workflow](framework/governance-operations/governance-workflow.md) and the [control register](framework/governance-operations/control-register.md). Every other document adds detail to a stage or a control. [START-HERE.md](START-HERE.md) turns the first phases into a 30-day plan.

1. **Inventory and tiering:** list every AI and GenAI system, run the Step 0 prohibited-use screen, and tier each one with the risk matrices.
2. **Pilot the workflow on one high-risk system:** walk it through the stages and close its gaps against the control register.
3. **Templates org-wide:** make the use case assessment the intake for every new system, and the model card, prompt review checklist and incident report templates the defaults.
4. **Operating model:** AI Risk Committee, review cadence, escalation paths and approvals by tier.
5. **GenAI and agentic standards:** evaluation governance, prompt and RAG standards, human oversight patterns, agentic and multi-agent controls.
6. **Security:** red-teaming, adversarial robustness and supply chain controls.
7. **Global compliance:** extend the mappings to every jurisdiction you operate in and run regulatory change monitoring.

Start where the risk is highest. T3 and T4 systems can use the [fast lane](framework/governance-operations/governance-workflow.md#fast-lane-t3t4) from day one.

## Regulatory Alignment

The framework maps to these instruments. "Reference only" means the repo cites the instrument and points to the relevant docs, without a clause-level mapping.

| Regulation | Coverage |
|---|---|
| **EU AI Act** | Deployer and provider obligations for high-risk systems, GPAI downstream checks (Arts. 53 to 55), transparency (Art. 50), AI literacy and prohibited practices (Arts. 4 and 5), application dates as amended by Regulation (EU) 2026/1744 |
| **NIST AI RMF** | Category-level mapping of all 19 AI RMF 1.0 Core categories to framework docs and control IDs, with gaps marked (subcategories not mapped); NIST AI 600-1 Generative AI Profile risk mapping |
| **ISO/IEC 42001** | Clauses 4 to 10 and Annex A (A.2 to A.10) mapped to framework docs and control IDs; lists what a certification audit needs that the framework lacks (AI policy, Statement of Applicability, AIMS scope, AI Risk Committee charter) |
| **SR 26-2 (Federal Reserve, OCC, FDIC; replaced SR 11-7 in April 2026)** | Model risk management for traditional and non-generative AI models: development, validation, monitoring and vendor models. GenAI and agentic AI are outside SR 26-2's scope; the framework's GenAI and agentic controls stand on their own |
| **MAS Guidelines on AI Risk Management (issued 7 October 2026)** | Document-level mapping in the Singapore profile and third-party hooks; AI inventory via RA-006 and GV-006; phase dates in the regulatory change monitoring deadlines table |
| **MAS FEAT Principles** | Reference only: Singapore profile maps FEAT at document level to the bias, transparency and human oversight standards |
| **IMDA/PDPC Model AI Governance Framework (incl. Agentic AI)** | Reference only: Singapore profile; the agentic framework points to the agentic risk and multi-agent standards |
| **DORA** | ICT third-party risk for AI vendors: Arts. 28 to 30 contract terms, data locations, exit strategies, concentration risk and CTPP status (third-party model risk, data residency). No register-of-information control yet; ICT risk management and incident reporting articles are not mapped |
| **GDPR** | Data protection, automated decision-making (Art. 22), DPIAs (RA-005), right to explanation |
| **PRA SS1/23** | Reference only: UK profile maps it at document level to model lifecycle standards and vendor assessment (AR-005) |
| **OSFI Guideline E-23 (effective 1 May 2027)** | Reference only: Canada profile maps it to tiering, lifecycle and review controls; model inventory via RA-006 and GV-006 |
| **Consumer Duty (FCA)** | Reference only: cited in transparency standards, the human oversight table and the UK profile |
| **Colorado SB 26-189 (from 1 January 2027)** | Reference only: US profile and deadline table; human review maps to PM-003; notice and adverse-outcome explanation are gaps |
| **BCBS 239** | Reference only: data lineage expectations cited in risk classification and data residency |
| **MiFID II** | Reference only: record-keeping reference for interaction-log retention (Art. 16(7)) |
| **LGPD (Brazil)** | Reference only: Brazil profile |

## Contributing

Contributions are welcome. If you work in regulated industries and have governance patterns worth sharing, open a PR. Practical experience matters more than theoretical frameworks.

### Related Writing

- [Your ML Risk Framework Wasn't Built for GenAI](https://sunilprakash.com/writing/ai-governance-genai/)
- [The Year LLMs Met Compliance, And Compliance Wasn't Ready](https://sunilprakash.com/writing/llms-meet-compliance/)

## Changelog

### March 2026: Comprehensive Update

- **AI Security:** Added red-teaming protocol, adversarial robustness standards, supply chain security
- **Regulatory breadth:** Added NIST AI RMF mapping, ISO/IEC 42001 mapping, multi-jurisdictional guide (8 jurisdictions), regulatory change monitoring, cross-border data governance
- **Frontier AI coverage:** Added multimodal AI risk matrix and governance, multi-agent governance, open-source model governance, model deprecation governance
- **Enterprise operations:** Added board reporting, governance metrics/KPIs, cost governance, GRC integration, incident forensics
- **Templates:** Added board risk report and red-team report templates
- **Examples:** Added T3 internal knowledge search (lighter governance demonstration)
- **Updated:** EU AI Act mappings with enforcement status and compliance evidence requirements; agentic AI risk taxonomy with multi-agent, persistent memory, and tool chain risk dimensions

## License

Apache 2.0. See [LICENSE](LICENSE).
