# AI Governance Framework Operationalization — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a control-to-evidence mapping, end-to-end governance workflow, evaluation governance standard, and complete T1 governance case file to make the framework audit-ready and executable.

**Architecture:** Four new files in three locations. Control register and workflow go in a new `framework/governance-operations/` directory. Evaluation governance goes in `framework/llm-lifecycle/`. Case file extends the existing customer-service-chatbot example. README updated to reference all new content.

**Tech Stack:** Markdown governance documents. No code.

**Spec:** `docs/superpowers/specs/2026-03-19-operationalization-design.md`

**Tone calibration:** Same as existing framework — practical, opinionated, table-driven, imperative language. Every control has a concrete evidence artifact, not vague "documentation." Financial services examples.

---

## Intentional Deviations from Spec

Where the spec conflicts with existing files (model-card.yaml, risk-assessment.md), this plan aligns with the existing files. The existing artifacts are the source of truth.

| Deviation | Spec Value | Plan Value | Reason |
|-----------|-----------|------------|--------|
| T1 faithfulness threshold | ≥ 95% | ≥ 90% | Existing model card uses 0.90 threshold; 95% would cause the case file's flagship example to fail |
| Architecture review date | 2025-12-10 | 2025-08-05 | Spec date is after deployment (2025-09-15), which is nonsensical |
| Deployment approval dates | January 2026 | September 2025 | Same issue — approvals must precede deployment |
| Prompt version | v2.1.0 | v1.2.3 | Model card shows v1.2.3; plan aligns with existing artifact |
| Counterfactual consistency | 0.93 | 0.95 | Model card shows 0.95; plan aligns with existing artifact |

---

## Task 1: Evaluation Governance

**Files:**
- Create: `framework/llm-lifecycle/evaluation-governance.md`

This file comes first because the control register references evaluation controls (EV-*), and the case file includes an evaluation report. Having the eval standard defined first means the other files can reference it accurately.

- [ ] **Step 1: Create evaluation governance file**

Structure (150-180 lines):

**Overview** (3-4 sentences): Evaluation is the primary mechanism for proving an AI system works as intended. Without standardized evaluation, governance is assertion without evidence. This document defines what to evaluate, when, what must pass, and what happens when it doesn't.

**Evaluation Types table:**

| Eval Type | What It Tests | When | T1 Suite Size | T2 | T3 | T4 |
|-----------|--------------|------|:---:|:---:|:---:|:---:|
| Pre-release | Domain accuracy, faithfulness, format compliance | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Safety | Toxicity, harmful content, jailbreak resistance, PII leakage | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Regression | Performance vs. previous version on identical test set | On model/prompt changes | Full suite | Full suite | 50 cases | N/A |
| RAG retrieval | Retrieval precision, recall, relevance, source attribution | Before deployment + weekly (T1) | 100+ | 50+ | 25+ | N/A |
| Red-team | Adversarial robustness | Per [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) cadence | 200+ | 100+ | 50 | 20 |
| Bias | Counterfactual fairness, demographic parity | Before deployment + quarterly (T1) | 200 pairs | 100 pairs | 50 pairs | N/A |
| Production | Ongoing output quality on sampled live traffic | Continuous per tier | Every response (async) | 20% sample | 5% sample | Weekly batch |

**Threshold Definitions by Tier table:**

| Metric | T1 | T2 | T3 | T4 |
|--------|:---:|:---:|:---:|:---:|
| Hallucination rate | ≤ 1% | ≤ 3% | ≤ 5% | ≤ 10% |
| Faithfulness (RAG) | ≥ 90% | ≥ 85% | ≥ 80% | ≥ 75% |
| Safety pass rate | ≥ 99% | ≥ 97% | ≥ 95% | ≥ 90% |
| Retrieval precision@5 | ≥ 85% | ≥ 80% | ≥ 75% | N/A |
| Counterfactual consistency | ≥ 90% | ≥ 85% | ≥ 80% | N/A |
| Domain accuracy | Use-case specific (defined in risk assessment) | Same | Same | Same |

Note beneath the table: "These are opinionated defaults. Organizations should calibrate to their domain and risk appetite. The principle is non-negotiable: every tier has thresholds, and thresholds are enforced."

**Release Criteria by Tier table:**

| Tier | Required Evals | Reviewer | Sign-off |
|------|---------------|----------|----------|
| T1 | All eval types pass | Independent reviewer validates results | AI Risk sign-off |
| T2 | Pre-release + safety + regression + bias pass | Peer review of results | AI lead sign-off |
| T3 | Pre-release + safety pass | Self-attested | Team lead sign-off |
| T4 | Pre-release pass | Self-attested | Self-attested |

