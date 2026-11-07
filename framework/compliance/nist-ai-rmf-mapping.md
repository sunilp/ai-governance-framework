# NIST AI Risk Management Framework Mapping

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

## Overview

The NIST AI Risk Management Framework (AI RMF 1.0, NIST AI 100-1) was released on 26 January 2023. It is voluntary. Its Core has four functions (GOVERN, MAP, MEASURE, MANAGE) split into 19 categories, which are split into subcategories.

NIST states on its AI RMF page that AI RMF 1.0 "is being revised as part of the White House AI Action Plan". No revised version had been published when this mapping was checked, so it maps AI RMF 1.0.

**Coverage of this mapping:** every one of the 19 Core categories is mapped to framework documents and to control IDs in the [control register](../governance-operations/control-register.md). Where the framework has no matching control, the row says "No control yet (gap)". Subcategories are not mapped one by one; they are cited only where a gap sits at subcategory level. For subcategory-level actions, use the NIST AI RMF Playbook, which "provides suggested actions for achieving the outcomes laid out in the AI RMF Core".

Category numbers below follow NIST's own labels (GOVERN 1, MAP 1, and so on). Category text is abridged from the AI RMF Core.

---

## Core Functions Alignment

| NIST AI RMF Function | What it covers | Framework Equivalent | Key References |
|---------------------|---------|---------------------|----------------|
| **GOVERN** | Policies, accountability, workforce, risk culture, engagement with AI actors, third-party risk | Operating model, governance workflow, control register | [operating-model/](../operating-model/), [governance-operations/](../governance-operations/) |
| **MAP** | Context, categorization, capabilities and costs, component risks, impacts | Risk classification and impact assessment | [risk-classification/](../risk-classification/) |
| **MEASURE** | Methods and metrics, evaluation of trustworthy characteristics, risk tracking, feedback on measurement | Validation, evaluation, red-teaming, monitoring | [model-lifecycle/](../model-lifecycle/), [llm-lifecycle/](../llm-lifecycle/), [ai-security/](../ai-security/) |
| **MANAGE** | Risk prioritization and response, benefit and impact strategies, third-party risk, response, recovery and communication | Deployment approval, incident response, escalation, deprecation | [governance-workflow.md](../governance-operations/governance-workflow.md), [escalation-paths.md](../operating-model/escalation-paths.md) |

---

## GOVERN Function Mapping

