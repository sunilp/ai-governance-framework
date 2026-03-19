# AI Incident Forensics

## Overview

When an AI incident occurs, the immediate priority is mitigation. But without structured forensics — evidence preservation, chain reconstruction, and root cause analysis — the organization cannot learn from the incident, satisfy regulatory obligations, or prevent recurrence.

AI incident forensics differs from traditional IT forensics. The "evidence" is probabilistic model outputs, context windows measured in tens of thousands of tokens, and inter-agent communication chains. Reconstructing what happened requires purpose-built procedures.

---

## Evidence Preservation

Preserve evidence within 1 hour of incident detection. AI evidence degrades: model providers update models, context windows expire, and log rotation may delete critical records.

### Evidence Collection Checklist

| Evidence Type | Collection Method | Retention | Priority |
|--------------|------------------|-----------|:---:|
| Prompt/response logs | Extract from audit trail system | Per [audit trail requirements](../compliance/audit-trail-requirements.md) | Immediate |
| Full conversation context | Extract complete session including system prompt, all turns, retrieved documents | Incident retention (minimum 3 years) | Immediate |
| Model version at time of incident | Record exact model version (API model ID, checkpoint hash) | Incident retention | Immediate |
| Guardrail configuration | Capture active guardrail rules, thresholds, filter versions | Incident retention | Within 1 hour |
| RAG retrieval results | Documents retrieved, relevance scores, source metadata | Incident retention | Within 1 hour |
| System metrics | Latency, error rates, token usage, cost at time of incident | Incident retention | Within 1 hour |
| User session context | Session metadata (sanitized, PII-redacted where possible) | Incident retention | Within 4 hours |
| Infrastructure state | Server/container logs, resource utilization, deployment state | Incident retention | Within 4 hours |
| Vendor status | Model provider status page snapshots, known issues, recent updates | Incident retention | Within 4 hours |

### Evidence Integrity

- Store incident evidence in a separate, tamper-evident location (not the same system that had the incident)
- Hash all collected evidence at time of collection (SHA-256)
- Maintain chain of custody: who collected what, when, from where
- Do not modify evidence — create copies for analysis

---

## LLM-Specific Forensics

### Prompt/Response Chain Reconstruction

Rebuild the complete interaction that led to the incident:

1. **System prompt at time of incident** — was it the approved, version-controlled prompt? Had it been modified?
2. **Full conversation history** — all user turns and model responses leading to the incident
3. **Retrieved context (RAG)** — what documents were retrieved? Were they legitimate? Were any adversarial?
4. **Tool call history (agentic)** — every tool call with parameters and results
5. **Guardrail decisions** — what did each guardrail layer decide at each step? What passed? What was filtered?

### Context Window Analysis

| Question | Investigation Approach |
|----------|----------------------|
| Was the safety instruction displaced? | Compare context window at incident time against expected structure |
| Was the context window full? | Check token count; safety instruction anchoring may have failed |
| Was adversarial content in context? | Search retrieved documents and tool outputs for injection patterns |
| Was the context constructed correctly? | Verify prompt assembly pipeline produced expected context structure |

### Model Version Investigation

| Question | Investigation Approach |
|----------|----------------------|
| Which exact model version produced the output? | Cross-reference API logs with vendor changelog |
| Had the vendor recently updated the model? | Check vendor changelog around incident date (±7 days) |
| Is this a known model issue? | Search vendor known issues, community reports, safety benchmarks for similar behavior |
| Can the incident be reproduced? | Replay the exact prompt/context on the same model version (if available) |

### Guardrail Replay

Replay the incident through the current guardrail pipeline:
1. Submit the incident-triggering input through current safety classifiers
2. Did current guardrails catch it? If yes — were guardrails modified since the incident?
3. If no — this is a guardrail gap that needs remediation
4. Document guardrail version at time of incident vs. current

### Evaluation Suite Regression

Run the incident scenario through the evaluation suite:
1. Was this scenario covered in the eval suite? If not — add it
2. If covered, did the eval suite catch it? If not — why? (threshold too lenient? eval methodology gap?)
3. Was the eval suite current at time of incident? (had it been run recently?)

---

## Multi-Agent Incident Tracing

For incidents involving multi-agent systems, additional forensics are required.

### Correlation ID Tracking

Every multi-agent system must use correlation IDs that persist across agent boundaries. During forensics:
1. Identify the correlation ID for the incident session
2. Extract all logs across all agents for that correlation ID
3. Reconstruct the full agent chain: which agent called which, with what inputs, producing what outputs

### Causation Chain Reconstruction

| Step | Activity |
|------|----------|
| 1 | Identify the agent that produced the problematic output |
| 2 | Trace backward: what input did this agent receive? From which agent? |
| 3 | Continue tracing until you reach the root input (user or external trigger) |
| 4 | Identify the point where the chain went wrong — was it the input, the agent's reasoning, or the tool output? |
| 5 | Assess whether the failure would have been caught by any downstream agent |

### Inter-Agent State Examination

- What was each agent's state/memory at the time of the incident?
- Had any agent accumulated adversarial context from earlier interactions?
- Were inter-agent messages validated at each boundary?
- Did any agent exceed its privilege boundaries?

---

## Post-Mortem Process

### Timeline and Ownership

| Activity | Timeline | Owner |
|----------|----------|-------|
| Evidence preservation | Within 1 hour of detection | On-call engineer |
| Initial investigation summary | Within 24 hours (S1) / 48 hours (S2) | Incident commander |
| Post-mortem meeting | Within 48 hours (S1) / 1 week (S2) | Incident commander |
| Post-mortem report | Within 1 week (S1) / 2 weeks (S2) | Incident commander |
| Remediation tracking | Until all actions complete | System owner |

### Blameless Review Principles

1. Focus on systemic causes, not individual errors
2. Ask "why did the system allow this?" not "who caused this?"
3. Assume everyone acted with the best information available to them
4. The goal is to improve the system, not to assign blame

### Post-Mortem Report Structure

1. **Incident summary** — what happened, severity, impact
2. **Timeline** — chronological reconstruction from evidence
3. **Root cause analysis** — 5 Whys or equivalent; identify the systemic issue
4. **Contributing factors** — what conditions enabled the incident
5. **What went well** — detection, response, communication that worked
6. **What could improve** — gaps identified during response
7. **Systemic improvements** — changes to governance controls, guardrails, monitoring, training
8. **Control gap assessment** — which governance control should have prevented this? Why didn't it?
9. **Action items** — specific, owned, time-bound remediation actions
10. **Follow-up schedule** — when to verify remediation effectiveness

### Sign-Off

| Role | Sign-off |
|------|----------|
| Incident commander | Confirms report accuracy |
| System owner | Accepts remediation actions |
| AI Risk Lead | Confirms control gap assessment |
| Compliance (if regulatory impact) | Confirms regulatory notification assessment |

---

## Evidence Retention

Incident evidence follows the system's tier-based retention per [audit-trail-requirements.md](../compliance/audit-trail-requirements.md):

| Tier | Retention |
|------|-----------|
| T1 | 7 years |
| T2 | 5 years |
| T3 | 3 years |
| T4 | 3 years (minimum for incident evidence, regardless of tier) |

Post-mortem reports are retained for the same period as incident evidence.

---

## Implementation Notes

- Automate evidence collection where possible — manual collection under incident pressure is error-prone
- Pre-configure forensics queries in your logging platform so they're ready when needed
- Practice forensics procedures during incident drills — don't wait for a real incident to discover your evidence is incomplete
- Cross-reference incident findings across the portfolio — one system's incident may reveal a vulnerability in others
