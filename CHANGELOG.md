# Changelog

## Versioning and Control IDs

Releases follow semantic versioning. A major version changes control IDs, tier rules or thresholds in ways that change what an adopter must evidence. A minor version adds controls, documents or mappings. A patch fixes errors without changing requirements.

Control IDs are stable. A retired control keeps its ID, is marked retired in `controls/`, and the ID is never reused. Each release lists added, changed and retired control IDs.

Regulatory documents carry a "Status as of" line. CI warns when one is older than 90 days and fails after 180 days.

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