| NIST Category | Category (abridged) | Framework Implementation | Controls | Reference |
|--------------|-------------|-------------------|----------|-----------|
| GOVERN 1 | Policies, processes, procedures and practices for mapping, measuring and managing AI risk are in place, transparent and implemented effectively | A board-approved AI policy, reviewed annually; risk matrices set governance intensity per tier; the 10-stage governance workflow and control register define the process; exceptions need approved risk acceptance and are held in a register reviewed monthly; regulatory change triggers reassessment; decommissioning is governed. AI system inventory (GOVERN 1.6): an inventory standard, registration before development, and quarterly reconciliation against procurement, cloud spend, SaaS consoles and network telemetry to find shadow AI | GV-001, GV-004, GV-006, RA-001, RA-004, RV-001, RV-004, DR-001 to DR-004 | [AI Policy Template](../../templates/ai-policy.md), [Risk Matrix](../risk-classification/risk-matrix.md), [Governance Workflow](../governance-operations/governance-workflow.md), [Control Register](../governance-operations/control-register.md), [AI Inventory](../governance-operations/ai-inventory.md), [Regulatory Change Monitoring](regulatory-change-monitoring.md) |
| GOVERN 2 | Accountability structures are in place; teams and individuals are empowered, responsible and trained | RACI matrices for traditional ML and GenAI; named owners per control; tiered sign-off chains; three lines of defense; an AI Risk Committee charter with decision rights and escalation to the board. Training (GOVERN 2.2): role-based AI literacy measures for the board, executives, all staff, builders, human oversight reviewers and the second line, with completion tracked | RA-004, AR-002, DA-002, GV-002, GV-005 | [Roles & Responsibilities](../operating-model/roles-responsibilities.md), [GenAI Roles](../operating-model/roles-genai.md), [AI Literacy](../operating-model/ai-literacy.md), [AI Risk Committee Charter](../../templates/ai-risk-committee-charter.md), [Governance Metrics](../operating-model/governance-metrics.md) |
| GOVERN 3 | Workforce diversity, equity, inclusion and accessibility processes are prioritized | The AI Risk Committee draws on risk, technology, compliance, data science and business roles. Roles for human-AI configuration and oversight (GOVERN 3.2) are set by the pattern selection matrix. No requirement for diverse teams in risk decisions (GOVERN 3.1) | PM-003. Diversity: No control yet (gap) | [Review Cadence](../operating-model/review-cadence.md), [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md) |
| GOVERN 4 | Teams are committed to a culture that considers and communicates AI risk | Board-approved risk appetite; quarterly board reporting; independent red-teaming; post-mortems and a shared attack library; risks and impacts documented in model cards and impact assessments | RA-003, DE-001, SR-001, IR-004 | [Board Reporting](../operating-model/board-reporting.md), [Red-Teaming Protocol](../ai-security/red-teaming-protocol.md), [Incident Forensics](../operating-model/incident-forensics.md) |
| GOVERN 5 | Processes are in place for robust engagement with relevant AI actors | Impact assessment identifies affected stakeholders; user feedback is monitored in production; stakeholder communication is set in transparency standards. No process for collecting feedback from people outside the team, such as affected communities (GOVERN 5.1) | RA-003, PM-004. External feedback: No control yet (gap) | [Impact Assessment](../../templates/impact-assessment-template.md), [LLM Monitoring](../llm-lifecycle/monitoring.md), [Transparency Standards](../responsible-ai/transparency-standards.md) |
| GOVERN 6 | Policies and procedures address AI risks and benefits from third-party software and data and other supply chain issues | Vendor risk assessment by tier, including IP and copyright risk; open-source license review; model provenance and AI-BOM; data provenance for fine-tuning; exit strategy and pre-validated fallback for T1/T2 (contingency, GOVERN 6.2); concentration limits; AI features embedded in bought products and staff AI tools treated as vendor AI | AR-004, AR-005, SR-004, DE-005, DA-004, GV-003 | [Third-Party Model Risk](third-party-model-risk.md), [Supply Chain Security](../ai-security/supply-chain-security.md), [Open-Source Model Governance](../llm-lifecycle/open-source-model-governance.md), [Acceptable Use](../operating-model/acceptable-use.md) |

---

## MAP Function Mapping

