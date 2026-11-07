# Start Here

This framework is large, and nobody needs all of it on day one. Pick the path that matches your job, read the documents in order, and stop when you have what you need. Two documents carry the rest: the [governance workflow](framework/governance-operations/governance-workflow.md) is the process, and the [control register](framework/governance-operations/control-register.md) is the evidence. Every other document adds detail to a stage or a control.

- [Reading paths](#reading-paths): builder, risk and audit, executive
- [Should this use GenAI at all?](#should-this-use-genai-at-all)
- [Minimum viable governance: the first 30 days](#minimum-viable-governance-the-first-30-days)
- [A 6-week path for a GenAI system](#a-6-week-path-for-a-genai-system)
- [Fast lane for T3 and T4](#fast-lane-for-t3-and-t4)
- [Small teams](#small-teams)

## Reading Paths

### Builder: You Are Shipping an AI or GenAI System

1. [Governance workflow](framework/governance-operations/governance-workflow.md): the one process from intake to retirement. Read Stage 2, the minimum evidence pack under Stage 7, and the Fast Lane and Small Teams sections. Skim the rest.
2. [When to say no](framework/governance-operations/when-to-say-no.md): check that the use case should be GenAI at all before you spend time assessing it.
3. [GenAI risk matrix](framework/risk-classification/genai-risk-matrix.md): the Step 0 screen, the five dimensions and the override list. Your tier decides everything downstream.
4. [GenAI use case assessment](templates/genai-use-case-assessment.md): the risk assessment you submit (RA-001). Start with section 0.
5. [Evaluation governance](framework/llm-lifecycle/evaluation-governance.md): suite sizes, thresholds and release criteria by tier. Start the eval sets early: they need labelled answers from the people who own the content. At T1 and T2 a metric passes on its 95% confidence bound, so a T1 pre-release or safety suite needs at least 300 cases, and more if you expect any failures.
6. [Prompt engineering standards](framework/llm-lifecycle/prompt-engineering-standards.md): version control and review rules for prompts (DE-002, DE-003), with reviewers by tier.
7. [Red-teaming protocol](framework/ai-security/red-teaming-protocol.md): testing depth by tier, and why the build team never red-teams its own system.
8. [Control register](framework/governance-operations/control-register.md): owner, evidence and escalation for every control. Use it as the checklist when you assemble the evidence pack.

Add if they apply: [RAG governance](framework/llm-lifecycle/rag-governance.md) for retrieval systems, [agentic AI risk](framework/risk-classification/agentic-ai-risk.md) for anything with tools, and the [pattern selection matrix](framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) for output that reaches customers or other external parties. For traditional ML, read the [risk matrix](framework/risk-classification/risk-matrix.md) in place of 3, and the [development](framework/model-lifecycle/development.md) and [validation](framework/model-lifecycle/validation.md) standards in place of 5 to 7.

### Risk, Compliance and Audit: Second Line, CRO Office, Internal Audit

1. [Control register](framework/governance-operations/control-register.md): the evidence to expect for each control, who owns it and what happens when it fails.
2. [Governance workflow](framework/governance-operations/governance-workflow.md): gates, approvers by tier, the minimum evidence pack, exceptions and the non-waivable list, and retroactive governance for systems already live.
3. [Roles and responsibilities](framework/operating-model/roles-responsibilities.md): approvals by tier, lines of defence and separation of duties.
4. [GenAI risk matrix](framework/risk-classification/genai-risk-matrix.md): the tiering rule and the canonical override list, which are the basis for challenging a tier.
5. [Evaluation governance](framework/llm-lifecycle/evaluation-governance.md): what "passed" means. Thresholds, release criteria and who validates at each tier.
6. [Third-party model risk](framework/compliance/third-party-model-risk.md): vendor assessment depth by tier, exit strategy, and the DORA and SR 26-2 hooks.
7. [EU AI Act mapping](framework/compliance/eu-ai-act-mapping.md): obligations by role and application dates, with gaps marked "No control yet".
8. [T1 governance case file](examples/customer-service-chatbot/governance-case-file.md): a complete evidence trail for a T1 GenAI system, to test your expectations against.

For internal audit planning, add [GRC integration](framework/operating-model/grc-integration.md) (audit universe and procedures). For other regimes, see the [NIST AI RMF](framework/compliance/nist-ai-rmf-mapping.md) and [ISO/IEC 42001](framework/compliance/iso-42001-mapping.md) mappings and the [multi-jurisdictional guide](framework/compliance/multi-jurisdictional-guide.md).

### Executive and Board

1. [Board reporting](framework/operating-model/board-reporting.md): what the quarterly report covers, which incidents reach the board and how fast, and the risk appetite statement the board approves.
2. [Governance metrics](framework/operating-model/governance-metrics.md): the KPIs that show whether governance is working, with targets.
3. [Risk tiers](framework/risk-classification/genai-risk-matrix.md#risk-tier-determination-for-genai): the four tiers, what puts a system in T1, and the governance each tier carries.
4. [EU AI Act application dates](framework/compliance/eu-ai-act-mapping.md#application-dates): the dates that drive the compliance roadmap.

## Should This Use GenAI at All?

Before anyone scores a risk dimension, answer the eight questions in [section 0 of the use case assessment](templates/genai-use-case-assessment.md#0-should-this-use-genai-at-all). They come from [when to say no](framework/governance-operations/when-to-say-no.md), which sets out where GenAI, an agent or an external model API is the wrong tool: figures with legal effect, adverse regulated decisions, agent actions that cannot be undone, data flows you cannot evidence, quality you cannot measure, prohibited practices, problems a simpler method solves, and critical processes tied to one vendor.

## Minimum Viable Governance: The First 30 Days

For an organisation with no AI governance in place. By day 30 you should know what AI you run and how risky each system is, have your highest-risk system moving through the workflow, have new work arriving through the templates, and have a committee that can make decisions. Everything else can wait until those are in place.

**1. Inventory what exists (week 1).**
- List every AI and GenAI system in production or pilot, including vendor tools with AI features that staff use for work.
- For each, record the fields in the [AI system inventory](framework/responsible-ai/transparency-standards.md#ai-system-inventory) and name one Business owner, one Product owner and one AI lead ([accountability principles](framework/operating-model/roles-responsibilities.md#accountability-principles)).
- Charter the AI Risk Committee now so it can meet by day 30 (step 5).

**2. Tier it with the matrices (weeks 1 to 2).**
- Run the [Step 0 prohibited-use screen](framework/risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen). Anything prohibited stops here.
- Score each system with the [GenAI](framework/risk-classification/genai-risk-matrix.md), [traditional ML](framework/risk-classification/risk-matrix.md), [agentic](framework/risk-classification/agentic-ai-risk.md) or [multimodal](framework/risk-classification/multimodal-risk-matrix.md) matrix, then check every item on the [override list](framework/risk-classification/genai-risk-matrix.md#tier-override-rules). The highest-scoring dimension sets the tier, so a first pass is quick.
- Record the tier and the reasoning in the [GenAI use case assessment](templates/genai-use-case-assessment.md) or the [assessment template](framework/risk-classification/assessment-template.yaml).
- Look for non-waivable gaps first: audit logging, a kill switch for T1 customer-facing and all agentic systems, the prohibited-use check, a DPIA where the law requires one, and unresolved Critical red-team findings ([non-waivable list](framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance)). None of these can be excepted. For a live system missing one, the choices are to fix it fast, restrict the system, or switch it off.

**3. Apply the workflow to the highest-risk system (weeks 2 to 4).**
- Pick one T1 system, or your highest-tier system if you have no T1.
- Follow [Retroactive Governance](framework/governance-operations/governance-workflow.md#retroactive-governance): walk the [control register](framework/governance-operations/control-register.md) and mark each control as evidence exists, evidence missing, or not applicable.
- Write the remediation plan: who produces each missing item, by when, and what interim mitigation covers the gap. The framework's deadlines are 3 months for T1, 6 for T2 and 12 for T3 and T4.
- Aim to end the month with a gap matrix and a dated plan for this system. The full evidence pack follows on the retroactive timeline. The [T1 case file](examples/customer-service-chatbot/governance-case-file.md) shows what a complete one looks like.

**4. Adopt the templates (week 3).**
- From now on, every new AI system enters through the [GenAI use case assessment](templates/genai-use-case-assessment.md), or the [assessment template](framework/risk-classification/assessment-template.yaml) for traditional ML.
- Make these the defaults: the [LLM model card](templates/llm-model-card.yaml) or [model card](templates/model-card-template.yaml), the [prompt review checklist](templates/prompt-review-checklist.md), and the [GenAI](templates/incident-report-genai.md) and [traditional ML](templates/incident-report-template.md) incident reports.
- Leave the red-team report and board report templates until you need them.

**5. Stand up the committee (first meeting by day 30).**
- The AI Risk Committee is chaired by the CRO, with the membership in [review cadence](framework/operating-model/review-cadence.md#monthly-ai-risk-committee). It meets monthly, with a quarterly full-portfolio meeting.
- First meeting: approve the tiers of T1 systems, approve the remediation plan from step 3, open the [exception register](framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance) for live systems that cannot yet meet a control, and confirm who in the second line approves T2 risk assessments (AI Risk) and performs T2 validation (MRM or another second-line reviewer).
- Ask AI Risk to draft the [risk appetite statement](framework/operating-model/board-reporting.md#ai-risk-appetite-statement) for the board.

Leave for later: board reporting, the GenAI and agentic standards beyond the pilot system, the security programme, and compliance mappings for jurisdictions beyond your main one. The [Adoption Approach](README.md#adoption-approach) in the README puts them in order.

## A 6-Week Path for a GenAI System

For a team taking one GenAI system, such as a RAG assistant, from intake to go-live. Each week maps to [workflow stages](framework/governance-operations/governance-workflow.md) and to rows of the [minimum evidence pack](framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier). Six weeks fits T3 comfortably and T2 if you book outside reviewers in week 1. T1 is the hard case: read its notes below before you commit to a date.

| Week | Stages | Work | Pack rows |
|---|---|---|---|
| 1 | 1, 2 | Intake. Section 0 of the assessment and the Step 0 screen. Score the dimensions, check the overrides, define domain accuracy for the use case, write the risk assessment. DPIA screening if personal data is processed; impact assessment at T1/T2. Book every outside dependency for your tier (see below). | 1, 2, 3 |
| 2 | 3 | Architecture document and data flows, data residency confirmation, model selection, vendor risk assessment, and the architecture review (T1) or design review (T2). Start building the eval sets, kept apart from anything used to tune prompts (EV-006). Risk assessment approved by the end of the week. | 4, 5, 6 |
| 3 | 4 | Build: model card, prompts in version control, guardrails, retrieval access controls. Prompt review. Monitoring and cost alerts configured. | 7, 8, 9 |
| 4 | 5, 6 | Pre-release, safety and RAG retrieval evaluations, plus regression, bias and judge calibration at T1/T2. Freeze a prompt version and start the red team on it. | 10, 12 |
| 5 | 5, 6 | Fix red-team findings and re-run the affected evaluations. Validation at your tier. Security assessment where required. | 11, 12, 13 |
| 6 | 7, 8 | Monitoring, alerting and production evaluation live before traffic, with human oversight at T1/T2. Incident playbook, on-call and rollback test at T1/T2. Evidence checklist, gate evidence, sign-offs, go-live. | 14 to 17 |

Two rules shape the calendar:
- **No build before approval.** The register sets RA-001, RA-004 and AR-001 to AR-005 as "before development", so the build starts only after the risk assessment is approved and the Stage 3 evidence exists. That is why week 2 ends with the approval.
- **Prompt changes after the red team cost time.** Every prompt change means re-running the affected evaluations: regression is required at T1/T2 and recommended at T3, and T1/T2 also re-run an adversarial regression set of at least 50 cases ([production evaluation](framework/llm-lifecycle/evaluation-governance.md#production-evaluation)).

### What Changes by Tier

**T3.** Fits with room to spare. Approvals stay with the team lead and the business owner (see the [fast lane](#fast-lane-for-t3-and-t4)). Two things come from outside the team, so ask for both in week 1: AI Risk's simplified vendor risk assessment if you call an external API, and a red-teamer from outside the build team for the automated scan and 50 manual cases. Pack rows 2, 5, 9, 15 and 16 do not apply.

**T2.** Fits if these are booked in week 1:
- AI Risk (second line) to approve the risk assessment by the end of week 2.
- The Head of AI or a delegate for the recorded design review and the model selection in week 2.
- A reduced-scope validator from MRM or the second line, who did not work on the build, for week 5.
- An internal red team for 100+ cases in weeks 4 and 5.
- The prompt engineering lead for the week 3 prompt review.
- The DPO for a full DPIA, if personal data is processed.

Before go-live you also need staffed human oversight (PM-003), an incident playbook and on-call rotation (IR-001, IR-002), a tested rollback (DA-004), and, for external models, a validated fallback model and a documented exit strategy. The Head of AI signs the deployment and the Business Unit Head co-signs.

**T1.** Six weeks is possible only if everything below starts in week 1. Treat it as a stretch target. The worked [T1 case file](examples/customer-service-chatbot/governance-case-file.md#9-deployment-approval-stage-7) ran a little over eight weeks from the start of the risk assessment to go-live.
- Two AI Risk Committee decisions inside six weeks: the risk assessment and model selection before the build (end of week 2), and deployment in week 6. The committee meets monthly and convenes out of cycle within 10 business days of a request ([review cadence](framework/operating-model/review-cadence.md#monthly-ai-risk-committee)), so request both slots in week 1.
- Architecture review board sign-off in week 2, and the CISO's co-signature on model selection.
- MRM reserved for full-scope validation in week 5. MRM also validates the tier for T1 systems ([decision process](framework/risk-classification/risk-matrix.md#decision-process)), so bring them in during week 1.
- A red team of 200+ cases including manual testing. External testers are recommended; contract them in week 1.
- A full DPIA started in week 1. The DPO co-signs deployment when personal data is processed.
- Human oversight designed and staffed. For a customer-facing informational system that means Pattern 1, or Pattern 3 with all five safeguards evidenced, including daily review of at least 1% of outputs (minimum 50 a day) and a kill switch that can stop or degrade the channel within 15 minutes ([pattern selection matrix](framework/responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix)).
- A validated fallback model and a documented exit strategy; T1 fallbacks are tested quarterly.

If any of these slips, move the date. Do not cut validation or the red team to hold it: an unresolved Critical finding cannot be excepted, and a missed threshold at T1 needs an exception approved by the committee.

**T4.** Most of the table falls away. See the fast lane.

## Fast Lane for T3 and T4

T3 and T4 systems follow the same stages with lighter evidence and no committee. The team lead holds the approvals that the second line or the committee holds at higher tiers. T3 adds a peer review, a red team from outside the build team (automated scan plus 50 manual cases) and the business owner's co-signature on deployment. T4 runs on self-assessment, self-review and self-test, with the team lead acknowledging the assessment and signing the deployment. Neither tier needs an impact assessment, architecture review, guardrail evidence, incident playbook, on-call rotation or rollback test in its pack. The non-waivable items and the re-tiering check apply in full.

The exact evidence list, the sign-offs and the triggers that move a system out of the fast lane are in [Fast Lane (T3/T4)](framework/governance-operations/governance-workflow.md#fast-lane-t3t4). The [internal knowledge search](examples/internal-knowledge-search/risk-assessment.md) example is a T3 RAG system governed this way.

## Small Teams

A team of three to five people can run a T3 or T4 system on its own, apart from a few named touchpoints. It cannot govern a T1 or T2 system on its own, because the framework requires validation and approval from outside the team. The rules are in [Small Teams](framework/governance-operations/governance-workflow.md#small-teams) in the workflow. This section shows how to apply them.

### Covering the Roles

| Role | T3 and T4 | T1 and T2 |
|---|---|---|
| Product owner and System owner | One person, often the team lead | Same |
| AI lead and Technical owner | One engineer can hold both | Same |
| AI Operations: monitoring, production evaluation, cost | The team runs it | The team runs it, with an on-call rotation (IR-002) shared with a platform or AI Operations team |
| Peer reviewer for T3 validation and prompt review | A teammate who did not write the code or prompt, or an engineer from another team | Peer prompt review still applies; validation needs the independent validator below |
| Red team | T3: Security or another team, never the builders. T4: automated scan recommended | Security's internal red team; external testers recommended at T1 |
| Independent validator | Not required: peer review at T3, self-test at T4 | MRM (T1); MRM or another second-line reviewer (T2) |
| Prompt review beyond the peer | Not required | Prompt engineering lead (T2); add security review and AI Risk sign-off (T1) |
| Business owner | A senior business stakeholder; at T3 a different person from the team lead, since both sign | Same; the Business Unit Head co-signs T2 deployments |
| Human reviewers (PM-003) | Not required | Qualified, trained reviewers from the business operation ([reviewer requirements](framework/responsible-ai/human-in-loop-patterns.md#reviewer-requirements)) |
| Approvers | Team lead, plus the business owner at T3 | Second line or committee, per [Approvals by Tier](framework/operating-model/roles-responsibilities.md#approvals-by-tier) |

### Where Independence Comes From at T1 and T2

1. **The second line.** MRM performs T1 validation. MRM or another second-line reviewer performs T2 validation. AI Risk approves T2 risk assessments and runs vendor risk assessments. Book them at intake, because their capacity usually sets your date.
2. **Another team.** An engineer from another team makes a good T3 peer reviewer, and the prompt engineering lead often sits in a central AI team. Another first-line team does not meet the T1/T2 validation rule, which requires MRM or the second line.
3. **An external validator.** If the second line lacks GenAI depth, it can bring in an external validator, and external red-teamers are recommended for T1 anyway. My recommendation is that the second line sets the scope, reviews the work and signs the validation conclusion, so the rule that MRM or the second line validates still holds. An external report that nobody in the second line has reviewed does not meet it.

### Traps

- **The team lead is the only builder.** At T4 nothing forbids it, but ask the team lead's own manager to acknowledge the self-assessment. It takes minutes and closes an obvious audit question.
- **Pair-written work.** Someone who co-wrote the code or the prompt is a developer, so they cannot be the T3 peer reviewer.
- **Oversight capacity.** Daily review of at least 1% of outputs (minimum 50 a day) under Pattern 3 is real work. Agree reviewers with the business before week 6, not after launch.
- **On-call depth.** The S1 response SLA is 15 minutes ([severity classification](framework/operating-model/escalation-paths.md#severity-classification)). A rota of three people is fragile; share one.
