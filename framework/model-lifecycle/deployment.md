# Deployment Gates and Standards

## Purpose

No AI system reaches production without meeting defined deployment criteria. This is not about slowing down deployment: it is about ensuring that what reaches production is safe, monitored, and reversible.

This document is not a separate gate model. The [governance workflow](../governance-operations/governance-workflow.md) is the only process; the checklists below are the detailed criteria for traditional ML models at its stages. Which evidence each tier must produce is set by the [minimum evidence pack by tier](../governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier). Control DA-003 (deployment gates passed) means the criteria below that apply to the system's tier are met.

## Pre-Deployment Criteria by Workflow Stage

### Development Complete (Stage 4, All Tiers)
- [ ] Model development document finalized
- [ ] Model card completed
- [ ] Code peer-reviewed and merged to main branch
- [ ] Unit tests passing with adequate coverage
- [ ] All training artifacts versioned and stored

### Validation Approved (Stage 5)

Depth by tier, per [validation.md](validation.md#validation-independence): T1 full independent validation by MRM; T2 reduced-scope independent validation by a qualified reviewer outside the development team; T3 peer review; T4 self-test.

- [ ] Validation report (T1/T2) or peer review record (T3) completed with pass recommendation; self-test recorded (T4)
- [ ] All critical findings resolved
- [ ] Major findings have documented remediation plan with timeline
- [ ] Challenger model benchmarked (T1 required, T2 recommended)

### Risk and Compliance Review (Stage 2, Confirmed at Stage 7; T1, T2)
- [ ] Risk assessment completed, tier confirmed and approved (AI Risk Committee for T1, AI Risk for T2)
- [ ] Impact assessment reviewed by compliance
- [ ] Data privacy review completed: DPIA screening for any system processing personal data (all tiers), full DPIA where required
- [ ] Fairness testing results reviewed and approved
- [ ] Regulatory mapping documented (which regulations apply, how requirements are met)

### Operational Readiness (Stages 6 and 8; T1, T2)
- [ ] Monitoring dashboards deployed and tested
- [ ] Alert thresholds configured and escalation paths defined
- [ ] Fallback mechanism tested (what happens when the model is unavailable)
- [ ] Runbook documented (incident response, rollback procedure, on-call contacts)
- [ ] Load testing completed against production traffic estimates
- [ ] Security review completed (access controls, data encryption, API security)

T3 and T4 systems need the monitoring and alerting their tier requires in [monitoring.md](monitoring.md) before traffic is enabled.

### Deployment Approval (Stage 7, All Tiers)
- [ ] Deployment approval recorded (DA-002): AI Risk Committee with the CISO, and the DPO if personal data is processed (T1); Head of AI and Business Unit Head (T2); team lead and business owner (T3); team lead (T4). See [Approvals by Tier](../operating-model/roles-responsibilities.md#approvals-by-tier)
- [ ] Independent validation sign-off on file (MRM for T1; MRM or second line for T2)
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
