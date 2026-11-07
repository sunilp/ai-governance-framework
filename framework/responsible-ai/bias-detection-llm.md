# Bias Detection for LLM Systems

## Overview

Bias in LLM outputs manifests differently from bias in traditional ML models. Traditional models produce discriminatory predictions that can be measured with statistical parity metrics. LLMs produce free-text outputs where bias appears in tone, framing, representation, stereotyping, and differential quality across demographic groups.

This document defines standards for detecting, measuring, and mitigating bias in enterprise LLM deployments.

---

## Bias Categories in LLM Systems

### 1. Representational Bias

The model systematically associates certain demographic groups with specific attributes, roles, or characteristics.

**Examples:**
- Describing male executives as "decisive" and female executives as "collaborative"
- Associating certain nationalities with specific industries or roles
- Defaulting to male pronouns in professional contexts

### 2. Quality Disparity

The model produces higher-quality outputs for some groups than others.

**Examples:**
- More detailed and accurate responses for queries about majority-group topics
- Lower fluency or accuracy when discussing minority cultures, languages, or contexts
- Better performance in English than in other languages used by the organization

### 3. Stereotyping and Toxicity

The model generates outputs that reinforce stereotypes or produce differentially harmful content.

**Examples:**
- Generating stereotypical descriptions when asked about specific demographic groups
- Producing more negative sentiment when discussing certain groups
- Differential refusal rates based on demographic context in the query

### 4. Allocation Bias (Decision-Influencing Systems)

When LLM outputs influence resource allocation or decisions, bias can lead to discriminatory outcomes.

**Examples:**
- Resume screening summaries that emphasize different qualities based on candidate demographics
- Credit memo drafts that frame similar financial situations differently based on applicant characteristics
- Risk assessment narratives that use different language for similar risk profiles

---

## Testing Framework

### Pre-Deployment Bias Evaluation

Bias testing has two named activities:

