# Risk Assessment: Investment Research Assistant Agent

## System Overview

| Field | Value |
|-------|-------|
| System Name | Investment Research Assistant Agent |
| System ID | research-agent-v0.9 |
| Business Unit | Investment Research |
| Assessment Date | 2026-01-15 |
| Prepared by | Product Owner, Investment Research |
| Risk assessment approved by | AI Risk Committee, 2026-01-25 |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect financial data or analysis in research drafts. Mitigated by mandatory analyst review of all outputs. |
| Data Exposure Risk | **High (3)** | Processes confidential research data and market analysis. No customer PII, but sensitive business data. Vendor API with zero retention. |
| Prompt Injection Susceptibility | **Medium (2)** | Internal users only. However, agent processes retrieved documents which could contain adversarial content. |
| Output Controllability | **Medium (2)** | Agent executes multi-step plans autonomously within a session. Plan approval gate exists but intermediate steps are automated. |
| Third-Party Model Dependency | **High (3)** | Anthropic Claude API; Vertex AI fallback (Gemini 2.5 Pro, recorded as validated in the [model card](model-card.yaml)). No switch to the fallback is recorded, so it is not a tested fallback and counts as degraded. Core workflow depends on LLM capability, and no outage tolerance is recorded. |

**Highest Dimension: High (3)**
**Aggregate Score: 13** (context only; does not set the tier)

### Risk Tier Determination

**Tier: T1 (Critical)**

