# AI Inventory Standard

## Purpose

The AI inventory is the record of every AI system and material AI feature the organisation builds, buys or uses. Every other control starts from it. A system nobody has recorded cannot be tiered, reviewed, monitored or retired, and it will not appear in the board report.

This standard sets what goes in the inventory, the fields each entry carries, who owns it, how entries are created and kept current, how the inventory is reconciled against what is actually running, and how it feeds board reporting.

| Item | Where |
|---|---|
| Register controls | RA-006 (system registered before development), GV-006 (inventory complete and reconciled quarterly) |
| Entry template | [ai-inventory-entry.yaml](../../templates/ai-inventory-entry.yaml) |
| Machine-readable schema | [inventory-entry.schema.json](../../schemas/inventory-entry.schema.json) |
| Public or regulator-facing view | [AI system inventory](../responsible-ai/transparency-standards.md#ai-system-inventory) in the transparency standards, which is a subset of these fields |

---

## What Goes in the Inventory

### AI systems

Register every AI system. Where the EU AI Act applies, use its definition of an AI system (Art. 3(1)). Elsewhere, and as the framework default everywhere, register anything that:

- uses a machine learning model, a foundation model (language, image, speech or multimodal) or a statistical model trained or calibrated on data to produce predictions, classifications, content, recommendations or decisions; and
- is used in, or to support, business operations, customer interactions, decisions about people, or regulatory and financial reporting.

This covers systems built in-house, systems built on a vendor's model, vendor products bought for a purpose, pilots and proofs of concept that touch real data, and agents of every kind. Deterministic rules and scripts with no trained model are out of scope unless they call a model or their rules were derived from one.

Where a model is also in the model risk inventory, keep one inventory entry per AI system and record the model risk inventory ID in it. Model risk management keeps its own inventory for its own purposes; the two are reconciled each quarter.

### Material AI features in bought products

An AI capability inside a product the organisation already uses (a productivity suite, CRM, HR platform, service desk, developer tool or other SaaS) is registered as a **material AI feature** when any of these is true:

1. It processes Confidential data, personal data, MNPI or regulated data ([data classes](../compliance/data-residency-llm.md#residency-requirements-by-data-classification)).
2. Its output reaches customers or other external parties.
3. It makes or directly influences a regulated decision or a decision about an employee (recruitment, promotion, performance, termination).
4. It can take actions in other systems, such as sending messages, changing records or calling tools.
5. It generates code that goes into production systems.
6. It is enabled for a whole business unit or the whole organisation.

Register at the level of the feature in the tenant, not per user: one entry for the assistant in the productivity suite, not one per licence. A feature that meets criterion 3 or 4 also goes through the [governance workflow](governance-workflow.md) as an AI system, and the [override list](../risk-classification/genai-risk-matrix.md#tier-override-rules) applies to it like any other system.

AI features that meet none of the criteria are covered by the [acceptable use standard](../operating-model/acceptable-use.md) and the approved tools list, not by individual entries.

When in doubt, register. An entry costs little. An unrecorded system cannot be governed.

---

## Required Fields

Field names match the [template](../../templates/ai-inventory-entry.yaml) and the [schema](../../schemas/inventory-entry.schema.json).

| Field | What to record | Set at | Kept current by |
|---|---|---|---|
| `system_id` | Unique, stable identifier. Never reused, even after retirement | Intake | AI Risk (issues IDs) |
| `name`, `purpose`, `business_unit` | What the system does and for whom | Intake | Product owner, then system owner |
| `entry_type`, `host_product` | AI system or material AI feature; the product a feature sits in | Intake or reconciliation | Product owner |
| `owners` | Exactly one business owner, one product owner and one AI lead ([accountability principles](../operating-model/roles-responsibilities.md#accountability-principles)); system owner and technical owner once named | Intake | Product owner, then system owner |
| `deployment_status` | proposed, in-development, pilot, production, deprecated, retired or rejected | Intake; each stage gate | Product owner, then system owner |
| `risk_tier`, `tier_basis` | Tier and the dimension or override item that set it; `pending` until the Stage 2 approval (RA-004); `not-tiered` only for a use rejected at the [Step 0 screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen) | Stage 2 | System owner at each re-tiering check |
| `characteristics` | ml, genai, rag, agentic, fine-tuned, external-model, open-source, personal-data, external-data-flow, customer-facing. These are the values the control register uses to decide which controls apply | Stage 2 | Product owner or system owner on material change |
| `data` | Data classes processed and the regions where data is processed and stored | Stage 2; confirmed at Stage 3 (AR-003) | Technical owner |
| `decision_impact`, `human_oversight` | How outputs are used; the oversight pattern from the [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) | Stage 2; confirmed at deployment | AI lead (from the model card) |
| `eu_ai_act` | Whether the Act applies; the role (provider, deployer or both); whether the system is built on a general-purpose AI model; the Annex III point or `none`; high-risk status; whether Art. 50 transparency duties apply; reference to the RA-008 role record. See [working out the role](../compliance/eu-ai-act-mapping.md#working-out-the-role) | Intake (RA-008) | Compliance on material change |
| `vendor_and_model` | Vendor, hosting model, and each model with provider, identifier, version and role (primary, fallback, embedding, judge) | Stage 3 (AR-004) | AI lead on every model or provider change |
| `dates` | Registered, deployed, last formal review, next formal review, retired | As each event happens | System owner |
| `linked_controls` | Each applicable control with status (evidence exists, evidence missing, not applicable, excepted) and the evidence reference | Stage 2 onward | Product owner, then system owner |
| `exceptions` | Exception IDs from the [exception register](../../templates/exception-register.md) | When an exception is approved | AI Risk (GV-004) |
| `references` | Risk assessment, model card, model risk inventory ID, vendor assessment | As each document is approved | System owner |
| `registration_source` | intake, reconciliation (found by GV-006) or retroactive (registered at framework adoption) | On creation | AI Risk |

An entry in pilot or production must have a tier from T1 to T4, a deployed date and a next review date. The schema enforces these rules.

---

## Ownership

| Role | Responsibility |
|---|---|
| AI Risk (second line) | Owns the inventory as a register: this standard, the field definitions, ID issue, data quality checks, the quarterly reconciliation (GV-006) and inventory reporting |
| Product owner | Creates the entry at intake and keeps it current until production (RA-006) |
| System owner | Keeps the entry current in production: status, dates, tier, linked evidence |
| AI lead | Model and vendor fields and the model card reference (RV-002) |
| Compliance | EU AI Act fields (RA-008) |
| Security | Shadow AI discovery feeds from network, endpoint and SaaS telemetry (GV-003) |
| Model Risk Management | Model risk inventory IDs and the quarterly match between the two inventories |
| Procurement and vendor management | Feed of AI purchases, renewals and vendor notices of new AI features |

Hold the inventory in a system of record with access control and change history, such as the GRC platform ([GRC integration](../operating-model/grc-integration.md)). A spreadsheet is acceptable to start, as long as changes are attributable and the history is kept.

---

## How Entries Are Created

1. **At intake.** The Stage 1 intake form creates the entry with status `proposed` and tier `pending`. RA-006 requires the entry to exist before development begins. The Step 0 screen and the RA-008 role record are recorded against it.
2. **At tiering.** When the Stage 2 assessment is approved (RA-004), the tier, tier basis, characteristics and data classes are set.
3. **From reconciliation.** Anything the quarterly reconciliation finds that has no entry gets one, with `registration_source: reconciliation`, and is routed to intake. A live system found this way follows [Retroactive Governance](governance-workflow.md#retroactive-governance).
4. **At adoption.** Systems already running when the framework is adopted are registered with `registration_source: retroactive` in week 1 ([START-HERE](../../START-HERE.md#minimum-viable-governance-the-first-30-days)).

A use rejected at Step 0 keeps its entry with status `rejected` and tier `not-tiered`. The entry is evidence that the screen ran and stopped it.

---

## How Entries Stay Current

| Event | Fields to update | Who | Control |
|---|---|---|---|
| Stage gate passed | `deployment_status`, `linked_controls` | Product owner | RA-006 |
| Deployment approved | `deployment_status`, `dates.deployed`, `dates.next_review`, model versions | System owner | DA-002 |
| Formal governance review | `dates.last_review`, `dates.next_review`, `risk_tier` after the re-tiering check, `linked_controls` | System owner | RV-001 |
| Model card updated | `vendor_and_model`, `human_oversight`, `references.model_card` | AI lead | RV-002 |
| Material change (model, provider, prompt, scope, data, autonomy, regulation) | `risk_tier`, `characteristics`, `data`, `eu_ai_act` | System owner; Compliance for the Act fields | RV-003, RA-008 |
| Exception approved, renewed or closed | `exceptions`, the control's status in `linked_controls` | AI Risk | GV-004 |
| Deprecation or retirement | `deployment_status`, `dates.retired` | System owner | DR-001, DR-003 |

Retired entries stay in the inventory. Governance records are kept for the life of the system plus the tier period after retirement ([retention periods](../compliance/audit-trail-requirements.md#retention-periods)), so the entry must still be findable.

The next review date follows the tier cadence in [review cadence](../operating-model/review-cadence.md#cadence-by-tier). Overdue reviews are calculated from this field, so a wrong date hides an overdue review.

---

## Quarterly Reconciliation (GV-006)

The inventory says what the organisation believes it runs. Reconciliation checks that against what it pays for, what is enabled, and what traffic shows.

| Source | What to look for | Provided by |
|---|---|---|
| Procurement and accounts payable | Purchases from AI vendors; contracts with AI terms; renewals where the vendor has added AI features; AI subscriptions on expense claims and corporate cards | Procurement, Finance |
| Cloud spend | Model APIs, managed ML platforms and GPU capacity billed to any cloud account | Cloud platform or FinOps |
| SaaS admin consoles | AI features enabled in each tenant; third-party apps granted access to mail, files or chat | Application owners |
| Network and endpoint telemetry | Traffic to AI service endpoints (proxy, secure web gateway, CASB, DNS); desktop AI apps and browser extensions | Security (GV-003) |
| Code repositories | Calls to model APIs and AI SDKs; model files; API keys for AI services | Engineering, Security |
| Model risk inventory | Models with no linked AI inventory entry, and the reverse | Model Risk Management |

Steps:

1. Pull each source for the quarter.
2. Match each item to an inventory entry.
3. For each unmatched item, find an owner. Register it and route it to intake, or switch it off. Framework default: resolved within 30 days. If the item meets an automatic T1 override (for example customer-facing output without per-output review, or customer personal data sent to an external model without all four safeguards), report it to the AI Risk Committee chair at once rather than waiting for the quarter.
4. Check the reverse: an entry in production with no spend, no traffic and no users may be retired in practice. Confirm, then run the Stage 10 controls.
5. Record the result: items found, items matched, entries created, items switched off, items still open. Present it to the quarterly full-portfolio meeting of the AI Risk Committee.

---

## Board Reporting

The inventory is the single source for the portfolio numbers the committee and the board see. Do not keep a second count.

| Output | Fields used | Where it goes |
|---|---|---|
| System count by tier, new deployments, retirements | `risk_tier`, `deployment_status`, `dates` | [Portfolio KPIs](../operating-model/governance-metrics.md#portfolio-kpis); [board report section 2](../operating-model/board-reporting.md#2-portfolio-overview) |
| Vendor concentration | `vendor_and_model` for T1 and T2 systems | [Board report section 3](../operating-model/board-reporting.md#3-risk-concentration) |
| Risk assessment coverage and overdue reviews | `linked_controls`, `dates.next_review` | [Governance Health KPIs](../operating-model/governance-metrics.md#governance-health-kpis) |
| Active exceptions by tier | `exceptions` | Policy exception count KPI |
| Current inventory summary by tier, and the reconciliation result | All | [Quarterly full-portfolio meeting](../operating-model/review-cadence.md#monthly-ai-risk-committee) |
| Systems in scope of the EU AI Act by role and Annex III point | `eu_ai_act` | Regulatory update section of the board report |

---

## Supervisory Expectations

Several regimes expect an inventory. The table points to where each is described in the framework; the obligations themselves are in the linked mappings.

| Source | Expectation | Framework reference |
|---|---|---|
| NIST AI RMF, GOVERN 1.6 | Mechanisms are in place to inventory AI systems, resourced according to organisational risk priorities | [NIST AI RMF mapping](../compliance/nist-ai-rmf-mapping.md) |
| ISO/IEC 42001 | Documented resources for AI systems (Annex A.4); an AI system inventory is evidence an AIMS audit will ask for | [ISO/IEC 42001 mapping](../compliance/iso-42001-mapping.md) |
| MAS Guidelines on AI Risk Management | An inventory of AI use cases, systems or models | [Singapore profile](../compliance/multi-jurisdictional-guide.md) |
| OSFI Guideline E-23 | An enterprise model inventory that includes AI and ML models | [Canada profile](../compliance/multi-jurisdictional-guide.md) |
| CBUAE AI guidance note | An AI model inventory under the CBUAE Model Management Standards | [UAE profile](../compliance/multi-jurisdictional-guide.md) |
| EU AI Act | No general inventory duty, but the role, high-risk classification and Art. 50 duties are set per system, so a per-system record is the practical way to show which obligations apply | [EU AI Act mapping](../compliance/eu-ai-act-mapping.md) |
