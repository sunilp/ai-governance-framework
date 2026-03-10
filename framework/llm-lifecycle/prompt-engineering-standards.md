# Prompt Engineering Standards

## Overview

Prompts are not code comments or ad hoc strings. In an enterprise LLM deployment, prompts are executable artifacts that directly determine system behavior, output quality, and risk exposure. They must be governed with the same rigor as application code.

This document defines organizational standards for prompt development, review, versioning, and lifecycle management.

---

## Core Principles

1. **Prompts are code.** Version-controlled, peer-reviewed, tested, deployed through CI/CD.
2. **Prompts are auditable.** Every prompt in production must be traceable to an approved version.
3. **Prompts are tested.** Every prompt must pass an evaluation suite before deployment.
4. **Prompts are documented.** Purpose, expected behavior, known limitations, and edge cases.
5. **Prompts are owned.** Every prompt has a designated owner accountable for its behavior.

---

## Prompt Development Standards

### Structure

All production prompts must follow a standard structure:

```
[SYSTEM CONTEXT]
Role definition, behavioral constraints, output format requirements.

[TASK INSTRUCTIONS]
Specific task description with clear success criteria.

[GUARDRAILS]
Explicit constraints: what the model must not do, topics to avoid,
escalation triggers.

[OUTPUT FORMAT]
Expected structure, schema, examples.

[FEW-SHOT EXAMPLES] (when applicable)
Representative input/output pairs demonstrating expected behavior.
```

### Naming Convention

```
{use-case}/{component}/{version}

Example: customer-service/complaint-classification/v2.3
Example: credit-analysis/memo-draft/v1.0
```

### Documentation Requirements

Each prompt must include:

| Field | Description |
|-------|-------------|
| `prompt_id` | Unique identifier |
| `version` | Semantic version (major.minor) |
| `owner` | Team and individual responsible |
| `purpose` | What this prompt does and why |
| `target_model` | Which model(s) this prompt is designed for |
| `input_schema` | Expected input variables and types |
| `output_schema` | Expected output format and constraints |
| `guardrails` | Safety constraints embedded in the prompt |
| `known_limitations` | Edge cases, failure modes, known weaknesses |
| `evaluation_results` | Link to most recent eval report |
| `approval_date` | Date of last review and approval |
| `next_review` | Scheduled review date |

---

## Prompt Review Process

### Review Checklist

Before a prompt enters production, it must pass the following review:

**Functional Review:**
- [ ] Prompt produces correct outputs for representative test cases
- [ ] Edge cases are tested and documented
- [ ] Output format is consistent and parseable (if structured)
- [ ] Prompt handles missing or malformed input gracefully

**Safety Review:**
- [ ] No prompt injection vulnerabilities (tested with standard injection payloads)
- [ ] No PII leakage — prompt does not instruct model to reveal training data or context
- [ ] Guardrails are explicit — not relying on model's default safety behavior
- [ ] Toxicity constraints are defined where applicable
- [ ] Hallucination mitigation is appropriate (e.g., "only answer based on provided context")

**Compliance Review:**
- [ ] Output cannot be mistaken for regulated advice (financial, legal, medical) unless appropriately qualified
- [ ] Disclosure requirements are met (if output is customer-facing)
- [ ] Prompt does not violate model provider's usage policy
- [ ] Data handling in prompt context complies with data classification policy

**Operational Review:**
- [ ] Token usage is within budget (system prompt + expected input + output)
- [ ] Latency is acceptable for the use case
- [ ] Prompt works with the fallback model (if T1/T2)

### Review Authority

| Tier | Reviewer |
|------|----------|
| T1 | Peer review + prompt engineering lead + security review + AI risk sign-off |
| T2 | Peer review + prompt engineering lead |
| T3 | Peer review |
| T4 | Self-review with documentation |

---

## Version Control

### Repository Structure

```
prompts/
├── {use-case}/
│   ├── {component}/
│   │   ├── prompt.yaml          # Current production prompt
│   │   ├── config.yaml          # Model, parameters, guardrail config
│   │   ├── eval/
│   │   │   ├── test_cases.yaml  # Evaluation test cases
│   │   │   └── results/         # Historical eval results
│   │   └── CHANGELOG.md         # Version history with rationale
```

### Versioning Rules

- **Major version (v1 → v2):** Behavioral change — different output characteristics, new guardrails, different model target. Requires full review.
- **Minor version (v1.0 → v1.1):** Refinement — improved phrasing, additional examples, minor guardrail adjustments. Requires peer review.
- **No unversioned changes.** Every prompt change creates a new version.

### Deployment

- Prompts deploy through the same CI/CD pipeline as application code
- Evaluation suite runs automatically on every prompt change (PR gate)
- Canary deployment for T1/T2: new prompt version serves a percentage of traffic, monitored before full rollout
- Rollback procedure: revert to previous version within defined SLA

---

## Prompt Evaluation

### Evaluation Dimensions

| Dimension | Metric | Method |
|-----------|--------|--------|
| Correctness | Accuracy against ground truth | Automated comparison with labeled test set |
| Faithfulness | Output grounded in provided context | LLM-as-judge or human evaluation |
| Consistency | Same input produces consistent outputs | Run N times, measure variance |
| Safety | Resistance to adversarial inputs | Adversarial test suite |
| Format compliance | Output matches expected schema | Automated schema validation |
| Latency | Response time | Automated measurement |
| Cost | Token usage | Automated measurement |

### Minimum Evaluation Suite Size

| Tier | Test Cases | Adversarial Tests |
|------|-----------|-------------------|
| T1 | ≥ 200 | ≥ 50 |
| T2 | ≥ 100 | ≥ 25 |
| T3 | ≥ 50 | ≥ 10 |
| T4 | ≥ 20 | ≥ 5 |

---

## Anti-Patterns

The following practices are prohibited in production prompt engineering:

1. **Hardcoded secrets in prompts.** Never include API keys, credentials, or internal system details in prompt text.
2. **Implicit safety reliance.** Do not assume the model will behave safely without explicit constraints. Always include guardrails.
3. **Copy-paste prompts.** Do not copy prompts between use cases without independent evaluation. A prompt optimized for one task may behave unpredictably in another context.
4. **Prompt-as-documentation.** Prompts should be supplemented with separate documentation. The prompt text alone is not sufficient documentation.
5. **Unbounded output.** Always constrain output length, format, or scope. Open-ended generation in production creates unpredictable behavior and cost.
6. **Over-prompting.** Excessively long system prompts consume tokens, increase cost, and can degrade model attention. Keep prompts as concise as possible while maintaining safety and quality.
