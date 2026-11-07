# Multi-Agent System Governance

## Overview

Multi-agent systems — where multiple AI agents collaborate, coordinate, or are orchestrated to complete tasks — introduce governance challenges absent in single-agent deployments. Accountability is diffuse, failures cascade, and emergent behaviors arise from inter-agent interactions that individual agent testing cannot predict.

This document defines governance standards for multi-agent systems. It extends the single-agent risk taxonomy in [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md) and should be used alongside it.

Every agent in a multi-agent system also meets [agent identity and tool governance](agent-identity-and-tool-governance.md): its own identity, delegation that only narrows at each hop, a tool allowlist with scopes, approval gates, memory controls, authenticated inter-agent messages, a sandbox for code execution, the kill switch and the agent action audit record (AR-006, PM-006, PM-007). This document adds what is specific to agents working together.

All multi-agent systems are **minimum T2 (High)**, and T1 when any agent meets an automatic T1 condition. The tier rule is in [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md#mandatory-risk-tier-classification).

---

## Architecture Patterns

| Pattern | Description | Governance Complexity | Example |
|---------|-------------|:---:|---------|
| Orchestrator-worker | Single orchestrator dispatches tasks to specialized agents | Moderate | Research orchestrator sends data-gathering tasks to retrieval agent, analysis to reasoning agent |
| Pipeline | Sequential agents — output of A becomes input of B | Moderate | Document intake → summarization → classification → routing |
| Peer-to-peer | Agents negotiate and coordinate without central authority | High | Multiple agents collaborating on a shared analysis, each contributing expertise |
| Hierarchical | Multi-level orchestration — agents spawn sub-agents | High | Planning agent creates sub-plans executed by sub-agents, which may create their own sub-agents |

### Governance Requirements by Pattern

| Requirement | Orchestrator-Worker | Pipeline | Peer-to-Peer | Hierarchical |
|------------|:---:|:---:|:---:|:---:|
| Clear accountability chain | Orchestrator is accountable | Each stage has named owner | Must designate lead agent | Top-level orchestrator accountable |
| Inter-agent communication logging | All messages logged | All handoffs logged | All messages logged | All messages at every level logged |
| Privilege boundary enforcement | Per-agent permissions | Per-stage permissions | Per-agent permissions | Per-level + per-agent permissions |
| Failure isolation | Worker failure doesn't take down orchestrator | Stage failure halts pipeline | Requires explicit isolation design | Circuit breaker at each level |
| Depth limits | N/A (single level) | Pipeline length limit | N/A | Maximum nesting depth required |
| Human oversight insertion point | Before orchestrator dispatches | Between pipeline stages | At coordination points | At top level + configurable intermediate |

---

## Inter-Agent Communication Governance

### Message Validation

- All inter-agent messages must be logged in structured format with: source agent, destination agent, timestamp, message content (PII-redacted/tokenized per data classification policy), correlation ID
- Log retention follows the system's tier-based retention policy; apply data minimization — log message metadata and content hashes at minimum, full content only where required by tier
- Messages must conform to a defined schema — free-form text between agents creates untraceable accountability
- No agent may inject instructions to another agent's system prompt — inter-agent communication is data, not instructions
- Authentication, integrity protection and replay protection for messages are set in [inter-agent messages](agent-identity-and-tool-governance.md#6-inter-agent-messages-owasp-asi07); each message is also an entry in the [agent action audit record](../compliance/prompt-audit-trail.md#agent-action-audit-record)

### Privilege Boundaries

Per-agent identity, no shared credentials, least privilege, tool access fixed at deployment and delegation that never widens are set in [agent identity](agent-identity-and-tool-governance.md#1-agent-identity), [delegation](agent-identity-and-tool-governance.md#2-delegation) and [tools](agent-identity-and-tool-governance.md#3-tools-mcp-servers-and-a2a-peers). Two rules apply to the system as a whole:

| Rule | Description |
|------|-------------|
| Aggregate privilege analysis | Assess the combined permissions of agents that pass work to each other. Agents A and B together must not reach what neither is approved to reach alone |
| Cross-agent action validation | If Agent A requests Agent B to take an action, Agent B independently validates the request against its own policy and allowlist |

### Information Flow Controls

- Classify data at each agent boundary — data classification may change as it flows through agents
- Prevent unintended information propagation (e.g., Agent A has access to PII; Agent B should not receive PII in its context)
- Implement data minimization — each agent receives only the information it needs, not the full context of previous agents
- Apply PII redaction/tokenization at each boundary crossing where the downstream agent does not need PII to perform its task
- Monitor for information leakage patterns across agent boundaries

---

## State Management

### Persistent Memory Governance

Memory scope, time to live (default: session-scoped), PII scanning, provenance, audit, versioning, isolation between users and sessions, and erasure are set for every agent in [memory](agent-identity-and-tool-governance.md#5-memory-owasp-asi06). In a multi-agent system, also record which agents may read another agent's memory; by default none can.

### Context Window Management

- Safety instructions must be preserved as context grows — implement anchoring at beginning and end of context
- Define context pruning strategies that never remove safety-critical instructions
- Monitor context utilization — alert when agents approach context limits (degraded performance)

### Shared State

If agents share mutable state (databases, queues, shared memory):
- Implement validation gates on all shared state access
- Log all reads and writes with agent ID and correlation ID
- Use optimistic concurrency control or locking to prevent conflicting writes
- Monitor for anomalous shared state access patterns

---

## Cascading Failure Governance

### Blast Radius Analysis

Before deploying a multi-agent system, document:
- Maximum number of downstream agents affected by a single agent's failure
- Maximum number of actions that can be taken before a human checkpoint
- Maximum financial exposure of an uninterrupted agent chain
- Worst-case scenario analysis: what happens if the first agent in the chain fails silently?

### Circuit Breakers

| Level | Trigger | Action |
|-------|---------|--------|
| Per-agent | > N consecutive errors; budget exceeded; anomaly detected | Halt agent; alert operator; system continues without failed agent if possible |
| System-wide | > N agent failures; aggregate error rate > threshold; total cost exceeded | Halt all agents; alert operator; require human restart |
| Depth limit | Agent nesting exceeds maximum depth | Prevent sub-agent creation; return error to parent |
| Rate limit | Aggregate action rate across all agents exceeds threshold | Throttle; alert operator |

### Graceful Degradation

Define degraded operation modes:
- Single agent failure: can the system continue with reduced capability?
- Multiple agent failure: at what point does the system stop and alert a human?
- Infrastructure failure: what happens if the communication channel between agents fails?

---

## Accountability Chain

### Output Attribution

- Every output of a multi-agent system must be traceable to the specific agent that produced it
- Audit trail must span agent boundaries — use correlation IDs that persist across the full agent chain
- Final output must attribute contributing agents and their individual contributions

### Human Accountability

| Requirement | Description |
|-------------|-------------|
| Single accountable owner | Every multi-agent system has exactly one human owner accountable for its behavior |
| Incident accountability | The system owner is responsible for incidents, regardless of which agent caused them |
| No diffusion of responsibility | "The agent did it" is never an acceptable root cause; systemic governance failure is |

---

## Human Oversight Patterns

### Approval Gates

- Irreversible actions require human confirmation, regardless of which agent initiates them
- High-impact actions (financial, customer-facing, data-modifying) require human approval even if the individual agent has permission
- Configure approval gates at the system level, not per-agent — the orchestrator manages human checkpoints
- What the approver sees and how the gate is enforced: [human approval gates](agent-identity-and-tool-governance.md#4-human-approval-gates)

### Visibility

- Provide humans visibility into inter-agent reasoning, not just the final output
- Dashboard showing: which agents are active, what each is doing, what actions have been taken
- Full session replay capability for incident investigation

### Override and Kill Switch

| Control | Scope | Access |
|---------|-------|--------|
| Pause single agent | Halt one agent without stopping others | Operator |
| Pause all agents | Halt entire multi-agent system | Operator |
| Kill switch | Stop or degrade every agent in the system and revoke their credentials and delegated tokens; non-waivable | Per [kill switch](agent-identity-and-tool-governance.md#8-kill-switch) (PM-006), which also sets time to effect and testing |
| Override agent decision | Human overrides a specific agent's output or action | System owner |

---

## Pre-Deployment Requirements

For all multi-agent systems (in addition to single-agent requirements in [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md)):

| Requirement | Description |
|-------------|-------------|
| Architecture review | Full review including inter-agent communication, privilege boundaries, failure modes |
| Agent identity and tool review | AR-006 completed for every agent in the system, including the delegation limits between them |
| Blast radius analysis | Document maximum impact of cascading failures |
| Inter-agent testing | Test agent interactions specifically — not just individual agents in isolation |
| Emergent behavior assessment | Test for behaviors that emerge from agent interaction but are absent in individual testing |
| Depth/breadth limits | Define and enforce maximum nesting depth and maximum concurrent agents |
| Human checkpoint design | Document where and how humans oversee the multi-agent system |
| Circuit breaker testing | Verify all circuit breakers function correctly |
| Kill switch testing | Verify the kill switch stops every agent and revokes their credentials within the time set in [kill switch](agent-identity-and-tool-governance.md#8-kill-switch) (PM-006) |

---

## Implementation Notes

- Test multi-agent systems as a system, not just as individual agents. Emergent behaviors are the primary risk.
- Start with the simplest architecture pattern (orchestrator-worker) before adopting more complex patterns.
- The complexity of governance increases non-linearly with the number of agents. More agents = disproportionately more governance effort.
- Monitor inter-agent communication volume and patterns — unexpected changes often signal problems.
