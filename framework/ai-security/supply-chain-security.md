# AI Supply Chain Security

## Overview

Every AI system depends on components the organization did not build: foundation models, inference frameworks, embedding models, vector databases, and evaluation tools. A vulnerability in any of these components compromises the systems built on top of them.

AI supply chain security extends traditional software supply chain practices to cover model provenance, training data risk, and the unique legal and safety considerations of AI components.

---

## Model Provenance

Before deploying any model — commercial, open-source, or community-contributed — verify its provenance.

| Check | Description | Tier Requirement |
|-------|-------------|:---:|
| Weight verification | Verify model weights match published checksums (SHA-256) from the official source | T1/T2 |
| Source authentication | Download only from official channels (vendor API, official Hugging Face org, signed releases) | All |
| Training data attestation | Review provider's training data disclosure; assess data sourcing practices | T1/T2 |
| Model card review | Verify model card exists, is complete, and matches observed behavior | All |
| Safety evaluation verification | Reproduce key safety benchmarks; compare against provider's claimed scores | T1 |
| Licensing review | Legal review of model license terms, restrictions, and obligations | All |
| Known vulnerability check | Check for disclosed vulnerabilities or security advisories | All |

### Model Card Credibility Assessment

Model cards are self-reported. Treat them as claims, not facts:
1. Are safety evaluation results reproducible with your own test data?
2. Do observed capabilities match documented capabilities?
3. Are limitations honestly disclosed, or is the card marketing material?
4. Is training data composition described with enough specificity to assess bias risk?
5. Is the card regularly updated, or was it published once and abandoned?

---

## Open-Source Model Risk

Open-source models offer control and cost advantages but shift responsibility for safety, security, and maintenance to the deployer.

| Risk Category | Description | Mitigation |
|--------------|-------------|------------|
| Licensing restrictions | Some "open" licenses restrict commercial use, derivatives, or specific use cases | Legal review before deployment; maintain license compliance register |
| Training data copyright | Model may be trained on copyrighted content; deployer may inherit liability | Review provider's copyright policy; assess litigation exposure; monitor pending cases |
| Safety evaluation gaps | Community safety claims may be overstated or untested for your domain | Run your own safety evaluations; do not rely solely on community benchmarks |
| Backdoor risk | Community-uploaded models may contain poisoned weights or hidden behaviors | Download from verified sources only; run behavioral testing before deployment |
| Maintenance risk | Project may become abandoned; no security patches or safety updates | Assess community health (contributors, commit frequency, issue responsiveness); have alternatives identified |
| Supply chain tampering | Model files modified between source and deployment | Verify checksums; use signed releases where available; store models in controlled artifact registry |

### Open-Source License Risk Matrix

| License | Commercial Use | Derivative Works | Restrictions | Risk Level |
|---------|:---:|:---:|-------------|:---:|
| Apache 2.0 | Yes | Yes | Patent grant; attribution | Low |
| MIT | Yes | Yes | Attribution | Low |
| Llama Community License | Conditional | Yes | Revenue threshold; use restrictions | Medium |
| Mistral Research License | No | Limited | Research only | High |
| CC BY-NC | No | Yes | Non-commercial only | High |
| Custom community licenses | Varies | Varies | Case-by-case legal review required | Variable |

For T1/T2 systems, only use models with Low or Medium license risk. High-risk licenses require legal sign-off and documented risk acceptance.

---

## Community Model Governance

Models from Hugging Face, GitHub, or other community platforms require additional due diligence beyond what commercial API providers absorb.

### Pre-Deployment Verification Checklist

- [ ] Model downloaded from verified organization page (not a fork or re-upload)
- [ ] Weight checksums verified against official publication
- [ ] License terms reviewed and approved by legal
- [ ] Safety evaluation suite executed (not just provider benchmarks)
- [ ] Domain-specific evaluation suite executed
- [ ] Behavioral testing for known failure modes completed
- [ ] Infrastructure sizing validated (GPU requirements, memory, latency)
- [ ] Ongoing vulnerability monitoring source identified
- [ ] Fallback model identified (if community model fails or is abandoned)
- [ ] Maintenance owner assigned internally

### Ongoing Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Community health check (contributor activity, issue resolution) | Quarterly | AI Operations |
| CVE and vulnerability scan (model, framework, dependencies) | Weekly (automated) | Security |
| License change monitoring | Quarterly | Legal |
| Safety benchmark re-evaluation | Semi-annually | AI Risk |
| Performance regression testing | Monthly | AI Operations |

---

## Dependency Management

AI systems depend on inference frameworks, libraries, and infrastructure components beyond the model itself.

| Component | Risk | Mitigation |
|-----------|------|------------|
| Inference frameworks (vLLM, TGI, Triton) | CVEs, breaking changes, performance regressions | Pin versions; test upgrades; subscribe to security advisories |
| ML frameworks (PyTorch, TensorFlow, JAX) | CVEs, API changes | Pin major versions; security scan in CI/CD |
| Embedding models | Quality degradation, version changes, licensing | Pin versions; re-evaluate on updates |
| Vector databases | Data corruption, access control bypass, performance | Standard database security practices; access auditing |
| Container images | Unpatched OS vulnerabilities, bloated attack surface | Minimal base images; weekly vulnerability scanning; rebuild on critical CVEs |
| Python packages | Dependency confusion, typosquatting, compromised packages | Use verified package sources; pin exact versions; audit new dependencies |

---

## AI Bill of Materials (AI-BOM)

Every AI system should maintain an AI Bill of Materials documenting its supply chain. This extends traditional SBOM concepts to AI-specific components.

### AI-BOM Contents

| Component | Details to Document |
|-----------|-------------------|
| Foundation model | Provider, model name, version/checkpoint, access method (API/self-hosted) |
| Model license | License type, commercial use permitted, derivative restrictions, obligations |
| Training data summary | Provider's disclosure; known data sources; opt-out compliance status |
| Safety evaluations | Provider's published evaluations + your own evaluation results |
| Known limitations | Provider-documented + internally discovered limitations |
| Embedding model | Provider, version, embedding dimensions, hosting |
| Inference framework | Name, version, deployment configuration |
| Key dependencies | Framework versions, critical libraries, container base image |
| Guardrail components | Safety classifiers, content filters, PII detectors — versions and sources |

### Maintenance

- AI-BOM updated on every model change, framework upgrade, or dependency update
- Reviewed as part of deployment gate process
- Stored alongside model card and risk assessment
- Retained per audit trail requirements

---

## Decision Framework: Open-Source vs. Commercial API

| Factor | Open-Source Advantage | Commercial API Advantage | Decision Guidance |
|--------|----------------------|-------------------------|-------------------|
| Cost at scale | Lower marginal cost after infrastructure investment | Lower upfront cost; pay-per-use | Open-source at >$10K/month API spend |
| Control | Full control over model, data, infrastructure | Limited to API parameters | Open-source when data residency is non-negotiable |
| Data residency | Complete; all processing on your infrastructure | Depends on vendor's regional endpoints | Open-source for MNPI or strict residency |
| Capability | Varies; may lag frontier models | Frontier performance; regular updates | API for state-of-the-art requirements |
| Support | Community only; no SLA | Vendor SLA; dedicated support | API for T1 systems requiring guaranteed uptime |
| Security patching | Self-managed; may lag | Vendor-managed; typically faster | API unless you have dedicated ML security team |
| Compliance | Full audit access; self-attested | Vendor certifications (SOC 2, ISO 27001) | Depends on regulatory expectations |

Use this framework during model selection; document the decision rationale in the risk assessment.
