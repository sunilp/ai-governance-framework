# Multi-Jurisdictional AI Governance Guide

## Overview

Organizations operating AI systems across multiple jurisdictions face a patchwork of regulations, guidelines, and enforcement regimes. This guide provides a practical reference for understanding what each jurisdiction requires, how this framework satisfies those requirements, and what additional controls are needed locally.

For data-specific cross-border considerations, see [cross-border-data-governance.md](cross-border-data-governance.md). This document covers the broader regulatory landscape.

---

## Jurisdictional Profiles

### European Union

| Aspect | Detail |
|--------|--------|
| **Primary regulation** | EU AI Act (Regulation 2024/1689) |
| **Status** | Prohibited practices in force (Feb 2025); GPAI obligations in force (Aug 2025); full enforcement Aug 2026 |
| **Key requirements** | Risk-based classification (prohibited, high-risk, limited, minimal); GPAI model obligations; transparency for AI-generated content; conformity assessment for high-risk systems |
| **Framework coverage** | [EU AI Act Mapping](eu-ai-act-mapping.md), [EU AI Act GenAI Mapping](eu-ai-act-genai-mapping.md) — detailed article-level mapping |
| **Local gaps** | Harmonized standards from CEN/CENELEC (still in development); sector-specific codes of practice |
| **Financial services overlay** | EBA/ESMA/EIOPA AI guidance; DORA (ICT risk); MiFID II (investment communications) |

### United States

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | NIST AI RMF (voluntary); sector-specific guidance (OCC, SEC, FTC); state laws |
| **Status** | No comprehensive federal AI law; state laws active (CO AI Act effective Feb 2026 with enforcement from Feb 2027; verify CA/IL/TX AI law status as these evolve rapidly) |
| **Key requirements** | NIST AI RMF (Govern, Map, Measure, Manage); SR 11-7 model risk management; SEC AI risk disclosure; FTC AI enforcement (unfair/deceptive practices) |
| **Framework coverage** | [NIST AI RMF Mapping](nist-ai-rmf-mapping.md); SR 11-7 alignment throughout lifecycle standards |
| **Local gaps** | State-level compliance varies; Colorado AI Act requires impact assessments for "high-risk" AI; California AI transparency rules |
| **Financial services overlay** | OCC SR 11-7; Fed supervisory guidance on AI/ML; SEC AI risk disclosure expectations |

### Singapore

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | MAS FEAT Principles; Model AI Governance Framework (2nd Edition); AI Verify toolkit |
| **Status** | Voluntary/guidance-based; MAS FEAT principles expected (not formally mandated by regulation, but MAS-supervised institutions are expected to adopt them) |
| **Key requirements** | Fairness, Ethics, Accountability, Transparency (FEAT); model risk management; explainability for customer-affecting decisions |
| **Framework coverage** | FEAT principles mapped to responsible-ai/ section; risk classification aligns with MAS model risk expectations |
| **Local gaps** | AI Verify self-assessment toolkit — consider completing for Singapore-deployed systems |
| **Financial services overlay** | MAS Technology Risk Management Guidelines; Notice on Outsourcing; Board and senior management responsibility for AI |

### United Arab Emirates

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | ADGM data protection regulations; DIFC Data Protection Law; UAE National AI Strategy |
| **Status** | Active; evolving rapidly |
| **Key requirements** | Data protection in free zones (ADGM/DIFC); sector-specific requirements; onshore processing for certain government and financial data |
| **Framework coverage** | Risk classification and lifecycle standards align with UAE expectations; data residency covered in [cross-border-data-governance.md](cross-border-data-governance.md) |
| **Local gaps** | ADGM/DIFC-specific data protection registration; UAE-specific AI ethics guidelines |
| **Financial services overlay** | CBUAE regulations; DFSA/FSRA expectations for technology risk |

### Brazil

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | LGPD (Lei Geral de Protecao de Dados); AI Bill (PL 2338/2023 — approved by Senate Dec 2024, advancing in Chamber of Deputies) |
| **Status** | LGPD in force; AI Bill progressing — verify current legislative status before relying on specific provisions |
| **Key requirements** | LGPD: consent/legal basis for AI processing; data subject rights; DPIA for high-risk processing. AI Bill (proposed): risk classification, impact assessments, transparency, human oversight |
| **Framework coverage** | LGPD requirements covered by GDPR-aligned controls; risk classification aligns with proposed AI Bill categories |
| **Local gaps** | Monitor AI Bill progress; prepare for impact assessment requirements when enacted |
| **Financial services overlay** | Central Bank Resolution 4,893 (cloud computing); Central Bank AI guidance |

