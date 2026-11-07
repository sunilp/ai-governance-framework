# Agent Identity and Tool Governance

## Purpose

This is the standard for any AI system that calls tools, MCP servers, other agents or code interpreters. It sets who the agent is, whose authority it acts on, what it may call, which actions need a human, how memory, inter-agent messages and code execution are contained, how the agent is stopped, and what is logged.

The risk taxonomy stays in [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md). Multi-agent architecture patterns, circuit breakers and accountability stay in [multi-agent-governance.md](multi-agent-governance.md). Both link here for the requirements below.

## How It Fits the Workflow

- **Scope:** every agentic system, including read-only tool use, and every multi-agent system. A "tool" is anything the model can invoke: a function or API, an MCP server, an A2A peer, a browser, a code interpreter or another agent.
- **Tier:** every agentic system is at least T2 (override item 6), and T1 when it has write access to production systems or data stores, or authority to move money, communicate with customers, or change identity and access (override item 4). See the [canonical override list](../risk-classification/agentic-ai-risk.md#tier-override-rules). A T3 or T4 system that gains tool access is re-tiered before the change goes live.
- **Stage 3:** AR-006 reviews the agent identity record, tool allowlist, delegation limits and approvals in this document. AR-007 covers the contract for any external tool, MCP server or A2A peer run by a vendor.
- **Stage 6:** SR-001 tests tool misuse, privilege escalation, delegation abuse and memory poisoning against the limits recorded here.
- **Stage 8:** PM-006 tests the kill switch. PM-007 checks the agent action audit record is complete.
- **Stage 9:** the AR-006 record is re-checked at every formal review (RV-001) and whenever a tool, scope or delegation limit changes.
- **What it changes:** no tier, threshold, approver, cadence or retention period. Values marked "framework default" are starting points the tier approver can tighten.

---

## 1. Agent Identity

Every agent has its own non-human identity. The agent proves who it is to every tool and peer it calls, and every action it takes is attributable to that identity.

| Requirement | Rule |
|-------------|------|
| One identity per agent | Each agent has its own identity, issued by the organisation's identity provider or workload identity platform. Two agents never share a service account. Replicas of the same agent may share an identity only if the audit record still identifies the instance |
| No borrowed human credentials | An agent never uses a person's password, session cookie, personal access token or API key. When it acts for a user, it uses delegated authority (section 2), not the user's credentials |
| Accountable human owner | Each agent identity names one accountable person, normally the system owner. An identity with no active owner is disabled until a new owner accepts it |
| Credentials out of the model's reach | Secrets and tokens are held by the agent runtime or tool gateway, never placed in the prompt, memory, tool outputs or logs the model can read |
| Issue | The identity is created at deployment, recorded in the agent identity record below, and linked to the system's [AI inventory](../governance-operations/ai-inventory.md) entry (RA-006) |
| Rotate | Prefer short-lived credentials issued at runtime. Where a static secret cannot be avoided, keep it in a secrets manager and rotate it at least every 90 days (framework default) and on any suspected exposure |
| Revoke | Revoke on retirement (DR-004), on loss of an owner, on suspected compromise and as part of every kill switch activation (section 8) |

### Agent Identity Record

The AR-006 evidence for each agent:

| Field | Content |
|-------|---------|
| Agent ID | Unique identifier, the same one used in the agent action audit record |
| System | System name, system ID and tier |
| Accountable owner | Named person and role |
| Purpose | What the agent is for, in one or two sentences |
| Identity type and issuer | For example a workload identity, a service principal or a certificate, and the system that issues it |
| Credential lifetime and rotation | Token lifetime or rotation schedule |
| Delegation mode | Acts as itself, on behalf of users, on behalf of other agents, or a combination; with the delegation limits from section 2 |
| Tool allowlist | Reference to the allowlist in section 3 |
| Memory scope | What the agent may store and for how long (section 5) |
| Kill switch | How to activate it, who can, and the last test date (section 8) |
| Approvals | Who approved the record and each later change, with dates |

---

## 2. Delegation

When an agent acts on behalf of a user or another agent, the downstream system must be able to see both who is acting and on whose behalf.

| Requirement | Rule |
|-------------|------|
| Explicit | The authority is granted by a recorded grant or token, not inferred from the conversation. "The user asked me to" is not authority |
| Scoped | The grant names the tools, actions, resources and value limits it covers |
| Time-bound | The grant expires when the task or session ends, or earlier. No standing delegation |
| Narrows at each hop | Each hop receives a subset of the authority it was given. Scope can stay the same or narrow; it never widens. An agent cannot grant another agent a permission it does not hold itself |
| Bounded by the principal | The agent's effective permission is the intersection of its own permissions and the principal's. An agent never does for a user something that user could not do directly |
| Traceable | The original principal and every intermediate agent stay identifiable through the chain, and the chain is written to the agent action audit record |
| Verified downstream | The tool or peer that executes the action checks the whole chain, not just the last caller |
| No impersonation | The agent does not present itself as the user in a way that makes the two indistinguishable downstream. Use delegation, which keeps both identities visible |
| Depth limit | The maximum delegation depth is recorded and enforced, in line with the [depth limits](multi-agent-governance.md#governance-requirements-by-pattern) for multi-agent patterns |

---

## 3. Tools, MCP Servers and A2A Peers

### Allowlist

Tool access is deny by default. Each agent has an allowlist, fixed at deployment, and the agent cannot add tools or change tool definitions at runtime.

| Field per allowlist entry | Content |
|---------------------------|---------|
| Tool | Name and type: function or API, MCP server, A2A peer, browser, code execution, other agent |
| Owner | Team or vendor accountable for the tool |
| Source and version | Where it comes from, the pinned version, and a hash of the tool definition or description the model sees |
| Scopes | The least-privilege permissions granted: read or write, and the specific resources (accounts, tables, folders, endpoints) |
| Data | The highest data classification the tool may receive or return |
| Consequential | Whether the tool can take a consequential action (below) |
| Limits | Rate limit and caps |
| Approval gate | Whether a human approves before execution (section 4) |

### Least Privilege

- Grant scopes per tool, not per agent. Separate read from write.
- Scope to resources, not whole systems: one queue, one folder, one set of accounts.
- Assess tool combinations as well as single tools. Read access to customer data plus an outbound email tool is an exfiltration path even though neither is on its own. See [complex tool chain risk](../risk-classification/agentic-ai-risk.md#8-complex-tool-chain-risk).

### Tool Approval and Supply Chain (OWASP ASI04)

- **Approval:** a new tool, MCP server or A2A peer, a new version, or a wider scope is a change to the AR-006 record and needs the approval in the tier table below.
- **Provenance:** record the publisher and source of each tool in the AI-BOM ([agent tools and integrations](../ai-security/supply-chain-security.md#ai-bom-contents)). Install from verified sources and internal mirrors, not directly from public registries at runtime.
- **Version pinning:** pin tool and MCP server versions. Store a hash of each tool definition the model sees.
- **No silent changes:** at runtime, compare tool definitions with the approved hash. A tool whose name, description, parameters or behaviour changed without review is blocked until it is reviewed. Remote MCP servers and A2A peers run by others can change without a version bump, so monitor their definitions on every connection.
- **Third parties:** a tool, MCP server or A2A peer run by an external party is a third-party service. It needs the vendor assessment (AR-005), the contract terms in [AI procurement clauses](../compliance/ai-procurement-clauses.md) (AR-007) and data residency confirmation (AR-003).

### Caps on Consequential Actions

A consequential action moves money, changes customer or production records, sends an external communication, changes identity or access, deletes data, or runs code with side effects.

- Each consequential tool has a per-action cap (value, record count or recipients), a per-session cap and a rate limit. T1 systems also have a daily cap.
- Caps are enforced in the tool gateway or the tool itself, outside the model. A prompt cannot raise them.
- A cap breach blocks the action and raises an alert.

---

## 4. Human Approval Gates

Irreversible and high-value actions need a human decision before they run. The gate patterns are in [HITL for agentic AI](../responsible-ai/human-in-loop-patterns.md#hitl-for-agentic-ai).

- The AR-006 record lists which actions are gated and sets the value threshold for "high-value" per use case.
- The approver sees the actual action and its parameters, not only the agent's summary of it. This guards against an agent talking a reviewer into approval (OWASP ASI09).
- Only a person can approve. An agent cannot approve another agent's action.
- The approver must hold the authority for the action. Approval does not extend anyone's authority.
- The gate is enforced in the tool gateway or policy layer, so an injected instruction cannot skip it.
- Each approval is recorded with approver, action, parameters shown, decision and time, and referenced from the agent action audit record.

---

## 5. Memory (OWASP ASI06)

| Requirement | Rule |
|-------------|------|
| What may be stored | Defined per agent in the AR-006 record. Default: session-scoped, nothing persists. Never credentials or secrets. Personal data only for a documented purpose covered by the DPIA screening (RA-005) |
| Retention | Each memory category has a time to live. Personal data is kept no longer than its purpose needs |
| PII scanning | Scan every write to persistent memory for personal data and apply the redaction policy |
| Provenance | Tag each memory entry with its source (user, tool, retrieved document, other agent) and time |
| Poisoning defences | Content from tools, documents and other agents is stored as data and never promoted to instructions. Validate writes against the memory schema. Keep each user's and tenant's memory separate |
| Audit and rollback | Log every write. Version memory so it can be rolled back to a known-good state during an incident. Review a sample of stored memory at each formal review |
| Erasure | Support deletion of a person's data from memory, to meet erasure requests |

For multi-agent systems, memory sharing between agents and shared mutable state are covered in [persistent memory governance](multi-agent-governance.md#persistent-memory-governance) and [shared state](multi-agent-governance.md#shared-state).

---

## 6. Inter-Agent Messages (OWASP ASI07)

- **Authenticated:** each message carries the sender's agent identity, and the receiver verifies it (mutual TLS or signed tokens).
- **Integrity-protected:** messages are signed or sent over a channel that protects integrity, with expiry and replay protection.
- **Logged:** messages are logged with source, destination, time and correlation ID per [message validation](multi-agent-governance.md#message-validation).
- **Data, not instructions:** the receiver treats message content as data and checks any requested action against its own policy and allowlist.
- **External peers:** A2A peers outside the organisation are on the allowlist, and their published descriptions are pinned and reviewed like tool definitions.

---

## 7. Code Execution (OWASP ASI05)

Code written by a model runs only in a sandbox:

- isolated from the host and from other sessions (container or micro-VM);
- no network egress by default, and an allowlist where egress is needed;
- no access to production credentials or data, apart from the minimum read-only inputs mounted for the task;
- limits on CPU, memory, run time and output size;
- created for the task and destroyed afterwards, with nothing carried over between users;
- packages from an internal mirror only.

The application never evaluates model output in its own process. A shell tool with production access is not allowed at any tier.

---

## 8. Kill Switch

Every agentic system and every T1 customer-facing system has a kill switch. This is non-waivable ([Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance)).

| Requirement | Rule |
|-------------|------|
| Time to effect | Stop or degrade the system within 15 minutes of the decision to activate, the same limit as safeguard d in the [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) |
| What stop means | No new actions start. In-flight actions are halted or completed safely as the runbook says. Queued and scheduled tasks are cancelled. In a multi-agent system, every agent stops, not only the one that failed |
| Credential revocation | The agent's credentials and outstanding delegated tokens are revoked or suspended as part of the stop, so a process that keeps running cannot act |
| Degrade options | Defined in advance: read-only mode, approval for every action, specific tools disabled, or routing to a human team |
| Who can activate | The on-call operator (IR-002), the incident commander or the system owner, with no further approval needed |
| Testing | Tested at least quarterly for T1 customer-facing systems and all agentic systems, and after any change to the agent's runtime or identity set-up (PM-006). The test records the decision time, the time stop was confirmed, and proof that a revoked credential was refused |

---

## 9. Agent Action Audit Record

Every tool call, delegation, memory write and inter-agent message is logged in the [agent action audit record](../compliance/prompt-audit-trail.md#agent-action-audit-record), alongside the per-request record. Retention follows the interaction log periods in [retention requirements](../compliance/prompt-audit-trail.md#retention-requirements). Audit logging is non-waivable. PM-007 checks the record is complete.

---

## Tier Scaling

T3 and T4 do not apply: every agentic system is at least T2.

| Requirement | T1 | T2 |
|-------------|----|----|
| Own non-human identity and named owner | Required | Required |
| Credentials | Short-lived, issued at runtime; no static secrets in the agent runtime | Short-lived preferred; static secrets in a secrets manager, rotated at least every 90 days (framework default) |
| Delegation | Narrowed at every hop; chain verified by the executing tool on every call | Narrowed at every hop; chain recorded in the audit record and checked by the executing tool |
| Tool allowlist with per-tool scopes | Required | Required |
| Approval of a new tool, peer, version or wider scope | Technical owner and Security; changes that add write access or an external peer also go to the architecture review board (AR-002) | Technical owner and Security; changes that add write access also go to the Head of AI or delegate design review (AR-002) |
| Tool definition change detection | Block any unapproved change | Block unapproved changes to tools with write scopes; alert on read-only tools |
| Caps on consequential actions | Per action, per session and per day; breach blocks | Per action and per session; breach blocks |
| Human approval gates | Irreversible or high-value actions; plan review before a multi-step task that includes a consequential action | Irreversible or high-value actions |
| Memory | Section 5 in full | Section 5 in full |
| Inter-agent messages | Each message signed by the sender, with replay protection; logged | Authenticated channel that protects integrity (for example mutual TLS), with replay protection; logged |
| Code execution | Sandbox per section 7 | Sandbox per section 7 |
| Kill switch | Within 15 minutes, with credential revocation; tested quarterly (PM-006) | Within 15 minutes, with credential revocation; tested quarterly (PM-006) |
| Agent action audit record | Every tool call, delegation, memory write and inter-agent message (PM-007) | Every tool call, delegation, memory write and inter-agent message (PM-007) |
| Review of the AR-006 record | At each formal review (RV-001) and on any change | At each formal review (RV-001) and on any change |

---

## Reference Implementation Options

Status as of November 2026. These are options to evaluate, not requirements. The standard above is technology-neutral; pick the mechanisms that fit your identity platform.

| Option | What it is | Where it helps |
|--------|-----------|----------------|
| OAuth 2.0 Token Exchange (RFC 8693) | IETF Standards Track RFC, January 2020. A client exchanges one token for another, and can request a narrower scope and a specific audience or resource. The `act` claim identifies the acting party, nested `act` claims express a delegation chain, and `may_act` states who may act for a subject. The RFC distinguishes delegation from impersonation | Delegated, narrowed tokens for on-behalf-of calls (section 2) |
| IETF WIMSE working group | Workload Identity in Multi System Environments, an active IETF working group. Its charter covers the propagation, representation and processing of workload identities, a token to protect a chain of HTTP calls, and token exchange at security boundaries. The charter does not name AI agents | Workload identity and call-chain context for agent runtimes (sections 1 and 2) |
| SPIFFE and SPIRE | Secure Production Identity Framework for Everyone, a CNCF graduated project (August 2022). Issues short-lived identity documents (SVIDs) in X.509 or JWT form; SPIRE is its implementation | Issuing and rotating workload identities for agent runtimes (section 1) |
| NCCoE concept paper on software and AI agent identity and authorization | Published by NIST's National Cybersecurity Center of Excellence on 5 February 2026; comments closed 2 April 2026. Scopes a potential project applying identity standards and practices to AI agents, covering identification, authorization, auditing, non-repudiation and prompt injection controls | Track for a reference architecture; see [Related NIST Work](../compliance/nist-ai-rmf-mapping.md#related-nist-work) |
| OWASP Top 10 for Agentic Applications 2026 | Threat list from the OWASP GenAI Security Project. ASI02 Tool Misuse and Exploitation, ASI03 Identity and Privilege Abuse, ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory and Context Poisoning and ASI07 Insecure Inter-Agent Communication map to sections 1 to 7 | Shared vocabulary for findings; see the [threat taxonomy mapping](../ai-security/adversarial-robustness.md#threat-taxonomy-mapping) |
| Agent Identity Protocol (AIP) | An open specification (Apache 2.0) for verifiable agent identity and delegation chains, in which each hop can only narrow scope. It defines bindings for MCP and A2A and has Python and Rust implementations. Published as an individual IETF Internet-Draft (draft-prakash-aip-02, October 2026), not a working group document. Disclosure: AIP is maintained by the author of this framework | Cryptographically verifiable delegation chains across agent hops (sections 1, 2 and 6) |

---

## Sources

- IETF, RFC 8693 OAuth 2.0 Token Exchange: https://www.rfc-editor.org/rfc/rfc8693
- IETF, Workload Identity in Multi System Environments (WIMSE) working group: https://datatracker.ietf.org/wg/wimse/about/
- SPIFFE overview: https://spiffe.io/docs/latest/spiffe-about/overview/
- CNCF, SPIFFE project page: https://www.cncf.io/projects/spiffe/
- NIST CSRC, Concept paper: Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization: https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd
- OWASP GenAI Security Project, OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- Agent Identity Protocol specification and implementations: https://github.com/sunilp/aip
- Agent Identity Protocol site: https://sunilprakash.com/aip/
- IETF Datatracker, draft-prakash-aip: https://datatracker.ietf.org/doc/draft-prakash-aip/