Override check against the [canonical override list](../../framework/risk-classification/genai-risk-matrix.md#tier-override-rules):
- [ ] 1. Regulated decisions: *No. Research informs investment decisions, but there is no credit, insurance, AML/sanctions or employment decision.*
- [ ] 2. Customer-facing content without per-output review: *No. Internal drafts; an analyst reviews every output.*
- [ ] 3. Customer personal data through an external LLM API without all four safeguards: *No. No customer personal data.*
- [ ] 4. Agentic write access or authority: *No. Tools are read-only. The agent cannot write to production systems, move money, communicate with customers, or change identity and access.*
- [ ] 5. Biometric, deepfake-capable media, voice cloning, medical imagery: *No.*
- [x] 6. Any agentic system: *Yes. Minimum T2.*
- [ ] 7 to 9: *No.*

Scoring (highest dimension High) and override item 6 give T2. The AI Risk Committee classified the pilot as T1 at its 2026-01-25 meeting because the agent sends confidential research data to an external vendor API, plans and runs multi-step tool use within a session, and its drafts feed research distributed under MiFID II. All T1 controls apply.

---

## Agentic AI Risk Analysis

### Uncontrolled Action Risk

**Scenario:** Agent executes data queries that are technically permitted but contextually inappropriate (e.g., querying data about a company where the firm has MNPI).

**Likelihood:** Low (MNPI systems are architecturally isolated; agent has no access)
**Impact:** Critical (MAR violation; regulatory enforcement)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. Agent has read-only access to approved data sources only
2. MNPI systems are not connected to the agent's tool set: architectural isolation
3. MNPI indicator detection on all outputs
4. Plan review gate: analyst approves data sources before agent queries them
5. Tool call allowlist: only pre-approved queries permitted

### Prompt Injection via Retrieved Documents

**Scenario:** A document in the research corpus contains adversarial content that manipulates the agent's analysis or causes it to bypass guardrails.

**Likelihood:** Very Low (internal document corpus; controlled ingestion)
**Impact:** Medium (manipulated research draft; caught in analyst review)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. Document corpus is internal, curated, and access-controlled
2. Input sanitization on retrieved document content
3. Output guardrails validate analysis against expected patterns
4. All outputs reviewed by analyst before use

### Cascading Error Risk

**Scenario:** Agent makes incorrect interpretation in step 2 of a 10-step plan; subsequent steps build on the error, producing a coherent but fundamentally flawed analysis.

**Likelihood:** Medium (multi-step reasoning is an LLM weakness)
**Impact:** Medium (flawed draft; analyst review is the catch)
**Residual risk after mitigation:** Medium-Low

**Mitigations:**
1. Maximum 20 tool calls per session limits cascade depth
2. Mandatory source attribution: analyst can verify each claim
3. Intermediate results visible in session log
4. Analyst trained to verify independently, not rubber-stamp

---

## Governance Requirements (T1: Agentic)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| AI Risk Committee approval | Complete | Approved with conditions 2026-01-25 |
| Architecture review (full tool and data flow audit) | Complete | Architecture review doc AR-2026-RA-001 |
| Action inventory and blast radius assessment | Complete | 12 permitted tools documented |
| Pre-release evaluation | Complete, with exception | 300 cases, 2026-01-20. Hallucination rate 1.3% against the T1 cap of 1%: see [exception EXC-2026-004](#exception-exc-2026-004-hallucination-threshold) |
| Adversarial testing (red-team) | Complete | 220 adversarial cases including manual testing, 2026-01-19 (T1 minimum 200); no unresolved Critical findings |
| MNPI isolation verification | Complete | Security team verification dated 2026-01-18 |
| Plan review gate | Implemented | Analyst must approve plan before execution |
| Full session logging | Active | 7-year retention; every tool call, parameter, and result |
| Real-time action monitoring | Active | Anomaly detection on tool call patterns |
| Circuit breaker | Implemented | Triggers on: >3 consecutive errors, budget exceeded, anomaly detected |
| Kill switch | Implemented | Operator can halt any session immediately |
| Metrics review | Active | Daily dashboard check by AI Operations; monthly system-owner review |
| Formal governance review | Scheduled | Quarterly. Next: 2026-05-01 |
| Quarterly red-team testing | Scheduled | Next: 2026-04-15 |

---

## Conditions of Approval (AI Risk Committee, 2026-01-25)

1. **Pilot phase only:** Limited to 5 named senior analysts for 3 months
2. **No expansion without re-assessment:** Expanding to additional users or use cases requires new risk assessment
3. **Weekly session review:** AI Risk team reviews 20% of sessions weekly
4. **MNPI controls verification:** Security team re-verifies MNPI isolation quarterly
5. **Analyst training required:** All pilot users must complete agentic AI awareness training
6. **Hallucination rate gate:** If the production hallucination rate exceeds 1% (the [T1 cap](../../framework/llm-lifecycle/evaluation-governance.md#threshold-definitions-by-tier)) in any rolling 2-week window, the system is paused pending investigation. A use-case tolerance applies only when it is stricter than the tier cap, so this gate cannot be set above 1%.
7. **Hallucination threshold exception:** Deployment proceeds under exception EXC-2026-004 (below). The exception covers the pre-release result only and does not relax the gate in condition 6.

---

## Exception EXC-2026-004: Hallucination Threshold

Recorded in the exception register per [exceptions and risk acceptance](../../framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance).

| Field | Value |
|-------|-------|
| Exception ID | EXC-2026-004 |
| System | Investment Research Assistant Agent (research-agent-v0.9) |
| Control ID | EV-001 (pre-release evaluation; hallucination rate against the T1 cap of 1%) |
| Reason | Pre-release evaluation on 2026-01-20 measured a hallucination rate of 1.3% (4 of 300 responses). All other metrics passed. The four failures were unsourced figures in multi-source synthesis. |
| Compensating controls | Pattern 1 (human-in-the-loop): an analyst reviews every output in full before any use, with no move to sampled review, until a re-evaluation passes. Prompt fix to require a source citation for every figure. |
| Approver | AI Risk Committee (signed by the Chair) |
| Start date | 2026-01-25 |
| Expiry date | 2026-03-26 (60 days) |
| Status | Closed 2026-03-01. The full suite re-run on prompt v0.9.1 (2026-02-28) measured 0.0% (0 of 300; one-sided 95% upper bound 0.99%), within the T1 cap under the statistical pass rule. |
