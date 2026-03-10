# Risk Assessment: Investment Research Assistant Agent

## System Overview

| Field | Value |
|-------|-------|
| System Name | Investment Research Assistant Agent |
| System ID | research-agent-v0.9 |
| Business Unit | Investment Research |
| Assessment Date | 2026-01-15 |
| Assessor | Senior AI Risk Analyst, Model Risk Management |

---

## GenAI Risk Dimension Scoring

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Hallucination Severity | **High (3)** | Incorrect financial data or analysis in research drafts. Mitigated by mandatory analyst review of all outputs. |
| Data Exposure Risk | **High (3)** | Processes confidential research data and market analysis. No customer PII, but sensitive business data. Vendor API with zero retention. |
| Prompt Injection Susceptibility | **Medium (2)** | Internal users only. However, agent processes retrieved documents which could contain adversarial content. |
| Output Controllability | **Medium (2)** | Agent executes multi-step plans autonomously within a session. Plan approval gate exists but intermediate steps are automated. |
| Third-Party Model Dependency | **High (3)** | Anthropic Claude API; Vertex AI fallback. Core workflow depends on LLM capability. |

**Aggregate Score: 13**
**Highest Dimension: High (3)**

### Risk Tier Determination

**Tier: T1 — Critical**

Automatic T1 trigger:
- [ ] Processes customer PII through external LLM API — *No*
- [ ] Generates customer-facing content without human review — *No*
- [ ] Makes or influences regulated decisions — *Indirect: research informs investment decisions*
- [x] Involves agentic behavior with production system access — *Yes: queries internal databases*

Automatic T1 due to agentic behavior with production data access.

---

## Agentic AI Risk Analysis

### Uncontrolled Action Risk

**Scenario:** Agent executes data queries that are technically permitted but contextually inappropriate (e.g., querying data about a company where the firm has MNPI).

**Likelihood:** Low (MNPI systems are architecturally isolated; agent has no access)
**Impact:** Critical (MAR violation; regulatory enforcement)
**Residual risk after mitigation:** Very Low

**Mitigations:**
1. Agent has read-only access to approved data sources only
2. MNPI systems are not connected to the agent's tool set — architectural isolation
3. MNPI indicator detection on all outputs
4. Plan review gate — analyst approves data sources before agent queries them
5. Tool call allowlist — only pre-approved queries permitted

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
2. Mandatory source attribution — analyst can verify each claim
3. Intermediate results visible in session log
4. Analyst trained to verify independently, not rubber-stamp

---

## Governance Requirements (T1 — Agentic)

| Requirement | Status | Evidence |
|-------------|--------|----------|
| AI Risk Committee approval | Complete | Approved with conditions 2026-01-25 |
| Architecture review (full tool and data flow audit) | Complete | Architecture review doc AR-2026-RA-001 |
| Action inventory and blast radius assessment | Complete | 12 permitted tools documented |
| Adversarial testing (red-team) | Complete | 100 adversarial scenarios tested |
| MNPI isolation verification | Complete | Security team verification dated 2026-01-18 |
| Plan review gate | Implemented | Analyst must approve plan before execution |
| Full session logging | Active | 7-year retention; every tool call, parameter, and result |
| Real-time action monitoring | Active | Anomaly detection on tool call patterns |
| Circuit breaker | Implemented | Triggers on: >3 consecutive errors, budget exceeded, anomaly detected |
| Kill switch | Implemented | Operator can halt any session immediately |
| Monthly review | Active | Next: 2026-04-01 |
| Quarterly red-team testing | Scheduled | Next: 2026-04-15 |

---

## Conditions of Approval (AI Risk Committee, 2026-01-25)

1. **Pilot phase only:** Limited to 5 named senior analysts for 3 months
2. **No expansion without re-assessment:** Expanding to additional users or use cases requires new risk assessment
3. **Weekly session review:** AI Risk team reviews 20% of sessions weekly
4. **MNPI controls verification:** Security team re-verifies MNPI isolation quarterly
5. **Analyst training required:** All pilot users must complete agentic AI awareness training
6. **Hallucination rate gate:** If hallucination rate exceeds 2% in any rolling 2-week window, system is paused pending investigation