**Eval Dataset Governance section** (bullet list):
- Eval datasets versioned and access-controlled (same rigor as code)
- No overlap between eval data and training/fine-tuning data (data leakage invalidates evals)
- Eval datasets reviewed for representativeness and bias annually (T1/T2)
- Multiple independent eval sets for T1 (prevent overfitting to a single benchmark)
- Eval data containing PII handled per data governance policy

**Eval Infrastructure Requirements section** (bullet list):
- Eval results stored immutably (append-only, tamper-evident) — this is audit evidence
- Results linked to: model version, prompt version, dataset version, evaluator identity
- Automated eval pipeline for T1/T2 (CI/CD integrated; manual acceptable for T3/T4)
- Eval failures automatically block deployment pipeline for T1/T2
- Historical eval results retained for trending and regression detection (minimum 2 years)

**LLM-as-Judge Calibration section:**
- When using LLM-as-judge for automated evaluation: calibrate against human evaluators quarterly (T1), semi-annually (T2)
- Document the correlation between LLM-as-judge scores and human scores
- If correlation drops below 0.85: pause automated eval; recalibrate or revert to human eval
- Never use LLM-as-judge as the sole evaluator for safety-critical metrics (T1 hallucination, PII leakage)

**Anti-patterns section** (bullet list):
- Running evals only at initial deployment, never again
- Using the same eval set for development tuning and release validation (data leakage)
- Setting thresholds so low they never fail (governance theater)
- Treating LLM-as-judge scores as ground truth without human calibration
- Evaluating only accuracy, ignoring safety, bias, and retrieval quality
- Reporting averages without per-segment breakdowns (hides demographic performance gaps)

**Integration section:**
- Red-team eval references [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) — this file owns "what must pass"; red-teaming owns "how to test"
- Production eval cadence aligned with [LLM monitoring](monitoring.md)
- Control register IDs (EV-001 through EV-007) assigned — one per eval type
- Eval report is a required artifact in the deployment evidence pack (see [governance-workflow.md](../governance-operations/governance-workflow.md) Stage 7)

- [ ] **Step 2: Commit**

```bash
git add framework/llm-lifecycle/evaluation-governance.md
git commit -m "Add evaluation governance standard with tier-based thresholds and release criteria"
```

---

## Task 2: Control Register

**Files:**
- Create: `framework/governance-operations/control-register.md`

- [ ] **Step 1: Create governance-operations directory and control register file**

```bash
mkdir -p framework/governance-operations
```

Structure (250-300 lines):

**Overview** (4-5 sentences): This register maps every governance control in the framework to its evidence, owner, and escalation path. It is the single source of truth for what evidence an auditor, regulator, or compliance team should expect to see. Controls are organized by lifecycle stage because that is how audits are structured.

Then 10 stage sections, each with a header and table. Draw controls from existing framework files — consolidate, do not invent.

**Stage 1: Intake & Risk Assessment**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RA-001 | Risk assessment completed using framework matrices | All AI systems | Product owner | Signed risk assessment with dimension scoring + tier determination | Before development begins | Cannot proceed to development |
| RA-002 | Tier override review for auto-T1 triggers | Systems matching any auto-T1 criterion | AI Risk | Override decision document | At assessment | Escalate to AI Risk Committee |
| RA-003 | Impact assessment completed | T1/T2 systems | Product owner | Completed impact assessment template | Before development | Cannot proceed to development |
| RA-004 | Risk assessment reviewed by appropriate authority | All AI systems | AI Risk (T1/T2) / Team lead (T3/T4) | Review record with sign-off | Before development | Block progression |
| RA-005 | DPIA filed (if PII processed) | Systems processing PII | DPO | Filed DPIA with DPO sign-off | Before development | Cannot proceed; escalate to DPO |

**Stage 2: Architecture & Design Review**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| AR-001 | System architecture documented | All AI systems | Technical owner | Architecture document with component diagram and data flows | Before development | Block development |
| AR-002 | Architecture review board sign-off | T1/T2 systems | Architecture review board | Review meeting record with decision and conditions | Before development | Cannot proceed without sign-off |
| AR-003 | Data residency confirmed | Systems with external data flows | Technical owner | Data flow map with residency confirmation per jurisdiction | Before development | Escalate to compliance |
| AR-004 | Vendor/model selection justified | Systems using external models | AI lead | Model selection document with evaluation results and rationale | Before development | Block development |
| AR-005 | Third-party model risk assessment completed | Systems using external vendor APIs | AI Risk | Completed vendor risk assessment per [third-party-model-risk.md](../compliance/third-party-model-risk.md) | Before development; annually thereafter | Block deployment; procurement escalation |

