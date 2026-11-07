# Third-Party Model Risk Assessment

## Overview

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

When an organization uses a foundation model developed by an external provider (OpenAI, Anthropic, Google, Meta, Mistral, Cohere, etc.), it assumes risks it cannot fully control. The model's behavior, safety properties, training data, and operational characteristics are determined by the provider.

Third-party model risk management ensures that the organization understands, monitors, and mitigates these risks throughout the relationship lifecycle.

The contract terms that back these controls are in [AI procurement clauses](ai-procurement-clauses.md): model change and deprecation notice, version pinning, no training on customer data, retention, data location, sub-processors, incident notification, audit rights, EU AI Act value-chain cooperation and exit. AR-007 checks the executed contract against that clause set.

---

## Risk Categories

### 1. Model Behavior Risk

| Risk | Description | Likelihood |
|------|-------------|------------|
| Unannounced behavior changes | Provider updates model weights or safety tuning without notice; outputs change | High: vendors routinely update models |
| Model deprecation | Provider retires a model version; forces migration | Medium: deprecation cycles vary |
| Capability regression | Model update degrades performance on your specific use case | Medium: general improvements may harm niche performance |
| Safety alignment changes | Provider changes content policy; model refuses valid enterprise queries | Medium |
| Benchmark gaming | Model optimized for public benchmarks but underperforms on real tasks | Low-Medium |

