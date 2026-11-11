# When to Say No

## Purpose

Most of this framework is about making an AI system safe enough to run. This standard covers the cases where the right answer is that GenAI, an agent or an external model API is the wrong tool. Saying no at intake costs a conversation. Saying no at the deployment gate costs the build.

Each position below gives the rule, why it holds, what to do instead, and which control or document enforces it.

## How It Fits the Workflow

- **When:** at [Stage 1](governance-workflow.md#stage-1-idea-intake) and [Stage 2](governance-workflow.md#stage-2-risk-assessment--tiering). The Product owner answers the questions in section 0 of the [GenAI use case assessment](../../templates/genai-use-case-assessment.md) before scoring the risk dimensions. The tier approver reviews the answers when approving the risk assessment (RA-004). At Stage 3, the architecture review (T1), the design review (T2) or the technical owner's architecture document (T3/T4) checks positions 3, 4 and 8 against the actual design.
- **What it changes:** no tier, threshold, approver, cadence or retention period. Positions 1, 4, 5 and 7 go further than the controls they rest on, and each says so. The approver applies them and records the decision in the risk assessment approval.
- **Disagreement:** a team that thinks a position should not apply takes its reasoning to the tier approver, who decides and records the decision. Positions that rest on a non-waivable control (position 6, and the kill switch in position 3) cannot be set aside. See [Exceptions and Risk Acceptance](governance-workflow.md#exceptions-and-risk-acceptance).

## Summary

| # | Position | Enforced by |
|---|----------|-------------|
| 1 | [Figures with legal or contractual effect come from a system of record](#1-figures-with-legal-or-contractual-effect-come-from-a-system-of-record) | EV-001, DE-004, hallucination policy, pattern selection matrix |
| 2 | [GenAI never makes an adverse regulated decision on its own](#2-genai-never-makes-an-adverse-regulated-decision-on-its-own) | Override item 1, RA-002, PM-003 |
| 3 | [No autonomous write that cannot be undone or capped](#3-no-autonomous-write-that-cannot-be-undone-or-capped) | Override item 4, agentic pre-deployment requirements, DA-004, kill switch |
| 4 | [No external model API without evidenced residency and zero retention](#4-no-external-model-api-without-evidenced-residency-and-zero-retention) | AR-003, AR-005, RA-005, override items 3 and 8 |
| 5 | [No launch when the evaluation cannot show the threshold is met](#5-no-launch-when-the-evaluation-cannot-show-the-threshold-is-met) | EV-001 to EV-009, statistical pass rule, release criteria, independent validation |
| 6 | [Prohibited practices are rejected at Step 0](#6-prohibited-practices-are-rejected-at-step-0) | RA-001, non-waivable list |
| 7 | [No GenAI where a simpler method meets the need](#7-no-genai-where-a-simpler-method-meets-the-need) | Business justification, AR-004, validation |
| 8 | [No business-critical process on a model you cannot replace](#8-no-business-critical-process-on-a-model-you-cannot-replace) | AR-004, AR-005, exit strategy requirements |

---

## 1. Figures With Legal or Contractual Effect Come From a System of Record

**Rule.** A language model never generates a fee, interest rate, charge, balance, limit, eligibility outcome, or regulatory or reported figure. The value comes from the system of record. GenAI may fetch it through a tool or API call, and code places it into the response. The model explains the figure; it does not produce or retype it.

**Why.** Hallucination can be managed but not eliminated ([hallucination policy](../responsible-ai/hallucination-policy.md)). The framework treats facts, figures, policy terms, fees, dates and eligibility as material claims ([metric definitions](../llm-lifecycle/evaluation-governance.md#metric-definitions)). Even the T1 cap of ≤ 1% allows some wrong answers. On a high-volume customer channel, that means a steady stream of misquoted fees. Each one is a potential complaint or conduct issue. Regulatory reporting and disclosure carry a zero tolerance, with a qualified human verifying every output ([use-case overrides](../responsible-ai/hallucination-policy.md#use-case-specific-overrides)). A figure computed by a model also breaks the traceable data lineage expected for risk reporting under BCBS 239 ([data residency compliance mapping](../compliance/cross-border-data-governance.md#compliance-mapping)). The hallucination policy sets tolerances; this position goes further and keeps these figures out of generation altogether.

**Instead.**
- Look the value up deterministically, insert it with code, and let the model explain what it means.
- Cross-verify factual claims against structured data. This is required for T1 factual claims ([tier-specific mitigations](../responsible-ai/hallucination-policy.md#tier-specific-mitigations)).
- Route fee and pricing disputes to a human (safeguard b in the [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix)).

**Enforced by.** Domain accuracy defined in the risk assessment and tested in pre-release evaluation (EV-001); guardrails (DE-004); output scope guardrails and risk-based routing in the pattern selection matrix; human verification of regulatory output under the hallucination policy.

## 2. GenAI Never Makes an Adverse Regulated Decision on Its Own

**Rule.** No GenAI system is the sole decision maker for an adverse or non-standard regulated outcome: a credit decline, adverse pricing, an account restriction, an AML or sanctions disposition, an underwriting decision or an employment decision. A qualified human makes that decision and owns it.

**Why.** These decisions are automatic T1 under override item 1 ([override rules](../risk-classification/genai-risk-matrix.md#tier-override-rules)). The [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) requires Pattern 1, a human review before the outcome takes effect, for adverse or non-standard outcomes, in line with GDPR Art. 22. Creditworthiness assessment and life and health insurance pricing are high-risk under Annex III of the EU AI Act from 2 December 2027, with a right to an explanation for affected people (Art. 86; see the [EU AI Act mapping](../compliance/eu-ai-act-mapping.md#how-the-acts-categories-relate-to-framework-tiers)). A free-text generator is hard to validate for conceptual soundness and hard to explain decision by decision ([validation scope](../model-lifecycle/validation.md#validation-scope)).

**Instead.**
- Use GenAI around the decision: summarise the file, extract information for a validated decision model, draft the letter that the human decision maker approves.
- Where the law permits automating favourable outcomes within approved policy (with a route to human review on request), let a validated model or rule set make that call, with GenAI limited to drafting and explanation.

**Enforced by.** Override item 1 and the override decision (RA-002); human oversight (PM-003); [reviewer qualifications](../responsible-ai/human-in-loop-patterns.md#reviewer-requirements).

## 3. No Autonomous Write That Cannot Be Undone or Capped

**Rule.** An agent may take a write action on its own only when the action can be reversed and is both rate-limited and capped in scope. If an action cannot be undone, such as a payment, an outbound customer message, a deletion or an access change, the agent proposes it and a human confirms before it executes. If an action cannot be rate-limited and capped, the agent does not get it.

**Why.** The agentic standard requires a defined undo path for every action, rate limits per time window, blast radius limits, and confirmation gates for irreversible or high-impact actions ([uncontrolled action execution](../risk-classification/agentic-ai-risk.md#1-uncontrolled-action-execution), [cascading failure](../risk-classification/agentic-ai-risk.md#5-cascading-failure-and-feedback-loops)). Without an undo path or a cap, those controls cannot be evidenced. One misread instruction or injected tool output can then repeat at machine speed until someone pulls the kill switch. Write access to production systems, or authority to move money, communicate with customers or change identity and access, is automatic T1 (override item 4).

**Instead.**
- Stage the write: the agent writes to a pending queue or draft state, and a person or a deterministic service releases it.
- Give the agent read-only tools where the task allows. It is still at least T2 (override item 6), but the failure modes are smaller.
- Cap records per action and actions per session, with budget and time limits ([runtime controls](../risk-classification/agentic-ai-risk.md#runtime-controls)).

**Enforced by.** The action inventory, blast radius assessment and rollback plan in the [agentic pre-deployment requirements](../risk-classification/agentic-ai-risk.md#pre-deployment); rollback tested (DA-004); confirmation gates in [HITL for agentic AI](../responsible-ai/human-in-loop-patterns.md#hitl-for-agentic-ai); a kill switch for every agentic system (non-waivable); agentic red-team tests (SR-001).

## 4. No External Model API Without Evidenced Residency and Zero Retention

**Rule.** Do not send customer personal data or regulated data to an external model API unless the contract and the vendor assessment evidence all of the following: a processing region that meets your residency rules, zero data retention, no training on your data, and a signed DPA. Personal data is also redacted or minimised before the call. MNPI does not go to external APIs at all. A vendor web page or a sales assurance is not evidence.

**Why.** Data residency concerns block deployment at every tier ([Stage 3](governance-workflow.md#stage-3-architecture--design-review)). The [PII override rule](../risk-classification/genai-risk-matrix.md#tier-override-rules) (item 3) makes customer personal data through an external API without all four safeguards (zero retention, a compliant regional endpoint, a signed DPA, redaction or minimisation before the call) automatic T1. This standard is stricter than the override. T1 governance does not repair a data flow you cannot evidence, so fix a missing safeguard before Stage 3 passes instead of absorbing it as T1. The residency standard says MNPI generally cannot use external APIs and requires self-hosting or a private VPC ([residency by data classification](../compliance/cross-border-data-governance.md#residency-requirements-by-data-classification)). DORA requires every ICT services contract, including each model API, to state where data is processed and stored (Art. 30(2)), and some banking secrecy regimes bar customer data from leaving the jurisdiction ([compliance mapping](../compliance/cross-border-data-governance.md#compliance-mapping)).

**An external API is unacceptable when:**
- the data is MNPI;
- the vendor will not commit in the contract to a processing region that meets your residency rules;
- the vendor retains prompts or outputs containing customer personal data or regulated data, or uses them for training, and you cannot evidence otherwise;
- banking secrecy or local law bars customer data from leaving the jurisdiction;
- the data is credit, AML or sanctions data and the legal review the residency standard requires has not cleared it.

**Instead.**
- Self-host an open-weight model under [open-source model governance](../llm-lifecycle/open-source-model-governance.md).
- Use a private endpoint or VPC in the required region.
- Use the redaction pattern, with redaction validated for completeness and residual re-identification risk assessed ([architecture patterns](../compliance/cross-border-data-governance.md#architecture-patterns-and-residency)).
- Minimise the data so it never needs to leave.

**Enforced by.** Data residency confirmation (AR-003, escalates to Compliance); vendor risk assessment (AR-005); DPIA (RA-005); override items 3 and 8 (RA-002); the [vendor assessment checklist](../compliance/cross-border-data-governance.md#vendor-assessment-checklist).

## 5. No Launch When the Evaluation Cannot Show the Threshold Is Met

**Rule.** A system does not launch unless its evaluation can show, on suites of at least the tier size and against an agreed definition of a correct answer, that it meets the tier thresholds. That rules out launching with: no agreed definition of domain accuracy; no labelled data or subject matter experts to judge outputs; a suite below the tier size; an eval set that overlaps the data used to tune prompts; or an uncalibrated LLM judge.

**Why.** Every tier has thresholds, and they are enforced ([threshold definitions](../llm-lifecycle/evaluation-governance.md#threshold-definitions-by-tier)). Domain accuracy is use-case specific and defined in the risk assessment; if nobody can say what a right answer is, nothing can be measured. At T1 and T2 a metric passes on its one-sided 95% confidence bound, not on the point estimate ([statistical pass rule](../llm-lifecycle/evaluation-governance.md#statistical-pass-rule)). For the T1 hallucination cap of 1%, a 300-case suite passes only with zero failing responses, 500 cases allow one and 1,000 allow four. A 200-case suite cannot show the cap at all: even a clean run leaves an upper bound of 1.49%. Results from a contaminated eval set are invalid (EV-006). An LLM judge must be calibrated against human evaluators (EV-007) and is never the sole evaluator for T1 hallucination or PII leakage ([LLM-as-judge calibration](../llm-lifecycle/evaluation-governance.md#llm-as-judge-calibration)).

**Instead.**
- Build the evaluation set first, before the prompts, with the people who own the answers.
- Size the suite for the rate you expect, not the floor, using the [maximum failures table](../llm-lifecycle/evaluation-governance.md#maximum-failures-allowed). At the minimum size, one failure fails the gate.
- If that is out of reach, narrow the scope to something you can measure.

**Relation to exceptions.** A system that misses a threshold can proceed under an approved [exception](governance-workflow.md#exceptions-and-risk-acceptance) with compensating controls. An exception is for a known, measured gap. A system that cannot be measured has no known gap to accept, so this standard asks approvers not to grant one in that case.

**Enforced by.** EV-001 to EV-009; the [statistical pass rule](../llm-lifecycle/evaluation-governance.md#statistical-pass-rule) and [release criteria by tier](../llm-lifecycle/evaluation-governance.md#release-criteria-by-tier); the AI lead's certification at Stage 5; independent validation at T1 and T2.

## 6. Prohibited Practices Are Rejected at Step 0

**Rule.** A use that falls under EU AI Act Art. 5 or the internal prohibited-use policy is rejected before scoring. It is not tiered and it cannot be excepted. A redesign that removes the practice is a new use case and starts again at intake.

**Why.** The [Step 0 prohibited-use screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen) is non-waivable. Banking examples from the [EU AI Act mapping](../compliance/eu-ai-act-mapping.md#prohibited-practices-art-5): manipulative sales or collections journeys, targeting financially vulnerable customers, scoring customers on behaviour unrelated to the product, and inferring the emotions of employees, such as call-centre staff analytics. From 2 December 2026 the list adds systems that generate non-consensual intimate imagery of identifiable people or child sexual abuse material, so check the safeguards of any image or video tool. Recognising customers' emotions from biometric data is outside Art. 5(1)(f), but it is high-risk under the Act and automatic T1 here (override item 5).

**Instead.** Stop. If the business need survives without the practice, redesign and restart at intake.

**Enforced by.** The Step 0 result recorded in the risk assessment (RA-001); the non-waivable list in [Exceptions and Risk Acceptance](governance-workflow.md#exceptions-and-risk-acceptance).

## 7. No GenAI Where a Simpler Method Meets the Need

**Rule.** If search, a rules engine, a form or a conventional model meets the requirement, use it. GenAI has to earn its place against the simplest alternative that works.

**Why.** Every GenAI system brings hallucination, prompt injection and vendor dependency, plus the evaluation, red-team and monitoring cost that comes with them. A deterministic solution brings none of that. The validation standard asks whether model complexity is justified relative to interpretable alternatives ([conceptual soundness](../model-lifecycle/validation.md#1-conceptual-soundness)), but that question gets an independent answer only at T1 and T2, and only after the build. This position asks it of every use case at intake.

**Instead.** In the business justification (section 1 of the [assessment template](../../templates/genai-use-case-assessment.md)), describe the current process and the simplest working alternative, and state what GenAI adds that the alternative cannot.

**Enforced by.** Business justification at intake (Stage 1); model selection rationale (AR-004); conceptual soundness review in T1 and T2 validation.

## 8. No Business-Critical Process on a Model You Cannot Replace

**Rule.** A business-critical process does not depend on a single vendor model without a validated fallback and a documented exit.

**Why.** A business-critical process on one vendor API with no fallback of any kind scores Critical on [third-party model dependency](../risk-classification/genai-risk-matrix.md#dimension-5-third-party-model-dependency), which makes the system T1. With only a degraded fallback, such as a manual process, it scores High. Only a tested fallback, served by a different vendor or self-hosted, evaluated at the tier's thresholds and with the switch exercised, brings it to Medium. T1 and T2 systems need a documented exit strategy with at least one validated alternative, and T1 fallbacks are tested quarterly ([exit strategy requirements](../compliance/third-party-model-risk.md#exit-strategy-requirements)). DORA expects an exit strategy for ICT services that support critical or important functions (Art. 28(8)). Vendors retire models on their own timelines ([model deprecation governance](../llm-lifecycle/model-deprecation-governance.md)).

**Instead.** Design for a fallback served by a second vendor, or a self-hosted fallback, from the start. Keep prompts and eval suites portable, and run the evaluation suite on the fallback and exercise the switch before you need it.

**Enforced by.** Model selection (AR-004) and vendor risk assessment (AR-005); the fallback and exit strategy questions in section 6 of the [assessment template](../../templates/genai-use-case-assessment.md).
