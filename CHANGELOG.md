# Changelog

## Versioning and Control IDs

Releases follow semantic versioning. A major version changes control IDs, tier rules or thresholds in ways that change what an adopter must evidence. A minor version adds controls, documents or mappings. A patch fixes errors without changing requirements.

Control IDs are stable. A retired control keeps its ID, is marked retired in `controls/`, and the ID is never reused. Each release lists added, changed and retired control IDs.

Regulatory documents carry a "Status as of" line. CI warns when one is older than 90 days and fails after 180 days.

## 2.3.0 (13 November 2026)

This release fixes how prompt injection exposure is scored.

### Changed
- **Prompt injection susceptibility** in the [GenAI risk matrix](framework/risk-classification/genai-risk-matrix.md#dimension-3-prompt-injection-susceptibility) now counts every channel that puts text in front of the model. Low used to read "No user input; fully automated prompts" with batch summarization as the example, but uploaded files, emails, retrieved documents, web pages and tool results can carry instructions as well. A pipeline that reads untrusted content now scores at least Medium. Low is kept for pipelines whose every input is trusted internal content.
- **Document summarization example:** prompt injection susceptibility moves from Low to Medium, because its input is uploaded documents. The aggregate score moves from 11 to 12. The tier stays T2, since the highest dimension sets the tier.

No control IDs were added, changed or retired.

## 2.2.0 (11 November 2026)

This release adds one control and fixes places where two documents disagreed.

### Added
- **PM-008, Fallback model switch tested.** The quarterly fallback test for T1 systems using external models was required in [third-party model risk](framework/compliance/third-party-model-risk.md#fallback-architecture) but had no control and no evidence. It now has both.
- **Policy on a Page** at the front of the [AI policy template](templates/ai-policy.md): six commitments, each with an owner and how a breach would show.
- **Use case assessment rows** to record how a vendor API earned a Medium on third-party model dependency: the business owner's outage statement, or the tested fallback's vendor and dates.

### Changed
- **Exit strategy** is now also required at any tier when the use case supports a critical or important function under DORA Art. 28(8). Before, only T1 and T2 needed one, so a T3 system with a tested fallback could support such a function with no exit strategy.
- **Risk appetite:** [board reporting](framework/operating-model/board-reporting.md) now says the AI Risk Committee endorses the statement, matching the committee charter, the policy template and the review cadence. It used to say the CTO and CRO.
- **RA-006:** the inventory entry is opened at intake (Stage 1) and evidenced at Stage 2. The workflow, control register and inventory standard now say the same thing.
- **Step 0 screen:** recorded under RA-007 everywhere. The use case assessment, when to say no and the fast-lane pack used to cite RA-001.
- **Agent identity record:** written and approved at Stage 3 (AR-006), with the identity issued at deployment. One row used to say the identity was created at deployment, after the review that checks it.
- **Model selection:** the fallback must be served by a different vendor, or self-hosted. "A different provider" allowed two models on one vendor's platform.
- **Document summarization example:** the fallback is Claude Sonnet 4.5 on Vertex AI throughout. Six lines still called it the Anthropic API.
- **EU AI Act mapping:** the Art. 16 row now lists registration (Art. 49) among the gaps.
- **README:** the ISO/IEC 42001 and DORA rows match their mappings, and the opening is in plainer words.

### Why this is a minor version
It adds a control and widens one requirement (the DORA exit strategy). No control ID, tier rule or threshold changes.

### Retired
- No control IDs retired. Added: PM-008. Changed: none.

## 2.1.0 (11 November 2026)

This release fixes how the GenAI risk matrix scores dependency on a vendor-hosted model.

### Changed
- **Third-party model dependency (GenAI Dimension 5)** now grades a vendor API by how much the process relies on the vendor, not only by where the model runs, so a vendor-API system can score Medium. In 2.0.0 only a self-hosted model could score Medium, which put every vendor-API GenAI system at T2 or above and kept it out of the T3/T4 fast lane. A vendor API now scores Medium in either of two cases:
  - the process is internal and not business-critical, and the business owner records in the risk assessment that an outage is tolerable and names the degraded fallback;
  - it has a tested fallback: one served by a different vendor or self-hosted, run through the system's evaluation suite at the tier's thresholds, and with the switch exercised.

  A vendor API that meets neither scores High. Critical needs a customer-facing or business-critical process with no fallback of any kind. The level text now defines customer-facing, business-critical, degraded fallback, tested fallback and outage tolerance. It also closes a gap in the 2.0.0 text, which did not say how to score a customer-facing process with no fallback: it is Critical, as the 2.0.0 example (core customer service on one vendor's API) already implied.
- **Worked examples:** the recorded Dimension 5 scores now match the level text. Document summarization is corrected from Medium to High, and its aggregate from 10 to 11, because its fallback has no recorded switch exercise and so is not a tested fallback. Its tier stays T2. The chatbot, the agentic assistant and internal knowledge search keep their scores, and their rationales now name the clause each meets.
- **Restatements aligned** with the new levels: position 8 in [when to say no](framework/governance-operations/when-to-say-no.md#8-no-business-critical-process-on-a-model-you-cannot-replace) and the fallback architecture in [third-party model risk](framework/compliance/third-party-model-risk.md#fallback-architecture).

### Why this is a minor version
Under the policy above, a major version changes tier rules in ways that change what an adopter must evidence. This change relaxes the rule: a vendor-API system can now score Medium if it records outage tolerance or a tested fallback. No evidence an adopter produced under 2.0.0 becomes insufficient. The T1 and T2 requirements for a validated fallback model and a documented exit strategy are unchanged. One worked example's Dimension 5 score is corrected to High, with no tier change.

### Retired
- No control IDs retired. None added or changed.

## 2.0.0 (November 2026)

This release turns the framework from a set of consistent-looking documents into one system with a single source for every rule, checks that enforce it, and regulatory content updated to November 2026.

### Added
- **Machine-readable controls and policy.** `controls/` holds every control as YAML with owner, evidence, frequency, escalation, control type, automation level, key-control flag, the test an auditor runs and the docs that define it. `policy/` holds roles, tier parameters, evaluation thresholds and pass rules, and incident severity. `schemas/` validates them and the model cards. 23 Markdown tables are generated from this YAML.
- **CI checks** (`tools/check.py`, `.github/workflows/validate.yml`): schemas, control references, links and anchors, generated-table drift, example conformance, statistical pass rule on example evaluations, and staleness of regulatory status lines.
- **Statistical pass rule.** T1/T2 metrics pass on the one-sided 95% confidence bound, T3/T4 on the point estimate. T1 suites are 300+ cases, the smallest size at which zero failures demonstrates a 1% cap. Regression, segment and human evaluation rules; agent evaluation; guardrail evaluation.
- **New controls (22):**
  - Programme: GV-001 AI policy, GV-002 AI literacy, GV-003 acceptable use, GV-004 exception register, GV-005 committee charter, GV-006 inventory reconciliation.
  - Risk assessment: RA-006 inventory registration, RA-007 prohibited-use screen, RA-008 EU AI Act role, RA-009 fundamental rights impact assessment.
  - Architecture: AR-006 agent identity, tool and permission review; AR-007 AI vendor contract clauses and DORA register of information.
  - Development: DE-006 AI interaction disclosure, DE-007 content marking and labelling, DE-008 retrieval permissions, DE-009 decision notices.
  - Evaluation: EV-008 agent evaluation, EV-009 guardrail evaluation.
  - Operations: PM-006 kill switch testing, PM-007 audit logging, IR-006 regulatory incident notification.
  - Review: RV-005 explanation and human review for adverse outcomes.
- **New documents:** START-HERE guide with reading paths, a 30-day plan and a six-week path; when to say no; agent identity and tool governance; AI procurement clauses; AI inventory; AI literacy; acceptable use of AI tools; fast lane for T3/T4 and small-team rules in the workflow; exceptions and risk acceptance process.
- **New templates:** AI policy, AI Risk Committee charter, exception register, AI inventory entry, fundamental rights impact assessment section.
- **Reference implementations:** a governance-gate GitHub Action that checks evidence and evaluation results against the controls and thresholds before deployment, plus ticketing, model registry and audit logging patterns.
- **Jurisdictions:** UK, South Korea, China and India profiles; upcoming deadlines table through 2028.
- **Threat taxonomy mapping** to OWASP Top 10 for LLM Applications 2025, OWASP Top 10 for Agentic Applications and MITRE ATLAS.

### Changed
- **Tiering:** the highest-scoring dimension sets the tier across all risk matrices; one canonical override list; approvers may raise a tier, never lower it; customer data through an external LLM API is a T2 floor when zero retention, regional endpoint, DPA and redaction are in place.
- **Human oversight at T1** is risk-based: adverse regulated outcomes need a human in the loop; customer-facing informational systems may run human-over-the-loop with sampled review, routing, scope guardrails, a tested kill switch and hallucination monitoring.
- **Cadence:** formal review quarterly (T1), semi-annual (T2), annual (T3/T4); AI Risk Committee meets monthly.
- **One source** for approvers, RACI, retention (7/5/3/1 years for interaction logs; life of system plus tier period for governance records), incident severity and the alert-to-severity mapping.
- **Control register** stages now match the workflow; Applies To names tiers.
- **EU AI Act:** one mapping organised by role, with dates as amended by Regulation (EU) 2026/1744 (Annex III high-risk from 2 December 2027, Annex I from 2 August 2028; Art. 50 from 2 August 2026).
- **US model risk:** SR 26-2 replaces SR 11-7 throughout. SR 26-2 excludes generative and agentic AI, so the framework's GenAI and agentic controls stand on their own.
- **NIST AI RMF** categories and **ISO/IEC 42001** Annex A titles corrected and mapped to control IDs.
- **Worked examples** rebuilt to follow the framework: the T1 chatbot case file, fraud detection (now T1), credit scoring, document summarization, the agentic assistant (with a recorded exception) and internal knowledge search.
- Duplicated content consolidated; em dashes removed.

### Retired
- No control IDs retired.
- `framework/compliance/eu-ai-act-genai-mapping.md` merged into `eu-ai-act-mapping.md`.
- `framework/compliance/data-residency-llm.md` merged into `cross-border-data-governance.md` (stub kept for old links).

## March 2026 update

- AI security: red-teaming protocol, adversarial robustness, supply chain security.
- Regulatory breadth: NIST AI RMF and ISO/IEC 42001 mappings, multi-jurisdictional guide, regulatory change monitoring, cross-border data governance.
- Frontier AI: multimodal risk and governance, multi-agent governance, open-source model governance, model deprecation governance.
- Enterprise operations: board reporting, governance metrics, cost governance, GRC integration, incident forensics.
- Governance operations: control register (48 controls), end-to-end governance workflow, evaluation governance, T1 governance case file.
- Templates: board risk report, red-team report. Example: T3 internal knowledge search.

## 2024 to early 2026

Initial framework for traditional ML in regulated industries: risk classification, model lifecycle standards (development, validation, deployment, monitoring), EU AI Act mapping, audit trail, responsible AI checklist, roles, review cadence, escalation paths, templates and worked examples (credit scoring, fraud detection). GenAI and LLM governance added in March 2026.
