# AI Procurement Clauses

## Purpose

Status as of November 2026. Regulatory positions change; check the sources below before relying on article references.

This is the contract clause set for any vendor that supplies an AI model or AI service: model APIs, hosted models, fine-tuning services, MCP servers and agent tools run by a vendor, and SaaS products with embedded AI. The [third-party model risk assessment](third-party-model-risk.md) decides whether a vendor is acceptable. This document sets what the contract must say before production data reaches that vendor.

## How It Fits the Workflow

- **Stage 3:** AR-004 selects the model, AR-005 assesses the vendor, AR-003 confirms data residency, and AR-007 checks that the executed contract meets this clause set and is recorded in the register of information.
- **Who:** Legal negotiates the terms with procurement. AI Risk confirms the clause set as part of the AR-005 assessment and records the fourth-party dependencies. For EU financial entities, the register of information entry is made before the contract takes effect.
- **When:** before production data is sent to the vendor, and again at renewal or on a material change to the service, the model or the sub-processors.
- **T4:** T4 systems use a vendor already on the approved list, so they rely on the contract checked when the vendor was approved.
- **What it changes:** no tier, threshold, approver, cadence or retention period. Notice periods and incident times marked "framework default" are negotiating targets; a tier approver may accept a different value through the exception process.

---

## Clause Set

"Required" means the contract must contain the clause for the systems listed. "Critical or important function" refers to DORA Art. 28(4): whether the service supports a critical or important function of an EU financial entity.

