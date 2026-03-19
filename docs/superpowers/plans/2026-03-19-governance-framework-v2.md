# AI Governance Framework v2 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evolve the AI governance framework from EU/UK-focused, text-LLM-centric into a globally relevant, frontier-AI-aware, enterprise-operational governance body of work.

**Architecture:** Add ~24 new markdown files and update ~4 existing files across three dimensions — regulatory breadth (NIST, ISO 42001, multi-jurisdictional), AI frontier coverage (multimodal, multi-agent, security), and enterprise operationalization (board reporting, metrics, cost governance, GRC). One new directory (`framework/ai-security/`). All existing paths preserved.

**Tech Stack:** Markdown governance documents. YAML for model cards. No code.

**Spec:** `docs/superpowers/specs/2026-03-19-governance-framework-v2-design.md`

**Tone calibration:** Match existing framework files — practical, opinionated, field-tested. Use tables for structured requirements. Include specific examples from financial services. 80–180 lines per file (mapping files may exceed). No academic language. Every standard includes: what, when, who, which tier.

---

## Phase 1: Foundations (no inter-file dependencies)

### Task 1: Multimodal Risk Matrix

**Files:**
- Create: `framework/risk-classification/multimodal-risk-matrix.md`

- [ ] **Step 1: Create the multimodal risk matrix**

Structure to follow — mirrors `genai-risk-matrix.md` pattern:
- Overview: why multimodal AI needs its own risk dimensions beyond text-only GenAI
- Modality-specific risk dimensions (each as a table with Level/Description/Examples):
  - **Vision risks:** deepfake generation, CSAM detection failure, bias in facial/image recognition, OCR hallucination
  - **Audio risks:** voice cloning/impersonation, speaker identification without consent, transcription errors in regulated contexts, accent/dialect bias
  - **Video risks:** temporal manipulation (selective frame editing), surveillance-grade analysis, real-time deepfake
  - **Cross-modal risks:** text-to-image safety (generating harmful imagery from text), image-to-text hallucination (misinterpreting visual data), audio-visual synthesis (lip-sync deepfakes)
- Tier adjustment rules:
  - Systems generating synthetic media → minimum T2
  - Deepfake-capable systems → mandatory T1
  - Biometric processing systems → mandatory T1
  - Systems processing medical/diagnostic imagery → mandatory T1
- Integration note: use alongside `risk-matrix.md` and `genai-risk-matrix.md`; highest tier across all applicable matrices applies

- [ ] **Step 2: Verify cross-references**

Confirm links to `risk-matrix.md` and `genai-risk-matrix.md` are correct relative paths.

- [ ] **Step 3: Commit**

```bash
git add framework/risk-classification/multimodal-risk-matrix.md
git commit -m "Add multimodal AI risk classification matrix"
```

---

### Task 2: Adversarial Robustness Standards

**Files:**
- Create: `framework/ai-security/adversarial-robustness.md`

- [ ] **Step 1: Create the ai-security directory and adversarial robustness file**

```bash
mkdir -p framework/ai-security
```

Structure:
- Overview: defense-oriented standards for AI systems against adversarial attacks
- **Jailbreaking defenses** (table: Attack Type / Description / Defense / Tier Requirement):
  - Direct jailbreaking (role-play, authority impersonation, encoding tricks)
  - Multi-turn escalation (gradual boundary pushing)
  - Universal adversarial suffixes
  - Defenses: system prompt hardening, input classification, output filtering, layered defense patterns
- **Prompt injection mitigation** (table: Vector / Description / Mitigation):
  - Direct injection (user input)
  - Indirect injection (via RAG documents, tool outputs, API responses)
  - Defenses: input/output separation, instruction hierarchy, context isolation, sandwich defense
- **Model extraction prevention** (table: Attack / Risk / Mitigation):
  - Systematic querying to reconstruct model behavior
  - API abuse for training data extraction
  - Defenses: rate limiting, output perturbation, API access controls, watermarking, query logging
- **Data poisoning defenses**:
  - Training data poisoning (fine-tuning context)
  - RAG corpus poisoning (document injection)
  - Defenses: provenance tracking, integrity verification, anomaly detection on corpus changes
- **Privacy attacks**:
  - Membership inference, model inversion, PII extraction via crafted prompts
  - Defenses: differential privacy awareness, output filtering, PII detection
- **Monitoring for attacks** (table: Signal / Detection Method / Alert Threshold):
  - Anomalous query patterns, output distribution shifts, cost spikes, repeated similar queries, unusual error rates
- Tier requirements table: which defenses are mandatory at each tier

- [ ] **Step 2: Commit**

```bash
git add framework/ai-security/adversarial-robustness.md
git commit -m "Add adversarial robustness standards for AI security"
```

---

### Task 3: Supply Chain Security

**Files:**
- Create: `framework/ai-security/supply-chain-security.md`

- [ ] **Step 1: Create supply chain security file**

Structure:
- Overview: securing the AI model and component supply chain
- **Model provenance** (table: Check / Description / Tier Requirement):
  - Weight verification (checksums, signed releases)
  - Training data attestation (what data was used, opt-out compliance)
  - Model card credibility assessment (does the card match observed behavior?)
  - Safety evaluation verification (are claimed safety scores reproducible?)
- **Open-source model risk** (table: Risk Category / Description / Mitigation):
  - Licensing (Apache 2.0, Llama license, Mistral license — use restriction analysis)
  - Training data copyright exposure (pending litigation, opt-out compliance)
  - Safety evaluation gaps (community safety claims vs. independent verification)
  - Backdoor risk (poisoned weights in community uploads)
  - Maintenance risk (abandoned models, no security patches)
- **Community model governance** (Hugging Face, etc.):
  - Additional evaluation requirements vs. commercial APIs
  - Verification checklist before deploying community models
  - Ongoing vulnerability monitoring sources
- **Dependency management**:
  - ML framework versions (PyTorch, TensorFlow, vLLM CVEs)
  - Inference library scanning
  - Container image provenance
  - SBOM requirements
- **AI Bill of Materials (AI-BOM)** — what an AI supply chain manifest includes:
  - Model identity and version
  - Training data summary
  - Known limitations and safety evaluations
  - Dependencies (inference frameworks, libraries)
  - Licensing terms
- **Decision framework** (table: Factor / Open-Source Advantage / Commercial API Advantage):
  - Cost, control, compliance, capability, support, security patching

- [ ] **Step 2: Commit**

```bash
git add framework/ai-security/supply-chain-security.md
git commit -m "Add AI supply chain security standards"
```

---

### Task 4: Governance Metrics & KPIs

**Files:**
- Create: `framework/operating-model/governance-metrics.md`

- [ ] **Step 1: Create governance metrics file**

Structure:
- Overview: measuring governance program effectiveness. What gets measured gets managed.
- **Governance health KPIs** (table: Metric / Definition / Target / Cadence / Owner):
  - % of AI systems with current risk assessment (target: 100% T1/T2, 95% T3/T4)
  - Mean time from development to production (trend, not absolute target)
  - % deployment gates passed on first attempt
  - Audit finding closure rate within SLA
  - % of systems with up-to-date model cards
  - Overdue review count (by tier)
