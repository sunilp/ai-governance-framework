# Cross-Border AI Data Governance

## Overview

AI systems increasingly operate across jurisdictional boundaries — training data sourced globally, models hosted in one region, users in another, and compliance obligations varying by jurisdiction. This creates data governance challenges that go beyond what traditional data residency frameworks address.

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

This document provides governance standards for AI data flows crossing jurisdictions. It complements [data-residency-llm.md](data-residency-llm.md), which covers LLM-specific architecture patterns and EU/US data flows. This document takes a broader view: all AI system types across 8+ jurisdictions.

---

## Multi-Jurisdictional Data Flow Mapping

### Data Categories in AI Systems

| Data Category | Description | Jurisdictional Sensitivity |
|--------------|-------------|:---:|
| Training data (traditional ML) | Datasets used to train models | High — may contain PII from multiple jurisdictions |
| Feature stores | Aggregated features derived from source data | Medium — may inherit restrictions from source data |
| Model artifacts | Trained model weights and configurations | Low-Medium — but may encode training data properties |
| Fine-tuning data | Datasets used to fine-tune foundation models | High — same considerations as training data |
| Prompts and context | User inputs, system prompts, RAG-retrieved documents | High — often contains PII or confidential data |
| Model outputs | Generated text, images, audio, predictions | Medium — may contain PII or be subject to transparency rules |
| Evaluation data | Test datasets used for model validation | Medium-High — may contain PII |
| Audit trail | Logs of prompts, responses, decisions | High — contains operational PII; subject to retention rules |
| User feedback | Ratings, corrections, escalation records | Medium — linked to user identity |

For each AI system, document which of these data categories cross jurisdictional boundaries and which jurisdictions are involved.

---

## Sovereignty Requirements by Jurisdiction

