# Governance Metrics & KPIs

## Overview

What gets measured gets managed. A governance program without metrics is a governance program without evidence — of effectiveness, of compliance, or of value.

These KPIs measure the health of the AI governance program itself, not the performance of individual AI systems (which is covered in [monitoring](../llm-lifecycle/monitoring.md) and [model-lifecycle monitoring](../model-lifecycle/monitoring.md)).

---

## Governance Health KPIs

Measure whether governance controls are being applied consistently across the AI portfolio.

| Metric | Definition | Target | Cadence | Owner |
|--------|-----------|--------|---------|-------|
| Risk assessment coverage | % of AI systems with current (non-expired) risk assessment | 100% T1/T2; 95% T3/T4 | Monthly | AI Risk |
| Model card currency | % of systems with model card updated within review cycle | 100% T1; 95% T2; 90% T3/T4 | Monthly | AI Operations |
| Overdue reviews | Count of systems past their scheduled review date, by tier | 0 for T1; ≤ 2 for T2 | Monthly | AI Risk |
| Deployment gate pass rate | % of deployment attempts passing gates on first attempt | > 80% | Quarterly | AI Operations |
| Mean time to production | Calendar days from development complete to production deployment | Trend (not absolute target) | Quarterly | AI Operations |
| Audit finding closure rate | % of audit findings closed within SLA | > 90% | Quarterly | AI Risk |
| Governance training completion | % of AI practitioners who completed required training | > 95% | Quarterly | AI Risk |
| Policy exception count | Number of active governance exceptions, by tier | Trend; investigate increases | Quarterly | AI Risk |

### Interpreting Governance Health

- **Deployment gate pass rate < 60%**: standards may be unclear or teams undertrained — investigate root causes, not symptoms
- **Overdue reviews increasing**: governance team may be under-resourced or review process too burdensome
- **Policy exceptions increasing**: either the policy is too rigid or risk acceptance is becoming a habit — either way, investigate

---

## Responsible AI KPIs

Measure whether AI systems are meeting ethical and fairness standards.

| Metric | Definition | Target | Cadence | Owner |
|--------|-----------|--------|---------|-------|
| Bias incident count | Number of confirmed bias incidents across portfolio | Quarter-over-quarter decrease | Quarterly | Responsible AI |
| Fairness compliance rate | % of T1/T2 systems meeting fairness metric thresholds | 100% | Quarterly | Responsible AI |
| Hallucination rate | Per-system hallucination rate for T1/T2 GenAI systems | Within system-specific threshold | Monthly (T1), Quarterly (T2) | AI Operations |
| Human override rate | % of AI outputs overridden by human reviewers | Trend analysis | Monthly | AI Operations |
| Transparency compliance | % of customer-facing AI systems with proper disclosure | 100% | Quarterly | Compliance |
| Counterfactual test coverage | % of T1 systems with current counterfactual bias testing | 100% | Quarterly | Responsible AI |

### Interpreting Responsible AI KPIs

- **Human override rate too high (>30%)**: model quality may be poor; investigate output quality
- **Human override rate too low (<2% for T1)**: possible rubber-stamping; investigate whether humans are genuinely reviewing
- **Hallucination rate trending up**: may indicate model drift, RAG corpus degradation, or provider model change

---

## Portfolio KPIs

Measure the AI portfolio's risk profile, spend, and concentration.

| Metric | Definition | Target | Cadence | Owner |
|--------|-----------|--------|---------|-------|
| System count by tier | Number of AI systems at each tier (T1/T2/T3/T4) | Awareness; no target | Quarterly | AI Risk |
| New deployments | Number of new AI systems deployed this period | Awareness; capacity planning | Quarterly | AI Operations |
| Retirements | Number of AI systems decommissioned this period | Awareness | Quarterly | AI Operations |
| Vendor concentration | % of T1/T2 systems dependent on a single model provider | < 70% on any single provider | Quarterly | AI Risk |
| AI spend by tier | Total AI cost allocated by risk tier | Within budget | Monthly | Finance / AI Operations |
| AI spend by business unit | Total AI cost allocated by business unit | Within BU budgets | Monthly | Finance |
| Risk concentration heatmap | Systems plotted by business impact × probability of failure | Visual review; no outliers without documented risk acceptance | Quarterly | AI Risk |

---

## Operational KPIs

Measure the operational reliability of AI systems (aggregated portfolio view for governance reporting).

| Metric | Definition | Alert Threshold | Cadence | Owner |
|--------|-----------|----------------|---------|-------|
| Incident count by severity | Number of S1/S2/S3/S4 incidents across portfolio | S1 >0 triggers board notification | Monthly | AI Operations |
| Mean time to detect (MTTD) | Average time from incident occurrence to detection | Trending; T1 target < 15 min | Quarterly | AI Operations |
| Mean time to resolve (MTTR) | Average time from detection to resolution | Trending; T1 target < 4 hours | Quarterly | AI Operations |
| System availability | Aggregate availability across T1/T2 systems | > 99.5% (T1), > 99% (T2) | Monthly | AI Operations |
| Cost per transaction trend | Average inference cost per transaction, trending over time | Within budget; alert on > 20% increase | Monthly | AI Operations |

---

## Measurement Cadence and Reporting

| KPI Category | Reporting Frequency | Primary Audience | Report Vehicle |
|-------------|-------------------|-----------------|----------------|
| Governance health | Monthly | AI Risk Committee | Monthly dashboard |
| Responsible AI | Quarterly | AI Risk Committee, Board | Quarterly risk report |
| Portfolio | Quarterly | CTO, CFO, Board | Quarterly risk report |
| Operational | Monthly | AI Operations, CTO | Operational dashboard |

See [board-reporting.md](board-reporting.md) for the board-level reporting template and format.

---

## Anti-Patterns: What NOT to Measure

| Anti-Pattern | Why It's Harmful |
|-------------|-----------------|
| Number of models deployed (as a success metric) | Incentivizes deployment over quality; more models ≠ more value |
| Lines of governance documentation produced | Incentivizes bureaucracy over effectiveness |
| Time spent in governance reviews (as efficiency metric) | Incentivizes rushing reviews; governance is not an obstacle to optimize away |
| Model accuracy in isolation (without business context) | A 99% accurate model on the wrong problem creates zero value |
| Vanity metrics ("AI maturity score") | Self-assessed scores without grounding in measurable outcomes are meaningless |

---

## Implementation Notes

- Start with 3–5 KPIs that your organization can actually measure today. Expand coverage as data collection matures.
- Automate collection wherever possible — manual KPI collection degrades within months.
- Every KPI must have a named owner. Unowned metrics stop being measured.
- Review the KPI framework itself annually — retire metrics that no longer drive behavior, add metrics for emerging risks.
