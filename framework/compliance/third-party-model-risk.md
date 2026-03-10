# Third-Party Model Risk Assessment

## Overview

When an organization uses a foundation model developed by an external provider (OpenAI, Anthropic, Google, Meta, Mistral, Cohere, etc.), it assumes risks it cannot fully control. The model's behavior, safety properties, training data, and operational characteristics are determined by the provider.

Third-party model risk management ensures that the organization understands, monitors, and mitigates these risks throughout the relationship lifecycle.

---

## Risk Categories

### 1. Model Behavior Risk

| Risk | Description | Likelihood |
|------|-------------|------------|
| Unannounced behavior changes | Provider updates model weights or safety tuning without notice; outputs change | High — vendors routinely update models |
| Model deprecation | Provider retires a model version; forces migration | Medium — deprecation cycles vary |
| Capability regression | Model update degrades performance on your specific use case | Medium — general improvements may harm niche performance |
| Safety alignment changes | Provider changes content policy; model refuses valid enterprise queries | Medium |
| Benchmark gaming | Model optimized for public benchmarks but underperforms on real tasks | Low-Medium |

**Controls:**
- Run your domain-specific evaluation suite continuously (not just at onboarding)
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

## Vendor Assessment Process

### Initial Assessment

| Phase | Activities |
|-------|-----------|
| Due diligence | Security questionnaire, financial review, reference checks |
| Technical evaluation | Domain-specific eval suite, safety testing, latency testing |
| Legal review | DPA, terms of service, liability, IP indemnification |
| Compliance review | Data residency, regulatory alignment, certification verification |
| Architecture review | Integration design, fallback architecture, monitoring plan |
| Risk acceptance | Residual risks documented and accepted by appropriate authority |

### Assessment Depth by Tier

| Tier | Assessment Depth |
|------|-----------------|
| T1 | Full assessment: all phases, CISO + CRO + Legal sign-off |
| T2 | Standard assessment: all phases, Head of AI + Security sign-off |
| T3 | Simplified assessment: technical eval + security checklist + DPA |
| T4 | Minimal: security checklist + acceptable use policy compliance |

---

## Ongoing Monitoring

| Activity | Frequency | Responsibility |
|----------|-----------|---------------|
| Domain eval suite execution | Daily (T1), Weekly (T2), Monthly (T3/T4) | AI Operations |
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
