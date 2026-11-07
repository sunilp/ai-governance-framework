# GenAI Incident Report Template

This template is for GenAI and agentic systems. For traditional ML systems, use the [AI system incident report](incident-report-template.md).

## Instructions

Complete this template for any incident involving a GenAI system. Classify severity using the definitions in [escalation-paths.md](../framework/operating-model/escalation-paths.md#severity-classification); any incident on a T1 system that reached customers is at least S2. Submit within 24 hours of incident resolution. For S1 and S2, record the root cause within 48 hours and complete the post-mortem within 1 week (S1) or 2 weeks (S2), per IR-004.

---

## 1. Incident Summary

| Field | Value |
|-------|-------|
| Incident ID | GEN-YYYY-NNN |
| Severity | S1 Critical / S2 High / S3 Medium / S4 Low |
| Triggering alert priority (if any) | P1 / P2 / P3 / P4 / None |
| Status | Open / Investigating / Mitigated / Resolved / Closed |
| AI System | |
| Risk Tier | T1 / T2 / T3 / T4 |
| Incident Commander | |
| Detection Time (UTC) | |
| Mitigation Time (UTC) | |
| Resolution Time (UTC) | |
| Duration | |

---

## 2. Incident Classification

### Incident Type

- [ ] Hallucination: System generated factually incorrect or fabricated content
- [ ] Prompt injection: Adversarial input manipulated system behavior
- [ ] Data leakage: Sensitive data exposed through model outputs
- [ ] PII exposure: Personally identifiable information in outputs
- [ ] Bias incident: Discriminatory or biased output detected
- [ ] Toxicity: Harmful, offensive, or inappropriate content generated
- [ ] Safety bypass: Model safety controls circumvented
- [ ] Unauthorized action: Agentic system took unintended action
- [ ] Service degradation: Quality or performance fell below thresholds
- [ ] Vendor incident: Issue with external model provider
- [ ] Cost overrun: Unexpected or unauthorized cost spike
- [ ] Other: _______________

### Detection Method

- [ ] Automated monitoring alert
- [ ] Guardrail trigger
- [ ] User complaint / feedback
- [ ] Human reviewer
- [ ] Internal audit / spot-check
- [ ] External report
- [ ] Vendor notification
- [ ] Other: _______________

---

## 3. Incident Description

**What happened?**

> [Clear, factual description of the incident]

**What was the expected behavior?**

> [What should the system have done?]

**What was the actual behavior?**

> [What did the system actually do?]

**Specific examples (if available):**

> [Include sanitized examples of problematic inputs/outputs. Redact PII.]

---

## 4. Impact Assessment

### Customer Impact

| Question | Response |
|----------|----------|
| Were customers affected? | Yes / No |
| Number of customers impacted | |
| Nature of customer impact | |
| Were customers notified? | Yes / No / Not required |
| Is customer remediation required? | Yes / No |
| Remediation actions | |

### Financial Impact

| Question | Response |
|----------|----------|
| Estimated financial impact | |
| Direct costs (remediation, compensation) | |
| Indirect costs (operational, reputational) | |

### Regulatory Impact

| Question | Response |
|----------|----------|
| Does this trigger regulatory notification? | Yes / No / Under review |
| Applicable regulations | |
| Notification deadline | |
| Notification status | |

### Data Impact

| Question | Response |
|----------|----------|
| Was sensitive data exposed? | Yes / No |
| Data classification of exposed data | |
| Number of records affected | |
| Has data been contained? | Yes / No |
| Is breach notification required (GDPR Art. 33/34)? | Yes / No / Under review |

---

## 5. Root Cause Analysis

### Immediate Cause

> [What directly caused the incident?]

### Contributing Factors

> [What conditions enabled the incident to occur?]

### Root Cause

> [The underlying systemic issue]

### Root Cause Category

- [ ] Prompt design flaw
- [ ] Guardrail gap or failure
- [ ] Data quality issue (RAG corpus, training data)
- [ ] Model behavior change (vendor update, drift)
- [ ] Monitoring gap
- [ ] Human process failure
- [ ] Infrastructure issue
- [ ] Vendor issue
- [ ] Unknown (investigation ongoing)

---

## 6. Timeline

| Time (UTC) | Event |
|-----------|-------|
| | Incident occurred / started |
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

> [Detection, response, communication that worked effectively]

### What could be improved?

> [Gaps in detection, response, communication, or process]

### Prevention Measures

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
| Update prompt/guardrails | | | |
| Re-evaluate risk tier | | | |
| Update incident playbook | | | |
| Communicate lessons learned | | | |
| Schedule follow-up review | | | |

---

## 10. Approvals

| Role | Name | Date | Sign-off |
|------|------|------|----------|
| Incident Commander | | | [ ] |
| AI Risk Lead | | | [ ] |
| Business Owner | | | [ ] |
| Compliance (if regulatory impact) | | | [ ] |
| CISO (if data/security impact) | | | [ ] |
