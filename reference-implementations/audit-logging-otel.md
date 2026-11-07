# Audit Logging With OpenTelemetry

**Purpose:** Map the framework's [per-request audit record](../framework/compliance/prompt-audit-trail.md#per-request-audit-record) and [agent action audit record](../framework/compliance/prompt-audit-trail.md#agent-action-audit-record) to the OpenTelemetry semantic conventions for generative AI, so teams that already instrument with OpenTelemetry can produce PM-007 evidence from the same telemetry without losing what the audit trail needs.

**Version checked.** Attribute names below were checked on 2026-11-07 against the [OpenTelemetry GenAI semantic conventions repository](https://github.com/open-telemetry/semantic-conventions-genai) (main branch, commit e6658f1, 2026-11-06), where the GenAI conventions now live; the pages in the main semantic-conventions repository are marked as moved. General attributes (`user.id`, `error.type`, `service.name`) are from the [main attribute registry](https://github.com/open-telemetry/semantic-conventions/tree/main/docs/registry/attributes). Every GenAI attribute is at **Development** stability, so names can still change. Pin the conventions version your instrumentation emits, record it with the system's configuration, and re-check this mapping on every upgrade.

---

## Four Rules Before the Mapping

1. **Telemetry is not the audit trail.** The framework's audit trail is append-only, tamper-evident and separate from application logs ([logging architecture](../framework/compliance/prompt-audit-trail.md#logging-architecture)). Use OpenTelemetry to carry correlation IDs and metadata, and write the audit record to the audit store. An observability backend that operators can edit, sample or expire does not meet PM-007 on its own.
2. **Keep content out of general telemetry.** Prompt, response, retrieved document and tool argument attributes are Opt-In in the conventions, and the conventions warn that they are likely to contain personal data. Store the content in the audit store and put the matching `*_ref` attribute (an absolute URI into external storage) on the span: `gen_ai.input.messages_ref`, `gen_ai.output.messages_ref`, `gen_ai.system_instructions_ref`, `gen_ai.tool.definitions_ref`. The [PII rules for audit logs](../framework/compliance/prompt-audit-trail.md#pii-in-audit-logs) then apply in one place.
3. **Never sample audit records.** Traces are often sampled; PM-007 needs a record for every request and every agent action. Write audit records through an unsampled path, and reconcile the count of audit records with the count of inference and tool spans as the completeness check.
4. **Use your own namespace for the gaps.** Where no convention exists (marked "none" below), add attributes under a namespace your organisation owns, such as `acme.audit.*`, and list them in the system's logging design so the PM-007 test knows where to look.

## Per-Request Audit Record

Spans: the inference span (`gen_ai.operation.name` = `chat`, `generate_content` or `text_completion`; span name `{gen_ai.operation.name} {gen_ai.request.model}`) and, for RAG, a retrieval span (`gen_ai.operation.name` = `retrieval`).

| Framework field | OpenTelemetry | Notes |
|---|---|---|
| `request_id` | Trace ID and the root span ID; none for an application request ID | Also record `gen_ai.response.id`, the provider's ID for the completion, which the vendor can trace |
| `timestamp` | Span start time | |
| `user_id` | `user.id` | Pseudonymise before it leaves the application |
| `session_id` | `gen_ai.conversation.id` | |
| `use_case_id` | None; `service.name` names the service | Record the AI inventory ID in your namespace |
| `system_prompt` | `gen_ai.system_instructions_ref` (`gen_ai.system_instructions` is Opt-In) | T1, T2 |
| `system_prompt_version` | `gen_ai.prompt.name`, `gen_ai.prompt.version` | Conditionally required by the conventions when a named prompt template is used |
| `user_input` | `gen_ai.input.messages_ref` (`gen_ai.input.messages` is Opt-In) | |
| `retrieved_context` | Retrieval span: `gen_ai.retrieval.documents` (Opt-In; an `id` and `score` per document), `gen_ai.data_source.id`, `gen_ai.retrieval.top_k` | T1, T2 if RAG. Store the chunk text in the audit store, keyed by document ID |
| `retrieval_scores` | `score` within `gen_ai.retrieval.documents` | T1 if RAG |
| `model_id` | `gen_ai.provider.name`, `gen_ai.request.model`, `gen_ai.response.model` | The response model shows the version actually served, which matters for vendor model changes |
| `model_parameters` | `gen_ai.request.temperature`, `gen_ai.request.top_p`, `gen_ai.request.top_k`, `gen_ai.request.max_tokens`, `gen_ai.request.seed`, `gen_ai.request.stop_sequences` | T1, T2 |
| `raw_response` | `gen_ai.output.messages_ref` on the inference span (`gen_ai.output.messages` is Opt-In); `gen_ai.response.finish_reasons` | T1, T2. This is the model output before guardrails |
| `processed_response` | None | The post-guardrail output is application-level. Record a reference on the application span |
| `guardrail_actions` | None | Record each trigger and action as attributes or span events on a guardrail span |
| `token_count_input`, `token_count_output` | `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens` | |
| `latency_ms` | Span duration; metric `gen_ai.client.inference.duration` | |
| `user_feedback` | None | |
| `error_details` | `error.type` and span status; event `gen_ai.client.inference.exception` | |

Online scoring results (PM-004) fit the `gen_ai.evaluation.result` event, which carries `gen_ai.evaluation.name`, `gen_ai.evaluation.score.value`, `gen_ai.evaluation.score.label` and `gen_ai.evaluation.explanation`. That lets the production hallucination monitor and the audit record share one correlation ID.

For the [per-session record](../framework/compliance/prompt-audit-trail.md#per-session-audit-record-conversational-systems), `session_id` maps to `gen_ai.conversation.id`; turn count, escalation and outcome have no convention.

## Agent Action Audit Record

One record per tool call, delegation, memory write and inter-agent message ([agent identity and tool governance](../framework/llm-lifecycle/agent-identity-and-tool-governance.md#9-agent-action-audit-record)). Spans: `execute_tool` (span name `execute_tool {gen_ai.tool.name}`), `invoke_agent`, and the memory operations.

| Framework field | OpenTelemetry | Notes |
|---|---|---|
| `action_id` | Span ID of the action span; `gen_ai.tool.call.id` where the model or provider supplied one | |
| `request_id` | Trace ID, and the parent span | |
| `correlation_id` | Trace ID, kept across agents only if every hop propagates trace context; `gen_ai.conversation.id` | Across A2A, MCP or queue boundaries that drop trace context, carry a correlation ID explicitly in your namespace |
| `action_type` | `gen_ai.operation.name`: `execute_tool` (tool call), `invoke_agent` (delegation or call to another agent), `create_memory`, `update_memory`, `upsert_memory`, `delete_memory` (memory writes) | Inter-agent messages over A2A add `a2a.method.name`, `a2a.task.id`, `a2a.message.id`; MCP calls add `mcp.method.name`, `mcp.session.id` |
| `agent_id` | `gen_ai.agent.id`, `gen_ai.agent.name`, `gen_ai.agent.version` | The conventions define `gen_ai.agent.id` as the stable ID of the agent resource (provider-assigned for hosted agents). Also record the ID from the agent identity record (AR-006) in your namespace |
| `principal_id` | `user.id` when the principal is a user; none for a system principal or an agent acting on its own authority | |
| `delegation_chain` | None | Record each hop with its grant or token reference and scope, never the token itself |
| `tool` | `gen_ai.tool.name`, `gen_ai.tool.type`, `gen_ai.tool.description`; `gen_ai.tool.definitions_ref` | Tool version and definition hash have no convention |
| `arguments_hash` | None | Hash the full arguments before redaction |
| `arguments_redacted` | `gen_ai.tool.call.arguments` (Opt-In) | Only after redaction; full values stay in the audit store under the PII controls |
| `authorisation_decision` | None | Record on an authorisation child span: allowed or denied, the deciding policy, cap and rate-limit results |
| `approval_reference` | None | |
| `result` | `gen_ai.tool.call.result` (Opt-In); `error.type` on failure | Records affected and value moved have no convention |
| `timestamp_requested`, `timestamp_decided`, `timestamp_completed` | Action span start; end of the authorisation child span; action span end | |
| `error_details` | `error.type`; event `gen_ai.execute_tool.exception` | |

Memory writes can add `gen_ai.memory.store.id` and `gen_ai.memory.record.id`.

## What This Gives PM-007

- **Completeness:** reconcile audit records against inference and `execute_tool` span counts per day, and against agent action counts per trace.
- **Reconstruction:** from a complaint or incident, the trace ID leads to every span, and the `*_ref` attributes lead to the stored content, which is what [decision reconstruction](../framework/compliance/prompt-audit-trail.md#reconstruction-capability) and IR-004 post-mortems need.
- **Gaps to close:** guardrail actions, the processed response, delegation chain, authorisation decision, approval reference and the inventory ID have no convention. They are the fields regulators and auditors ask for first, so design them explicitly.

## Sources

- [GenAI semantic conventions overview](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/README.md)
- [GenAI attribute registry](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/gen-ai.md)
- [Client inference spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/client-inference.md), [execute tool spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/execute-tool.md), [retrieval spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/retrieval.md), [agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md), [events](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-events.md)
- [MCP attributes](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/mcp.md), [A2A attributes](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/a2a.md)
- [User](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/attributes/user.md), [error](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/attributes/error.md) and [service](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/attributes/service.md) attributes in the main registry
