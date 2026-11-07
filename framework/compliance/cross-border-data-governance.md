# Cross-Border Data and LLM Data Residency

## Overview

AI systems increasingly operate across jurisdictional boundaries: training data sourced globally, models hosted in one region, users in another, and compliance obligations that vary by jurisdiction. LLM architectures add a further layer. Data flows through several processing stages (prompt assembly, API transmission, inference, response delivery, logging), and each stage can cross a jurisdictional boundary.

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

This document sets governance standards for AI data flows that cross jurisdictions, for all AI system types across 8+ jurisdictions. It also maps data flows in common LLM architectures and defines the residency controls for each.

---

## Multi-Jurisdictional Data Flow Mapping

### Data Categories in AI Systems

| Data Category | Description | Jurisdictional Sensitivity |
|--------------|-------------|:---:|
| Training data (traditional ML) | Datasets used to train models | High: may contain PII from multiple jurisdictions |
| Feature stores | Aggregated features derived from source data | Medium: may inherit restrictions from source data |
| Model artifacts | Trained model weights and configurations | Low-Medium: but may encode training data properties |
| Fine-tuning data | Datasets used to fine-tune foundation models | High: same considerations as training data |
| Prompts and context | User inputs, system prompts, RAG-retrieved documents | High: often contains PII or confidential data |
| Model outputs | Generated text, images, audio, predictions | Medium: may contain PII or be subject to transparency rules |
| Evaluation data | Test datasets used for model validation | Medium-High: may contain PII |
| Monitoring data | Data collected to monitor model behaviour in production | Medium-High: may contain PII; residency-controlled |
| Audit trail | Logs of prompts, responses, decisions | High: contains operational PII; subject to retention rules |
| User feedback | Ratings, corrections, escalation records | Medium: linked to user identity |

For each AI system, document which of these data categories cross jurisdictional boundaries and which jurisdictions are involved.

### LLM Data Flow Stages

**1. Prompt assembly**

| Stage | Data Involved | Residency Consideration |
|-------|--------------|------------------------|
| User input capture | User query, session context | Processed in application layer; governed by application hosting location |
| Context retrieval (RAG) | Enterprise documents, knowledge base | Retrieved from internal stores; residency governed by existing data governance |
| Prompt construction | System prompt + user input + retrieved context | Assembled in application layer; may contain PII, confidential data, or regulated information |