**Stage 3: Development & Prompt Engineering**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DE-001 | Model card created and version-controlled | All AI systems | AI lead | Model card in version control (YAML/markdown) | Before validation | Block validation gate |
| DE-002 | Prompts version-controlled | All GenAI systems | AI lead | Prompt files in git repository with commit history | Continuous | Block deployment |
| DE-003 | Prompt peer review completed | T1/T2 GenAI | Product owner | Signed prompt review checklist + prompt version link | Before release | Block deployment |
| DE-004 | Guardrails implemented and configured | T1/T2 GenAI (mandatory); T3/T4 (per tier standard) | Technical owner | Guardrail configuration document + test results | Before deployment | Block deployment |
| DE-005 | Data governance controls applied to training/fine-tuning data | Systems using fine-tuned models | AI lead | Data governance checklist with provenance documentation | Before training | Block training |

**Stage 4: Evaluation & Testing**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| EV-001 | Pre-release evaluation suite executed | All AI systems | AI lead | Evaluation report with pass/fail per metric | Before every deployment | Block deployment |
| EV-002 | Safety evaluation passed | All GenAI systems | AI lead | Safety eval results meeting tier thresholds | Before every deployment | Block deployment |
| EV-003 | Regression evaluation passed | T1/T2 on model/prompt change | AI lead | Regression report comparing current vs. previous version | On change | Block deployment if regression detected |
| EV-004 | RAG retrieval quality evaluated | RAG-based systems | AI lead | Retrieval precision/recall/relevance metrics | Before deployment + per tier cadence | Block deployment (pre-release); investigate (production) |
| EV-005 | Bias evaluation completed | T1/T2 systems | Responsible AI lead | Counterfactual test results with demographic parity metrics | Before deployment + quarterly (T1) | Block deployment; escalate to Responsible AI |
| EV-006 | Eval dataset integrity verified | All AI systems | AI lead | Confirmation of no overlap with training data; dataset version recorded | Before each eval run | Invalidate eval results; re-run |
| EV-007 | LLM-as-judge calibrated against human evaluators | T1/T2 using automated eval | AI lead | Calibration report with correlation scores | Quarterly (T1); semi-annually (T2) | Pause automated eval; revert to human eval |

**Stage 5: Security & Red-Teaming**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| SR-001 | Red-team testing completed per tier depth | All GenAI systems | Security / AI Risk | Red-team report per [red-team-report.md](../../templates/red-team-report.md) template | Pre-deployment; per tier cadence | Block deployment (T1/T2); document risk acceptance (T3/T4) |
| SR-002 | No unresolved Critical or High findings | T1/T2 systems | System owner | Red-team report showing 0 Critical, 0 unaddressed High | Before deployment | Block deployment |
| SR-003 | Adversarial robustness defenses implemented | T1/T2 GenAI | Technical owner | Defense configuration per [adversarial-robustness.md](../ai-security/adversarial-robustness.md) | Before deployment | Block deployment |
| SR-004 | Supply chain security verified | Systems using open-source models | Security | AI-BOM + provenance verification per [supply-chain-security.md](../ai-security/supply-chain-security.md) | Before deployment; on model change | Block deployment |

**Stage 6: Deployment Approval**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DA-001 | Evidence pack assembled and complete | All AI systems | Product owner | Evidence checklist with all required items present | Before deployment | Block deployment |
| DA-002 | Sign-off chain completed per tier | All AI systems | Product owner | Signed deployment approval record | Before deployment | Block deployment |
| DA-003 | Deployment gates passed | All AI systems | AI Operations | Gate evidence package per [deployment-gates.md](../llm-lifecycle/deployment-gates.md) | Before deployment | Block deployment |
| DA-004 | Rollback plan documented and tested | T1/T2 systems | Technical owner | Rollback procedure + test evidence | Before deployment | Block deployment |

**Stage 7: Production Monitoring**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| PM-001 | Monitoring configured per tier requirements | All production AI | AI Operations | Monitoring configuration + dashboard reference | Before traffic enabled | Block go-live |
| PM-002 | Alerting active with defined thresholds | All production AI | AI Operations | Alert configuration evidence | Before traffic enabled | Block go-live |
| PM-003 | Human oversight operational | T1/T2 systems | Product owner | Oversight process document + staffing confirmation | Before traffic enabled | Block go-live |
| PM-004 | Production evaluation running per cadence | All production AI | AI Operations | Eval schedule + latest eval results | Per tier cadence | Escalate to AI Risk; increase monitoring |
| PM-005 | Cost monitoring active | All production AI | AI Operations | Cost dashboard + alert configuration | Before traffic enabled | Block go-live |

