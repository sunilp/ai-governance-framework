# Governance Review Cadence

## Purpose

Governance is not a one-time activity. It requires a rhythm of reviews, escalations, and decisions that keep AI systems aligned with organizational risk appetite and regulatory expectations.

## Cadence by Tier

| Activity | T1 | T2 | T3 | T4 |
|----------|----|----|----|----|
| Formal governance review (RV-001) | Quarterly | Semi-annual | Annual | Annual self-assessment |
| Metrics review (operational) | Daily dashboard check by AI Operations, plus a monthly system-owner review | Weekly | Monthly | Quarterly |
| Revalidation (independent for T1/T2) | Annual, and on material change | Every 24 months, and on material change | On material change (peer re-review) | On material change (peer re-review) |
| Risk re-assessment (re-tiering check) | At every formal governance review, and on material change | Same | Same | Same |

Who performs validation at each tier is set in [validation.md](../model-lifecycle/validation.md#validation-independence). Production evaluation cadences for GenAI systems are in [LLM monitoring](../llm-lifecycle/monitoring.md#production-evaluation).

## Meeting Structure

### Monthly: AI Risk Committee

The AI Risk Committee meets monthly. One meeting each quarter is the full-portfolio meeting, which also reviews the quarterly board report (see [board-reporting.md](board-reporting.md)).

**Attendees:** CRO (chair), CTO, Head of MRM, Head of Compliance, Head of Data Science, Business Line Heads (as needed). The CISO attends for T1 deployment and model selection approvals, and the DPO when the system processes personal data.

**T1 approvals:** T1 risk assessments, model selections, deployments and exceptions are approved at the monthly meeting. If a decision cannot wait, the chair convenes an out-of-cycle session within 10 business days of the request.

**Monthly agenda:**
1. **T1 approvals** (as needed)
   - Risk assessments, model selection, deployments, exceptions
   - Risk tier changes
2. **T1 system health** (20 min)
   - Monthly system-owner metrics reviews
   - S1 and S2 incidents since the last meeting and their remediation
3. **Escalations** (15 min)
   - Items escalated by the Model Review Board, AI Risk or Compliance
4. **Decisions and actions** (10 min)
   - Assign actions with owners and deadlines

**Quarterly full-portfolio agenda:**
1. **AI system portfolio review** (15 min)
   - New systems added to production since last meeting
   - Systems retired or materially changed
   - Current inventory summary by tier
2. **T1 system deep dives** (30 min)
   - Performance trends and drift analysis
   - Fairness monitoring results
   - Incident summary and remediations
   - Retraining decisions and validations completed
3. **Regulatory and policy updates** (15 min)
   - New regulations or supervisory guidance affecting AI
   - Internal policy changes proposed
   - Examination findings and remediation status
4. **Risk appetite and thresholds** (15 min)
   - Review of risk appetite statements for AI
   - Threshold adjustments based on experience
   - Emerging risks or systemic concerns
5. **Board report and decisions** (15 min)
   - Approve the quarterly AI risk report for the board
   - Approve/reject T1 system deployments and risk tier changes
   - Assign actions with owners and deadlines

**Output:** Meeting minutes with decisions, action items, and owners. Distributed within 5 business days.

---

### Monthly: Model Review Board

**Attendees:** Head of MRM (chair), Data Science Leads, MLOps Lead, Compliance representative

**Agenda:**
1. **Pipeline review** (20 min)
   - Models in development — status, timeline, tier
   - Models in validation — findings, blockers
   - Models pending deployment — gate status
2. **Production model health** (20 min)
   - Monitoring dashboard review — T1 and T2 systems
   - Models with active alerts or drift warnings
   - Retraining pipeline status
3. **Validation backlog** (10 min)
   - Upcoming validations and resource allocation
   - Overdue validations and remediation plans
4. **Operational issues** (10 min)
   - Incidents since last meeting
   - Infrastructure or tooling concerns
   - Staffing and capacity

**Output:** Status report and escalation items for AI Risk Committee (if applicable).

---

### Weekly: AI Operations Stand-up

**Attendees:** MLOps Lead, on-call engineers, Data Science Lead (rotating)

**Agenda:**
1. **Monitoring review** (10 min)
   - Active alerts and their status
   - Systems with degraded performance
   - Drift warnings requiring investigation
2. **Deployment status** (5 min)
   - Deployments scheduled this week
   - Shadow/canary results from active deployments
3. **Incidents and on-call** (5 min)
   - Open incidents and remediation status
   - On-call handoff notes
4. **Blockers** (5 min)
   - Any blockers requiring escalation

**Output:** Brief notes in team channel. Escalations raised immediately.

## Escalation Triggers

The following conditions require immediate escalation outside the regular cadence:

| Trigger | Escalate To | Timeline |
|---------|-------------|----------|
| S1 incident ([severity definitions](escalation-paths.md#severity-classification)) | AI Risk Committee chair + CTO | Within 1 hour |
| Regulatory examination notification | Head of Compliance + AI Risk Committee | Same day |
| Fairness metric breach beyond threshold | MRM + Compliance | Within 24 hours |
| Data breach affecting model training data (S1) | DPO + Security; AI Risk Committee chair | DPO and Security immediately; chair within 1 hour |
| Model performance below absolute minimum | MRM + Business Owner | Within 4 hours |

## Annual Activities

| Activity | Owner | Timeline |
|----------|-------|----------|
| Framework review and update | Head of MRM | Q1 |
| Risk appetite recalibration | AI Risk Committee | Q1 |
| Internal audit of AI governance | Internal Audit | Q2 |
| Regulatory compliance mapping update | Compliance | When regulations change |
| Mock regulatory examination (T1 systems) | MRM + Compliance | Q3 |
| Training and awareness program | Data Science Lead + Compliance | Ongoing |
