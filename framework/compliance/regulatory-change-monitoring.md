# Regulatory Change Monitoring

## Overview

Status as of November 2026. Regulatory positions change; check the sources below before relying on dates.

AI regulation changes quickly. Recent changes include NIST's AI RMF (26 January 2023); the EU AI Act's entry into force (1 August 2024) and its amendment by the Digital Omnibus on AI (in force 27 July 2026); the replacement of SR 11-7 by SR 26-2 (17 April 2026); new US state AI laws; and AI or model risk guidance for financial institutions from supervisors in Singapore, the UAE, Australia and Canada. The [multi-jurisdictional guide](multi-jurisdictional-guide.md) holds the current profile for each jurisdiction.

Organizations deploying AI systems cannot treat compliance as a one-time exercise. A structured process to detect, assess, and respond to regulatory changes is essential.

---

## Horizon Scanning Process

| Activity | Frequency | Responsibility | Output |
|----------|-----------|---------------|--------|
| Monitor regulatory body publications | Weekly | Compliance / AI Risk | Regulatory change log entry |
| Track industry body guidance (OECD, FSB, BIS) | Monthly | Compliance | Briefing note if material |
| Review peer institution approaches | Quarterly | AI Risk | Competitive intelligence summary |
| Attend regulatory consultations and working groups | As published | Compliance / Legal | Feedback submissions; internal impact notes |
| Review academic and industry publications on AI regulation | Monthly | AI Risk | Trend assessment |

---

## Sources to Monitor

### By Jurisdiction

| Jurisdiction | Key Sources | Focus Areas |
|-------------|-------------|-------------|
| **EU** | AI Office (European Commission), AI Board, EDPB, EBA, ESMA, EIOPA, CEN-CENELEC JTC 21 | AI Act dates as amended by the Digital Omnibus, Commission guidelines, GPAI Code of Practice signatories, harmonised standards, DORA oversight of critical ICT third-party providers, ESA statements on AI |
| **US** | Federal Reserve, OCC, FDIC (SR 26-2 and the planned request for information on AI), SEC, FTC, NIST, DOJ AI Litigation Task Force, Commerce, state legislatures, attorneys general and the CPPA (CO, CA, TX, IL, NY) | AI guidance for GenAI and agentic AI at banks, federal preemption actions and litigation, Colorado SB 26-189 rulemaking, California ADMT and risk assessment rules, NIST AI RMF revision |
| **UK** | PRA, FCA, ICO, DSIT, AI Security Institute | SS1/23 updates for AI, FCA response to the Mills Review, AI Live Testing results, ICO guidance on automated decisions under Arts. 22A-22D, any AI bill |
| **Singapore** | MAS, IMDA, PDPC, AI Verify Foundation | MAS AI Risk Management Guidelines implementation, Third-Party Risk Management Guidelines, FEAT and Veritas, IMDA agentic AI framework versions |
| **UAE** | CBUAE, DFSA, FSRA, DIFC Commissioner of Data Protection, ADGM, Artificial Intelligence and Data Authority | CBUAE AI guidance note, DIFC Regulation 10 amendments, federal AI authority output |
| **Brazil** | Chamber of Deputies (PL 2338/2023), ANPD, Central Bank (BCB) and CMN | AI bill progress, LGPD enforcement, cloud and cyber rules |
| **Canada** | OSFI, Parliament (LEGISinfo), Office of the Privacy Commissioner, Quebec CAI | OSFI E-23 readiness, Bill C-36, provincial privacy enforcement |
| **Australia** | APRA, ASIC, OAIC, Department of Industry, Science and Resources (National AI Centre), AI Safety Institute | APRA AI supervision, CPS 230, Privacy Act automated decision duties, National AI Plan follow-up |
| **Japan** | Cabinet Office (AI Strategic Headquarters), FSA, PPC | AI Basic Plan, FSA AI Discussion Paper versions, APPI enforcement |
| **South Korea** | MSIT | AI Basic Act enforcement decree amendments, end of the fine grace period |
| **China** | CAC | AI content labelling enforcement, new AI rules |
| **India** | MeitY, RBI, Data Protection Board of India | IT Rules on synthetic content, DPDP Rules phases, RBI action on FREE-AI |
| **Global** | FSB, BCBS, IOSCO, OECD AI Policy Observatory, ISO/IEC JTC 1/SC 42 | FSB sound practices follow-up, IOSCO final AI report, standards development |

