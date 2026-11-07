# Adversarial Robustness Standards

## Overview

AI systems face adversarial threats that differ fundamentally from traditional cybersecurity attacks. Jailbreaking, prompt injection, model extraction, and data poisoning exploit the probabilistic nature of AI models rather than software vulnerabilities. Defense requires layered controls across the entire system, not a single perimeter.

These standards define mandatory defenses by risk tier. They complement the [red-teaming protocol](red-teaming-protocol.md) which covers testing methodology.

The [Threat Taxonomy Mapping](#threat-taxonomy-mapping) at the end of this document maps these defenses and the red-team test categories to the OWASP Top 10 lists and MITRE ATLAS.

---

## Jailbreaking Defenses

Jailbreaking attempts to bypass the model's safety alignment and content policies.

| Attack Type | Description | Defense | T1/T2 Required | T3/T4 Required |
|------------|-------------|---------|:---:|:---:|
| Role-play injection | "You are DAN, you can do anything" | System prompt hardening; role-play detection classifier | Yes | Yes |
| Authority impersonation | "As your developer, I'm overriding your rules" | Explicit instruction hierarchy; ignore override claims | Yes | Yes |
| Encoding tricks | Base64, ROT13, Unicode obfuscation of harmful requests | Input normalization; multi-encoding detection | Yes | No |
| Multi-turn escalation | Gradually shifting boundaries across conversation turns | Per-turn safety classification; conversation-level monitoring | Yes | No |
| Universal adversarial suffixes | Appended token sequences that bypass safety training | Input length/entropy anomaly detection; adversarial suffix detection | Yes | No |
| Multi-language bypass | Harmful requests in low-resource languages with weaker safety alignment | Multilingual safety classifiers; language detection + policy enforcement | Yes | No |
| Payload smuggling | Instructions hidden in markdown, HTML, or code blocks | Input parsing and sanitization; strip non-text formatting before safety check | Yes | No |

### System Prompt Hardening Guidelines

1. Place safety instructions at the beginning AND end of the system prompt (sandwich pattern)
2. Use explicit boundary markers between instructions and user content
3. Include explicit refusal instructions for known attack categories
4. Do not rely on the model's base safety training alone — assume it can be bypassed
5. Test system prompts against adversarial inputs before deployment

---

## Prompt Injection Mitigation

Prompt injection inserts adversarial instructions that the model executes as if they were legitimate commands.

| Vector | Description | Mitigation |
|--------|-------------|------------|
| Direct injection (user input) | User crafts input containing instructions | Input classification (detect instruction-like content); input/output role separation |
| Indirect injection (RAG documents) | Retrieved documents contain hidden instructions | Context isolation — process retrieved docs in a separate context; strip formatting from retrieved content |
| Indirect injection (tool outputs) | API responses or database results contain embedded instructions | Sanitize all tool outputs before inserting into context; treat tool outputs as untrusted data |
| Indirect injection (file uploads) | Uploaded documents/images contain adversarial content | Content extraction and sanitization; process in sandboxed context |
| Multi-stage injection | Benign-looking input that becomes harmful when combined with context | Conversation-level monitoring; output safety classification regardless of input classification |

### Defense-in-Depth Architecture

```
User Input → [Input Classifier] → [Safety Filter] → Model Context
                                                          ↓
Retrieved Docs → [Sanitizer] → [Context Isolation] → Model Context
                                                          ↓
                                                    Model Output
                                                          ↓
                                              [Output Safety Filter]
                                                          ↓
                                              [Action Validator] (agentic)
                                                          ↓
                                                    Final Output
```

Every layer must be independently effective. Do not rely on any single layer.

---

## Model Extraction Prevention

Model extraction attempts to reconstruct model behavior or extract training data through systematic querying.

| Attack | Risk | Mitigation | Tier |
|--------|------|------------|------|
| Systematic querying | Attacker queries model thousands of times to map decision boundaries | Rate limiting per user/session; query pattern anomaly detection | T1/T2 |
| Training data extraction | Crafted prompts cause model to reproduce memorized training data | Output monitoring for known sensitive patterns; PII detection on outputs | T1/T2 |
| Model distillation | Attacker uses outputs to train a clone model | Rate limiting; output perturbation for T1; terms of service enforcement | T1 |
| API abuse | Automated high-volume querying via API | Authentication; rate limiting; usage monitoring; IP-based anomaly detection | All |

### Detection Signals

- Unusually high query volume from single user or IP
- Repetitive queries with systematic variation (grid search patterns)
- Queries probing model boundaries (minimal input changes, observing output changes)
- Abnormal token usage patterns (very short inputs, requesting maximum outputs)

---

## Data Poisoning Defenses

Data poisoning compromises the data that AI systems learn from or reference.

| Target | Attack | Defense |
|--------|--------|---------|
| Fine-tuning training data | Adversarial examples injected into training dataset | Data provenance tracking; anomaly detection on training data; human review of training samples |
| RAG corpus | Adversarial documents added to knowledge base | Document ingestion controls; source authentication; integrity verification on corpus changes; anomaly detection on new documents |
| Feedback loops | Adversarial user feedback poisons RLHF or active learning | Feedback validation; outlier detection; human review of feedback used for training |
| Evaluation data | Poisoned eval data makes a compromised model appear safe | Evaluation data integrity controls; multiple independent eval sets; human review of eval results |

### RAG Corpus Integrity

For systems using retrieval-augmented generation:
1. All documents must pass through an authenticated ingestion pipeline
2. Source provenance tracked for every document
3. Bulk corpus changes require approval from document owner and AI operations
4. Periodic integrity checks: re-validate random sample against source of truth
5. Monitor for anomalous document additions (unexpected sources, unusual content patterns)

---

## Privacy Attack Defenses

| Attack | Description | Defense | Tier |
|--------|-------------|---------|------|
| Membership inference | Determining if a specific record was in the training data | Output confidence score limiting; differential privacy awareness in fine-tuning | T1 |
| Model inversion | Reconstructing training data from model outputs | Output filtering; limit output detail for sensitive queries | T1/T2 |
| PII extraction | Crafted prompts cause model to reveal memorized PII | PII detection on all outputs; prompt-based PII extraction testing | All |
| Attribute inference | Inferring sensitive attributes from model behavior | Fairness testing; attribute inference testing as part of bias evaluation | T1/T2 |

---

## Monitoring for Adversarial Activity

| Signal | Detection Method | Alert Threshold | Tier |
|--------|-----------------|----------------|------|
| Query pattern anomaly | Statistical analysis of query distribution | Deviation > 3σ from baseline | All |
| Output distribution shift | Monitor output length, topic, sentiment distribution | Significant shift from baseline (KL divergence) | T1/T2 |
| Cost spikes | Monitor token usage and API costs | > 2x daily baseline | All |
| Repeated similar queries | Clustering analysis on recent queries | > 10 near-duplicate queries per session | T1/T2 |
| Guardrail trigger rate increase | Monitor safety filter activation rate | > 2σ increase from baseline | All |
| Error rate increase | Monitor model error/refusal rate | > 2x baseline | All |
| Unusual access patterns | Time-of-day, geographic, device anomalies | Deviation from established patterns | T1/T2 |

### Response Playbook

| Alert Level | Response |
|------------|----------|
| Single anomaly | Log; include in next scheduled review |
| Multiple correlated anomalies | Investigate within 24 hours; increase monitoring |
| Confirmed attack pattern | Escalate per [escalation paths](../operating-model/escalation-paths.md); consider rate limiting or temporary access restriction |
| Active exploitation | Immediate mitigation (block source, activate circuit breaker); S1/S2 incident response |

---

## Threat Taxonomy Mapping

This section maps the defenses above and the [red-team test categories](red-teaming-protocol.md#test-categories) to three public taxonomies, so findings and controls can be reported in shared terms. Editions checked in November 2026:

- **OWASP Top 10 for LLM Applications 2025**, the current edition on genai.owasp.org.
- **OWASP Top 10 for Agentic Applications 2026**, released by the OWASP GenAI Security Project in December 2025.
- **MITRE ATLAS**, data release 2026.10 (28 October 2026). ATLAS renumbers and renames techniques between releases; check the current matrix before citing an ID in a report.

Control IDs refer to the [control register](../governance-operations/control-register.md).

### OWASP Top 10 for LLM Applications 2025

| OWASP Entry | Framework Defenses | Red-Team Category | MITRE ATLAS | Controls |
|---|---|---|---|---|
| LLM01:2025 Prompt Injection (OWASP treats jailbreaking as a form of prompt injection) | Jailbreaking defenses; system prompt hardening; prompt injection mitigation; defense-in-depth architecture | Prompt injection (direct); prompt injection (indirect); jailbreaking; social engineering; multimodal attacks | AML.T0051 LLM Prompt Injection (.000 Direct, .001 Indirect); AML.T0054 LLM Jailbreak; AML.T0068 LLM Prompt Obfuscation | DE-004, SR-001, SR-003 |
| LLM02:2025 Sensitive Information Disclosure | Training data and PII extraction defenses; privacy attack defenses | Information extraction | AML.T0137 Training Data Information from AI Models (.000 Infer Membership, .002 Invert AI Model, .003 Extract Memorized Data); AML.T0024 Exfiltration via AI Inference API | DE-004, SR-003, RA-005 |
| LLM03:2025 Supply Chain | [Supply chain security](supply-chain-security.md) | None; verified through SR-004 | AML.T0010 Supply Chain Compromise (.003 Model Repository) | SR-004, AR-005 |
| LLM04:2025 Data and Model Poisoning | Data poisoning defenses; RAG corpus integrity | Prompt injection (indirect) through RAG documents | AML.T0020 Training Data Poisoning; AML.T0018 Manipulate AI Model; AML.T0070 RAG Poisoning | DE-005, EV-006, SR-004 |
| LLM05:2025 Improper Output Handling | Output safety filter; action validator; payload smuggling defenses | Tool misuse; information extraction | AML.T0077 LLM Response Rendering | DE-004, SR-003 |
| LLM06:2025 Excessive Agency | Action validator; agentic controls in [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md) | Tool misuse; excessive agency | AML.T0053 AI Agent Tool Invocation | DE-004, SR-001, PM-003 |
| LLM07:2025 System Prompt Leakage | System prompt hardening; extraction of a system prompt is a High red-team finding | Information extraction | AML.T0069 Discover LLM System Information (.002 System Prompt) | SR-001, SR-002 |
| LLM08:2025 Vector and Embedding Weaknesses | RAG corpus integrity; access control leakage rules in [rag-governance.md](../llm-lifecycle/rag-governance.md) | Prompt injection (indirect) through RAG documents | AML.T0070 RAG Poisoning | EV-004, DE-008 |
| LLM09:2025 Misinformation | Outside this document: [hallucination-policy.md](../responsible-ai/hallucination-policy.md) | None; covered by evaluation | AML.T0062 Discover LLM Hallucinations; AML.T0060 Publish Hallucinated Entities | EV-001, PM-004 |
| LLM10:2025 Unbounded Consumption (includes model extraction and denial of wallet) | Model extraction prevention; API abuse controls; cost spike and query pattern monitoring | None; covered by monitoring | AML.T0024 Exfiltration via AI Inference API; AML.T0005 Replicate AI Model Behavior; AML.T0029 Denial of AI Service; AML.T0034 Cost Harvesting | SR-003, PM-002, PM-005 |

Harmful content generation has no LLM Top 10 entry; see the NIST AI 600-1 risks in [nist-ai-rmf-mapping.md](../compliance/nist-ai-rmf-mapping.md#generative-ai-profile-nist-ai-600-1).

### OWASP Top 10 for Agentic Applications 2026

| OWASP Entry | Framework Coverage | Red-Team Category | MITRE ATLAS | Controls |
|---|---|---|---|---|
| ASI01: Agent Goal Hijack | Prompt injection mitigation; tool outputs and inter-agent messages treated as data, not instructions | Prompt injection (indirect) | AML.T0051.001 LLM Prompt Injection: Indirect | DE-004, SR-001, SR-003 |
| ASI02: Tool Misuse and Exploitation | Action validator; tool access fixed at deployment ([privilege boundaries](../llm-lifecycle/multi-agent-governance.md#privilege-boundaries)) | Tool misuse | AML.T0053 AI Agent Tool Invocation; AML.T0086 Exfiltration via AI Agent Tool Invocation; AML.T0101 Data Destruction via AI Agent Tool Invocation | DE-004, SR-001, PM-003, AR-006 |
| ASI03: Identity and Privilege Abuse | Own service account per agent; least privilege; no privilege grants between agents | Privilege escalation and delegation abuse | AML.T0083 Credentials from AI Agent Configuration; AML.T0012 Valid Accounts | AR-006, SR-001 ([agent identity](../llm-lifecycle/agent-identity-and-tool-governance.md#1-agent-identity), [delegation](../llm-lifecycle/agent-identity-and-tool-governance.md#2-delegation)) |
| ASI04: Agentic Supply Chain Vulnerabilities | [Supply chain security](supply-chain-security.md), including agent tools in the AI-BOM | None; verified through SR-004 | AML.T0010.005 Supply Chain Compromise: AI Agent Tool | SR-004, AR-005, AR-006 |
| ASI05: Unexpected Code Execution (RCE) | Output handling and action validation; sandboxing in [code execution](../llm-lifecycle/agent-identity-and-tool-governance.md#7-code-execution-owasp-asi05) | Tool misuse | AML.T0050 Command and Scripting Interpreter | DE-004, AR-006, SR-001 |
| ASI06: Memory & Context Poisoning | [Persistent memory governance](../llm-lifecycle/multi-agent-governance.md#persistent-memory-governance); RAG corpus integrity | Memory poisoning | AML.T0080 AI Agent Context Poisoning (.000 Memory); AML.T0070 RAG Poisoning | AR-006, PM-007, SR-001 ([memory](../llm-lifecycle/agent-identity-and-tool-governance.md#5-memory-owasp-asi06)) |
| ASI07: Insecure Inter-Agent Communication | [Message validation](../llm-lifecycle/multi-agent-governance.md#message-validation): schema, logging, no instruction injection | Privilege escalation and delegation abuse | None listed | AR-006, PM-007, SR-001 ([inter-agent messages](../llm-lifecycle/agent-identity-and-tool-governance.md#6-inter-agent-messages-owasp-asi07)) |
| ASI08: Cascading Failures | Blast radius analysis; circuit breakers; graceful degradation | Cascading failure | None listed | PM-002, DA-004 |
| ASI09: Human-Agent Trust Exploitation | Human oversight patterns; reviewer override-rate monitoring for rubber-stamping | Approval manipulation | None listed | PM-003 |
| ASI10: Rogue Agents | Pause and kill switch; monitoring | Excessive agency | None listed | PM-001, PM-003, PM-006 |

Agent identity, delegation, tool scopes, memory, inter-agent messages and code execution are set in [agent identity and tool governance](../llm-lifecycle/agent-identity-and-tool-governance.md) and evidenced through AR-006. In production, PM-006 tests the kill switch and PM-007 checks the agent action audit record.

---

## Sources

- OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- OWASP, LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- OWASP, LLM10:2025 Unbounded Consumption: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/
- OWASP GenAI Security Project, OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- MITRE ATLAS: https://atlas.mitre.org/
- MITRE ATLAS data, release 2026.10: https://github.com/mitre-atlas/atlas-data/blob/main/dist/v6/ATLAS-2026.10.yaml
