# Board-Level AI Risk Reporting

## Overview

Board and executive reporting on AI risk ensures informed oversight without operational overload. The board needs to understand the organization's AI risk posture, not the details of individual models. Report what matters for strategic decisions: portfolio health, material incidents, regulatory exposure, and cost trajectory.

This document defines the structure, content, and cadence of board-level AI risk reporting. For the fill-in-ready template, see [board-ai-risk-report.md](../../templates/board-ai-risk-report.md). For the metrics that feed these reports, see [governance-metrics.md](governance-metrics.md).

---

## Quarterly AI Risk Report Structure

The AI Risk Committee should receive a structured quarterly report covering these sections:

### 1. Executive Summary

3–5 bullet points. Lead with what the board needs to know or decide. No jargon.
- Material changes since last report
- Key decisions required
- Overall risk posture assessment (improving / stable / deteriorating)

### 2. Portfolio Overview

| Content | Description |
|---------|-------------|
| Systems by tier | T1/T2/T3/T4 count; quarter-over-quarter trend |
| New deployments | Systems deployed this quarter with tier and business owner |
| Retirements | Systems decommissioned this quarter |
| Pipeline | Systems in development or pilot, expected deployment dates |

### 3. Risk Concentration

| Dimension | What to Report |
|-----------|---------------|
| Vendor concentration | % of T1/T2 systems on each model provider; single-vendor dependency risk |
| Geographic concentration | Data residency compliance status by jurisdiction |
| Tier distribution | Are we accumulating T1 systems without proportional governance investment? |
| Business unit concentration | Which BUs have the most AI systems? Is governance capacity proportional? |

### 4. Material Incidents

S1 and S2 incidents only. For each:
- Incident ID, system, severity
- Customer/financial/regulatory impact
- Root cause (one sentence)
- Remediation status
- Systemic issue (if any) and action taken

Reference full incident reports — do not reproduce them in the board report.

### 5. Governance Health

Key metrics from [governance-metrics.md](governance-metrics.md):
- % of systems with current risk assessments
- Overdue reviews by tier
- Deployment gate pass rate
- Open audit findings past SLA

RAG status (Red/Amber/Green) for each metric with brief commentary on any non-green items.

### 6. Responsible AI

- Bias incident count and trend
- Fairness metric compliance rate
- Transparency disclosure compliance
- Any emerging responsible AI concerns

### 7. Regulatory Update

- Regulatory changes identified since last report
- Compliance readiness status for upcoming deadlines
- Actions required from the board (if any)

Reference [regulatory-change-monitoring.md](../compliance/regulatory-change-monitoring.md) for detail.

### 8. Budget

- AI spend vs. budget by category (inference, infrastructure, human review, vendor)
- Material variances with explanation
- Cost trajectory and forecast

### 9. Recommendations

Actions requiring board decision or awareness. Each recommendation should include:
- What is being recommended
- Why (risk rationale)
- What happens if we don't act
- Decision required from the board (approve / note / defer)

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