| Jurisdiction | Key Requirement | AI-Specific Impact | Financial Services Overlay |
|-------------|----------------|-------------------|---------------------------|
| **EU (GDPR + AI Act)** | Personal data processed in EEA or with adequate safeguards (SCCs, adequacy); AI Act transparency obligations | Prompts with PII must be processed in compliant regions; synthetic media labeling required; GPAI model provider obligations | EBA/ESMA outsourcing guidelines; DORA (applies from 17 January 2025): every ICT services contract goes in the register of information (Art. 28(3)) and must state where services are provided and data is processed and stored (Art. 30(2)(b)). Critical ICT third-party provider status is designated by the ESAs (Art. 31), not assessed by the firm |
| **UK** | UK GDPR as amended by the Data (Use and Access) Act 2025; the EU renewed its UK adequacy decisions on 19 December 2025, to expire on 27 December 2031 | EU-UK transfers rely on adequacy; automated decisions follow UK Arts. 22A-22D (in force 5 February 2026), not GDPR Art. 22 | PRA SS1/23 for models at banks with internal model approval; FCA Consumer Duty for customer outcomes |
| **US** | Sector-specific: HIPAA (health), GLBA (financial), state laws (CA CCPA/CPRA, CO, VA, CT, TX, etc.); no federal AI data residency | State-by-state compliance for consumer-facing AI, including California ADMT rules and Colorado SB 26-189 (both from 1 January 2027) | SR 26-2 model risk guidance (Federal Reserve, OCC, FDIC; 17 April 2026; replaced SR 11-7). GenAI and agentic AI are outside its scope |
| **Singapore** | PDPA; MAS guidelines on cloud outsourcing; MAS FEAT principles | Relatively flexible on data flows; MAS expects risk management for cloud-hosted AI, and its AI Risk Management Guidelines (take effect 7 October 2027) expect controls over third-party AI | MAS Technology Risk Management Guidelines; MAS Guidelines on Outsourcing (to be superseded by proposed Third-Party Risk Management Guidelines) |
| **UAE** | DIFC/ADGM data protection, including DIFC Regulation 10 on autonomous and semi-autonomous systems; sector-specific requirements | Onshore processing requirements for certain government and financial data | CBUAE regulations, including its AI guidance note for licensed financial institutions (11 February 2026), which covers outsourcing and third-party risk; DFSA/FSRA requirements |
| **Brazil** | LGPD; AI Bill PL 2338/2023 (passed by the Senate 10 December 2024; awaiting the rapporteur's report in a Chamber of Deputies special committee; not law as of November 2026) | Data localization for government data; LGPD consent requirements for AI processing | CMN Resolution 4,893/2021 on data processing, storage and cloud contracting, amended by CMN Resolution 5,274/2025 |
| **Canada** | PIPEDA + provincial laws. AIDA (Part 3 of Bill C-27) died on the Order Paper on 6 January 2025. Bill C-36, a privacy bill introduced 15 June 2026, is at second reading | PIPEDA applies to cross-border transfers; Quebec Law 25 adds notice for decisions made exclusively by automated processing | OSFI B-13 Technology and Cyber Risk; B-10 Third-Party Risk Management; E-23 Model Risk Management from 1 May 2027 |
| **Australia** | Privacy Act; the National AI Plan (2 December 2025) relies on existing laws rather than mandatory AI guardrails | Relatively flexible; APP 8 requires reasonable steps for overseas disclosure; automated decision transparency in privacy policies from 10 December 2026 | APRA CPS 230 (material service providers) and CPS 234 |
| **Japan** | APPI; EU adequacy decision; AI Promotion Act (fully in force 1 September 2025) | Adequacy decision simplifies EU-Japan transfers; APPI consent rules for third-party provision | FSA AI Discussion Paper (version 1.1, 3 March 2026) |

---

## Conflict Resolution Patterns

Cross-border AI systems inevitably encounter regulatory conflicts. These patterns provide resolution approaches.

### GDPR Right-to-Delete vs. Regulatory Retention

**Conflict:** GDPR Article 17 gives data subjects the right to erasure. Financial regulators require retention of transaction records, communications, and model decision logs for 5–7 years.

**Resolution:**
1. Identify the legal basis for retention (regulatory obligation under GDPR Article 17(3)(b))
2. Restrict access to retained data — remove from active AI processing
3. Delete from training data, RAG corpus, and active model context
4. Retain in audit trail with access restriction and documented legal basis
5. Delete when retention obligation expires

### Data Localization vs. Cloud-First Strategy

**Conflict:** Jurisdictions requiring onshore processing vs. organizational preference for centralized cloud infrastructure.

**Resolution:**
1. Classify data by sensitivity and jurisdictional restrictions
2. Non-sensitive data: process in centralized cloud infrastructure
3. Restricted data: process in jurisdiction-compliant regional infrastructure
4. MNPI and highly regulated data: self-hosted infrastructure in required jurisdiction
5. Document the architecture decision for each data category

### Divergent Consent Requirements

**Conflict:** Different jurisdictions have different consent standards for AI processing of personal data.

**Resolution:**
- Apply the strictest applicable consent standard across all jurisdictions where the system operates
- If this is impractical, implement jurisdiction-aware consent collection (detect user jurisdiction; apply local rules)
- Document the consent basis per jurisdiction in the risk assessment

### AI Transparency vs. Trade Secrets

**Conflict:** Regulatory transparency requirements (explainability, disclosure) vs. protection of proprietary model architecture.

**Resolution:**
- Disclose methodology and approach without revealing proprietary architecture
- Provide decision-level explainability (why this output for this input) without model internals
- Document what is disclosed and what is protected, with legal basis for each
- Monitor regulatory guidance on acceptable explainability levels

---

## Transfer Mechanisms for AI Data

| Mechanism | Description | Applicability to AI |
|-----------|-------------|-------------------|
| Standard Contractual Clauses (SCCs) | EU-approved contract terms for cross-border transfers | Most common for LLM API usage (data flows to vendor infrastructure); also applies to training data transfers |
| Adequacy Decisions | EU determination that a jurisdiction provides adequate data protection | Simplifies transfers to: UK, Japan, South Korea, etc. Does not cover US broadly (use SCCs) |
| Binding Corporate Rules (BCRs) | Intra-group transfer mechanism approved by supervisory authorities | Suitable for organizations training models on data from multiple EU entities |
| Consent | Explicit consent from data subjects for the specific transfer | Impractical at scale for AI training data; viable for user-facing systems |
| Contractual Necessity | Transfer necessary for a contract with the data subject | Limited applicability; use for specific customer-facing AI services |
| GDPR Article 49 Derogations | Specific situations allowing transfer without SCCs/adequacy | Last resort; not suitable as primary mechanism for ongoing AI data flows |

### AI-Specific Transfer Considerations

- **Prompts containing PII**: every prompt sent to a vendor API is a data transfer — ensure DPA and SCCs cover this
- **Training/fine-tuning data**: bulk transfers of training data are subject to all standard transfer mechanisms
- **Model outputs**: generated outputs containing PII constitute processed personal data — transfer rules apply
- **Audit trail data**: retention of prompts/responses in logging infrastructure constitutes storage — residency rules apply
- **Evaluation data**: test datasets containing PII must comply with transfer mechanisms

---

## Cloud Provider Selection Criteria

For multi-jurisdictional AI deployments, cloud provider selection must account for:

| Criterion | Requirement |
|-----------|-------------|
| Regional availability | Provider offers compute and storage in all required jurisdictions |
| Data residency guarantees | Contractual commitment that data stays in specified region — not just default behavior |
| Sub-processor transparency | Full disclosure of sub-processors and their locations |
| Encryption and key management | Customer-managed encryption keys for T1 systems; provider-managed acceptable for T3/T4 |
| Compliance certifications | SOC 2 Type II, ISO 27001 minimum; local certifications where required (C5 for Germany, HDS for France, IRAP for Australia) |
| DPA availability | Data processing agreement covering GDPR and local requirements |
| Government access risk | Assess provider's jurisdiction of incorporation and government access obligations (CLOUD Act, etc.) |
| Exit strategy | Data portability, migration support, deletion certification |

---

## Implementation Notes

- Start by mapping data flows for T1 systems. Extend to T2, then T3/T4 as governance matures.
- Work with legal to maintain a jurisdiction-specific requirement register. Update it quarterly via [regulatory change monitoring](regulatory-change-monitoring.md).
- Automate jurisdiction detection where possible — know where your data is at all times, not just where you intend it to be.
- Cross-border data governance is a continuous activity, not a one-time assessment. Regulatory requirements, vendor infrastructure, and organizational operations all change.

---

## Sources

- Regulation (EU) 2022/2554 (DORA): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Hunton, "European Commission renews UK data adequacy decisions": https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-renews-uk-data-adequacy-decisions
- eucrim, "Commission renewed adequacy decisions for data transfers to the UK": https://eucrim.eu/news/commission-renewed-adequacy-decisions-for-data-transfers-to-the-uk/
- GOV.UK, Data (Use and Access) Act 2025: plans for commencement: https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement
- Federal Reserve, SR 26-2: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
- MAS, Guidelines on AI Risk Management for Financial Institutions: https://www.mas.gov.sg/regulation/guidelines/guidelines-on-artificial-intelligence-risk-management-for-financial-institutions
- CBUAE Rulebook, AI and ML guidance note for licensed financial institutions: https://rulebook.centralbank.ae/en/rulebook/guidance-note-consumer-protection-and-responsible-adoption-and-use-artificial-intelligence
- Camara dos Deputados, PL 2338/2023: https://www.camara.leg.br/propostas-legislativas/2487262
- BCB, Resolucao CMN 5.274: https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=5274
- LEGISinfo, Bill C-36: https://www.parl.ca/legisinfo/en/bill/45-1/c-36
- OSFI, Guideline E-23: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027
- OAIC, APP Guidelines Chapter 1: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information
- Cabinet Office (Japan), AI Promotion Act overview: https://www8.cao.go.jp/cstp/ai/ai_hou_gaiyou.pdf
- FSA, AI Discussion Paper: https://www.fsa.go.jp/en/news/2025/20250304/aidp.html
- Further jurisdiction sources: [multi-jurisdictional-guide.md](multi-jurisdictional-guide.md#sources)
