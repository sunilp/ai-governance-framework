# Responsible AI Pre-Deployment Checklist

## Purpose

This checklist must be completed before any AI system is deployed to production. The depth of evidence required is proportional to the system's risk tier.

---

## 1. Fairness

| Check | T1 | T2 | T3 | T4 | Evidence |
|-------|----|----|----|----|----------|
| Protected attributes identified and documented | Required | Required | Required | - | Risk assessment |
| Proxy feature analysis completed | Required | Required | Recommended | - | Development document |
| Bias testing across demographic subgroups | Required | Required | Recommended | - | Validation report |
| Disparate impact ratios calculated and within thresholds | Required | Required | - | - | Validation report |
| Fairness metrics selected with documented justification | Required | Required | - | - | Model card |
| Mitigation measures documented (if bias detected) | Required | Required | - | - | Development document |
| Ongoing fairness monitoring configured | Required | Required | - | - | Monitoring dashboard |

**Sign-off:** Model Risk Management (T1), Senior Data Scientist (T2), Team Lead (T3)

---

## 2. Transparency

| Check | T1 | T2 | T3 | T4 | Evidence |
|-------|----|----|----|----|----------|
| Model methodology documented and justified | Required | Required | Required | Required | Development document |
| Individual prediction explanations available | Required | Required | Recommended | - | Explainability module |
| Global feature importance documented | Required | Required | Required | - | Model card |
| Known limitations and failure modes documented | Required | Required | Required | Recommended | Model card |
| User-facing disclosure (for customer-facing systems) | Required | Required | Required | - | Product documentation |
| Decision logic auditable by regulators | Required | Required | - | - | Audit trail + documentation |

**Sign-off:** Compliance (T1/T2), Model Owner (T3/T4)

---

## 3. Privacy

| Check | T1 | T2 | T3 | T4 | Evidence |
|-------|----|----|----|----|----------|
| Data Protection Impact Assessment (DPIA) completed | Required | Required | If PII | - | DPIA document |
| PII identified and minimized | Required | Required | Required | Recommended | Data inventory |
| Consent/legal basis for data processing documented | Required | Required | Required | - | Privacy review |
| Data retention policies defined and implemented | Required | Required | Required | Recommended | Data governance config |
| Cross-border data transfer assessed | Required | Required | If applicable | - | Privacy review |
| Right-to-delete mechanism tested | Required | Required | If PII | - | Test report |

**Sign-off:** Data Protection Officer (T1/T2), Privacy team (T3)

---

## 4. Security

| Check | T1 | T2 | T3 | T4 | Evidence |
|-------|----|----|----|----|----------|
| Access controls implemented (least privilege) | Required | Required | Required | Required | Security config |
| API authentication and authorization configured | Required | Required | Required | Required | Security review |
| Input validation implemented | Required | Required | Required | Recommended | Code review |
| Adversarial robustness tested | Required | Required | Recommended | - | Validation report |
| Prompt injection defenses (LLM systems) | Required | Required | Required | - | Security test report |
| Model artifact encryption at rest and in transit | Required | Required | Required | Recommended | Infrastructure config |
| Penetration testing completed | Required | Recommended | - | - | Pentest report |

**Sign-off:** Security team (T1/T2), Engineering Lead (T3/T4)

---

## 5. Accountability

| Check | T1 | T2 | T3 | T4 | Evidence |
|-------|----|----|----|----|----------|
| Model owner identified and documented | Required | Required | Required | Required | AI system inventory |
| Escalation paths defined | Required | Required | Required | Recommended | Operating model docs |
| Incident response plan documented | Required | Required | Required | Recommended | Runbook |
| Rollback procedure tested | Required | Required | Recommended | - | Deployment test report |
| Monitoring and alerting configured | Required | Required | Required | Recommended | Monitoring dashboard |
| Audit logging enabled | Required | Required | Required | Recommended | Audit trail config |
| Quarterly review scheduled | Required | Required | Annually | - | Calendar/tracker |

**Sign-off:** AI Risk Committee (T1), Senior Management (T2), Team Lead (T3/T4)

---

## Final Approval

| Role | T1 | T2 | T3 | T4 |
|------|----|----|----|----|
| Model Owner | Required | Required | Required | Required |
| Model Risk Management | Required | Required | - | - |
| Compliance | Required | Required | - | - |
| Security | Required | Recommended | - | - |
| AI Risk Committee | Required | - | - | - |
| Senior Management Sponsor | Required | Required | - | - |

All sign-offs must be documented with name, role, date, and any conditions or caveats.
