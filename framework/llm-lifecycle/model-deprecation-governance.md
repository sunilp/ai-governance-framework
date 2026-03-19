# Model Deprecation Governance

## Overview

AI models have finite lifespans. Commercial providers routinely retire model versions — OpenAI, Anthropic, and Google each sunset models on timelines of months to a year. Open-source models lose community support. Internal models are replaced by newer versions. Each deprecation event is a governance event: it can trigger re-assessment, require migration, and affect compliance posture.

Unmanaged model deprecation leads to rushed migrations, untested replacements, and compliance gaps. Structured deprecation governance prevents this.

---

## Deprecation Triggers

| Trigger | Source | Typical Timeline | Governance Action |
|---------|--------|-----------------|-------------------|
| Vendor deprecation announcement | Provider changelog / email | 3–12 months notice | Impact assessment within 5 business days |
| Vendor end-of-life (model removed) | Provider API | Immediate / previously announced | Emergency migration if not already planned |
| Community model abandoned | No commits, unresolved CVEs, maintainer departure | Gradual; often no announcement | Quarterly community health check detects this |
| Internal replacement decision | AI team | Self-determined | Standard lifecycle process |
| Regulatory non-compliance | Compliance / Legal | Event-driven | Urgent assessment; may require immediate action |
| Performance degradation below thresholds | Monitoring alerts | Detected in production | Investigation → retraining or migration decision |
| Security vulnerability (unpatched) | CVE / security advisory | Event-driven | Security patch SLA; migration if no patch available |

---

## Impact Assessment Protocol

When a deprecation trigger is identified, complete the following assessment.

### Step 1: System Identification

| Question | Document |
|----------|----------|
| Which AI systems use this model? | List by system ID, name, tier, business owner |
| What tier are affected systems? | T1 systems get priority treatment |
| Are there downstream dependencies? | Other systems consuming outputs of affected systems |
| What is the deprecation timeline? | Vendor end-of-support date; end-of-life date |

### Step 2: Impact Classification

| Impact Level | Criteria | Response Timeline |
|-------------|----------|-------------------|
| Critical | T1 system affected; no validated fallback; deprecation < 3 months | Immediate action; AI Risk Committee notification |
| High | T2 system affected; or T1 with validated fallback; deprecation < 6 months | Action plan within 2 weeks |
| Medium | T3/T4 systems; or deprecation > 6 months | Action plan within 1 month |
| Low | Non-production systems; or deprecation > 12 months | Plan at next scheduled review |

### Step 3: Compliance Assessment

| Question | Document |
|----------|----------|
| Does the replacement model require re-assessment? | New risk assessment if model capabilities, provider, or architecture change |
| Does migration affect regulatory compliance? | EU AI Act conformity, audit trail continuity, data residency |
| Do existing model cards need updating? | Always — document model change and rationale |
| Are there audit trail implications? | Ensure traceability across model versions |

---

## Migration Governance

### Replacement Model Evaluation

The replacement model goes through the same evaluation rigor as initial model selection:

| Activity | Requirement | Reference |
|----------|-------------|-----------|
| Model evaluation | Run domain-specific eval suite against replacement model | [Model Selection](model-selection.md) |
| Safety evaluation | Full safety benchmark suite | [Red-Teaming Protocol](../ai-security/red-teaming-protocol.md) |
| Prompt compatibility testing | Test existing prompts on new model; document behavior differences | [Prompt Engineering Standards](prompt-engineering-standards.md) |
| Performance comparison | Side-by-side comparison: accuracy, latency, cost, safety scores | Document in migration assessment |
| Vendor/license assessment | If changing provider: full [third-party model risk assessment](../compliance/third-party-model-risk.md) | If changing provider |

### Parallel Running Period

For T1 and T2 systems:

| Phase | Duration | Activity |
|-------|----------|----------|
| Shadow mode | 1–2 weeks | New model runs alongside old; outputs compared but not served |
| Canary deployment | 1–2 weeks | New model serves subset of traffic (5–10%); monitor quality metrics |
| Gradual rollout | 1–2 weeks | Increase to 50%, then 100% if metrics hold |
| Full cutover | — | Old model decommissioned; new model at 100% |

For T3/T4 systems: shadow mode (1 week) → full cutover is acceptable.

### Cutover Gates

Migration cutover follows the same [deployment gates](deployment-gates.md) as any new deployment:
- Evaluation suite results meet or exceed deprecated model performance
- Safety evaluation results meet thresholds
- Prompt compatibility confirmed (no behavioral regressions)
- Monitoring and alerting configured for new model
- Rollback plan documented and tested

### Rollback Plan

| Element | Requirement |
|---------|-------------|
| Rollback capability | Ability to revert to a validated fallback path for at least 30 days post-cutover. If the deprecated model is unavailable (vendor EOL), the fallback must be the pre-validated alternative model, not the deprecated version. |
| Rollback trigger | Define metrics that trigger automatic or manual rollback |
| Rollback testing | Test rollback procedure before cutover |
| Vendor API rollback | Confirm deprecated model version remains available during transition period; if not, validate the alternative fallback model before cutover begins |

---

## Communication and Stakeholder Management

| Activity | Timeline | Audience |
|----------|----------|----------|
| Deprecation notification to system owners | Within 5 business days of trigger | All system owners of affected systems |
| Migration timeline published | Within 10 business days of trigger | System owners, AI operations, AI Risk |
| Status reporting | At each review cadence meeting | AI Risk Committee |
| Business owner briefing (T1) | Within 10 business days | Business owners of T1 affected systems |
| Completion notification | Upon successful migration | All stakeholders |

---

## Archival Requirements

When a model is deprecated, preserve the following for audit and compliance:

| Artifact | Retention | Purpose |
|----------|-----------|---------|
| Model card (deprecated version) | Per tier retention policy (7/5/3/1 years) | Audit trail; regulatory evidence |
| Risk assessment (deprecated version) | Per tier retention policy | Compliance evidence |
| Evaluation results (deprecated model) | Per tier retention policy | Performance baseline; comparison evidence |
| Sample outputs (deprecated model) | 1 year minimum | Behavioral comparison; incident investigation |
| Migration decision rationale | Per tier retention policy | Audit trail for model change |
| Prompt versions used with deprecated model | Per tier retention policy | Reconstruction capability |

---

## Vendor Deprecation Monitoring

Proactively monitor vendor deprecation signals to avoid surprises.

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Check vendor changelogs and deprecation notices | Weekly | AI Operations |
| Review vendor model lifecycle roadmaps | Quarterly | AI Operations |
| Maintain model version inventory | Continuous (automated where possible) | AI Operations |
| Test with vendor beta/preview models | Before committing to upgrades | AI Operations |
| Track vendor deprecation patterns | Annually | AI Risk |

### Vendor Deprecation Risk

Include model lifecycle risk in vendor assessment:
- What is the vendor's historical deprecation notice period?
- Does the vendor offer extended support for enterprise customers?
- Is there a contractual commitment to minimum model availability period?
- What is the vendor's backward compatibility track record?