- **Responsible AI KPIs** (table: Metric / Definition / Target / Cadence):
  - Bias incident count (quarter-over-quarter)
  - Fairness metric compliance rate across portfolio
  - Hallucination rate by system (T1/T2 systems tracked individually)
  - Human override rate (trend analysis — too high or too low both signals)
  - Transparency disclosure compliance rate
- **Portfolio KPIs** (table: Metric / Definition / Target):
  - Total AI systems by tier (T1/T2/T3/T4 distribution)
  - AI spend by tier and business unit
  - Vendor concentration (% on single provider)
  - Risk concentration heatmap inputs
- **Operational KPIs** (table: Metric / Definition / Alert Threshold):
  - System availability by tier
  - Incident count by severity (trending)
  - Mean time to detect / mean time to resolve
  - Cost per transaction trending
- **Measurement cadence** table mapping each KPI category to reporting frequency and audience
- **Anti-patterns** — what NOT to measure (vanity metrics, gaming-prone metrics)

- [ ] **Step 2: Commit**

```bash
git add framework/operating-model/governance-metrics.md
git commit -m "Add governance metrics and KPI framework"
```

---

### Task 5: Cost Governance

**Files:**
- Create: `framework/operating-model/cost-governance.md`

- [ ] **Step 1: Create cost governance file**

Structure:
- Overview: AI cost governance ensures spend is intentional, attributed, and proportional to value
- **Cost categories** (table: Category / Description / Examples):
  - Inference costs (API tokens, self-hosted GPU compute)
  - Fine-tuning costs (training compute, data preparation)
  - Infrastructure (vector DBs, monitoring, logging storage)
  - Human costs (review, evaluation, red-teaming labor)
  - Vendor costs (licensing, support tiers)
- **Budgeting model** (table: Tier / Budget Approval / Review Frequency):
  - T1: CTO/CFO approval, monthly review
  - T2: VP approval, quarterly review
  - T3: Team lead approval, semi-annual review
  - T4: Self-service within department budget
- **Cost attribution**:
  - Per-system tracking (tag every API call to system ID)
  - Per-BU allocation (chargeback or showback)
  - Shared infrastructure allocation methodology
- **Threshold alerts and escalation** (table: Threshold / Action):
  - 80% of budget → alert to system owner
  - 100% of budget → alert to budget approver + auto-throttle consideration
  - 120% of budget → escalation to VP/CTO
  - Anomaly (>3σ daily spend) → immediate investigation
- **Cost optimization governance**:
  - When cost reduction is acceptable (prompt optimization, model downsizing, caching)
  - When cost reduction is NOT acceptable (reducing eval coverage, removing guardrails, eliminating human review for T1)
  - Change governance for cost optimization: same deployment gate process

- [ ] **Step 2: Commit**

```bash
git add framework/operating-model/cost-governance.md
git commit -m "Add AI cost governance framework"
```

---

### Task 6: GRC Integration

**Files:**
- Create: `framework/operating-model/grc-integration.md`

- [ ] **Step 1: Create GRC integration file**

Structure:
- Overview: how AI governance plugs into existing enterprise governance, risk, and compliance functions
- **COSO ERM mapping** (table: COSO Component / AI Governance Implementation / Framework Reference):
  - Governance & Culture → AI risk appetite, roles, training
  - Strategy & Objective Setting → AI strategy alignment, use case assessment
  - Performance → monitoring, metrics, KPIs
  - Review & Revision → review cadence, model lifecycle
  - Information, Communication & Reporting → board reporting, escalation
- **ISO 31000 mapping** (table: Process Step / AI Governance Implementation):
  - Scope, context, criteria → risk classification
  - Risk identification → risk assessment template
  - Risk analysis → tier determination, impact assessment
  - Risk evaluation → governance intensity
  - Risk treatment → lifecycle controls, deployment gates
  - Monitoring and review → production monitoring, review cadence
  - Communication and consultation → escalation, board reporting
- **Three lines of defense** (table: Line / AI Governance Role / Activities):
  - 1st line (AI teams): build, test, monitor AI systems per standards
  - 2nd line (AI Risk, Compliance): independent risk assessment, policy, challenge
  - 3rd line (Internal Audit): independent assurance, framework effectiveness
- **Control embedding**:
  - How AI controls map to existing enterprise control libraries
  - Integration with GRC platforms (ServiceNow, Archer, etc.)
  - Evidence collection for AI controls
- **Audit integration**:
  - AI audit universe — which AI systems are in scope
  - AI-specific audit procedures
  - Coordinating AI audit with IT audit and operational audit

- [ ] **Step 2: Commit**

```bash
git add framework/operating-model/grc-integration.md
git commit -m "Add GRC integration patterns for AI governance"
```

---

### Task 7: Regulatory Change Monitoring

**Files:**
- Create: `framework/compliance/regulatory-change-monitoring.md`

- [ ] **Step 1: Create regulatory change monitoring file**

Structure:
- Overview: AI regulation is evolving rapidly. A structured process to detect, assess, and respond to regulatory changes.
- **Horizon scanning process** (table: Activity / Frequency / Responsibility):
  - Monitor regulatory body publications (weekly)
  - Track industry body guidance (monthly)
  - Review peer institution approaches (quarterly)
  - Attend regulatory consultations (as published)
- **Sources to monitor** (table: Jurisdiction / Key Sources):
  - EU: AI Office, EDPB, EBA, ESMA, EIOPA
  - US: NIST, Fed/OCC (SR letters), SEC, FTC, state legislatures
  - Singapore: MAS, PDPC, IMDA
  - UK: FCA, PRA, ICO, DSIT
  - Global: OECD, FSB, BIS
- **Impact assessment protocol** when new regulation emerges:
  1. Identification — what changed, which jurisdiction, effective date
  2. Applicability — does it apply to our AI systems? Which tiers?
  3. Gap analysis — what controls do we already have? What's missing?
  4. Action plan — what needs to change, by when, who owns it
  5. Implementation — update framework, controls, templates as needed
  6. Communication — notify affected teams, update training
