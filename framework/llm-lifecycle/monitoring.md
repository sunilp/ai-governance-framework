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
| Hallucination rate | Proportion of outputs containing unsupported claims | LLM-as-judge + human spot-check |

**Sampling cadence:**

| Tier | Automated Eval | Human Eval |
|------|---------------|------------|
| T1 | Every response (async) | 5% of responses, daily review |
| T2 | 20% of responses | 2% of responses, weekly review |
| T3 | 5% of responses | Monthly spot-check |
| T4 | Weekly batch | Quarterly spot-check |

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
| Retrieval empty rate (RAG) | Queries with no relevant documents retrieved | > 10% |

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

---

## Alerting and Escalation

### Alert Severity

| Severity | Criteria | Response SLA | Notification |
|----------|----------|-------------|-------------|
| P1 | PII leakage, safety breach, system down | 15 minutes | On-call + management + CISO |
| P2 | Quality degradation below threshold, cost overrun, sustained errors | 4 hours | On-call + team lead |
| P3 | Trend anomaly, guardrail trigger increase, minor metric drift | 24 hours | Team lead |
| P4 | Informational, cosmetic, minor anomalies | Next business day | Logged for review |

### Escalation Path

```
P4: Team lead review → log
P3: Team lead → investigate → remediate or escalate
P2: On-call → team lead → remediate within SLA → post-incident review
P1: On-call → immediate action (circuit breaker/shutdown if needed)
    → management + CISO notification
    → incident commander assigned
    → root cause analysis within 48 hours
    → board notification if customer/regulatory impact
```

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
| Behavior change detection | Run a fixed evaluation suite daily; alert on score changes |
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
| Log retention | Per audit trail requirements (7 years T1, 5 years T2, 3 years T3/T4) |
| Log immutability | Append-only storage; tamper-evident |
| Data classification | Monitoring data classified and handled per data governance policy |
| PII in logs | PII redacted from monitoring logs unless explicitly required and approved |
| Access control | Monitoring dashboards and raw logs access-controlled by role |
| Availability | Monitoring infrastructure availability ≥ system SLA |
