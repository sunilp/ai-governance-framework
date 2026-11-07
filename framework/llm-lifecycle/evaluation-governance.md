# Evaluation Governance

## Overview

Evaluation is the primary mechanism for proving an AI system works as intended. Without standardized evaluation, governance is assertion without evidence. This document defines what to evaluate, when, what must pass, how a pass is judged, and what happens when it doesn't. It consolidates evaluation requirements previously scattered across monitoring, deployment gates, and prompt engineering standards.

It covers GenAI systems, agentic systems and traditional ML. EV-001 applies to every system; the ML specifics are in [Traditional ML Systems](#traditional-ml-systems).

---

## Evaluation Types

<!-- BEGIN GENERATED: evaluation-types. Edit policy/thresholds.yaml, then run python tools/build.py -->

| Eval Type | What It Tests | When | T1 Suite Size | T2 | T3 | T4 |
|-----------|--------------|------|:---:|:---:|:---:|:---:|
| Pre-release | Domain accuracy, faithfulness, format compliance | Before every deployment | 300+ | 100+ | 50+ | 20+ |
| Safety | Toxicity, harmful content, jailbreak resistance, PII leakage | Before every deployment | 300+ | 100+ | 50+ | 20+ |
| Regression | Performance vs. previous version on identical test set | On model/prompt changes | Full suite | Full suite | 50 cases | N/A |
| RAG retrieval | Retrieval precision, recall, relevance, source attribution | Before deployment, then weekly (T1), monthly (T2), quarterly (T3) | 100+ | 50+ | 25+ | Recommended |
| Red-team | Adversarial robustness | Before deployment, then per [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) cadence | 200+, including manual testing (external testers recommended) | 100+ | Automated adversarial scan + 50 manual cases | Automated scan, 20+ cases (recommended) |
| Bias | Counterfactual fairness, demographic parity | Formal bias evaluation before deployment, then quarterly (T1), semi-annual (T2) | 200 pairs per attribute | 100 pairs per attribute | 50 pairs | N/A |
| Agent | Task success, tool-call accuracy, unsafe or out-of-policy actions, recovery from tool errors, human trajectory review (agentic systems) | Before every deployment, and on any change to the model, prompt, tools or permissions | 300+ | 100+ | N/A | N/A |
| Guardrail | False negatives (harmful or out-of-scope content passed) and false positives (legitimate requests blocked), on labelled sets (systems with guardrails) | Before deployment, and on every guardrail configuration change | 300+ of each set | 100+ of each set | 50+ of each set | N/A |
| Production | Ongoing output quality on live traffic | Continuous: three activities, see [Production Evaluation](#production-evaluation) | Every response scored (async) | 20% sample | 5% sample | Weekly batch sample |

<!-- END GENERATED: evaluation-types -->

Suite sizes apply whenever an eval type is run. Which eval types must pass before release at each tier is set in [Release Criteria by Tier](#release-criteria-by-tier). The T1 and T2 pre-release and safety sizes follow from the [statistical pass rule](#statistical-pass-rule): they are sized so that a clean run demonstrates the threshold. Agent evaluation applies only to agentic systems, which are minimum T2. Guardrail evaluation applies to systems with guardrails.

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
| Guardrail false negative rate | ≤ 1% | ≤ 3% | ≤ 5% | N/A |
| Guardrail false positive rate | Set in risk assessment; framework default ceiling 5% customer-facing, 10% internal | Same | Same | N/A |
| Task success rate (agentic) | Use-case specific (defined in risk assessment) | Same | N/A | N/A |
| Tool-call accuracy (agentic) | Use-case specific (defined in risk assessment) | Same | N/A | N/A |
| Unsafe or out-of-policy action rate (agentic) | 0 (any occurrence blocks) | 0 (any occurrence blocks) | N/A | N/A |
| Domain accuracy | Use-case specific (defined in risk assessment) | Same | Same | Same |

<!-- END GENERATED: threshold-definitions -->

These are opinionated defaults. Organizations should calibrate to their domain and risk appetite. The principle is non-negotiable: every tier has thresholds, and thresholds are enforced.

This document is the single source for these thresholds and for suite sizes. Other documents link here rather than restating different values. Use-case tolerances (for example in [hallucination-policy.md](../responsible-ai/hallucination-policy.md)) apply only when they are stricter than the tier threshold.

Agentic metrics show N/A at T3 and T4 because every agentic system is at least T2 ([override item 6](../risk-classification/agentic-ai-risk.md#tier-override-rules)). The guardrail false positive ceiling is a framework default: the risk assessment sets the target, and the target may be stricter, never looser.

---

## Metric Definitions

<!-- BEGIN GENERATED: metric-definitions. Edit policy/thresholds.yaml, then run python tools/build.py -->

| Metric | Definition |
|--------|-----------|
| Hallucination rate | Share of evaluated responses that contain at least one material unsupported or false claim. Measured at response level. A claim is material if a user could act on it: facts, figures, policy terms, fees, dates, eligibility. |
| Faithfulness | Average share of claims in a response that are supported by the retrieved context. Measured at claim level. Faithfulness and hallucination rate measure different things and both thresholds apply: a response with high faithfulness still counts as a hallucination if its one unsupported claim is material. |
| Safety pass rate | Share of safety test cases where the system responds acceptably. Each test case defines the acceptable response (for example, a refusal, a safe completion, or no PII in the output). The safety failure rate is 100% minus the pass rate. |
| Retrieval precision@5 | Share of the top 5 retrieved chunks that are relevant to the query, averaged across evaluation queries. Relevance is judged against labelled references or by a calibrated LLM-as-judge. |
| Counterfactual consistency | Share of counterfactual pairs (prompts identical except for a demographic attribute) whose outputs are consistent: same substance and conclusion, comparable sentiment and level of detail. Judged per attribute. Test protocol: [bias-detection-llm.md](../responsible-ai/bias-detection-llm.md). |
| Guardrail false negative rate | Share of harmful or out-of-scope items in the labelled guardrail set that the guardrail layer lets through. The cap equals the safety failure cap at the tier. |
| Guardrail false positive rate | Share of legitimate requests in the labelled guardrail set that the guardrail layer blocks or degrades. |
| Task success rate | Share of evaluation tasks the agent completes correctly end to end: the final output meets the task's acceptance criteria within the step, time and cost budget. |
| Tool-call accuracy | Average across tasks of the share of the task's tool calls that use the right tool with valid arguments. Calls within one task are not independent, so the lower bound resamples tasks, not calls. |
| Unsafe or out-of-policy action rate | Share of evaluation tasks in which the agent attempts at least one action outside its action inventory or policy: a tool or scope it is not allowed, a write without the required human confirmation, or a breach of its rate, budget or blast-radius caps. Counted whether or not a runtime control stopped the action. |

<!-- END GENERATED: metric-definitions -->

---

## Statistical Pass Rule

A threshold is a statement about the system's true rate, not about one run. A point estimate on a small suite cannot show that the true rate is inside the threshold. At the T1 hallucination cap of 1%, a perfect run of 0 failures in 200 cases still leaves a one-sided 95% upper bound of 1.49%, so that suite cannot demonstrate the cap at all. The rule below makes the gate honest at T1 and T2 and keeps it simple at T3 and T4.

### How a Metric Passes

| Tier | Proportion metrics | Mean-score metrics |
|------|--------------------|--------------------|
| T1, T2 | The one-sided 95% Clopper-Pearson upper bound on the failure rate is within the failure-rate cap | The one-sided 95% lower confidence bound meets the threshold. Use a percentile bootstrap over cases (10,000 resamples), or a t-interval when n is at least 100. The report states which |
| T3, T4 | The point estimate meets the threshold on at least the minimum suite size | Same |

- **Proportion metrics** count cases that pass or fail: hallucination rate, safety failure rate (100% minus the safety pass rate), counterfactual inconsistency rate (judged per attribute), guardrail false negative and false positive rates, task failure rate (100% minus task success) and the unsafe or out-of-policy action rate.
- **Mean-score metrics** average a score over cases: faithfulness, retrieval precision@5 and tool-call accuracy.
- **A threshold of zero** (unsafe or out-of-policy actions) is met only by zero failures. The suite size then sets what that zero demonstrates.
- **Use-case metrics.** Domain accuracy and other metrics set in the risk assessment follow the same split. The risk assessment states each metric's kind and whether it gates on the bound or the point estimate. Gating on the bound is recommended at T1 and T2.

The bounds assume independent cases. Do not pad a suite with paraphrases or near-duplicates of the same case to reach the size. Where cases cluster (several turns of one conversation, several tool calls in one task), count at the cluster level or bootstrap over clusters.

### Minimum Suite Sizes

Zero failures in n cases demonstrates a failure-rate cap p when n ≥ ln(0.05) / ln(1 − p).

| Failure-rate cap | Where it applies | Smallest suite | Framework minimum |
|:---:|------------------|:---:|:---:|
| 1% | T1 hallucination, safety and guardrail false negatives | 299 | 300 |
| 3% | T2 hallucination, safety and guardrail false negatives | 99 | 100 |
| 5% | T1 customer-facing guardrail false positive default ceiling | 59 | 300 (T1 legitimate set) |
| 10% | T1 counterfactual inconsistency, per attribute | 29 | 200 pairs per attribute |

A suite at the 1% or 3% minimum passes only with zero failures. Larger suites leave room for a few. Size the suite for the rate you expect, not the floor. A system whose true hallucination rate is 0.3% fails the T1 gate on 59% of 300-case runs, 44% of 500-case runs and 18% of 1,000-case runs (exact binomial).

### Maximum Failures Allowed

Computed exactly from the binomial distribution by [tools/build.py](../../tools/build.py) from the thresholds in [policy/thresholds.yaml](../../policy/thresholds.yaml).

<!-- BEGIN GENERATED: max-failures. Edit policy/thresholds.yaml, then run python tools/build.py -->

| Tier | Failure-rate cap | Metrics | Suite size | Maximum failures | Upper bound at the maximum | Upper bound with one more failure |
|------|:---:|---------|:---:|:---:|:---:|:---:|
| T1 | 1% | Hallucination rate, safety failure rate, guardrail false negative rate | 300 | 0 | 0.99% | 1.57% |
|  |  |  | 500 | 1 | 0.95% | 1.25% |
|  |  |  | 1,000 | 4 | 0.91% | 1.05% |
| T2 | 3% | Hallucination rate, safety failure rate, guardrail false negative rate | 100 | 0 | 2.95% | 4.66% |
|  |  |  | 200 | 1 | 2.35% | 3.11% |
|  |  |  | 300 | 3 | 2.56% | 3.03% |
| T1 | 10% | Counterfactual inconsistency rate | 200 pairs per attribute | 12 | 9.54% | 10.14% |
| T2 | 15% | Counterfactual inconsistency rate | 100 pairs per attribute | 8 | 13.97% | 15.18% |

<!-- END GENERATED: max-failures -->

Two readings of the table:

- **T1 caps are tight.** A 500-case pre-release suite allows one hallucination: 1 in 500 has an upper bound of 0.95% and passes. 4 in 500 has an upper bound of 1.82% and fails, even though its point estimate of 0.8% is inside the cap. A 200-case safety suite with 2 failures (99% pass rate) has an upper bound of 3.11% and fails the T1 rule.
- **The pair counts stand.** 200 pairs per attribute at T1 allow up to 12 inconsistent pairs (observed consistency of 94% or better); 100 pairs at T2 allow up to 8 (92% or better). A system that is consistent in practice can meet that, so the bias suite sizes are unchanged.

### What the Evaluation Report Records

For every T1 or T2 metric: the case count n, then either the failure count (proportion metrics) or the lower bound and the interval method (mean-score metrics), the bound, and pass or fail. The [LLM model card template](../../templates/llm-model-card.yaml) has fields for each (`n`, `failures`, `lower_bound`, `interval_method`), and [tools/check.py](../../tools/check.py) recomputes the Clopper-Pearson bound for the example cards.

---

## Regression Rule

Control EV-003. A new version is compared with the previous version on the identical suite.

| Rule | T1, T2 |
|------|--------|
| Tolerance | No metric's point estimate is worse than the previous version's by more than the half-width of the previous version's two-sided 95% interval on the same suite (Clopper-Pearson for proportions; the same bootstrap or t method for means) |
| Threshold | The new version also passes the [statistical pass rule](#statistical-pass-rule) in its own right. A change within tolerance does not excuse a missed threshold |
| Safety | Any safety regression blocks release: the safety pass rate falls, a safety case that the previous version passed now fails, the guardrail false negative rate rises, or an agent takes an unsafe or out-of-policy action |
| Exceptions | Only through [exceptions and risk acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance). An exception for a T1 or T2 safety regression is decided by the tier's exception approver itself (the AI Risk Committee at T1, the Head of AI Risk at T2), never by a delegate |

The tolerance matters most where a metric has headroom. On a 500-case suite, a faithfulness drop from 0.94 to 0.91 still clears the 90% threshold but is larger than the measurement noise, so it is a regression. At T3, regression testing is recommended and judged on point estimates.

---

## Segment Results

Averages hide gaps. At T1 and T2, the evaluation report gives every metric for each segment named in the risk assessment: for example product, channel, language and customer vulnerability indicators, alongside the protected attributes covered by bias testing.

- A segment with at least 100 cases must meet the threshold on its point estimate. A miss fails the metric, as an overall miss would.
- A segment with fewer than 100 cases is reported, not gated. A gap in a small segment is recorded as a finding, and the suite is extended for that segment before the next evaluation.
- Segments are slices of the same suite. Build the suite so that the segments that matter most reach 100 cases.

At T3 and T4, report segment results where the risk assessment names segments; they are not gated.

---

## Human Evaluation Protocol

This protocol applies to every human-rated metric and to the human labels used to calibrate an LLM judge (EV-007).

| Requirement | T1, T2 | T3, T4 |
|-------------|--------|--------|
| Rater qualification | Subject matter experts for the domain, who pass a qualification set with known answers before rating | Team members who know the domain |
| Training | Written rubric with worked examples, and a calibration session before each evaluation | Written rubric |
| Double rating | At least 20% of items rated independently by two raters | Recommended |
| Agreement | Cohen's kappa (two raters) or Krippendorff's alpha (more than two raters, or missing ratings) of at least 0.6 on the double-rated items before results are accepted (framework default) | Recommended |
| Adjudication | Disagreements resolved by a third qualified rater or a panel; the adjudicated label is the one recorded | Team lead resolves |
| Independence | Raters did not build the system and do not know which version produced an output | Where practical |

If agreement is below 0.6, the results are not accepted: tighten the rubric, retrain the raters and re-rate. The model card records the double-rated share, the statistic and its value.

**LLM-as-judge linkage.** A judge can be no more reliable than the labels it is calibrated against. Calibration under EV-007 uses labels produced under this protocol, and the judge's correlation is measured against the adjudicated labels.

---

## Agent Evaluation

Control EV-008 applies to every agentic system. Agentic systems are at least T2, so the requirements are set for T1 and T2.

**Suite.** Realistic multi-step tasks drawn from the intended use, each with written acceptance criteria, run end to end with the production tool set and permissions (or faithful sandboxed versions of them). Include tasks that sit just outside the agent's scope or would tempt it past a cap or confirmation gate. Size: 300 tasks at T1 and 100 at T2, so that zero unsafe actions demonstrates a rate of at most 1% (T1) or 3% (T2). Adversarial attacks stay in the red-team (SR-001, [agentic-specific tests](../ai-security/red-teaming-protocol.md#agentic-specific-tests)).

| Metric or test | What counts | Threshold |
|----------------|-------------|-----------|
| Task success rate | Task completed correctly end to end, within its step, time and cost budget | Set in the risk assessment; judged on the bound at T1/T2 |
| Tool-call accuracy | Right tool with valid arguments, averaged per task; the bound resamples tasks, not calls | Set in the risk assessment; judged on the lower bound |
| Unsafe or out-of-policy action rate | A task with any attempted action outside the action inventory or policy: a tool or scope not allowed, a write without the required confirmation, or a breach of rate, budget or blast-radius caps. Counted even when a runtime control stopped it | Zero. Any occurrence in the pre-release suite blocks release |
| Recovery from tool errors | Tool failures (timeouts, errors, empty or malformed results) injected into at least 10% of tasks (framework default). The agent retries within limits, falls back or escalates; it never invents a tool result or loops past its budget | Set in the risk assessment. An invented tool result is a hallucination |
| Human trajectory review | Humans review the full trajectory (plan, tool calls, arguments, results, output) of every failed task and of a random sample of at least 20% of passed tasks, under the [human evaluation protocol](#human-evaluation-protocol) | An unsafe step that automated checks missed counts as an unsafe action |

A clean run is evidence of a low rate, not of a zero rate: 0 unsafe actions in 300 tasks bounds the rate at 0.99%. Runtime controls (confirmation gates, caps, the kill switch) remain mandatory ([agentic AI risk](../risk-classification/agentic-ai-risk.md#runtime-controls)). An unsafe action is a safety failure: any exception follows the no-delegation rule for safety regressions.

Re-run on any change to the model, the prompt, the tool set or the agent's permissions.

---

## Guardrail Evaluation

Control EV-009 applies to T1 to T3 GenAI systems with guardrails: input and output filters, scope classifiers, PII redaction, toxicity gates and custom rules. It measures the guardrail layer on its own. End-to-end safety stays with the safety evaluation (EV-002).

| | T1 | T2 | T3 |
|---|:---:|:---:|:---:|
| Labelled sets | 300+ harmful or out-of-scope items and 300+ legitimate requests | 100+ of each | 50+ of each |
| False negative rate (harmful or out-of-scope content passed) | ≤ 1% | ≤ 3% | ≤ 5% |
| False positive rate (legitimate requests blocked or degraded) | Target in the risk assessment; framework default ceiling 5% customer-facing, 10% internal | Same | Same |
| Pass rule | Bound | Bound | Point estimate |

The false negative cap equals the safety failure cap at the tier. The legitimate set includes hard cases near the boundary: requests that mention a restricted topic but are allowed. A guardrail that blocks too much fails legitimate users, and teams under pressure then loosen it without evaluation; setting the false positive target up front prevents that.

Re-run on every guardrail configuration change (rules, classifier model or threshold, block lists), and with the full evaluation on any model change.

---

## Traditional ML Systems

EV-001 applies to every system, including traditional ML models. For ML:

- **Performance criteria** are the [discriminatory performance](../model-lifecycle/validation.md#3-discriminatory-performance) and [fairness](../model-lifecycle/validation.md#4-fairness-assessment) measures in the validation standard. The risk assessment sets the thresholds for the use case; this framework sets no default AUC, Gini or error-rate values.
- **Drift and degradation** use the PSI bands and the performance degradation thresholds in the [monitoring standard](../model-lifecycle/monitoring.md#monitoring-dimensions).
- **T1 and T2** report a 95% confidence interval for every gating metric (for example by bootstrap over the hold-out set) and performance by segment. Segments of 100 or more cases meet the threshold on the point estimate, as in [Segment Results](#segment-results).
- **Regression** (EV-003) applies to retrained ML models under the same [regression rule](#regression-rule).

---

## Release Criteria by Tier

| Tier | Required Evals | Reviewer | Sign-off |
|------|---------------|----------|----------|
| T1 | All eval types pass: pre-release, safety, regression, RAG retrieval (if RAG), bias, red-team, agent (if agentic), guardrail (if guardrails) | Full independent validation by Model Risk Management (MRM) | AI Risk sign-off |
| T2 | Pre-release + safety + regression + bias + RAG retrieval (if RAG) + red-team + agent (if agentic) + guardrail (if guardrails) | Independent validation, reduced scope, by a qualified reviewer outside the development team (MRM or second line) | AI lead sign-off |
| T3 | Pre-release + safety + RAG retrieval (if RAG) + guardrail (if guardrails) + red-team (automated scan + 50 manual cases) | Peer review | Team lead sign-off |
| T4 | Pre-release + safety (automated, 20+ cases each). RAG retrieval eval and red-team scan recommended | Self-test | Self-attested |

"Pass" means pass under the [statistical pass rule](#statistical-pass-rule) for the tier, including segments of 100 or more cases at T1 and T2. The team that builds a T1 or T2 system never validates its own evaluation results.

---

## Production Evaluation

Production evaluation is three named activities (control PM-004):

| Activity | T1 | T2 | T3 | T4 |
|----------|:---:|:---:|:---:|:---:|
| 1. Online automated scoring of live traffic | Every response (async) | 20% sample | 5% sample | Weekly batch sample |
| 2. Metrics review | Daily dashboard check by AI Operations, plus monthly system-owner review | Weekly | Monthly | Quarterly |
| 3. Full offline suite re-run | Monthly | Quarterly | Semi-annual | Semi-annual |

Always re-run the full offline suite on a model, provider or prompt change. A re-run that serves as release evidence for a change is judged by the same pass rule as pre-release evaluation. Alerts on live traffic use rolling rates against the alert lines in [LLM monitoring](monitoring.md).

Related production checks with their own cadence:

- **RAG retrieval evaluation:** weekly (T1), monthly (T2), quarterly (T3); recommended for T4.
- **Production counterfactual spot-checks:** weekly (T1), monthly (T2). These are separate from the formal bias evaluation (before deployment, then quarterly for T1 and semi-annual for T2). See [bias-detection-llm.md](../responsible-ai/bias-detection-llm.md).
- **Vendor behaviour canary:** for third-party models, a fixed domain set run daily (T1), weekly (T2), monthly (T3/T4) to detect silent vendor model changes. See [third-party-model-risk.md](../compliance/third-party-model-risk.md#ongoing-monitoring).
- **Prompt-change adversarial regression set:** at least 50 cases for T1/T2, re-run on every prompt change. This is separate from the pre-release red-team. See [prompt-engineering-standards.md](prompt-engineering-standards.md#minimum-evaluation-suite-size).

---

## Eval Dataset Governance

- Eval datasets versioned and access-controlled (same rigor as code)
- No overlap between eval data and training/fine-tuning data (data leakage invalidates evals)
- Suite sizes count distinct cases; paraphrases and near-duplicates of one case count once
- Eval datasets reviewed for representativeness and bias annually (T1/T2), including whether the segments named in the risk assessment are large enough to gate
- Multiple independent eval sets for T1 (prevent overfitting to a single benchmark)
- Eval data containing PII handled per data governance policy

---

## Eval Infrastructure Requirements

- Eval results stored immutably (append-only, tamper-evident). They are audit evidence
- Results linked to: model version, prompt version, dataset version, evaluator identity
- Automated eval pipeline for T1/T2 (CI/CD integrated; manual acceptable for T3/T4), computing the confidence bounds as well as the point estimates
- Eval failures automatically block deployment pipeline for T1/T2
- Evaluation results are governance records: retain them for the life of the system plus the tier retention period, per [audit-trail-requirements.md](../compliance/audit-trail-requirements.md). Historical results also support trending and regression detection.

---

## LLM-as-Judge Calibration

- When using LLM-as-judge for automated evaluation: calibrate against human evaluators quarterly (T1), semi-annually (T2)
- Calibrate against labels produced under the [human evaluation protocol](#human-evaluation-protocol), with inter-rater agreement of at least 0.6
- Document the correlation between LLM-as-judge scores and human scores
- If correlation drops below 0.85: pause automated eval; recalibrate or revert to human eval
- Never use LLM-as-judge as the sole evaluator for safety-critical metrics (T1 hallucination, PII leakage)

---

## Anti-patterns

- Running evals only at initial deployment, never again
- Using the same eval set for development tuning and release validation (data leakage)
- Setting thresholds so low they never fail (governance theater)
- Reading a point estimate on a small suite as proof that a threshold is met
- Padding a suite with paraphrases to reach the minimum size
- Treating LLM-as-judge scores as ground truth without human calibration
- Evaluating only accuracy, ignoring safety, bias, and retrieval quality
- Reporting averages without per-segment breakdowns (hides demographic performance gaps)

---

## Integration

- Red-team eval references [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md). This file owns "what must pass"; red-teaming owns "how to test"
- Production eval cadence aligned with [LLM monitoring](monitoring.md)
- Control register IDs ([control-register.md](../governance-operations/control-register.md)): pre-release EV-001, safety EV-002, regression EV-003, RAG retrieval EV-004, bias EV-005, agent EV-008, guardrail EV-009, red-team SR-001, production PM-004. EV-006 covers eval dataset integrity and EV-007 covers LLM-as-judge calibration.
- Eval report is a required artifact in the deployment evidence pack (see [governance-workflow.md](../governance-operations/governance-workflow.md) Stage 7)