---

## Impact Assessment Protocol

When a new regulation, guidance, or enforcement action is identified:

### Step 1: Identification

| Question | Document |
|----------|----------|
| What changed? | Name, jurisdiction, date published |
| What type of change? | New legislation / amendment / guidance / enforcement action / standard |
| Effective date? | When does it take effect? Is there a transition period? |
| Mandatory or voluntary? | Binding regulation vs. guidance vs. best practice |

### Step 2: Applicability

| Question | Document |
|----------|----------|
| Does it apply to our organization? | Jurisdictional scope, sector applicability, entity size thresholds |
| Which AI systems are affected? | List by system ID and tier |
| Which teams need to be aware? | Business owners, AI teams, compliance, legal |
| Is there overlap with existing obligations? | Cross-reference with current regulatory mapping |

### Step 3: Gap Analysis

| Question | Document |
|----------|----------|
| What controls do we already have? | Map new requirements to existing framework controls |
| What's missing? | Identify gaps between new requirements and current governance |
| What's the effort to close gaps? | T-shirt size: S/M/L/XL |
| What's the risk of non-compliance? | Financial penalties, enforcement action, reputational impact |

### Step 4: Action Plan

| Element | Description |
|---------|-------------|
| Priority | Based on effective date, risk of non-compliance, enforcement likelihood |
| Owner | Named individual responsible for each action |
| Timeline | Aligned with regulatory effective date minus implementation buffer |
| Resources | Budget, headcount, external support needed |
| Dependencies | Other initiatives, vendor actions, infrastructure changes |

### Step 5: Implementation

- Update framework documents as needed (risk matrices, compliance mappings, templates)
- Update controls and procedures
- Communicate changes to affected teams
- Update training materials
- Verify implementation through testing or audit

### Step 6: Communication

- Notify AI Risk Committee at next scheduled meeting (or ad-hoc for material changes)
- Brief affected business owners
- Update regulatory alignment section of the framework README
- Include in next board report regulatory update section

---

## Integration with Review Cadence

Regulatory change monitoring is a standing agenda item at the [quarterly AI Risk Committee](../operating-model/review-cadence.md):

