# Governance Workflow

This document defines the end-to-end governance process for AI systems — from idea to retirement. Every AI system, regardless of tier, follows these stages. The depth of governance at each stage scales with the system's risk tier. For the master list of controls and their evidence requirements, see [control-register.md](control-register.md).

## Stage 1: Idea Intake

**What happens:** A use case proposal is submitted with business justification, intended users, and data requirements. An initial risk screening identifies early signals — customer-facing? Regulated decisions? PII? Agentic capabilities?

**Gate criteria:** Sponsor identified, business justification documented, initial risk screening completed.

**Evidence produced:**
- Intake form with business justification (no Control ID — pre-register artifact)
- Initial risk screening questionnaire (no Control ID — pre-register artifact)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Intake form submission | Required | Required | Required | Required |
| Initial risk screening | Required | Required | Required | Required |
| Early AI Risk team notification | Required | Required | Recommended | N/A |
| Executive sponsor briefing | Required | Recommended | N/A | N/A |

**Decision point:** Product owner submits; AI Platform team triages. T1/T2 flags trigger immediate AI Risk involvement.

**Framework references:**
- [Risk matrix](../risk-classification/risk-matrix.md)
- [GenAI risk matrix](../risk-classification/genai-risk-matrix.md)

## Stage 2: Risk Assessment & Tiering

**What happens:** Full risk assessment using framework matrices. Tier determined through structured dimension scoring. Auto-override rules applied — certain characteristics force a minimum tier regardless of aggregate score.

**Gate criteria:** All dimensions scored, tier determination documented, auto-overrides checked, assessment reviewed and accepted by the appropriate authority.

**Evidence produced:**
- Signed risk assessment with dimension scoring and tier determination (Control ID: RA-001)
- Override decision document for auto-T1 triggers (Control ID: RA-002)
- Completed impact assessment (Control ID: RA-003)
- Risk assessment review record with sign-off (Control ID: RA-004)
- Filed DPIA if PII is processed (Control ID: RA-005)

### Tier Determination Decision Flowchart

```
START: New AI system proposed
  │
  ├─ Does it make or directly influence regulated decisions?
  │   YES → T1 (Critical)
  │
  ├─ Does it process customer PII through an external LLM API?
  │   YES → T1 (Critical)
  │
  ├─ Does it generate customer-facing content without human review?
  │   YES → T1 (Critical)
  │
  ├─ Is it agentic with production system access?
  │   YES → T1 (Critical)
  │
  ├─ Score GenAI risk dimensions (hallucination, data exposure,
  │  prompt injection, output control, vendor dependency)
  │   Any dimension = Critical, or aggregate ≥ 16 → T1
  │   Aggregate 12–15, no Critical → T2
  │   Aggregate 8–11 → T3
  │   Aggregate ≤ 7 → T4
  │
  └─ Apply multimodal/agentic overrides if applicable
      Synthetic media generation → minimum T2
      Biometric processing → T1
      Multi-agent system → minimum T2
```

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Full risk assessment | Required | Required | Required | Required |
| Impact assessment | Required | Required | Recommended | N/A |
| DPIA (if PII) | Required | Required | Required | N/A |
| AI Risk Committee review | Required | N/A | N/A | N/A |
| Head of AI review | N/A | Required | N/A | N/A |
| Team lead review | N/A | N/A | Required | N/A |
| Self-assessment | N/A | N/A | N/A | Required |

**Decision point:** Reviewed by: AI Risk Committee (T1), Head of AI (T2), team lead (T3), self-assessment (T4). Any stakeholder can challenge and escalate.

**Framework references:**
- [Risk matrix](../risk-classification/risk-matrix.md)
- [GenAI risk matrix](../risk-classification/genai-risk-matrix.md)
- [Multimodal risk matrix](../risk-classification/multimodal-risk-matrix.md)
- [Agentic AI risk](../risk-classification/agentic-ai-risk.md)
- [Assessment template](../../templates/genai-use-case-assessment.md)

## Stage 3: Architecture & Design Review

**What happens:** System architecture documented with component diagrams, data flows, and integration points. Vendor/model selection justified. Data residency confirmed against jurisdictional rules.

