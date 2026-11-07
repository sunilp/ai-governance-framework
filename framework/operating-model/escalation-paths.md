# Escalation Paths

## Purpose

When something goes wrong with an AI system — or when a governance control identifies a material concern — clear escalation paths ensure the right people are informed and empowered to act.

## Severity Classification

This section is the single definition of incident severity for every AI system: traditional ML, GenAI and agentic. Other documents may list domain examples per severity, but they do not redefine the levels. The response SLA depends on severity, not on tier.

| Severity | Definition | Response SLA |
|----------|------------|--------------|
| S1 Critical | Harm to customers, financial loss, a regulatory breach or a data exposure has occurred or is occurring. | 15 minutes |
| S2 High | Incorrect or harmful output reached customers or external parties with no confirmed harm yet, or a key control failed on a T1/T2 system. | 4 hours |
| S3 Medium | A problem detected internally before it reached anyone outside, or quality degraded but still within tolerance on a T1/T2 system. | 24 hours |
| S4 Low | Minor issue, no external exposure, no control failure. | Next business day |

The response SLA is the time to acknowledge the incident and start containment.

**Tier floor:** any incident on a T1 system that reached customers is at least S2.

### Follow-Up by Severity

| Severity | Root cause | Post-mortem |
|----------|-----------|-------------|
| S1 | Identified within 48 hours | Report within 1 week (IR-004) |
| S2 | Identified within 48 hours | Report within 2 weeks (IR-004) |
| S3 | Documented within 10 business days | Not required |
| S4 | Tracked in the team backlog | Not required |

### Notifications

- **S1:** AI Risk Committee chair within 1 hour. Every S1 is a material incident: the Board Risk Committee is notified within 24 hours (see [board-reporting.md](board-reporting.md#material-incident-criteria)).
- **S2:** Board Risk Committee notified when the incident meets the [material incident criteria](board-reporting.md#material-incident-criteria).
- **Regulators:** see [Regulatory Notification](#regulatory-notification) below.

---

### S1 Critical

**Examples:**
- Credit model approving all applications regardless of risk
- Fraud detection system failing to flag known fraud patterns
- Customer PII exposed through model API
- Discriminatory outcomes identified in production decisions
- A customer assistant shows one customer another customer's account details
- An agent executes payments or changes production records outside its authority

**Response time:** 15 minutes
**Escalation chain:**
1. On-call engineer assesses and initiates rollback, kill switch or fallback if needed
2. AI lead and AI Operations notified immediately; incident commander assigned
3. Business owner notified within 30 minutes
4. AI Risk Committee chair and CTO notified within 1 hour
5. Compliance notified if regulatory implications exist; DPO notified if personal data is involved
6. Board Risk Committee notified within 24 hours (every S1)

**Actions:**
- Immediate rollback to previous model version or fallback mechanism
- Customer impact assessment initiated
- Incident war room established
- External communication assessed (regulator notification, customer notification)

---

### S2 High

**Examples:**
- Model accuracy on a T1/T2 system dropped 15% over the past week, outside tolerance, with no confirmed customer harm yet
- PSI > 0.25 on multiple key features sustained for 14+ days while the model keeps making customer decisions
- Fairness control breached: disparate impact ratio below threshold for a protected group
- Critical validation finding discovered post-deployment
- A chatbot gave customers incorrect product or fee information; no customer is known to have acted on it
- A guardrail, PII redaction step or agent permission boundary found disabled on a T1/T2 system, with no confirmed exposure

**Response time:** 4 hours
**Escalation chain:**
1. On-call engineer documents the issue and assesses impact
2. AI lead investigates root cause
3. AI Operations assesses operational implications
4. Business owner informed within 8 hours
5. MRM or AI Risk (second line) informed within 24 hours
6. Escalated to AI Risk Committee at next meeting (or sooner if warranted); Board Risk Committee notified if the incident meets the material incident criteria

**Actions:**
- Increased monitoring frequency
- Root cause identified within 48 hours
- Retraining assessment or model replacement evaluation
- Impact assessment on affected decisions

---

### S3 Medium

**Examples:**
- Model accuracy declined 5-10% over the past month, still within tolerance
- PSI between 0.10 and 0.25 on some features
- Non-critical validation finding identified
- Intermittent latency spikes affecting SLA
- Hallucination rate on a T1/T2 assistant rising but still below its tier threshold
- Internal testing finds a prompt injection path or an over-broad agent tool permission before anyone outside is affected

**Response time:** 24 hours
**Escalation chain:**
1. Assigned to the system owner for investigation
2. AI lead reviews within 48 hours
3. Reported at monthly Model Review Board

**Actions:**
- Investigation, with root cause documented within 10 business days
- Monitoring threshold review
- Remediation plan with timeline

---

### S4 Low

**Examples:**
- Slight shift in prediction distribution within normal bounds
- Feature importance ranking change without performance impact
- Documentation gap identified
- Formatting errors in an internal assistant's outputs
- Small rise in refusal rate on an internal T4 tool with no user impact

**Response time:** Next business day
**Escalation chain:**
1. Logged by monitoring system
2. Reviewed at weekly AI Operations Stand-up

**Actions:**
- Logged for trend analysis
- Tracked in the team backlog and addressed in normal workflow

## Alert Priority to Incident Severity

Monitoring raises alerts at priority P1 to P4. Incident severity S1 to S4 is a separate classification, made when an incident is declared. Use P-levels only for alerts and S-levels only for incidents. Alert criteria and response SLAs are defined in [LLM monitoring](../llm-lifecycle/monitoring.md#alerting-and-escalation) and [model monitoring](../model-lifecycle/monitoring.md#alert-configuration).

| Alert priority | Acknowledgement | Incident severity if one is declared |
|----------------|-----------------|--------------------------------------|
| P1 | Within 15 minutes, then triaged | S1 or S2 if external impact is confirmed |
| P2 | Within 1 hour | Usually S2 or S3 |
| P3, P4 | Within the monitoring standard's response SLA | S3 or S4, or no incident |

If triage does not confirm external impact, classify against the definitions in [Severity Classification](#severity-classification). Once an incident is declared, its severity sets the response SLA, follow-ups and notifications. Incidents can also be declared without an alert, for example from a customer complaint, an internal review or an audit finding.

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

