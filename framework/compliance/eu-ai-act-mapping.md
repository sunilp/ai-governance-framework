# EU AI Act Mapping

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

## Overview

The EU AI Act is Regulation (EU) 2024/1689. It entered into force on 1 August 2024 and was amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force since 27 July 2026. This document maps the Act's obligations to framework controls, organised by the role the organisation plays for a given AI system:

- (a) [Deployer of high-risk AI systems](#a-deployer-of-high-risk-ai-systems), the usual position for a bank
- (b) [Provider of high-risk AI systems](#b-provider-of-high-risk-ai-systems), when the bank builds a system or changes one enough to become its provider
- (c) [Downstream user of general-purpose AI models](#c-downstream-user-of-general-purpose-ai-models)
- (d) [Transparency duties (Art. 50)](#d-transparency-duties-art-50) for providers and deployers
- (e) [AI literacy (Art. 4) and prohibited practices (Art. 5)](#e-ai-literacy-art-4-and-prohibited-practices-art-5)

Control IDs come from the [control register](../governance-operations/control-register.md). "No control yet (gap)" means the register has no control that evidences the obligation. Article numbers follow the Official Journal text: the requirements for high-risk systems are in Chapter III, Section 2 (Arts. 8 to 15), and the obligations of providers and deployers in Chapter III, Section 3 (Arts. 16 to 27).

The Act applies to providers placing AI systems or general-purpose AI models on the EU market or putting systems into service in the EU, wherever they are established; to deployers established or located in the EU; and to providers and deployers outside the EU where the system's output is used in the EU (Art. 2(1)).

## Application Dates

| Obligation | Applies from | Status (November 2026) | Notes |
|---|---|---|---|
| Prohibited practices (Art. 5) | 2 February 2025 | Applies | Art. 113, point (a) |
| AI literacy (Art. 4) | 2 February 2025 | Applies, as amended | Regulation 2026/1744 replaced the duty to "ensure, to their best extent, a sufficient level of AI literacy" with a duty to take measures to support AI literacy. See [section (e)](#e-ai-literacy-art-4-and-prohibited-practices-art-5) |
| Penalties (Chapter XII, Art. 99) | 2 August 2025 | Applies | Member States set the rules within the Art. 99 caps |
| General-purpose AI model obligations (Chapter V, Arts. 53 to 55) | 2 August 2025 | Applies | Models placed on the market before 2 August 2025 must comply by 2 August 2027 (Art. 111(3)) |
| Commission enforcement powers over general-purpose AI model providers (Arts. 88 to 94) and fines (Art. 101) | 2 August 2026 | Applies | Art. 113, point (b) excluded Art. 101 from the 2025 date; Chapter IX, Section 5 falls under the general date |
| Transparency duties (Art. 50) | 2 August 2026 | Applies | Providers of generative systems placed on the market before 2 August 2026 have until 2 December 2026 to meet Art. 50(2) marking (Art. 111(4), added by Regulation 2026/1744) |
| New prohibitions: AI that generates non-consensual intimate imagery of identifiable people, or child sexual abuse material (Art. 5(1)(ba) and (bb), 5(1a), 5(1b)) | 2 December 2026 | Adopted, not yet applicable | Added by Regulation 2026/1744; date set in amended Art. 113, point (a) |
| High-risk systems under Annex III (Chapter III, Sections 1 to 3) | 2 December 2027 | Not yet applicable | Amended Art. 113, point (c)(i). Originally 2 August 2026 |
| High-risk systems under Annex I (product safety legislation) | 2 August 2028 | Not yet applicable | Amended Art. 113, point (c)(ii). Originally 2 August 2027 |

High-risk systems already placed on the market or put into service before the Chapter III date fall under the Act only if their design changes significantly after that date. Systems intended for use by public authorities must comply by 2 August 2030 in any case (Art. 111(2) as amended).

The other high-risk duties mapped below (Arts. 49, 72, 73 and 86) depend on a system being classified as high-risk under Art. 6, which is in Chapter III, Section 1. Plan for the same dates.

## Working Out the Role

Roles attach to each AI system, not to the organisation as a whole. Record the role for each system at intake and again on material change, including the Art. 25(1) check below (RA-008).

- **Provider:** develops an AI system, or has one developed, and places it on the market or puts it into service under its own name, including for its own use (Art. 3(3), 3(11)). A bank that builds a chatbot or a scoring model on a vendor's foundation model and runs it under its own name is the provider of that AI system. The vendor remains the provider of the general-purpose AI model.
- **Deployer:** uses an AI system under its own authority (Art. 3(4)). A bank that builds and runs its own system is both provider and deployer.
- **High-risk:** a system listed in Annex III (Art. 6(2)), or a safety component of a product under Annex I (Art. 6(1)). An Annex III system is not high-risk if it does not pose a significant risk of harm and meets one of the Art. 6(3) conditions (narrow procedural task, improving a completed human activity, detecting patterns without replacing human assessment, or a preparatory task). An Annex III system that profiles natural persons is always high-risk (Art. 6(3)).

Annex III uses most relevant to a bank:

| Annex III point | Use | Notes |
|---|---|---|
| 5(b) | Evaluating the creditworthiness of natural persons or establishing their credit score | Expressly excludes AI systems used to detect financial fraud |
| 5(c) | Risk assessment and pricing for natural persons in life and health insurance | Relevant to bancassurance |
| 4(a), 4(b) | Recruitment and selection; decisions on promotion, termination and task allocation; monitoring and evaluating workers | HR systems |
| 1(a) | Remote biometric identification | Excludes biometric verification whose sole purpose is to confirm a person is who they claim to be |
| 1(b) | Biometric categorisation by sensitive or protected attributes | Categorisation to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation is prohibited (Art. 5(1)(g)) |
| 1(c) | Emotion recognition | Prohibited in the workplace and in education (Art. 5(1)(f)) |

### How the Act's Categories Relate to Framework Tiers

| Act category | Framework treatment |
|---|---|
| Prohibited (Art. 5) | Not tiered. Rejected at the [Step 0 prohibited-use screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen), recorded under RA-007 |
| High-risk (Art. 6, Annexes I and III) | The Annex III uses above match override item 1 (regulated decisions: credit, insurance underwriting or pricing, employment) or item 5 (biometrics) in the [canonical override list](../risk-classification/genai-risk-matrix.md#tier-override-rules), so they are T1. A T1 tier does not by itself make a system high-risk under the Act |
| Transparency duties (Art. 50) | Apply to any system that meets the conditions in Art. 50, whatever its tier and whether or not it is high-risk |
| General-purpose AI models (Chapter V) | Duties fall on the model provider. The bank checks them through the vendor assessment (AR-005) |
| All other AI systems | No Act duties beyond Arts. 4 and 5 (and Art. 50 where it applies). The framework tier sets the controls |

## (a) Deployer of High-Risk AI Systems

The usual position for a bank: it buys a high-risk system, such as a vendor credit-scoring model, and uses it under its own authority. These duties apply from 2 December 2027 for Annex III systems.

Financial-institution provisions:
- **Art. 26(5):** for deployers that are financial institutions subject to internal governance requirements under Union financial services law, the monitoring duty is deemed met by complying with those governance rules.
- **Art. 26(6):** such deployers keep the logs as part of the documentation kept under financial services law.
- **Art. 74(6):** the market surveillance authority for high-risk systems used by financial institutions, in direct connection with financial services, is the national financial supervisor. Member States may designate another authority (Art. 74(7)).

| Article | Requirement | Controls | Framework doc |
|---|---|---|---|
| 26(1) | Take technical and organisational measures to use the system in line with the provider's instructions for use | AR-005, DA-003 (no explicit check against the instructions for use: gap) | [Third-party model risk](third-party-model-risk.md), [Deployment gates](../llm-lifecycle/deployment-gates.md) |
| 26(2) | Assign human oversight to people with the competence, training, authority and support to do it | PM-003 | [Human-in-the-loop patterns](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix) |
| 26(4) | Where the deployer controls input data, keep it relevant and sufficiently representative for the intended purpose | EV-004 for RAG corpora; otherwise no control yet (gap) | [RAG governance](../llm-lifecycle/rag-governance.md) |
| 26(5) | Monitor operation against the instructions for use; if the system presents a risk, inform the provider and the market surveillance authority and suspend use; report serious incidents to the provider, then to the authorities | PM-001, PM-002, PM-004, IR-003, IR-006 (serious incidents assessed under Arts. 26(5) and 73; see [regulatory notification](../operating-model/escalation-paths.md#regulatory-notification)) | [LLM monitoring](../llm-lifecycle/monitoring.md), [Escalation paths](../operating-model/escalation-paths.md) |
| 26(6) | Keep automatically generated logs under the deployer's control for at least 6 months | DA-003 (audit logging verified at the gates), PM-007 (audit logging complete and retained) | [Audit trail](audit-trail-requirements.md#retention-periods), [Prompt audit trail](prompt-audit-trail.md#retention-requirements) |
| 26(7) | Before using a high-risk system at the workplace, inform workers' representatives and affected workers | DE-009 (record that workers' representatives and affected workers were informed before use) | [Transparency standards](../responsible-ai/transparency-standards.md#ai-assisted-decision-notices) |
| 26(9) | Use the provider's Art. 13 information to carry out the DPIA | RA-005 | |
| 26(11) | Tell natural persons that they are subject to an Annex III system that makes, or assists in making, decisions about them | DE-009 | [Transparency standards](../responsible-ai/transparency-standards.md#ai-assisted-decision-notices) |
| 27 | Before first use, carry out a fundamental rights impact assessment and notify the results to the market surveillance authority. Required for deployers of Annex III point 5(b) and 5(c) systems, and for bodies governed by public law or private entities providing public services (any Annex III system except point 2). The assessment may cross-refer to the DPIA (Art. 27(4) as amended) | RA-009 (assessment of the Art. 27(1) elements and notification record), drawing on RA-003 and RA-005; RA-008 identifies the systems in scope | [Impact assessment template, section 5](../../templates/impact-assessment-template.md#5-fundamental-rights-impact-assessment-eu-ai-act-art-27) |
| 86 | Give a person affected by a decision based on an Annex III system's output, with legal or similarly significant effects, a clear and meaningful explanation of the system's role and the main elements of the decision | RV-005 | [Transparency standards: explainability](../responsible-ai/transparency-standards.md#explainability) |

Registration in the EU database by deployers (Arts. 26(8), 49(3)) applies only to public authorities and EU bodies.

## (b) Provider of High-Risk AI Systems

The bank is the provider when it develops a high-risk system, such as an in-house credit-scoring model, and puts it into service under its own name, including for its own use.

**When a deployer becomes a provider (Art. 25(1)).** A deployer or other third party takes on the provider obligations in Art. 16 if it:
- (a) puts its name or trademark on a high-risk system already on the market or in service;
- (b) makes a substantial modification to a high-risk system so that it remains high-risk; or
- (c) changes the intended purpose of a system that is not high-risk, including a general-purpose AI system, so that it becomes high-risk. Example: using a general-purpose chatbot to assess the creditworthiness of applicants.

The initial provider must then cooperate and hand over documentation, unless it clearly specified that its system is not to be changed into a high-risk system (Art. 25(2) as amended). A provider of a high-risk system and any third party supplying an AI system, AI model, tools, services or components used in it must set out by written agreement the information, technical access and assistance the provider needs (Art. 25(4) as amended). Control: RA-008 records the role at intake and repeats the Art. 25(1) check on every material change, which RA-001 re-assessment and RV-003 revalidation trigger. The Art. 25(4) written agreement with suppliers has no control yet (gap).

Financial-institution provisions:
- **Art. 17(4):** for providers that are financial institutions subject to internal governance requirements under Union financial services law, the quality management system obligation is deemed met by complying with those rules, except for Art. 17(1)(g) risk management, (h) post-market monitoring and (i) serious incident reporting.
- **Art. 18(3) and 19(2):** technical documentation and logs are kept as part of the documentation kept under financial services law.
- **Art. 72(4):** for Annex III point 5 systems, financial institutions may integrate post-market monitoring into their existing systems and plans.

Conformity assessment for Annex III points 2 to 8 uses the internal control procedure in Annex VI, without a notified body (Art. 43(2)). Annex VI requires the provider to verify that its quality management system meets Art. 17, that the technical documentation shows compliance with Chapter III, Section 2, and that design, development and post-market monitoring match that documentation.

| Article | Requirement | Controls | Framework doc |
|---|---|---|---|
| 9 | Risk management system run across the lifecycle: identify, estimate and evaluate risks, adopt measures, test | RA-001, RA-003, RV-001, RV-003 | [Risk matrix](../risk-classification/risk-matrix.md), [Impact assessment template](../../templates/impact-assessment-template.md) |
| 10 | Training, validation and testing data meet quality criteria; examine and correct bias. Art. 4a (added by Regulation 2026/1744) allows processing of special category data for bias detection under strict conditions | DE-005, EV-005, EV-006 | [Development](../model-lifecycle/development.md), [Bias detection](../responsible-ai/bias-detection-llm.md) |
| 11 | Technical documentation (Annex IV) drawn up before placing on the market and kept up to date | DE-001, AR-001, RV-002 | [Model card template](../../templates/model-card-template.yaml), [LLM model card](../../templates/llm-model-card.yaml) |
| 12 | Automatic recording of events over the system's lifetime | DA-003 (audit logging verified at the gates) | [Audit trail](audit-trail-requirements.md), [Prompt audit trail](prompt-audit-trail.md) |
| 13 | Enough transparency for deployers to interpret and use the output; instructions for use | DE-001 | [Transparency standards](../responsible-ai/transparency-standards.md) |
| 14 | Designed for effective human oversight, including the ability to override or stop the system | PM-003, DA-004 | [Human-in-the-loop patterns](../responsible-ai/human-in-loop-patterns.md), [Deployment](../model-lifecycle/deployment.md) |
| 15 | Appropriate accuracy, robustness and cybersecurity | EV-001, EV-002, EV-003, EV-008, EV-009, SR-001, SR-002, SR-003, SR-004 | [Validation](../model-lifecycle/validation.md), [Red-teaming protocol](../ai-security/red-teaming-protocol.md), [Adversarial robustness](../ai-security/adversarial-robustness.md) |
| 16 | Provider obligations: meet Section 2, show name and contact on the system, keep documentation and logs, complete conformity assessment, EU declaration of conformity (Art. 47), CE marking (Art. 48), registration (Art. 49), corrective action (Art. 20), accessibility | DA-001, DA-002. Declaration of conformity, CE marking and accessibility: no control yet (gap) | [Governance workflow, Stage 7](../governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier) |
| 17 | Documented quality management system (see Art. 17(4) above) | The control register as a whole; RV-001, RV-004 | [Control register](../governance-operations/control-register.md), [Governance workflow](../governance-operations/governance-workflow.md) |
| 18 | Keep technical documentation, quality management system records and the declaration of conformity for 10 years | DR-003 | [Audit trail: retention](audit-trail-requirements.md#retention-periods) |
| 19 | Keep automatically generated logs under the provider's control for at least 6 months | DA-003, DR-003 | [Prompt audit trail](prompt-audit-trail.md#retention-requirements) |
| 20 | Take corrective action on non-conformity and inform deployers and authorities | IR-003, IR-005 | [Escalation paths](../operating-model/escalation-paths.md) |
| 43 | Conformity assessment before placing on the market or putting into service | DA-001, DA-002, DA-003 (evidence pack, sign-off and gates support the Annex VI procedure but do not complete it alone) | [Governance workflow](../governance-operations/governance-workflow.md), [Validation](../model-lifecycle/validation.md) |
| 49(1) | Register the provider and the system in the EU database before placing an Annex III system (except point 2) on the market | No control yet (gap) | |
| 6(3), 6(4), 49(2) | If the provider concludes an Annex III system is not high-risk, document the assessment before placing it on the market and register the system | RA-001 for the assessment; registration: no control yet (gap) | [Assessment template](../../templates/genai-use-case-assessment.md) |
| 72 | Post-market monitoring system and plan, proportionate to the risk | PM-001, PM-004, RV-001 | [LLM monitoring](../llm-lifecycle/monitoring.md), [Model monitoring](../model-lifecycle/monitoring.md) |
| 73 | Report serious incidents to the market surveillance authority: immediately after establishing a causal link, and no later than 15 days after becoming aware; 2 days for a widespread infringement or serious disruption of critical infrastructure; 10 days in the event of a death | IR-003, IR-006 | [Escalation paths: regulatory notification](../operating-model/escalation-paths.md#regulatory-notification) |

### GenAI Systems in a High-Risk Use

When a GenAI system is used in an Annex III context, Arts. 9 to 15 apply in full. The framework's GenAI controls carry most of the evidence:

| Article | GenAI-specific evidence | Framework doc |
|---|---|---|
| 9 | Hallucination, prompt injection, data leakage and vendor dependency risks scored | [GenAI risk matrix](../risk-classification/genai-risk-matrix.md) |
| 10 | RAG corpus freshness, accuracy and access control; bias in retrieved context; foundation model training data assessed from the provider's documentation | [RAG governance](../llm-lifecycle/rag-governance.md) |
| 11 | Model selection rationale, prompt architecture, RAG pipeline design, GenAI metrics and limitations | [LLM model card](../../templates/llm-model-card.yaml), [Model selection](../llm-lifecycle/model-selection.md) |
| 12 | Prompt and response logging with context documents; prompt, model and guardrail version history | [Prompt audit trail](prompt-audit-trail.md) |
| 13 | Source attribution, limitation disclosure, guidance on interpreting outputs | [Transparency standards](../responsible-ai/transparency-standards.md) |
| 14 | Human review before consequential use; ability to override, correct or reject output | [Human-in-the-loop patterns](../responsible-ai/human-in-loop-patterns.md) |
| 15 | Hallucination rate, faithfulness, adversarial prompt testing, prompt injection defence; retrieval that enforces source permissions (DE-008) | [Evaluation governance](../llm-lifecycle/evaluation-governance.md), [Red-teaming protocol](../ai-security/red-teaming-protocol.md) |

## (c) Downstream User of General-Purpose AI Models

The obligations in Arts. 53 to 55 fall on the providers of general-purpose AI models (the foundation model vendors), not on the bank that uses them. The bank needs the vendor's information to meet its own duties as provider or deployer of the AI system it builds on the model. If that system is high-risk, Art. 25(4) requires a written agreement with the vendor.

How providers show compliance:
- **General-Purpose AI Code of Practice**, published 10 July 2025, with chapters on transparency, copyright, and safety and security. The Commission and the AI Board confirmed it is an adequate voluntary tool. Providers may rely on it to demonstrate compliance until a harmonised standard is published; providers that do not adhere must show alternative adequate means (Arts. 53(4), 55(2)).
- **Commission guidelines on the scope of the obligations** for providers of general-purpose AI models, published 18 July 2025. As an indicative criterion, they treat a model trained with more than 10^23 FLOP that can generate language (text or audio), text-to-image or text-to-video as a general-purpose AI model.
- **Template for the public summary of training content**, published 24 July 2025, for Art. 53(1)(d).
- **Systemic risk:** a model is presumed to have high-impact capabilities above 10^25 FLOP of cumulative training compute (Art. 51(2)), or the Commission can designate it (Art. 52(4)). The Commission must publish and maintain a list of models with systemic risk (Art. 52(6)). Ask the vendor whether its model is classified as systemic-risk rather than assuming.
- **Enforcement:** the Commission (AI Office) supervises model providers and can fine them up to 3% of annual worldwide turnover or EUR 15 million, whichever is higher, from 2 August 2026 (Art. 101).

| Provider obligation | Article | What to ask the vendor and file | Controls |
|---|---|---|---|
| Technical documentation of the model (Annex XI), kept for the AI Office and national authorities | 53(1)(a) | Confirmation that it exists; it is not normally shared with downstream users | AR-005 |
| Information and documentation for downstream providers (Annex XII): capabilities, limitations, intended and acceptable uses | 53(1)(b) | Model documentation (for Code of Practice signatories, the Model Documentation Form); date obtained; review notes | AR-004, AR-005 |
| Copyright policy, including respecting text and data mining opt-outs | 53(1)(c) | The policy; contract terms on IP indemnity | AR-005 |
| Public summary of training content on the Commission template | 53(1)(d) | Link to the published summary; note on relevance and bias risks | AR-005 |
| Authorised representative in the EU for non-EU providers | 54 | Name and contact of the representative | AR-005 |
| Systemic-risk duties: model evaluation including adversarial testing, systemic risk assessment and mitigation, serious incident reporting to the AI Office, cybersecurity | 55 | Whether the model is classified as systemic-risk; summary of the provider's safety and security measures; incident notification terms in the contract. The bank still red-teams its own use case (SR-001) | AR-005, SR-001 |
| Code of Practice adherence or alternative means of compliance | 53(4), 55(2) | Which chapters the vendor signed | AR-005 |
| Models placed on the market before 2 August 2025 | 111(3) | Plan to comply by 2 August 2027 | AR-005 |

See [third-party model risk](third-party-model-risk.md) and [model selection](../llm-lifecycle/model-selection.md) for the assessment process.

## (d) Transparency Duties (Art. 50)

Art. 50 applies from 2 August 2026. It applies to any system that meets its conditions, whatever the framework tier and whether or not the system is high-risk; where both apply, it sits alongside the high-risk requirements (Art. 50(6)). It is a duty on providers and deployers of AI systems, not a general-purpose AI model obligation. The information must be given clearly and distinguishably at the latest at the first interaction or exposure, and must meet accessibility requirements (Art. 50(5)).

| Paragraph | Who | Duty | Exceptions | Controls | Framework doc |
|---|---|---|---|---|---|
| 50(1) | Provider | Design systems that interact directly with people so that the people are told they are interacting with AI | Obvious to a reasonably well-informed, observant and circumspect person (the Commission reads this narrowly); systems authorised by law to detect, prevent, investigate or prosecute criminal offences | DE-006 | [Transparency standards](../responsible-ai/transparency-standards.md#user-interaction-disclosure) |
| 50(2) | Provider | Mark synthetic audio, image, video or text output in a machine-readable format so it is detectable as AI-generated or manipulated | Assistive function for standard editing; no substantial change to the input or its meaning; law enforcement uses authorised by law. Systems placed on the market before 2 August 2026: by 2 December 2026 (Art. 111(4)) | DE-007 | [Transparency standards](../responsible-ai/transparency-standards.md#content-labeling), [Multimodal governance](../llm-lifecycle/multimodal-governance.md#synthetic-media-labeling) |
| 50(3) | Deployer | Inform people exposed to an emotion recognition or biometric categorisation system, and process their data under the GDPR | Uses permitted by law to detect, prevent or investigate criminal offences | DE-006 | [Multimodal risk matrix](../risk-classification/multimodal-risk-matrix.md#tier-override-rules) |
| 50(4), first subparagraph | Deployer | Disclose that image, audio or video content forming a deep fake is AI-generated or manipulated | Law enforcement uses; for evidently artistic, creative, satirical or fictional work, disclosure in a way that does not hamper the work | DE-007 | [Multimodal governance](../llm-lifecycle/multimodal-governance.md#synthetic-media-labeling) |
| 50(4), second subparagraph | Deployer | Disclose that text published to inform the public on matters of public interest is AI-generated or manipulated | Content that has undergone human review or editorial control, with a person holding editorial responsibility; law enforcement uses | DE-007 | [Transparency standards](../responsible-ai/transparency-standards.md#labeling-by-content-destination) |

A bank that builds a customer chatbot on a vendor model and runs it under its own name is the provider for Art. 50(1) and 50(2). The Commission's Art. 50 guidelines give an in-house chatbot put into service for the organisation's own use as an example of a provider, list customer support chatbots as in scope of Art. 50(1), and list AI-generated summaries of text among the outputs that need Art. 50(2) marking. They also treat an internal assistant used by trained, AI-literate staff as an example where the interaction is obvious.

**Emotion recognition.** The Act defines it as inferring emotions or intentions from biometric data (Art. 3(39)). The Commission's guidelines on prohibited practices say that inferring emotions from written text, such as sentiment analysis, is not based on biometric data. Emotion recognition is:
- prohibited in the workplace and in education, unless used for medical or safety reasons (Art. 5(1)(f)). The same guidelines give the example that a call centre tracking its employees' emotions is prohibited, while tracking its customers' emotions is not prohibited by Art. 5(1)(f);
- otherwise high-risk (Annex III point 1(c)), and the deployer must give the Art. 50(3) notice.

The framework treats it under override item 5 (automatic T1); see the [multimodal risk matrix](../risk-classification/multimodal-risk-matrix.md#tier-override-rules).

Support for Art. 50:
- **Commission Guidelines on the transparency obligations under Art. 50**, published 20 July 2026 and adopted as Communication C(2026) 7702 on 5 November 2026, covering Art. 50(1) to (5).
- **Code of Practice on marking and labelling of AI-generated content**, final version published 10 June 2026. It is voluntary and covers marking and detection (providers) and labelling of deep fakes and public-interest text (deployers). In July 2026 the Commission and the AI Board assessed it as adequate for Art. 50(2), (4) and (5). Art. 50(1) and 50(3) are outside its scope; the guidelines cover them.

## (e) AI Literacy (Art. 4) and Prohibited Practices (Art. 5)

### AI Literacy (Art. 4)

Providers and deployers must take measures to support the development of AI literacy of their staff and of others operating or using AI systems on their behalf. The measures take into account people's technical knowledge, experience, education and training, the context of use, and the people the systems are used on. The duty does not require a guaranteed level of AI literacy for any individual (Art. 4(1), as replaced by Regulation 2026/1744). The original duty, to ensure a sufficient level of AI literacy to the best extent possible, applied from 2 February 2025.

| Requirement | Controls | Framework doc |
|---|---|---|
| Measures to support AI literacy of staff and others acting on the organisation's behalf | GV-002 (literacy measures by role, completion tracked) | [AI literacy](../operating-model/ai-literacy.md), [Governance metrics](../operating-model/governance-metrics.md) |

### Prohibited Practices (Art. 5)

Prohibited uses are not tiered. They are rejected at the [Step 0 prohibited-use screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen), which runs before scoring in the risk assessment (RA-001) and is evidenced by RA-007. The Commission's guidelines on prohibited practices (content approved 4 February 2025, adopted as C(2025) 5052 on 29 July 2025) explain each prohibition with examples. They are not binding.

| Article | Prohibited practice | Relevance to a bank |
|---|---|---|
| 5(1)(a) | Subliminal, purposefully manipulative or deceptive techniques that materially distort behaviour and cause, or are reasonably likely to cause, significant harm | Sales and collections journeys, marketing personalisation |
| 5(1)(b) | Exploiting vulnerabilities due to age, disability or a specific social or economic situation, causing significant harm | Targeting of financially vulnerable customers |
| 5(1)(c) | Social scoring that leads to detrimental treatment in unrelated contexts, or treatment unjustified or disproportionate to the behaviour | Customer scores built from behaviour unrelated to the product |
| 5(1)(d) | Assessing or predicting the risk that a person will commit a criminal offence based solely on profiling or personality traits. Does not cover systems supporting a human assessment already based on objective, verifiable facts linked to criminal activity | Screen fraud and financial crime models against this |
| 5(1)(e) | Building or expanding facial recognition databases through untargeted scraping of facial images from the internet or CCTV | Identity and KYC tooling |
| 5(1)(f) | Inferring emotions in the workplace or in education, except for medical or safety reasons | Employee monitoring, call-centre staff analytics |
| 5(1)(g) | Biometric categorisation to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation | Any biometric analytics |
| 5(1)(h) | Real-time remote biometric identification in publicly accessible spaces for law enforcement | Not normally relevant |
| 5(1)(ba), (bb), from 2 December 2026 | Systems that generate or manipulate realistic intimate imagery of an identifiable person without explicit consent, or child sexual abuse material | Image and video generation tools: check the vendor's safeguards |

Control coverage: RA-007 (Step 0 screen recorded for every system before scoring; non-waivable), within the RA-001 risk assessment.

## Penalties

| Infringement | Maximum fine | Article |
|---|---|---|
| Prohibited practices (Art. 5) | EUR 35 million or 7% of total worldwide annual turnover, whichever is higher | 99(3) |
| Obligations of providers (Art. 16), deployers (Art. 26), other operators, Art. 25(2) and (4), and transparency (Art. 50) | EUR 15 million or 3%, whichever is higher | 99(4) |
| Incorrect, incomplete or misleading information to notified bodies or national authorities | EUR 7.5 million or 1%, whichever is higher | 99(5) |
| SMEs and small mid-cap enterprises | The lower of the two amounts | 99(6), 99(6a) |
| Providers of general-purpose AI models (imposed by the Commission, from 2 August 2026) | EUR 15 million or 3%, whichever is higher | 101 |

## Standards and Commission Guidance

| Item | Status (November 2026) |
|---|---|
| EN 18286:2026, Artificial intelligence: Quality management system for EU AI Act regulatory purposes | First harmonised standard under the Act. Reference published in the Official Journal by Commission Implementing Decision (EU) 2026/2274 of 12 October 2026, published 14 October 2026. It covers quality management systems for providers, including post-market monitoring processes (Art. 17). Compliance gives a presumption of conformity for the requirements it covers (Art. 40) |
| Other harmonised standards requested under Commission Implementing Decision C(2025) 3871 (23 June 2025) | EN 18286 was the first to be cited. Check the Commission's list of cited standards for later additions before relying on one |
| Guidelines on prohibited AI practices | Content approved 4 February 2025; adopted as Communication C(2025) 5052 on 29 July 2025 |
| Guidelines on the scope of obligations for general-purpose AI model providers | Published 18 July 2025 |
| Template for the public summary of training content | Published 24 July 2025 |
| General-Purpose AI Code of Practice | Published 10 July 2025; confirmed by the Commission and the AI Board as an adequate voluntary tool |
| Code of Practice on marking and labelling of AI-generated content | Final version published 10 June 2026; assessed as adequate for Art. 50(2), (4) and (5) in July 2026 |
| Guidelines on transparency obligations (Art. 50) | Published 20 July 2026; adopted as Communication C(2026) 7702 on 5 November 2026 |
| Guidelines on high-risk classification (Art. 6) | Draft published 19 May 2026 for targeted consultation. Check for the final version before relying on it |
| Guidance and template for the post-market monitoring plan | Due by 2 September 2027 (Art. 72(3) as amended) |

## Implementation Notes

- Financial services AI systems may also be subject to sector-specific requirements (CRD, Solvency II, MiFID II) that complement the AI Act. The Act's financial-institution provisions (Arts. 17(4), 18(3), 19(2), 26(5), 26(6), 72(4)) let banks meet several duties through their existing internal governance, and Art. 74(6) makes the financial supervisor the market surveillance authority.
- Review this mapping when the Commission adopts guidelines, delegated or implementing acts, or harmonised standards (RV-004, [regulatory change monitoring](regulatory-change-monitoring.md)).

## Sources

- Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Regulation (EU) 2026/1744 (Digital Omnibus on AI), Official Journal, 24 July 2026: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Commission Implementing Decision (EU) 2026/2274 on harmonised standards for high-risk AI systems (EN 18286:2026): https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj
- CEN-CENELEC, First ever European standard on AI published in the OJEU: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-10-15-en-18286-2026-published-in-ojeu/
- European Commission, Guidelines on prohibited AI practices (publication page and C(2025) 5052 text): https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-prohibited-artificial-intelligence-ai-practices-defined-ai-act and https://ec.europa.eu/newsroom/dae/redirection/document/112367
- European Commission, The General-Purpose AI Code of Practice: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
- European Commission, General-purpose AI obligations under the AI Act: https://digital-strategy.ec.europa.eu/en/factpages/general-purpose-ai-obligations-under-ai-act
- European Commission, Guidelines for providers of general-purpose AI models: https://digital-strategy.ec.europa.eu/en/news/commission-publishes-guidelines-providers-general-purpose-ai-models
- European Commission, Explanatory notice and template for the public summary of training content: https://digital-strategy.ec.europa.eu/en/library/explanatory-notice-and-template-public-summary-training-content-general-purpose-ai-models
- European Commission, Code of Practice on marking and labelling AI-generated content: https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content
- European Commission, Guidelines on transparency obligations for providers and deployers of AI systems (publication page and C(2026) 7702 text): https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems and https://ec.europa.eu/newsroom/dae/redirection/document/131215
- European Commission, Draft guidelines on the classification of high-risk AI systems: https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems
- Reed Smith, Code of Practice adequacy decision and final Article 50 guidelines: https://www.reedsmith.com/our-insights/blogs/viewpoints/102nbz0/transparency-obligations-for-ai-generated-content-the-code-of-practice-adequacy/
- Faegre Drinker, Commission confirms transparency Code of Practice as adequate: https://www.faegredrinker.com/en/insights/publications/2026/7/eu-ai-act-commission-confirms-transparency-code-of-practice-as-adequate-and-publishes-final-version-of-its-guidelines-on-transparency-obligations
