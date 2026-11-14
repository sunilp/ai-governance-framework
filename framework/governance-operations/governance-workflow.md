# Governance Workflow

This document defines the end-to-end governance process for AI systems, from idea to retirement. Every AI system, regardless of tier, follows these stages. The depth of governance at each stage scales with the system's risk tier. For the master list of controls and their evidence requirements, see [control-register.md](control-register.md).

## Stage 1: Idea Intake

**What happens:** A use case proposal is submitted with business justification, intended users, and data requirements. An initial risk screening identifies early signals: customer-facing? Regulated decisions? PII? Agentic capabilities?

**Gate criteria:** Sponsor identified, business justification documented, initial risk screening completed.

**Evidence produced:**
- Intake form with business justification (no Control ID; pre-register artifact)
- Initial risk screening questionnaire (no Control ID; pre-register artifact)
- AI inventory entry opened with status `proposed` (evidenced under RA-006 at Stage 2)

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

**What happens:** The Product owner prepares a full risk assessment using the framework matrices. Each risk dimension is scored Critical (4), High (3), Medium (2) or Low (1), and the highest-scoring dimension sets the tier. Override rules are then applied. Overrides can raise the tier, never lower it. The approver may raise a tier with a recorded rationale (for example, a pilot with an unusual exposure profile). Nobody can lower a tier below what the scoring and overrides give. The aggregate score is recorded for context and comparison only; it does not set the tier.

**Prohibited-use screen first:** before scoring, run the [Step 0 prohibited-use screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen) against EU AI Act Art. 5 and the internal prohibited-use policy. A prohibited use is rejected, not tiered (RA-007).

**Gate criteria:** All dimensions scored, tier determination documented, override list checked, assessment approved by the appropriate authority.

**Evidence produced:**
- Signed risk assessment with dimension scoring and tier determination (Control ID: RA-001)
- Override decision document for any override trigger, automatic T1 or minimum T2 (Control ID: RA-002)
- Completed impact assessment (Control ID: RA-003)
- Risk assessment approval record with sign-off (Control ID: RA-004)
- DPIA screening for any system processing personal data; full DPIA for T1/T2 and wherever screening indicates high risk (Control ID: RA-005)
- AI inventory entry created before development (Control ID: RA-006)
- Step 0 prohibited-use screen result (Control ID: RA-007)
- EU AI Act role determination, including the Art. 25 provider check (Control ID: RA-008)
- Fundamental rights impact assessment, where Art. 27 applies (Control ID: RA-009)

### Tier Determination Decision Flowchart

