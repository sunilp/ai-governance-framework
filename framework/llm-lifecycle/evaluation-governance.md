# Evaluation Governance

## Overview

Evaluation is the primary mechanism for proving an AI system works as intended. Without standardized evaluation, governance is assertion without evidence. This document defines what to evaluate, when, what must pass, and what happens when it doesn't. It consolidates evaluation requirements previously scattered across monitoring, deployment gates, and prompt engineering standards.

---

## Evaluation Types

| Eval Type | What It Tests | When | T1 Suite Size | T2 | T3 | T4 |
|-----------|--------------|------|:---:|:---:|:---:|:---:|
| Pre-release | Domain accuracy, faithfulness, format compliance | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Safety | Toxicity, harmful content, jailbreak resistance, PII leakage | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Regression | Performance vs. previous version on identical test set | On model/prompt changes | Full suite | Full suite | 50 cases | N/A |
| RAG retrieval | Retrieval precision, recall, relevance, source attribution | Before deployment + weekly (T1) | 100+ | 50+ | 25+ | N/A |
| Red-team | Adversarial robustness | Per [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) cadence | 200+ | 100+ | 50 | 20 |
| Bias | Counterfactual fairness, demographic parity | Before deployment + quarterly (T1) | 200 pairs | 100 pairs | 50 pairs | N/A |
| Production | Ongoing output quality on sampled live traffic | Continuous per tier | Every response (async) | 20% sample | 5% sample | Weekly batch |

---

## Threshold Definitions by Tier

| Metric | T1 | T2 | T3 | T4 |
|--------|:---:|:---:|:---:|:---:|
| Hallucination rate | ≤ 1% | ≤ 3% | ≤ 5% | ≤ 10% |
| Faithfulness (RAG) | ≥ 90% | ≥ 85% | ≥ 80% | ≥ 75% |
| Safety pass rate | ≥ 99% | ≥ 97% | ≥ 95% | ≥ 90% |
| Retrieval precision@5 | ≥ 85% | ≥ 80% | ≥ 75% | N/A |
| Counterfactual consistency | ≥ 90% | ≥ 85% | ≥ 80% | N/A |
| Domain accuracy | Use-case specific (defined in risk assessment) | Same | Same | Same |

These are opinionated defaults. Organizations should calibrate to their domain and risk appetite. The principle is non-negotiable: every tier has thresholds, and thresholds are enforced.

---

## Release Criteria by Tier

| Tier | Required Evals | Reviewer | Sign-off |
|------|---------------|----------|----------|
| T1 | All eval types pass | Independent reviewer validates results | AI Risk sign-off |
| T2 | Pre-release + safety + regression + bias pass | Peer review of results | AI lead sign-off |
| T3 | Pre-release + safety pass | Self-attested | Team lead sign-off |
| T4 | Pre-release pass | Self-attested | Self-attested |

---

## Eval Dataset Governance

- Eval datasets versioned and access-controlled (same rigor as code)
- No overlap between eval data and training/fine-tuning data (data leakage invalidates evals)
- Eval datasets reviewed for representativeness and bias annually (T1/T2)
- Multiple independent eval sets for T1 (prevent overfitting to a single benchmark)
- Eval data containing PII handled per data governance policy

---

## Eval Infrastructure Requirements

- Eval results stored immutably (append-only, tamper-evident) — this is audit evidence
- Results linked to: model version, prompt version, dataset version, evaluator identity
- Automated eval pipeline for T1/T2 (CI/CD integrated; manual acceptable for T3/T4)
- Eval failures automatically block deployment pipeline for T1/T2
- Historical eval results retained for trending and regression detection (minimum 2 years)

---

## LLM-as-Judge Calibration

- When using LLM-as-judge for automated evaluation: calibrate against human evaluators quarterly (T1), semi-annually (T2)
- Document the correlation between LLM-as-judge scores and human scores
- If correlation drops below 0.85: pause automated eval; recalibrate or revert to human eval
- Never use LLM-as-judge as the sole evaluator for safety-critical metrics (T1 hallucination, PII leakage)

---

## Anti-patterns

- Running evals only at initial deployment, never again
- Using the same eval set for development tuning and release validation (data leakage)
- Setting thresholds so low they never fail (governance theater)
- Treating LLM-as-judge scores as ground truth without human calibration
- Evaluating only accuracy, ignoring safety, bias, and retrieval quality
- Reporting averages without per-segment breakdowns (hides demographic performance gaps)

---

## Integration

- Red-team eval references [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) — this file owns "what must pass"; red-teaming owns "how to test"
- Production eval cadence aligned with [LLM monitoring](monitoring.md)
- Control register IDs (EV-001 through EV-007) assigned — one per eval type
- Eval report is a required artifact in the deployment evidence pack (see [governance-workflow.md](../governance-operations/governance-workflow.md) Stage 7)
