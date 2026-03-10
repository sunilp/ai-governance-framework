# Fine-Tuning Governance

## Overview

Fine-tuning a foundation model creates a derivative model that the organization owns and is accountable for. Unlike prompt engineering, fine-tuning modifies model weights, introducing risks related to training data quality, bias amplification, safety alignment degradation, and ongoing maintenance obligations.

This document defines when fine-tuning is appropriate, what governance controls apply, and how fine-tuned models are managed through their lifecycle.

---

## When to Fine-Tune

Fine-tuning is appropriate when:

| Criterion | Description |
|-----------|-------------|
| Prompt engineering is insufficient | The task requires consistent behavior that cannot be reliably achieved through prompting alone |
| Domain-specific performance gap | The base model underperforms on domain-specific tasks despite optimized prompts and few-shot examples |
| Cost optimization | A smaller fine-tuned model can match the performance of a larger base model at lower inference cost |
| Consistency requirements | The use case demands highly consistent output format, tone, or style across all interactions |
| Latency requirements | A smaller fine-tuned model meets latency SLAs that larger models cannot |

Fine-tuning is **not appropriate** when:
- Prompt engineering or RAG can achieve acceptable results (always try these first)
- Training data is insufficient in quantity or quality (< 1,000 high-quality examples for most tasks)
- The use case requirements change frequently (fine-tuning is slow to iterate)
- The organization cannot commit to ongoing model maintenance (retraining, evaluation, monitoring)

---

## Training Data Governance

### Data Quality Requirements

| Requirement | Standard |
|-------------|----------|
| Labeling accuracy | ≥ 95% inter-annotator agreement for supervised tasks |
| Data provenance | Every training example traceable to its source |
| Deduplication | Training set deduplicated; no leakage between train/eval splits |
| Recency | Training data reflects current domain knowledge and policies |
| Balance | Class balance appropriate to the task; documented if imbalanced |
| Volume | Minimum viable dataset size documented and justified |

### Data Classification and Handling

| Data Classification | Fine-Tuning Permitted? | Conditions |
|--------------------|----------------------|------------|
| Public data | Yes | Standard data governance |
| Internal data | Yes | Data owner approval; access controls on training environment |
| Confidential data | Conditional | CISO approval; isolated training environment; data anonymization where feasible |
| PII / Customer data | Conditional | DPO approval; privacy impact assessment; anonymization or synthetic data preferred |
| Regulated data (MNPI, etc.) | Restricted | Legal + Compliance + CISO approval; may be prohibited by regulation |

### Data Lineage

Maintain a complete record of:
- Source datasets and their versions
- Preprocessing and transformation steps
- Filtering criteria and exclusions
- Annotation methodology and guidelines
- Train/validation/test split rationale
- Any synthetic data generation methods

---

## Fine-Tuning Process Controls

### Pre-Training

| Step | Requirement |
|------|-------------|
| Use case approval | Fine-tuning justification approved by appropriate authority (per tier) |
| Base model selection | Base model selected per [model-selection.md](model-selection.md) criteria |
| Data review | Training data reviewed for quality, bias, and compliance |
| Evaluation design | Evaluation suite defined before training begins |
| Safety baseline | Base model safety benchmarks established for comparison |
| Infrastructure | Training environment meets security and data residency requirements |
| Budget approval | Compute cost estimated and approved |

### During Training

| Control | Description |
|---------|-------------|
| Experiment tracking | All hyperparameters, training curves, and checkpoints logged |
| Checkpoint management | Intermediate checkpoints saved at defined intervals |
| Monitoring | Training loss, validation metrics tracked in real-time |
| Access control | Training environment access restricted to authorized personnel |
| Data isolation | Training data does not leave the approved environment |

### Post-Training

| Step | Requirement |
|------|-------------|
| Performance evaluation | Full evaluation suite on held-out test set |
| Safety evaluation | Safety benchmarks compared to base model; no regression permitted |
| Bias evaluation | Bias testing on protected attributes relevant to the use case |
| Hallucination evaluation | Hallucination rate compared to base model on domain tasks |
| Red-team testing | Adversarial testing for prompt injection, jailbreaking, unintended behaviors |
| Documentation | Model card completed with training details, evaluation results, limitations |
| Approval | Tier-appropriate approval before deployment |

---

## Safety Alignment Risks

Fine-tuning can degrade the base model's safety alignment. Common degradation patterns:

| Risk | Description | Mitigation |
|------|-------------|------------|
| Safety bypass | Fine-tuning on task data without safety examples erodes refusal behavior | Include safety-relevant examples in training data |
| Bias amplification | Training data biases are amplified in the fine-tuned model | Bias evaluation pre and post fine-tuning; balanced training data |
| Capability overhang | Fine-tuning unlocks capabilities the base model was trained to suppress | Comprehensive red-team testing |
| Distribution shift | Model performs well on training distribution but degrades unpredictably elsewhere | Evaluate on out-of-distribution test cases |

### Mandatory Safety Checks

For all fine-tuned models, regardless of tier:
1. Compare refusal rates on standard safety benchmarks (base vs. fine-tuned)
2. Test with standard adversarial prompt suites
3. Evaluate toxicity scores on open-ended generation tasks
4. Document any safety regression with risk acceptance sign-off

---

## Lifecycle Management

### Retraining Triggers

| Trigger | Action |
|---------|--------|
| Domain drift | Source data or domain knowledge has changed materially |
| Performance degradation | Production metrics fall below defined thresholds |
| Base model update | New version of the base model available with improved capabilities |
| Safety concern | Post-deployment safety issue identified |
| Regulatory change | New requirements affect the model's compliance posture |

### Retraining Governance

Each retraining cycle follows the same governance as initial fine-tuning:
- Updated training data must be reviewed and approved
- Full evaluation suite re-run
- Safety benchmarks re-validated
- Model card updated
- Tier-appropriate approval before redeployment

### Retirement

Fine-tuned models must be retired when:
- The use case is decommissioned
- A replacement model is deployed and validated
- Safety or compliance issues cannot be remediated
- The base model is deprecated by the vendor

Retirement process:
1. Notify all dependent systems and stakeholders
2. Migrate traffic to replacement (if applicable)
3. Archive model artifacts, training data references, and evaluation records
4. Retain documentation per audit trail requirements
5. Decommission inference infrastructure
