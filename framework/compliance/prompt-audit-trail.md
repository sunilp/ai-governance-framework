# Prompt and Response Audit Trail

## Overview

In a regulated environment, every consequential AI output must be reconstructable. For LLM systems, this means logging sufficient information to reproduce what the system was asked, what context it had, what it generated, and what the user did with that output.

This is not application logging. This is regulatory-grade audit trail designed to answer the question: "On this date, for this user, with this query, what did your AI system produce, and why?"

---

## What Must Be Logged

### Per-Request Audit Record

| Field | Description | Required For |
|-------|-------------|-------------|
| `request_id` | Unique identifier for the request | All tiers |
| `timestamp` | ISO 8601 timestamp (UTC) | All tiers |
| `user_id` | Authenticated user identifier | All tiers |
| `session_id` | Session or conversation identifier | All tiers |
| `use_case_id` | Which GenAI use case processed this request | All tiers |
| `system_prompt` | Full system prompt (or version reference) | T1, T2 |
| `system_prompt_version` | Version identifier of the system prompt | All tiers |
| `user_input` | The user's query or input | All tiers |
| `retrieved_context` | Documents/chunks retrieved by RAG (with source IDs) | T1, T2 (if RAG) |
| `retrieval_scores` | Relevance scores for retrieved documents | T1 (if RAG) |
| `model_id` | Model identifier and version | All tiers |
| `model_parameters` | Temperature, top_p, max_tokens, etc. | T1, T2 |
| `raw_response` | Full model output before post-processing | T1, T2 |
| `processed_response` | Output after guardrails, filtering, formatting | All tiers |
| `guardrail_actions` | Any guardrail triggers and actions taken | All tiers |
| `token_count_input` | Input token count | All tiers |
| `token_count_output` | Output token count | All tiers |
| `latency_ms` | End-to-end response time | All tiers |
| `user_feedback` | Explicit feedback (thumbs up/down, rating) if provided | All tiers |
| `error_details` | Error information if request failed | All tiers |

### Per-Session Audit Record (Conversational Systems)

| Field | Description |
|-------|-------------|
| `session_id` | Unique session identifier |
| `session_start` | Timestamp |
| `session_end` | Timestamp |
| `user_id` | Authenticated user |
| `turn_count` | Number of interaction turns |
| `escalation` | Whether the session was escalated to a human |
| `outcome` | Session outcome (resolved, abandoned, escalated) |

### Agent Action Audit Record