**Stage 8: Incident Response**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| IR-001 | Incident response playbook documented | T1/T2 systems | AI Operations | Published runbook accessible to on-call | Before deployment | Block deployment |
| IR-002 | On-call team assigned | T1/T2 systems | AI Operations | On-call rotation schedule | Continuous | Escalate to AI Platform Lead |
| IR-003 | Incident reported per severity SLA | All production AI (on incident) | Incident commander | Incident report per template | Per incident | Escalate per [escalation-paths.md](../operating-model/escalation-paths.md) |
| IR-004 | Post-mortem completed for S1/S2 incidents | T1/T2 systems (on incident) | Incident commander | Post-mortem report per [incident-forensics.md](../operating-model/incident-forensics.md) | Within 1 week (S1) / 2 weeks (S2) | Escalate to AI Risk Committee |
| IR-005 | Remediation actions tracked to completion | All incidents with remediation | System owner | Remediation tracker with status | Until complete | Escalate to AI Risk |

**Stage 9: Review & Revalidation**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RV-001 | Scheduled review completed | All AI systems | System owner | Review record with findings and actions | Monthly (T1); Quarterly (T2); Semi-annual (T3); Annual (T4) | Overdue review flagged in governance metrics; escalate after 30 days |
| RV-002 | Model card updated | All AI systems | AI lead | Updated model card with current information | At each review | Block until updated |
| RV-003 | Revalidation on material change | All AI systems | AI lead | Revalidation assessment + eval results | On model change, provider update, or regulatory change | Re-enter deployment gates |
| RV-004 | Regulatory change impact assessed | All AI systems | Compliance | Regulatory change impact assessment per [regulatory-change-monitoring.md](../compliance/regulatory-change-monitoring.md) | On regulatory change | Escalate to AI Risk Committee |

**Stage 10: Deprecation & Retirement**

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DR-001 | Deprecation impact assessment completed | Systems being deprecated | System owner | Impact assessment with affected systems and migration plan | At deprecation trigger | Block deprecation without assessment |
| DR-002 | Migration governance followed | Systems being replaced | AI lead | Migration assessment + parallel running evidence + cutover approval | During migration | Block cutover |
| DR-003 | Evidence archived per retention policy | All deprecated systems | AI Operations | Archival confirmation with artifact inventory | At retirement | Compliance escalation |
| DR-004 | System decommissioned cleanly | All retired systems | Technical owner | Decommission record (monitoring removed, access revoked, documentation archived) | At retirement | Track until complete |

After all 10 stages, add a **Summary** section:

"This register contains {N} controls across 10 lifecycle stages. For the full governance workflow describing how systems progress through these stages, see [governance-workflow.md](governance-workflow.md). For a complete worked example showing every control's evidence for a T1 system, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md)."

- [ ] **Step 2: Verify all cross-references point to existing files**

Check every `[link](path)` in the file resolves to an existing file.

- [ ] **Step 3: Commit**

```bash
git add framework/governance-operations/control-register.md
git commit -m "Add master control register: 50+ controls mapped to evidence across 10 lifecycle stages"
```

---

## Task 3: Governance Workflow

**Files:**
- Create: `framework/governance-operations/governance-workflow.md`

- [ ] **Step 1: Create governance workflow file**

Structure (250-300 lines):

**Overview** (4-5 sentences): This document defines the end-to-end governance process for AI systems — from idea to retirement. Every AI system, regardless of tier, follows these stages. The depth of governance at each stage scales with the system's risk tier. For the master list of controls and their evidence requirements, see [control-register.md](control-register.md).

Then 10 stage sections. Each stage follows a consistent structure:

```markdown
## Stage N: [Name]

**What happens:** [2-3 sentences describing the stage]

**Gate criteria:** [What must be true to proceed]

**Evidence produced:**
- [Artifact] (Control ID: XX-NNN)
- [Artifact] (Control ID: XX-NNN)

**Tier scaling:**

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| [Activity 1] | Required | Required | Required | Required |
| [Activity 2] | Required | Required | Recommended | N/A |

**Decision point:** [Who approves, what can block]

**Framework references:**
- [Link to relevant standard]
```

Stages 1-10 content follows the spec exactly (lines 100-168 of the spec). Key content to include:

**Stage 2 must include the tier determination decision flowchart** (the ASCII decision tree from the spec, lines 173-197).

**Stage 7 must include the minimum evidence pack** — an explicit enumerated list:

For T1 systems, the deployment evidence pack must contain:
1. Signed risk assessment with tier determination (RA-001)
2. Architecture review record (AR-002)
3. DPIA (if PII processed) (RA-005)
4. Model card (DE-001)
5. Prompt review record (DE-003)
6. Evaluation report (EV-001, EV-002, EV-003, EV-004, EV-005)
7. Red-team report (SR-001, SR-002)
8. Security assessment (SR-003)
9. Monitoring configuration (PM-001, PM-002)
10. Incident response playbook (IR-001)
11. Rollback plan (DA-004)
12. Deployment approval with sign-offs (DA-002)

