# Escalation Paths

## Purpose

When something goes wrong with an AI system — or when a governance control identifies a material concern — clear escalation paths ensure the right people are informed and empowered to act.

## Severity Classification

### Severity 1 — Critical
**Definition:** AI system producing materially incorrect outputs at scale, complete system failure affecting customers, data breach involving model training data, or regulatory violation identified.

**Examples:**
- Credit model approving all applications regardless of risk
- Fraud detection system failing to flag known fraud patterns
- Customer PII exposed through model API
- Discriminatory outcomes identified in production decisions

**Response time:** 15 minutes
**Escalation chain:**
1. On-call engineer assesses and initiates rollback if needed
2. Data Science Lead and MLOps Lead notified immediately
3. Business Owner notified within 30 minutes
4. AI Risk Committee chair and CTO notified within 1 hour
5. Compliance notified if regulatory implications exist
6. Board Risk Committee notified within 24 hours (if customer impact)

**Actions:**
- Immediate rollback to previous model version or fallback mechanism
- Customer impact assessment initiated
- Incident war room established
- External communication assessed (regulator notification, customer notification)

---

### Severity 2 — High
**Definition:** Significant performance degradation, sustained data drift beyond thresholds, fairness metric breach, or validation finding that should have blocked deployment.

**Examples:**
- Model accuracy dropped 15% over the past week
- PSI > 0.25 on multiple key features sustained for 14+ days
- Disparate impact ratio below threshold for a protected group
- Critical validation finding discovered post-deployment

**Response time:** 4 hours
**Escalation chain:**
1. On-call engineer documents the issue and assesses impact
2. Data Science Lead investigates root cause
3. MLOps Lead assesses operational implications
4. Business Owner informed within 8 hours
5. MRM informed within 24 hours
6. Escalated to AI Risk Committee at next meeting (or sooner if warranted)

**Actions:**
- Increased monitoring frequency
- Root cause analysis initiated
- Retraining assessment or model replacement evaluation
- Impact assessment on affected decisions

---

### Severity 3 — Medium
**Definition:** Moderate performance decline, early drift signals, minor validation findings, or operational anomalies that do not immediately affect decision quality.

**Examples:**
- Model accuracy declined 5–10% over the past month
- PSI between 0.10–0.25 on some features
- Non-critical validation finding identified
- Intermittent latency spikes affecting SLA

**Response time:** 24 hours
**Escalation chain:**
1. Assigned to model owner for investigation
2. Data Science Lead reviews within 48 hours
3. Reported at monthly Model Review Board

**Actions:**
- Investigation and root cause analysis
- Monitoring threshold review
- Remediation plan with timeline

---

### Severity 4 — Low
**Definition:** Informational anomaly, minor drift signals within acceptable range, or process improvement opportunity.

**Examples:**
- Slight shift in prediction distribution within normal bounds
- Feature importance ranking change without performance impact
- Documentation gap identified

**Response time:** Next business day
**Escalation chain:**
1. Logged by monitoring system
2. Reviewed at weekly AI Operations Stand-up

**Actions:**
- Logged for trend analysis
- Addressed in normal workflow

## Communication Templates

### Severity 1 — Initial Notification

```
SUBJECT: [S1] AI System Incident — {System Name}

Severity: 1 — Critical
System: {System Name} (ID: {system_id})
Tier: {T1/T2}
Time detected: {timestamp UTC}
Detected by: {monitoring alert / manual review / customer report}

Issue: {Brief description of the issue}

Impact:
- Affected customers: {estimated count}
- Affected decisions: {estimated count}
- Financial exposure: {if known}

Immediate actions taken:
- {e.g., Model rolled back to version X}
- {e.g., Fallback mechanism activated}

Next steps:
- Root cause investigation underway
- War room: {link}
- Next update: {time}

Incident commander: {name}
```

### Severity 2 — Notification

```
SUBJECT: [S2] AI System Alert — {System Name}

Severity: 2 — High
System: {System Name} (ID: {system_id})
Time detected: {timestamp UTC}

Issue: {Description}
Impact assessment: {Current assessment of customer/business impact}
Root cause: {Known / Under investigation}

Actions:
- {Action 1}
- {Action 2}

Owner: {name}
Next update: {time}
```

## Regulatory Notification

For incidents that may require regulatory notification:

1. **Compliance assesses** whether notification obligations are triggered (within 24 hours of Severity 1)
2. **Legal reviews** the notification content
3. **Regulatory affairs** submits the notification through established channels
4. **AI Risk Committee** is informed of the notification

Regulatory notification triggers include:
- Material model failure affecting customer outcomes
- Data breach involving model training or prediction data
- Discriminatory outcomes identified in production
- Failure of a model subject to specific supervisory requirements

