# AI Policy

## Instructions

This is the skeleton of the board-approved AI policy required by control GV-001. The policy is short: it states what the organisation commits to and who decides what, and points to the framework standards for how. Aim for 6 to 10 pages. The first page is the Policy on a Page: publish that page to all staff, and keep the sections behind it for the approver and the auditor. Replace every bracketed item, delete guidance in italics, and keep the section numbers so the policy can be cited.

The policy is drafted by AI Risk, endorsed by the AI Risk Committee, and approved by the board or the Board Risk Committee. It is reviewed at least annually and on a material change in regulation, strategy or risk appetite.

*ISO/IEC 42001 clause 5.2 expects top management to approve an AI policy that fits the organisation's purpose, gives a framework for setting AI objectives, commits to meeting applicable requirements and to continual improvement, and is communicated. Sections 2, 3, 13 and 15 cover these points; Annex A holds the AI management system items an ISO/IEC 42001 audit will look for.*

---

## Document Control

| Field | Value |
|---|---|
| Policy owner | [Chief Risk Officer, as chair of the AI Risk Committee] |
| Drafted by | [Head of AI Risk] |
| Endorsed by | AI Risk Committee, [date] |
| Approved by | [Board / Board Risk Committee], [date] |
| Version | [x.y] |
| Effective date | [date] |
| Next review | [no later than 12 months after approval] |
| Related standards | [Governance workflow](../framework/governance-operations/governance-workflow.md), [control register](../framework/governance-operations/control-register.md), [acceptable use](../framework/operating-model/acceptable-use.md), [AI literacy](../framework/operating-model/ai-literacy.md), [AI inventory](../framework/governance-operations/ai-inventory.md) |

---

## Policy on a Page

*Publish this page to everyone. Each line names an owner and how a breach would show. Keep it to one page.*