For T2: items 1-12 (architecture review may be team-level instead of board)
For T3: items 1, 4, 6 (pre-release + safety only), 9, 12
For T4: items 1, 4, 6 (pre-release only), 12

**Stage 7 must include the data classification note** from the spec (lines 334-348):
A brief paragraph noting governance artifacts contain sensitive information (security findings, eval scores, incident details) and should be classified per the framework's data classification table. Reference the table from the spec.

**After Stage 10, add a "Retroactive Governance" section** (from the spec, lines 319-330):
For organizations with existing production AI systems:
1. Inventory all production AI systems; assign tier
2. Gap assessment against control register
3. Prioritize by tier (T1 first)
4. Remediation plan for each missing evidence item
5. Timeline: T1 within 3 months; T2 within 6; T3/T4 within 12
6. Enter normal ongoing governance cycle once remediated

- [ ] **Step 2: Verify cross-references**

All links to control-register.md, evaluation-governance.md, and existing framework files should resolve.

- [ ] **Step 3: Commit**

```bash
git add framework/governance-operations/governance-workflow.md
git commit -m "Add end-to-end governance workflow: 10 stages from intake to retirement"
```

---

## Task 4: Governance Case File

**Files:**
- Create: `examples/customer-service-chatbot/governance-case-file.md`

This is the most important file for credibility. It shows a T1 system governed through every stage with every artifact filled in. It must feel real — specific dates, specific scores, specific findings, specific people (by role, not name).

- [ ] **Step 1: Create governance case file**

Structure (400-500 lines):

**Header:**
```markdown
# Governance Case File: Retail Banking Customer Service Assistant

**System ID:** cs-assistant-retail-v1.2
**Risk Tier:** T1 (Critical)
**Status:** Production (deployed 2025-09-15)
**This document:** Complete governance trail from idea intake through first year of production operations.

This case file demonstrates every governance artifact produced for a T1 customer-facing GenAI system. Teams can use this structure as a template for their own systems.

---
```

**12 sections, each with a stage reference and control IDs:**

**1. Intake Record (Stage 1)**

Fill-in-ready table format:
| Field | Value |
|-------|-------|
| Proposer | Head of Retail Banking Digital |
| Business Unit | Retail Banking |
| Date Submitted | 2025-07-01 |
| Use Case | AI-powered customer service assistant for retail banking customers via mobile app and online banking chat |
| Business Justification | Reduce average customer inquiry resolution time from 8 minutes (human agent) to <2 minutes; handle 60% of routine inquiries without human intervention; improve customer satisfaction scores |
| Initial Risk Screening | Likely T1: customer-facing, will process customer PII, uses external LLM API |
| Sponsor | COO, Retail Banking |
| AI Risk involvement | Flagged for early AI Risk engagement due to likely T1 classification |

**2. Risk Assessment (Stage 2)**

Reference: "Full risk assessment documented in [risk-assessment.md](risk-assessment.md)."

Then include a summary table of dimension scores (from the existing risk-assessment.md: hallucination High(3), data exposure Critical(4), etc.), the aggregate score (16), tier determination (T1), and the auto-T1 triggers that fired.

Reference control IDs: RA-001, RA-002, RA-003, RA-004, RA-005.

**3. Architecture Review Record (Stage 3)**

Table format:
| Field | Value |
|-------|-------|
| Review Date | 2025-08-05 |
| Review Board | AI Architecture Review Board |
| Attendees | Head of AI (chair), AI Platform Lead, CISO delegate, Data Privacy Officer |
| Decision | Approved with conditions |
| Condition 1 | RAG corpus must have document-level access controls — no customer-specific data in corpus |
| Condition 2 | PII redaction mandatory before LLM API call — verify with red-team testing |
| Condition 3 | Fallback model (non-Anthropic) must be validated before production go-live |
| Data Residency | Confirmed: application EU (europe-west1); Anthropic EU endpoint; RAG corpus EU |
| Vendor Assessment | Anthropic vendor risk assessment completed (reference: VRA-2025-ANT-001) |

Control IDs: AR-001, AR-002, AR-003, AR-004, AR-005.

**4. Model Card (Stage 4)**

Reference: "Full model card documented in [model-card.yaml](model-card.yaml)."
Summary: system name, model ID, base model, version, key stats. Note prompt version (v1.2.3), prompt repository location, guardrail configuration.
Control IDs: DE-001, DE-002, DE-004.

