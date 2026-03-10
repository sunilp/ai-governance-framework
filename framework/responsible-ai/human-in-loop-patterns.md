# Human-in-the-Loop Patterns for GenAI

## Overview

Human-in-the-loop (HITL) is not a single pattern. It is a spectrum of human involvement ranging from full human control to minimal human oversight. The appropriate pattern depends on the risk tier, use case, regulatory requirements, and operational constraints.

This document defines HITL patterns for GenAI systems and provides guidance on selecting the appropriate level of human involvement.

---

## HITL Pattern Spectrum

### Pattern 1: Human-in-the-Loop (Full Review)

```
AI generates → Human reviews every output → Human approves/edits → Output delivered
```

**Characteristics:**
- Every AI output is reviewed by a qualified human before use
- Human has full authority to approve, edit, or reject
- AI output is a draft; human output is the final product

**Appropriate for:**
- T1 use cases with customer-facing or regulated outputs
- Regulatory submissions and disclosures
- Legal and compliance communications
- Medical or safety-related guidance

**Trade-offs:**
- Highest quality assurance
- Lowest throughput; does not scale linearly
- Human reviewer can become a bottleneck
- Reviewer fatigue degrades effectiveness over time

### Pattern 2: Human-on-the-Loop (Sampling Review)

```
AI generates → Output delivered → Human reviews sampled outputs → Feedback loop
```

**Characteristics:**
- AI outputs are delivered without individual review
- A percentage of outputs are sampled for human quality review
- Anomaly detection flags outputs for human review
- Feedback from reviews improves the system

**Appropriate for:**
- T2 use cases with internal audiences
- High-volume, lower-risk applications
- Use cases where output quality is measurable automatically

**Trade-offs:**
- Higher throughput than full review
- Some incorrect outputs reach users before review
- Requires robust automated quality monitoring
- Sampling must be statistically valid

### Pattern 3: Human-over-the-Loop (Exception Handling)

```
AI generates → Automated quality checks → Pass: output delivered; Fail: escalate to human
```

**Characteristics:**
- AI outputs are automatically evaluated by guardrails and quality checks
- Only flagged outputs are escalated to human review
- Humans handle exceptions, edge cases, and guardrail triggers

**Appropriate for:**
- T2/T3 use cases with effective automated quality monitoring
- Use cases where the failure modes are well-understood and detectable
- High-volume applications where full review is not feasible

**Trade-offs:**
- Scales well
- Depends entirely on the quality of automated detection
- Unknown failure modes bypass human review
- Exception volume must be manageable

### Pattern 4: Human-out-of-the-Loop (Autonomous)

```
AI generates → Output delivered → Periodic audit
```

**Characteristics:**
- AI operates autonomously with minimal real-time human involvement
- Humans perform periodic audits and reviews
- System is monitored for aggregate performance, not individual outputs

**Appropriate for:**
- T4 use cases with minimal consequence
- Internal productivity tools
- Content drafting where human editing is the next natural step

**Trade-offs:**
- Maximum throughput and scalability
- Highest risk exposure; relies on monitoring to catch issues
- Not appropriate for consequential decisions or customer-facing applications

---

## Pattern Selection Matrix

| Factor | Pattern 1 (Full) | Pattern 2 (Sampling) | Pattern 3 (Exception) | Pattern 4 (Autonomous) |
|--------|------------------|---------------------|----------------------|----------------------|
| Risk tier | T1 | T2 | T2, T3 | T3, T4 |
| Output volume | Low-Medium | Medium-High | High | Very High |
| Consequence of error | Critical | Significant | Moderate | Low |
| Regulatory requirement | Often mandated | May satisfy with controls | Conditional | Rarely required |
| Reviewer availability | High | Medium | Low (exception only) | Minimal |
| Automated quality detection | Nice-to-have | Important | Essential | Essential |

---

## Reviewer Requirements

### Reviewer Qualifications

| Use Case Category | Reviewer Qualification |
|------------------|----------------------|
| Regulatory/compliance content | Compliance officer or qualified analyst |
| Financial analysis | Financial analyst with domain expertise |
| Customer communications | Customer service specialist or communications professional |
| Technical content | Subject matter expert in the relevant domain |
| Legal content | Legal professional |
| General business content | Business professional with domain awareness |

### Reviewer Training

All human reviewers must be trained on:
1. **AI system capabilities and limitations** — what the system can and cannot do reliably
2. **Common failure modes** — hallucination patterns, bias indicators, quality degradation signs
3. **Review criteria** — what to check, what constitutes acceptable vs. unacceptable output
4. **Feedback procedures** — how to report issues and provide feedback that improves the system
5. **Escalation procedures** — when and how to escalate concerns

### Reviewer Fatigue Mitigation

| Control | Description |
|---------|-------------|
| Review quotas | Maximum number of reviews per reviewer per shift |
| Rotation | Rotate reviewers to prevent habituation |
| Quality checks on reviewers | Inject known-bad outputs to verify reviewer attentiveness |
| Tool support | Provide tooling that highlights areas of concern, reducing cognitive load |
| Breaks | Mandatory breaks during review sessions |

---

## HITL for Agentic AI

Agentic AI systems require special HITL considerations due to their autonomous, multi-step nature:

| Control | Description |
|---------|-------------|
| Action confirmation gates | Human must approve irreversible or high-impact actions before execution |
| Plan review | For multi-step tasks, human reviews the agent's plan before execution begins |
| Checkpoint review | For long-running tasks, human reviews intermediate results at defined checkpoints |
| Budget gates | Agent must pause and seek approval when approaching token, cost, or action limits |
| Emergency stop | Operator can immediately halt agent execution |

---

## Regulatory Requirements for Human Oversight

| Regulation | Requirement | Minimum Pattern |
|-----------|-------------|-----------------|
| EU AI Act (Article 14) | High-risk systems must have human oversight measures | Pattern 1 or 2 for high-risk; specific requirements vary |
| GDPR (Article 22) | Right not to be subject to solely automated decisions with legal effects | Pattern 1 for decisions with legal/significant effects |
| SR 11-7 | Model outputs used in consequential decisions require appropriate oversight | Pattern 1 or 2 based on model risk tier |
| Consumer Duty (FCA) | Fair outcomes for consumers | Pattern appropriate to consumer impact |
| EBA Guidelines on ML | Human judgment in credit decisions | Pattern 1 for credit decisions |

---

## Monitoring HITL Effectiveness

| Metric | Description | Action Threshold |
|--------|-------------|-----------------|
| Review throughput | Reviews completed per hour/day | Below capacity → increase reviewers or adjust pattern |
| Reviewer agreement | Inter-reviewer consistency | < 85% → retrain reviewers or clarify criteria |
| Override rate | How often reviewer changes AI output | Trending up → investigate AI quality; trending down → check for rubber-stamping |
| Time per review | Average time spent per review | Increasing → investigate complexity; decreasing → check for thoroughness |
| Escalation rate | Reviews escalated to senior staff | Trending up → investigate root causes |
| Miss rate | Errors that passed human review (detected later) | Any occurrence → review process and training |
