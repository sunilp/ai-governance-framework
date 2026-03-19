# AI Governance Framework — Comprehensive Update Design

**Date:** 2026-03-19
**Scope:** Regulatory breadth + AI frontier coverage + Enterprise operationalization
**Approach:** Cohesive revision — add ~24 new files, update ~4 existing files, 1 new directory

---

## Goal

Evolve the AI governance framework from a strong EU/UK-focused, text-LLM-centric governance framework into a globally relevant, frontier-AI-aware, enterprise-operational governance body of work.

Three dimensions:
1. **Regulatory breadth** — NIST AI RMF, ISO 42001, multi-jurisdictional coverage
2. **AI frontier coverage** — multimodal, multi-agent, AI security/red-teaming, open-source models
3. **Enterprise operationalization** — board reporting, metrics/KPIs, cost governance, GRC integration, incident forensics

## Constraints

- Existing directory structure preserved (no renames, no moves)
- One new directory: `framework/ai-security/`
- All existing file URLs remain valid
- Tone and depth consistent with existing files (80–180 lines, practical, opinionated, actionable)
- Mapping files (NIST AI RMF, ISO 42001, multi-jurisdictional guide) may exceed 180 lines where completeness requires it
- Apache 2.0 license
- No versioning ceremony; changelog section in README signals the update

---

## New Files (25)

### Regulatory Breadth (4 new + 2 existing updates)

#### `framework/compliance/nist-ai-rmf-mapping.md`
Maps framework controls to NIST AI RMF four functions:
- **Govern** — organizational governance, risk culture, legal compliance → operating-model section
- **Map** — context, stakeholder identification, risk framing → risk-classification section
- **Measure** — assessment, testing, monitoring → lifecycle and monitoring sections
- **Manage** — prioritize, respond, recover → escalation, incident, review cadence
- Control-by-control mapping table (NIST subcategory → framework file + section)
- Profiles and tiers alignment with framework's T1–T4

#### `framework/compliance/iso-42001-mapping.md`
Maps to ISO/IEC 42001:2024 AI Management System clauses:
- Clause 4 (Context) → risk classification
- Clause 5 (Leadership) → board reporting, roles
- Clause 6 (Planning) → risk assessment, lifecycle standards
- Clause 7 (Support) → training, competence, documentation
- Clause 8 (Operation) → lifecycle, deployment gates
- Clause 9 (Performance evaluation) → monitoring, metrics
- Clause 10 (Improvement) → incident response, review cadence
- Designed so orgs pursuing ISO 42001 certification can use this framework as implementation backbone

#### `framework/compliance/multi-jurisdictional-guide.md`
Per jurisdiction: EU (AI Act), US (NIST + state laws + SEC guidance), Singapore (MAS FEAT + Model Governance Framework), UAE (ADGM), Brazil (LGPD + AI Bill), Canada (AIDA), Australia (voluntary framework), Japan (Social Principles).
- Each entry: key requirements, enforcement timeline, how framework satisfies it, gaps to address locally
- Decision matrix: "If you operate in X + Y, here's what you need beyond the base framework"
- Conflict resolution patterns (e.g., GDPR deletion vs. regulatory retention)

#### `framework/compliance/regulatory-change-monitoring.md`
- Regulatory horizon scanning process
- Sources to monitor per jurisdiction
- Assessment protocol: impact analysis → gap assessment → control update → communication
- Quarterly regulatory review integration with existing review cadence

#### Updates to existing files:
- `eu-ai-act-mapping.md` — enforcement status markers (Aug 2025 in force, Aug 2026 coming)
- `eu-ai-act-genai-mapping.md` — practical compliance evidence requirements

### AI Frontier Coverage (7 new + 1 existing update)