**Gate criteria:** Architecture approved, data residency confirmed, vendor/model assessment completed.

**Evidence produced:**
- Architecture document with data flows (Control ID: AR-001)
- Architecture review board sign-off (Control ID: AR-002)
- Data residency confirmation per jurisdiction (Control ID: AR-003)
- Model selection document with evaluation rationale (Control ID: AR-004)
- Third-party model risk assessment (Control ID: AR-005)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Architecture documentation | Required | Required | Required | Required |
| Architecture review board | Required | Required | N/A | N/A |
| Team-level architecture review | N/A | N/A | Required | Required |
| Data residency confirmation | Required | Required | Required | Recommended |
| Vendor risk assessment | Required | Required | Required | Recommended |

**Decision point:** Architecture review board approves (T1/T2); team lead approves (T3/T4). Data residency concerns block regardless of tier.

**Framework references:**
- [Deployment gates](../llm-lifecycle/deployment-gates.md)
- [Data residency for LLMs](../compliance/data-residency-llm.md)
- [Third-party model risk](../compliance/third-party-model-risk.md)

## Stage 4: Development & Prompt Engineering

**What happens:** Model cards created documenting capabilities, limitations, and intended use. Prompts developed, version-controlled, and peer-reviewed. Guardrails implemented per tier requirements.

**Gate criteria:** Model card exists (all tiers), peer review completed (T1/T2), guardrails tested, data governance applied to training data.

**Evidence produced:**
- Model card in version control (Control ID: DE-001)
- Prompts version-controlled with commit history (Control ID: DE-002)
- Signed prompt review checklist (Control ID: DE-003)
- Guardrail configuration and test results (Control ID: DE-004)
- Data governance checklist for training data (Control ID: DE-005)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Model card creation | Required | Required | Required | Required |
| Prompt version control | Required | Required | Required | Recommended |
| Prompt peer review | Required | Required | Recommended | N/A |
| Guardrail implementation | Required | Required | Recommended | N/A |
| Fine-tuning data governance | Required | Required | Required | Recommended |

**Decision point:** Prompt review sign-off from second engineer (T1/T2). Cannot proceed to evaluation without a model card.

**Framework references:**
- [Prompt engineering standards](../llm-lifecycle/prompt-engineering-standards.md)
- [Fine-tuning governance](../llm-lifecycle/fine-tuning-governance.md)
- [Model card template](../../templates/model-card-template.yaml)

## Stage 5: Evaluation & Testing

**What happens:** Eval suites executed per evaluation governance standard — safety benchmarks, domain accuracy, RAG retrieval quality, bias evaluation, and regression testing. Eval dataset integrity verified to prevent contamination.

**Gate criteria:** All required evals pass tier thresholds, safety eval passed, regression shows no degradation (T1/T2), dataset integrity verified.

**Evidence produced:**
- Pre-release evaluation report with pass/fail per metric (Control ID: EV-001)
- Safety evaluation results meeting tier thresholds (Control ID: EV-002)
- Regression report comparing current vs. previous version (Control ID: EV-003)
- RAG retrieval precision/recall/relevance metrics (Control ID: EV-004)
- Bias evaluation with counterfactual test results (Control ID: EV-005)
- Eval dataset integrity confirmation (Control ID: EV-006)
- LLM-as-judge calibration report (Control ID: EV-007)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Pre-release evaluation | Required | Required | Required | Required |
| Safety evaluation | Required | Required | Required | Recommended |
| Regression evaluation | Required | Required | Recommended | N/A |
| RAG retrieval evaluation | Required | Required | Required | Recommended |
| Bias evaluation | Required | Required | Recommended | N/A |
| LLM-as-judge calibration | Required | Required | N/A | N/A |

**Decision point:** AI lead certifies all evals pass. Failures block deployment. Threshold exceptions: AI Risk Committee (T1), Head of AI (T2).

**Framework references:**
- [Evaluation governance](../llm-lifecycle/evaluation-governance.md)

## Stage 6: Security Review & Red-Teaming

**What happens:** Adversarial testing per red-teaming protocol. Depth scales with tier — T1/T2 get comprehensive red-teaming; T3/T4 use automated scanning. Supply chain verified for open-source models.

