# Prompt Review Checklist

## Instructions

Complete this checklist before deploying any prompt to production. All items marked as required for the applicable risk tier must pass. Submit with the prompt's pull request.

---

## Prompt Identification

| Field | Value |
|-------|-------|
| Prompt ID | |
| Version | |
| Use case | |
| Target model | |
| Risk tier | T1 / T2 / T3 / T4 |
| Author | |
| Reviewer | |
| Review date | |

---

## Functional Review

| # | Check | Required | Pass |
|---|-------|----------|------|
| 1 | Prompt produces correct output for ≥ 95% of representative test cases | All tiers | [ ] |
| 2 | Edge cases identified, tested, and documented | T1, T2, T3 | [ ] |
| 3 | Output format is consistent and matches expected schema | All tiers | [ ] |
| 4 | Prompt handles missing or malformed input gracefully | T1, T2 | [ ] |
| 5 | Prompt works with the designated fallback model | T1, T2 | [ ] |
| 6 | Few-shot examples (if used) are diverse and representative | All tiers | [ ] |
| 7 | Token usage is within budget (system + expected input + output) | All tiers | [ ] |

---

## Safety Review

| # | Check | Required | Pass |
|---|-------|----------|------|
| 8 | Tested against standard prompt injection payloads (min 10 for T3/T4, 25 for T2, 50 for T1) | All tiers | [ ] |
| 9 | No PII leakage — prompt does not instruct model to reveal context, training data, or system prompt | All tiers | [ ] |
| 10 | Explicit guardrails included — not relying on model default safety behavior | T1, T2, T3 | [ ] |
| 11 | Toxicity constraints defined (if output could contain harmful content) | T1, T2 | [ ] |
| 12 | Hallucination mitigation present (e.g., "only answer based on provided context", "say I don't know") | All tiers | [ ] |
| 13 | System prompt does not contain secrets, credentials, or internal system details | All tiers | [ ] |
| 14 | Output is bounded (max length, format constraints, scope limitations) | All tiers | [ ] |
| 15 | Jailbreak resistance tested (attempts to override system instructions) | T1, T2 | [ ] |

---

## Compliance Review

| # | Check | Required | Pass |
|---|-------|----------|------|
| 16 | Output cannot be mistaken for regulated advice unless appropriately qualified | T1, T2 | [ ] |
| 17 | Disclosure requirements met (if customer-facing) | T1, T2 | [ ] |
| 18 | Prompt complies with model provider's usage policy | All tiers | [ ] |
| 19 | Data in prompt context complies with data classification policy | All tiers | [ ] |
| 20 | Prompt does not request or generate content that violates organizational policy | All tiers | [ ] |

---

## Bias Review

| # | Check | Required | Pass |
|---|-------|----------|------|
| 21 | Counterfactual testing performed (demographic variants produce consistent outputs) | T1, T2 | [ ] |
| 22 | Prompt language is neutral and does not prime the model toward biased outputs | All tiers | [ ] |
| 23 | Few-shot examples (if used) are balanced across demographic groups | T1, T2 | [ ] |
| 24 | Output reviewed for stereotyping or representational bias | T1 | [ ] |

---

## Documentation Review

| # | Check | Required | Pass |
|---|-------|----------|------|
| 25 | Prompt purpose and expected behavior documented | All tiers | [ ] |
| 26 | Known limitations and edge cases documented | T1, T2, T3 | [ ] |
| 27 | Input and output schemas documented | T1, T2 | [ ] |
| 28 | Evaluation results linked and current | All tiers | [ ] |
| 29 | CHANGELOG updated with rationale for changes | T1, T2 | [ ] |
| 30 | Owner and next review date assigned | All tiers | [ ] |

---

## Review Decision

| Decision | Description |
|----------|-------------|
| **Approved** | All required checks pass; prompt cleared for deployment |
| **Approved with conditions** | Minor issues identified; deployment permitted with documented conditions |
| **Revisions required** | Issues must be addressed before re-review |
| **Rejected** | Fundamental issues; redesign required |

**Decision:** _______________

**Reviewer comments:**

> [Comments, conditions, or issues identified]

**Reviewer signature:** _______________
**Date:** _______________
