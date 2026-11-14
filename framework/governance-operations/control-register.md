# Control Register

This register maps every governance control in the framework to its evidence, owner, and escalation path. It is the single source of truth for what evidence an auditor, regulator, or compliance team should expect. Controls are grouped by the stages of the [governance workflow](governance-workflow.md), using the same stage numbers and names. "Applies To" names the tiers explicitly and matches the workflow's tier tables.

A control can only be bypassed through an approved exception: see [Exceptions and Risk Acceptance](governance-workflow.md#exceptions-and-risk-acceptance). Some controls are non-waivable.

For the end-to-end process connecting these stages, see [governance-workflow.md](governance-workflow.md). For a worked example, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md#control-coverage). It shows the evidence for every control that applies to that T1 GenAI RAG system and lists the controls that do not apply, with reasons.

The stage tables and the [Traceability](#traceability) section are generated from the YAML files in [controls/](../../controls/), which also record each control's type, automation level, key-control flag, test procedure and source documents. Do not edit the tables by hand. To change a control, edit its YAML file, run `python tools/build.py`, then run `python tools/check.py`. CI fails if a table no longer matches the YAML. See [tools/README.md](../../tools/README.md).

## Programme-Level Controls

These controls apply to the AI programme as a whole, not to one system: the AI policy, literacy, acceptable use, the exception register, the committee charter and the AI inventory. They are defined in [controls/stage-01-programme.yaml](../../controls/stage-01-programme.yaml) with stage 1 and group "Programme".

<!-- BEGIN GENERATED: controls-stage-01-programme. Edit controls/stage-01-programme.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| GV-001 | Board-approved AI policy, reviewed annually | Programme-wide (all tiers) | AI Risk Committee | AI policy approved by the board or the Board Risk Committee, with the approval minute, version history, annual review record and evidence that the policy was communicated to staff | Annual review; on a material change in regulation, strategy or risk appetite | Escalate to Board Risk Committee |
| GV-002 | AI literacy measures in place by role, with completion tracked | Programme-wide: board, executives, all staff, AI builders, human oversight reviewers, second line, and contractors who operate or use AI systems | Head of AI (programme and content) / AI Risk (completion tracking and reporting) | Role-based curriculum mapped to each audience; completion and attendance records by audience; training date for each named human oversight reviewer before first review; annual refresh log | On joining, on role change and before acting as a reviewer; refreshed annually; completion reported quarterly | Completion below the governance training target reported to AI Risk Committee. A reviewer or approver without current training does not act in the role until trained |
| GV-003 | Acceptable use policy for employee use of AI tools, with shadow AI detection | Programme-wide: all staff and contractors, and every AI tool used for work (public chatbots, enterprise assistants, AI coding assistants, AI features embedded in SaaS) | CISO (policy and approved tools list) / Security (shadow AI detection) | Approved acceptable use policy and approved tools list with permitted data classes; staff attestation records; monthly shadow AI detection reports with the outcome of each finding | Policy reviewed annually; approved tools list updated on change; detection continuous, reported monthly | Unapproved tool blocked or routed to intake; data sent to an unapproved tool handled as an incident per severity |
| GV-004 | Exception register maintained and reviewed monthly by the AI Risk Committee | T1-T4 (every approved exception) | AI Risk (maintains the register) / AI Risk Committee (monthly review) | Exception register holding every field required by the governance workflow for every exception at every tier; monthly AI Risk Committee minutes recording review of open, expiring and expired exceptions | Updated on every exception decision; reviewed monthly | An expired or unrecorded exception means the control it covers is failed; escalate to the tier approver and the AI Risk Committee |
| GV-005 | AI Risk Committee charter approved and reviewed annually | Programme-wide (all tiers) | AI Risk Committee | Charter approved by the Board Risk Committee setting purpose, membership, quorum, decision rights, delegation, escalation to the board, and minutes; annual review record | Annual review; on a change to membership or decision rights | Escalate to Board Risk Committee. A decision taken without quorum is retaken at a quorate meeting |
| GV-006 | AI inventory complete and reconciled quarterly, including shadow AI discovery | Programme-wide: every AI system and material AI feature, built, bought or embedded in vendor products | AI Risk | AI inventory with every required field for each entry; quarterly reconciliation record against procurement, cloud spend, SaaS admin consoles, network telemetry, code repositories and the model risk inventory, listing unmatched items and their resolution; inventory summary presented to the quarterly AI Risk Committee portfolio meeting | Maintained continuously; reconciled quarterly | Unregistered item registered and routed to intake, or switched off, within 30 days; an item that meets an automatic T1 override is reported to the AI Risk Committee chair at once |

<!-- END GENERATED: controls-stage-01-programme -->

## Stage 1: Idea Intake

No register controls. Intake produces the intake form, the initial risk screening and a `proposed` AI inventory entry. The entry is evidenced under RA-006 at Stage 2; see workflow Stage 1.

## Stage 2: Risk Assessment & Tiering

<!-- BEGIN GENERATED: controls-stage-02. Edit controls/stage-02-risk-assessment.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RA-001 | Risk assessment completed using framework matrices | T1-T4 | Product owner | Signed risk assessment with dimension scoring + tier determination | Before development begins | Cannot proceed to development |
| RA-002 | Tier override review against the canonical override list | T1-T4 (any system matching an override trigger, automatic T1 or minimum T2) | AI Risk | Override decision document | At assessment | Escalate to AI Risk Committee |
| RA-003 | Impact assessment completed | T1-T2 (T3: recommended) | Product owner | Completed impact assessment template | Before development; reviewed on material change | Cannot proceed to development |
| RA-004 | Risk assessment approved by appropriate authority | T1-T4 | AI Risk Committee (T1) / AI Risk, second line (T2) / Team lead (T3, T4: acknowledges self-assessment) | Approval record with sign-off | Before development | Block progression |
| RA-005 | DPIA screening and, where required, full DPIA | T1-T4 processing personal data: screening for all; full DPIA always for T1-T2 and wherever screening indicates high risk | DPO | DPIA screening record; filed DPIA with DPO sign-off where required | Before development | Cannot proceed; escalate to DPO |
| RA-006 | System registered in the AI inventory before development | T1-T4 | Product owner | Inventory entry with the required fields of the AI inventory standard, created before development started and updated at each later stage gate | Before development begins; updated at each stage gate | Cannot proceed to development |
| RA-007 | Prohibited-use screen recorded (non-waivable) | T1-T4 (every system, before scoring; non-waivable) | Product owner | Completed Step 0 screen in the risk assessment: each EU AI Act Art. 5 practice and each internal prohibited-use criterion answered, with a short rationale and the screen date | Before risk scoring; repeated on material change | Use rejected and does not proceed. Doubtful cases go to Compliance and Legal before any further work. Cannot be excepted |
| RA-008 | EU AI Act role determined and recorded | T1-T4 systems in scope of the EU AI Act (Art. 2(1)) | Compliance | Role record per system: provider, deployer or both; downstream user of a general-purpose AI model; the Art. 25(1) check (own name or trademark on a high-risk system, substantial modification, change of intended purpose that makes the system high-risk); and the obligation sets that follow from the role | At intake and on material change (with RV-003) | Cannot proceed to development; escalate to AI Risk Committee |
| RA-009 | Fundamental rights impact assessment completed and notified | Deployers in scope of EU AI Act Art. 27: Annex III point 5(b) and 5(c) systems, and any Annex III system except point 2 where the deployer is a body governed by public law or a private entity providing public services (usually T1 through override item 1) | Product owner (assessment) / Compliance (notification to the market surveillance authority) | Completed fundamental rights impact assessment section of the impact assessment template, covering Art. 27(1)(a) to (f), with cross-references to the DPIA where used; record of notification of the results to the market surveillance authority | Before first use (Annex III duties apply from 2 December 2027); updated when any Art. 27(1) element changes | Block deployment |

<!-- END GENERATED: controls-stage-02 -->

## Stage 3: Architecture & Design Review

<!-- BEGIN GENERATED: controls-stage-03. Edit controls/stage-03-architecture.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| AR-001 | System architecture documented | T1-T4 | Technical owner | Architecture document with component diagram and data flows | Before development | Block development |
| AR-002 | Architecture review sign-off | T1 (review board); T2 (team-level design review) | Architecture review board (T1) / Head of AI or delegate (T2) | T1: review board meeting record with decision and conditions. T2: recorded team-level design review approved by the Head of AI or delegate | Before development | Cannot proceed without sign-off |
| AR-003 | Data residency confirmed | T1-T4 with external data flows | Technical owner | Data flow map with residency confirmation per jurisdiction | Before development | Escalate to compliance |
| AR-004 | Vendor/model selection justified and approved | T1-T4 using external models | AI lead | Model selection document with evaluation results and rationale; approval by AI Risk Committee + CISO (T1), Head of AI (T2), team lead from the approved vendor list (T3/T4) | Before development | Block development |
| AR-005 | Third-party model risk assessment completed | T1-T3 using external vendor APIs (T4: approved vendors only, no separate assessment) | AI Risk | Completed vendor risk assessment | Before development; annually thereafter | Block deployment; procurement escalation |
| AR-006 | Agent identity, tool and permission review | T1-T2 agentic systems, including any system with tool access (every agentic system is at least T2) | Technical owner, with Security sign-off | Agent identity record for each agent (own non-human identity, named owner, credential lifetime, memory scope and retention); tool allowlist with per-tool scopes, pinned versions and definition hashes; delegation limits (scope, expiry, depth); caps and approval gates for consequential actions; sandbox configuration for code execution; inter-agent message authentication for multi-agent systems; approval record for the record and each later change | Before development; on any change to tools, scopes or delegation limits; re-checked at each formal review | Block development; a tool or scope change does not go live until approved |
| AR-007 | Vendor contract meets the AI clause set and is recorded in the register of information | T1-T4 using external models or AI vendors (T4: the approved vendor's contract); register of information entry for EU financial entities under DORA | Legal (contract terms) with AI Risk (clause check, register entry and fourth-party map) | Executed contract checked against the AI procurement clause set, with any gaps and their exception IDs; register of information entry (DORA Art. 28(3)) marking whether the service supports a critical or important function; fourth-party dependency map | Before production data is sent to the vendor; at renewal and on material change | Block deployment; procurement escalation |

<!-- END GENERATED: controls-stage-03 -->

## Stage 4: Development & Prompt Engineering

<!-- BEGIN GENERATED: controls-stage-04. Edit controls/stage-04-development.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DE-001 | Model card created and version-controlled | T1-T4 | AI lead | Model card in version control ([LLM model card](../../templates/llm-model-card.yaml) for GenAI) | Before validation | Block validation gate |
| DE-002 | Prompts version-controlled | T1-T4 GenAI | AI lead | Prompt files in git repository with commit history | Continuous | Block deployment |
| DE-003 | Prompt review completed per tier | T1-T3 GenAI (T3: peer review only; T4: self-review) | AI lead | Signed prompt review checklist + prompt version link. Reviewers for a new prompt or a major version: T1 peer review + prompt engineering lead + security review + AI Risk sign-off; T2 peer review + prompt engineering lead; T3 peer review. A minor version: peer review | Before release | Block deployment |
| DE-004 | Guardrails implemented and configured | T1-T2 GenAI (T3: recommended) | Technical owner | Guardrail configuration document + test results | Before deployment | Block deployment |
| DE-005 | Data governance controls applied to training/fine-tuning data | T1-T3 using fine-tuned models (T4: recommended) | AI lead | Data governance checklist with provenance documentation | Before training | Block training |
| DE-006 | AI interaction and exposure disclosure implemented | T1-T4 systems that interact directly with people, customer-facing or internal, unless the interaction is obvious under the EU AI Act Art. 50(1) test; any emotion recognition or biometric categorisation system (Art. 50(3)) | Product owner | Approved disclosure text per channel and language, with the legal basis (Art. 50(1), Art. 50(3), Korea AI Basic Act Art. 31(1) or framework policy); screenshot or automated UI test showing it is given at or before the first interaction or exposure; where the obvious-interaction exception is used, the recorded rationale | Before deployment; re-tested on any change to the channel or user interface | Block deployment |
| DE-007 | AI-generated content marked and labelled | T1-T4 GenAI systems the organisation provides that generate synthetic text, image, audio or video (Art. 50(2) marking), and systems whose output is published as a deep fake or as text informing the public on matters of public interest (Art. 50(4) labelling) | Technical owner (machine-readable marking) / Product owner (visible labels and disclosures) | Marking design (metadata fields and, for media, provenance standard such as C2PA) and detection test results on sample outputs; visible label rules by content destination; for each jurisdiction that applies (EU Art. 50(2) and 50(4), China labelling measures and GB 45438-2025, India IT Rules for intermediaries, Korea AI Basic Act Art. 31(2) and (3)), the rule applied or the exception relied on | Before deployment; re-tested on model or output format change. Generative systems placed on the market before 2 August 2026 must meet Art. 50(2) by 2 December 2026 | Block deployment |
| DE-008 | Retrieval enforces source permissions | T1-T4 RAG systems whose sources carry access restrictions | Technical owner | Access control design: document-level permissions carried from each source into the index, and a filter on the requesting user's identity applied at query time before documents enter the context; pre-deployment test results with test identities holding different entitlements, showing no cross-entitlement retrieval | Before deployment; re-tested on any change to sources, index, retrieval logic or identity integration | Block deployment |
| DE-009 | Notice given to people subject to AI-assisted decisions | T1-T4 systems that make or assist decisions about people where a notice duty applies: EU AI Act Art. 26(11) (Annex III systems) and Art. 26(7) (workplace use), Colorado SB 26-189, CPPA ADMT rules, Quebec Law 25 s. 12.1, Australia APP 1.7 to 1.9 (usually T1 through override item 1) | Product owner | Notice pack per system: each notice that applies, its legal basis, approved text and where and when it is given in the customer or employee journey; privacy policy wording on automated decisions where required; for workplace high-risk systems, record that workers' representatives and affected workers were informed before use | Before deployment; reviewed on material change and when a new jurisdiction applies | Block deployment |

<!-- END GENERATED: controls-stage-04 -->

## Stage 5: Evaluation & Testing

<!-- BEGIN GENERATED: controls-stage-05. Edit controls/stage-05-evaluation.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| EV-001 | Pre-release evaluation suite executed | T1-T4 | AI lead | Evaluation report with pass/fail per metric | Before every deployment | Block deployment |
| EV-002 | Safety evaluation passed | T1-T4 GenAI (T4: automated, 20+ cases) | AI lead | Safety eval results meeting tier thresholds | Before every deployment | Block deployment |
| EV-003 | Regression evaluation passed | T1-T2 on model/prompt change (T3: recommended) | AI lead | Regression report comparing current vs. previous version | On change | Block deployment if regression detected; a T1/T2 safety regression proceeds only under an exception from the tier exception approver, not a delegate |
| EV-004 | RAG retrieval quality evaluated | T1-T3 RAG systems (T4: recommended) | AI lead | Retrieval precision/recall/relevance metrics | Before deployment; then weekly (T1), monthly (T2), quarterly (T3) | Block deployment (pre-release); investigate (production) |
| EV-005 | Bias evaluation completed | T1-T2 (T3: recommended) | Responsible AI lead | Counterfactual test results with demographic parity metrics | Formal evaluation before deployment, then quarterly (T1) or semi-annual (T2); production counterfactual spot-checks weekly (T1) or monthly (T2) | Block deployment; escalate to Responsible AI |
| EV-006 | Eval dataset integrity verified | T1-T4 | AI lead | Confirmation of no overlap with training data; dataset version recorded | Before each eval run | Invalidate eval results; re-run |
| EV-007 | LLM-as-judge calibrated against human evaluators | T1-T2 using automated eval | AI lead | Calibration report with correlation scores | Quarterly (T1); semi-annually (T2) | Pause automated eval; revert to human eval |
| EV-008 | Agent evaluation passed | T1-T2 agentic systems (every agentic system is minimum T2) | AI lead | Agent evaluation report on a versioned suite of multi-step tasks; task success, tool-call accuracy, unsafe or out-of-policy actions, tool-error recovery and the human trajectory review | Before every deployment; on any change to the model, prompt, tools or permissions | Block deployment; any unsafe or out-of-policy action in the suite blocks release |
| EV-009 | Guardrail evaluation passed | T1-T3 GenAI systems with guardrails | AI lead | Guardrail evaluation report; false negative and false positive rates on labelled harmful or out-of-scope and legitimate sets, with set and guardrail configuration versions | Before deployment; on every guardrail configuration change | Block deployment |

<!-- END GENERATED: controls-stage-05 -->

## Stage 6: Security Review & Red-Teaming

<!-- BEGIN GENERATED: controls-stage-06. Edit controls/stage-06-security.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| SR-001 | Red-team testing completed per tier depth | T1-T3 GenAI (T4: automated scan recommended) | Security / AI Risk | Red-team report. Depth: T1 200+ cases including manual testing; T2 100+; T3 automated scan + 50 manual cases | Pre-deployment; per [red-teaming protocol](../ai-security/red-teaming-protocol.md) cadence | Block deployment |
| SR-002 | No unresolved Critical or High findings | T1-T2: 0 Critical, 0 unaddressed High. T3-T4: 0 Critical (High needs recorded risk acceptance) | System owner | Red-team report showing 0 Critical and, for T1-T2, 0 unaddressed High | Before deployment | Block deployment. Unresolved Critical findings cannot be excepted |
| SR-003 | Adversarial robustness defenses implemented | T1-T2 GenAI (T3: recommended) | Technical owner | Defense configuration documentation | Before deployment | Block deployment |
| SR-004 | Supply chain security verified | T1-T3 using open-source models (T4: recommended) | Security | AI-BOM + provenance verification | Before deployment; on model change | Block deployment |

<!-- END GENERATED: controls-stage-06 -->

## Stage 7: Deployment Approval

<!-- BEGIN GENERATED: controls-stage-07. Edit controls/stage-07-deployment.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DA-001 | Evidence pack assembled and complete | T1-T4 | Product owner | Evidence checklist against the [minimum evidence pack](governance-workflow.md#minimum-evidence-pack-by-tier) | Before deployment | Block deployment |
| DA-002 | Sign-off chain completed per tier | T1-T4 | Product owner | Signed deployment approval record. Approvers: T1 AI Risk Committee + CISO (+ DPO if personal data is processed); T2 Head of AI + Business Unit Head; T3 team lead + business owner; T4 team lead | Before deployment | Block deployment |
| DA-003 | Deployment gates passed | T1-T4 | AI Operations | Gate evidence package | Before deployment | Block deployment |
| DA-004 | Rollback plan documented and tested | T1-T2 | Technical owner | Rollback procedure + test evidence | Before deployment | Block deployment |

<!-- END GENERATED: controls-stage-07 -->

## Stage 8: Production Operations

<!-- BEGIN GENERATED: controls-stage-08. Edit controls/stage-08-operations.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| PM-001 | Monitoring configured per tier requirements | T1-T4 (T4: basic usage and error monitoring) | AI Operations | Monitoring configuration + dashboard reference | Before traffic enabled | Block go-live |
| PM-002 | Alerting active with defined thresholds | T1-T3 (T4: covered by platform-level budget alerts) | AI Operations | Alert configuration evidence | Before traffic enabled | Block go-live |
| PM-003 | Human oversight operational | T1-T2 | Product owner | Oversight process document per the [pattern selection matrix](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) + staffing confirmation | Before traffic enabled | Block go-live |
| PM-004 | Production evaluation running per cadence | T1-T4 | AI Operations | Schedule and latest results for online automated scoring, metrics review and full offline suite re-run | Per tier cadence (workflow Stage 8) | Escalate to AI Risk; increase monitoring |
| PM-005 | Cost monitoring active | T1-T3 (T4: covered by platform-level budget alerts) | AI Operations | Cost dashboard + alert configuration | Before traffic enabled | Block go-live |
| PM-006 | Kill switch tested | T1 customer-facing systems and all agentic systems (T1-T2) | AI Operations | Kill switch runbook; quarterly test record showing the decision time, the time stop or degrade was confirmed (within 15 minutes) and, for agentic systems, that revoked credentials were refused | Before traffic enabled; at least quarterly; after any change to the runtime or agent identity set-up | Block go-live; a live system is restricted or switched off until a test passes. Cannot be excepted (non-waivable) |
| PM-007 | Audit logging complete and retained | T1-T4 (agent action records for agentic systems) | AI Operations | Audit log configuration covering the per-request record and, for agentic systems, the agent action audit record; retention set to the tier period; completeness and integrity check results | Before traffic enabled; completeness checked in real time, integrity daily | Block go-live; a gap in a live system is raised as an incident and fixed. Cannot be excepted (non-waivable) |
| PM-008 | Fallback model switch tested | T1 systems using external models | AI Operations | Fallback test record for each quarter: date, time taken to switch, and the evaluation result on the fallback model | At least quarterly from go-live | Escalate to AI Risk; the system counts as having no tested fallback until a test passes, and its third-party model dependency score is reviewed |

<!-- END GENERATED: controls-stage-08 -->

### Stage 8 sub-group: Incident Response

Severity, response SLAs and notifications: [escalation paths](../operating-model/escalation-paths.md#severity-classification).

<!-- BEGIN GENERATED: controls-stage-08-incident-response. Edit controls/stage-08-operations.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| IR-001 | Incident response playbook documented | T1-T2 | AI Operations | Published runbook accessible to on-call | Before deployment | Block deployment |
| IR-002 | On-call team assigned | T1-T2 | AI Operations | On-call rotation schedule | Continuous | Escalate to AI Platform Lead |
| IR-003 | Incident reported and handled per severity SLA | T1-T4 (on incident) | Incident commander | Incident report per template, with root cause: S1/S2 within 48 hours, S3 within 10 business days | Per incident. Response SLA by severity: S1 15 minutes, S2 4 hours, S3 24 hours, S4 next business day | Escalate per escalation paths |
| IR-004 | Post-mortem completed for S1/S2 incidents | T1-T4 (S1 and S2 incidents) | Incident commander | Post-mortem report | Within 1 week (S1) / 2 weeks (S2) | Escalate to AI Risk Committee |
| IR-005 | Remediation actions tracked to completion | T1-T4 (incidents with remediation actions) | System owner | Remediation tracker with status; S4 items tracked in the backlog | Until complete | Escalate to AI Risk |
| IR-006 | Regulatory incident notification assessed | T1-T4 (every S1 and S2 incident, and any suspected serious incident under the EU AI Act) | Compliance | Notification assessment per incident: regimes considered (EU AI Act Art. 73 and Art. 26(5), DORA major ICT-related incident, GDPR Arts. 33 and 34, other applicable regimes), decision and rationale, Legal review, and each notification made with its deadline and time sent | Per incident: started when the incident is declared, completed within 24 hours of an S1 and before the earliest legal deadline that could apply | Escalate immediately to Legal and the AI Risk Committee chair |

<!-- END GENERATED: controls-stage-08-incident-response -->

## Stage 9: Ongoing Governance

<!-- BEGIN GENERATED: controls-stage-09. Edit controls/stage-09-review.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| RV-001 | Formal governance review completed | T1-T4 | System owner | Review record with findings, actions and risk re-assessment (re-tiering check) | Quarterly (T1); semi-annual (T2); annual (T3); annual self-assessment (T4) | Overdue review flagged in governance metrics; escalate after 30 days |
| RV-002 | Model card updated | T1-T4 | AI lead | Updated model card with current information | At each review | Block until updated |
| RV-003 | Revalidation on material change | T1-T4 | AI lead | Revalidation assessment + eval results | On material change (model, provider, major prompt version, scope, data, autonomy or regulation). Independent revalidation also annual (T1) and every 24 months (T2) | Re-enter deployment gates |
| RV-004 | Regulatory change impact assessed | T1-T3 (T4: recommended) | Compliance | Regulatory change impact assessment | On regulatory change | Escalate to AI Risk Committee |
| RV-005 | Explanation and human review provided for adverse outcomes | T1-T4 systems that make or support decisions with legal or similarly significant effects on people (EU AI Act Art. 86, GDPR Art. 22(3), Colorado SB 26-189, CPPA ADMT rules, Quebec Law 25 s. 12.1); usually T1 through override item 1 | System owner | Request log per system: date received, request type (explanation, human review, contest, access), decision reference, date answered against the deadline that applies, the explanation sent, and the human review outcome (upheld or changed) with the reviewer's name. The log also records explanations the law requires without a request (Colorado: within 30 days of an adverse outcome). Deadline: the shortest statutory period that applies (for example one month under GDPR Art. 12(3)); framework default 30 days where none applies | On each request or adverse outcome that triggers a duty; log reviewed at each formal review (RV-001) | Escalate to Compliance; a missed statutory deadline is recorded as a compliance breach |

<!-- END GENERATED: controls-stage-09 -->

## Stage 10: Deprecation & Retirement

<!-- BEGIN GENERATED: controls-stage-10. Edit controls/stage-10-retirement.yaml, then run python tools/build.py -->

| Control ID | Control | Applies To | Owner | Evidence | Frequency | Escalation if Failed |
|---|---|---|---|---|---|---|
| DR-001 | Deprecation impact assessment completed | T1-T4 systems being deprecated | System owner | Impact assessment with affected systems and migration plan | At deprecation trigger | Block deprecation without assessment |
| DR-002 | Migration governance followed | T1-T2 systems being replaced (T3: recommended) | AI lead | Migration assessment + parallel running evidence + cutover approval | During migration | Block cutover |
| DR-003 | Evidence archived per retention policy | T1-T4 deprecated systems | AI Operations | Archival confirmation with artifact inventory | At retirement | Compliance escalation |
| DR-004 | System decommissioned cleanly | T1-T3 retired systems (T4: recommended) | Technical owner | Decommission record (monitoring removed, access revoked, documentation archived) | At retirement | Track until complete |

<!-- END GENERATED: controls-stage-10 -->

---

## Summary

This register contains 71 controls: 6 programme-level controls and 65 grouped under stages 2 to 10 of the governance workflow (Stage 1, Idea Intake, has no register controls). For the full governance workflow describing how systems progress through these stages, see [governance-workflow.md](governance-workflow.md). For a worked example, see the [customer service chatbot governance case file](../../examples/customer-service-chatbot/governance-case-file.md#control-coverage): it shows the evidence for every control that applies to that T1 GenAI RAG system and lists the controls that do not apply, with reasons.

## Traceability

For each control: the framework documents that define the requirement (the `sources` field in its YAML file), and which regulatory mapping documents cite its ID. The table is rebuilt from a scan of those four documents, so it changes when a mapping adds or drops a control.

<!-- BEGIN GENERATED: traceability. Edit controls/*.yaml, then run python tools/build.py -->

| Control | Source documents | [EU AI Act](../compliance/eu-ai-act-mapping.md) | [NIST AI RMF](../compliance/nist-ai-rmf-mapping.md) | [ISO/IEC 42001](../compliance/iso-42001-mapping.md) | [Multi-jurisdictional](../compliance/multi-jurisdictional-guide.md) |
|---|---|---|---|---|---|
| GV-001 | [ai-policy.md](../../templates/ai-policy.md), [board-reporting.md](../operating-model/board-reporting.md) |  | Yes | Yes |  |
| GV-002 | [ai-literacy.md](../operating-model/ai-literacy.md), [governance-metrics.md](../operating-model/governance-metrics.md), [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md) | Yes | Yes | Yes |  |
| GV-003 | [acceptable-use.md](../operating-model/acceptable-use.md), [third-party-model-risk.md](../compliance/third-party-model-risk.md), [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md) |  | Yes | Yes |  |
| GV-004 | [exception-register.md](../../templates/exception-register.md), [governance-workflow.md](governance-workflow.md), [review-cadence.md](../operating-model/review-cadence.md) |  | Yes | Yes |  |
| GV-005 | [ai-risk-committee-charter.md](../../templates/ai-risk-committee-charter.md), [review-cadence.md](../operating-model/review-cadence.md), [roles-responsibilities.md](../operating-model/roles-responsibilities.md) |  | Yes | Yes |  |
| GV-006 | [ai-inventory.md](ai-inventory.md), [ai-inventory-entry.yaml](../../templates/ai-inventory-entry.yaml), [transparency-standards.md](../responsible-ai/transparency-standards.md) |  | Yes | Yes | Yes |
| RA-001 | [governance-workflow.md](governance-workflow.md), [risk-matrix.md](../risk-classification/risk-matrix.md), [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md) | Yes | Yes | Yes | Yes |
| RA-002 | [governance-workflow.md](governance-workflow.md), [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md) |  | Yes | Yes | Yes |
| RA-003 | [governance-workflow.md](governance-workflow.md) | Yes | Yes | Yes | Yes |
| RA-004 | [governance-workflow.md](governance-workflow.md), [roles-responsibilities.md](../operating-model/roles-responsibilities.md) |  | Yes | Yes | Yes |
| RA-005 | [governance-workflow.md](governance-workflow.md), [responsible-ai-checklist.md](../compliance/responsible-ai-checklist.md) | Yes | Yes | Yes | Yes |
| RA-006 | [ai-inventory.md](ai-inventory.md), [governance-workflow.md](governance-workflow.md) |  |  |  | Yes |
| RA-007 | [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md), [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [governance-workflow.md](governance-workflow.md) | Yes |  |  | Yes |
| RA-008 | [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [governance-workflow.md](governance-workflow.md) | Yes |  |  | Yes |
| RA-009 | [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [impact-assessment-template.md](../../templates/impact-assessment-template.md) | Yes |  |  | Yes |
| AR-001 | [governance-workflow.md](governance-workflow.md) | Yes | Yes | Yes |  |
| AR-002 | [governance-workflow.md](governance-workflow.md), [roles-responsibilities.md](../operating-model/roles-responsibilities.md) |  | Yes |  |  |
| AR-003 | [governance-workflow.md](governance-workflow.md), [cross-border-data-governance.md](../compliance/cross-border-data-governance.md) |  | Yes | Yes | Yes |
| AR-004 | [governance-workflow.md](governance-workflow.md), [model-selection.md](../llm-lifecycle/model-selection.md) | Yes | Yes | Yes | Yes |
| AR-005 | [governance-workflow.md](governance-workflow.md), [third-party-model-risk.md](../compliance/third-party-model-risk.md) | Yes | Yes | Yes | Yes |
| AR-006 | [agent-identity-and-tool-governance.md](../llm-lifecycle/agent-identity-and-tool-governance.md), [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md), [multi-agent-governance.md](../llm-lifecycle/multi-agent-governance.md) |  | Yes |  |  |
| AR-007 | [ai-procurement-clauses.md](../compliance/ai-procurement-clauses.md), [third-party-model-risk.md](../compliance/third-party-model-risk.md), [cross-border-data-governance.md](../compliance/cross-border-data-governance.md) |  |  |  | Yes |
| DE-001 | [governance-workflow.md](governance-workflow.md), [development.md](../model-lifecycle/development.md) | Yes | Yes | Yes |  |
| DE-002 | [governance-workflow.md](governance-workflow.md), [prompt-engineering-standards.md](../llm-lifecycle/prompt-engineering-standards.md) |  |  |  |  |
| DE-003 | [governance-workflow.md](governance-workflow.md), [prompt-engineering-standards.md](../llm-lifecycle/prompt-engineering-standards.md) |  |  |  | Yes |
| DE-004 | [governance-workflow.md](governance-workflow.md), [adversarial-robustness.md](../ai-security/adversarial-robustness.md) |  | Yes | Yes | Yes |
| DE-005 | [governance-workflow.md](governance-workflow.md), [fine-tuning-governance.md](../llm-lifecycle/fine-tuning-governance.md) | Yes | Yes | Yes |  |
| DE-006 | [transparency-standards.md](../responsible-ai/transparency-standards.md), [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [multi-jurisdictional-guide.md](../compliance/multi-jurisdictional-guide.md) | Yes |  |  | Yes |
| DE-007 | [transparency-standards.md](../responsible-ai/transparency-standards.md), [multimodal-governance.md](../llm-lifecycle/multimodal-governance.md), [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [multi-jurisdictional-guide.md](../compliance/multi-jurisdictional-guide.md) | Yes |  |  | Yes |
| DE-008 | [rag-governance.md](../llm-lifecycle/rag-governance.md), [governance-workflow.md](governance-workflow.md) | Yes |  |  |  |
| DE-009 | [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [multi-jurisdictional-guide.md](../compliance/multi-jurisdictional-guide.md), [transparency-standards.md](../responsible-ai/transparency-standards.md) | Yes |  |  | Yes |
| EV-001 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md), [validation.md](../model-lifecycle/validation.md) | Yes | Yes | Yes | Yes |
| EV-002 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md) | Yes | Yes |  |  |
| EV-003 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md) | Yes |  |  |  |
| EV-004 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md), [rag-governance.md](../llm-lifecycle/rag-governance.md) | Yes | Yes | Yes |  |
| EV-005 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md), [bias-detection-llm.md](../responsible-ai/bias-detection-llm.md) | Yes | Yes | Yes | Yes |
| EV-006 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md) | Yes | Yes | Yes |  |
| EV-007 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md) |  | Yes |  |  |
| EV-008 | [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md), [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md) | Yes | Yes |  |  |
| EV-009 | [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md), [adversarial-robustness.md](../ai-security/adversarial-robustness.md) | Yes | Yes | Yes | Yes |
| SR-001 | [governance-workflow.md](governance-workflow.md), [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md) | Yes | Yes | Yes | Yes |
| SR-002 | [governance-workflow.md](governance-workflow.md), [red-teaming-protocol.md](../ai-security/red-teaming-protocol.md) | Yes | Yes |  |  |
| SR-003 | [governance-workflow.md](governance-workflow.md), [adversarial-robustness.md](../ai-security/adversarial-robustness.md) | Yes | Yes | Yes | Yes |
| SR-004 | [governance-workflow.md](governance-workflow.md), [supply-chain-security.md](../ai-security/supply-chain-security.md), [open-source-model-governance.md](../llm-lifecycle/open-source-model-governance.md) | Yes | Yes | Yes | Yes |
| DA-001 | [governance-workflow.md](governance-workflow.md) | Yes | Yes | Yes |  |
| DA-002 | [governance-workflow.md](governance-workflow.md), [roles-responsibilities.md](../operating-model/roles-responsibilities.md), [deployment-gates.md](../llm-lifecycle/deployment-gates.md) | Yes | Yes | Yes |  |
| DA-003 | [governance-workflow.md](governance-workflow.md), [deployment-gates.md](../llm-lifecycle/deployment-gates.md), [deployment.md](../model-lifecycle/deployment.md) | Yes | Yes | Yes |  |
| DA-004 | [governance-workflow.md](governance-workflow.md), [deployment.md](../model-lifecycle/deployment.md) | Yes | Yes | Yes |  |
| PM-001 | [governance-workflow.md](governance-workflow.md), [llm-lifecycle/monitoring.md](../llm-lifecycle/monitoring.md), [model-lifecycle/monitoring.md](../model-lifecycle/monitoring.md) | Yes | Yes | Yes |  |
| PM-002 | [governance-workflow.md](governance-workflow.md), [llm-lifecycle/monitoring.md](../llm-lifecycle/monitoring.md), [model-lifecycle/monitoring.md](../model-lifecycle/monitoring.md) | Yes | Yes | Yes |  |
| PM-003 | [governance-workflow.md](governance-workflow.md), [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md) | Yes | Yes | Yes | Yes |
| PM-004 | [governance-workflow.md](governance-workflow.md), [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md), [llm-lifecycle/monitoring.md](../llm-lifecycle/monitoring.md) | Yes | Yes | Yes |  |
| PM-005 | [governance-workflow.md](governance-workflow.md), [cost-governance.md](../operating-model/cost-governance.md) |  | Yes | Yes |  |
| PM-006 | [agent-identity-and-tool-governance.md](../llm-lifecycle/agent-identity-and-tool-governance.md), [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md), [governance-workflow.md](governance-workflow.md) |  |  |  |  |
| PM-007 | [prompt-audit-trail.md](../compliance/prompt-audit-trail.md), [audit-trail-requirements.md](../compliance/audit-trail-requirements.md), [agent-identity-and-tool-governance.md](../llm-lifecycle/agent-identity-and-tool-governance.md), [governance-workflow.md](governance-workflow.md) | Yes |  |  |  |
| PM-008 | [third-party-model-risk.md](../compliance/third-party-model-risk.md), [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md) |  |  |  |  |
| IR-001 | [governance-workflow.md](governance-workflow.md), [escalation-paths.md](../operating-model/escalation-paths.md) |  | Yes |  |  |
| IR-002 | [governance-workflow.md](governance-workflow.md), [escalation-paths.md](../operating-model/escalation-paths.md) |  |  |  |  |
| IR-003 | [governance-workflow.md](governance-workflow.md), [escalation-paths.md](../operating-model/escalation-paths.md) | Yes |  | Yes |  |
| IR-004 | [governance-workflow.md](governance-workflow.md), [escalation-paths.md](../operating-model/escalation-paths.md), [incident-forensics.md](../operating-model/incident-forensics.md) |  | Yes | Yes |  |
| IR-005 | [governance-workflow.md](governance-workflow.md), [escalation-paths.md](../operating-model/escalation-paths.md) | Yes | Yes | Yes |  |
| IR-006 | [escalation-paths.md](../operating-model/escalation-paths.md), [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md) | Yes |  |  |  |
| RV-001 | [governance-workflow.md](governance-workflow.md), [review-cadence.md](../operating-model/review-cadence.md) | Yes | Yes | Yes | Yes |
| RV-002 | [governance-workflow.md](governance-workflow.md) | Yes |  |  |  |
| RV-003 | [governance-workflow.md](governance-workflow.md), [validation.md](../model-lifecycle/validation.md), [review-cadence.md](../operating-model/review-cadence.md) | Yes | Yes | Yes | Yes |
| RV-004 | [governance-workflow.md](governance-workflow.md), [regulatory-change-monitoring.md](../compliance/regulatory-change-monitoring.md) | Yes | Yes | Yes |  |
| RV-005 | [eu-ai-act-mapping.md](../compliance/eu-ai-act-mapping.md), [multi-jurisdictional-guide.md](../compliance/multi-jurisdictional-guide.md), [transparency-standards.md](../responsible-ai/transparency-standards.md), [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md) | Yes |  |  | Yes |
| DR-001 | [governance-workflow.md](governance-workflow.md), [model-deprecation-governance.md](../llm-lifecycle/model-deprecation-governance.md) |  | Yes | Yes |  |
| DR-002 | [governance-workflow.md](governance-workflow.md), [model-deprecation-governance.md](../llm-lifecycle/model-deprecation-governance.md) |  | Yes |  |  |
| DR-003 | [governance-workflow.md](governance-workflow.md), [model-deprecation-governance.md](../llm-lifecycle/model-deprecation-governance.md), [audit-trail-requirements.md](../compliance/audit-trail-requirements.md) | Yes |  | Yes |  |
| DR-004 | [governance-workflow.md](governance-workflow.md), [model-deprecation-governance.md](../llm-lifecycle/model-deprecation-governance.md) |  | Yes | Yes |  |

Controls cited by no regulatory mapping: DE-002, PM-006, PM-008, IR-002.

<!-- END GENERATED: traceability -->