### Canada

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | PIPEDA; provincial privacy laws (Quebec Law 25, Alberta/BC PIPA); AIDA (proposed) |
| **Status** | PIPEDA and provincial laws in force; AIDA (part of Bill C-27) died on the order paper when Parliament was prorogued Jan 2025 — monitor for reintroduction |
| **Key requirements** | PIPEDA: consent for personal data processing; accountability principle; transparency. Quebec Law 25: automated decision-making transparency; DPIA for high-risk AI |
| **Framework coverage** | Risk classification and transparency standards align with Canadian expectations |
| **Local gaps** | Quebec Law 25 compliance for systems affecting Quebec residents; AIDA readiness (if enacted) |
| **Financial services overlay** | OSFI Guideline B-13 (Technology and Cyber Risk); OSFI model risk management expectations |

### Australia

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | Privacy Act 1988; Voluntary AI Ethics Framework; sector-specific prudential standards |
| **Status** | Voluntary AI governance; mandatory privacy obligations; privacy reform anticipated |
| **Key requirements** | Privacy Act APP 8 (cross-border disclosure); Voluntary AI Ethics Principles (8 principles); APRA CPS 234 (information security) |
| **Framework coverage** | Risk classification and responsible AI standards align with AI Ethics Principles; privacy controls align with Privacy Act |
| **Local gaps** | APRA CPS 234 compliance for AI systems in financial services; monitor Privacy Act reform |
| **Financial services overlay** | APRA Prudential Standard CPS 234; APRA AI/ML risk expectations; ASIC regulatory guidance on AI in financial advice |

### Japan

| Aspect | Detail |
|--------|--------|
| **Primary frameworks** | APPI (Act on Protection of Personal Information); Social Principles of Human-centric AI; sector guidelines |
| **Status** | APPI in force; Social Principles (voluntary); sector guidelines evolving |
| **Key requirements** | APPI: consent for personal data processing; cross-border transfer rules; data breach notification. Social Principles: human-centric, fair, transparent, accountable |
| **Framework coverage** | EU adequacy decision simplifies GDPR-Japan transfers; risk classification aligns with Social Principles |
| **Local gaps** | Sector-specific guidelines (FSA for financial services); APPI amendments monitoring |
| **Financial services overlay** | FSA guidelines on AI in financial services; JFSA expectations for model risk management |

---

## Decision Matrix

"If you operate in these jurisdictions, here is what you need beyond the base framework."

| Operating Jurisdictions | Additional Requirements |
|------------------------|------------------------|
| EU only | Base framework sufficient. Ensure EU AI Act compliance timeline adherence. |
| EU + US | Add [NIST AI RMF mapping](nist-ai-rmf-mapping.md). Monitor state AI laws (CO, CA, IL). Comply with sector regulators (OCC, SEC). |
| EU + Singapore | Complete MAS FEAT self-assessment. Consider AI Verify toolkit. Add MAS Technology Risk Management compliance. |
| EU + UAE | Assess ADGM/DIFC data protection registration. Confirm onshore processing for restricted data. |
| EU + Brazil | Monitor AI Bill progress. Ensure LGPD consent mechanisms. Add Central Bank cloud compliance. |
| EU + Canada | Comply with PIPEDA/provincial laws. Quebec Law 25 impact assessment for Quebec-affecting systems. Monitor AIDA. |
| EU + Japan | Leverage EU adequacy decision for data transfers. Add FSA-specific requirements for financial services. |
| Global (4+ jurisdictions) | Implement [regulatory change monitoring](regulatory-change-monitoring.md). Appoint jurisdictional compliance leads. Use [cross-border data governance](cross-border-data-governance.md) for data flow management. Apply strictest standard as default; document exceptions. |

---

## Regulatory Conflict Resolution

When regulations from different jurisdictions conflict:

| Principle | Application |
|-----------|-------------|
| **Apply the strictest standard** | Unless doing so creates a direct conflict with another jurisdiction's mandatory requirement |
| **Document the conflict** | Record the conflicting requirements, analysis, and chosen resolution |
| **Seek legal guidance** | Regulatory conflicts require legal analysis — do not resolve based on technical judgment alone |
| **Implement jurisdiction-aware controls** | Where standards differ, implement controls that detect user/data jurisdiction and apply appropriate rules |
| **Engage regulators** | For genuine conflicts with no clear resolution, engage with the relevant regulators (after legal counsel) |

Common conflict patterns and resolutions are documented in [cross-border-data-governance.md](cross-border-data-governance.md).

---

## Implementation Notes

- No organization needs to comply with all 8 jurisdictions simultaneously. Start with your primary operating jurisdictions.
- The base framework (designed for EU + UK + US financial services) covers approximately 80% of requirements across all listed jurisdictions.
- Regulatory landscape is evolving rapidly — review this guide quarterly against [regulatory change monitoring](regulatory-change-monitoring.md) outputs.
- Engage local legal counsel in each operating jurisdiction — this guide provides governance direction, not legal advice.
