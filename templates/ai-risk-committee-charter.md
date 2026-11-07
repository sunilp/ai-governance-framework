# AI Risk Committee Charter

## Instructions

This is the terms of reference for the AI Risk Committee, required by control GV-005. Membership, cadence and decision rights below restate the framework: [review cadence](../framework/operating-model/review-cadence.md#monthly-ai-risk-committee), [Approvals by Tier](../framework/operating-model/roles-responsibilities.md#approvals-by-tier) and [Exceptions and Risk Acceptance](../framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance). If this charter and those documents differ, change one of them so they agree; do not leave the conflict. Items marked "framework default" can be adjusted. Replace every bracketed item.

The charter is approved by the Board Risk Committee and reviewed annually.

---

## Document Control

| Field | Value |
|---|---|
| Approved by | Board Risk Committee, [date] |
| Version | [x.y] |
| Effective date | [date] |
| Next review | [no later than 12 months after approval] |
| Secretary | [Member of the AI Risk function, non-voting] |

---

## 1. Purpose and Authority

The AI Risk Committee oversees the risk of AI systems across [the organisation]. It is a management committee. It acts under authority delegated by the [Board Risk Committee] and reports to it.

The committee:
- approves T1 decisions under the AI policy;
- oversees the AI portfolio, the exception register and the AI inventory;
- recommends the AI policy and the AI risk appetite statement to the board;
- escalates to the Board Risk Committee as set out in section 7.

It does not run AI systems or approve T2 to T4 decisions, which sit with the roles in [Approvals by Tier](../framework/operating-model/roles-responsibilities.md#approvals-by-tier).

## 2. Membership

| Member | Role on the committee |
|---|---|
| Chief Risk Officer | Chair (voting) |
| Chief Technology Officer | Voting member |
| Head of Model Risk Management | Voting member |
| Head of Compliance | Voting member |
| Head of Data Science | Voting member |
| Business Line Heads | Attend as needed for their systems |
| CISO | Attends and co-signs T1 deployment and T1 model selection approvals |
| DPO | Attends when a system processes personal data, and co-signs T1 deployments that do |
| [Deputy chair] | [Named member who chairs when the CRO cannot] |

Which members vote is a framework default. Members may name one standing delegate each, recorded by the secretary. [Add or remove members to fit the organisation, keeping at least one independent second-line voting member.]

## 3. Quorum and Conflicts

Framework default:
- Quorum is the chair or deputy chair plus at least half of the voting members, including at least one of the Head of Model Risk Management and the Head of Compliance (or their delegates).
- A T1 deployment or model selection decision also needs the CISO or delegate present, and the DPO or delegate when the system processes personal data, because they co-sign.
- A member who sponsors, owns or built a system declares the conflict and does not vote on it. The declaration is minuted.
- A decision taken without quorum is not valid. It is retaken at a quorate meeting.

## 4. Meetings

- Monthly. One meeting each quarter is the full-portfolio meeting, which also approves the quarterly AI risk report for the board.
- If a T1 decision cannot wait, the chair convenes an out-of-cycle session within 10 business days of the request.
- Agendas follow [review cadence](../framework/operating-model/review-cadence.md#monthly-ai-risk-committee). In addition, every monthly meeting reviews the exception register (GV-004), and every quarterly full-portfolio meeting reviews the AI inventory and its reconciliation result (GV-006).
- Papers go to members at least [3] business days before the meeting (framework default).

## 5. Decision Rights

| Decision | Committee role |
|---|---|
| T1 risk assessment | Approves (RA-004) |
| T1 model selection | Approves; CISO co-signs |
| T1 deployment | Approves; CISO co-signs, and the DPO if personal data is processed (DA-002) |
| T1 exception | Approves; a renewal needs a full committee decision, not a delegated or out-of-cycle one, and is reported to the Board Risk Committee |
| Risk tier changes for T1 systems | Approves |
| Escalations from tier override reviews (RA-002), regulatory change assessments (RV-004) and other register controls | Decides |
| Quarterly AI risk report to the board | Approves |
| AI policy and AI risk appetite statement | Endorses and recommends to the board (GV-001) |
| This charter | Proposes changes to the Board Risk Committee |
| T2 to T4 decisions | None. Delegated to the roles in [Approvals by Tier](../framework/operating-model/roles-responsibilities.md#approvals-by-tier); the committee receives escalations |

The committee may attach conditions to any approval. Conditions are minuted with an owner and a date, and the system owner reports on them until they are met.

## 6. Delegation

Framework default:
- The committee may delegate an urgent first-time T1 exception that cannot wait for an out-of-cycle session to the chair acting with the Head of Model Risk Management or the Head of Compliance. The decision is recorded in the exception register and reported for ratification at the next meeting.
- The committee may delegate to AI Risk the check that conditions of approval have been met, with the result reported at the next meeting.
- The committee does not delegate T1 risk assessment, model selection or deployment approvals, exception renewals, or its recommendations on the AI policy and risk appetite.
- Every delegated decision is minuted at the next meeting.

## 7. Escalation to the Board Risk Committee

| Item | When |
|---|---|
| Every S1 incident | Within 24 hours ([escalation paths](../framework/operating-model/escalation-paths.md#notifications)) |
| An S2 incident that meets the [material incident criteria](../framework/operating-model/board-reporting.md#material-incident-criteria) | Within the timeline in board reporting |
| A T1 exception renewal | At the next Board Risk Committee meeting |
| The quarterly AI risk report | Each quarter |
| A breach of the AI risk appetite | At the next Board Risk Committee meeting, or sooner if the chair judges it urgent |
| The AI policy, risk appetite statement and this charter | For approval, annually and on change |
| Supervisory findings on AI and their remediation | At the next Board Risk Committee meeting |
| A disagreement the committee cannot resolve with the first line | At the chair's discretion |

## 8. Minutes and Evidence

- Minutes record attendance and quorum, conflicts declared, each decision with its conditions, dissent where a member asks for it to be recorded, delegated decisions reported, and actions with owners and deadlines.
- Minutes are distributed within 5 business days.
- Each T1 approval is filed with the system's evidence so it can be traced from the inventory entry and the control register (RA-004, DA-002).
- Minutes and papers are kept under the organisation's records retention schedule.

## 9. Review

The committee reviews this charter and its own effectiveness annually, including attendance, quorum failures, decisions taken out of cycle or by delegation, and overdue conditions, and reports the result to the Board Risk Committee with any proposed changes (GV-005).