- **Integration with review cadence**: regulatory change is a standing agenda item at quarterly AI Risk Committee
- **Regulatory change log template** (table: Date / Regulation / Jurisdiction / Impact / Action Required / Owner / Status)

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/regulatory-change-monitoring.md
git commit -m "Add regulatory change monitoring process"
```

---

### Task 8: Open-Source Model Governance

**Files:**
- Create: `framework/llm-lifecycle/open-source-model-governance.md`

- [ ] **Step 1: Create open-source model governance file**

Structure:
- Overview: open-weight and community models offer control and cost advantages but introduce risks that commercial API providers absorb
- **Evaluation requirements before deployment** (table: Evaluation Area / Requirement / Tier Applicability):
  - Safety benchmarks (run standard safety evals: ToxiGen, BBQ, TruthfulQA or equivalent)
  - Capability assessment (domain-specific eval suite — same as commercial model assessment)
  - Comparison against commercial alternatives (performance, safety, cost)
  - Infrastructure readiness (can you host it? GPU requirements, latency, scaling)
- **Licensing risk matrix** (table: License / Commercial Use / Derivative Works / Restrictions / Risk Level):
  - Apache 2.0 — permissive, low risk
  - MIT — permissive, low risk
  - Llama Community License — commercial use with restrictions, medium risk
  - Other community licenses — case-by-case legal review required
- **Training data risk**:
  - Copyright exposure — is the model subject to pending litigation?
  - Opt-out compliance — does the provider honor data subject opt-outs?
  - Data provenance gaps — is training data composition disclosed?
  - PII in training data — has the provider audited for PII?
- **Ongoing maintenance responsibilities** (table: Activity / Frequency / Owner):
  - CVE monitoring (model, inference framework, dependencies)
  - Community health assessment (is the project actively maintained?)
  - Security patch application
  - Re-evaluation on major version releases
- **Fine-tuning governance**: cross-references `fine-tuning-governance.md` with additions:
  - Open-source base model fine-tuning requires same governance as commercial
  - Additional: training data licensing must be compatible with base model license
  - Weight distribution: if you distribute fine-tuned weights, additional obligations may apply
- **Decision framework** (table: Factor / Open-Source / Commercial API / When to Choose):
  - Cost (lower at scale vs. lower to start)
  - Control (full vs. limited)
  - Compliance (full data residency vs. vendor DPA)
  - Capability (varies vs. frontier performance)
  - Support (community vs. vendor SLA)
  - Security (self-managed vs. vendor-managed)

- [ ] **Step 2: Commit**

```bash
git add framework/llm-lifecycle/open-source-model-governance.md
git commit -m "Add open-source model governance standards"
```

---

### Task 9: Multimodal Governance

**Files:**
- Create: `framework/llm-lifecycle/multimodal-governance.md`

- [ ] **Step 1: Create multimodal governance file**

Structure:
- Overview: governance standards for AI systems that process or generate non-text content — images, audio, video, or mixed modalities
- **Input governance** (table: Modality / Risk / Required Control / Tier):
  - Image inputs: content moderation (CSAM, violence, explicit), PII in images (faces, documents), consent for biometric processing
  - Audio inputs: speaker consent, recording disclosure, accent/dialect bias assessment
  - Video inputs: surveillance classification, consent, temporal integrity
  - All modalities: data classification of non-text content, residency compliance for biometric data (GDPR Article 9)
- **Output governance** (table: Output Type / Requirement / Standard):
  - Synthetic image labeling: C2PA/Content Credentials metadata, visible watermarking for external distribution
  - Synthetic audio: disclosure of AI generation, watermarking
  - Synthetic video: mandatory disclosure per EU AI Act Article 50
  - All synthetic content: machine-readable provenance metadata
- **Evaluation standards** (table: Modality / Evaluation Type / Minimum Suite Size by Tier):
  - Vision: object recognition accuracy, bias across demographics, safety (harmful content detection), hallucination (misidentified objects/text)
  - Audio: transcription accuracy across accents/languages, speaker diarization accuracy, safety
  - Video: temporal consistency, action recognition accuracy, safety
  - Cross-modal: consistency between text description and visual/audio output
- **Responsible AI for multimodal**:
  - Fairness in image recognition (demographic performance parity)
  - Representation bias in generated imagery (diversity of generated outputs)
  - Voice bias (recognition accuracy across accents, genders, ages)
  - Accessibility considerations (alt-text generation quality, audio descriptions)
- **Monitoring** (table: Metric / Description / Cadence):
  - Output type distribution (track modality mix over time)
  - Content safety classifier metrics per modality
  - Modality-specific drift indicators
  - Cross-modal consistency scores

- [ ] **Step 2: Commit**

```bash
git add framework/llm-lifecycle/multimodal-governance.md
git commit -m "Add multimodal AI governance standards"
```

---

### Task 10: Model Deprecation Governance

**Files:**
- Create: `framework/llm-lifecycle/model-deprecation-governance.md`

- [ ] **Step 1: Create model deprecation governance file**

Structure:
- Overview: when vendors sunset model versions or organizations retire their own models, structured governance ensures continuity and compliance
- **Deprecation triggers** (table: Trigger / Source / Typical Timeline):
  - Vendor deprecation announcement (OpenAI, Anthropic, Google version retirements) — typically 3–12 months notice
  - End of community support (open-source model no longer maintained)
  - Internal decision (model replaced by newer version)
  - Regulatory requirement (model no longer meets compliance standards)
  - Performance degradation below thresholds
- **Impact assessment protocol**:
  1. Identify all systems using the deprecated model
  2. Classify by tier — T1/T2 systems get priority migration
  3. Assess downstream impacts (integrations, workflows, dependent systems)
  4. Evaluate compliance implications (does the new model require re-assessment?)
  5. Estimate migration effort and timeline
- **Migration governance** (table: Activity / Requirement / Tier Applicability):
  - Replacement model evaluation (same rigor as initial model selection)
  - Prompt compatibility testing (prompts may behave differently on new model)
  - Evaluation suite execution (compare new model vs. deprecated on domain tasks)
  - Parallel running period (both models active; compare outputs)
  - Cutover gates (same as deployment gates — `deployment-gates.md`)
  - Rollback plan (ability to revert to deprecated model if issues arise)
- **Communication and stakeholder management**:
  - Notification to system owners within 5 business days of deprecation announcement
  - Migration timeline published within 10 business days
  - Status reporting at each review cadence meeting
- **Archival requirements**:
  - Preserve model behavior evidence (evaluation results, sample outputs) for audit
  - Retain model card and risk assessment for deprecated model per retention policy
  - Document migration decision rationale

- [ ] **Step 2: Commit**

```bash
git add framework/llm-lifecycle/model-deprecation-governance.md
git commit -m "Add model deprecation and sunsetting governance"
```

---

## Phase 2: Files with dependencies on Phase 1

### Task 11: Red-Teaming Protocol

**Files:**
- Create: `framework/ai-security/red-teaming-protocol.md`

**Dependencies:** References `adversarial-robustness.md` (Task 2)

- [ ] **Step 1: Create red-teaming protocol file**

Structure:
- Overview: structured adversarial testing methodology for AI systems. Red-teaming is not optional for T1/T2.
- **Scope definition** (table: Test Category / Description / Applicable Systems):
  - Prompt injection (direct and indirect)
  - Jailbreaking (safety bypass attempts)
  - Information extraction (PII, training data, system prompt leakage)
  - Harmful content generation (toxicity, bias elicitation)
  - Tool misuse (agentic systems — unauthorized actions via adversarial prompts)
  - Social engineering (manipulating the model into inappropriate disclosures)
- **Tiered testing depth** (table: Tier / Pre-Deployment / Ongoing / Methodology):
  - T1: full adversarial red-team (internal + external if available), 200+ test cases, quarterly retesting
  - T2: internal red-team, 100+ test cases, semi-annual retesting
  - T3: automated adversarial scanning + 50 manual test cases, annual retesting
  - T4: automated scanning only, annual
  - All tiers: ad-hoc retesting on model provider updates
- **Attack taxonomy** — categorized test scenarios:
  - Direct prompt injection (20+ patterns: role-play, authority, encoding, multi-language, token smuggling)
  - Indirect injection via context (RAG poisoning, tool output manipulation)
  - Multi-turn escalation (gradual boundary pushing across conversation turns)
  - Payload smuggling (hiding instructions in base64, Unicode, markdown, HTML)
  - Social engineering (building rapport, authority claims, urgency)
- **Testing protocol**:
  1. Pre-engagement: define scope, success criteria, rules of engagement
  2. Reconnaissance: understand system architecture, tools, guardrails
  3. Test execution: systematic testing against taxonomy categories
  4. Severity classification (table: Severity / Definition / Example):
     - Critical: complete safety bypass, data exfiltration, unauthorized action execution
     - High: partial safety bypass, PII leakage, significant behavior deviation
     - Medium: minor safety gap, information disclosure, degraded guardrail
     - Low: theoretical vulnerability, cosmetic issue
  5. Documentation: findings, reproduction steps, evidence, remediation recommendations
- **Frequency and integration**:
  - Pre-deployment: mandatory for all tiers (depth varies)
  - Integration with deployment gates: red-team sign-off required for T1/T2 (`deployment-gates.md`)
  - Retesting: after any model change, prompt update, or guardrail modification
- Cross-reference: defenses detailed in `adversarial-robustness.md`

- [ ] **Step 2: Commit**

```bash
git add framework/ai-security/red-teaming-protocol.md
git commit -m "Add red-teaming protocol for AI security testing"
```

---

### Task 12: Multi-Agent Governance

**Files:**
- Create: `framework/llm-lifecycle/multi-agent-governance.md`

**Dependencies:** References `agentic-ai-risk.md`

- [ ] **Step 1: Create multi-agent governance file**

Structure:
- Overview: governance standards for systems where multiple AI agents collaborate, coordinate, or are orchestrated to complete tasks. Extends single-agent governance in `agentic-ai-risk.md`.
- **Architecture patterns** (table: Pattern / Description / Governance Complexity / Example):
  - Orchestrator-worker: single orchestrator dispatches tasks to specialized agents → clear accountability, moderate complexity
  - Peer-to-peer: agents negotiate and coordinate directly → high complexity, accountability diffuse
  - Hierarchical: multi-level orchestration (agent spawns sub-agents) → cascading risk, needs depth limits
  - Pipeline: sequential agents where output of A becomes input of B → data integrity across boundaries
- **Governance requirements per pattern** (table: Requirement / Orchestrator-Worker / Peer-to-Peer / Hierarchical / Pipeline):
  - Accountability assignment, communication logging, privilege boundaries, failure isolation
- **Inter-agent communication governance**:
  - Message validation: all inter-agent messages logged and validated against schema
  - Privilege boundaries: no agent can escalate another agent's permissions
  - Information flow controls: classify data at each boundary; prevent unintended information propagation
  - No credential sharing: agents use separate service accounts
- **State management**:
  - Persistent memory governance: what can be stored, TTL, who can read/write
  - Context window management: context pruning strategies, safety instruction preservation
  - Session isolation: define session boundaries; prevent cross-session contamination
  - Shared state: mutable shared state requires validation gates between agents
- **Cascading failure governance**:
  - Blast radius analysis: maximum number of downstream agents affected by single failure
  - Circuit breakers: per-agent and system-wide circuit breakers
  - Graceful degradation: define degraded operation modes when agents fail
  - Depth limits: maximum nesting depth for hierarchical patterns
  - Rate limiting: aggregate action rate across all agents in a system
- **Accountability chain**:
  - Each output must trace to a responsible agent
  - Audit trail must span agent boundaries (correlating IDs across agents)
  - Clear ownership: every multi-agent system has a single human accountable owner
- **Human oversight patterns for multi-agent systems**:
  - Approval gates for irreversible actions (regardless of which agent initiates)
  - Visibility into inter-agent reasoning (not just final output)
  - Kill switch that halts all agents in the system
  - Mandatory human checkpoints at configurable intervals

- [ ] **Step 2: Commit**

```bash
git add framework/llm-lifecycle/multi-agent-governance.md
git commit -m "Add multi-agent system governance standards"
```

---

### Task 13: Board Reporting

**Files:**
- Create: `framework/operating-model/board-reporting.md`

**Dependencies:** References `governance-metrics.md` (Task 4)

- [ ] **Step 1: Create board reporting file**

Structure:
- Overview: board and executive reporting on AI risk ensures informed oversight without operational overload
- **Quarterly AI risk report structure** (each section 2-3 sentences describing content):
  1. Portfolio overview: AI systems by tier, new deployments since last report, retirements
  2. Risk concentration: vendor dependency, geographic concentration, tier distribution
  3. Material incidents: S1/S2 incidents with impact, root cause, remediation status
  4. Governance health: key metrics from `governance-metrics.md` (% compliant, overdue reviews, audit findings)
  5. Responsible AI: bias incidents, fairness metric trending, transparency compliance
  6. Regulatory horizon: upcoming regulatory changes, compliance readiness status
  7. Budget: AI spend vs. budget by BU, cost trending, material variances
  8. Recommendations: actions requiring board decision or awareness
- **Material incident criteria** — when the board must be notified (table: Criterion / Threshold / Notification Timeline):
  - Customer impact: >100 affected customers or any financial harm → 24 hours
  - Financial impact: >$100K direct cost → 24 hours
  - Regulatory exposure: any regulatory notification triggered → 24 hours
  - Reputational risk: media coverage or social media escalation → immediately
  - Data breach: any PII breach involving AI systems → per breach notification policy
  - Systemic failure: T1 system unavailable >4 hours → 24 hours
- **AI risk appetite statement**:
  - What a risk appetite statement for AI should cover
  - Template: qualitative statements (we accept / we do not accept) + quantitative thresholds
  - Annual review and board approval
- **Executive dashboard dimensions** (table: Dimension / Visualization / Cadence):
  - System count by tier (stacked bar, quarterly)
  - Compliance status (RAG heatmap, quarterly)
  - Incident trending (line chart, quarterly)
  - Cost trending (line chart, monthly)
  - Vendor concentration (pie chart, quarterly)
- Cross-reference: detailed metrics defined in `governance-metrics.md`

- [ ] **Step 2: Commit**

```bash
git add framework/operating-model/board-reporting.md
git commit -m "Add board-level AI risk reporting standards"
```

---

### Task 14: Incident Forensics

**Files:**
- Create: `framework/operating-model/incident-forensics.md`

**Dependencies:** References `audit-trail-requirements.md`

- [ ] **Step 1: Create incident forensics file**

Structure:
- Overview: when an AI incident occurs, structured forensics enables root cause analysis, regulatory evidence, and systemic improvement
- **Evidence preservation protocol** (table: Evidence Type / Collection Method / Retention):
  - Prompt/response logs (extract from audit trail within 1 hour of incident)
  - Model version and configuration at time of incident
  - Guardrail configuration and filter logs
  - RAG retrieval results (documents retrieved, relevance scores)
  - System metrics at time of incident (latency, error rates, token usage)
  - User session context (sanitized, PII-redacted where possible)
- **LLM-specific forensics**:
  - Prompt/response chain reconstruction: rebuild the full conversation leading to the incident
  - Context window analysis: what was in the model's context at the time? Was safety instruction displaced?
  - Model version identification: which exact model version produced the output? (vendor changelog correlation)
  - Guardrail replay: replay the incident input through current guardrails — did they catch it? If not, why?
  - Evaluation suite regression: run the incident scenario through the eval suite — was it a known gap?
- **Multi-agent incident tracing**:
  - Correlation ID tracking across agent boundaries
  - Causation chain reconstruction: which agent's output caused the downstream failure?
  - State examination: what was each agent's state/memory at the time?
  - Tool call audit: every tool call in the chain with parameters and results
- **Post-mortem process**:
  1. Incident commander initiates post-mortem within 48 hours of resolution (S1/S2)
  2. Blameless review — focus on systemic causes, not individual errors
  3. Timeline reconstruction from evidence
  4. Root cause analysis (5 whys or equivalent)
  5. Systemic improvements identified and tracked
  6. Control gap assessment — what governance control should have prevented this?
  7. Update to incident playbook, monitoring, or guardrails as needed
  8. Sign-off by AI Risk Lead and system owner
- **Evidence retention**: aligned with `audit-trail-requirements.md` — incident evidence follows the system's tier-based retention (7 years T1, 5 years T2, etc.)

- [ ] **Step 2: Commit**

```bash
git add framework/operating-model/incident-forensics.md
git commit -m "Add AI incident forensics protocol"
```

---

### Task 15: NIST AI RMF Mapping

**Files:**
- Create: `framework/compliance/nist-ai-rmf-mapping.md`

**Dependencies:** Maps to all framework sections

- [ ] **Step 1: Create NIST AI RMF mapping file**

Structure (this file may exceed 180 lines due to mapping completeness):
- Overview: mapping framework controls to NIST AI Risk Management Framework (AI 100-1, January 2023). Covers all 4 functions at category level with key subcategory callouts.
- **Framework alignment** (table: NIST Function / Framework Equivalent / Key References):
  - Govern → operating-model/ (roles, review cadence, escalation, board reporting)
  - Map → risk-classification/ (risk matrix, assessment template, tier determination)
  - Measure → model-lifecycle/ + llm-lifecycle/ (validation, evaluation, monitoring)
  - Manage → compliance/ + operating-model/ (incident response, escalation, audit trail)
- **Govern function mapping** (table: NIST Category / NIST Description / Framework Control / Reference):
  - GV.1 (Policies) → risk classification, lifecycle standards, responsible AI standards
  - GV.2 (Accountability) → RACI, roles-responsibilities, roles-genai
  - GV.3 (Workforce) → training awareness (note: gap — recommend adding training program)
  - GV.4 (Organizational context) → risk appetite, board reporting
  - GV.5 (Processes) → review cadence, deployment gates
  - GV.6 (Stakeholder engagement) → escalation paths, board reporting
- **Map function mapping** (table: same format):
  - MP.1 (Context) → risk-classification, genai-risk-matrix, multimodal-risk-matrix
  - MP.2 (Categorization) → tier determination (T1–T4)
  - MP.3 (Stakeholders) → impact assessment template
  - MP.4 (Risks) → risk assessment template, agentic-ai-risk
  - MP.5 (Impacts) → impact assessment template, escalation criteria
- **Measure function mapping** (table: same format):
  - MS.1 (Test/evaluation) → validation, eval suites, red-teaming
  - MS.2 (Metrics) → governance-metrics, monitoring
  - MS.3 (Monitoring) → production monitoring, drift detection
  - MS.4 (Feedback) → review cadence, user feedback monitoring
- **Manage function mapping** (table: same format):
  - MG.1 (Risk treatment) → deployment gates, lifecycle controls
  - MG.2 (Incident response) → escalation paths, incident report templates, incident forensics
  - MG.3 (Risk communication) → board reporting, escalation communication templates
  - MG.4 (Documentation) → model cards, audit trail, technical documentation
- **NIST AI RMF Profiles alignment**: how framework tiers (T1–T4) map to NIST profile concept
- **Gaps and recommendations**: areas where framework could be further strengthened for NIST alignment (note the workforce/training gap)

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/nist-ai-rmf-mapping.md
git commit -m "Add NIST AI RMF mapping"
```