| Agenda Item | Content |
|------------|---------|
| Regulatory horizon update | Summary of changes identified since last meeting |
| Impact assessments completed | Results of gap analysis for new regulations |
| Action plan status | Progress on implementation of regulatory changes |
| Upcoming deadlines | Regulatory compliance deadlines in next 6 months, from [Upcoming Deadlines](#upcoming-deadlines) |
| Resource requirements | Additional resources needed for compliance |

---

## Upcoming Deadlines

Verified dates from November 2026 to the end of 2028. Control IDs are from the [control register](../governance-operations/control-register.md). Add new dates through the impact assessment protocol above.

| Date | Jurisdiction | Instrument | What applies | Framework action |
|------|-------------|------------|--------------|------------------|
| 2 December 2026 | EU | AI Act as amended by Regulation (EU) 2026/1744 | New prohibitions on AI that generates non-consensual intimate images or child sexual abuse material; Art. 50(2) marking for generative systems placed on the market before 2 August 2026 | Confirm no system can generate prohibited material; confirm machine-readable marking per [transparency-standards.md](../responsible-ai/transparency-standards.md#machine-readable-marking) |
| 10 December 2026 | Australia | Privacy Act, APP 1.7 to 1.9 | Privacy policies must cover automated decisions that use personal information | List in-scope automated decisions and update privacy policies. No control yet (gap) |
| 1 January 2027 | US (Colorado) | SB 26-189 | Developer documentation; deployer notice, adverse-outcome explanation within 30 days, data correction, human review | Human review: PM-003. Notice and explanation: No control yet (gap) |
| 1 January 2027 | US (California) | CPPA ADMT regulations | ADMT requirements apply | Identify ADMT used for significant decisions; RA-003, RA-005 |
| 1 January 2027 | US (New York) | RAISE Act as amended | Duties for large frontier developers | Collect vendor frameworks and transparency reports in AR-005 |
| 22 January 2027 | South Korea | AI Basic Act | Earliest end of MSIT's grace period of at least one year on fact-finding and fines | Confirm AI notice and domestic agent duties are met |
| 1 May 2027 | Canada | OSFI Guideline E-23 | Model risk management guideline takes effect for all FRFIs, including AI/ML models | Model inventory: RA-006, GV-006 ([AI inventory](../governance-operations/ai-inventory.md)). Risk rating via [risk-matrix.md](../risk-classification/risk-matrix.md); lifecycle evidence |
| May 2027 | India | DPDP Rules 2025 | End of the 18-month phase that began on notification (13 November 2025) | RA-005 for in-scope processing; consent and notice mapping |
| 2 August 2027 | EU | AI Act Art. 111(3) | GPAI models placed on the market before 2 August 2025 must comply | Re-check vendor GPAI evidence per [third-party-model-risk.md](third-party-model-risk.md#regulatory-hooks) |
| 7 October 2027 | Singapore | MAS Guidelines on AI Risk Management | Guidelines take effect; Sections 3-4 (oversight; risk management systems, policies and procedures) | AI inventory: RA-006, GV-006. Materiality: RA-001, RA-002. Oversight: RV-001 |
| 2 December 2027 | EU | AI Act high-risk obligations, Annex III (as amended) | High-risk obligations for Annex III systems, including credit scoring | Conformity work per [eu-ai-act-mapping.md](eu-ai-act-mapping.md) |
| 1 April 2028 | US (California) | CPPA regulations | Risk assessment attestation and summary due; first cybersecurity audit certifications (revenue over $100 million) | RA-003, RA-005 evidence |
| 2 August 2028 | EU | AI Act high-risk obligations, Annex I (as amended) | High-risk obligations for Annex I systems (products under EU harmonisation law) | Usually outside financial services; confirm scope |
| 7 October 2028 | Singapore | MAS Guidelines on AI Risk Management | Sections 5-6 (life cycle controls; capability and capacity) | DE, EV, DA and PM controls; AR-005 for third-party AI |

---

## Regulatory Change Log

Maintain a running log of all regulatory changes identified and their disposition.

| Date Identified | Regulation / Guidance | Jurisdiction | Type | Applicability | Impact (H/M/L) | Action Required | Owner | Due Date | Status |
|----------------|----------------------|-------------|------|--------------|----------------|----------------|-------|----------|--------|
| | | | | | | | | | |

### Status Values

- **Monitoring** — change identified, tracking progress (e.g., proposed legislation not yet enacted)
- **Assessing** — gap analysis in progress
- **Implementing** — changes being made to framework, controls, or procedures
- **Complete** — all actions completed; compliance verified
- **Not Applicable** — assessed and determined not to apply to our organization

---

## Implementation Notes

- Assign a named owner for regulatory change monitoring — this cannot be a shared responsibility
- Subscribe to mailing lists and RSS feeds from key regulatory bodies (automate where possible)
- Build relationships with industry working groups — early awareness of regulatory direction is valuable
- Budget for regulatory change — it is a recurring operational cost, not a one-time project

---

## Sources

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Regulation (EU) 2024/1689 (AI Act), Arts. 111 and 113: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Regulation (EU) 2026/1744 (Digital Omnibus on AI): https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Federal Reserve, SR 26-2: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
- OCC Bulletin 2026-13: https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html
- Colorado SB 26-189: https://leg.colorado.gov/bills/sb26-189
- CPPA, approved ADMT, risk assessment and cybersecurity audit regulations: https://cppa.ca.gov/announcements/2025/20250923.html
- New York S8828 (RAISE Act chapter amendment): https://www.nysenate.gov/legislation/bills/2025/S8828
- Privacy and Other Legislation Amendment Act 2024 (commencement table): https://legislation.gov.au/C2024A00128/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html
- AI Basic Act (law.go.kr): https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=282791
- MSIT press release on AI Basic Act implementation (21 January 2026): https://www.msit.go.kr/bbs/view.do?sCode=user&mId=307&mPid=208&bbsSeqNo=94&nttSeqNo=3186786
- OSFI, Guideline E-23 Model Risk Management (2027): https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/guideline-e-23-model-risk-management-2027
- PIB, DPDP Rules 2025 (14 November 2025): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014
- MAS, Guidelines on AI Risk Management for Financial Institutions: https://www.mas.gov.sg/regulation/guidelines/guidelines-on-artificial-intelligence-risk-management-for-financial-institutions
- Further sources for each jurisdiction: [multi-jurisdictional-guide.md](multi-jurisdictional-guide.md#sources)