The rule and the override list below are canonical in the [GenAI risk matrix](../risk-classification/genai-risk-matrix.md#risk-tier-determination-for-genai). The same rule applies to the ML, multimodal and agentic matrices.

```
START: New AI system proposed
  │
  ├─ Score each risk dimension: Critical (4), High (3), Medium (2), Low (1)
  │   The highest-scoring dimension sets the tier:
  │   any Critical → T1; else any High → T2;
  │   else any Medium → T3; all Low → T4
  │   (Record the aggregate score for context only. It does not set the tier.)
  │
  ├─ Automatic T1 overrides (any YES → T1 Critical)
  │   1. Makes or directly influences regulated decisions (credit,
  │      insurance underwriting or pricing, AML/sanctions, employment)?
  │   2. Generates customer-facing content delivered without
  │      per-output human review?
  │   3. Processes customer personal data through an external LLM API
  │      without ALL four safeguards: vendor zero data retention, a
  │      regional endpoint that meets data residency requirements, a
  │      signed DPA, and PII redaction or minimisation before the call?
  │   4. Agentic with write access to production systems or data stores,
  │      or with authority to move money, communicate with customers,
  │      or change identity and access?
  │   5. Biometric identification or categorisation, synthetic media
  │      that can depict real people (deepfake-capable), voice cloning,
  │      or medical imagery?
  │
  ├─ Minimum T2 overrides (any YES → at least T2)
  │   6. Any agentic system, including read-only tool use, and any
  │      multi-agent system?
  │   7. Synthetic media generation not covered by item 5?
  │   8. Customer personal data through an external LLM API with all
  │      four safeguards in place?
  │   9. Personal data in visual content?
  │
  └─ Final tier = the higher of the scored tier and any override
```

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Full risk assessment (prepared by Product owner) | Required | Required | Required | Required |
| Override list check | Required | Required | Required | Required |
| Impact assessment | Required | Required | Recommended | N/A |
| DPIA screening (if personal data) | Required | Required | Required | Required |
| Full DPIA (if personal data) | Required | Required | If screening indicates high risk | If screening indicates high risk |
| Risk assessment approval | AI Risk Committee | AI Risk (second line) | Team lead | Team lead (acknowledges self-assessment) |

**Decision point:** Prepared by the Product owner. Approved by the AI Risk Committee (T1), AI Risk as second line (T2), or the team lead (T3; for T4 the team lead acknowledges the self-assessment). Any stakeholder can challenge and escalate.

**Framework references:**
- [Risk matrix](../risk-classification/risk-matrix.md)
- [GenAI risk matrix](../risk-classification/genai-risk-matrix.md)
- [Multimodal risk matrix](../risk-classification/multimodal-risk-matrix.md)
- [Agentic AI risk](../risk-classification/agentic-ai-risk.md)
- [Assessment template](../../templates/genai-use-case-assessment.md)

## Stage 3: Architecture & Design Review

**What happens:** System architecture documented with component diagrams, data flows, and integration points. Vendor/model selection justified. Data residency confirmed against jurisdictional rules.

**Gate criteria:** Architecture approved (T1/T2) or documented (T3/T4), data residency confirmed, model selection approved, vendor assessment completed where required.

**Evidence produced:**
- Architecture document with data flows (Control ID: AR-001)
- Architecture review record: review board sign-off (T1) or recorded team-level design review (T2) (Control ID: AR-002)
- Data residency confirmation per jurisdiction (Control ID: AR-003)
- Model selection document with evaluation rationale and approval (Control ID: AR-004)
- Third-party model risk assessment (Control ID: AR-005)
- Agent identity, tool allowlist and permission review for tool-using agents (Control ID: AR-006)
- Vendor contract checked against the [AI procurement clauses](../compliance/ai-procurement-clauses.md) and recorded in the register of information (Control ID: AR-007)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Architecture documentation (technical owner) | Required | Required | Required | Required |
| Architecture review board sign-off | Required | N/A | N/A | N/A |
| Recorded team-level design review, approved by Head of AI or delegate | N/A | Required | N/A | N/A |
| Data residency confirmation (external data flows) | Required | Required | Required | Required |
| Model selection approval (external models) | AI Risk Committee + CISO | Head of AI | Team lead (approved vendor list) | Team lead (approved vendor list) |
| Vendor risk assessment | Required | Required | Required | Approved vendors only, no separate assessment |

**Decision point:** T1: architecture review board signs off. T2: a recorded team-level design review is approved by the Head of AI or delegate. T3/T4: the technical owner documents the architecture; no separate review. Data residency concerns block regardless of tier.

**Framework references:**
- [Deployment gates](../llm-lifecycle/deployment-gates.md)
- [Cross-border data and LLM data residency](../compliance/cross-border-data-governance.md)
- [Third-party model risk](../compliance/third-party-model-risk.md)

## Stage 4: Development & Prompt Engineering

**What happens:** Model cards created documenting capabilities, limitations, and intended use. Prompts developed, version-controlled, and peer-reviewed. Guardrails implemented per tier requirements.

**Gate criteria:** Model card exists (all tiers), prompts version-controlled (all GenAI tiers), prompt review completed per tier (T1-T3), guardrails tested (T1/T2), data governance applied to training data.

**Evidence produced:**
- Model card in version control (Control ID: DE-001)
- Prompts version-controlled with commit history (Control ID: DE-002)
- Signed prompt review checklist (Control ID: DE-003)
- Guardrail configuration and test results (Control ID: DE-004)
- Data governance checklist for training data (Control ID: DE-005)
- AI interaction disclosure (Control ID: DE-006)
- Marking and labelling of AI-generated content (Control ID: DE-007)
- Retrieval permission tests for RAG systems (Control ID: DE-008)
- Notices to people subject to AI-assisted decisions (Control ID: DE-009)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Model card creation | Required | Required | Required | Required |
| Prompt version control (GenAI) | Required | Required | Required | Required |
| Prompt review | Peer review + prompt engineering lead + security review + AI Risk sign-off | Peer review + prompt engineering lead | Peer review | Self-review |
| Guardrail implementation | Required | Required | Recommended | N/A |
| Fine-tuning data governance | Required | Required | Required | Recommended |

**Decision point:** The AI lead owns prompt review (DE-003). Sign-off per tier is in the table above and in the [prompt engineering standards](../llm-lifecycle/prompt-engineering-standards.md). Cannot proceed to evaluation without a model card.

**Framework references:**
- [Prompt engineering standards](../llm-lifecycle/prompt-engineering-standards.md)
- [Fine-tuning governance](../llm-lifecycle/fine-tuning-governance.md)
- [LLM model card template](../../templates/llm-model-card.yaml) (GenAI systems)
- [Model card template](../../templates/model-card-template.yaml) (traditional ML systems)

## Stage 5: Evaluation & Testing

**What happens:** Eval suites executed per evaluation governance standard: safety benchmarks, domain accuracy, RAG retrieval quality, bias evaluation, and regression testing. Eval dataset integrity verified to prevent contamination.

**Gate criteria:** All required evals pass tier thresholds under the [statistical pass rule](../llm-lifecycle/evaluation-governance.md#statistical-pass-rule) (T1/T2 judged on the 95% confidence bound), safety eval passed, regression shows no degradation (T1/T2), dataset integrity verified.

**Evidence produced:**
- Pre-release evaluation report with pass/fail per metric (Control ID: EV-001)
- Safety evaluation results meeting tier thresholds (Control ID: EV-002)
- Regression report comparing current vs. previous version (Control ID: EV-003)
- RAG retrieval precision/recall/relevance metrics (Control ID: EV-004)
- Bias evaluation with counterfactual test results (Control ID: EV-005)
- Eval dataset integrity confirmation (Control ID: EV-006)
- LLM-as-judge calibration report (Control ID: EV-007)
- Agent evaluation report for agentic systems: task success, tool-call accuracy, unsafe actions, trajectory review (Control ID: EV-008)
- Guardrail evaluation with false negative and false positive rates (Control ID: EV-009)
- Validation report: independent validation per tier (no separate control ID; see [validation](../model-lifecycle/validation.md))

Suite sizes, thresholds and release criteria are set in [evaluation governance](../llm-lifecycle/evaluation-governance.md#release-criteria-by-tier). Release criteria: T1 all eval types pass, including agent evaluation (agentic systems) and guardrail evaluation; T2 pre-release, safety, regression, bias, RAG retrieval (if RAG), agent evaluation (if agentic), guardrail evaluation and red-team; T3 pre-release, safety, RAG retrieval (if RAG), guardrail evaluation (if guardrails are used) and red-team (automated scan + 50 manual cases); T4 pre-release and safety (automated, 20+ cases each), with RAG retrieval evaluation and a red-team scan recommended.

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Pre-release evaluation | Required | Required | Required | Required |
| Safety evaluation (GenAI) | Required | Required | Required | Required (automated, 20+ cases) |
| Regression evaluation (on model or prompt change) | Required | Required | Recommended | N/A |
| RAG retrieval evaluation (RAG systems) | Required | Required | Required | Recommended |
| Bias evaluation | Required | Required | Recommended | N/A |
| Eval dataset integrity check | Required | Required | Required | Required |
| LLM-as-judge calibration (where automated eval is used) | Required | Required | N/A | N/A |
| Independent validation | Full, by Model Risk Management (MRM) | Reduced scope, by a qualified reviewer outside the development team (MRM or second line) | Peer review | Self-test |

The team that builds a T1 or T2 model never validates it.

**Decision point:** AI lead certifies all evals pass; release sign-off per tier is in the [release criteria](../llm-lifecycle/evaluation-governance.md#release-criteria-by-tier). Failures block deployment. A system that misses a threshold can proceed only under an approved exception (see [Exceptions and Risk Acceptance](#exceptions-and-risk-acceptance)).

**Framework references:**
- [Evaluation governance](../llm-lifecycle/evaluation-governance.md)
- [Model validation](../model-lifecycle/validation.md)

## Stage 6: Security Review & Red-Teaming

**What happens:** Adversarial testing per the red-teaming protocol. Depth scales with tier, using the suite sizes in [evaluation governance](../llm-lifecycle/evaluation-governance.md#evaluation-types): T1 200+ cases including manual testing (external testers recommended); T2 100+ cases; T3 an automated adversarial scan plus 50 manual cases; T4 an automated scan of 20+ cases, recommended. Application security review and penetration testing for customer-facing or internet-exposed systems. Supply chain verified for open-source models.

**Gate criteria:** No unresolved Critical findings (all tiers; this cannot be excepted), no unaddressed High (T1/T2), adversarial defenses validated (T1/T2).

**Evidence produced:**
- Red-team report with findings and severity ratings (Control ID: SR-001)
- Confirmation of zero Critical/High findings or remediation evidence (Control ID: SR-002)
- Adversarial robustness defense documentation (Control ID: SR-003)
- AI-BOM and supply chain provenance verification (Control ID: SR-004)
- Application security review and penetration test report, where required (deployment gate criteria, recorded under DA-003)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Red-team testing (GenAI) | 200+ cases incl. manual (external testers recommended) | 100+ cases | Automated scan + 50 manual cases | Automated scan, 20+ cases (recommended) |
| Zero unresolved Critical findings | Required | Required | Required | Required (if red-teamed) |
| Zero unaddressed High findings | Required | Required | Risk acceptance | Risk acceptance |
| Adversarial defense implementation | Required | Required | Recommended | N/A |
| Penetration testing (customer-facing or internet-exposed) | Required | Required | Recommended | N/A |
| Supply chain verification (open-source models) | Required | Required | Required | Recommended |

**Decision point:** Security lead signs off. T1/T2 blocked by any unaddressed High/Critical. T3/T4: Critical blocks; High requires a recorded risk acceptance (see [Exceptions and Risk Acceptance](#exceptions-and-risk-acceptance)).

**Framework references:**
- [Red-teaming protocol](../ai-security/red-teaming-protocol.md)
- [Adversarial robustness](../ai-security/adversarial-robustness.md)
- [Supply chain security](../ai-security/supply-chain-security.md)

## Stage 7: Deployment Approval

**What happens:** Evidence pack assembled, verified for completeness, and routed through the sign-off chain. This is the final gate before production. It captures who approved, what was reviewed, and any conditions.

**Gate criteria:** All evidence present per tier requirements, all sign-offs obtained, deployment gates passed, rollback plan tested (T1/T2).

**Evidence produced:**
- Evidence checklist with all required items present (Control ID: DA-001)
- Signed deployment approval record (Control ID: DA-002)
- Deployment gate evidence package (Control ID: DA-003)
- Rollback procedure with test evidence (Control ID: DA-004)

### Minimum Evidence Pack by Tier

Each row lists what the pack must contain at each tier. "Not required" means the item is not part of the minimum pack for that tier.

| # | Evidence | Controls | T1 (Critical) | T2 (High) | T3 (Medium) | T4 (Low) |
|---|----------|----------|---------------|-----------|-------------|----------|
| 1 | Signed risk assessment with tier determination, override check and approval | RA-001, RA-002, RA-004 | Required | Required | Required | Required |
| 2 | Impact assessment | RA-003 | Required | Required | Not required | Not required |
| 3 | DPIA (if personal data processed) | RA-005 | Full DPIA | Full DPIA | Screening; full DPIA if high risk | Screening; full DPIA if high risk |
| 4 | Architecture document and data residency confirmation | AR-001, AR-003 | Required | Required | Required | Required |
| 5 | Architecture review record | AR-002 | Review board sign-off | Team-level design review | Not required | Not required |
| 6 | Model selection record and vendor risk assessment (external models) | AR-004, AR-005 | Required | Required | Required | Model selection only (approved vendor) |
| 7 | Model card and prompt version history | DE-001, DE-002 | Required | Required | Required | Required |
| 8 | Prompt review record (GenAI) | DE-003 | Required | Required | Peer review record | Not required |
| 9 | Guardrail configuration and test results (GenAI) | DE-004 | Required | Required | Not required | Not required |
| 10 | Evaluation report | EV-001 to EV-009 | All eval types | Pre-release, safety, regression, bias, RAG retrieval (if RAG), dataset integrity, judge calibration | Pre-release, safety, RAG retrieval (if RAG), dataset integrity | Pre-release, safety (automated, 20+ cases), dataset integrity |
| 11 | Validation report | (see Stage 5) | Full independent validation (MRM) | Reduced-scope independent validation | Peer review | Self-test |
| 12 | Red-team report (GenAI) | SR-001, SR-002 | 200+ cases | 100+ cases | Automated scan + 50 manual cases | Not required (scan recommended) |
| 13 | Security assessment: adversarial defense configuration; application security review and penetration test (customer-facing or internet-exposed); supply chain verification (open-source models) | SR-003, SR-004, DA-003 | Required | Required | Supply chain verification if open-source models | Not required |
| 14 | Monitoring, alerting, human oversight, production evaluation and cost monitoring configuration | PM-001 to PM-005 | Required | Required | PM-001, PM-002, PM-004, PM-005 | PM-001, PM-004 |
| 15 | Incident response playbook and on-call rotation | IR-001, IR-002 | Required | Required | Not required | Not required |
| 16 | Rollback plan with test evidence | DA-004 | Required | Required | Not required | Not required |
| 17 | Evidence checklist, deployment gate evidence and signed deployment approval | DA-001, DA-002, DA-003 | Required | Required | Required | Required |

The pack also includes evidence for every other control whose Applies To in the [control register](control-register.md) covers the system: the inventory entry and prohibited-use screen (RA-006, RA-007, all tiers), EU AI Act role and fundamental rights impact assessment where in scope (RA-008, RA-009), agent identity and tool review (AR-006, agentic systems), vendor contract check (AR-007, external models), disclosure, marking, retrieval permissions and decision notices (DE-006 to DE-009, where they apply), agent and guardrail evaluations (EV-008, EV-009), kill switch test (PM-006, T1 customer-facing and agentic) and audit logging (PM-007, all tiers).

### Data Classification Note

Governance artifacts (risk assessments, case files, red-team reports, incident post-mortems) contain sensitive information. Classify the evidence pack per organizational data classification policy. Red-team reports should be classified as **Confidential**. Board reports as **Board Confidential**.

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Evidence pack per the minimum evidence pack table | Required | Required | Required | Required |
| Deployment gate criteria ([deployment gates](../llm-lifecycle/deployment-gates.md)) | Required | Required | Required | Required |
| Rollback plan tested | Required | Required | N/A | N/A |
| Deployment approval | AI Risk Committee + CISO (+ DPO if personal data is processed) | Head of AI + Business Unit Head | Team lead + business owner | Team lead |

**Decision point:** Sign-off chain as in the table above. Missing evidence blocks deployment unless an exception is approved under [Exceptions and Risk Acceptance](#exceptions-and-risk-acceptance). Non-waivable items can never be excepted.

**Framework references:**
- [Deployment gates](../llm-lifecycle/deployment-gates.md)

## Stage 8: Production Operations

**What happens:** Monitoring configured and validated before traffic. Alerting thresholds set per tier. Human oversight activated for T1/T2. Cost dashboards track inference spend. Production evaluation runs as three named activities. Incidents are handled under the incident response controls below.

**Gate criteria:** Monitoring operational, alerting configured, human oversight staffed (T1/T2), production evaluation schedule running, cost monitoring active, incident playbook published and on-call assigned (T1/T2), audit logging active, kill switch tested for T1 customer-facing and all agentic systems.

**Evidence produced:**
- Monitoring configuration with dashboard reference (Control ID: PM-001)
- Alert configuration with thresholds and escalation paths (Control ID: PM-002)
- Human oversight process document with staffing confirmation (Control ID: PM-003)
- Production evaluation schedule and latest results (Control ID: PM-004)
- Cost dashboard with alert configuration (Control ID: PM-005)
- Kill switch test record (Control ID: PM-006)
- Audit logging configuration and retention check (Control ID: PM-007)
- Quarterly fallback model test record for T1 systems using external models (Control ID: PM-008)

**Production evaluation** ([evaluation governance](../llm-lifecycle/evaluation-governance.md#production-evaluation) owns the cadences restated below):
1. Online automated scoring of live traffic.
2. Metrics review.
3. Full offline suite re-run, and always on a model, provider or prompt change.

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Basic usage and error monitoring | Required | Required | Required | Required |
| Alerting with escalation | Required | Required | Required | Covered by platform-level budget alerts |
| Human oversight process ([pattern selection](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix)) | Required | Required | N/A | N/A |
| Online automated scoring of live traffic | Every response (async) | 20% sample | 5% sample | Weekly batch sample |
| Metrics review | Daily dashboard check (AI Operations) + monthly system-owner review | Weekly | Monthly | Quarterly |
| Full offline suite re-run | Monthly | Quarterly | Semi-annual | Semi-annual |
| Vendor behaviour canary (external models, see [third-party model risk](../compliance/third-party-model-risk.md#ongoing-monitoring)) | Daily | Weekly | Monthly | Monthly |
| Cost monitoring | Required | Required | Required | Covered by platform-level budget alerts |

**Decision point:** AI Operations confirms monitoring is live before traffic. Traffic is not enabled without monitoring unless an exception is approved under [Exceptions and Risk Acceptance](#exceptions-and-risk-acceptance). Audit logging and the kill switch are non-waivable.

### Incident Response (Stage 8 sub-group)

Severity (S1-S4), response SLAs and notifications are defined in [escalation paths](../operating-model/escalation-paths.md#severity-classification). Monitoring alerts use priorities P1-P4, which are not incident severities; the mapping is in [alert priority to incident severity](../operating-model/escalation-paths.md#alert-priority-to-incident-severity).

**Evidence produced:**
- Published incident response playbook accessible to on-call (Control ID: IR-001)
- On-call rotation schedule (Control ID: IR-002)
- Incident report per template, with root cause: S1/S2 within 48 hours, S3 within 10 business days (Control ID: IR-003)
- Post-mortem report: S1 within 1 week, S2 within 2 weeks (Control ID: IR-004)
- Remediation tracker with status; S4 items tracked in the backlog (Control ID: IR-005)
- Regulatory notification assessment for every S1/S2 and suspected serious incident (Control ID: IR-006)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Incident response playbook | Required | Required | N/A | N/A |
| On-call team assigned | Required | Required | N/A | N/A |
| Incident reporting per severity SLA | Required | Required | Required | Required |
| Post-mortem for S1/S2 incidents | Required | Required | Required | Required |
| Remediation tracking | Required | Required | Required | Required |

Response SLAs depend on severity, not tier. Any incident on a T1 system that reached customers is at least S2.

**Framework references:**
- [LLM monitoring](../llm-lifecycle/monitoring.md)
- [Model lifecycle monitoring](../model-lifecycle/monitoring.md)
- [Escalation paths](../operating-model/escalation-paths.md)

## Stage 9: Ongoing Governance

**What happens:** Scheduled reviews per tier cadence assess performance, risk assessment relevance, and provider updates. Material changes trigger a risk re-assessment and revalidation outside cadence.

**Material change.** A change is material when it can alter what the system does or the risk it carries:

- a model swap or a new model version, including a provider update to a hosted model;
- a major prompt version, meaning a change in behaviour under the [prompt versioning rules](../llm-lifecycle/prompt-engineering-standards.md#versioning-rules);
- a change of scope or use: a new purpose, user group or channel;
- a new class or source of data (a routine update to an approved source follows [RAG governance](../llm-lifecycle/rag-governance.md#updates));
- a change to its autonomy or tool authority;
- a change in the regulatory environment that applies to it.

A material change triggers the re-tiering check and revalidation (RV-003) before release. A minor prompt version is not material on its own: it takes peer review and the evaluation suite at the pull request gate. The change record states the classification and who approved it. When in doubt, treat the change as material. Every other document that says "material change" means this definition.

**Gate criteria:** Review completed within cadence, risk re-assessment (re-tiering check) done, model card updated, revalidation done for material changes, regulatory impact assessed.

**Evidence produced:**
- Review record with findings, actions and risk re-assessment (Control ID: RV-001)
- Updated model card (Control ID: RV-002)
- Revalidation assessment with evaluation results (Control ID: RV-003)
- Regulatory change impact assessment (Control ID: RV-004)
- Log of explanations and human reviews provided for adverse outcomes (Control ID: RV-005)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| Formal governance review | Quarterly | Semi-annual | Annual | Annual self-assessment |
| Metrics review (operational, see Stage 8) | Daily dashboard check + monthly system-owner review | Weekly | Monthly | Quarterly |
| Risk re-assessment (re-tiering check) | At every formal review and on material change | At every formal review and on material change | At every formal review and on material change | At every formal review and on material change |
| Model card update | At each review | At each review | At each review | At each review |
| Revalidation on material change | Required | Required | Required | Required |
| Independent revalidation | Annual and on material change | Every 24 months and on material change | On material change (peer re-review) | On material change (peer re-review) |
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
- Decommission record: monitoring removed, access revoked, documentation archived (Control ID: DR-004)

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

## Fast Lane (T3/T4)

T3 and T4 systems follow the same ten stages with less evidence and no committee. This section gathers the T3 and T4 columns of the tier tables above and the [minimum evidence pack](#minimum-evidence-pack-by-tier) in one place. It adds no requirement and removes none. If it ever differs from those tables, the tables govern.

**Entry.** The Stage 2 assessment gives T3 or T4 after scoring and the full override check. Any override item puts a system at T2 or above, so a system that matches one is never in the fast lane. The [Step 0 prohibited-use screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen) and the [when to say no](when-to-say-no.md) questions apply as at every tier.

**Required evidence.** Row numbers refer to the minimum evidence pack.

| Pack row | Evidence | Controls | T3 | T4 |
|---|---|---|---|---|
| 1 | Signed risk assessment with Step 0 result, tier determination, override check and approval | RA-001, RA-002, RA-004, RA-007 | Approved by the team lead | Self-assessment acknowledged by the team lead |
| 3 | DPIA (if personal data is processed) | RA-005 | Screening; full DPIA if screening indicates high risk | Screening; full DPIA if screening indicates high risk |
| 4 | Architecture document and data residency confirmation (external data flows) | AR-001, AR-003 | Documented by the technical owner | Documented by the technical owner |
| 6 | Model selection (external models) | AR-004 | Team lead, from the approved vendor list | Team lead, from the approved vendor list |
| 6 | Vendor risk assessment (external vendor APIs) | AR-005 | Simplified assessment: technical evaluation, security checklist and DPA ([assessment depth](../compliance/third-party-model-risk.md#assessment-depth-by-tier)) | No separate assessment; approved vendors only |
| 7 | Model card and prompt version history | DE-001, DE-002 | Required | Required |
| 8 | Prompt review (GenAI) | DE-003 | Peer review record | Self-review with documentation |
| 10 | Evaluation report | EV-001, EV-002, EV-004, EV-006 | Pre-release, safety, RAG retrieval (if RAG) and dataset integrity | Pre-release and safety (automated, 20+ cases each) and dataset integrity |
| 11 | Validation | Stage 5 | Peer review | Self-test |
| 12 | Red-team report (GenAI) | SR-001, SR-002 | Automated scan + 50 manual cases | Not required (automated scan recommended) |
| 13 | Supply chain verification (open-source models) | SR-004 | Required | Not required (recommended at Stage 6) |
| 14 | Monitoring and production evaluation configuration | PM-001, PM-002, PM-004, PM-005 | PM-001, PM-002, PM-004, PM-005 | PM-001, PM-004 |
| 17 | Evidence checklist, deployment gate evidence and signed deployment approval | DA-001, DA-002, DA-003 | Team lead + business owner | Team lead |

Suite sizes and thresholds are in [evaluation governance](../llm-lifecycle/evaluation-governance.md#evaluation-types). Not in the fast-lane pack at either tier: impact assessment (row 2, recommended at T3), architecture review record (row 5), guardrail configuration and test results (row 9; the [GenAI risk matrix](../risk-classification/genai-risk-matrix.md#governance-requirements-by-tier-genai-specific) still expects basic input validation at T3), incident response playbook and on-call (row 15), rollback plan (row 16) and human oversight (PM-003).

**Sign-off.** No fast-lane decision goes to the AI Risk Committee or the architecture review board, and the second line does not approve the risk assessment, the design or the deployment.

| Decision | T3 | T4 |
|---|---|---|
| Risk assessment | Team lead | Team lead acknowledges the self-assessment |
| Model selection | Team lead (approved vendor list) | Team lead (approved vendor list) |
| Evaluation release | Team lead sign-off | Self-attested |
| Red-team result (where run) | Security lead; Critical blocks, High needs a recorded risk acceptance | Security lead; Critical blocks, High needs a recorded risk acceptance |
| Deployment | Team lead; business owner co-signs | Team lead |
| Exception | Head of AI | Team lead |

Two second-line touchpoints remain: AI Risk owns the T3 vendor risk assessment (AR-005) when the system calls an external vendor API, and the DPO owns DPIA screening (RA-005) when personal data is processed. Request both at intake.

**Still non-waivable.** Audit logging (interaction logs retained 3 years at T3 and 1 year at T4, per [prompt audit trail](../compliance/prompt-audit-trail.md#retention-requirements)), the prohibited-use check, zero unresolved Critical red-team findings, and a DPIA where the law requires one.

**After go-live.** From the Stage 8 and Stage 9 tables: online automated scoring of a 5% sample (T3) or a weekly batch sample (T4); metrics review monthly (T3) or quarterly (T4); full offline suite re-run semi-annually; vendor behaviour canary monthly for external models; RAG retrieval evaluation quarterly (T3); formal review annually (T3) or annual self-assessment (T4); revalidation by peer re-review on material change. Incident reporting per severity SLA and post-mortems for S1/S2 incidents apply at every tier.

**Leaving the fast lane.** Run the re-tiering check at every formal review and on any [material change](#stage-9-ongoing-governance) ([risk matrix decision process](../risk-classification/risk-matrix.md#decision-process)). The system leaves the fast lane when the check gives T2 or above. Common triggers:
- It starts serving customers or other external parties. Customer-facing content without per-output human review is automatic T1 (override item 2).
- Customer personal data reaches an external LLM API (override items 3 and 8).
- It gains tool use of any kind, read-only included (item 6), or write access or authority to act (item 4).
- Its output starts to make or directly influence a regulated decision (item 1).
- It adds biometric, synthetic media or visual personal data processing (items 5, 7 and 9).
- Any risk dimension scores High or Critical, for example confidential business data entering prompts (Data Exposure Risk: High).

A proposed change that raises the tier goes back through Stage 2 for approval at the new tier, and the changed version needs the new tier's minimum evidence pack and deployment approval before it goes live. If the change has already happened, for example scope drift found at a review, the missing controls for the new tier are handled under [Exceptions and Risk Acceptance](#exceptions-and-risk-acceptance) until the evidence exists.

## Small Teams

These rules decide which roles one person may combine. They restate [roles and responsibilities](../operating-model/roles-responsibilities.md), [validation independence](../model-lifecycle/validation.md#validation-independence) and the [red-teaming protocol](../ai-security/red-teaming-protocol.md#team-and-qualifications). [START-HERE](../../START-HERE.md#small-teams) shows how a team of 3 to 5 people applies them.

**May be combined at any tier.** The first-line delivery roles: Product owner, System owner, AI lead, Technical owner and AI Operations. Each is still named in the AI system inventory, with exactly one Business owner, one Product owner and one AI lead per system.

**Must be different people wherever the activity applies.**
- Red-teaming is never done by the build team: you cannot red-team your own system.
- T3 peer review, for validation and for prompt review, is done by someone other than the developer.
- Where two roles sign (T3 deployment: team lead and business owner), two different people sign.

**Must sit outside the team at T1 and T2.**
- Independent validation: Model Risk Management, full scope (T1); MRM or another second-line reviewer who did not contribute to development, reduced scope (T2). The team that builds a T1 or T2 model never validates it.
- Risk assessment approval: AI Risk Committee (T1); AI Risk, second line (T2).
- Architecture, model selection and deployment approval, per [Approvals by Tier](../operating-model/roles-responsibilities.md#approvals-by-tier).
- Prompt review beyond the peer: the prompt engineering lead (T2), plus security review and AI Risk sign-off (T1).
- Vendor risk assessment (AR-005, AI Risk) and DPIA (RA-005, DPO).

A small team cannot supply any of these from inside. Book them at intake, not at Stage 5. A T1 or T2 system also needs a staffed on-call rotation (IR-002) and staffed human oversight (PM-003), which usually means sharing with an AI Operations or business operations team.

## Exceptions and Risk Acceptance

This is the only process for proceeding without meeting a control. An exception is time-limited, recorded, and approved by the authority for the system's tier.

**Non-waivable.** These cannot be excepted at any tier:
- A DPIA where it is legally required
- Checks against prohibited uses (RA-007)
- Zero unresolved Critical red-team findings (the Critical part of SR-002)
- A kill switch for T1 customer-facing systems and for all agentic systems (PM-006)
- Audit logging (PM-007)

Any other control can be excepted through this process.

**Exception register.** Every exception is recorded with these fields:

| Field | Content |
|-------|---------|
| Exception ID | Unique reference |
| System | System name and ID |
| Control ID | The control being excepted |
| Reason | Why the control cannot be met now |
| Compensating controls | What reduces the risk while the exception is open |
| Approver | Name and role, per the table below |
| Start date | Date the exception takes effect |
| Expiry date | No more than 90 days after the start date |
| Status | Open, renewed, closed or expired |

**Duration.** 90 days maximum. One renewal at most, approved one level higher than the original approver. For T1, where the AI Risk Committee is already the approver, a renewal needs a full committee decision (not a delegated or out-of-cycle one) and is reported to the Board Risk Committee.

**Approvers:**

| Tier | Approver |
|------|----------|
| T1 | AI Risk Committee |
| T2 | Head of AI Risk |
| T3 | Head of AI |
| T4 | Team lead |

## Retroactive Governance

For organizations with AI systems already in production without this evidence trail:

1. **Inventory**: List all production AI systems. Assign a tier to each using the risk assessment process in Stage 2. Do not skip the auto-override checks.
2. **Gap assessment**: For each system, walk the control register and mark every control as: evidence exists, evidence missing, or not applicable. This produces a gap matrix per system.
3. **Prioritize by tier**: T1 systems are remediated first, then T2, T3, and T4. Within a tier, prioritize by customer impact and regulatory exposure.
4. **Remediation plan**: For each missing evidence item, define: who will produce it, by when, and what interim mitigation is in place until the evidence is produced.
5. **Timeline**: T1 gap remediation within 3 months. T2 within 6 months. T3/T4 within 12 months. These timelines are non-negotiable for regulated environments.
6. **Governance operations**: Once remediated, systems enter the normal ongoing governance cycle (Stage 9). From that point forward, they follow the same cadence as newly deployed systems.