---

### Task 16: ISO 42001 Mapping

**Files:**
- Create: `framework/compliance/iso-42001-mapping.md`

**Dependencies:** Maps to all framework sections

- [ ] **Step 1: Create ISO 42001 mapping file**

Structure:
- Overview: mapping to ISO/IEC 42001:2024 — AI Management System. Designed so organizations pursuing ISO 42001 certification can use this framework as their implementation backbone.
- **Clause mapping** (table: ISO 42001 Clause / Requirement Summary / Framework Implementation / Reference):
  - Clause 4 (Context of the organization) → risk classification matrices, regulatory alignment, stakeholder analysis via impact assessment
  - Clause 5 (Leadership) → board reporting, AI risk appetite, roles-responsibilities, RACI
  - Clause 6 (Planning) → risk assessment template, risk matrices, lifecycle standards, deployment gates
  - Clause 7 (Support) → training/competence (gap noted — recommend adding), documentation via model cards and audit trails, communication via escalation paths
  - Clause 8 (Operation) → model-lifecycle/, llm-lifecycle/ (development through monitoring), deployment gates, prompt governance
  - Clause 9 (Performance evaluation) → governance-metrics, production monitoring, review cadence, internal audit (via grc-integration)
  - Clause 10 (Improvement) → incident response templates, incident forensics, post-mortem process, review cadence for continuous improvement