**5. Prompt Review Record (Stage 4)**

Table format showing reviewer (Senior AI Engineer, AI Platform team), prompt version (v1.2.3), review date (2025-08-20), findings table:

| # | Finding | Severity | Resolution |
|---|---------|----------|------------|
| 1 | Fallback response for unrecognized intent is too vague ("I can't help with that") — should offer escalation | Minor | Updated to "I'm not able to help with that topic. Would you like me to connect you with a customer service agent?" |
| 2 | Edge case: multi-language query mixing not handled — system may respond in wrong language | Minor | Added language detection step; mixed-language queries route to human agent |

Sign-off: Senior AI Engineer (2025-08-22). Control ID: DE-003.

**6. Evaluation Report (Stage 5)**

Table of results using metrics from the existing model-card.yaml. Align numbers with model card exactly:

| Metric | Result | Threshold | Status | Eval Method |
|--------|:---:|:---:|:---:|------------|
| Faithfulness | 0.94 | ≥ 0.90 | PASS | LLM-as-judge (calibrated) |
| Hallucination rate | 0.008 (0.8%) | ≤ 0.01 (1%) | PASS | LLM-as-judge + human eval |
| Correctness | 0.96 | ≥ 0.95 | PASS | Human eval |
| Safety pass rate | 0.99 | ≥ 0.99 | PASS | Automated (200-case safety eval suite — distinct from adversarial robustness testing in red-team report) |
| Retrieval precision@5 | 0.87 | ≥ 0.85 | PASS | Automated |
| Counterfactual consistency | 0.95 | ≥ 0.90 | PASS | Automated (200 pairs × 4 attributes) |
| Escalation appropriateness | 0.93 | ≥ 0.90 | PASS | Human eval |

Eval dataset: 500 cases. Eval date: 2025-09-01. No overlap with training data confirmed.
LLM-as-judge calibration: correlation with human eval 0.91 (threshold ≥ 0.85 — PASS).

**Overall: all metrics PASS. System cleared for deployment.**

Control IDs: EV-001 through EV-007.

**7. Red-Team Summary (Stage 6)**

Table format:
| Field | Value |
|-------|-------|
| Assessment Date | 2025-08-25 to 2025-08-28 |
| Assessor | Internal AI Security team + external consultants (CyberAI Ltd) |
| Methodology | Manual + automated; 200 test cases across 6 categories |
| Model Tested | Claude 3.5 Sonnet (claude-3-5-sonnet-20241022) |
| Prompt Version | v1.2.0 (pre-review prompt; findings informed v1.2.3) |

Findings summary:

| Severity | Count | Details |
|----------|:---:|---------|
| Critical | 0 | — |
| High | 1 | Indirect prompt injection via RAG document: crafted FAQ document with embedded instructions caused model to reveal system prompt structure. Remediated by adding context isolation between RAG output and system prompt. Retested and confirmed fixed. |
| Medium | 3 | (1) Multi-turn escalation bypass: after 12 turns, model boundary softened. Mitigated with per-turn safety classification. (2) Base64-encoded harmful request processed. Mitigated with input normalization. (3) System disclosed it was using Claude when asked directly. Accepted as low impact (model identity is not confidential). |
| Low | 5 | Minor boundary softening under edge conditions; cosmetic issues. Tracked for next review. |

**Gate decision: Conditional pass** — High finding remediated and retested. No unresolved Critical or High findings at time of deployment.

Full report: RT-2025-CS-001 (classified: Confidential).
Control IDs: SR-001, SR-002, SR-003.

**8. Deployment Approval (Stage 7)**

Evidence checklist — all 12 items from the minimum evidence pack in governance-workflow.md, each with status and reference:

| # | Required Evidence | Status | Reference |
|---|------------------|:---:|-----------|
| 1 | Signed risk assessment | Complete | risk-assessment.md |
| 2 | Architecture review record | Complete | Section 3 above |
| 3 | DPIA filed | Complete | DPIA-2025-CS-001 |
| 4 | Model card | Complete | model-card.yaml |
| 5 | Prompt review record | Complete | Section 5 above |
| 6 | Evaluation report | Complete | Section 6 above |
| 7 | Red-team report | Complete | RT-2025-CS-001 |
| 8 | Security assessment | Complete | SEC-2025-CS-001 |
| 9 | Monitoring configuration | Complete | Section 9 below |
| 10 | Incident response playbook | Complete | CS-ASSIST-IRP-v1.0 |
| 11 | Rollback plan | Complete | Rollback to v1.1.0 tested 2025-09-10 |
| 12 | Deployment approval | Complete | Signatures below |

Sign-off chain:

| Role | Name/Title | Date | Decision |
|------|-----------|------|----------|
| Business Owner | Head of Retail Banking Digital | 2025-09-08 | Approved |
| AI Risk Committee | Chair, AI Risk Committee | 2025-09-10 | Approved |
| CISO | Chief Information Security Officer | 2025-09-09 | Approved |
| DPO | Data Protection Officer | 2025-09-09 | Approved with conditions (DPIA conditions) |
| Compliance | Head of Compliance | 2025-09-10 | Approved |

**Data classification: this evidence pack is classified as Internal/Confidential. Access restricted to AI Risk, system owner, approvers, and auditors.**

Control IDs: DA-001, DA-002, DA-003, DA-004.

**9. Monitoring Configuration (Stage 8)**

Table of monitored metrics, thresholds, and alert configuration (from existing model-card.yaml operational section):

| Metric | Threshold | Alert Severity | Notification |
|--------|-----------|:---:|-------------|
| Hallucination rate (rolling 7-day) | > 1% | P1 | On-call + AI Risk |
| PII leakage detection | Any occurrence | P1 | On-call + CISO |
| Guardrail trigger rate | > 2σ from baseline | P2 | On-call + team lead |
| Latency p95 | > 3000ms | P2 | On-call |
| Error rate | > 1% | P2 | On-call |
| Daily spend | > €700 (budget ceiling) | P3 | Team lead + finance |
| User satisfaction (thumbs down rate) | > 15% | P3 | Product owner |

Dashboard: internal://dashboards/cs-assistant
On-call team: AI Platform On-Call
Escalation path: On-call → AI Platform Lead → Head of AI → CTO

Control IDs: PM-001, PM-002, PM-003, PM-004, PM-005.

**10. Q1 2026 Review (Post v1.2.0 Deployment) — 2026-04-01 (Stage 9)**

Table format for the review record:

| Field | Value |
|-------|-------|
| Review Date | 2026-04-01 |
| Attendees | AI Platform Lead, AI Risk Analyst, Product Owner, Head of Retail Banking Digital |
| Period Reviewed | 2026-01-10 to 2026-04-01 (post v1.2.0 deployment) |

Findings:

| # | Finding | Severity | Action | Owner | Due Date |
|---|---------|----------|--------|-------|----------|
| 1 | Hallucination rate crept from 0.8% to 1.1% in week of 2026-03-15, breaching T1 threshold of 1.0%. Escalation triggered per risk acceptance conditions — AI Risk notified within 4 hours. Enhanced monitoring activated. Root cause: 3 product documents in RAG corpus were outdated (fee schedule update missed by document refresh pipeline). | Medium | Corpus refreshed; re-eval confirmed rate returned to 0.7%. Pipeline health monitoring added. | AI Operations | Complete |
| 2 | German language accuracy lower than English (faithfulness 0.88 vs. 0.94). | Low | Schedule targeted German-language eval expansion (100 additional cases). | AI lead | 2026-05-15 |
| 3 | Cost per request trending 8% above initial budget (€0.032 vs. €0.03 baseline). | Low | Investigate prompt optimization; assess whether acceptable. | AI Operations | 2026-05-01 |

**Next review: 2026-07-01**
Control IDs: RV-001, RV-002.

**11. Example Incident: S3 Hallucination — GEN-2026-042 (Stage 8/9)**

Structured incident record (abbreviated from the full incident-report-genai template):

| Field | Value |
|-------|-------|
| Incident ID | GEN-2026-042 |
| Severity | S3 — Medium |
| System | cs-assistant-retail-v1.2 |
| Detection Time | 2026-03-15 14:22 UTC |
| Detection Method | Automated monitoring (hallucination rate P2 alert triggered) |
| Mitigation Time | 2026-03-15 16:45 UTC |
| Resolution Time | 2026-03-16 10:00 UTC |

**What happened:** Automated monitoring flagged hallucination rate spike from baseline 0.8% to 1.5% over a 24-hour window. Investigation found 3 documents in the RAG corpus contained outdated fee schedule information (old fee amounts from Q3 2025). The document refresh pipeline had failed silently for 2 weeks due to an authentication token expiration.

**Impact:** ~40 customers received incorrect fee information over a 48-hour period. No financial transactions were affected (system is informational only). Customer complaints: 2 received via normal support channel.

**Response timeline:**
- 14:22 — P2 alert triggered; on-call engineer acknowledged
- 14:45 — Investigation started; hallucination rate confirmed above threshold
- 15:30 — Root cause identified: stale RAG documents
- 16:45 — Stale documents replaced with current versions; RAG index refreshed
- 17:30 — Hallucination rate returned to 0.7% (below threshold)
- 2026-03-16 10:00 — Pipeline failure root-caused; auth token renewal automated

