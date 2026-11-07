# Exception Register

## Instructions

Every exception at every tier is recorded here (control GV-004). AI Risk maintains the register; the AI Risk Committee reviews it every month. The fields and rules come from [Exceptions and Risk Acceptance](../framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance). If this template and that section differ, the workflow governs.

Rules to check before recording an entry:

- **Non-waivable.** These can never be excepted: a DPIA where it is legally required; checks against prohibited uses; zero unresolved Critical red-team findings; a kill switch for T1 customer-facing systems and for all agentic systems; audit logging. Do not record an exception against them. Refuse it.
- **Approver by tier.** T1: AI Risk Committee. T2: Head of AI Risk. T3: Head of AI. T4: Team lead.
- **Duration.** 90 days maximum from the start date. One renewal at most, approved one level higher than the original approver. A T1 renewal needs a full committee decision (not a delegated or out-of-cycle one) and is reported to the Board Risk Committee.
- **ID.** `EXC-YYYY-NNN`, issued by AI Risk. Quote the ID in the model card, the deployment approval and the inventory entry, so the register can be reconciled against them.

Keep the register in the GRC platform or another system of record with change history. This Markdown table shows the fields and a worked entry.

---

## Register

| Exception ID | System | Control ID | Reason | Compensating controls | Approver | Start date | Expiry date | Status |
|---|---|---|---|---|---|---|---|---|
| EXC-2026-004 | Investment Research Assistant Agent (research-agent-v0.9) | EV-001 (pre-release evaluation; hallucination rate against the T1 cap of 1%) | Pre-release evaluation on 2026-01-20 measured a hallucination rate of 1.3% (4 of 300 responses). All other metrics passed. The four failures were unsourced figures in multi-source synthesis | Pattern 1 (human-in-the-loop): an analyst reviews every output in full before any use, with no move to sampled review, until a re-evaluation passes. Prompt fix to require a source citation for every figure | AI Risk Committee (signed by the Chair) | 2026-01-25 | 2026-03-26 (60 days) | Closed 2026-03-01. The full suite re-run on prompt v0.9.1 (2026-02-28) measured 0.7% (2 of 300), within the T1 cap |
| | | | | | | | | |

The worked entry is the exception in the [agentic research assistant example](../examples/agentic-research-assistant/risk-assessment.md#exception-exc-2026-004-hallucination-threshold).

Status values: open, renewed, closed or expired. For a renewal, set the status to renewed and add the renewal approver and the new expiry date to the row, keeping the original approver and expiry in the record history.

---

## Monthly Review Record

The AI Risk Committee completes one row per monthly meeting and minutes the actions.

| Meeting date | Open | Expiring within 30 days | Expired since last meeting | Renewals requested | Closed since last meeting | Actions (owner, date) |
|---|---|---|---|---|---|---|
| | | | | | | |

At each review, the committee checks:

1. Every open exception is within its expiry date. An expired exception means the control is failed, and the escalation for that control in the [control register](../framework/governance-operations/control-register.md) applies.
2. Compensating controls are operating, with evidence from the system owner.
3. No exception covers a non-waivable control.
4. No exception has been renewed more than once.
5. The count of active exceptions by tier is reported in [governance metrics](../framework/operating-model/governance-metrics.md#governance-health-kpis) (policy exception count). A rising count is investigated, not just recorded.