**Gate criteria:** No Critical findings (all tiers), no unaddressed High (T1/T2), adversarial defenses validated (T1/T2).

**Evidence produced:**
- Red-team report with findings and severity ratings (Control ID: SR-001)
- Confirmation of zero Critical/High findings or remediation evidence (Control ID: SR-002)
- Adversarial robustness defense documentation (Control ID: SR-003)
- AI-BOM and supply chain provenance verification (Control ID: SR-004)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Comprehensive red-teaming | Required | Required | N/A | N/A |
| Automated adversarial scanning | Required | Required | Required | Recommended |
| Supply chain verification | Required | Required | Required | Recommended |
| Adversarial defense implementation | Required | Required | Recommended | N/A |

**Decision point:** Security lead signs off. T1/T2 blocked by any unaddressed High/Critical. T3/T4 Critical blocks; High requires risk acceptance.

**Framework references:**
- [Red-teaming protocol](../ai-security/red-teaming-protocol.md)
- [Adversarial robustness](../ai-security/adversarial-robustness.md)
- [Supply chain security](../ai-security/supply-chain-security.md)

## Stage 7: Deployment Approval

**What happens:** Evidence pack assembled, verified for completeness, and routed through the sign-off chain. This is the final gate before production — captures who approved, what was reviewed, and any conditions.

**Gate criteria:** All evidence present per tier requirements, all sign-offs obtained, deployment gates passed, rollback plan tested (T1/T2).

**Evidence produced:**
- Evidence checklist with all required items present (Control ID: DA-001)
- Signed deployment approval record (Control ID: DA-002)
- Deployment gate evidence package (Control ID: DA-003)
- Rollback procedure with test evidence (Control ID: DA-004)

### Minimum Evidence Pack by Tier

**T1 (Critical) — all 12 items required:**

1. Signed risk assessment with tier determination (RA-001)
2. Architecture review record (AR-002)
3. DPIA, if PII processed (RA-005)
4. Model card (DE-001)
5. Prompt review record (DE-003)
6. Evaluation report — pre-release, safety, regression, RAG, bias (EV-001, EV-002, EV-003, EV-004, EV-005)
7. Red-team report (SR-001, SR-002)
8. Security assessment (SR-003)
9. Monitoring configuration (PM-001, PM-002)
10. Incident response playbook (IR-001)
11. Rollback plan (DA-004)
12. Deployment approval with sign-offs (DA-002)

**T2 (High):** Items 1–12 (architecture review may be team-level rather than review board).

**T3 (Moderate):** Items 1, 4, 6 (pre-release + safety evaluation only), 9, 12.

**T4 (Low):** Items 1, 4, 6 (pre-release evaluation only), 12.

### Data Classification Note

Governance artifacts (risk assessments, case files, red-team reports, incident post-mortems) contain sensitive information. Classify the evidence pack per organizational data classification policy. Red-team reports should be classified as **Confidential**. Board reports as **Board Confidential**.

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Full evidence pack (12 items) | Required | Required | N/A | N/A |
| Reduced evidence pack | N/A | N/A | Required | Required |
| AI Risk Committee sign-off | Required | N/A | N/A | N/A |
| Head of AI sign-off | N/A | Required | N/A | N/A |
| Team lead sign-off | N/A | N/A | Required | N/A |
| Self-certification | N/A | N/A | N/A | Required |

**Decision point:** Sign-off chain: AI Risk Committee (T1), Head of AI (T2), team lead (T3), self-certification (T4). Missing evidence blocks — no exceptions.

**Framework references:**
- [Deployment gates](../llm-lifecycle/deployment-gates.md)

## Stage 8: Production Operations

**What happens:** Monitoring configured and validated before traffic. Alerting thresholds set per tier. Human oversight activated for T1/T2. Cost dashboards track inference spend.

**Gate criteria:** Monitoring operational, alerting configured, human oversight staffed (T1/T2), eval schedule running, cost monitoring active.

