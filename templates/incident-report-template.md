# AI System Incident Report

This template is for traditional ML systems. For GenAI and agentic systems, use the [GenAI incident report](incident-report-genai.md).

## Instructions

Complete this template for any incident involving a traditional ML system. Classify severity using the definitions in [escalation-paths.md](../framework/operating-model/escalation-paths.md#severity-classification); any incident on a T1 system that reached customers is at least S2. For S1 and S2, record the root cause within 48 hours and complete the post-mortem within 1 week (S1) or 2 weeks (S2), per IR-004.

---

## 1. Incident Summary

| Field | Value |
|-------|-------|
| Incident ID | |
| Severity | S1 Critical / S2 High / S3 Medium / S4 Low |
| Triggering alert priority (if any) | P1 / P2 / P3 / P4 / None |
| Status | Open / Investigating / Mitigated / Resolved / Closed |
| AI System | |
| System ID | |
| Risk Tier | T1 / T2 / T3 / T4 |
| Incident Commander | |
| Detection Time (UTC) | |
| Mitigation Time (UTC) | |
| Resolution Time (UTC) | |
| Duration | |
| Report Author | |
| Report Date | |

---

## 2. Incident Classification

### Detection Method

- [ ] Automated monitoring alert
- [ ] Manual review / spot check
- [ ] Customer complaint
- [ ] Internal user report
- [ ] Regulatory examination
- [ ] Other: _______________

**Detection details:** _Which alert, metric, or observation identified the issue?_

**Time to detect:** _How long was the system operating in a degraded or failed state before detection?_

---

## 3. Incident Description

**What happened?**

> [Clear, factual description of the incident]

**What was the expected behavior?**

> [What should the system have done?]

**What was the actual behavior?**

> [What did the system actually do?]

**Specific examples (if available):**

> [Include sanitized examples of affected inputs, scores or decisions. Redact PII.]

---

## 4. Impact Assessment

### Customer Impact

| Question | Response |
|----------|----------|
| Were customers affected? | Yes / No |
| Number of customers impacted | |
| Types of decisions affected | |
| Were incorrect decisions communicated to customers? | Yes / No |
| Were any customers materially harmed? | Yes / No |
| Were customers notified? | Yes / No / Not required |
| Is customer remediation required? | Yes / No |
| Remediation actions | |

### Financial Impact

| Question | Response |
|----------|----------|
| Estimated financial impact | |
| Direct costs (losses, remediation, compensation) | |
| Indirect costs (operational, reputational) | |

### Regulatory Impact

| Question | Response |
|----------|----------|
| Does this trigger regulatory notification? | Yes / No / Under review |
| Applicable regulations | |
| Notification deadline | |
| Notification status | |
| Are there examination implications? | |

### Data Impact

| Question | Response |
|----------|----------|
| Was sensitive data exposed? | Yes / No |
| Data classification of exposed data | |
| Number of records affected | |
| Has data been contained? | Yes / No |
| Is breach notification required (GDPR Art. 33/34)? | Yes / No / Under review |

### Reputational Impact

| Question | Response |
|----------|----------|
| Was the incident visible to customers or the public? | Yes / No |
| Media coverage | |

---

## 5. Root Cause Analysis

### Immediate Cause

> [What directly caused the incident?]

### Contributing Factors

> [What conditions enabled the incident to occur or kept it from being caught earlier?]

### Root Cause

> [The underlying systemic issue that, if addressed, would prevent recurrence]

### Root Cause Category

- [ ] Data quality issue
- [ ] Model degradation / drift
- [ ] Feature pipeline failure
- [ ] Infrastructure / serving failure
- [ ] Deployment error
- [ ] Monitoring gap
- [ ] Process / governance gap
- [ ] Third-party dependency failure
- [ ] Unknown (investigation ongoing)
- [ ] Other: _______________

---

## 6. Timeline

| Time (UTC) | Event |
|-----------|-------|
| | Incident occurred / started (estimated) |
| | Incident detected |
| | Incident confirmed |
| | Incident commander assigned |
| | Initial mitigation applied |
| | [Additional events] |
| | Incident resolved |
| | Post-incident review completed |

---

## 7. Response and Remediation

### Immediate Actions Taken

| # | Action | Owner | Status |
|---|--------|-------|--------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Remediation Actions

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## 8. Lessons Learned

### What went well?

> [Detection, response, communication or governance that worked as intended]

### What could be improved?

> [Gaps in detection, response, communication, or process]

### Prevention Measures

Consider monitoring enhancements, model improvements, process changes, training and awareness, infrastructure improvements and new governance controls.

| # | Measure | Description | Owner | Due Date |
|---|---------|-------------|-------|----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## 9. Follow-Up

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Update risk assessment | | | |
| Update monitoring/alerting | | | |
| Retrain, recalibrate or roll back the model | | | |
| Re-evaluate risk tier | | | |
| Update incident playbook | | | |
| Communicate lessons learned | | | |
| Schedule follow-up review | | | |

---

## 10. Approvals

| Role | Name | Date | Sign-off |
|------|------|------|----------|
| Incident Commander | | | [ ] |
| Model Owner | | | [ ] |
| Head of MRM (T1/T2) | | | [ ] |
| Compliance (if regulatory impact) | | | [ ] |