#### `framework/ai-security/red-teaming-protocol.md`
- Scope definition: prompt injection, jailbreaking, information extraction, harmful content, tool misuse
- Tiered testing depth: T1 full adversarial red-team; T3/T4 automated scanning + spot checks
- Attack taxonomy: direct prompt injection, indirect via context, multi-turn escalation, payload smuggling, social engineering
- Testing protocol: pre-engagement scoping, execution, severity classification, findings documentation
- Frequency: pre-deployment mandatory, quarterly T1, semi-annual T2, annual T3/T4, ad-hoc on provider updates
- Integration with deployment gates: red-team sign-off as gate for T1/T2

#### `framework/ai-security/adversarial-robustness.md`
- Jailbreaking defenses: system prompt hardening, input classification, output filtering, layered defense
- Prompt injection mitigation: input/output separation, instruction hierarchy, context isolation for RAG
- Model extraction prevention: rate limiting, output perturbation, API access controls, watermarking
- Data poisoning defenses: training data provenance, RAG corpus integrity, document authentication
- Privacy attacks: membership inference, model inversion, PII extraction — detection and mitigation
- Monitoring: anomaly detection on query patterns, output distribution shifts, cost spikes as attack signals

#### `framework/ai-security/supply-chain-security.md`
- Model provenance: weight verification, training data attestation, model card credibility
- Open-source model risk: licensing, safety evaluation requirements, vulnerability monitoring
- Community model governance: additional evaluation vs. commercial APIs
- Dependency management: ML framework versions, inference library CVEs, container scanning
- SBOM for AI: model identity, training data summary, known limitations, safety evaluations

#### `framework/risk-classification/multimodal-risk-matrix.md`
- Vision risks: deepfake, CSAM detection, bias in image recognition
- Audio risks: voice cloning, consent, speaker identification
- Video risks: temporal manipulation, surveillance
- Cross-modal risks: text-to-image safety, image-to-text hallucination, audio-visual synthesis
- Tier adjustments: synthetic media default minimum T2; deepfake-capable mandatory T1

#### `framework/llm-lifecycle/multimodal-governance.md`
- Input governance: content moderation on image/audio/video, PII in non-text modalities, biometric consent
- Output governance: synthetic media labeling (C2PA), watermarking, disclosure obligations
- Evaluation standards: modality-specific eval suites, cross-modal consistency, safety benchmarks
- Monitoring: output type distribution, content safety classifier metrics, modality-specific drift
- Responsible AI for multimodal: fairness in image recognition, representation bias in generated imagery, voice bias, accessibility — extends the text-focused bias-detection-llm.md to non-text modalities

#### `framework/llm-lifecycle/multi-agent-governance.md`
- Architecture patterns: orchestrator-worker, peer-to-peer, hierarchical — governance per pattern
- Inter-agent communication: message validation, privilege boundaries, information flow controls
- State management: persistent memory governance, context window management, session isolation
- Cascading failure: blast radius analysis, circuit breakers, graceful degradation
- Accountability chain: which agent owns which output; audit trail across boundaries
- Human oversight: where humans insert into multi-agent flows; approval gates for irreversible actions

#### `framework/llm-lifecycle/open-source-model-governance.md`
- Evaluation requirements: safety benchmarks, capability assessment, comparison against commercial
- Licensing risk: compatibility matrix, use restriction analysis, derivative work obligations
- Training data risk: copyright exposure, opt-out compliance, data provenance gaps
- Ongoing maintenance: CVE monitoring, community health, update cadence
- Decision framework: when open-source vs. commercial (cost, control, compliance, capability)

#### `framework/llm-lifecycle/model-deprecation-governance.md`
When vendors or communities sunset model versions:
- Deprecation impact assessment: which systems affected, regulatory re-assessment triggers
- Migration governance: testing requirements, parallel running, cutover gates
- Notification and communication: stakeholder awareness, timeline management
- Archival: preserving model behavior evidence for audit/compliance

#### Update to existing file:
- `agentic-ai-risk.md` — add multi-agent risk dimensions, persistent memory risks, complex tool chains, cross-reference multi-agent-governance.md