**Evidence produced:**
- Monitoring configuration with dashboard reference (Control ID: PM-001)
- Alert configuration with thresholds and escalation paths (Control ID: PM-002)
- Human oversight process document with staffing confirmation (Control ID: PM-003)
- Production evaluation schedule and latest results (Control ID: PM-004)
- Cost dashboard with alert configuration (Control ID: PM-005)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Real-time monitoring | Required | Required | Required | Recommended |
| Alerting with escalation | Required | Required | Required | Recommended |
| Human oversight process | Required | Required | N/A | N/A |
| Production evaluation cadence | Daily | Weekly | Monthly | Quarterly |
| Cost monitoring | Required | Required | Required | Recommended |

**Decision point:** AI Operations confirms monitoring is live before traffic. Hard gate — no manual overrides.

**Framework references:**
- [LLM monitoring](../llm-lifecycle/monitoring.md)
- [Model lifecycle monitoring](../model-lifecycle/monitoring.md)

## Stage 9: Ongoing Governance

**What happens:** Scheduled reviews per tier cadence assess performance, risk assessment relevance, and provider updates. Material changes (model swap, prompt revision, regulatory change) trigger revalidation outside cadence.

**Gate criteria:** Review completed within cadence, model card updated, revalidation done for material changes, regulatory impact assessed.

**Evidence produced:**
- Review record with findings and actions (Control ID: RV-001)
- Updated model card (Control ID: RV-002)
- Revalidation assessment with evaluation results (Control ID: RV-003)
- Regulatory change impact assessment (Control ID: RV-004)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Scheduled review | Monthly | Quarterly | Semi-annually | Annually |
| Model card update | At each review | At each review | At each review | At each review |
| Revalidation on change | Required | Required | Required | Required |
| Regulatory change assessment | Required | Required | Required | Recommended |

**Decision point:** System owner certifies review complete. Overdue >30 days escalates to AI Risk. Revalidation failure sends system back through Stage 5.

**Framework references:**
- [Review cadence](../operating-model/review-cadence.md)
- [Regulatory change monitoring](../compliance/regulatory-change-monitoring.md)

## Stage 10: Deprecation & Retirement

**What happens:** Deprecation trigger identified (vendor EOL, replacement approved, use case retired, regulatory prohibition). Impact assessment maps downstream dependencies. Migration governance ensures replacements go through full lifecycle.

**Gate criteria:** Impact assessment completed before action, migration governance followed, consumers migrated, evidence archived.

**Evidence produced:**
- Impact assessment with affected systems and migration plan (Control ID: DR-001)
- Migration assessment with parallel running evidence and cutover approval (Control ID: DR-002)
- Archival confirmation with artifact inventory (Control ID: DR-003)
- Decommission record — monitoring removed, access revoked, documentation archived (Control ID: DR-004)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Deprecation impact assessment | Required | Required | Required | Required |
| Migration governance | Required | Required | Recommended | N/A |
| Parallel running period | Required | Required | Recommended | N/A |
| Evidence archival | Required | Required | Required | Required |
| Formal decommission record | Required | Required | Required | Recommended |

**Decision point:** AI Risk Committee approves (T1), Head of AI approves (T2). No decommission until evidence archival confirmed.

**Framework references:**
- [Model deprecation governance](../llm-lifecycle/model-deprecation-governance.md)

## Retroactive Governance

For organizations with AI systems already in production without this evidence trail:

1. **Inventory** — List all production AI systems. Assign a tier to each using the risk assessment process in Stage 2. Do not skip the auto-override checks.
2. **Gap assessment** — For each system, walk the control register and mark every control as: evidence exists, evidence missing, or not applicable. This produces a gap matrix per system.
3. **Prioritize by tier** — T1 systems are remediated first, then T2, T3, and T4. Within a tier, prioritize by customer impact and regulatory exposure.
4. **Remediation plan** — For each missing evidence item, define: who will produce it, by when, and what interim mitigation is in place until the evidence is produced.
5. **Timeline** — T1 gap remediation within 3 months. T2 within 6 months. T3/T4 within 12 months. These timelines are non-negotiable for regulated environments.
6. **Governance operations** — Once remediated, systems enter the normal ongoing governance cycle (Stage 9). From that point forward, they follow the same cadence as newly deployed systems.