Required for every agentic system, alongside the per-request record. One record per tool call, delegation, memory write and inter-agent message. The fields support the [agent identity and tool governance](../llm-lifecycle/agent-identity-and-tool-governance.md#9-agent-action-audit-record) standard.

| Field | Description |
|-------|-------------|
| `action_id` | Unique identifier for the action |
| `request_id` | The per-request record that led to the action |
| `correlation_id` | Identifier that persists across every agent in a multi-agent chain |
| `action_type` | Tool call, delegation, memory write or inter-agent message |
| `agent_id` | Identity of the acting agent, as in its agent identity record |
| `principal_id` | The original principal: the user or system on whose behalf the agent acts, or the agent itself when it acts on its own authority |
| `delegation_chain` | Every agent between the principal and this action, in order, with the grant or token reference and the scope held at each hop |
| `tool` | Tool name, type (function or API, MCP server, A2A peer, code execution), version and definition hash |
| `arguments_hash` | Hash of the full arguments |
| `arguments_redacted` | Arguments with personal data and secrets redacted. For T1 and T2, the full values must be recoverable under the PII controls below where decision reconstruction needs them |
| `authorisation_decision` | Allowed or denied, the policy or rule that decided, and the result of cap and rate limit checks |
| `approval_reference` | Approval record ID and approver where a human approval gate applied |
| `result` | Success, failure or blocked; a summary or hash of the output; records affected or value moved |
| `timestamp_requested` | When the agent requested the action (ISO 8601, UTC) |
| `timestamp_decided` | When authorisation or approval was decided |
| `timestamp_completed` | When the action completed or failed |
| `error_details` | Error information if the action failed |

PM-007 checks that per-request records and agent action records are complete and kept for the tier's retention period.

---

## Logging Architecture

### Design Principles

1. **Append-only.** Audit records are immutable once written. No updates or deletions.
2. **Tamper-evident.** Use cryptographic hashing or blockchain-style chaining to detect modification.
3. **Separated from application logs.** Audit trail is a distinct data store with independent access controls.
4. **Asynchronous capture.** Logging must not degrade system performance. Write asynchronously with guaranteed delivery.
5. **Structured format.** All records in structured format (JSON) for queryable retrieval.

### Access Controls

| Role | Access Level |
|------|-------------|
| Application service account | Write-only (append) |
| Operations team | Read-only (for incident investigation) |
| Compliance / Audit | Read-only (full access for examinations) |
| Data science team | Read-only (anonymized, for quality analysis) |
| Model risk management | Read-only (full access for validation) |
| All others | No access |

---

## Retention Requirements

This section sets retention for interaction logs: prompts, responses, predictions and agent actions. Governance records (risk assessments, approvals, evaluation and incident reports, model cards, change history) follow [audit-trail-requirements.md](audit-trail-requirements.md#retention-periods).

<!-- BEGIN GENERATED: interaction-log-retention. Edit policy/tiers.yaml, then run python tools/build.py -->

| Tier | Retention Period |
|------|-----------------|
| T1 | 7 years |
| T2 | 5 years |
| T3 | 3 years |
| T4 | 1 year |

<!-- END GENERATED: interaction-log-retention -->

Tier periods are framework defaults. Set retention to the longest obligation that applies to you. Reference points: EU AI Act Art. 18 (provider technical documentation, 10 years), Art. 19 (provider-generated logs, at least 6 months), Art. 26(6) (deployer logs, at least 6 months); MiFID II Art. 16(7) (records of client communications, 5 years, up to 7 if the authority requests).

### PII in Audit Logs

If audit records contain PII (user queries about their own accounts, for example):
- PII fields must be encrypted at rest with key management per data security policy
- Access to PII fields requires additional authorization
- GDPR right-to-erasure requests must be handled; implement pseudonymization at ingestion so that PII can be removed without destroying the audit record's integrity
- Document the legal basis for PII retention in audit logs (legitimate interest for regulatory compliance)

---

## Reconstruction Capability

### Decision Reconstruction

For T1 and T2 use cases, the audit trail must support full decision reconstruction:

Given a `request_id`, you must be able to reproduce:
1. The exact system prompt that was active at that time
2. The user's input
3. The retrieved context (if RAG): the actual documents, not just references
4. The model and version used
5. The raw model output
6. The guardrail actions applied
7. The final output delivered to the user
8. For agentic systems, every action taken, with its delegation chain, authorisation decision and any human approval ([agent action audit record](#agent-action-audit-record))

This requires:
- **Prompt versioning:** System prompts stored with version history; audit record references the version, not the content (but content must be recoverable from the version)
- **Context archival:** Retrieved documents stored or referenced with sufficient detail to reconstruct the exact context window
- **Model version tracking:** Exact model version recorded (vendor models change without notice; track via behavior hashing or version API if available)

### Regulatory Examination Readiness

When a regulator asks to examine your AI system:

| Request | Source |
|---------|--------|
| "Show me all decisions made by this AI system in Q3" | Query audit trail by `use_case_id` and date range |
| "Reconstruct this specific AI interaction" | Look up by `request_id`; reconstruct full context |
| "Show me the model's performance over the last 12 months" | Aggregate evaluation metrics from monitoring data |
| "What guardrails were in place on this date?" | Guardrail configuration versioned and dated |
| "How was this model validated?" | Validation records linked to model version |
| "Who approved this system for production?" | Deployment gate approvals with signatures and dates |

---

## Monitoring the Audit Trail

The audit trail itself must be monitored:

| Check | Frequency | Alert |
|-------|-----------|-------|
| Completeness | Real-time | Missing audit records for processed requests |
| Integrity | Daily | Hash chain validation; detect tampering |
| Storage capacity | Weekly | Approaching storage limits |
| Access audit | Monthly | Unusual access patterns to audit data |
| Retention compliance | Quarterly | Records approaching retention expiry handled correctly |
