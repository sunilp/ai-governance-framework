# AI Impact Assessment

## System Information

| Field | Value |
|-------|-------|
| System Name | |
| System ID | |
| Risk Tier | |
| Business Owner | |
| Assessment Date | |
| Assessor | |

## 1. Business Impact

### 1.1 Business Objective
_What business problem does this AI system solve? What is the expected benefit?_

### 1.2 Scale of Deployment
- Expected number of decisions/predictions per day:
- Number of customers affected:
- Capital or revenue at risk:
- Geographic scope:

### 1.3 Business Dependency
- What happens if the system is unavailable for 1 hour?
- What happens if the system is unavailable for 24 hours?
- Is there a manual fallback process? Describe it.
- How long can the fallback operate before business impact becomes critical?

### 1.4 Competitive and Strategic Impact
_Does this system provide a competitive advantage? What is the strategic importance?_

## 2. Customer Impact

### 2.1 Decision Consequences
_What happens to a customer when the system produces its output? What are the consequences of an incorrect output?_

### 2.2 Recourse Mechanisms
- Can a customer challenge or appeal a decision made by this system?
- How is the appeal process communicated to the customer?
- What is the average resolution time for appeals?
- Where a right to an explanation or human review applies, how are requests handled and logged (RV-005)?

### 2.3 Vulnerable Populations
_Could this system disproportionately affect vulnerable populations (elderly, low-income, non-native speakers, people with disabilities)?_

### 2.4 Customer Communication
- Are customers informed that AI is involved in the decision?
- How is this communicated?
- Can customers opt out of AI-assisted decisions?
- Which notice duties apply, and where in the journey is each notice given (DE-006 for AI interaction, DE-009 for AI-assisted decisions)?

## 3. Ethical Considerations

### 3.1 Fairness
- Which protected attributes are relevant to this use case?
- Has the system been tested for disparate impact across these attributes?
- What fairness metrics were selected and why?
- Results:

### 3.2 Transparency
- Can the system explain its decisions in terms understandable to the affected individual?
- Are the factors driving decisions aligned with what a reasonable person would expect?
- Is there any "black box" component that cannot be explained?

### 3.3 Privacy
- What personal data does the system process?
- Is the data usage proportionate to the objective?
- Has a DPIA been completed?
- Are there data minimization opportunities?

### 3.4 Autonomy
- Does the system respect individual autonomy and choice?
- Could the system create feedback loops that limit future options for individuals?
- Is there meaningful human oversight? Which pattern applies: human-in-the-loop, human-on-the-loop, human-over-the-loop or human-out-of-the-loop (see [human-in-loop-patterns.md](../framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix))?

## 4. Regulatory Impact

### 4.1 Applicable Regulations
_List all regulations that apply to this AI system and its use case._

| Regulation | Relevance | Compliance Status |
|-----------|-----------|-------------------|
| | | |

### 4.2 Supervisory Expectations
_Are there any supervisory expectations or guidance (beyond formal regulations) that apply?_

### 4.3 Compliance Gaps
_Are there any gaps between current system capabilities and regulatory requirements?_

## 5. Fundamental Rights Impact Assessment (EU AI Act Art. 27)

Complete this section when the EU AI Act role record (RA-008) shows the organisation is a deployer in scope of Art. 27. This is control RA-009. Otherwise record "Not applicable" and the reason in 5.1. The duty applies to Annex III systems from 2 December 2027. See the [EU AI Act mapping](../framework/compliance/eu-ai-act-mapping.md#a-deployer-of-high-risk-ai-systems).

### 5.1 Scope

| Question | Answer |
|----------|--------|
| Is the system high-risk under Art. 6(2) (listed in Annex III)? Which point? | |
| Is it used under Annex III point 5(b) (creditworthiness or credit score of natural persons, not fraud detection) or point 5(c) (risk assessment and pricing for natural persons in life and health insurance)? | |
| If not, is the organisation a body governed by public law or a private entity providing public services, using an Annex III system other than point 2? | |
| Is this the first use? If a previous assessment for a similar case, or the provider's existing impact assessment, is relied on (Art. 27(2)), give the reference | |
| Result: assessment required / not applicable (with reason) | |

### 5.2 Assessment (Art. 27(1))

| Art. 27(1) | Element | Response | Related section |
|:---:|---------|----------|-----------------|
| (a) | The deployer's processes in which the system will be used, in line with its intended purpose | | 1.1 |
| (b) | The period of time within which, and the frequency with which, the system is intended to be used | | 1.2 |
| (c) | The categories of natural persons and groups likely to be affected by its use in this context | | 2.3 |
| (d) | The specific risks of harm likely to affect the people and groups in (c), taking into account the information the provider gives under Art. 13 | | 3.1, 6 |
| (e) | How the human oversight measures in the instructions for use are implemented | | 3.4 |
| (f) | The measures to be taken if those risks materialise, including internal governance arrangements and complaint mechanisms | | 2.2 |

### 5.3 DPIA Cross-Reference (Art. 27(4))

Where the DPIA (RA-005) already meets part of this assessment, the FRIA can cross-refer to the relevant DPIA sections or include the relevant parts (Art. 27(4), as amended by Regulation (EU) 2026/1744).

| Field | Value |
|-------|-------|
| DPIA reference | |
| DPIA sections relied on, and the Art. 27(1) elements they cover | |

### 5.4 Notification to the Market Surveillance Authority (Art. 27(3))

Once the assessment is done, notify the market surveillance authority of the results, submitting the filled-out AI Office template (Art. 27(3) and 27(5)). Check whether the AI Office has published the template before planning the notification. For high-risk systems used by financial institutions in direct connection with financial services, the market surveillance authority is the national financial supervisor, unless the Member State has designated another authority (Art. 74(6) and 74(7)).

| Field | Value |
|-------|-------|
| Authority notified | |
| Date notified | |
| Notification reference | |
| Template version used | |

### 5.5 Updates (Art. 27(2))

If any element in 5.2 changes or is no longer up to date during use, update the assessment and consider whether a new notification is needed.

| Date | Element changed | Update made | Notified (Y/N) |
|------|-----------------|-------------|----------------|
| | | | |

## 6. Risk Summary

| Risk Category | Assessment | Mitigation |
|--------------|------------|------------|
| Incorrect decisions at scale | | |
| Discriminatory outcomes | | |
| Privacy breach | | |
| System unavailability | | |
| Regulatory non-compliance | | |
| Reputational damage | | |
| Gaming or adversarial manipulation | | |

## 7. Recommendation

_Based on this assessment, is the system appropriate for deployment? Under what conditions?_

- [ ] Approved for deployment as designed
- [ ] Approved with conditions (list below)
- [ ] Not approved: material concerns require resolution
- [ ] Further assessment needed

**Conditions (if applicable):**

## Approval

| Role | Name | Date | Decision |
|------|------|------|----------|
| Business Owner | | | |
| Model Risk Management | | | |
| Compliance | | | |
| AI Risk Committee (T1 only) | | | |