| # | Clause | What the contract says | Required for |
|---|--------|------------------------|--------------|
| 1 | Model change notice | The vendor gives written notice before changing model weights, safety tuning, content filters or default parameters for any model version the customer uses that is not pinned. Framework default: at least 30 days for planned changes, and prompt notice of urgent security or legal changes with a description of the expected effect | All tiers |
| 2 | Version pinning | The customer can call a fixed, dated model version that does not change while it is supported. T1 and T2 systems call pinned versions, not "latest" aliases. Behaviour changes are still detected by the vendor behaviour canary in [Ongoing Monitoring](third-party-model-risk.md#ongoing-monitoring) | T1-T2; T3-T4 where available |
| 3 | Deprecation notice | Minimum notice before a pinned version is retired, with a period in which old and new versions run side by side for parallel evaluation. Framework default: 6 months for T1 and T2, 3 months for T3 and T4. Notice under 3 months puts a T1 system without a validated fallback into the Critical class of the [deprecation impact classification](../llm-lifecycle/model-deprecation-governance.md#step-2-impact-classification) | All tiers |
| 4 | No training on customer data | Prompts, outputs, files, embeddings, fine-tuning data and feedback are not used to train, fine-tune or improve the vendor's models or anyone else's, and are not used for vendor human review except for abuse monitoring under clause 5. The same applies to the vendor's sub-processors. Any opt-in needs the customer's written agreement | All tiers |
| 5 | Data retention | Zero data retention: prompts and outputs are not stored after the request is processed. Where the vendor keeps data for abuse monitoring, the contract states the period, the purpose, who can access it and that it is deleted at the end. Zero data retention is one of the four safeguards for customer personal data sent to an external API ([override item 3](../risk-classification/genai-risk-matrix.md#tier-override-rules)) | All tiers sending personal or regulated data; otherwise T1-T2 |
| 6 | Data location | The regions or countries where the service is provided and where data is processed and stored, including backups, logs, abuse monitoring and support access, with advance notice of any change (DORA Art. 30(2)(b)). See [data residency](cross-border-data-governance.md#compliance-mapping) | All tiers |
| 7 | Sub-processors and fourth parties | A list of sub-processors with their function and location; prior notice of additions or replacements with a right to object (GDPR Art. 28(2)); the same obligations flowed down. The vendor discloses the AI supply chain behind the service: the underlying model provider if the vendor builds on another company's model, the hosting provider, and any third-party safety or monitoring service that sees customer data. For critical or important functions, whether subcontracting is permitted and on what conditions (DORA Art. 30(2)(a)) | All tiers |
| 8 | Data protection and security | Measures for availability, authenticity, integrity and confidentiality of data (DORA Art. 30(2)(c)); encryption in transit and at rest; tenant isolation; current certifications such as SOC 2 or ISO/IEC 27001; a signed DPA meeting GDPR Art. 28 where personal data is processed. For critical or important functions, the vendor implements and tests business contingency plans (DORA Art. 30(3)(c)) | All tiers |
| 9 | Security testing cooperation | The customer may red-team its own use of the service (SR-001) within agreed rules, and the vendor responds to reported findings. For critical or important functions, the vendor participates and cooperates in threat-led penetration testing (DORA Art. 30(3)(d)) | T1-T2; DORA where it applies |
| 10 | Incident notification | The vendor notifies the customer of security incidents, personal data breaches and AI incidents that affect the customer's service, such as a model malfunction, a safety failure or an unannounced behaviour change. Framework default: within 4 hours of the vendor becoming aware for services supporting a critical or important function, so the customer can meet the DORA initial notification time limit, and within 24 hours otherwise. A processor notifies personal data breaches without undue delay (GDPR Art. 33(2)). The vendor provides the information the customer needs for its own regulatory notifications (see IR-006) and assists at no cost or at a cost agreed in advance (DORA Art. 30(2)(f)) | All tiers |
| 11 | Audit and information rights | The vendor makes available the information needed to demonstrate compliance and allows audits and inspections by the customer or an auditor it appoints (GDPR Art. 28(3)(h)), and cooperates with competent and resolution authorities (DORA Art. 30(2)(g)). For critical or important functions: unrestricted rights of access, inspection and audit for the customer, an appointed third party and the competent authority (DORA Art. 30(3)(e)). AI-specific information on request: model documentation, evaluation and safety results, change logs, and GPAI Code of Practice status | All tiers; full rights for T1 and critical or important functions |
| 12 | EU AI Act value-chain cooperation | See [EU AI Act Value-Chain Terms](#eu-ai-act-value-chain-terms) below | Systems in scope of the EU AI Act |
| 13 | Service levels | Availability, latency, rate limits, capacity headroom and support response times (DORA Art. 30(2)(e)). For critical or important functions, precise quantitative and qualitative performance targets that allow monitoring and corrective action (DORA Art. 30(3)(a)) | T1-T2; DORA where it applies |
| 14 | Material developments | The vendor notifies developments that could materially affect its ability to provide the service (DORA Art. 30(3)(b)), including a change of control, a change to its acceptable use policy that could block the use case, and designation as a critical ICT third-party provider | T1-T2; DORA where it applies |
| 15 | Exit and transition | Termination rights with minimum notice periods (DORA Art. 30(2)(h)); return of data in an easily accessible format on termination, insolvency or discontinuation, followed by certified deletion (DORA Art. 30(2)(d)). For critical or important functions, a mandatory transition period during which the vendor keeps providing the service while the customer migrates (DORA Art. 30(3)(f)). Customer-owned artefacts are exportable: fine-tuned weights or adapters where the vendor's terms allow, embeddings, prompts and evaluation data. Supports the [exit strategy requirements](third-party-model-risk.md#exit-strategy-requirements) | All tiers; transition period for T1-T2 and critical or important functions |
| 16 | IP and liability | Ownership of outputs and of customer-funded fine-tuned artefacts; IP indemnity for outputs where available; liability allocation for harm caused by model outputs | T1-T2 |
| 17 | Training and awareness | For EU financial entities, the conditions for the vendor's participation in the customer's ICT security awareness programmes and digital operational resilience training (DORA Art. 30(2)(i)) | DORA where it applies |

### EU AI Act Value-Chain Terms

Which terms apply depends on the customer's role for the AI system, recorded at intake ([Working Out the Role](eu-ai-act-mapping.md#working-out-the-role)). High-risk duties apply from the dates in [Application Dates](eu-ai-act-mapping.md#application-dates).

| Customer's role | What the contract secures | Article |
|-----------------|---------------------------|---------|
| Provider of a high-risk AI system that uses the vendor's model, tool, service or component | A written agreement specifying the information, capabilities, technical access and other assistance the customer needs to comply as provider. This does not apply to tools or components (other than GPAI models) made publicly available under a free and open-source licence. The AI Office may recommend voluntary model terms for these contracts; check whether it has published them | 25(4) |
| Deployer of a high-risk AI system the vendor provides | Instructions for use, including how the deployer collects, stores and interprets logs (Art. 13(3)(f)); access to logs so the deployer can keep them for at least six months (Art. 26(6)); a named contact for serious incidents, which the deployer must report to the provider first (Art. 26(5)); the vendor's cooperation with its own serious incident reporting (Art. 73) and post-market monitoring (Art. 72) | 13, 26(5), 26(6), 72, 73 |
| Downstream user of a general-purpose AI model | The model documentation for downstream providers (Art. 53(1)(b)); Code of Practice signatory status; whether the model is classified as systemic-risk, and notice if that changes. See [Downstream User of General-Purpose AI Models](eu-ai-act-mapping.md#c-downstream-user-of-general-purpose-ai-models) | 53(1)(b), 55 |
| Becomes provider by modifying the system (Art. 25(1)) | The original provider's cooperation: the information, technical access and assistance the new provider needs | 25(2) |

---

## DORA Contract Requirements

For EU financial entities, every contract for an AI model API or AI service is a contract for ICT services. Art. 30 sets the minimum content. The clause numbers above map to it as follows.

| DORA | Requirement | Clause |
|------|-------------|--------|
| Art. 30(1) | Rights and obligations in writing, in one document that includes the service level agreements | Whole contract |
| Art. 30(2)(a) | Description of all functions and services; whether subcontracting is permitted for critical or important functions and on what conditions | 7 |
| Art. 30(2)(b) | Locations where services are provided and data processed and stored; advance notice of changes | 6 |
| Art. 30(2)(c) | Availability, authenticity, integrity and confidentiality of data, including personal data | 8 |
| Art. 30(2)(d) | Access, recovery and return of data on insolvency, resolution, discontinuation or termination | 15 |
| Art. 30(2)(e) | Service level descriptions | 13 |
| Art. 30(2)(f) | Assistance on ICT incidents at no cost or a cost set in advance | 10 |
| Art. 30(2)(g) | Full cooperation with competent and resolution authorities | 11 |
| Art. 30(2)(h) | Termination rights and minimum notice periods | 15 |
| Art. 30(2)(i) | Participation in security awareness and resilience training | 17 |
| Art. 30(3)(a) | Full service levels with precise performance targets (critical or important functions) | 13 |
| Art. 30(3)(b) | Notice periods and reporting obligations, including material developments | 14 |
| Art. 30(3)(c) | Business contingency plans and security measures | 8 |
| Art. 30(3)(d) | Participation in threat-led penetration testing | 9 |
| Art. 30(3)(e) | Unrestricted access, inspection and audit rights | 11 |
| Art. 30(3)(f) | Exit strategy with a mandatory adequate transition period | 15 |

Art. 28(8) also requires an exit strategy for ICT services supporting critical or important functions; see [exit strategy requirements](third-party-model-risk.md#exit-strategy-requirements).

### Register of Information

Art. 28(3) requires a register of information on all contractual arrangements for ICT services, kept at entity, sub-consolidated and consolidated level, distinguishing those that support critical or important functions. The entity reports at least yearly to its competent authority on new arrangements, makes the register available on request, and informs the authority in a timely manner of any planned arrangement for a critical or important function.

Record each AI vendor contract in the register before it takes effect (AR-007). Alongside the regulatory fields, record for AI services: the model and version, the data location from clause 6, the sub-processors and fourth-party dependencies from clause 7, the vendor's critical ICT third-party provider status, the link to the exit plan, and the system IDs from the AI inventory that use the contract.

---

## Fourth-Party Dependencies

Many AI services run on someone else's model or cloud. Map these during the AR-005 assessment and keep the map current from the sub-processor notices in clause 7:

- the foundation model provider behind the vendor's product;
- the cloud or hosting provider;
- third-party safety, monitoring or abuse-detection services that see customer data;
- for agent tools and MCP servers, the services the tool itself calls.

Two vendors that run on the same underlying model or cloud are one dependency for [concentration risk](third-party-model-risk.md#concentration-risk). APRA's letter to industry on AI asks for visibility of material third- and fourth-party AI dependencies ([regulatory hooks](third-party-model-risk.md#regulatory-hooks)).

---

## When the Vendor Will Not Agree

Large model providers often offer standard terms only. In order of preference:

1. Use an enterprise agreement, or reach the model through a cloud provider whose contract already contains the terms.
2. Narrow the use: keep personal and regulated data out, or restrict the vendor to lower tiers.
3. Apply compensating controls (PII redaction before the call, a validated fallback model, more frequent canary runs) and seek an exception through [Exceptions and Risk Acceptance](../governance-operations/governance-workflow.md#exceptions-and-risk-acceptance).

An exception cannot make a contract lawful. Where a clause is a legal requirement, such as DORA Art. 30 for an EU financial entity or GDPR Art. 28 for a processor of personal data, the vendor cannot be used for that service until the term is in place. Record any accepted gap in the AR-005 assessment.

---

## Sources

- Regulation (EU) 2022/2554 (DORA), Arts. 28 and 30: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Regulation (EU) 2016/679 (GDPR), Arts. 28 and 33: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Regulation (EU) 2024/1689 (AI Act), Arts. 13, 25, 26, 53, 72 and 73: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- APRA, Letter to industry on AI (30 April 2026): https://www.apra.gov.au/news-and-publications/apra-letter-industry-artificial-intelligence-ai
