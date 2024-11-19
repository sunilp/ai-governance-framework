# Deployment Gates and Standards

## Purpose

No AI system reaches production without passing through defined gates. The number and rigor of gates is proportional to the system's risk tier. This is not about slowing down deployment — it is about ensuring that what reaches production is safe, monitored, and reversible.

## Pre-Deployment Gates

### Gate 1: Development Complete (All Tiers)
- [ ] Model development document finalized
- [ ] Model card completed
- [ ] Code peer-reviewed and merged to main branch
- [ ] Unit tests passing with adequate coverage
- [ ] All training artifacts versioned and stored

### Gate 2: Validation Approved (T1, T2, T3)
- [ ] Validation report completed with pass recommendation
- [ ] All critical findings resolved
- [ ] Major findings have documented remediation plan with timeline
- [ ] Challenger model benchmarked (T1 required, T2 recommended)

### Gate 3: Risk and Compliance Review (T1, T2)
- [ ] Risk assessment completed and tier confirmed
- [ ] Impact assessment reviewed by compliance
- [ ] Data privacy review completed (DPIA where required)
- [ ] Fairness testing results reviewed and approved
- [ ] Regulatory mapping documented (which regulations apply, how requirements are met)

### Gate 4: Operational Readiness (T1, T2)
- [ ] Monitoring dashboards deployed and tested
- [ ] Alert thresholds configured and escalation paths defined
- [ ] Fallback mechanism tested (what happens when the model is unavailable)
- [ ] Runbook documented (incident response, rollback procedure, on-call contacts)
- [ ] Load testing completed against production traffic estimates
- [ ] Security review completed (access controls, data encryption, API security)

### Gate 5: Deployment Approval (T1)
- [ ] AI Risk Committee approval obtained
- [ ] Senior management sign-off documented
- [ ] Model Risk Management sign-off documented
- [ ] Deployment window agreed with operations team

## Deployment Patterns

### Shadow Deployment
Run the new model alongside the existing system without affecting production decisions. Compare outputs for a defined period.

**When to use:** T1 and T2 systems, or any system replacing an existing production model.

**Duration:** Minimum 2 weeks for T1, 1 week for T2.

**Exit criteria:**
- Output distribution aligns with expectations
- No unexpected edge cases identified
- Performance metrics match or exceed validation results

### Canary Deployment
Route a small percentage of production traffic to the new model. Gradually increase traffic as confidence grows.

**When to use:** T2 and T3 systems where shadow deployment is not feasible.

**Traffic ramp:**
- Day 1–3: 5% of traffic
- Day 4–7: 25% of traffic
- Day 8–14: 50% of traffic
- Day 15+: 100% (full rollout)

**Automatic rollback triggers:**
- Error rate exceeds 2x baseline
- Latency exceeds SLA threshold
- Model output distribution shifts beyond defined bounds

### Direct Deployment
Deploy directly to production with monitoring.

**When to use:** T3 and T4 systems with low risk and well-understood behavior.

## Rollback Procedures

Every deployment must have a tested rollback plan:

1. **Model rollback:** Revert to the previous model version. Model registry must retain the last 3 production versions.
2. **Feature rollback:** If a feature pipeline change is the root cause, revert the pipeline independently.
3. **Full system rollback:** If the model service itself is compromised, fall back to the defined backup mechanism (e.g., business rules engine, manual process).

**Rollback SLAs:**
| Tier | Maximum Rollback Time |
|------|----------------------|
| T1 | 15 minutes |
| T2 | 1 hour |
| T3 | 4 hours |
| T4 | 24 hours |

## Post-Deployment Verification

Within the first 48 hours of full production deployment:

- [ ] Confirm model is receiving expected input volume
- [ ] Verify output distribution matches validation expectations
- [ ] Confirm monitoring alerts are firing correctly (test with synthetic trigger)
- [ ] Review initial production predictions for quality
- [ ] Confirm audit logging is capturing all required fields
- [ ] Update AI system inventory with production deployment date and version
