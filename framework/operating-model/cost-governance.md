# AI Cost Governance

## Overview

AI cost governance ensures that spending on AI systems is intentional, attributed, and proportional to business value. Without structured cost governance, AI spend becomes opaque — individual teams optimize locally, shared costs go unattributed, and cost overruns surface only when budgets are already blown.

This is not about minimizing cost. It is about making cost visible, accountable, and governed with the same rigor as other operational expenses.

---

## Cost Categories

| Category | Description | Examples |
|----------|-------------|----------|
| Inference | Token costs for API-based models; GPU compute for self-hosted models | OpenAI API charges, Anthropic API charges, GPU instance costs |
| Fine-tuning | Compute for training/fine-tuning, data preparation labor | GPU training runs, dataset curation, annotation |
| Infrastructure | Supporting infrastructure for AI systems | Vector databases, embedding services, logging/monitoring storage, guardrail compute |
| Human review | Labor costs for human-in-the-loop oversight | Analyst review time, quality assurance, red-teaming labor |
| Vendor licensing | Platform fees, enterprise agreements, support tiers | Enterprise API agreements, model licensing fees |
| Evaluation | Testing, benchmarking, safety evaluation | Eval suite compute costs, LLM-as-judge inference costs |

---

## Budgeting by Tier

| Tier | Budget Approval Authority | Review Frequency | Budget Change Process |
|------|--------------------------|-----------------|----------------------|
| T1 — Critical | CTO + CFO | Monthly | Change request to AI Risk Committee |
| T2 — High | VP / Head of AI | Quarterly | Approval from budget owner |
| T3 — Medium | Team lead / Director | Semi-annually | Standard budget process |
| T4 — Low | Self-service within department budget | Annually | No separate approval |

### Budget Setting

- Set inference budgets based on projected usage (requests/day × average tokens × price per token)
- Add 30% buffer for T1 systems (demand spikes, retries, evaluation runs)
- Fine-tuning budgets set per project, not per system
- Infrastructure budgets aligned with standard cloud cost governance

---

## Cost Attribution

Every AI cost must be attributable to a system, owner, and business unit.

### Attribution Model

| Cost Type | Attribution Method |
|-----------|-------------------|
| API inference costs | Tag every API call with system ID, business unit, environment (prod/dev/eval) |
| Self-hosted GPU compute | Allocate by GPU-hours per system; shared infrastructure allocated by usage ratio |
| Vector database | Allocate by storage volume and query volume per system |
| Monitoring/logging | Allocate by log volume per system |
| Shared platform costs | Allocate proportionally by system tier weight (T1=4, T2=3, T3=2, T4=1) |

### Chargeback vs. Showback

| Model | When to Use | Advantages | Disadvantages |
|-------|------------|------------|---------------|
| Chargeback | Mature AI programs with clear system ownership | Drives cost accountability; teams optimize spend | Administrative overhead; may discourage experimentation |
| Showback | Early AI programs; innovation-focused teams | Visibility without friction; encourages adoption | Less accountability; costs absorbed centrally |
| Hybrid | Most organizations | Chargeback for production systems; showback for development/experimentation | Moderate complexity |

Start with showback. Move to chargeback for production systems once attribution infrastructure is mature.

---

## Threshold Alerts and Escalation

| Threshold | Action | Notification |
|-----------|--------|-------------|
| 80% of monthly budget consumed | Alert to system owner | Automated notification |
| 100% of monthly budget consumed | Alert to budget approver; assess whether to continue or throttle | System owner + budget approver |
| 120% of monthly budget consumed | Escalation to VP/CTO; root cause investigation required | Budget approver + VP/CTO |
| Daily spend anomaly (> 3σ from baseline) | Immediate investigation; potential automated throttling for T3/T4 | On-call + system owner |
| Single request cost anomaly (> 10x average) | Log and flag; investigate if repeated | System owner |

### Automated Controls

- T1/T2: alert only — never auto-throttle production critical systems
- T3/T4: auto-throttle option available (reduce request rate, switch to smaller model) — must be pre-configured and tested
- All tiers: daily cost digest email to system owners
- All tiers: weekly cost summary to budget approvers

---

## Cost Optimization Governance

Cost optimization is legitimate and encouraged — but not at the expense of safety, quality, or compliance.

### Acceptable Optimization

| Optimization | Governance Requirement |
|-------------|----------------------|
| Prompt optimization (shorter prompts, fewer tokens) | Verify output quality unchanged via eval suite |
| Model downsizing (e.g., GPT-4 → GPT-4-mini) | Full model selection re-evaluation; same deployment gates |
| Response caching (repeated queries) | Verify cache invalidation strategy; assess stale response risk |
| Batch processing (instead of real-time) | Verify latency requirements still met |
| Request routing (simple queries to smaller models) | Verify routing accuracy; eval quality for routed responses |

### Never Acceptable for Cost Reduction

| Anti-Pattern | Why |
|-------------|-----|
| Reducing evaluation coverage | Degraded eval = undetected quality regression |
| Removing guardrails or safety filters | Cost savings from removing safety = incident cost waiting to happen |
| Eliminating human review for T1 systems | Human oversight is a governance control, not a cost center |
| Reducing logging or audit trail | Compliance violation; unrecoverable in an audit |
| Skipping red-team testing | Security testing is non-negotiable for T1/T2 |

### Change Governance for Cost Optimization

Any cost optimization that changes model behavior, output quality, or safety posture follows the same deployment gate process as any other system change. Document the optimization rationale, expected cost savings, and quality impact assessment in the change request.

---

## Reporting

| Report | Audience | Frequency | Content |
|--------|----------|-----------|---------|
| System cost dashboard | System owners | Real-time | Per-system cost breakdown, trends, budget utilization |
| BU cost summary | Business unit heads | Monthly | Costs by system, tier, category; budget variance |
| Portfolio cost report | CTO, CFO | Quarterly | Total AI spend, tier distribution, vendor concentration, cost efficiency trends |
| Board cost section | Board / Risk Committee | Quarterly | Included in [board-ai-risk-report](../../templates/board-ai-risk-report.md) |