**2. Model inference.** This is where the full prompt most often leaves your infrastructure. The residency controls depend on the hosting option; see [architecture patterns](#architecture-patterns-and-residency).

**3. Response processing**

| Stage | Data Involved | Residency Consideration |
|-------|--------------|------------------------|
| Raw response receipt | Model output | Received from vendor infrastructure; enters application layer |
| Guardrail processing | Response filtered for safety, PII, compliance | Processed in application layer |
| Delivery to user | Final response | Delivered through application infrastructure |

**4. Logging and storage.** Audit trail, monitoring, evaluation and feedback data follow the rules for their category in the table above and for their classification below. The audit trail must also meet regulatory retention requirements.

---

## Residency Requirements by Data Classification

| Data Classification | Residency Requirement | Vendor API Permitted? |
|--------------------|----------------------|----------------------|
| Public data | No restrictions | Yes |
| Internal data | Organizational policy applies | Yes, with DPA |
| Confidential data | Regional restrictions may apply | Conditional: DPA required; regional endpoint preferred |
| PII (customer data) | GDPR / local DPR applies; regional processing | Conditional: DPA with Article 28 compliance; data processing region verified |
| MNPI (material non-public information) | Strict controls; may be prohibited from external processing | Generally no for external APIs; self-hosted or VPC required |
| Regulated data (credit, AML, sanctions) | Sectoral regulations apply (banking secrecy, BCBS) | Case-by-case; legal review required |

---

## Architecture Patterns and Residency

### Pattern 1: External Vendor API

```
User → Application (your cloud) → Vendor API (vendor's region) → Application → User
```

**Residency controls:**
- Verify vendor's data processing regions; the full prompt crosses to the vendor's processing region and is subject to the vendor's DPA
- Where the vendor offers regional inference endpoints, verify that data does not leave the specified region at any stage
- Confirm data is not retained by vendor (or retention terms are acceptable)
- Confirm data is not used for model training
- DPA in place with adequate clauses (GDPR Article 28, SCCs if cross-border)
- PII redaction before API call (where feasible)

**Suitable for:** Internal tools with non-sensitive data; public-facing applications with no PII in prompts.

### Pattern 2: Self-Hosted Model

```
User → Application (your cloud) → Model inference (your cloud) → Application → User
```

**Residency controls:**
- All data stays within organizational infrastructure; no cross-boundary transit
- Standard cloud security and residency controls apply
- No vendor data processing concerns

**Suitable for:** Use cases with strict data residency requirements; MNPI processing; high-sensitivity regulated data.

### Pattern 3: Vendor API with PII Redaction

```
User → Application → PII Redactor → Vendor API → PII Re-inserter → User
```

**Residency controls:**
- PII is stripped before data leaves organizational infrastructure
- Vendor processes de-identified data only
- PII redaction/re-insertion logic must be validated for completeness
- Residual re-identification risk must be assessed

**Suitable for:** Use cases where vendor API capability is needed but data contains PII.

### Pattern 4: Private Endpoint / VPC

```
User → Application (your cloud) → Vendor inference (dedicated VPC/private endpoint) → Application → User
```

**Residency controls:**
- Vendor provides dedicated compute in specified region
- Network traffic stays within private network
- Verify isolation guarantees, and that data does not egress to vendor's shared infrastructure
- DPA with enhanced isolation guarantees

**Suitable for:** High-sensitivity use cases where self-hosting is not feasible but vendor capability is required.

---

## Sovereignty Requirements by Jurisdiction

| Jurisdiction | Key Requirement | AI-Specific Impact | Financial Services Overlay |
|-------------|----------------|-------------------|---------------------------|
| **EU (GDPR + AI Act)** | Personal data processed in EEA or with adequate safeguards (SCCs, adequacy); AI Act transparency obligations | Prompts with PII must be processed in compliant regions; synthetic media labeling required; GPAI model provider obligations | EBA/ESMA outsourcing guidelines; DORA (applies from 17 January 2025) for every ICT services contract, including each model API (see [compliance mapping](#compliance-mapping)) |
| **UK** | UK GDPR as amended by the Data (Use and Access) Act 2025; the EU renewed its UK adequacy decisions on 19 December 2025, to expire on 27 December 2031 | EU-UK transfers rely on adequacy; automated decisions follow UK Arts. 22A-22D (in force 5 February 2026), not GDPR Art. 22 | PRA SS1/23 for models at banks with internal model approval; FCA Consumer Duty for customer outcomes |
| **US** | Sector-specific: HIPAA (health), GLBA (financial), state laws (CA CCPA/CPRA, CO, VA, CT, TX, etc.); no federal AI data residency | State-by-state compliance for consumer-facing AI, including California ADMT rules and Colorado SB 26-189 (both from 1 January 2027) | SR 26-2 model risk guidance (Federal Reserve, OCC, FDIC; 17 April 2026; replaced SR 11-7). GenAI and agentic AI are outside its scope |
| **Singapore** | PDPA; MAS guidelines on cloud outsourcing; MAS FEAT principles | Relatively flexible on data flows; MAS expects risk management for cloud-hosted AI, and its AI Risk Management Guidelines (take effect 7 October 2027) expect controls over third-party AI | MAS Technology Risk Management Guidelines; MAS Guidelines on Outsourcing (to be superseded by proposed Third-Party Risk Management Guidelines) |
| **UAE** | DIFC/ADGM data protection, including DIFC Regulation 10 on autonomous and semi-autonomous systems; sector-specific requirements | Onshore processing requirements for certain government and financial data | CBUAE regulations, including its AI guidance note for licensed financial institutions (11 February 2026), which covers outsourcing and third-party risk; DFSA/FSRA requirements |
| **Brazil** | LGPD; AI Bill PL 2338/2023 (passed by the Senate 10 December 2024; awaiting the rapporteur's report in a Chamber of Deputies special committee; not law as of November 2026) | Data localization for government data; LGPD consent requirements for AI processing | CMN Resolution 4,893/2021 on data processing, storage and cloud contracting, amended by CMN Resolution 5,274/2025 |
| **Canada** | PIPEDA + provincial laws. AIDA (Part 3 of Bill C-27) died on the Order Paper on 6 January 2025. Bill C-36, a privacy bill introduced 15 June 2026, is at second reading | PIPEDA applies to cross-border transfers; Quebec Law 25 adds notice for decisions made exclusively by automated processing | OSFI B-13 Technology and Cyber Risk; B-10 Third-Party Risk Management; E-23 Model Risk Management from 1 May 2027 |
| **Australia** | Privacy Act; the National AI Plan (2 December 2025) relies on existing laws rather than mandatory AI guardrails | Relatively flexible; APP 8 requires reasonable steps for overseas disclosure; automated decision transparency in privacy policies from 10 December 2026 | APRA CPS 230 (material service providers) and CPS 234 |
| **Japan** | APPI; EU adequacy decision; AI Promotion Act (fully in force 1 September 2025) | Adequacy decision simplifies EU-Japan transfers; APPI consent rules for third-party provision | FSA AI Discussion Paper (version 1.1, 3 March 2026) |

---

## Compliance Mapping

Sector rules that shape LLM data flows in financial services. Privacy regimes by jurisdiction, including GDPR, are in the table above.

| Regulation | Residency Requirement | LLM Impact |
|-----------|----------------------|------------|
| BCBS 239 | Data governance and aggregation standards | LLM outputs used in risk reporting must have traceable data lineage |
| Banking secrecy (varies) | Customer data may not leave jurisdiction | External LLM APIs may be prohibited for customer data processing |
| MiFID II | Transaction and communication recording | AI-assisted communications with clients must be recorded |
| DORA (Regulation (EU) 2022/2554, applies from 17 January 2025) | ICT risk management and ICT third-party risk for EU financial entities (Arts. 28-30) | Every LLM API contract is an ICT service: record it in the register of information (Art. 28(3)) and state in the contract the regions or countries where the service is provided and data is processed and stored, with advance notice of changes (Art. 30(2)(b)). Assess before contracting whether the service supports a critical or important function (Art. 28(4)); if it does, the extra terms in Art. 30(3) and an exit strategy (Art. 28(8)) apply. Critical ICT third-party provider status is a designation made by the ESAs (Art. 31), not something the firm assesses |
| PSD2 | Payment data security | Transaction data in LLM prompts subject to PSD2 security requirements |

---

## Conflict Resolution Patterns

Cross-border AI systems inevitably encounter regulatory conflicts. These patterns provide resolution approaches.

### GDPR Right-to-Delete vs. Regulatory Retention

**Conflict:** GDPR Article 17 gives data subjects the right to erasure. Financial regulators require retention of transaction records, communications, and model decision logs for 5–7 years.

**Resolution:**
1. Identify the legal basis for retention (regulatory obligation under GDPR Article 17(3)(b))
2. Restrict access to retained data; remove it from active AI processing
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

- **Prompts containing PII**: every prompt sent to a vendor API is a data transfer; ensure the DPA and SCCs cover it
- **Training/fine-tuning data**: bulk transfers of training data are subject to all standard transfer mechanisms
- **Model outputs**: generated outputs containing PII constitute processed personal data, so transfer rules apply
- **Audit trail data**: retention of prompts/responses in logging infrastructure constitutes storage, so residency rules apply
- **Evaluation data**: test datasets containing PII must comply with transfer mechanisms

---

## Vendor Assessment Checklist

Use before contracting an external LLM API, and when selecting a cloud provider for a multi-jurisdictional AI deployment.

| Question | Acceptable Answer |
|----------|-------------------|
| Where is inference performed and data stored? | Named region(s) that comply with your residency requirements, available in every jurisdiction you need |
| Can you specify data processing region? | Yes, with a contractual commitment that data stays in that region, not just default behaviour |
| Is data retained after inference? | No, or retention terms are acceptable and documented |
| Is data used for model training? | No, contractually excluded |
| Are there sub-processors? | Fully disclosed, with their locations, and assessed |
| Is there a DPA available? | Yes, covering GDPR Article 28 and local requirements |
| Are SCCs in place for cross-border transfers? | Yes, if data crosses EU/EEA boundaries |
| What certifications does the vendor hold? | SOC 2 Type II, ISO 27001 at minimum; local certifications where required (C5 for Germany, HDS for France, IRAP for Australia) |
| Is there a breach notification procedure? | Yes, within 72 hours (GDPR-aligned) |
| Can data be encrypted with your keys? | Required for T1 (customer-managed keys); preferred otherwise; provider-managed keys acceptable for T3/T4 |
| What government access obligations apply? | Assessed: the provider's jurisdiction of incorporation and government access obligations (CLOUD Act, etc.) |
| Is there an exit path? | Data portability, migration support, deletion certification |

---

## Implementation Notes

- Start by mapping data flows for T1 systems. Extend to T2, then T3/T4 as governance matures.
- Work with legal to maintain a jurisdiction-specific requirement register. Update it quarterly via [regulatory change monitoring](regulatory-change-monitoring.md).
- Automate jurisdiction detection where possible. Know where your data is at all times, not just where you intend it to be.
- Cross-border data governance is a continuous activity, not a one-time assessment. Regulatory requirements, vendor infrastructure, and organizational operations all change.

---

## Sources

- Regulation (EU) 2022/2554 (DORA), Arts. 28, 30, 31 and 64: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- ESAs, "European Supervisory Authorities designate critical ICT third-party providers" (18 November 2025): https://www.esma.europa.eu/press-news/esma-news/european-supervisory-authorities-designate-critical-ict-third-party-providers
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