### Enterprise Operationalization (8 new)

#### `framework/operating-model/board-reporting.md`
- Quarterly AI risk report structure: portfolio overview, risk concentration, material incidents, regulatory horizon, budget
- Material incident criteria: financial impact thresholds, regulatory exposure, reputational risk
- AI risk appetite statement template
- Executive dashboard dimensions: system count by tier, compliance status, incident trending, cost trending

#### `framework/operating-model/governance-metrics.md`
- Governance health KPIs: % current risk assessments, mean time dev-to-prod, % gates passed first attempt, audit closure rate
- Responsible AI KPIs: bias incident rate, fairness trending, hallucination rate, human override rate
- Portfolio KPIs: AI spend vs. value, risk concentration by vendor/model, system count by tier
- Operational KPIs: uptime, latency, cost per transaction, drift detection latency
- Measurement cadence and ownership per metric

#### `framework/operating-model/cost-governance.md`
- Token/compute budgeting by BU and tier
- Cost attribution: API costs, fine-tuning, inference infrastructure, human review
- Threshold alerts and escalation
- Cost optimization governance: when cost reduction acceptable vs. degrading safety/quality
- Chargeback vs. central funding decision framework

#### `framework/operating-model/grc-integration.md`
- COSO ERM mapping (5 components → framework controls)
- ISO 31000 mapping
- Three lines of defense integration patterns
- Control embedding in enterprise control libraries
- Audit integration: AI alongside traditional IT/operational audit

#### `framework/operating-model/incident-forensics.md`
- Post-incident investigation protocol: evidence preservation, timeline reconstruction, root cause
- LLM-specific forensics: prompt/response chain, context window analysis, model version identification
- Multi-agent incident tracing: causation across agent boundaries
- Post-mortem template: blameless review, systemic improvements, control gaps
- Evidence retention aligned with audit-trail-requirements.md

#### `framework/compliance/cross-border-data-governance.md`
Broader complement to existing `data-residency-llm.md` (which focuses on LLM-specific data flows and EU/US). This file covers:
- Multi-jurisdictional data flow mapping beyond LLM architectures (traditional ML training data, feature stores, model artifacts)
- Sovereignty requirements across 8 jurisdictions (existing file covers EU/US only)
- Conflict resolution patterns (GDPR deletion vs. regulatory retention — canonical treatment here; multi-jurisdictional-guide.md cross-references)
- Transfer mechanisms: SCCs, adequacy decisions, BCRs as applied to AI-specific data categories
- Cloud provider selection criteria for multi-jurisdictional AI deployments

#### `templates/board-ai-risk-report.md`
Quarterly board report template:
- Executive summary
- Portfolio health (systems by tier, compliance status)
- Material incidents
- Regulatory update
- Budget utilization
- Recommendations and decisions required

#### `templates/red-team-report.md`
Red-teaming findings template:
- Engagement scope and methodology
- Vulnerability summary with severity ratings
- Detailed findings (attack vector, impact, evidence)
- Remediation recommendations
- Retest requirements and timeline

### New Example (1)

#### `examples/internal-knowledge-search/`
T3 (Medium) worked example:
- `model-card.yaml` — streamlined model card for RAG-based internal search
- `risk-assessment.md` — lighter risk assessment demonstrating T3 governance
- Shows governance scales down: no board reporting, basic monitoring, streamlined review

### README Update
- Add AI Security section with 3 new files
- Add new compliance mappings (NIST, ISO 42001, multi-jurisdictional, regulatory monitoring, cross-border)
- Add new operating model files (board reporting, metrics, cost, GRC, forensics)
- Add new LLM lifecycle files (multimodal, multi-agent, open-source)
- Add multimodal risk matrix to risk classification
- Add new templates and example
- Expand regulatory alignment table: add NIST AI RMF, ISO 42001, MAS Model Governance Framework, Brazil LGPD
- Add changelog section at bottom