- **Annex A controls mapping** (table: Control / Description / Framework Implementation):
  - Map key Annex A controls to specific framework files
  - Note: ISO 42001 Annex A has 38 controls — map the most relevant to regulated industries
- **Certification readiness checklist**:
  - For each clause: what evidence this framework provides, what additional evidence the organization needs to produce
  - Gap summary: what the framework covers vs. what requires organization-specific implementation
- **Integration with ISO 27001**: note overlaps for organizations already ISO 27001 certified

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/iso-42001-mapping.md
git commit -m "Add ISO/IEC 42001 AI management system mapping"
```

---

### Task 17: Cross-Border Data Governance

**Files:**
- Create: `framework/compliance/cross-border-data-governance.md`

**Dependencies:** Complements existing `data-residency-llm.md`

- [ ] **Step 1: Create cross-border data governance file**

This file is the broader complement to `data-residency-llm.md` (which focuses on LLM-specific data flows and EU/US). This covers all AI system types across 8 jurisdictions.

Structure:
- Overview: governance for AI data flows crossing jurisdictional boundaries. Complements `data-residency-llm.md` which covers LLM-specific architecture patterns.
- **Multi-jurisdictional data flow mapping** (beyond LLM architectures):
  - Traditional ML: training data, feature stores, model artifacts, prediction logs
  - GenAI: covered in detail in `data-residency-llm.md` — reference, not duplicate
  - Fine-tuning: training data from multiple jurisdictions
  - Evaluation: test datasets containing cross-border PII
- **Sovereignty requirements** (table: Jurisdiction / Key Requirement / AI-Specific Impact / Enforcement):
  - EU (GDPR + AI Act): data processing in EEA or with adequacy/SCCs; AI Act transparency obligations
  - US: sector-specific (HIPAA, GLBA, state privacy laws); no federal AI data residency (yet)
  - Singapore: PDPA; MAS guidelines on cloud and data; relatively flexible
  - UAE: DIFC/ADGM data protection; onshore processing requirements for certain sectors
  - Brazil: LGPD; data localization requirements for government data
  - Canada: PIPEDA + provincial laws; AIDA (proposed)
  - Australia: Privacy Act; voluntary AI principles; sector-specific (APRA for financial services)
  - Japan: APPI; adequacy decision with EU
- **Conflict resolution patterns** (table: Conflict / Jurisdictions / Resolution Approach):
  - GDPR right-to-delete vs. regulatory retention (EU vs. financial regulators) → canonical treatment: retain with access restriction, delete from active processing, document legal basis for retention
  - Data localization vs. cloud-first strategy → assess by data classification; self-hosted for restricted data, cloud for non-sensitive
  - Consent requirements divergence → apply strictest applicable standard
  - AI-specific transparency vs. trade secrets → disclose methodology without revealing proprietary architecture
- **Transfer mechanisms for AI data** (table: Mechanism / Applicability / Limitations):
  - Standard Contractual Clauses (SCCs): most common for EU transfers
  - Adequacy decisions: Japan, UK, South Korea, etc.
  - Binding Corporate Rules: for intra-group transfers
  - Specific derogations: explicit consent, contractual necessity
  - Note: transfer mechanisms apply to training data, prompts containing PII, and prediction/output logs
- **Cloud provider selection criteria** (table: Criterion / Requirement):
  - Regional availability in required jurisdictions
  - Data residency guarantees (contractual, not just technical)
  - Encryption and key management (customer-managed keys for T1)
  - Sub-processor transparency
  - Compliance certifications per jurisdiction

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/cross-border-data-governance.md
git commit -m "Add cross-border AI data governance standards"
```

