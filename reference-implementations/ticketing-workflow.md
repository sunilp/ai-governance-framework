# Ticketing Workflow Pattern

**Purpose:** Run the [governance workflow](../framework/governance-operations/governance-workflow.md) in Jira, ServiceNow or a similar tool, so that a release cannot move to the next stage without the evidence and approvals its tier requires, and every exception expires on time. The pattern is tool-neutral: it names states, fields and transition rules, not product APIs.

The ticketing tool holds the documents and the human approvals. The [governance gate](README.md#governance-gate) checks the system's repository. Use both: the release ticket stores the gate's `gate-result.json`, and the gate's exception list is exported from the exception tickets.

---

## Ticket Types

| Ticket type | One per | Holds | Controls |
|---|---|---|---|
| AI system | System | Inventory ID, tier, system types, owners, link to the inventory entry | RA-006 |
| Release | First deployment, and each material change | Workflow state, evidence per control, approvals, gate result | RA-001 to DA-004, PM and IR pre-go-live controls |
| Exception | Exception | Every field of the [exception register](../templates/exception-register.md) | GV-004 |
| Finding | Red-team, validation or review finding | Severity, owner, remediation, retest result | SR-002, RV-001 |

A material change ([RV-003](../framework/governance-operations/control-register.md)) opens a new release ticket at the stage the change assessment names, linked to the previous release.

## Workflow States

One state per [workflow stage](../framework/governance-operations/governance-workflow.md). A release cannot skip a state.

| State | Workflow stage | Leaves when |
|---|---|---|
| Intake | 1 | Intake decision recorded |
| Risk assessment | 2 | Stage 2 evidence attached and the risk assessment approved by the tier approver |
| Design review | 3 | Stage 3 evidence attached and the architecture approver has signed |
| Build | 4 | Stage 4 evidence attached, prompt review complete for the tier |
| Evaluation | 5 | Evaluation reports attached and passing; validation complete for the tier |
| Security review | 6 | Red-team report attached, zero open Critical findings, open High findings remediated or excepted |
| Deployment approval | 7 | Evidence pack complete, gate result `pass` attached, sign-off chain complete |
| Live | 8 | Monitoring confirmed before traffic; release closes |

The order enforces the framework's "no build before approval" rule: RA-001, RA-004 and AR-001 to AR-005 are "before development" controls, so Build opens only after Risk assessment and Design review close.

## Required Attachments by Control and Tier

Give the release ticket one evidence field per control (attachment or link, document ID, version, SHA-256). Show only the fields the release needs.

**Generate the list, do not maintain it by hand.** The fields a release needs are exactly the controls the governance gate requires for its tier and system types: the same [matching rule](README.md#control-matching-rule), read from [`controls/`](../controls/). A small job can call the gate's applicability logic and write the field set into the ticket template whenever `controls/` changes. Hand-maintained checklists drift from the register; generated ones cannot.

What changes by tier is set by the [minimum evidence pack](../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier). Conditional controls (EU AI Act scope, disclosure, marking, retrieval permissions, decision notices) appear with a "not applicable" option that requires a reason; the deployment approver sees each reason.

## Transition Rules

Each transition is blocked unless its condition holds. In Jira this is a workflow validator (blocks the transition when a field is empty or a rule fails) plus a condition (hides the transition from users who may not perform it). In ServiceNow it is a flow or business rule that checks attachments and approval records before the state change. Keep the rule logic in one place and test it like code.

| Transition | Blocked unless |
|---|---|
| Risk assessment to Design review | Evidence for RA-001, RA-002, RA-004, RA-006, RA-007 and every other applicable Stage 2 control. RA-004 approved by `approvers.risk_assessment` for the tier in [tiers.yaml](../policy/tiers.yaml). RA-007 cannot be marked not applicable or excepted |
| Design review to Build | Evidence for the applicable Stage 3 controls; architecture approver per tier; vendor contract check (AR-007) before production data reaches the vendor |
| Build to Evaluation | Evidence for the applicable Stage 4 controls; DE-003 signed by the reviewer set for the tier (`approvers.prompt_review`) |
| Evaluation to Security review | Evaluation reports for the applicable Stage 5 controls; the gate run in `pre-approval` phase shows no evaluation failures, or each failure has a linked valid exception |
| Security review to Deployment approval | Red-team report (SR-001); no linked Critical finding open (no exception allowed); each open High finding has a linked valid exception |
| Deployment approval to Live | Evidence for DA-001, DA-003, DA-004 (T1/T2) and the pre-go-live PM and IR controls; `gate-result.json` with result `pass` attached; one approval task completed per signer in `approvers.deployment` (DA-002); the requester is not an approver |

Approval tasks map to groups, and groups map to the role ids in [roles.yaml](../policy/roles.yaml). Where a committee approves, the approval task records the minute reference.

## Exception Tickets

| Field | Rule |
|---|---|
| Exception ID | Unique, in the form EXC-YYYY-NNN |
| System, release | Linked tickets |
| Control | Pick list from `controls/`. RA-007, PM-006 and PM-007 are not selectable; SR-002 is selectable only for open High findings; RA-005 is not selectable where the DPIA is legally required ([non-waivable list](../framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance)) |
| Reason, compensating controls | Required |
| Approver | Approval task routed to `approvers.exception` for the tier in [tiers.yaml](../policy/tiers.yaml) |
| Start, expiry | Validator: expiry no more than 90 days after start |
| Renewal | Links to the original; at most one; routed one level higher than the original approver. At T1 the renewal needs a full committee decision and is reported to the Board Risk Committee |
| Status | Open, renewed, closed or expired |

Automation:

- **Before expiry:** notify the system owner and the approver, with time to remediate or request the one renewal.
- **At expiry:** set the status to expired, flag the linked release and system tickets, and treat the covered control as failed ([GV-004](../framework/governance-operations/control-register.md) escalates to the tier approver and the AI Risk Committee).
- **Monthly:** a saved filter of open, expiring and expired exceptions is the agenda item for the AI Risk Committee's register review.
- **Sync to the gate:** a job writes each system's open exceptions into its `governance.yaml` (or opens a pull request that does), so the gate judges the same register the committee reviews.

## What This Gives the Auditor

- **Timestamps.** Ticket history shows when each document was attached and each approval given, which settles "before development" and "before go-live" questions that the gate cannot answer.
- **Population and samples.** The second-line tests in [`controls/`](../controls/) sample deployments, exceptions and approvals. Release and exception tickets are those populations, already filtered by tier.
- **One trail.** Release ticket, gate result, evidence hashes and approval records point at each other, so a sampled deployment can be traced in both directions.
