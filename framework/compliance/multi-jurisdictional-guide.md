# Multi-Jurisdictional AI Governance Guide

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

## Overview

Organizations operating AI systems across multiple jurisdictions face a patchwork of regulations, guidelines, and enforcement regimes. This guide provides a practical reference for understanding what each jurisdiction requires, how this framework satisfies those requirements, and what additional controls are needed locally.

Each profile lists four things: the binding instruments, what financial supervisors expect, what this framework maps to (documents and control IDs from the [control register](../governance-operations/control-register.md)), and the gaps. "No control yet (gap)" means the register has no control for that obligation. Dates still to come are collected in [regulatory-change-monitoring.md](regulatory-change-monitoring.md#upcoming-deadlines).

For data-specific cross-border considerations, see [cross-border-data-governance.md](cross-border-data-governance.md). This document covers the broader regulatory landscape.

---

## Jurisdictional Profiles

### European Union

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | EU AI Act (Regulation (EU) 2024/1689), amended by the Digital Omnibus on AI (Regulation (EU) 2026/1744, in force 27 July 2026). Prohibited practices apply since 2 February 2025. GPAI model obligations apply since 2 August 2025; Commission fines for GPAI providers from 2 August 2026; models placed on the market before 2 August 2025 must comply by 2 August 2027. Art. 50 transparency duties apply since 2 August 2026. New prohibitions on non-consensual intimate deepfakes and child sexual abuse material, and Art. 50(2) marking for generative systems placed on the market before 2 August 2026, apply from 2 December 2026. High-risk obligations apply from 2 December 2027 (Annex III, which includes credit scoring) and 2 August 2028 (Annex I). GDPR, including Art. 22 on automated decisions. DORA (Regulation (EU) 2022/2554), applies since 17 January 2025. |
| **Supervisory expectations (financial sector)** | EBA AI Act mapping (21 November 2025): no significant contradictions between the AI Act and EU banking and payments law, and no immediate need for new or revised EBA guidelines; the work focused on creditworthiness assessment and credit scoring. EIOPA Opinion on AI governance and risk management (6 August 2025): applies existing Solvency II and IDD principles to insurance AI systems that are not prohibited or high-risk, without new requirements. ESMA public statement on AI and investment services (30 May 2024): MiFID II organisational, conduct and best-interest duties apply. ESAs joint statement on ICT risks from frontier AI models (31 July 2026). Under DORA the ESAs designated the first 19 critical ICT third-party providers on 18 November 2025. |
| **Framework maps to** | [EU AI Act Mapping](eu-ai-act-mapping.md) for article-level mapping and dates. DORA third-party duties: [third-party-model-risk.md](third-party-model-risk.md#regulatory-hooks), AR-003, AR-005. GDPR Art. 22 and AI Act Art. 14: [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md#regulatory-requirements-for-human-oversight), PM-003. DPIA: RA-005. AI Act prohibited-use screen: RA-007. Role as provider or deployer, including the Art. 25 check: RA-008. Fundamental rights impact assessment (Art. 27): RA-009. Art. 50 disclosure and marking: DE-006, DE-007, [transparency-standards.md](../responsible-ai/transparency-standards.md). Notices to affected people and workers (Arts. 26(7), 26(11)): DE-009. Explanation (Art. 86) and GDPR Art. 22(3) human intervention: RV-005. |
| **Gaps** | DORA register of information entries for AI vendors: AR-007 and the [AI procurement clauses](ai-procurement-clauses.md). Harmonised standards: only the quality management standard EN 18286:2026 has been referenced in the Official Journal (Implementing Decision (EU) 2026/2274); the others are still in development in CEN-CENELEC JTC 21. |

### United Kingdom

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | No AI-specific statute. The government has not introduced an AI bill; none was announced in the King's Speech of 13 May 2026. UK GDPR as amended by the Data (Use and Access) Act 2025 (Royal Assent 19 June 2025): section 80 replaces Art. 22 with Arts. 22A-22D, in force since 5 February 2026, moving from a prohibition on solely automated decisions with exceptions to permitting them subject to safeguards. FCA rules, including the Consumer Duty (in force 31 July 2023 for open products, 31 July 2024 for closed products) and the Senior Managers and Certification Regime (SM&CR). |
| **Supervisory expectations (financial sector)** | PRA SS1/23 Model risk management principles for banks (effective 17 May 2024) applies to banks with internal model approval and covers AI and machine learning to the extent they are models; amended on 23 April 2026 in a low-impact change that is not AI-specific. The Bank of England and PRA told the Chancellor on 1 April 2026 that they intend to build on this in 2026, noting most firms did not yet see a need for detailed AI-specific rules. The FCA does not plan AI-specific rules and relies on existing rules, naming the Consumer Duty and SM&CR (AI Update, 22 April 2024). FCA publications: the Mills Review report on AI in retail financial services (6 July 2026, recommendations to the FCA Board); "AI in financial services: good practice and areas for improvement" (19 October 2026, no new requirements); AI Live Testing (since December 2025). The AI Security Institute (renamed from the AI Safety Institute on 14 February 2025) publishes work on frontier model risks. |
| **Framework maps to** | SS1/23: [validation.md](../model-lifecycle/validation.md) and the model lifecycle standards, RA-001, RV-001, RV-003, AR-005 for vendor models. Consumer Duty: [transparency-standards.md](../responsible-ai/transparency-standards.md), [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md#regulatory-requirements-for-human-oversight). SM&CR: single named accountability in [roles-responsibilities.md](../operating-model/roles-responsibilities.md#accountability-principles). Arts. 22A-22D: PM-003, RA-005, RV-005. |
| **Gaps** | The human oversight table cites GDPR Art. 22 only; document the UK basis under Arts. 22A-22D separately. Mapping of SM&CR responsibilities to named AI roles is left to each firm. |

### United States

| Aspect | Detail |
|--------|--------|
| **Federal posture** | Executive Order 14365, "Ensuring a National Policy Framework for Artificial Intelligence" (signed 11 December 2025), calls for a national framework that preempts conflicting state AI laws. It directed the Department of Justice to set up an AI Litigation Task Force (established 9 January 2026) to challenge state AI laws; in April 2026 the United States moved to intervene in a suit challenging Colorado's 2024 AI Act. The White House sent "National Policy Framework for Artificial Intelligence: Legislative Recommendations" to Congress on 20 March 2026. The FTC proposed a policy statement on suppressing accuracy in AI systems on 7 July 2026 (not final). OMB M-25-21 and M-25-22 (3 April 2025) govern federal agencies' use and purchase of AI, which matters to firms selling AI to government. |
| **State laws** | **Colorado** SB 26-189 (signed 14 May 2026) repealed and re-enacted SB 24-205. From 1 January 2027 developers must give deployers documentation, and deployers must give notice at the point of interaction, a plain-language explanation within 30 days of an adverse outcome, data correction and human review. It drops impact assessments, disclosures to the Attorney General and the duty of care to avoid algorithmic discrimination. Attorney General enforcement only, with a 60-day cure period until 1 January 2030. **California**: CPPA regulations on automated decisionmaking technology (ADMT), risk assessments and cybersecurity audits (effective 1 January 2026; ADMT requirements from 1 January 2027; risk assessment attestations and summaries due 1 April 2028; audit certifications phased from 1 April 2028 to 1 April 2030 by revenue). SB 53 frontier AI transparency for large frontier developers (effective 1 January 2026). AI Transparency Act (SB 942, operative 2 August 2026 under AB 853, amended again in 2026 by SB 1000 and AB 2713) on disclosures in AI-generated content. **Texas** TRAIGA (HB 149, effective 1 January 2026): disclosure duties for government agencies, prohibited practices, intent required for discrimination claims, Attorney General enforcement with a cure period. **Illinois** HB 3773 (effective 1 January 2026): bars employer use of AI that has a discriminatory effect and requires notice. **New York** RAISE Act (signed 19 December 2025, chapter amendment signed 27 March 2026, effective 1 January 2027): frontier AI frameworks, transparency reports and 72-hour incident reporting for large frontier developers. **New York City** Local Law 144: bias audits and notices for automated employment decision tools, enforced since 5 July 2023. |
| **Supervisory expectations (financial sector)** | SR 26-2 "Revised Guidance on Model Risk Management", issued 17 April 2026 by the Federal Reserve with the OCC (Bulletin 2026-13) and FDIC (FIL-15-2026). It replaces SR 11-7, OCC Bulletin 2011-12 and FDIC FIL-22-2017, takes a risk-based approach scaled to model materiality, and is most relevant to banking organisations with over $30 billion in total assets. It covers traditional and non-generative AI models. Generative AI and agentic AI are outside its scope. The agencies plan a request for information on banks' use of AI, including generative and agentic AI; it had not been issued by November 2026. NIST AI RMF (January 2023) is voluntary and is being revised. The SEC withdrew its predictive data analytics proposal on 17 June 2025. |
| **Framework maps to** | SR 26-2: model lifecycle standards ([validation.md](../model-lifecycle/validation.md)), RA-001, RV-001, RV-003, and AR-005 for vendor models. GenAI and agentic AI: the framework's own controls (DE-003, DE-004, EV-001 to EV-009, SR-001 to SR-004, PM-003) stand on their own until the agencies issue AI guidance. NIST AI RMF: [NIST AI RMF Mapping](nist-ai-rmf-mapping.md). Colorado notice at the point of interaction: DE-009; adverse-outcome explanation and human review: RV-005, PM-003. CPPA ADMT Pre-use Notice: DE-009; ADMT access requests and opt-out or human appeal: RV-005. CPPA risk assessments: RA-003, RA-005. Frontier developer laws (SB 53, RAISE): use the vendor's published framework and reports as evidence in AR-005. |
| **Gaps** | NYC Local Law 144 independent bias audit and its publication: EV-005 covers bias evaluation, not an independent audit (gap). Federal preemption is being pursued through litigation and proposed legislation; state obligations still apply unless a court or Congress removes them. |

### Singapore

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | Personal Data Protection Act (PDPA). Financial sector AI expectations are set in MAS guidelines. |
| **Supervisory expectations (financial sector)** | MAS Guidelines on Artificial Intelligence Risk Management for Financial Institutions (issued 7 October 2026) apply to all financial institutions and all forms of AI, including generative AI and AI agents, in proportion to size and the materiality of AI risk. They cover board and senior management oversight, an inventory of AI use cases, systems or models, risk materiality assessment, life cycle controls and third-party AI. They take effect on 7 October 2027 for Sections 3-4 (oversight; risk management systems, policies and procedures), with Sections 5-6 (life cycle controls; capability and capacity) by 7 October 2028. Also: FEAT Principles (12 November 2018) and the Veritas toolkit; information paper on AI model risk management (5 December 2024); Technology Risk Management Guidelines (18 January 2021); Guidelines on Outsourcing (effective 11 December 2024), which proposed Third-Party Risk Management Guidelines (consultation of 6 March 2026) would supersede. |
| **Other national guidance** | The Model AI Governance Framework (2nd edition, 21 January 2020) is issued by IMDA and PDPC, not MAS. IMDA and the AI Verify Foundation issued the Model AI Governance Framework for Generative AI (30 May 2024). IMDA launched the Model AI Governance Framework for Agentic AI on 22 January 2026 and published version 1.5 on 20 May 2026. |
| **Framework maps to** | Materiality assessment: [risk-matrix.md](../risk-classification/risk-matrix.md), RA-001, RA-002. Oversight: [roles-responsibilities.md](../operating-model/roles-responsibilities.md), [review-cadence.md](../operating-model/review-cadence.md), RV-001. Life cycle controls: DE, EV, DA and PM controls. Third-party AI: AR-004, AR-005, [third-party-model-risk.md](third-party-model-risk.md#regulatory-hooks). FEAT: [bias-detection-llm.md](../responsible-ai/bias-detection-llm.md) (EV-005), [transparency-standards.md](../responsible-ai/transparency-standards.md), [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md). Agentic framework: [agentic-ai-risk.md](../risk-classification/agentic-ai-risk.md), [multi-agent-governance.md](../llm-lifecycle/multi-agent-governance.md). AI inventory: RA-006 (registration before development), GV-006 (completeness and reconciliation), [ai-inventory.md](../governance-operations/ai-inventory.md). |
| **Gaps** | Consider AI Verify testing for Singapore-deployed systems. |

### Canada

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | PIPEDA and provincial privacy laws. Quebec Law 25: section 12.1 of the private-sector Act (in force 22 September 2023) requires notice and a chance to have a decision reviewed when it is made exclusively by automated processing. AIDA (Part 3 of Bill C-27) died on the Order Paper when Parliament was prorogued on 6 January 2025. Bill C-36 (Protecting Privacy and Consumer Data Act), introduced 15 June 2026 and at second reading, is a privacy bill that would add transparency for automated decision systems; it does not revive AIDA. |
| **Supervisory expectations (financial sector)** | OSFI Guideline E-23 Model Risk Management (published 11 September 2025, effective 1 May 2027) applies to all federally regulated financial institutions; its model definition expressly includes AI/ML methods, and it expects an enterprise model inventory, risk rating, lifecycle controls and independent review. Guideline B-10 Third-Party Risk Management (effective 1 May 2024) and B-13 Technology and Cyber Risk Management (effective 1 January 2024). |
| **Framework maps to** | E-23: [risk-matrix.md](../risk-classification/risk-matrix.md) tiering, RA-001, RA-004, model lifecycle standards, RV-001, RV-003. B-10: AR-005, [third-party-model-risk.md](third-party-model-risk.md). B-13: [ai-security](../ai-security/adversarial-robustness.md) standards, SR-003. Quebec s. 12.1: PM-003, DE-009 (notice), RV-005 (review on request), [transparency-standards.md](../responsible-ai/transparency-standards.md#ai-assisted-decision-notices). E-23 enterprise model inventory: RA-006, GV-006. |
| **Gaps** | No open control gaps for the items above. Monitor Bill C-36 for automated decision transparency duties. |

### Australia

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | Privacy Act 1988, including APP 8 on cross-border disclosure. From 10 December 2026, APP 1.7 to 1.9 (added by the Privacy and Other Legislation Amendment Act 2024) require privacy policies to cover automated decisions that use personal information. The National AI Plan (2 December 2025) did not adopt mandatory guardrails or an AI-specific Act; it relies on existing, technology-neutral laws and funds an AI Safety Institute from early 2026. |
| **Supervisory expectations (financial sector)** | APRA CPS 230 Operational Risk Management (in force since 1 July 2025; remade version from 1 July 2026): material service providers, formal agreements and APRA notification. APRA CPS 234 Information Security (since 1 July 2019). APRA letter to industry on AI (30 April 2026): board AI literacy, visibility of the AI supply chain including material third- and fourth-party dependencies, continuous assurance, and stronger supervisory action where AI risks are not controlled. APRA and ASIC joint statement on frontier AI and cyber risk (27 August 2026). |
| **Framework maps to** | CPS 230: AR-005, [third-party-model-risk.md](third-party-model-risk.md#regulatory-hooks) exit and concentration requirements. CPS 234: [ai-security](../ai-security/adversarial-robustness.md) standards, SR-001 to SR-004. Automated decision transparency, including privacy policy wording under APP 1.7 to 1.9: DE-009, [transparency-standards.md](../responsible-ai/transparency-standards.md#ai-assisted-decision-notices). |
| **Gaps** | Fourth-party AI dependencies: mapped under AR-007 ([AI procurement clauses](ai-procurement-clauses.md)); ongoing monitoring of fourth parties beyond contract terms is not yet a control. |

### Japan

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | APPI (Act on the Protection of Personal Information). AI Promotion Act (Act No. 53 of 2025): enacted 28 May 2025, partly in force 4 June 2025, fully in force 1 September 2025; it set up the AI Strategic Headquarters. The Cabinet adopted the first AI Basic Plan on 23 December 2025 and a second on 14 July 2026. |
| **Supervisory expectations (financial sector)** | FSA "AI Discussion Paper" (Preliminary Discussion Points for Promoting the Sound Utilization of AI in the Financial Sector), published March 2025; version 1.1 published 3 March 2026. |
| **Framework maps to** | APPI: privacy controls and RA-005; the EU adequacy decision simplifies EU-Japan transfers ([cross-border-data-governance.md](cross-border-data-governance.md)). FSA paper: reference only. |
| **Gaps** | No mapping of the FSA AI Discussion Paper to framework controls. |

### Brazil

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | LGPD (Lei Geral de Protecao de Dados) in force. AI bill PL 2338/2023: passed by the Senate on 10 December 2024 and sent to the Chamber of Deputies on 17 March 2025, where it is awaiting the rapporteur's report in a special committee. It is not law as of November 2026. |
| **Supervisory expectations (financial sector)** | CMN Resolution 4,893/2021 on cyber security policy and contracting of data processing, storage and cloud services, amended by CMN Resolution 5,274 of 18 December 2025 (existing institutions to comply by 1 March 2026). No AI-specific Central Bank rule found. |
| **Framework maps to** | LGPD: GDPR-aligned privacy controls, RA-005. Cloud contracting: AR-003, AR-005. |
| **Gaps** | Monitor PL 2338/2023; its risk classification and impact assessment duties would need a local mapping if enacted. |

### United Arab Emirates

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | DIFC Data Protection Regulations, Regulation 10 (processing personal data through autonomous and semi-autonomous systems), in force 1 September 2023; amendments were consulted on in June 2026 and have not been enacted. ADGM Data Protection Regulations 2021, including section 20 on automated decision-making. The UAE government approved a federal Artificial Intelligence and Data Authority on 14 June 2026, chaired by the Minister of State for Artificial Intelligence. |
| **Supervisory expectations (financial sector)** | CBUAE "Guidance Note on Consumer Protection and the Responsible Adoption and Use of Artificial Intelligence and Machine Learning by Licensed Financial Institutions" (issued 11 February 2026; guidance, not binding): board and senior management accountability, fairness, transparency and explainability, human oversight (human-out-of-the-loop only for low-risk, non-material processes), an AI model inventory under the CBUAE Model Management Standards, and outsourcing and third-party risk. |
| **Framework maps to** | CBUAE note: [roles-responsibilities.md](../operating-model/roles-responsibilities.md), PM-003 and [human-in-loop-patterns.md](../responsible-ai/human-in-loop-patterns.md#pattern-selection-matrix), EV-005, AR-005. DIFC Regulation 10 and ADGM s. 20: RA-005, PM-003. Data residency: [cross-border-data-governance.md](cross-border-data-governance.md). AI model inventory: RA-006, GV-006. |
| **Gaps** | DIFC Regulation 10 duties need a local mapping. |

### South Korea

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | Framework Act on the Development of Artificial Intelligence and Establishment of Trust (AI Basic Act, Law No. 20676): promulgated 21 January 2025, in force 22 January 2026, with its Enforcement Decree. Fines of up to KRW 30 million apply for failing to give the notice required by Art. 31(1), failing to designate a domestic agent (Art. 36(1)) or not complying with a suspension or correction order (Art. 40(3)). MSIT announced a grace period of at least one year on fact-finding and fines; this is an administrative policy, not part of the Act. |
| **Framework maps to** | Advance notice that a product or service runs on high-impact or generative AI (Art. 31(1)): DE-006, [transparency-standards.md](../responsible-ai/transparency-standards.md#user-interaction-disclosure). Indication of generative AI output and notice of realistic synthetic sound, images or video (Art. 31(2) and (3)): DE-007. |
| **Gaps** | Domestic agent designation is a legal-entity matter outside the framework. |

### China

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | Measures for Labeling AI-Generated and Synthetic Content (CAC, MIIT, MPS and NRTA; issued 7 March 2025, effective 1 September 2025) and the mandatory national standard GB 45438-2025 on labelling methods (effective 1 September 2025). |
| **Framework maps to** | Content labelling: DE-007, [transparency-standards.md](../responsible-ai/transparency-standards.md#machine-readable-marking). |
| **Gaps** | This guide does not cover China's other AI and data rules. |

### India

| Aspect | Detail |
|--------|--------|
| **Binding instruments** | IT Rules 2021, amended on 10 February 2026 for synthetically generated information: intermediaries must label permitted AI-generated content with metadata, take technical measures against unlawful synthetic content, and remove content within 3 hours of a court order or reasoned government intimation. Digital Personal Data Protection Rules 2025, notified 13 November 2025 with an 18-month phased timeline. |
| **Supervisory expectations (financial sector)** | RBI FREE-AI committee report (Framework for Responsible and Ethical Enablement of AI, 13 August 2025): 7 Sutras and 26 recommendations under six pillars. No AI-specific RBI direction found as of November 2026. |
| **Framework maps to** | Synthetic content labelling, where the organisation acts as an intermediary: DE-007, [transparency-standards.md](../responsible-ai/transparency-standards.md#machine-readable-marking). DPDP: RA-005 and privacy controls. FREE-AI: reference only until the RBI issues directions. |
| **Gaps** | DPDP consent and notice duties need a local mapping before the 18-month phase ends. |

### International Standard Setters

| Body | Publication | Status | Use in this framework |
|------|-------------|--------|-----------------------|
| Financial Stability Board | "Sound Practices for Responsible Adoption of Artificial Intelligence (AI)", final report to the G20, 15 October 2026. Twelve sound practices, from board oversight and materiality assessment to human oversight and third-party AI risk; covers generative and agentic AI. Earlier: "Monitoring Adoption of AI and Related Vulnerabilities in the Financial Sector" (10 October 2025) | Final, non-binding | Cross-check: materiality ([risk-matrix.md](../risk-classification/risk-matrix.md)), human oversight (PM-003), third-party AI (AR-005), ICT risk (SR-003) |
| Basel Committee | "Digitalisation of finance" (16 May 2024), with a section on AI and machine learning; AI horizon scanning in the 2025-26 work programme | No AI-specific standard | Reference only |
| IOSCO | "Artificial Intelligence in Capital Markets: Use Cases, Risks, and Challenges", consultation report (March 2025) | Consultation | Reference only |

---

## Decision Matrix

"If you operate in these jurisdictions, here is what you need beyond the base framework."

| Operating Jurisdictions | Additional Requirements |
|------------------------|------------------------|
| EU only | Follow the [EU AI Act mapping](eu-ai-act-mapping.md) and its dates (Annex III high-risk from 2 December 2027). Financial entities: add AI vendors to the DORA register of information. |
| EU + UK | Apply PRA SS1/23 to models at banks with internal model approval. Evidence Consumer Duty outcomes for customer-facing AI. Document the UK automated decision basis (Arts. 22A-22D) separately from GDPR Art. 22. |
| EU + US | Add [NIST AI RMF mapping](nist-ai-rmf-mapping.md). Apply SR 26-2 to traditional and non-generative AI models; GenAI and agentic AI stay under framework controls. Prepare for Colorado SB 26-189 and California ADMT rules (both 1 January 2027): notices under DE-009, explanation and human review under RV-005. Track federal preemption litigation. |
| EU + Singapore | Map the MAS Guidelines on AI Risk Management: oversight and risk management systems by 7 October 2027, life cycle controls by 7 October 2028. Build the AI inventory MAS expects (RA-006, GV-006). Apply FEAT; consider AI Verify testing. Use the IMDA agentic framework for agent systems. |
| EU + Australia | Apply APRA CPS 230 to AI vendors that are material service providers, and CPS 234. Add automated decision disclosures to privacy policies by 10 December 2026 (DE-009). |
| EU + Japan | Leverage EU adequacy decision for data transfers. Use the FSA AI Discussion Paper (version 1.1) for financial services. |
| EU + South Korea, China or India | Korea: AI notice (DE-006), output labelling (DE-007) and domestic agent duties under the AI Basic Act. China: label AI-generated content (DE-007). India: synthetic content rules for platforms (DE-007 where the organisation is an intermediary); DPDP Rules timeline. |
| EU + UAE | Map the CBUAE AI guidance note for licensed financial institutions. Assess DIFC Regulation 10 and ADGM data protection duties. Confirm onshore processing for restricted data. |
| EU + Brazil | Ensure LGPD legal bases. Add CMN Resolution 4,893 cloud contracting. Monitor PL 2338/2023. |
| EU + Canada | Prepare for OSFI E-23 (1 May 2027), including a model inventory (RA-006, GV-006). Quebec Law 25 s. 12.1 notice for automated decisions. Monitor Bill C-36. |
| Global (4+ jurisdictions) | Implement [regulatory change monitoring](regulatory-change-monitoring.md). Appoint jurisdictional compliance leads. Use [cross-border data governance](cross-border-data-governance.md) for data flow management. Apply strictest standard as default; document exceptions. |

---

## Regulatory Conflict Resolution

When regulations from different jurisdictions conflict:

| Principle | Application |
|-----------|-------------|
| **Apply the strictest standard** | Unless doing so creates a direct conflict with another jurisdiction's mandatory requirement |
| **Document the conflict** | Record the conflicting requirements, analysis, and chosen resolution |
| **Seek legal guidance** | Regulatory conflicts require legal analysis; do not resolve based on technical judgment alone |
| **Implement jurisdiction-aware controls** | Where standards differ, implement controls that detect user/data jurisdiction and apply appropriate rules |
| **Engage regulators** | For genuine conflicts with no clear resolution, engage with the relevant regulators (after legal counsel) |

Common conflict patterns and resolutions are documented in [cross-border-data-governance.md](cross-border-data-governance.md).

---

## Implementation Notes

- No organization needs to comply with all 12 jurisdictions simultaneously. Start with your primary operating jurisdictions.
- The base framework was designed for EU, UK and US financial services. Use the gaps row in each profile to see what it does not cover elsewhere.
- Regulatory landscape is evolving rapidly; review this guide quarterly against [regulatory change monitoring](regulatory-change-monitoring.md) outputs.
- Engage local legal counsel in each operating jurisdiction; this guide provides governance direction, not legal advice.

---

## Sources

EU
- Regulation (EU) 2024/1689 (AI Act), Arts. 53, 101, 111, 113: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Regulation (EU) 2026/1744 (Digital Omnibus on AI): https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Commission Implementing Decision (EU) 2026/2274 on harmonised standards for high-risk AI systems: https://eur-lex.europa.eu/eli/dec_impl/2026/2274/oj
- European Commission, "Standardisation of the AI Act" (updated 19 October 2026): https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation
- Regulation (EU) 2022/2554 (DORA): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Regulation (EU) 2016/679 (GDPR), Art. 22(3): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- ESAs, "European Supervisory Authorities designate critical ICT third-party providers" (18 November 2025): https://www.esma.europa.eu/press-news/esma-news/european-supervisory-authorities-designate-critical-ict-third-party-providers
- EBA, "AI Act: implications for the EU banking and payments sector" (21 November 2025): https://www.eba.europa.eu/sites/default/files/2025-11/d8b999ce-a1d9-4964-9606-971bbc2aaf89/AI%20Act%20implications%20for%20the%20EU%20banking%20sector.pdf
- EIOPA, Opinion on AI governance and risk management (6 August 2025): https://www.eiopa.europa.eu/eiopa-publishes-opinion-ai-governance-and-risk-management-2025-08-06_en
- ESMA, public statement on AI and investment services (30 May 2024): https://www.esma.europa.eu/press-news/esma-news/esma-provides-guidance-firms-using-artificial-intelligence-investment-services
- ESAs, statement on ICT risks from frontier AI models (31 July 2026): https://www.esma.europa.eu/press-news/esma-news/eba-eiopa-and-esma-call-enhanced-governance-and-consistent-supervision

United Kingdom
- PRA, SS1/23 Model risk management principles for banks: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- PRA, Low Impact Amendments Finalisation April 2026: https://www.bankofengland.co.uk/prudential-regulation/publication/2026/april/low-impact-amendments-finalisation-april-2026
- Letter from Sarah Breeden and Sam Woods to the Chancellor (1 April 2026): https://www.bankofengland.co.uk/-/media/boe/files/letter/2026/letter-from-sarah-breeden-sam-woods-to-chancellor.pdf
- FCA, AI Update (April 2024): https://www.fca.org.uk/publication/corporate/ai-update.pdf
- FCA, AI approach: https://www.fca.org.uk/firms/innovation/ai-approach
- FCA, The Mills Review (6 July 2026): https://www.fca.org.uk/publications/corporate-documents/mills-review
- FCA, "AI in financial services: good practice and areas for improvement" (19 October 2026): https://www.fca.org.uk/publications/good-poor-practice/ai-financial-services
- FCA, "FCA helps firms to test AI safely" (3 December 2025): https://www.fca.org.uk/news/press-releases/fca-helps-firms-test-ai-safely
- FCA, Consumer Duty information for firms: https://www.fca.org.uk/firms/consumer-duty/information-firms
- GOV.UK, Data (Use and Access) Act 2025: plans for commencement: https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement
- IAPP, "King's Speech signals diffuse UK digital policy agenda but no AI bill" (14 May 2026): https://iapp.org/news/a/king-s-speech-signals-diffuse-uk-digital-policy-agenda-but-no-ai-bill
- GOV.UK, AI Security Institute renaming (14 February 2025): https://www.gov.uk/government/news/tackling-ai-security-risks-to-unleash-growth-and-deliver-plan-for-change

United States
- Federal Reserve, SR 26-2 Revised Guidance on Model Risk Management (17 April 2026): https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
- OCC Bulletin 2026-13: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html
- FDIC FIL-15-2026: https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance
- Executive Order 14365 (11 December 2025): https://www.govinfo.gov/content/pkg/DCPD-202501186/html/DCPD-202501186.htm
- Attorney General memorandum establishing the AI Litigation Task Force (9 January 2026): https://www.justice.gov/ag/media/1422986/dl
- United States motion to intervene, X.AI LLC v. Weiser, No. 1:26-cv-01515 (D. Colo.): https://storage.courtlistener.com/recap/gov.uscourts.cod.253513/gov.uscourts.cod.253513.12.0.pdf
- White House, National Policy Framework for AI: Legislative Recommendations (20 March 2026): https://www.whitehouse.gov/releases/2026/03/president-donald-j-trump-unveils-national-ai-legislative-framework/
- FTC, proposed Policy Statement Concerning the Suppression of Accuracy in AI Systems (7 July 2026): https://www.govinfo.gov/content/pkg/FR-2026-07-07/pdf/2026-13628.pdf
- OMB memoranda (M-25-21, M-25-22): https://www.whitehouse.gov/omb/information-resources/guidance/memoranda/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- SEC, Withdrawal of Proposed Regulatory Actions (17 June 2025): https://www.federalregister.gov/documents/2025/06/17/2025-11110/withdrawal-of-proposed-regulatory-actions
- Colorado SB 26-189: https://leg.colorado.gov/bills/sb26-189
- McDermott, "Colorado AI law in flux": https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/
- CPPA, announcement of approved ADMT, risk assessment and cybersecurity audit regulations (23 September 2025): https://cppa.ca.gov/announcements/2025/20250923.html
- CPPA, approved regulation text (ADMT: sections 7200, 7220 to 7222): https://cppa.ca.gov/regulations/pdf/ccpa_updates_cyber_risk_admt_appr_text.pdf
- Governor of California, SB 53 signing (29 September 2025): https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/
- AB 853 (2025): https://calmatters.digitaldemocracy.org/bills/ca_202520260ab853
- SB 1000 (2026): https://calmatters.digitaldemocracy.org/bills/ca_202520260sb1000
- Governor of California, AI bills signed 30 September 2026: https://www.gov.ca.gov/2026/09/30/californias-nation-leading-ai-framework-just-got-stronger-governor-newsom-signs-more-first-in-the-nation-worker-protections-and-more/
- Texas HB 149 history: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149
- Littler, "Texas joins the fray and enacts AI legislation": https://www.littler.com/news-analysis/asap/texas-joins-fray-and-enacts-ai-legislation
- Morgan Lewis, Illinois HB 3773: https://www.morganlewis.com/pubs/2024/09/illinois-passes-new-law-to-address-ai-in-the-workplace
- Epstein Becker Green, Illinois HB 3773: https://www.ebglaw.com/workforce-bulletin/illinois-prohibits-discriminatory-artificial-intelligence-in-employment-decisions
- New York S6953B (RAISE Act): https://www.nysenate.gov/legislation/bills/2025/S6953/amendment/B
- New York S8828 (RAISE Act chapter amendment): https://www.nysenate.gov/legislation/bills/2025/S8828
- NYC DCWP, Automated Employment Decision Tools: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page

Singapore
- MAS, Guidelines on AI Risk Management for Financial Institutions (7 October 2026): https://www.mas.gov.sg/regulation/guidelines/guidelines-on-artificial-intelligence-risk-management-for-financial-institutions
- MAS, FEAT Principles (2018): https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/feat
- MAS, Veritas: https://www.mas.gov.sg/schemes-and-initiatives/veritas
- MAS, Information Paper on AI Model Risk Management (5 December 2024): https://www.mas.gov.sg/publications/monographs-or-information-paper/2024/artificial-intelligence-model-risk-management
- MAS, Technology Risk Management Guidelines: https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines
- MAS, Guidelines on Outsourcing (Banks): https://www.mas.gov.sg/regulation/guidelines/guidelines-on-outsourcing-banks
- MAS, Annual Report 2025/26, operational and third-party risk management: https://www.mas.gov.sg/publications/annual-report/2026/annual-report-2025-2026/robust-and-resilient-financial-centre/operational-risk-and-third-party-risk-management
- IMDA and PDPC, Model AI Governance Framework (2nd edition): https://www.imda.gov.sg/-/media/imda/files/infocomm-media-landscape/sg-digital/tech-pillars/artificial-intelligence/second-edition-of-the-model-ai-governance-framework.pdf
- AI Verify Foundation, Model AI Governance Framework for Generative AI (30 May 2024): https://aiverifyfoundation.sg/news/press-release-launch-of-model-ai-governance-framework-for-generative-ai/
- MDDI, Model AI Governance Framework for Agentic AI (22 January 2026): https://www.mddi.gov.sg/newsroom/singapore-launches-new-model-ai-governance-framework-for-agentic-ai--/
- IMDA, Model AI Governance Framework for Agentic AI, version 1.5: https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf

Canada
- LEGISinfo, Bill C-27 (44th Parliament): https://www.parl.ca/legisinfo/en/bill/44-1/c-27
- LEGISinfo, Bill C-36 (45th Parliament): https://www.parl.ca/legisinfo/en/bill/45-1/c-36
- OSFI, Guideline E-23 Model Risk Management (2027): https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027
- OSFI, Guideline B-13 final release letter: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/osfi-releases-final-guideline-b-13-technology-cyber-risk-management-letter-2022
- OSFI, Guideline B-10 consultation summary: https://www.osfi-bsif.gc.ca/en/consultations/consultation-summaries/third-party-risk-management-guideline-summary-response-consultation-feedback
- Osler, Law 25 enforcement and automated decisions: https://www.osler.com/en/insights/updates/law-25-a-new-enforcement-scheme-for-protection-of-personal-information-in-the-private-sector-in-que/
- Clyde & Co, "Law 25: Quebec's second wave of new privacy amendments is here": https://www.clydeco.com/es/insights/2023/09/law-25-quebec-s-second-wave-of-new-privacy-amendme

Australia
- Privacy and Other Legislation Amendment Act 2024 (commencement table): https://legislation.gov.au/C2024A00128/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html
- OAIC, APP Guidelines Chapter 1: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information
- IAPP, "Australia unveils AI policy roadmap": https://iapp.org/news/a/australia-unveils-ai-policy-roadmap
- Lowy Institute, "Australia bets old laws can manage new AI risks" (3 December 2025): https://www.lowyinstitute.org/the-interpreter/australia-bets-old-laws-manage-new-ai-risks
- APRA, CPS 230 (2025 version): https://handbook.apra.gov.au/standard/cps-230-superseded
- APRA, CPS 230: https://www.apra.gov.au/standards/cps-230
- APRA, CPS 234: https://www.apra.gov.au/standards/cps-234
- APRA, Letter to industry on AI (30 April 2026): https://www.apra.gov.au/news-and-publications/apra-letter-industry-artificial-intelligence-ai
- APRA and ASIC, frontier AI statement (27 August 2026): https://www.apra.gov.au/news-and-publications/apra-and-asic-warn-frontier-ai-awareness-must-turn-action

Japan
- Cabinet Office, AI Promotion Act overview: https://www8.cao.go.jp/cstp/ai/ai_hou_gaiyou.pdf
- Cabinet Office, AI Basic Plan: https://www8.cao.go.jp/cstp/ai/ai_plan/ai_plan.html
- FSA, AI Discussion Paper: https://www.fsa.go.jp/en/news/2025/20250304/aidp.html

Brazil
- Senado Federal, PL 2338/2023: https://www25.senado.leg.br/web/atividade/materias/-/materia/157233
- Camara dos Deputados, PL 2338/2023: https://www.camara.leg.br/propostas-legislativas/2487262
- BCB, Resolucao CMN 4.893: https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=4893
- BCB, Resolucao CMN 5.274: https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=5274

United Arab Emirates
- CBUAE Rulebook, Guidance Note on Consumer Protection and the Responsible Adoption and Use of AI and ML (11 February 2026): https://rulebook.centralbank.ae/en/rulebook/guidance-note-consumer-protection-and-responsible-adoption-and-use-artificial-intelligence
- DIFC, "DIFC Enacts Amended Data Protection Regulations" (7 September 2023): https://www.difc.com/whats-on/news/difc-enacts-amended-data-protection-regulations
- DIFC, consultation on amended Data Protection Regulations (June 2026): https://www.difc.com/whats-on/news/difc-consultation-amended-data-protection-regulations
- ADGM Data Protection Regulations 2021: https://en.adgm.thomsonreuters.com/rulebook/data-protection-regulations-2021
- Dubai Media Office, Artificial Intelligence and Data Authority (14 June 2026): https://mediaoffice.ae/en/news/2026/june/14-06/mohammed-bin-rashid-approves-establishing-artificial-intelligence-and-data-authority

South Korea
- AI Basic Act (law.go.kr): https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=282791
- MSIT press release on implementation and grace period (21 January 2026): https://www.msit.go.kr/bbs/view.do?sCode=user&mId=307&mPid=208&bbsSeqNo=94&nttSeqNo=3186786

China
- CAC, Measures for Labeling AI-Generated and Synthetic Content: https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm

India
- PIB, Lok Sabha reply on synthetically generated information (6 August 2026): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2295500
- PIB, DPDP Rules 2025 (14 November 2025): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014
- RBI, FREE-AI committee report press release (13 August 2025): https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61018

International
- FSB, Sound Practices for Responsible Adoption of AI, final report (15 October 2026): https://www.fsb.org/2026/10/sound-practices-for-responsible-adoption-of-artificial-intelligence-ai-final-report/
- FSB, Monitoring Adoption of AI and Related Vulnerabilities in the Financial Sector (10 October 2025): https://www.fsb.org/2025/10/monitoring-adoption-of-artificial-intelligence-and-related-vulnerabilities-in-the-financial-sector/
- BCBS, Digitalisation of finance (16 May 2024): https://www.bis.org/bcbs/publ/d575.htm
- BCBS, work programme: https://www.bis.org/bcbs/about/work_programme.htm
- IOSCO, AI in Capital Markets consultation report (March 2025): https://www.iosco.org/library/pubdocs/pdf/IOSCOPD788.pdf