---

### Task 18: Multi-Jurisdictional Guide

**Files:**
- Create: `framework/compliance/multi-jurisdictional-guide.md`

**Dependencies:** References `cross-border-data-governance.md` (Task 17)

- [ ] **Step 1: Create multi-jurisdictional guide**

This file may exceed 180 lines due to 8 jurisdictions.

Structure:
- Overview: practical guide for organizations operating AI systems across multiple regulatory jurisdictions
- **Per jurisdiction section** (for each: EU, US, Singapore, UAE, Brazil, Canada, Australia, Japan):
  - Key AI regulation/guidance (name, status, enforcement timeline)
  - Core requirements relevant to enterprise AI
  - How this framework satisfies those requirements (specific file references)
  - Gaps: what additional controls or documentation are needed locally
  - Sector-specific overlay (financial services focus)
- **Decision matrix** (table: "If you operate in..." / Additional Requirements Beyond Base Framework):
  - EU only → base framework is sufficient
  - EU + US → add NIST AI RMF mapping, state privacy law compliance
  - EU + Singapore → add MAS FEAT alignment, PDPA compliance
  - EU + UAE → add ADGM/DIFC requirements, onshore processing for certain data
  - Global (4+ jurisdictions) → implement regulatory change monitoring, appoint jurisdictional compliance leads, use cross-border data governance
- **Conflict resolution**: cross-reference to `cross-border-data-governance.md` for data-specific conflicts; this file covers broader regulatory conflicts:
  - Different risk classification approaches across jurisdictions
  - Varying transparency requirements
  - Divergent incident reporting timelines
  - Resolution principle: apply the strictest requirement unless it creates a conflict with another jurisdiction's mandatory rule
- **Regulatory engagement**: when and how to engage with regulators in each jurisdiction about AI systems

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/multi-jurisdictional-guide.md
git commit -m "Add multi-jurisdictional AI governance guide"
```

---

## Phase 3: Updates to Existing Files

### Task 19: Update Agentic AI Risk

**Files:**
- Modify: `framework/risk-classification/agentic-ai-risk.md`

- [ ] **Step 1: Add multi-agent and advanced agentic risk dimensions**

Add new sections at the end of the file (after line 99, before the `---` separator at line 101):

**### 6. Multi-Agent Coordination Risk**

Content:
- Risk: multiple agents interacting create emergent behaviors not present in individual agent testing
- Contributing factors: inter-agent communication manipulation, privilege accumulation across agents, information leakage between agent contexts, emergent goal misalignment
- Example: Agent A (research) passes data to Agent B (writing) which passes to Agent C (publishing) — adversarial content in research data propagates through entire chain without individual agent detecting it
- Controls: message validation at each boundary, aggregate privilege limits, cross-agent monitoring, system-wide circuit breakers
- Cross-reference: detailed governance in `../llm-lifecycle/multi-agent-governance.md`

**### 7. Persistent Memory and Long-Term State Risk**

Content:
- Risk: agents with long-term memory accumulate context that can be manipulated, become stale, or create privacy obligations
- Contributing factors: memory poisoning over time, unbounded memory growth, stale context influencing current decisions, PII accumulation in memory
- Controls: memory TTL enforcement, periodic memory audit, PII scanning of stored context, memory versioning with rollback
- Cross-reference: state management governance in `../llm-lifecycle/multi-agent-governance.md`

**### 8. Complex Tool Chain Risk**

Content:
- Risk: agents using sequences of tools can create unintended effects through tool composition that individual tool permissions don't anticipate
- Contributing factors: tool A's output enables tool B to take an action neither was individually authorized for, tool composition creating write-then-read patterns that bypass access controls
- Controls: tool composition analysis at deployment, compound action review, tool chain depth limits

- [ ] **Step 2: Commit**

```bash
git add framework/risk-classification/agentic-ai-risk.md
git commit -m "Extend agentic AI risk taxonomy with multi-agent, memory, and tool chain risks"
```

---

### Task 20: Update EU AI Act Mapping

**Files:**
- Modify: `framework/compliance/eu-ai-act-mapping.md`

- [ ] **Step 1: Add enforcement status and evidence requirements**

Add at the end of the file (after line 94, the last line of the Implementation Notes section):

**## Enforcement Status (as of March 2026)**

Table: Obligation / Effective Date / Status / Action Required:
- Prohibited practices (Art. 5) → Feb 2025 → **In force** → Verify no prohibited AI practices
- GPAI obligations (Art. 53-55) → Aug 2025 → **In force** → Verify model provider compliance
- Transparency obligations (Art. 50) → Aug 2025 → **In force** → Ensure AI disclosure implemented
- High-risk system requirements (Art. 6-15) → Aug 2026 → **5 months to compliance** → Finalize conformity assessment for all T1 systems
- Annex I high-risk (regulated products) → Aug 2027 → Coming → Monitor and prepare

**## Compliance Evidence Requirements**

What auditors and regulators want to see (table: Article / Evidence / Framework Source):
- Art. 9 (Risk Management): completed risk assessments, review meeting minutes, remediation tracking → risk assessment templates, review cadence records
- Art. 10 (Data Governance): data quality reports, bias testing results, data lineage documentation → development standards, evaluation records
- Art. 11 (Technical Documentation): model cards, architecture documents, change history → model card templates, audit trail
- Art. 12 (Record-Keeping): audit trail exports, log retention evidence → audit-trail-requirements
- Art. 13 (Transparency): user-facing disclosures, model documentation → transparency standards
- Art. 14 (Human Oversight): oversight procedure documentation, override logs → human-in-loop-patterns
- Art. 15 (Accuracy/Robustness): validation reports, adversarial testing results, security assessments → validation, red-teaming protocol

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/eu-ai-act-mapping.md
git commit -m "Add enforcement status and evidence requirements to EU AI Act mapping"
```

