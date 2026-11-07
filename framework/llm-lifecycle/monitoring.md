# LLM Production Monitoring

## Overview

Monitoring an LLM system in production is fundamentally different from monitoring a traditional ML model. Traditional models produce numerical predictions that can be evaluated against known distributions. LLMs produce free-text outputs where quality is multi-dimensional, subjective, and use-case dependent.

This document defines monitoring standards for LLM-based systems in production, covering output quality, operational health, safety, cost, and user feedback.

---

## Monitoring Dimensions

### 1. Output Quality

| Metric | Description | Collection Method |
|--------|-------------|-------------------|
| Faithfulness | Output grounded in provided context (RAG systems) | LLM-as-judge on sampled outputs |
| Relevance | Output addresses the user's query | LLM-as-judge on sampled outputs |
| Correctness | Output is factually accurate | Human evaluation on sampled outputs (T1/T2) |
| Consistency | Same or similar inputs produce consistent outputs | Automated repeat-query testing |
| Format compliance | Output matches expected schema or format | Automated schema validation |
| Hallucination rate | Share of evaluated responses with at least one material unsupported or false claim | LLM-as-judge + human spot-check |

Metric definitions are in [evaluation-governance.md](evaluation-governance.md#metric-definitions) and thresholds in [Threshold Definitions by Tier](evaluation-governance.md#threshold-definitions-by-tier). Automated scoring rates are set in [Production Evaluation](#production-evaluation) below.

**Human evaluation of sampled outputs:**

| Tier | Human Eval |
|------|------------|
| T1 | 5% of responses, daily review |
| T2 | 2% of responses, weekly review |
| T3 | Monthly spot-check |
| T4 | Quarterly spot-check |

This is quality evaluation. Human oversight sampling for T1 systems running Pattern 3 is set separately in [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix).

### 2. Safety and Guardrails

| Metric | Description | Alert Threshold |
|--------|-------------|----------------|
| Guardrail trigger rate | Proportion of requests triggering input/output guardrails | Trend deviation > 2σ |
| Prompt injection detection rate | Proportion of requests flagged as injection attempts | Any increase triggers investigation |
| Toxicity score | Average and maximum toxicity in outputs | Use case dependent; any flagged output investigated |
| PII leakage events | Instances where PII appears in outputs | Zero tolerance; immediate alert |
| Refusal rate | Proportion of queries the model refuses to answer | Trend analysis; unexpected changes investigated |
| Jailbreak attempts | Detected attempts to bypass model safety | Logged and reviewed; pattern analysis |

### 3. Operational Health

| Metric | Description | Alert Threshold |
|--------|-------------|----------------|
| Latency (p50, p95, p99) | End-to-end response time | SLA breach |
| Error rate | Proportion of failed requests | > 1% |
| Throughput | Requests per second | Below expected range |
| Token usage (input) | Average input tokens per request | > 2σ from baseline |
| Token usage (output) | Average output tokens per request | > 2σ from baseline |
| Rate limit hits | Requests rejected by rate limiting | Any occurrence |
| Model availability | Upstream model API availability | < 99.9% (or SLA-defined) |
| Retrieval latency (RAG) | Time to retrieve context documents | SLA breach |

Retrieval empty-result rate and other RAG pipeline checks are in [RAG Pipeline Health](#rag-pipeline-health).

### 4. Cost

| Metric | Description | Alert Threshold |
|--------|-------------|----------------|
| Cost per request | Average token cost per request | > budget ceiling |
| Daily/weekly/monthly spend | Aggregate spending | Budget threshold (80%, 100%) |
| Cost by use case | Spend attributed to each use case or team | Budget deviation |
| Cost per user | Average cost per end user | Anomaly detection |
| Cost efficiency | Cost relative to output quality | Degrading ratio |

### 5. User Feedback

| Signal | Collection Method | Analysis |
|--------|-------------------|----------|
| Explicit feedback | Thumbs up/down, ratings on responses | Aggregate satisfaction score; trend analysis |
| Escalation rate | Proportion of interactions escalated to human | Trend analysis |
| Regeneration rate | How often users request a new response | Indicates dissatisfaction or quality issues |
| Session abandonment | Users leave without completing their task | Funnel analysis |
| Support tickets | Issues raised about AI system behavior | Categorization and trend analysis |

### RAG Pipeline Health

Required for T1 and T2 RAG systems; recommended for T3. Output quality is a lagging indicator of pipeline health: a stale corpus can serve wrong answers for days before the hallucination rate crosses its threshold. This requirement comes from a post-mortem in the [customer service chatbot case file](../../examples/customer-service-chatbot/governance-case-file.md), where a failed document refresh left outdated fee schedules in the corpus for two weeks.

| Metric | Description | Alert Threshold |
|--------|-------------|----------------|
| Ingestion and indexing job success | Scheduled document refresh and index build jobs complete successfully | Any failed run, or no successful run within the scheduled interval: P2 |
| Document corpus freshness | Age of the newest document from each source, compared with that source's expected update interval | Older than the expected interval: P3. Older than twice the interval: P2 |
| Index staleness | Source documents changed but not yet reflected in the index | Changes not indexed after one refresh cycle: P2 |
| Embedding job failures | Documents or chunks that failed to embed in a run | Any failure: P3. More than 1% of documents in a run: P2 |
| Chunk count drift | Change in total chunk count against the previous run, without a matching change in source documents | More than 10%: P3. More than 25%: P2 |
| Retrieval empty-result rate | Queries that retrieve no relevant documents | More than 10% of queries over 24 hours: P2 |

Show the last successful refresh time for each source on the system dashboard. Manage pipeline service-account credentials through automated rotation so that an expired credential cannot stop refreshes silently.

---

## Production Evaluation

Production evaluation is three named activities (control PM-004). Values match [evaluation-governance.md](evaluation-governance.md#production-evaluation), which owns them; thresholds are in [Threshold Definitions by Tier](evaluation-governance.md#threshold-definitions-by-tier).

| Activity | T1 | T2 | T3 | T4 |
|----------|----|----|----|----|
| 1. Online automated scoring of live traffic | Every response (async) | 20% sample | 5% sample | Weekly batch sample |
| 2. Metrics review | Daily dashboard check by AI Operations, plus a monthly system-owner review | Weekly | Monthly | Quarterly |
| 3. Full offline suite re-run | Monthly | Quarterly | Semi-annual | Semi-annual |

Always re-run the full offline suite on a model, provider or prompt change.

---

## Alerting and Escalation

### Alert Priority

| Priority | Criteria | Response SLA | Notification |
|----------|----------|-------------|-------------|
| P1 | PII leakage, safety breach, system down | 15 minutes | On-call + management + CISO |
| P2 | Quality degradation below threshold, cost overrun, sustained errors | 4 hours | On-call + team lead |
| P3 | Trend anomaly, guardrail trigger increase, minor metric drift | 24 hours | Team lead |
| P4 | Informational, cosmetic, minor anomalies | Next business day | Logged for review |

P1 to P4 are alert priorities, not incident severities. Acknowledgement targets (P1 within 15 minutes, P2 within 1 hour) and the mapping from alert priority to incident severity (S1 to S4) are in [escalation-paths.md](../operating-model/escalation-paths.md#alert-priority-to-incident-severity).

### Escalation Path

```
P4: Team lead review → log
P3: Team lead → investigate → remediate or escalate
P2: On-call → team lead → remediate within SLA → declare an incident if needed (usually S2 or S3)
P1: On-call → immediate action (circuit breaker/shutdown if needed)
    → triage; declare S1 or S2 if external impact is confirmed
    → management + CISO notification
    → incident commander assigned
```

Once an incident is declared, its severity sets the response SLA, root cause and post-mortem deadlines, and notifications, per [escalation-paths.md](../operating-model/escalation-paths.md#severity-classification). Board notification follows the [material incident criteria](../operating-model/board-reporting.md#material-incident-criteria).

---

## Drift Detection for LLMs

Traditional data drift metrics (PSI, KL divergence) apply to input distributions but not to output quality. LLM drift detection requires different approaches:

### Input Drift

| Method | Description |
|--------|-------------|
| Query distribution monitoring | Track topic, length, and complexity distribution of user queries |
| Out-of-scope query detection | Identify queries outside the intended use case boundary |
| Language distribution | Monitor for changes in input language or dialect |

### Output Drift

| Method | Description |
|--------|-------------|
| Output length distribution | Track changes in average output length |
| Sentiment drift | Monitor output sentiment distribution over time |
| Topic drift | Track whether outputs are covering different topics than baseline |
| Automated eval trending | Run evaluation metrics continuously; detect trend changes |
| Reference answer comparison | Compare current outputs to baseline reference answers for canonical queries |

### Model Provider Drift

| Monitor | Description |
|---------|-------------|
| Model version changes | Detect when the vendor updates the underlying model |
| Vendor behaviour canary | Run a fixed domain query set daily (T1), weekly (T2) or monthly (T3/T4) to detect silent vendor model changes; alert on score changes. See [third-party-model-risk.md](../compliance/third-party-model-risk.md#ongoing-monitoring) |
| Latency and throughput changes | Detect provider-side performance changes |

---

## Dashboards

### Operational Dashboard (Real-Time)

- Request volume, latency percentiles, error rate
- Guardrail trigger rates
- Cost accumulation (daily, MTD)
- Model API availability

### Quality Dashboard (Daily/Weekly)

- Output quality metrics (faithfulness, relevance, hallucination rate)
- User feedback scores
- Drift indicators
- Evaluation suite scores (latest run)

### Executive Dashboard (Monthly)

- Use case health summary (green/amber/red per use case)
- Cost vs. budget
- Incident count and severity
- User adoption and satisfaction
- Risk tier distribution across portfolio

---

## Monitoring Infrastructure Requirements

| Requirement | Standard |
|-------------|----------|
| Log retention | Interaction logs: 7 years T1, 5 years T2, 3 years T3, 1 year T4 ([prompt-audit-trail.md](../compliance/prompt-audit-trail.md#retention-requirements)) |
| Log immutability | Append-only storage; tamper-evident |
| Data classification | Monitoring data classified and handled per data governance policy |
| PII in logs | PII redacted from monitoring logs unless explicitly required and approved |
| Access control | Monitoring dashboards and raw logs access-controlled by role |
| Availability | Monitoring infrastructure availability ≥ system SLA |