---

## Files Modified (4)

| File | Changes |
|------|---------|
| `framework/compliance/eu-ai-act-mapping.md` | Add enforcement status markers, compliance evidence requirements |
| `framework/compliance/eu-ai-act-genai-mapping.md` | Add enforcement status markers, compliance evidence requirements |
| `framework/risk-classification/agentic-ai-risk.md` | Add multi-agent risk dimensions, persistent memory, tool chains, cross-references |
| `README.md` | New sections, expanded regulatory table, changelog |

---

## Existing Files NOT Modified

All other existing files remain unchanged. Cross-references from new files point to existing files but do not require existing files to be updated (new files reference existing; existing files don't need to know about new files except through README).

---

## Quality Standards

- Each file: 80–180 lines, consistent with existing framework tone
- Practical, opinionated, field-tested language — not academic or theoretical
- Every standard includes: what to do, when, who's responsible, what tier it applies to
- Templates are fill-in-ready, not abstract descriptions
- Examples show real governance artifacts, not placeholder text
- Cross-references use relative markdown links

---

## Success Criteria

1. Framework covers EU, US, Singapore, UAE, Brazil, Canada, Australia, Japan regulatory landscapes
2. NIST AI RMF and ISO 42001 have explicit control mappings
3. Multimodal AI (vision, audio, video) has dedicated risk matrix and lifecycle governance
4. Multi-agent systems have dedicated governance standards
5. AI security has structured red-teaming, adversarial robustness, and supply chain coverage
6. Board can receive quarterly AI risk reports using provided template
7. Governance program health is measurable via defined KPIs
8. T3 example demonstrates governance scales down appropriately
9. All new content matches existing framework quality and tone
10. README provides clear navigation to all new content

---

## Implementation Sequencing

Files have some dependencies. Recommended order:

**Phase 1 — Foundations (no dependencies):**
1. `framework/risk-classification/multimodal-risk-matrix.md`
2. `framework/ai-security/adversarial-robustness.md`
3. `framework/ai-security/supply-chain-security.md`
4. `framework/operating-model/governance-metrics.md`
5. `framework/operating-model/cost-governance.md`
6. `framework/operating-model/grc-integration.md`
7. `framework/compliance/regulatory-change-monitoring.md`
8. `framework/llm-lifecycle/open-source-model-governance.md`
9. `framework/llm-lifecycle/multimodal-governance.md`
10. `framework/llm-lifecycle/model-deprecation-governance.md`

**Phase 2 — Files with dependencies on Phase 1:**
11. `framework/ai-security/red-teaming-protocol.md` (references adversarial-robustness.md)
12. `framework/llm-lifecycle/multi-agent-governance.md` (references agentic-ai-risk.md)
13. `framework/operating-model/board-reporting.md` (references governance-metrics.md)
14. `framework/operating-model/incident-forensics.md` (references audit-trail-requirements.md)
15. `framework/compliance/nist-ai-rmf-mapping.md` (maps to all framework sections)
16. `framework/compliance/iso-42001-mapping.md` (maps to all framework sections)
17. `framework/compliance/cross-border-data-governance.md` (complements data-residency-llm.md)
18. `framework/compliance/multi-jurisdictional-guide.md` (references cross-border-data-governance.md)

**Phase 3 — Updates to existing files:**
19. Update `framework/risk-classification/agentic-ai-risk.md`
20. Update `framework/compliance/eu-ai-act-mapping.md`
21. Update `framework/compliance/eu-ai-act-genai-mapping.md`

**Phase 4 — Templates and examples (reference framework files):**
22. `templates/board-ai-risk-report.md`
23. `templates/red-team-report.md`
24. `examples/internal-knowledge-search/model-card.yaml`
25. `examples/internal-knowledge-search/risk-assessment.md`

**Phase 5 — README update (references everything):**
26. Update `README.md`
