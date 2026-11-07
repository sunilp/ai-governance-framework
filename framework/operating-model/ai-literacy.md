# AI Literacy

## Purpose

People who use, build, oversee and govern AI need to know enough to do it safely. This standard sets the literacy measures by role: who needs what, when, how often it is refreshed, and the evidence that the measures were taken. It is the source document for control GV-002.

Literacy is a control in its own right. A human reviewer who does not know how the system fails will approve its mistakes, and an approver who cannot read an evaluation report will sign one that does not support the decision. Most of the human oversight controls in this framework assume the people involved were trained.

---

## Why This Is Required

| Source | What it expects |
|---|---|
| EU AI Act, Art. 4, as replaced by Regulation (EU) 2026/1744 | Providers and deployers take measures to support the AI literacy of their staff and of others operating or using AI systems on their behalf, taking into account technical knowledge, experience, education and training, the context of use and the people the systems are used on. The duty is to take measures; it does not require a guaranteed level of literacy for any individual. See [AI literacy (Art. 4)](../compliance/eu-ai-act-mapping.md#ai-literacy-art-4) |
| NIST AI RMF, GOVERN 2.2 | Personnel and partners receive AI risk management training so they can perform their duties consistent with policies, procedures and agreements |
| ISO/IEC 42001, clause 7.2 | Determine the competence needed for AI work, make sure people have it, and keep documented evidence |
| APRA letter to industry on AI (30 April 2026) | Board AI literacy is one of the areas it raises ([Australia profile](../compliance/multi-jurisdictional-guide.md)) |

Completion records show that measures were taken. They do not prove that anyone is literate, and the framework does not treat them as proof. The knowledge checks and reviewer quality checks below are what show the measures work.

---

## Audiences and Measures

Framework defaults. Adjust format and length to the organisation; keep the audiences, the triggers and the evidence.

| Audience | Who | Content | When | Refresh |
|---|---|---|---|---|
| Board | Directors, starting with the Board Risk Committee | How AI creates value and risk in the business; the AI policy and risk appetite; what the tiers mean and what puts a system in T1; what reaches the board and how fast; regulatory exposure by jurisdiction; questions to ask management | On appointment | Annual briefing, plus a session on any major regulatory change |
| Executives and AI Risk Committee members | Executive committee, committee members and their delegates, Business Unit Heads who co-sign T2 deployments | Approval decisions by tier; reading an evidence pack and an evaluation report; the exception process and the non-waivable list; vendor concentration and exit; incident severity and escalation | On appointment, before the first approval | Annual |
| All staff | Everyone with access to AI tools, including contractors | The [acceptable use standard](acceptable-use.md): approved tools, data classes that never go into unapproved tools, checking output before relying on it, disclosure duties, how to report a concern, an incident or shadow AI | On joining, before access to any AI tool | Annual, with attestation to the acceptable use standard |
| AI builders | Product owners, AI leads, technical owners, prompt engineers, AI Operations, engineers using AI coding assistants | The [governance workflow](../governance-operations/governance-workflow.md) and evidence pack; tiering and the override list; evaluation thresholds; prompt standards; red-team rules; logging and the kill switch; the coding assistant rules in the acceptable use standard | Before first assignment to an AI system | Annual, and when the framework changes materially |
| Human oversight reviewers | Reviewers under Patterns 1 to 3, agent plan approvers, kill switch operators | The five areas in [reviewer training](../responsible-ai/human-in-loop-patterns.md#reviewer-training) (capabilities and limits, failure modes, review criteria, feedback, escalation), plus automation bias and the specific system they review | Before acting as a reviewer for a system | Annual, and on any material change to the system they review |
| Second line and audit | AI Risk, Model Risk Management, Compliance, the DPO's team, Internal Audit | Challenging a tier; reading evaluation evidence and judge calibration; red-team reports; vendor assessments; regulatory mapping; testing the register controls | On joining | Annual |
| Others acting on the organisation's behalf | Contractors and outsourced staff who operate or use AI systems for the organisation | The all-staff module, plus the system module for any system they operate or review | Before access | Annual, or as the contract requires |

### System-specific training by tier

Training on the specific system a person reviews or operates scales with the tier (framework default):

| Tier | System-specific measure |
|---|---|
| T1 | System training with a knowledge check before the person acts as reviewer or operator; reviewer quality checks with known-bad outputs ([fatigue mitigation](../responsible-ai/human-in-loop-patterns.md#reviewer-fatigue-mitigation)) |
| T2 | System training with a knowledge check before the person acts as reviewer or operator |
| T3 | System briefing recorded by the system owner |
| T4 | None beyond the all-staff module |

---

## Content Every Module Covers

Depth changes by audience. These topics appear in every module:

- What AI and GenAI can and cannot do reliably: probabilistic output, hallucination, bias, and the limits of evaluation results.
- How data leaks through AI tools, and how prompt injection works.
- The organisation's [AI policy](../../templates/ai-policy.md), the acceptable use standard and where to find them.
- How to report a concern or an incident ([escalation paths](escalation-paths.md)).
- The legal duties that touch the role, for example disclosure to customers ([transparency standards](../responsible-ai/transparency-standards.md)).

---

## Ownership

| Role | Responsibility |
|---|---|
| Head of AI | Owns the programme and the curriculum, delivered through the CoE enablement function ([AI CoE design](ai-coe-design.md)) |
| AI Risk | Tracks completion by audience and reports it against the governance training completion KPI; owns the second-line module |
| Compliance | Supplies the regulatory content for every module |
| AI leads | Deliver system-specific training for the systems they lead (the Data Science Lead for traditional ML) |
| System owners | Keep the list of named reviewers and operators for their system and confirm each was trained before acting |
| HR or Learning and Development | Runs the learning platform and the completion records |
| AI Risk Committee chair | Arranges the board and executive sessions with the company secretary |

---

## Evidence (GV-002)

| Evidence | Held by |
|---|---|
| Curriculum mapped to each audience, with owner, version and last review date | Head of AI |
| Completion records by audience, from the learning platform | HR or Learning and Development |
| Attendance records for board and executive sessions | Company secretary |
| Training date for each named reviewer and operator, earlier than their first review or action | System owner |
| Knowledge check results for T1 and T2 system training | Head of AI |
| Quarterly completion report against the governance training completion target in [governance metrics](governance-metrics.md#governance-health-kpis) | AI Risk |

A reviewer or approver whose training has lapsed does not act in the role until it is renewed. Completion below target is reported to the AI Risk Committee.