**Controls:**
- Run the vendor behaviour canary (see [Ongoing Monitoring](#ongoing-monitoring)) and the production evaluation in [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md#production-evaluation), not just onboarding evaluation
- Monitor for output distribution changes daily
- Maintain a fixed evaluation dataset; alert on score changes
- Subscribe to provider changelog and API announcements
- Maintain a validated fallback model (T1/T2)

### 2. Data Privacy and Security Risk

| Risk | Description |
|------|-------------|
| Data retention | Provider retains prompts or responses beyond agreed terms |
| Training data usage | Provider uses your data to improve models (despite contractual exclusion) |
| Data breach | Provider suffers a breach exposing customer data |
| Sub-processor exposure | Provider's sub-processors access your data |
| Cross-tenant leakage | In multi-tenant inference, data leaks between tenants |

**Controls:**
- DPA with explicit terms on retention, training data exclusion, and breach notification
- Regular compliance audits of provider (or reliance on SOC 2 / ISO 27001)
- PII redaction before API calls where feasible
- Encryption of data in transit (TLS 1.2+) and at rest
- Contractual right to audit or evidence of audit

### 3. Operational and Availability Risk

| Risk | Description |
|------|-------------|
| Service outage | Provider API unavailable |
| Rate limiting | Provider throttles your requests during peak demand |
| Latency degradation | Provider performance degrades under load |
| API breaking changes | Provider changes API contract |
| Geographic availability | Provider's regional endpoints don't cover your required jurisdictions |

**Controls:**
- SLA with defined uptime commitment, latency guarantees, and support response times
- Fallback model or graceful degradation for critical use cases
- Rate limit headroom: negotiate limits above expected peak
- API versioning: pin to specific API versions; test before upgrading
- Multi-region deployment where required

### 4. Vendor Viability Risk

| Risk | Description |
|------|-------------|
| Financial instability | Provider runs out of funding or pivots business model |
| Acquisition | Provider is acquired; terms, pricing, or product direction changes |
| Pricing changes | Provider increases prices significantly |
| Strategic misalignment | Provider's product direction diverges from your needs |

**Controls:**
- Vendor financial assessment (annually for T1/T2 dependencies)
- Contractual pricing commitments for defined periods
- Exit strategy documented: alternative providers identified, migration effort estimated
- Avoid single-vendor dependency for critical capabilities

### 5. Legal and Regulatory Risk

| Risk | Description |
|------|-------------|
| IP and copyright | Model outputs may infringe third-party copyright (trained on copyrighted data) |
| Liability | Who is liable when model outputs cause harm? |
| Regulatory non-compliance | Provider's practices don't meet your regulatory obligations |
| Jurisdictional conflict | Provider subject to laws that conflict with your regulatory requirements |
| EU AI Act compliance | Provider doesn't meet GPAI obligations (Articles 53–55) |

**Controls:**
- Legal review of provider terms and liability allocation
- IP indemnification clause in contract (if available)
- Regulatory compliance attestation from provider
- EU AI Act compliance verification for GPAI model obligations
- Documented legal basis for cross-border data transfers

---

## Regulatory Hooks

Regulations that set expectations for third-party models. Sources are listed at the end of this document.

| Regime | Who it binds | What it expects for third-party models | Framework coverage |
|--------|-------------|----------------------------------------|--------------------|
| **SR 26-2** (Federal Reserve, with OCC Bulletin 2026-13 and FDIC FIL-15-2026; issued 17 April 2026; replaced SR 11-7) | US banking organisations; most relevant above $30 billion in total assets | Vendor models stay under model risk management even when code, data or methodology are proprietary: understand the vendor model (conceptual soundness, design, development data, performance), validate it internally or through outside parties, run ongoing monitoring and outcome analysis, and document customisations. Covers traditional and non-generative AI models only. Generative and agentic AI are out of scope | AR-004, AR-005, [validation.md](../model-lifecycle/validation.md), [Ongoing Monitoring](#ongoing-monitoring). For foundation models, the controls in this document apply on their own until the agencies issue AI guidance; their planned request for information on AI had not been issued by November 2026 |
| **DORA** (Regulation (EU) 2022/2554, applies from 17 January 2025), Arts. 28-30 | EU financial entities | Keep a register of information on every ICT services contract, marking those that support critical or important functions (Art. 28(3)). Before contracting, assess whether the service supports a critical or important function, identify risks including concentration, and do due diligence (Arts. 28(4), 29). Every contract must state where the service is provided and where data is processed and stored (Art. 30(2)). For critical or important functions, add full service levels, notice duties, business contingency and security, participation in threat-led penetration testing, unrestricted access and audit rights, and exit terms (Art. 30(3)), with an exit strategy in place (Art. 28(8)). The firm stays fully responsible for compliance (Art. 28(1)(a)) | AR-005, AR-003, [Exit Strategy Requirements](#exit-strategy-requirements), [Concentration Risk](#concentration-risk). Art. 30 terms and the register of information entry: AR-007 and [DORA contract requirements](ai-procurement-clauses.md#dora-contract-requirements) |
| **DORA oversight of critical ICT third-party providers** (Art. 31 onwards) | The ESAs and the providers they designate | The ESAs, not the firm, designate critical ICT third-party providers (CTPPs), which are then overseen by a Lead Overseer. The first list (18 November 2025) named 19 providers, including AWS EMEA, Google Cloud EMEA, Microsoft Ireland Operations, IBM and Oracle Nederland. Designation does not reduce the firm's own Art. 28-30 duties | Record the provider's CTPP status in the AR-005 assessment and in [Concentration Risk](#concentration-risk) monitoring |
| **EU AI Act GPAI obligations and the GPAI Code of Practice** | Providers of general-purpose AI models (Arts. 53-55) | Providers must give downstream providers documentation on the model's capabilities and limitations (Art. 53(1)(b)). They may rely on a code of practice to show compliance; those that do not must show other adequate means (Art. 53(4)). The Commission confirmed the GPAI Code of Practice (published 10 July 2025) as adequate on 1 August 2025. Signatories on the Commission's list (updated 7 October 2026) include Amazon, Anthropic, Cohere, Google, IBM, Microsoft, Mistral AI and OpenAI; xAI signed the Safety and Security chapter only; Meta did not sign. Models placed on the market before 2 August 2025 have until 2 August 2027 | Ask for signatory status and the Art. 53(1)(b) documentation during AR-004 and AR-005, and record both in the model card (DE-001). Signatory status is evidence, not proof of compliance |
| **MAS Guidelines on AI Risk Management for Financial Institutions** (issued 7 October 2026; take effect 7 October 2027, life cycle controls by 7 October 2028) | Financial institutions in Singapore, in proportion to the materiality of their AI risk | Onboarding, development and deployment controls for third-party AI must be adequate for the risk materiality of the use case (para. 5.10). The guidelines also expect an inventory of AI use cases, systems or models (para. 4.5) and a risk materiality assessment method (para. 4.10) | AR-004, AR-005, [risk-matrix.md](../risk-classification/risk-matrix.md). AI inventory: RA-006, GV-006 ([AI inventory](../governance-operations/ai-inventory.md)) |
| **APRA CPS 230 Operational Risk Management** (in force since 1 July 2025; remade version from 1 July 2026) and APRA's letter to industry on AI (30 April 2026) | APRA-regulated entities in Australia | In the 2025 version, material service providers are those the entity relies on for a critical operation or that expose it to material operational risk; core technology services count unless the entity justifies otherwise. Material arrangements need a formal legally binding agreement, and APRA must be notified within 20 business days of entering into or materially changing one. Pre-existing contracts were covered from the earlier of renewal or 1 July 2026. APRA's AI letter asks for visibility of the AI supply chain, including material third- and fourth-party dependencies | AR-005, [Exit Strategy Requirements](#exit-strategy-requirements), [Concentration Risk](#concentration-risk). Fourth-party dependencies: AR-007 and [fourth-party dependencies](ai-procurement-clauses.md#fourth-party-dependencies) |

---

## Vendor Assessment Process

### Initial Assessment

| Phase | Activities |
|-------|-----------|
| Due diligence | Security questionnaire, financial review, reference checks |
| Technical evaluation | Domain-specific eval suite, safety testing, latency testing |
| Legal review | DPA, terms of service, liability, IP indemnification; contract checked against the [AI procurement clauses](ai-procurement-clauses.md#clause-set) (AR-007) |
| Compliance review | Data residency, regulatory alignment, certification verification |
| Architecture review | Integration design, fallback architecture, monitoring plan |
| Risk acceptance | Residual risks documented and accepted by appropriate authority |

### Assessment Depth by Tier

| Tier | Assessment Depth |
|------|-----------------|
| T1 | Full assessment: all phases, CISO + CRO + Legal sign-off |
| T2 | Standard assessment: all phases, Head of AI + Security sign-off |
| T3 | Simplified assessment: technical eval + security checklist + DPA |
| T4 | No separate assessment: T4 systems use an already-approved vendor (control AR-005 applies to T1 to T3) |

---

## Ongoing Monitoring

| Activity | Frequency | Responsibility |
|----------|-----------|---------------|
| Vendor behaviour canary: a fixed domain eval set run to detect silent vendor model changes (see [evaluation-governance.md](../llm-lifecycle/evaluation-governance.md#production-evaluation)) | Daily (T1), Weekly (T2), Monthly (T3/T4) | AI Operations |
| Provider changelog review | Weekly | AI Operations |
| Output distribution monitoring | Continuous | Automated monitoring |
| SLA compliance tracking | Monthly | Vendor Management |
| Financial health review | Annually | Vendor Management |
| DPA and contract review | Annually or on material change | Legal |
| Security certification review | Annually | Information Security |
| Regulatory compliance review | Annually or on regulatory change | Compliance |

---

## Exit Strategy Requirements

For T1 and T2 use cases, a documented exit strategy is mandatory:

| Component | Description |
|-----------|-------------|
| Alternative providers | At least one validated alternative model identified |
| Migration effort | Estimated effort to switch (prompts, evaluation, integration) |
| Performance delta | Documented performance difference between primary and fallback |
| Data portability | Confirm that no data is locked in the provider's platform |
| Contractual exit | Termination terms reviewed; notice periods documented |
| Timeline | Maximum switchover timeline defined |

### Fallback Architecture

```
Primary path:
  Application → Provider A API → Response

Fallback path (activated on Provider A failure or exit):
  Application → Provider B API (pre-validated) → Response
  or
  Application → Self-hosted model (pre-deployed) → Response
```

Fallback must be tested quarterly for T1 use cases.

---

## Concentration Risk

Monitor aggregate dependency on any single provider:

| Metric | Threshold | Action |
|--------|-----------|--------|
| % of GenAI use cases on single provider | > 70% | Review diversification strategy |
| % of T1 use cases on single provider | > 50% | Mandatory fallback validation |
| Annual spend with single provider | > $500K | Senior management review of concentration |
| Provider as single point of failure | Any critical path | Mandatory fallback architecture |

---

## Sources

- Federal Reserve, SR 26-2 Revised Guidance on Model Risk Management (17 April 2026), Section VII: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
- OCC Bulletin 2026-13: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html
- FDIC FIL-15-2026: https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance
- Regulation (EU) 2022/2554 (DORA), Arts. 28-31: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- ESAs, "European Supervisory Authorities designate critical ICT third-party providers" (18 November 2025): https://www.esma.europa.eu/press-news/esma-news/european-supervisory-authorities-designate-critical-ict-third-party-providers
- Regulation (EU) 2024/1689 (AI Act), Arts. 53 and 111(3): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European Commission, Signatories of the General-Purpose AI Code of Practice: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
- European Commission, opinion on the assessment of the GPAI Code of Practice (1 August 2025): https://digital-strategy.ec.europa.eu/en/library/commission-opinion-assessment-general-purpose-ai-code-practice
- MAS, Guidelines on AI Risk Management for Financial Institutions: https://www.mas.gov.sg/regulation/guidelines/guidelines-on-artificial-intelligence-risk-management-for-financial-institutions
- APRA, CPS 230 (2025 version): https://handbook.apra.gov.au/standard/cps-230-superseded
- APRA, Letter to industry on AI (30 April 2026): https://www.apra.gov.au/news-and-publications/apra-letter-industry-artificial-intelligence-ai