| What we commit to | Owner | How a breach shows |
|---|---|---|
| Every AI system is in the AI inventory before development starts, with one named business owner (section 7) | [Head of AI Risk] | An inventory check finds a system with no entry or no owner |
| Every system has a risk tier, and the tier sets who approves it and what it must pass (sections 7 and 8) | [Head of AI Risk] | A system is live without an approved risk assessment |
| Prohibited uses are rejected before tiering, with no exceptions (section 5, Annex B) | [Chief Risk Officer] | A Step 0 screen is missing or failed |
| Staff use only approved AI tools, with the data each tool is approved for (section 10) | [CISO] | Data loss prevention alerts and shadow AI reports |
| A control is missed only through an approved, time-limited exception (section 12) | [Approver for the system's tier] | A gap with no entry in the exception register |
| AI incidents and concerns are reported, and nobody is penalised for raising one (section 13) | [Head of AI Operations] | An incident found by audit that was never reported |

**Owner of this policy:** [name and role]. **Next review:** [date], or sooner on a material change in regulation, strategy or risk appetite.

---

## 1. Purpose

[One paragraph: why the organisation uses AI, and that this policy sets the rules for using it within the board's risk appetite and the law.]

## 2. Scope

- **Entities:** [legal entities and branches covered]
- **Systems:** every AI system the organisation builds, buys or uses, including material AI features in bought products, as defined in the [AI inventory standard](../framework/governance-operations/ai-inventory.md#what-goes-in-the-inventory)
- **People:** all employees and contractors, and third parties who operate or use AI systems on the organisation's behalf
- **Use of AI tools by staff:** covered by the [acceptable use standard](../framework/operating-model/acceptable-use.md)
- **Exclusions:** [any, with the reason]

## 3. Principles

*State each principle in one or two sentences, in the organisation's words. Keep them testable: each should map to controls.*

| Principle | Commitment | Where it is enforced |
|---|---|---|
| Accountability | Every AI system has one named business owner who accepts its residual risk | [Accountability principles](../framework/operating-model/roles-responsibilities.md#accountability-principles) |
| Proportionality | Governance scales with risk tier | [Risk tiers](../framework/risk-classification/genai-risk-matrix.md#risk-tier-determination-for-genai) |
| Human oversight | Humans oversee AI in proportion to its impact | [Human-in-the-loop patterns](../framework/responsible-ai/human-in-loop-patterns.md) |
| Fairness | [commitment] | [Bias detection](../framework/responsible-ai/bias-detection-llm.md) |
| Transparency | [commitment] | [Transparency standards](../framework/responsible-ai/transparency-standards.md) |
| Reliability and safety | [commitment] | [Evaluation governance](../framework/llm-lifecycle/evaluation-governance.md) |
| Security and privacy | [commitment] | [AI security](../framework/ai-security/adversarial-robustness.md), [data residency](../framework/compliance/cross-border-data-governance.md) |
| Lawful use | The organisation meets the legal and regulatory requirements that apply to each AI system in each jurisdiction where it operates | [Multi-jurisdictional guide](../framework/compliance/multi-jurisdictional-guide.md) |
| Continual improvement | Incidents, reviews and audit findings change the framework, not only the system | [Review cadence](../framework/operating-model/review-cadence.md) |

## 4. Risk Appetite

AI is used within the AI risk appetite statement approved by the board ([risk appetite](../framework/operating-model/board-reporting.md#ai-risk-appetite-statement)). [Reference the current statement and its approval date. Do not restate it here; restated copies drift.]

## 5. Prohibited Uses

The organisation does not develop or use AI for the practices prohibited by EU AI Act Art. 5 or for the internal prohibited uses listed in [Annex B / the prohibited-use list]. Prohibited uses are rejected at the [Step 0 screen](../framework/risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen), not tiered. This check cannot be excepted.

## 6. Governance Bodies and Roles

| Body or role | Responsibility under this policy |
|---|---|
| Board / Board Risk Committee | Approves this policy, the AI risk appetite and the AI Risk Committee charter; receives the quarterly AI risk report and material incident notifications |
| AI Risk Committee | Oversees AI risk under its [charter](ai-risk-committee-charter.md) (GV-005); approves T1 decisions; reviews the exception register monthly and the inventory quarterly |
| First line | Business owners, product and system owners, AI leads, technical owners and AI Operations own and operate AI systems |
| Second line | AI Risk, Model Risk Management, Compliance and the DPO set standards, challenge, validate and approve per tier |
| Third line | Internal Audit gives independent assurance over this policy and the framework |

Roles, lines of defence and approvers by tier are in [roles and responsibilities](../framework/operating-model/roles-responsibilities.md).

## 7. Inventory and Risk Tiering

- Every AI system is registered in the AI inventory before development begins (RA-006), and the inventory is reconciled quarterly (GV-006).
- Every AI system is assigned a risk tier from T1 to T4 using the framework risk matrices and the canonical override list before development begins (RA-001, RA-002, RA-004). Overrides can raise a tier, never lower it.

## 8. Lifecycle Controls

Every AI system follows the [governance workflow](../framework/governance-operations/governance-workflow.md) from intake to retirement and meets the controls in the [control register](../framework/governance-operations/control-register.md) for its tier. The following can never be excepted: a DPIA where the law requires one; the prohibited-use check; zero unresolved Critical red-team findings; a kill switch for T1 customer-facing systems and all agentic systems; audit logging.

## 9. Third-Party AI

AI from vendors, including AI features in bought products, is assessed at the depth set for its tier, contracted on terms that meet [third-party model risk](../framework/compliance/third-party-model-risk.md) requirements, and monitored for change.

## 10. Use of AI Tools by Staff

Staff use AI tools only as the [acceptable use standard](../framework/operating-model/acceptable-use.md) allows (GV-003).

## 11. AI Literacy

The organisation takes role-based measures to support the AI literacy of its staff and of others acting on its behalf, and tracks completion ([AI literacy](../framework/operating-model/ai-literacy.md), GV-002).

## 12. Exceptions

A control may be missed only through an approved, time-limited exception recorded in the [exception register](exception-register.md) (GV-004), approved by the authority for the system's tier, under [Exceptions and Risk Acceptance](../framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance). Non-waivable items in section 8 cannot be excepted.

## 13. Incidents, Reporting and Concerns

- AI incidents are classified and escalated per [escalation paths](../framework/operating-model/escalation-paths.md). Every S1, and every S2 that meets the [material incident criteria](../framework/operating-model/board-reporting.md#material-incident-criteria), is notified to the Board Risk Committee.
- The board receives a quarterly AI risk report ([board reporting](../framework/operating-model/board-reporting.md)).
- [How staff raise a concern about an AI system, including through the speak-up or whistleblowing channel, and the non-retaliation commitment.]

## 14. Breaches of This Policy

[How breaches are handled: disciplinary policy, regulatory notification where required.]

## 15. Review

This policy is reviewed at least annually by AI Risk, endorsed by the AI Risk Committee and approved by [the board / Board Risk Committee]. It is also reviewed on a material change in regulation, strategy or risk appetite. Each review considers incidents, audit findings, regulatory change (RV-004) and progress against the AI objectives in Annex A.

---

## Annex A: AI Management System Items (ISO/IEC 42001)

*Complete this annex if the organisation runs, or intends to certify, an AI management system under ISO/IEC 42001. Otherwise delete it.*

| Item | ISO/IEC 42001 clause | Content |
|---|---|---|
| Scope of the AI management system | 4.3 | [Entities, functions, locations and AI systems covered; what is excluded and why; the internal and external issues and requirements that set the scope] |
| AI objectives | 6.2 | [Measurable objectives consistent with this policy, each with an owner, a target date, the resources needed and how progress is measured. Governance health KPIs and targets in [governance metrics](../framework/operating-model/governance-metrics.md) are a starting point] |
| Statement of Applicability | 6.1.3 | [Reference to the separate Statement of Applicability: each Annex A control, whether it is included, and why] |
| Planning of changes | 6.3 | [How changes to the AI management system are proposed, assessed and approved, and by whom] |

## Annex B: Internal Prohibited Uses

[List uses the organisation prohibits beyond EU AI Act Art. 5.]
