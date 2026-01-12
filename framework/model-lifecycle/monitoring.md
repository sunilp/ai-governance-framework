# Production Monitoring Standards

## Purpose

A model that is not monitored is a model that is not governed. Monitoring is not optional — it is a regulatory expectation and an operational necessity. Every production AI system must have monitoring proportional to its risk tier.

## Monitoring Dimensions

### 1. Data Drift
Monitor for changes in input feature distributions that may indicate the model is operating outside its training domain.

**Methods:**
- Population Stability Index (PSI) for categorical and binned continuous features
- Kolmogorov-Smirnov test for continuous feature distributions
- Jensen-Shannon divergence for probability distributions

**Thresholds:**
| PSI Value | Interpretation | Action |
|-----------|---------------|--------|
| < 0.10 | No significant drift | Continue monitoring |
| 0.10–0.25 | Moderate drift | Investigate, increase monitoring frequency |
| > 0.25 | Significant drift | Trigger revalidation assessment |

**Frequency:** Daily for T1/T2, weekly for T3, monthly for T4.

### 2. Model Performance
Track model accuracy against ground truth as it becomes available.

**Metrics to monitor:**
- Primary business metric (e.g., default rate for credit models, false positive rate for fraud)
- Statistical performance metrics (AUC, precision, recall) computed on rolling windows
- Calibration — are predicted probabilities aligned with observed outcomes?

**Degradation thresholds:**
- **Warning:** Performance drops >5% relative from validation baseline
- **Critical:** Performance drops >10% relative or falls below absolute minimum threshold
- **Action:** Performance drop sustained for >7 days triggers revalidation

### 3. Prediction Distribution
Monitor the distribution of model outputs to detect shifts that may not be captured by input drift or performance monitoring.

- Track prediction score distributions over time
- Monitor decision rates (e.g., approval rate, flag rate) against expected baselines
- Alert on sudden distribution shifts even if input data appears stable

### 4. Operational Health
- **Latency:** p50, p95, p99 response times against SLA thresholds
- **Error rate:** Failed predictions, timeouts, malformed inputs
- **Throughput:** Requests per second against capacity planning estimates
- **Availability:** Uptime tracking against SLA targets
- **Resource utilization:** CPU, memory, GPU utilization for cost and capacity management

### 5. Fairness Monitoring (T1, T2)
Continue fairness assessments in production:
- Monitor performance metrics across demographic subgroups
- Track decision rates (e.g., approval rates) across subgroups
- Alert if disparate impact ratios cross defined thresholds
- Frequency: Monthly for T1, quarterly for T2

## Alert Configuration

### Severity Levels

| Severity | Description | Response Time | Escalation |
|----------|-------------|---------------|------------|
| P1 — Critical | Model producing incorrect outputs at scale, or complete system failure | 15 minutes | On-call → Engineering Lead → AI Risk Committee |
| P2 — High | Significant performance degradation or drift detected | 4 hours | On-call → Engineering Lead |
| P3 — Medium | Moderate drift or minor performance decline | 24 hours | Assigned to model owner |
| P4 — Low | Informational anomaly, no immediate action needed | Next business day | Logged for review |

### Alert Routing
- P1/P2 alerts must page the on-call engineer and notify the model owner simultaneously
- P3 alerts create tickets in the team's tracking system
- P4 alerts are logged to the monitoring dashboard for periodic review

## Retraining Triggers

A model retraining cycle is triggered when:

1. **Performance degradation:** Sustained performance drop beyond warning threshold for >7 days
2. **Data drift:** PSI > 0.25 on multiple key features sustained for >14 days
3. **Scheduled cadence:** T1 models retrained at minimum annually, T2 biannually
4. **Business change:** Material change to the business process the model supports
5. **Regulatory requirement:** Examiner finding or new regulatory guidance

### Retraining Process
Retraining follows the same lifecycle as initial development:
- New training data must meet the same quality standards
- Retrained model must pass validation (with updated challenger comparison)
- Deployment follows the same gate process (shadow/canary as appropriate)
- The retrained model is a new version — it does not overwrite the previous version

## Quarterly Model Review

For T1 and T2 systems, a quarterly review must cover:

1. **Performance summary:** Trend analysis of all monitored metrics
2. **Drift analysis:** Summary of data and prediction drift observations
3. **Incident review:** Any P1/P2 incidents, root causes, and remediations
4. **Fairness update:** Updated fairness metrics and any observed disparities
5. **Retraining assessment:** Is retraining warranted? Document decision rationale.
6. **Risk tier reassessment:** Has anything changed that would affect the risk classification?

The quarterly review is documented and presented to the AI Risk Committee for T1 systems.