1. **Formal bias evaluation** (control EV-005): before deployment, then quarterly (T1) and semi-annual (T2). Required for T1/T2 release; recommended for T3 ([governance-workflow.md](../governance-operations/governance-workflow.md), Stage 5).
2. **Production counterfactual spot-checks:** weekly (T1) and monthly (T2). See [Production Bias Monitoring](#production-bias-monitoring).

Cadences, suite sizes and thresholds are owned by [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md#evaluation-types).

| Test Category | Method | Required For |
|--------------|--------|-------------|
| Counterfactual testing | Swap demographic identifiers in prompts; compare outputs | T1, T2 (T3 recommended) |
| Stereotype association | Test for stereotypical associations using standardized prompts | T1, T2 |
| Quality parity | Measure output quality metrics across demographic contexts | T1, T2 |
| Sentiment analysis | Compare sentiment of outputs across demographic variations | T1, T2 |
| Refusal parity | Measure refusal rates across demographic contexts | T1, T2 (T3 recommended) |
| Red-team for bias | Adversarial prompts designed to elicit biased outputs | T1 |

### Counterfactual Testing Protocol

1. Create a set of representative prompts for the use case
2. Generate variants by substituting demographic identifiers (gender, ethnicity, age, nationality)
3. Run all variants through the system
4. Compare outputs across dimensions:
   - Semantic similarity (should be high for equivalent queries)
   - Sentiment (should be consistent)
   - Length and detail (should be comparable)
   - Recommendations or conclusions (should be equivalent)
5. Flag and investigate any systematic differences

**Minimum test set size** (pair counts restate [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md#evaluation-types)):

| Tier | Counterfactual Pairs | Most Inconsistent Pairs Allowed per Attribute | Protected Attributes Tested |
|------|---------------------|:---:|---------------------------|
| T1 | ≥ 200 pairs per attribute | 12 of 200 (upper bound 9.54%, cap 10%) | All legally protected attributes relevant to use case |
| T2 | ≥ 100 pairs per attribute | 8 of 100 (upper bound 13.97%, cap 15%) | Primary protected attributes |
| T3 | ≥ 50 pairs (when run) | 10 of 50 (point estimate, 80%) | Key protected attributes |
| T4 | N/A (not required) | N/A | N/A |

Each attribute is judged on its own pairs. At T1 and T2 an attribute passes only if the one-sided 95% upper confidence bound on its inconsistency rate is within the cap ([statistical pass rule](../llm-lifecycle/evaluation-governance.md#statistical-pass-rule)), which requires observed consistency of at least 94% at T1 and 92% at T2 at these pair counts. More pairs leave more room ([maximum failures allowed](../llm-lifecycle/evaluation-governance.md#maximum-failures-allowed)).

### Metrics

| Metric | Definition | Threshold |
|--------|-----------|-----------|
| Counterfactual consistency | Share of counterfactual pairs whose outputs are consistent ([definition](../llm-lifecycle/evaluation-governance.md#metric-definitions)) | T1 ≥ 90%, T2 ≥ 85%, T3 ≥ 80% per attribute; T1/T2 judged on the 95% confidence bound ([evaluation-governance](../llm-lifecycle/evaluation-governance.md#threshold-definitions-by-tier)) |
| Sentiment Parity | Max sentiment difference across demographic variants | ≤ 0.1 (normalized scale) |
| Quality Parity | Max quality score difference across demographic variants | ≤ 0.05 |
| Refusal Parity | Max refusal rate difference across demographic variants | ≤ 0.02 |
| Stereotype Score | Proportion of outputs flagged for stereotypical content | ≤ 0.01 for T1; ≤ 0.03 for T2 |

---

## Ongoing Monitoring

### Production Bias Monitoring

| Activity | Frequency | Method |
|----------|-----------|--------|
| Production counterfactual spot-checks | Weekly (T1), Monthly (T2) | Automated counterfactual testing on production model; separate from the formal bias evaluation |
| Output sentiment analysis | Continuous (sampled) | Automated sentiment analysis across demographic context |
| User complaint analysis | Continuous | Categorize complaints for bias-related issues |
| Fairness metric tracking | Monthly | Dashboard tracking of all bias metrics |
| Independent bias audit | Annually (T1), Every 2 years (T2) | External or independent internal review |

### Bias Incident Response

#### Examples by severity (definitions: [escalation-paths.md](../operating-model/escalation-paths.md#severity-classification))

Severity levels and response SLAs (S1 15 minutes, S2 4 hours, S3 24 hours, S4 next business day) are defined in escalation-paths.md. This table gives bias examples only.

| Severity | Example | Response |
|----------|----------|----------|
| S1 | Discriminatory output delivered to customer or used in regulated decision | Immediate system pause; root cause identified within 48 hours |
| S2 | Systematic bias detected in production outputs reaching customers or external parties (pattern, not isolated), no confirmed harm yet | Enhanced monitoring; remediation plan; root cause identified within 48 hours |
| S3 | Bias detected in testing or spot-checks before reaching anyone outside | Prompt/guardrail adjustment; root cause documented within 10 business days |
| S4 | Minor bias indicator in metrics trending | Tracked in backlog; next scheduled review |

---

## Mitigation Strategies

| Strategy | Description | Effectiveness |
|----------|-------------|---------------|
| Prompt engineering | Include explicit instructions for balanced, unbiased output | High for representational bias |
| Few-shot examples | Provide diverse, balanced examples in prompts | Medium-High |
| Output post-processing | Filter or flag outputs that fail bias checks | Medium — catches obvious cases |
| Model selection | Choose models with better bias benchmarks | Foundational |
| Fine-tuning | Fine-tune on balanced, curated datasets | High but resource-intensive |
| Guardrail rules | Automated rules that flag demographic-specific language patterns | Medium — limited to known patterns |
| Human review | Human reviewers check outputs for bias | High but not scalable |

### Mitigation Priority

For T1 use cases: implement all applicable strategies in combination.
For T2: prompt engineering + guardrails + monitoring.
For T3/T4: prompt engineering + basic monitoring.

---

## Documentation Requirements

For each GenAI use case, document:

1. **Protected attributes relevant to the use case** and why
2. **Bias testing methodology** used and results
3. **Bias metrics** and thresholds with justification
4. **Mitigation strategies** implemented
5. **Residual bias risk** assessment and acceptance
6. **Monitoring plan** for ongoing bias detection
7. **Incident response** procedures for bias incidents