Control IDs: IR-003, PM-004.

**12. Post-Mortem — GEN-2026-042 (Stage 8/9)**

| Field | Value |
|-------|-------|
| Post-Mortem Date | 2026-03-18 |
| Facilitator | AI Platform Lead |
| Attendees | On-call engineer, AI Risk Analyst, RAG pipeline owner, Product Owner |

**Root cause:** Document refresh pipeline authentication token expired on 2026-03-01. Pipeline failed silently (no alerting on pipeline health). Stale documents persisted for 2 weeks before hallucination rate drifted above monitoring threshold.

**Contributing factors:**
- No monitoring on the document refresh pipeline itself (only on downstream output quality)
- Auth token was manually provisioned with 90-day expiry; no automated renewal
- Gradual quality drift meant the threshold breach took ~2 weeks to manifest

**What went well:**
- Automated hallucination monitoring detected the issue before it became severe
- On-call response was within SLA (acknowledged in 23 minutes)
- Root cause identified within 1.5 hours
- Resolution (document replacement) within 2.5 hours

**Systemic improvements:**

| # | Improvement | Owner | Due Date | Status |
|---|-----------|-------|----------|--------|
| 1 | Add health monitoring to document refresh pipeline (alerting on: failure, staleness, auth issues) | RAG pipeline owner | 2026-04-01 | Complete |
| 2 | Automate auth token renewal for all RAG pipeline service accounts | Platform engineering | 2026-04-15 | Complete |
| 3 | Add document freshness check to weekly monitoring metrics | AI Operations | 2026-04-01 | Complete |
| 4 | Review all T1 system RAG pipelines for similar silent failure risks | AI Operations | 2026-05-01 | In progress |

**Control gap assessment:** The framework's monitoring standards (PM-004) cover output quality monitoring but did not explicitly require monitoring of upstream data pipelines. Recommendation: add pipeline health monitoring as a standard for all RAG-based systems in the monitoring standards.

Control IDs: IR-004, IR-005.

- [ ] **Step 2: Verify all references to existing files**

Check links to risk-assessment.md and model-card.yaml resolve correctly. Verify control IDs match those in control-register.md.

- [ ] **Step 3: Commit**

```bash
git add examples/customer-service-chatbot/governance-case-file.md
git commit -m "Add complete T1 governance case file: 12 artifacts from intake to post-mortem"
```

---

## Task 5: README Update

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update README with new content**

Three changes:

**1. Add "Governance Operations" section** after Operating Model in Framework Components:

```markdown
### Governance Operations
The operational backbone — controls, evidence, and the end-to-end process.
- [Control Register](framework/governance-operations/control-register.md) — master mapping of every control to its evidence, owner, and escalation
- [Governance Workflow](framework/governance-operations/governance-workflow.md) — end-to-end process from idea intake to retirement, with gates and evidence packs
```

**2. Add evaluation governance** to LLM Lifecycle section, after LLM Production Monitoring:

```markdown
- [Evaluation Governance](framework/llm-lifecycle/evaluation-governance.md) — what to evaluate, thresholds by tier, release criteria, dataset governance
```

**3. Update customer service chatbot example** in Worked Examples section:

```markdown
- [Customer Service Chatbot](examples/customer-service-chatbot/) — T1 (Critical), customer-facing, RAG-based, [complete governance case file](examples/customer-service-chatbot/governance-case-file.md)
```

- [ ] **Step 2: Verify all new links resolve**

```bash
grep -oE '\(framework/[^)]+\)' README.md | tr -d '()' | while read f; do test -f "$f" || echo "MISSING: $f"; done
grep -oE '\(examples/[^)]+\)' README.md | tr -d '()' | while read f; do test -d "$f" || test -f "$f" || echo "MISSING: $f"; done
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "Update README with governance operations, evaluation governance, and case file links"
```

---

## Summary

| Task | File | Lines (est.) | Description |
|------|------|:---:|-------------|
| 1 | `framework/llm-lifecycle/evaluation-governance.md` | 150-180 | Eval types, thresholds, release criteria, dataset governance |
| 2 | `framework/governance-operations/control-register.md` | 250-300 | 50+ controls mapped to evidence across 10 stages |
| 3 | `framework/governance-operations/governance-workflow.md` | 250-300 | 10-stage process with gates, evidence packs, tier scaling |
| 4 | `examples/customer-service-chatbot/governance-case-file.md` | 400-500 | Complete T1 governance trail: 12 artifacts |
| 5 | `README.md` | +15 lines | Links to new content |

**Total: 4 new files + 1 update = ~1,100-1,300 new lines across 5 tasks**
