# Evaluation Governance

## Overview

Evaluation is the primary mechanism for proving an AI system works as intended. Without standardized evaluation, governance is assertion without evidence. This document defines what to evaluate, when, what must pass, and what happens when it doesn't. It consolidates evaluation requirements previously scattered across monitoring, deployment gates, and prompt engineering standards.

---

## Evaluation Types

<!-- BEGIN GENERATED: evaluation-types. Edit policy/thresholds.yaml, then run python tools/build.py -->

| Eval Type | What It Tests | When | T1 Suite Size | T2 | T3 | T4 |
|-----------|--------------|------|:---:|:---:|:---:|:---:|
| Pre-release | Domain accuracy, faithfulness, format compliance | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Safety | Toxicity, harmful content, jailbreak resistance, PII leakage | Before every deployment | 200+ | 100+ | 50+ | 20+ |
| Regression | Performance vs. previous version on identical test set | On model/prompt changes | Full suite | Full suite | 50 cases | N/A |
| RAG retrieval | Retrieval precision, recall, relevance, source attribution | Before deployment, then weekly (T1), monthly (T2), quarterly (T3) | 100+ | 50+ | 25+ | Recommended |
| Red-team | Adversarial robustness | Before deployment, then per [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) cadence | 200+, including manual testing (external testers recommended) | 100+ | Automated adversarial scan + 50 manual cases | Automated scan, 20+ cases (recommended) |
| Bias | Counterfactual fairness, demographic parity | Formal bias evaluation before deployment, then quarterly (T1), semi-annual (T2) | 200 pairs | 100 pairs | 50 pairs | N/A |
| Production | Ongoing output quality on live traffic | Continuous: three activities, see [Production Evaluation](#production-evaluation) | Every response scored (async) | 20% sample | 5% sample | Weekly batch sample |

<!-- END GENERATED: evaluation-types -->

Suite sizes apply whenever an eval type is run. Which eval types must pass before release at each tier is set in [Release Criteria by Tier](#release-criteria-by-tier).

---

## Threshold Definitions by Tier

<!-- BEGIN GENERATED: threshold-definitions. Edit policy/thresholds.yaml, then run python tools/build.py -->

| Metric | T1 | T2 | T3 | T4 |
|--------|:---:|:---:|:---:|:---:|
| Hallucination rate | ≤ 1% | ≤ 3% | ≤ 5% | ≤ 10% |
| Faithfulness (RAG) | ≥ 90% | ≥ 85% | ≥ 80% | ≥ 75% |
| Safety pass rate | ≥ 99% | ≥ 97% | ≥ 95% | ≥ 90% |
| Retrieval precision@5 | ≥ 85% | ≥ 80% | ≥ 75% | N/A |
| Counterfactual consistency | ≥ 90% | ≥ 85% | ≥ 80% | N/A |
| Domain accuracy | Use-case specific (defined in risk assessment) | Same | Same | Same |

<!-- END GENERATED: threshold-definitions -->

These are opinionated defaults. Organizations should calibrate to their domain and risk appetite. The principle is non-negotiable: every tier has thresholds, and thresholds are enforced.

This document is the single source for these thresholds and for suite sizes. Other documents link here rather than restating different values. Use-case tolerances (for example in [hallucination-policy.md](../responsible-ai/hallucination-policy.md)) apply only when they are stricter than the tier threshold.

---

## Metric Definitions

<!-- BEGIN GENERATED: metric-definitions. Edit policy/thresholds.yaml, then run python tools/build.py -->

| Metric | Definition |
|--------|-----------|
| Hallucination rate | Share of evaluated responses that contain at least one material unsupported or false claim. Measured at response level. A claim is material if a user could act on it: facts, figures, policy terms, fees, dates, eligibility. |
| Faithfulness | Average share of claims in a response that are supported by the retrieved context. Measured at claim level. Faithfulness and hallucination rate measure different things and both thresholds apply: a response with high faithfulness still counts as a hallucination if its one unsupported claim is material. |
| Safety pass rate | Share of safety test cases where the system responds acceptably. Each test case defines the acceptable response (for example, a refusal, a safe completion, or no PII in the output). |
| Retrieval precision@5 | Share of the top 5 retrieved chunks that are relevant to the query, averaged across evaluation queries. Relevance is judged against labelled references or by a calibrated LLM-as-judge. |
| Counterfactual consistency | Share of counterfactual pairs (prompts identical except for a demographic attribute) whose outputs are consistent: same substance and conclusion, comparable sentiment and level of detail. Test protocol: [bias-detection-llm.md](../responsible-ai/bias-detection-llm.md). |

<!-- END GENERATED: metric-definitions -->

---

## Release Criteria by Tier

| Tier | Required Evals | Reviewer | Sign-off |
|------|---------------|----------|----------|
| T1 | All eval types pass: pre-release, safety, regression, RAG retrieval (if RAG), bias, red-team | Full independent validation by Model Risk Management (MRM) | AI Risk sign-off |
| T2 | Pre-release + safety + regression + bias + RAG retrieval (if RAG) + red-team | Independent validation, reduced scope, by a qualified reviewer outside the development team (MRM or second line) | AI lead sign-off |
| T3 | Pre-release + safety + RAG retrieval (if RAG) + red-team (automated scan + 50 manual cases) | Peer review | Team lead sign-off |
| T4 | Pre-release + safety (automated, 20+ cases each). RAG retrieval eval and red-team scan recommended | Self-test | Self-attested |

The team that builds a T1 or T2 system never validates its own evaluation results.

---

## Production Evaluation

Production evaluation is three named activities (control PM-004):

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| 1. Online automated scoring of live traffic | Every response (async) | 20% sample | 5% sample | Weekly batch sample |
| 2. Metrics review | Daily dashboard check by AI Operations, plus monthly system-owner review | Weekly | Monthly | Quarterly |
| 3. Full offline suite re-run | Monthly | Quarterly | Semi-annual | Semi-annual |

Always re-run the full offline suite on a model, provider or prompt change.

Related production checks with their own cadence:

- **RAG retrieval evaluation:** weekly (T1), monthly (T2), quarterly (T3); recommended for T4.
- **Production counterfactual spot-checks:** weekly (T1), monthly (T2). These are separate from the formal bias evaluation (before deployment, then quarterly for T1 and semi-annual for T2). See [bias-detection-llm.md](../responsible-ai/bias-detection-llm.md).
- **Vendor behaviour canary:** for third-party models, a fixed domain set run daily (T1), weekly (T2), monthly (T3/T4) to detect silent vendor model changes. See [third-party-model-risk.md](../compliance/third-party-model-risk.md#ongoing-monitoring).
- **Prompt-change adversarial regression set:** at least 50 cases for T1/T2, re-run on every prompt change. This is separate from the pre-release red-team. See [prompt-engineering-standards.md](prompt-engineering-standards.md#minimum-evaluation-suite-size).

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
- Evaluation results are governance records: retain them for the life of the system plus the tier retention period, per [audit-trail-requirements.md](../compliance/audit-trail-requirements.md). Historical results also support trending and regression detection.

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
- Control register IDs ([control-register.md](../governance-operations/control-register.md)): pre-release EV-001, safety EV-002, regression EV-003, RAG retrieval EV-004, bias EV-005, red-team SR-001, production PM-004. EV-006 covers eval dataset integrity and EV-007 covers LLM-as-judge calibration.
- Eval report is a required artifact in the deployment evidence pack (see [governance-workflow.md](../governance-operations/governance-workflow.md) Stage 7)
