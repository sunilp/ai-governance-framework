# AI Governance Framework — Operationalization Design (Spec 1)

**Date:** 2026-03-19
**Scope:** Control-to-evidence mapping + end-to-end governance workflow + evaluation governance
**Goal:** Move the framework from "governance reference" to "governance operating system" — audit-ready, evidence-oriented, executable.

---

## Problem Statement

The framework has strong coverage of governance controls, risk classification, lifecycle standards, and regulatory mapping. But a reader cannot yet answer: "What evidence do I need to produce, at what stage, and what happens if I don't?" That question is what auditors, compliance teams, and enterprise buyers ask first.

Three artifacts close this gap:
1. A master control register mapping every control to its evidence
2. An end-to-end workflow showing how governance flows from intake to retirement
3. An evaluation governance standard consolidating scattered eval requirements

---

## Artifact 1: Control Register

### File
`framework/governance-operations/control-register.md`

### Purpose
Single master table mapping every governance control to: who owns it, what evidence proves it exists and is operating, how often evidence is produced, and what happens if it fails.

### Structure
Tables organized by lifecycle stage (not by framework section), because auditors think in lifecycle stages. Ten stages, each with 5-10 controls. Total ~50-60 controls.

### Stages

1. **Intake & Risk Assessment** (RA-001 through RA-00N)
2. **Architecture & Design Review** (AR-001 through AR-00N)
3. **Development & Prompt Engineering** (DE-001 through DE-00N)
4. **Evaluation & Testing** (EV-001 through EV-00N)
5. **Security & Red-Teaming** (SR-001 through SR-00N)
6. **Deployment Approval** (DA-001 through DA-00N)
7. **Production Monitoring** (PM-001 through PM-00N)
8. **Incident Response** (IR-001 through IR-00N)
9. **Review & Revalidation** (RV-001 through RV-00N)
10. **Deprecation & Retirement** (DR-001 through DR-00N)

### Table Format

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RA-001 | Risk assessment completed | All AI systems | Product owner | Signed risk assessment + tier determination | Before development | Cannot proceed to development |

### Column Definitions

- **Control ID**: stable identifier (stage prefix + number) for cross-referencing from policy-as-code, audit reports, and case files
- **Control**: what must be done (imperative, specific)
- **Applies To**: tier + system type (e.g., "T1/T2 GenAI", "All agentic", "All production AI")
- **Owner**: role responsible for producing evidence (not a named person)
- **Evidence**: specific artifact(s) that prove the control is operating — never vague ("documentation"), always concrete ("signed risk assessment + tier determination")
- **Frequency**: when evidence must be produced (before development, before release, quarterly, annual, on change)
- **Escalation if Failed**: what happens if the control is not satisfied — always an action ("block deployment", "escalate to AI Risk Committee", "human review required")

### Content Sources
Controls are derived from existing framework files — this register does not invent new controls, it consolidates and maps evidence to what already exists:
- Risk classification → RA-* controls
- Deployment gates (Gate 1: architecture review) + data-residency-llm + third-party-model-risk → AR-* controls (no single architecture-review file exists; AR controls synthesized from these sources)
- Development/prompt engineering standards → DE-* controls
- Evaluation (new file) → EV-* controls
- Red-teaming protocol + adversarial robustness → SR-* controls
- Deployment gates → DA-* controls
- Production monitoring → PM-* controls
- Escalation paths + incident templates → IR-* controls
- Review cadence → RV-* controls
- Model deprecation governance → DR-* controls

### Cross-References
- Each control references the framework file that defines it in detail
- The governance workflow (Artifact 2) references control IDs at each stage
- The case file (Artifact 2) shows completed evidence for each control
- Policy-as-code (future Spec 2) will use these control IDs as machine-readable identifiers

---

## Artifact 2: End-to-End Governance Workflow + Case File

### Files
- `framework/governance-operations/governance-workflow.md` — the process
- `examples/customer-service-chatbot/governance-case-file.md` — the worked example

### Purpose
The workflow shows the 10 lifecycle stages as a step-by-step process with decision points, gates, and evidence produced. The case file shows a T1 customer service chatbot walked through every stage with every artifact filled in.

### Workflow Structure (`governance-workflow.md`)

Ten stages, each containing:
- **Description**: what happens at this stage (2-3 sentences)
- **Gate criteria**: what must be true to proceed to the next stage
- **Evidence produced**: specific artifacts, referencing control register IDs
- **Decision point**: who approves, what can block progress
- **Tier scaling**: how T1/T2/T3/T4 differ at this stage (table)
- **Framework references**: links to the detailed standard for each control

#### Stage 1: Idea Intake
- Use case proposal submitted
- Initial risk screening (could this be T1? Is it customer-facing? Agentic? Regulated decision?)
- Output: intake form with initial risk screening
- Gate: sponsor identified, business justification documented
- Tier scaling: same process all tiers; T1/T2 flagged for early AI Risk involvement

#### Stage 2: Risk Assessment & Tiering
- Full risk assessment using framework matrices (traditional ML, GenAI, multimodal, agentic as applicable)
- Tier determined; auto-overrides checked
- Output: completed risk assessment, tier determination
- Gate: risk assessment reviewed and accepted by appropriate authority (T1: AI Risk Committee; T2: Head of AI; T3: team lead; T4: self-assessment)
- Decision flowchart: text-based decision tree for T1/T2/T3/T4 determination

#### Stage 3: Architecture & Design Review
- System architecture documented; data flows mapped; vendor/model selection
- For T1/T2: architecture review board sign-off
- Output: architecture review record (attendees, decision, conditions)
- Gate: architecture approved; data residency confirmed; vendor assessment completed (if external)

#### Stage 4: Development & Prompt Engineering
- Model card created and version-controlled
- Prompts developed, reviewed, and version-controlled
- Guardrails implemented (input validation, output filtering, PII redaction)
- Output: model card, prompt versions in VCS, guardrail configuration
- Gate: peer review completed (T1/T2); model card exists (all)

#### Stage 5: Evaluation & Testing
- Evaluation suites run per evaluation-governance.md
- Safety benchmarks, domain accuracy, RAG retrieval quality
- Output: evaluation report with pass/fail per metric
- Gate: all required evals pass thresholds for the system's tier
- Cross-reference: EV-* controls in control register

#### Stage 6: Security Review & Red-Teaming
- Adversarial testing per red-teaming-protocol.md
- Security assessment (prompt injection, data leakage, model extraction)
- Output: red-team report, security assessment
- Gate: no Critical findings; no unaddressed High findings (T1/T2)
- Cross-reference: SR-* controls

#### Stage 7: Deployment Approval
- Evidence pack assembled: all artifacts from stages 1-6 collected
- Sign-off chain completed per tier
- Output: deployment approval record (evidence checklist + signatures)
- Gate: all evidence present; all sign-offs obtained; no blocking findings
- Minimum evidence pack enumerated explicitly

#### Stage 8: Production Operations
- Monitoring configured per monitoring standards
- Alerting active; human oversight in place
- Runbook documented; on-call assigned
- Output: monitoring configuration evidence, dashboard reference
- Gate: monitoring operational before traffic enabled

#### Stage 9: Ongoing Governance
- Scheduled reviews per review cadence (monthly T1, quarterly T2, semi-annual T3, annual T4)
- Revalidation triggered by: model changes, provider updates, regulatory changes, incidents
- Regulatory change impact assessed
- Output: review records, revalidation assessments
- Cross-reference: RV-* controls

#### Stage 10: Deprecation & Retirement
- Deprecation trigger identified; impact assessed
- Migration governance followed (if replacing)
- Evidence archived per retention policy
- System decommissioned
- Output: deprecation decision record, archival confirmation
- Cross-reference: DR-* controls

### Decision Flowchart
Text-based decision tree for tier determination, included in the workflow file:

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
  ├─ Score GenAI risk dimensions (hallucination, data exposure, prompt injection, output control, vendor dependency)
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

### Case File Structure (`governance-case-file.md`)

One long markdown file for the customer service chatbot showing completed governance artifacts at every stage:

1. **Intake Record** — proposer, business unit, use case description, business justification, initial risk screening (flagged as likely T1 due to customer-facing + RAG)
2. **Risk Assessment** — references existing `risk-assessment.md`; shows completed dimension scoring
3. **Architecture Review Record** — date (2025-12-10), attendees (4 roles), decision (approved with conditions), conditions (RAG access controls, PII redaction mandatory)
4. **Model Card** — references existing `model-card.yaml`
5. **Prompt Review Record** — reviewer name/role, prompt version (v2.1.0), review date, findings (2 minor — ambiguous fallback behavior, missing edge case), resolution, sign-off
6. **Evaluation Report** — table of eval results: faithfulness 0.94 (threshold 0.90 PASS), hallucination rate 0.008 (threshold 0.01 PASS), safety 0.99 (threshold 0.99 PASS), retrieval precision@5 0.87 (threshold 0.85 PASS), bias counterfactual consistency 0.93 (threshold 0.90 PASS)
7. **Red-Team Summary** — engagement scope, 200 test cases, findings: 0 Critical, 1 High (indirect injection via RAG document — remediated), 3 Medium, 5 Low. Gate decision: conditional pass after High finding remediated and retested.
8. **Deployment Approval** — evidence checklist (12 items all checked), sign-off: AI Risk Committee (2026-01-15), CISO (2026-01-14), Compliance (2026-01-13), Business Owner (2026-01-12)
9. **Monitoring Configuration** — metrics monitored (faithfulness, hallucination rate, guardrail triggers, latency, cost, user feedback), alert thresholds, dashboard URL, on-call team
10. **First Quarterly Review (2026-04-01)** — review date, attendees, findings (hallucination rate crept from 0.8% to 1.1% — breached T1 threshold of 1.0%, triggering escalation per risk assessment conditions; AI Risk notified within 4 hours; system placed under enhanced monitoring while root cause investigated; RAG corpus had stale documents), actions (corpus refresh, re-eval, hallucination rate returned to 0.7%), next review date
11. **Example Incident: S3 Hallucination** — incident ID GEN-2026-042, severity S3, detection (automated monitoring flagged hallucination rate spike to 1.5%), investigation (3 stale documents in RAG corpus generating incorrect policy answers), resolution (documents updated, re-eval passed), timeline
12. **Post-Mortem** — blameless review, root cause (document refresh pipeline had silent failure for 2 weeks), contributing factors (no alerting on document refresh pipeline health), systemic improvements (add pipeline health monitoring, add document freshness check to weekly metrics), remediation status

### Key Design Decisions
- Case file is one markdown file — scroll through the whole journey, don't jump between 12 files
- References existing model-card.yaml and risk-assessment.md rather than duplicating content
- The incident + post-mortem is fictional but realistic — demonstrates the framework in action, not just in theory
- Each section is structured so other teams can copy the format for their own systems
- Control register IDs cited in evidence sections — readers can trace from case file to control to standard

---

## Artifact 3: Evaluation Governance

### File
`framework/llm-lifecycle/evaluation-governance.md`

### Purpose
First-class governance standard for AI evaluations. Currently evaluation requirements are scattered across monitoring.md, deployment-gates.md, and prompt-engineering-standards.md. This consolidates into one authoritative source.

### Structure

#### Evaluation Types

| Eval Type | What It Tests | When | T1 Suite Size | T2 | T3 | T4 |
|-----------|--------------|------|:---:|:---:|:---:|:---:|
| Pre-release | Domain accuracy, faithfulness, format compliance | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Safety | Toxicity, harmful content, jailbreak resistance, PII leakage | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Regression | Performance vs. previous version on identical test set | On model/prompt changes | Full suite | Full suite | 50 cases | N/A |
| RAG retrieval | Retrieval precision, recall, relevance, source attribution | Before deployment + weekly (T1) | 100+ | 50+ | 25+ | N/A |
| Red-team | Adversarial robustness | Per red-teaming-protocol.md cadence | 200+ | 100+ | 50 | 20 |
| Bias | Counterfactual fairness, demographic parity | Before deployment + quarterly (T1) | 200 pairs | 100 pairs | 50 pairs | N/A |
| Production | Ongoing output quality on sampled live traffic | Continuous per tier | Every response (async) | 20% sample | 5% sample | Weekly batch |

#### Threshold Definitions by Tier

| Metric | T1 | T2 | T3 | T4 |
|--------|:---:|:---:|:---:|:---:|
| Hallucination rate | ≤ 1% | ≤ 3% | ≤ 5% | ≤ 10% |
| Faithfulness (RAG) | ≥ 95% | ≥ 90% | ≥ 85% | ≥ 80% |
| Safety pass rate | ≥ 99% | ≥ 97% | ≥ 95% | ≥ 90% |
| Retrieval precision@5 | ≥ 85% | ≥ 80% | ≥ 75% | N/A |
| Counterfactual consistency | ≥ 90% | ≥ 85% | ≥ 80% | N/A |
| Domain accuracy | Use-case specific (defined in risk assessment) | Same | Same | Same |

Note: these are opinionated defaults. Organizations should calibrate to their domain and risk appetite.

#### Release Criteria by Tier

| Tier | Required Evals | Reviewer | Sign-off |
|------|---------------|----------|----------|
| T1 | All eval types pass | Independent reviewer validates results | AI Risk sign-off |
| T2 | Pre-release + safety + regression + bias pass | Peer review of results | AI lead sign-off |
| T3 | Pre-release + safety pass | Self-attested | Team lead sign-off |
| T4 | Pre-release pass | Self-attested | Self-attested |

#### Eval Dataset Governance
- Eval datasets versioned and access-controlled (same rigor as code)
- No overlap between eval data and training/fine-tuning data
- Eval datasets reviewed for representativeness and bias annually (T1/T2)
- Multiple independent eval sets for T1 (prevent overfitting to a single benchmark)
- Eval data containing PII handled per data governance policy

#### Eval Infrastructure Requirements
- Eval results stored immutably (append-only, tamper-evident)
- Results linked to: model version, prompt version, dataset version, evaluator identity
- Automated eval pipeline for T1/T2 (CI/CD integrated; manual acceptable for T3/T4)
- Eval failures automatically block deployment pipeline for T1/T2
- Historical eval results retained for trending and regression detection

#### Anti-patterns
- Running evals only at initial deployment, never again
- Using the same eval set for development tuning and release validation (data leakage)
- Setting thresholds so low they never fail (governance theater)
- Treating LLM-as-judge scores as ground truth without human calibration
- Evaluating only accuracy, ignoring safety, bias, and retrieval quality

#### Integration
- Red-team eval references red-teaming-protocol.md (this file owns "what must pass"; red-teaming owns "how to test")
- Production eval cadence aligned with monitoring.md
- Control register IDs (EV-001 through EV-00N) assigned for each eval requirement
- Eval report is a required artifact in the deployment evidence pack (governance-workflow.md Stage 7)

---

## Files Summary

| File | Type | Lines (est.) |
|------|------|:---:|
| `framework/governance-operations/control-register.md` | New | 250-300 |
| `framework/governance-operations/governance-workflow.md` | New | 250-300 |
| `framework/llm-lifecycle/evaluation-governance.md` | New | 150-180 |
| `examples/customer-service-chatbot/governance-case-file.md` | New | 400-500 |
| `README.md` | Updated | +20 lines |

**File placement note:** `control-register.md` and `governance-workflow.md` are placed in a new `framework/governance-operations/` subdirectory rather than at the `framework/` root. The existing framework organizes all content into subdirectories. These files are cross-cutting (they reference every other section) but creating a dedicated subdirectory preserves the established convention.

### Existing File Updates
- `README.md` — add Governance Operations section with control register and workflow; add evaluation governance to LLM Lifecycle; add case file to customer service chatbot example

### Files NOT Modified
All existing framework files remain unchanged. The control register references them; they do not need to reference back.

---

## Retroactive Governance

For organizations with AI systems already in production without this evidence trail:

1. **Inventory** — list all production AI systems; assign tier using the risk assessment process
2. **Gap assessment** — for each system, walk the control register and mark: evidence exists / evidence missing / not applicable
3. **Prioritize by tier** — T1 systems remediated first, then T2, T3, T4
4. **Remediation plan** — for each missing evidence item, define: who will produce it, by when, and what interim mitigation is in place
5. **Timeline** — T1 gap remediation within 3 months; T2 within 6 months; T3/T4 within 12 months
6. **Governance operations** — once remediated, systems enter the normal ongoing governance cycle (Stage 9)

Include this as a section in `governance-workflow.md`.

---

## Data Classification of Governance Artifacts

Governance artifacts (risk assessments, case files, red-team reports, incident post-mortems) contain sensitive information: security findings, system architecture details, evaluation scores, incident details. These artifacts must themselves be classified and access-controlled.

| Artifact Type | Recommended Classification | Access |
|--------------|---------------------------|--------|
| Risk assessment | Internal / Confidential | AI Risk, system owner, approvers |
| Red-team report | Confidential | AI Risk, CISO, system owner |
| Incident post-mortem | Internal / Confidential | AI Risk, system owner, on-call |
| Governance case file | Internal | AI teams, compliance, audit |
| Control register | Internal | All AI practitioners |
| Evaluation reports | Internal | AI teams, AI Risk |
| Board reports | Board Confidential | Board, CTO, CRO, CISO |

Include a brief data classification note in `governance-workflow.md` (Stage 7: Deployment Approval, where the evidence pack is assembled).

---

## Success Criteria

1. An auditor can open `control-register.md` and know exactly what evidence to ask for at each governance stage
2. A new team can open `governance-workflow.md` and follow the process from intake to retirement without ambiguity
3. A reader can open `governance-case-file.md` and see exactly what "governed AI" looks like in practice — every artifact, every sign-off, every review
4. An AI lead can open `evaluation-governance.md` and know exactly what evals to run, what thresholds to hit, and what happens if they fail
5. Every control in the register traces to an existing framework file; no orphan controls
6. The case file's incident + post-mortem demonstrates the framework handling a real scenario, not just preventing one
7. Organizations with existing production AI systems have a clear retroactive governance path