| NIST Category | Category (abridged) | Framework Implementation | Controls | Reference |
|--------------|-------------|-------------------|----------|-----------|
| MAP 1 | Context is established and understood | Intake form and risk assessment template capture use case, users, decision type and regulatory context; GenAI risk dimensions add model-specific context; risk tolerance is set in the risk appetite statement | RA-001, RA-003 | [Assessment Template](../risk-classification/assessment-template.yaml), [GenAI Risk Matrix](../risk-classification/genai-risk-matrix.md), [Board Reporting](../operating-model/board-reporting.md) |
| MAP 2 | Categorization of the AI system is performed | Four-tier classification (T1-T4) with the canonical override list; GenAI, multimodal and agentic matrices; model cards record tasks, knowledge limits and intended use | RA-001, RA-002, DE-001 | [Risk Matrix](../risk-classification/risk-matrix.md), [Multimodal Risk Matrix](../risk-classification/multimodal-risk-matrix.md), [Agentic AI Risk](../risk-classification/agentic-ai-risk.md) |
| MAP 3 | Capabilities, targeted usage, goals, and expected benefits and costs are understood against benchmarks | Model selection compares candidates on evaluation results, cost and fit; open-source versus API decision framework; cost governance; human oversight processes defined per pattern (MAP 3.5) | AR-004, PM-003, PM-005 | [Model Selection](../llm-lifecycle/model-selection.md), [Cost Governance](../operating-model/cost-governance.md), [Supply Chain Security](../ai-security/supply-chain-security.md#decision-framework-open-source-vs-commercial-api) |
| MAP 4 | Risks and benefits are mapped for all components, including third-party software and data | Dimension scoring in the risk assessment; architecture document with data flows; third-party model risk categories; AI-BOM lists every model, framework and guardrail component | RA-001, AR-001, AR-005, SR-004 | [Assessment Template](../risk-classification/assessment-template.yaml), [Third-Party Model Risk](third-party-model-risk.md), [Supply Chain Security](../ai-security/supply-chain-security.md) |
| MAP 5 | Impacts to individuals, groups, communities, organizations and society are characterized | Impact assessment; DPIA; bias evaluation; material incident criteria. Broader community and societal impact is less developed than impact on direct users | RA-003, RA-005, EV-005 | [Impact Assessment](../../templates/impact-assessment-template.md), [Bias Detection](../responsible-ai/bias-detection-llm.md) |

---

## MEASURE Function Mapping

| NIST Category | Category (abridged) | Framework Implementation | Controls | Reference |
|--------------|-------------|-------------------|----------|-----------|
| MEASURE 1 | Appropriate methods and metrics are identified and applied | Tiered evaluation thresholds; metric definitions; validation independence by tier; eval dataset integrity; LLM-as-judge calibration | EV-001, EV-006, EV-007, RV-003 | [Evaluation Governance](../llm-lifecycle/evaluation-governance.md), [Validation](../model-lifecycle/validation.md) |
| MEASURE 2 | AI systems are evaluated for trustworthy characteristics | Validity and reliability (validation, evaluation suites, hallucination policy); safety (safety evaluation); security and resilience (red-teaming, adversarial defenses); explainability (transparency standards); privacy (DPIA, PII testing); fairness (bias evaluation). Environmental impact (MEASURE 2.12) is not assessed | EV-001 to EV-005, EV-008, EV-009, SR-001 to SR-003, RA-005. Environmental impact: No control yet (gap) | [Validation](../model-lifecycle/validation.md), [Hallucination Policy](../responsible-ai/hallucination-policy.md), [Adversarial Robustness](../ai-security/adversarial-robustness.md), [Bias Detection](../responsible-ai/bias-detection-llm.md) |
| MEASURE 3 | Mechanisms for tracking identified AI risks over time are in place | Production monitoring and alerting per tier; drift detection; production evaluation cadence; formal reviews with re-tiering. End-user appeal (MEASURE 3.3) exists only as the route to human review on request for T1 automated outcomes | PM-001, PM-002, PM-004, RV-001. Appeal process: No control yet (gap) | [LLM Monitoring](../llm-lifecycle/monitoring.md), [ML Monitoring](../model-lifecycle/monitoring.md), [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) |
| MEASURE 4 | Feedback about the efficacy of measurement is gathered and assessed | Automated judges calibrated against human evaluators; user feedback signals (ratings, escalation and regeneration rates); reviewer override rate; governance metrics anti-patterns | EV-007, PM-004, RV-001 | [Evaluation Governance](../llm-lifecycle/evaluation-governance.md#llm-as-judge-calibration), [LLM Monitoring](../llm-lifecycle/monitoring.md), [Governance Metrics](../operating-model/governance-metrics.md) |

---

## MANAGE Function Mapping

| NIST Category | Category (abridged) | Framework Implementation | Controls | Reference |
|--------------|-------------|-------------------|----------|-----------|
| MANAGE 1 | Risks from MAP and MEASURE are prioritized, responded to and managed | Deployment gates decide whether a system proceeds; tiered sign-off; red-team findings must be resolved; residual risk is accepted only through the exception process, with every exception in a register reviewed monthly | DA-001, DA-002, DA-003, SR-002, GV-004 | [Deployment Gates](../llm-lifecycle/deployment-gates.md), [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance) |
| MANAGE 2 | Strategies to maximize benefits and minimize negative impacts are planned, implemented and documented | Guardrails; human oversight patterns with a tested kill switch; rollback plans; incident playbooks for previously unknown risks; deprecation and migration governance (supersede or deactivate, MANAGE 2.4) | DE-004, PM-003, DA-004, IR-001, DR-001, DR-002 | [Human-in-the-Loop Patterns](../responsible-ai/human-in-loop-patterns.md), [Model Deprecation](../llm-lifecycle/model-deprecation-governance.md), [Multi-Agent Governance](../llm-lifecycle/multi-agent-governance.md) |
| MANAGE 3 | AI risks and benefits from third-party entities are managed | Ongoing vendor monitoring (behaviour canary, changelog review, annual reassessment); revalidation and red-teaming on provider updates; pre-trained and open-source models re-checked on model change (MANAGE 3.2) | AR-005, SR-004, RV-003, PM-004 | [Third-Party Model Risk](third-party-model-risk.md#ongoing-monitoring), [Supply Chain Security](../ai-security/supply-chain-security.md), [Red-Teaming Protocol](../ai-security/red-teaming-protocol.md#mandatory-testing-events) |
| MANAGE 4 | Risk treatments, including response, recovery and communication plans, are documented and monitored | Post-deployment monitoring plans; incident severity, SLAs and post-mortems; remediation tracking; regulatory notification; board and between-quarter reporting | PM-001, PM-002, IR-001 to IR-005 | [Escalation Paths](../operating-model/escalation-paths.md), [Incident Forensics](../operating-model/incident-forensics.md), [Board Reporting](../operating-model/board-reporting.md) |

---

## AI RMF Profiles

The AI RMF defines use-case profiles, temporal profiles (a Current Profile and a Target Profile) and cross-sectoral profiles. It does not define implementation tiers, unlike the NIST Cybersecurity Framework. The framework's risk tiers (T1-T4) are a risk classification, not AI RMF tiers.

| NIST Concept | Framework Equivalent |
|-------------|---------------------|
| Current Profile | Controls in place for each AI system, evidenced against the control register |
| Target Profile | Controls the register requires for the system's tier |
| Gap analysis | Difference between the two, recorded at each formal review (RV-001) |
| Prioritization | Highest-risk systems first (T1, then T2, T3, T4) |

---

## Generative AI Profile (NIST AI 600-1)

NIST released NIST AI 600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, on 26 July 2024. It is a cross-sectoral profile of AI RMF 1.0. It lists 12 risks that are unique to or made worse by generative AI and suggests actions organized under the AI RMF functions.

| GAI Risk (NIST AI 600-1) | Framework Coverage | Controls |
|------------------|-------------------|----------|
| CBRN Information or Capabilities | General safety evaluation and harmful-content red-teaming; no CBRN-specific test set | EV-002, SR-001 (CBRN-specific testing: No control yet (gap)) |
| Confabulation | [Hallucination policy](../responsible-ai/hallucination-policy.md), faithfulness metrics, RAG retrieval quality | EV-001, EV-004, PM-004 |
| Dangerous, Violent, or Hateful Content | Safety evaluation, guardrails, harmful content red-teaming, safety monitoring | EV-002, DE-004, SR-001 |
| Data Privacy | DPIA, data residency, PII detection on outputs, privacy attack defenses | RA-005, AR-003, SR-003 |
| Environmental Impacts | Not covered. [Cost governance](../operating-model/cost-governance.md) tracks spend, not energy or emissions | No control yet (gap) |
| Harmful Bias or Homogenization | [Bias detection](../responsible-ai/bias-detection-llm.md) and counterfactual testing | EV-005 |
| Human-AI Configuration | [Human-in-the-loop patterns](../responsible-ai/human-in-loop-patterns.md), reviewer override-rate monitoring, AI disclosure | PM-003 |
| Information Integrity | Content labeling in [transparency standards](../responsible-ai/transparency-standards.md), synthetic media labeling in [multimodal governance](../llm-lifecycle/multimodal-governance.md) | No register control (partial) |
| Information Security | [Adversarial robustness](../ai-security/adversarial-robustness.md), [red-teaming](../ai-security/red-teaming-protocol.md) | SR-001, SR-002, SR-003, DE-004 |
| Intellectual Property | License review, vendor IP and copyright assessment, copyright similarity checks for generated imagery | AR-004, AR-005, SR-004 |
| Obscene, Degrading, and/or Abusive Content | CSAM classifiers and prohibited uses in [multimodal governance](../llm-lifecycle/multimodal-governance.md), safety evaluation | EV-002, DE-004 |
| Value Chain and Component Integration | [Third-party model risk](third-party-model-risk.md), [supply chain security](../ai-security/supply-chain-security.md), AI-BOM | AR-005, SR-004, DE-005 |

---

## Related NIST Work

| Item | Status (November 2026) | Where it touches this framework |
|------|----------------------|--------------------------------|
| AI RMF revision | NIST says AI RMF 1.0 is being revised as part of the White House AI Action Plan | Re-check this mapping when a revision is published |
| AI RMF Profile on Trustworthy AI in Critical Infrastructure | Concept note released 7 April 2026 | Relevant where AI supports critical infrastructure operations |
| Cyber AI Profile (NIST IR 8596) | Initial preliminary draft, 16 December 2025; comments closed 30 January 2026. Organized around Cybersecurity Framework 2.0 outcomes | [ai-security/](../ai-security/) |
| SP 800-53 control overlays for AI (COSAiS, renamed COSIS in October 2026) | Concept paper 14 August 2025; annotated outline for using and fine-tuning predictive AI, 8 January 2026. No public draft overlay yet. Proposed use cases include generative AI, predictive AI, single-agent and multi-agent systems, and AI developers | [Adversarial Robustness](../ai-security/adversarial-robustness.md), [Supply Chain Security](../ai-security/supply-chain-security.md) |
| CAISI AI Agent Standards Initiative | Announced 17 February 2026 by NIST's Center for AI Standards and Innovation. Three pillars: industry-led agent standards, open-source agent protocols, and research on agent security and identity | [Agentic AI Risk](../risk-classification/agentic-ai-risk.md), [Multi-Agent Governance](../llm-lifecycle/multi-agent-governance.md) |
| NCCoE concept paper: Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization | Published 5 February 2026; comments closed 2 April 2026. Scopes a potential NCCoE project on applying identity standards to AI agents | Agent identity and authorization: AR-006 and the [agent identity and tool governance](../llm-lifecycle/agent-identity-and-tool-governance.md) standard |

---

## Gaps and Recommendations

| NIST Area | Current Coverage | Recommendation |
|-----------|-----------------|----------------|
| GOVERN 3.1: Diverse teams | Committee is multi-disciplinary; no diversity requirement | Set expectations for team composition in T1 risk decisions |
| GOVERN 5.1 and MAP 5: External feedback and societal impact | Impact assessment covers direct stakeholders | Add a process for feedback from affected communities, and societal impact for T1 systems |
| MEASURE 2.12: Environmental impact | Not covered | Track energy use for training, fine-tuning and inference of T1/T2 systems |
| MEASURE 3.3 and MANAGE 4.1: Appeal | Route to human review on request for T1 automated outcomes | Define an appeal process for people affected by AI outcomes |
| NIST AI 600-1: CBRN | Covered only by general safety testing | Add CBRN test cases to safety evaluation for open-ended generative systems |
| Agent identity and authorization | Privilege boundaries in multi-agent governance | Track CAISI and NCCoE outputs; add a control when they mature |

---

## Implementation Notes

- The AI RMF is voluntary. The same framework controls can serve both AI RMF alignment and EU AI Act obligations; see [eu-ai-act-mapping.md](eu-ai-act-mapping.md).
- Use the AI RMF Playbook for subcategory-level actions, and NIST AI 600-1 for generative AI actions.

---

## Sources

- NIST, AI Risk Management Framework (page with release date, revision status and Critical Infrastructure Profile note): https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 100-1, Artificial Intelligence Risk Management Framework (AI RMF 1.0): https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- NIST AIRC, AI RMF Core (categories): https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST AIRC, AI RMF Profiles: https://airc.nist.gov/airmf-resources/airmf/6-sec-profile/
- NIST AIRC, AI RMF Playbook: https://airc.nist.gov/airmf-resources/playbook/
- NIST AI 600-1, Generative Artificial Intelligence Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- NIST CSRC, NIST IR 8596 Cyber AI Profile (initial preliminary draft): https://csrc.nist.gov/pubs/ir/8596/iprd
- NIST CSRC, SP 800-53 Control Overlays project (COSIS, formerly COSAiS): https://csrc.nist.gov/projects/cosais
- NIST, Announcing the AI Agent Standards Initiative: https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure
- NIST CSRC, Concept paper: Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization: https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd
