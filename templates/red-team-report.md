# AI Red-Team Assessment Report

## Instructions

Complete this template after conducting adversarial testing of an AI system. For the testing methodology, see [red-teaming-protocol.md](../framework/ai-security/red-teaming-protocol.md). Submit to the system owner and AI Risk within 5 business days of assessment completion.

Sanitize all examples — redact any PII, confidential data, or content that could enable attacks if the report is shared.

---

## 1. Engagement Summary

| Field | Value |
|-------|-------|
| Report ID | RT-YYYY-NNN |
| System Under Test | |
| System ID | |
| Risk Tier | T1 / T2 / T3 / T4 |
| Assessment Date(s) | |
| Report Date | |
| Assessor(s) | |
| Assessment Type | Internal / External / Automated / Combined |
| Total Test Cases Executed | |
| Model Version(s) Tested | |
| Prompt Version(s) Tested | |

---

## 2. Scope

### In Scope

- [ ] Prompt injection (direct)
- [ ] Prompt injection (indirect / via context)
- [ ] Jailbreaking
- [ ] Information extraction (system prompt, PII, training data)
- [ ] Harmful content generation
- [ ] Tool misuse (agentic systems)
- [ ] Social engineering
- [ ] Multimodal attacks
- [ ] Other: _______________

### Out of Scope

> [Document what was explicitly excluded and why]

### Rules of Engagement

> [Any constraints on testing: no production data, no destructive actions, time windows, etc.]

---

## 3. Executive Summary

**Overall Risk Rating:** Critical / High / Medium / Low

> [2–3 sentence summary: what was tested, what was found, overall assessment of the system's adversarial robustness]

**Key Statistics:**

| Metric | Value |
|--------|-------|
| Total findings | |
| Critical findings | |
| High findings | |
| Medium findings | |
| Low findings | |
| Categories with zero findings | |

---

## 4. Findings Summary

| # | Finding Title | Severity | Category | Reproducibility | Status |
|---|-------------|----------|----------|:---:|--------|
| 1 | | Crit / High / Med / Low | | Always / Sometimes / Rare | Open / Remediated |
| 2 | | | | | |
| 3 | | | | | |

---

## 5. Detailed Findings

*Repeat this section for each finding.*

### Finding [N]: [Title]

| Field | Value |
|-------|-------|
| Severity | Critical / High / Medium / Low |
| Category | Prompt injection / Jailbreaking / Information extraction / Harmful content / Tool misuse / Social engineering / Other |
| Attack vector | Direct user input / Indirect via RAG / Indirect via tool output / Multi-turn / Multimodal |
| Reproducibility | Always / Sometimes / Rare |

**Description:**

> [What was found. What behavior was observed that should not have occurred.]

**Steps to reproduce:**

1.
2.
3.

**Evidence:**

> [Sanitized examples of inputs and outputs demonstrating the vulnerability. Redact all sensitive content.]

**Impact:**

> [What could an attacker achieve by exploiting this? What is the business impact?]

**Affected guardrails:**

> [Which safety controls should have caught this? Why didn't they?]

**Recommended remediation:**

> [Specific, actionable recommendation to address this finding.]

**Remediation priority:** Immediate / Next sprint / Next quarter

---

## 6. Positive Findings

*Document defenses that worked well — what attacks were successfully blocked.*

| Category | Finding |
|----------|---------|
| | [Defense that held up under testing] |
| | |

---

## 7. Recommendations

| Priority | Recommendation | Addresses Finding(s) | Owner | Due Date |
|----------|---------------|:---:|-------|----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## 8. Retest Requirements

| Finding # | Retest Required | Retest Scope | Retest Date | Retest Result |
|-----------|:---:|-------------|-------------|---------------|
| | Yes / No | | | Pass / Fail / Pending |

---

## 9. Deployment Gate Decision

Based on this assessment:

- [ ] **Pass** — no Critical or High findings; system may proceed to deployment
- [ ] **Conditional pass** — no Critical findings; High findings have documented remediation plan with timeline
- [ ] **Fail** — Critical or unaddressed High findings; system must not proceed to deployment

**Rationale:**

>

---

## 10. Approvals

| Role | Name | Date | Sign-off |
|------|------|------|:---:|
| Red-Team Lead | | | [ ] |
| System Owner | | | [ ] |
| AI Risk Lead | | | [ ] |
| CISO (if security findings) | | | [ ] |
