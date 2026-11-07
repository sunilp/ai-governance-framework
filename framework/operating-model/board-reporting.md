# Board-Level AI Risk Reporting

## Overview

Board and executive reporting on AI risk ensures informed oversight without operational overload. The board needs to understand the organization's AI risk posture, not the details of individual models. Report what matters for strategic decisions: portfolio health, material incidents, regulatory exposure, and cost trajectory.

This document defines the structure, content, and cadence of board-level AI risk reporting. For the fill-in-ready template, see [board-ai-risk-report.md](../../templates/board-ai-risk-report.md). For the metrics that feed these reports, see [governance-metrics.md](governance-metrics.md).

---

## Quarterly AI Risk Report Structure

The AI Risk Committee receives a structured quarterly report. The [board AI risk report template](../../templates/board-ai-risk-report.md) sets the sections and fields; this table summarises what each section must cover.

| Section | What it covers |
|---------|---------------|
| 1. Executive summary | 3 to 5 bullets, no jargon: material changes since the last report, decisions required, overall risk posture (improving / stable / deteriorating) |
| 2. Portfolio overview | Systems by tier with quarter-over-quarter trend; new deployments with tier and business owner; retirements; pipeline with expected deployment dates |
| 3. Risk concentration | Share of T1/T2 systems on each model provider; data residency compliance by jurisdiction; T1 growth against governance investment; business unit concentration against governance capacity |
| 4. Material incidents | S1 and S2 only: impact, one-sentence root cause, remediation status, systemic issues and action taken. Reference full incident reports; do not reproduce them |
| 5. Governance health | Key metrics from [governance-metrics.md](governance-metrics.md) with RAG status and commentary on non-green items |
| 6. Responsible AI | Bias incidents and trend, fairness compliance, transparency disclosure compliance, emerging concerns |
| 7. Regulatory update | Changes since the last report, readiness for upcoming deadlines, board actions; detail in [regulatory-change-monitoring.md](../compliance/regulatory-change-monitoring.md) |
| 8. Budget | Spend against budget by category, material variances, cost trajectory and forecast |
| 9. Recommendations | What is recommended, the risk rationale, what happens if we do not act, and the decision required (approve / note / defer) |

---

## Material Incident Criteria

Not every incident requires board notification. Material incidents do. Every S1 incident is material. An S2 incident is material when it meets any of the other criteria below. Severity levels are defined in [escalation-paths.md](escalation-paths.md#severity-classification).

| Criterion | Threshold | Notification Timeline |
|-----------|-----------|----------------------|
| Severity | Any S1 incident | Within 24 hours |
| Customer impact | > 100 customers affected OR any financial harm to customers | Within 24 hours |
| Financial impact | > $100K direct cost (remediation, compensation, fines) | Within 24 hours |
| Regulatory notification triggered | Any incident requiring regulatory notification | Within 24 hours |
| Reputational risk | Media coverage, social media escalation, or regulator inquiry | Immediately |
| Data breach | Any PII breach involving AI systems | Per existing breach notification policy |
| Systemic failure | T1 system unavailable > 4 hours | Within 24 hours |
| Safety bypass | Confirmed safety control bypass in production T1 system | Within 24 hours |

### Between-Quarter Notification

For material incidents between quarterly reports:
1. AI Risk Committee chair notified: within 1 hour for S1 ([escalation-paths.md](escalation-paths.md#notifications)); immediately once an S2 is assessed as material
2. Brief written summary within 24 hours
3. Incident report with root cause within 48 hours; post-mortem report within 1 week (S1) or 2 weeks (S2), per IR-004
4. Board Risk Committee notified within the timeline in the table above

---

## AI Risk Appetite Statement

The board should define and annually approve an AI risk appetite statement.

### What It Should Cover

| Dimension | Example Statement |
|-----------|------------------|
| Deployment scope | "We deploy AI systems up to T1 in customer-facing contexts with appropriate governance." |
| Vendor dependency | "No single model provider accounts for more than 70% of our T1/T2 AI systems." |
| Human oversight | "Every T1 customer-facing AI system meets our human oversight rules: a qualified human reviews adverse regulated decisions before they take effect, and informational systems have per-output review or evidenced Pattern 3 safeguards." (See [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix).) |
| Incident tolerance | "We target zero S1 incidents per year. S2 incidents have their root cause identified within 48 hours." |
| Regulatory posture | "We comply with all applicable AI regulation in jurisdictions where we operate." |
| Innovation balance | "We accept measured risk in T3/T4 systems to enable AI experimentation and innovation." |

### Annual Review Process

1. AI Risk function drafts updated risk appetite statement
2. CTO and CRO review and endorse
3. Board Risk Committee reviews and approves
4. Communicated to all AI practitioners
5. Governance controls calibrated to approved risk appetite

---

## Executive Dashboard

For ongoing visibility between quarterly reports, maintain an executive dashboard.

| Dimension | Visualization | Update Cadence |
|-----------|--------------|----------------|
| Portfolio health | System count by tier; green/amber/red status per system | Weekly |
| Incident trending | S1/S2/S3/S4 incidents over time (rolling 12 months) | Weekly |
| Compliance status | RAG heatmap per regulation per system | Monthly |
| Cost trending | Total AI spend with budget line overlay | Weekly |
| Vendor concentration | Provider distribution (pie chart) for T1/T2 systems | Monthly |
| Governance health | Key KPIs with target vs. actual | Monthly |

### Access

- CTO, CRO, CISO: full dashboard access
- AI Risk Committee members: full dashboard access
- Board members: quarterly snapshot included in board pack
- Business unit heads: filtered view of their systems

---

## Implementation Notes

- Keep the board report concise. If it exceeds 5 pages, it won't be read. Details belong in appendices.
- Lead with decisions required, not with data. The board's job is governance, not operations.
- Use consistent terminology quarter-over-quarter — changing how you describe risk confuses the audience.
- The first board report is the hardest. Start imperfect and iterate. The board values consistency and improvement.