---

### Task 21: Update EU AI Act GenAI Mapping

**Files:**
- Modify: `framework/compliance/eu-ai-act-genai-mapping.md`

- [ ] **Step 1: Add enforcement status and practical compliance notes**

Add at the end of the file (after line 143, the last line of the Action Items subsection):

**## Enforcement Status (as of March 2026)**

Table: Obligation / Status / Practical Impact:
- GPAI obligations (Art. 53) → **In force since Aug 2025** → Your model providers should already be compliant. If they are not providing technical documentation and training data summaries, escalate procurement.
- Systemic risk obligations (Art. 55) → **In force since Aug 2025** → If you use GPT-4, Claude, Gemini Ultra, etc. — verify provider has completed model evaluations and adversarial testing.
- Transparency (Art. 50) → **In force since Aug 2025** → All customer-facing GenAI systems must disclose AI involvement NOW.
- High-risk GenAI (Art. 6-15) → **Aug 2026** → T1 GenAI systems must have full conformity evidence in 5 months.

**## Practical Compliance Evidence**

For deployers of GPAI models — what you need in your files (table: Requirement / Evidence to Maintain):
- Provider technical documentation → file copy of provider's system card / model card
- Copyright compliance → provider's published copyright policy + your assessment
- Training data summary → provider's disclosure + your bias assessment based on it
- Deployment transparency → screenshots/logs of AI disclosure implementation
- Adversarial testing → red-team report from your own testing (not just provider's)
- Incident reporting → incident report template + records of any incidents reported

- [ ] **Step 2: Commit**

```bash
git add framework/compliance/eu-ai-act-genai-mapping.md
git commit -m "Add enforcement status and compliance evidence to GenAI AI Act mapping"
```

---

## Phase 4: Templates and Examples

### Task 22: Board AI Risk Report Template

**Files:**
- Create: `templates/board-ai-risk-report.md`

- [ ] **Step 1: Create board report template**

Follow the same fill-in-ready pattern as `incident-report-genai.md`. Structure:

```
# Quarterly AI Risk Report

## Instructions
Complete this template for quarterly board/risk committee reporting on AI systems.

## 1. Executive Summary
| Field | Value |
| Reporting Period | Q_ 20__ |
| Report Date | |
| Prepared By | |
| Approved By | |

Key highlights (3-5 bullets):
>

## 2. Portfolio Overview
| Metric | Current | Previous Quarter | Change |
| Total AI systems | | | |
| T1 (Critical) | | | |
| T2 (High) | | | |
| T3 (Medium) | | | |
| T4 (Low) | | | |
| New deployments this quarter | | | |
| Systems retired this quarter | | | |

## 3. Risk Concentration
### Vendor Concentration
| Provider | # Systems | % of T1/T2 | Trend |
### Geographic Concentration
| Region | # Systems | Data Residency Compliant | Notes |

## 4. Material Incidents
| Incident ID | Severity | System | Impact | Root Cause | Status | Board Action Required |
(Include S1/S2 only. Reference full incident reports.)

## 5. Governance Health
| KPI | Target | Actual | Status (RAG) |
| Systems with current risk assessment | 100% (T1/T2) | | |
| Overdue reviews | 0 (T1) | | |
| Deployment gates passed first attempt | >80% | | |
| Audit findings open past SLA | 0 | | |

## 6. Responsible AI
| Metric | Value | Trend | Notes |
| Bias incidents | | | |
| Fairness compliance rate | | | |
| Transparency disclosure compliance | | | |

## 7. Regulatory Update
| Regulation | Change | Impact | Action Required | Timeline |

## 8. Budget
| Category | Budget | Actual | Variance | Notes |
| Inference costs | | | | |
| Infrastructure | | | | |
| Human review | | | | |
| Vendor licensing | | | | |
| Total | | | | |

## 9. Recommendations
| # | Recommendation | Rationale | Decision Required |

## 10. Approvals
| Role | Name | Date | Sign-off |
| AI Risk Lead | | | [ ] |
| CTO/CIO | | | [ ] |
| CRO | | | [ ] |
```

- [ ] **Step 2: Commit**

```bash
git add templates/board-ai-risk-report.md
git commit -m "Add quarterly board AI risk report template"
```

---

### Task 23: Red-Team Report Template

**Files:**
- Create: `templates/red-team-report.md`

- [ ] **Step 1: Create red-team report template**

Structure (fill-in-ready, mirrors incident-report-genai.md style):

```
# AI Red-Team Assessment Report

## 1. Engagement Summary
| Field | Value |
| System Under Test | |
| System ID | |
| Risk Tier | T1 / T2 / T3 / T4 |
| Assessment Date | |
| Assessor(s) | |
| Methodology | Internal / External / Automated |
| Test Case Count | |

## 2. Scope
### In Scope
- [ ] Prompt injection (direct)
- [ ] Prompt injection (indirect / via context)
- [ ] Jailbreaking
- [ ] Information extraction
- [ ] Harmful content generation
- [ ] Tool misuse (agentic systems)
- [ ] Social engineering
- [ ] Other: ___

### Out of Scope
>

## 3. Executive Summary
Overall risk rating: Critical / High / Medium / Low
> [2-3 sentence summary of findings]

## 4. Findings Summary
| # | Finding | Severity | Category | Status |
| 1 | | Crit/High/Med/Low | | Open/Remediated |

## 5. Detailed Findings
### Finding N: [Title]
| Field | Value |
| Severity | |
| Category | |
| Attack vector | |
| Reproducibility | Always / Sometimes / Rare |

**Description:**
>

**Steps to reproduce:**
1.
2.
3.

**Evidence:**
> [Sanitized examples. Redact sensitive content.]

**Impact:**
>

**Recommended remediation:**
>

**Remediation priority:** Immediate / Next sprint / Next quarter

## 6. Recommendations
| Priority | Recommendation | Owner | Due Date |

## 7. Retest Requirements
| Finding # | Retest Required | Retest Date | Retest Result |

## 8. Approvals
| Role | Name | Date | Sign-off |
| Red-Team Lead | | | [ ] |
| System Owner | | | [ ] |
| AI Risk Lead | | | [ ] |
```

- [ ] **Step 2: Commit**

```bash
git add templates/red-team-report.md
git commit -m "Add red-team assessment report template"
```

---

### Task 24: Internal Knowledge Search Example (T3)

**Files:**
- Create: `examples/internal-knowledge-search/model-card.yaml`
- Create: `examples/internal-knowledge-search/risk-assessment.md`

- [ ] **Step 1: Create example directory**

```bash
mkdir -p examples/internal-knowledge-search
```

- [ ] **Step 2: Create model card**

Follow exact structure of existing example model cards (e.g., `customer-service-chatbot/model-card.yaml`). Key details:
- Name: "Internal Knowledge Search"
- Model ID: "knowledge-search-v1.0"
- Type: "rag"
- Base model: "Claude 3.5 Haiku" (cost-optimized for internal use)
- Risk Tier: T3
- Intended use: help employees find information across internal knowledge base (HR policies, IT procedures, product documentation)
- NOT customer-facing, NOT making regulated decisions
- Human oversight: human-on-the-loop (users evaluate results themselves)
- Lighter governance: approved vendor list (no architecture review board), prompts in version control (no mandatory peer review), basic input validation, pre-deployment eval + monthly spot checks, weekly metrics review, summary logging with 3-year retention
- RAG configuration: vector store, embedding model, chunking, top-k
- Evaluation: smaller eval suite (50 test cases per T3 requirement), faithfulness, relevance, hallucination rate
- No adversarial red-team (automated scanning only per T3)
- Cost: modest (~$500/month)

- [ ] **Step 3: Create risk assessment**

Follow `agentic-research-assistant/risk-assessment.md` structure but demonstrate LIGHTER governance:
- GenAI risk dimension scoring: all Medium or Low scores
- Aggregate score: 8 (T3 threshold)
- No automatic T1 triggers
- Governance requirements table showing T3 controls (simpler than T1 examples)
- Key message: governance is proportional to risk — T3 systems don't need monthly reviews, board reporting, or full red-teams

- [ ] **Step 4: Commit**

```bash
git add examples/internal-knowledge-search/
git commit -m "Add T3 internal knowledge search worked example"
```

---

## Phase 5: README Update

### Task 25: Update README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update README with all new content**

Changes needed (preserve existing structure, add new entries in correct sections):

**Risk Classification section** — add after Agentic AI Risk:
- `[Multimodal AI Risk Matrix](framework/risk-classification/multimodal-risk-matrix.md)` — risk dimensions for vision, audio, video, and mixed-modality systems

**LLM Lifecycle section** — add after LLM Production Monitoring:
- `[Multimodal Governance](framework/llm-lifecycle/multimodal-governance.md)` — input/output governance for non-text modalities
- `[Multi-Agent Governance](framework/llm-lifecycle/multi-agent-governance.md)` — orchestration, coordination, and accountability for multi-agent systems
- `[Open-Source Model Governance](framework/llm-lifecycle/open-source-model-governance.md)` — evaluation, licensing, and maintenance for open-weight models
- `[Model Deprecation Governance](framework/llm-lifecycle/model-deprecation-governance.md)` — sunsetting, migration, and archival

**Add new section "### AI Security" after LLM Lifecycle:**
```
### AI Security
Standards for securing AI systems against adversarial threats.
- [Red-Teaming Protocol](framework/ai-security/red-teaming-protocol.md) — structured adversarial testing methodology
- [Adversarial Robustness](framework/ai-security/adversarial-robustness.md) — defenses against jailbreaking, prompt injection, model extraction, data poisoning
- [Supply Chain Security](framework/ai-security/supply-chain-security.md) — model provenance, open-source risk, AI bill of materials
```

**Compliance Mapping section** — add:
- `[NIST AI RMF Mapping](framework/compliance/nist-ai-rmf-mapping.md)` — Govern, Map, Measure, Manage function alignment
- `[ISO/IEC 42001 Mapping](framework/compliance/iso-42001-mapping.md)` — AI management system certification backbone
- `[Multi-Jurisdictional Guide](framework/compliance/multi-jurisdictional-guide.md)` — EU, US, Singapore, UAE, Brazil, Canada, Australia, Japan
- `[Cross-Border Data Governance](framework/compliance/cross-border-data-governance.md)` — data flows, sovereignty, conflict resolution
- `[Regulatory Change Monitoring](framework/compliance/regulatory-change-monitoring.md)` — horizon scanning and impact assessment

**Operating Model section** — add:
- `[Board Reporting](framework/operating-model/board-reporting.md)` — quarterly risk report structure, material incident criteria
- `[Governance Metrics & KPIs](framework/operating-model/governance-metrics.md)` — measuring governance program health
- `[Cost Governance](framework/operating-model/cost-governance.md)` — budgeting, attribution, optimization
- `[GRC Integration](framework/operating-model/grc-integration.md)` — COSO, ISO 31000, three lines of defense
- `[Incident Forensics](framework/operating-model/incident-forensics.md)` — post-incident investigation and evidence preservation

**Templates section** — add under GenAI / LLM:
- `[Board AI Risk Report](templates/board-ai-risk-report.md)` — quarterly board reporting template
- `[Red-Team Report](templates/red-team-report.md)` — adversarial testing findings template

**Worked Examples section** — add:
- `[Internal Knowledge Search](examples/internal-knowledge-search/)` — T3 (Medium), internal RAG, lighter governance

**Regulatory Alignment table** — add rows:
| **NIST AI RMF** | Govern, Map, Measure, Manage functions — full category-level mapping |
| **ISO/IEC 42001** | AI management system — clause-by-clause implementation mapping |
| **MAS Model Governance Framework** | Singapore AI governance — model risk, fairness, explainability |
| **LGPD (Brazil)** | Data protection for AI systems — consent, data subject rights |

**Add Changelog section** before License:
```
## Changelog

### March 2026 — Comprehensive Update
- **AI Security:** Added red-teaming protocol, adversarial robustness standards, supply chain security
- **Regulatory breadth:** Added NIST AI RMF mapping, ISO 42001 mapping, multi-jurisdictional guide (8 jurisdictions), regulatory change monitoring, cross-border data governance
- **Frontier AI coverage:** Added multimodal risk matrix and governance, multi-agent governance, open-source model governance, model deprecation governance
- **Enterprise operations:** Added board reporting, governance metrics/KPIs, cost governance, GRC integration, incident forensics
- **Templates:** Added board risk report and red-team report templates
- **Examples:** Added T3 internal knowledge search (lighter governance)
- **Updated:** EU AI Act mappings with enforcement status, agentic AI risk with multi-agent and tool chain dimensions
```

- [ ] **Step 2: Verify all links**

Check that every new link in README points to a file that exists.

```bash
# Quick verification — all linked files should exist
grep -oE '\(framework/[^)]+\)' README.md | tr -d '()' | while read f; do test -f "$f" || echo "MISSING: $f"; done
grep -oE '\(templates/[^)]+\)' README.md | tr -d '()' | while read f; do test -f "$f" || echo "MISSING: $f"; done
grep -oE '\(examples/[^)]+\)' README.md | tr -d '()' | while read f; do test -d "$f" || test -f "$f" || echo "MISSING: $f"; done
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "Update README with all new governance framework content"
```

---

## Summary

| Phase | Tasks | Files | Description |
|-------|-------|-------|-------------|
| 1 | 1–10 | 10 new files | Foundations — no dependencies |
| 2 | 11–18 | 8 new files | Files referencing Phase 1 |
| 3 | 19–21 | 3 existing files updated | Updates to agentic-ai-risk, EU AI Act mappings |
| 4 | 22–24 | 4 new files (2 templates + 2 example) | Templates and worked example |
| 5 | 25 | 1 existing file updated | README update |

**Total: 22 new files + 2 new example files + 4 existing file updates = 28 file operations across 25 tasks**
