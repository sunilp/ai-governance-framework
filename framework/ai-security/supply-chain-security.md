# AI Supply Chain Security

## Overview

Every AI system depends on components the organization did not build: foundation models, inference frameworks, embedding models, vector databases, and evaluation tools. A vulnerability in any of these components compromises the systems built on top of them.

AI supply chain security extends traditional software supply chain practices to cover model provenance, training data risk, and the unique legal and safety considerations of AI components.

In public taxonomies this is OWASP [LLM03:2025 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/), OWASP ASI04 Agentic Supply Chain Vulnerabilities for agent tools, and MITRE ATLAS AML.T0010 Supply Chain Compromise. See the [threat taxonomy mapping](adversarial-robustness.md#threat-taxonomy-mapping). Control SR-004 in the [control register](../governance-operations/control-register.md) requires the AI-BOM and provenance verification described here for systems using open-source models.

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

### Open-Source License Risk

License risk levels are set in the license matrix in [open-source-model-governance.md](../llm-lifecycle/open-source-model-governance.md#license-compatibility-matrix). Legal approves the license; AI Risk is consulted, and the CISO is consulted on security terms. For T1/T2 systems, only use models with Low or Medium license risk.

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

Self-hosted community and open-source models follow the maintenance schedule in [open-source model governance](../llm-lifecycle/open-source-model-governance.md#ongoing-maintenance): weekly CVE scans, quarterly community health and license checks, semi-annual safety re-evaluation, performance re-evaluation by tier, and the security patch SLA.

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
| Agent tools and integrations | For agentic systems: each tool or tool server the agent can call, its version, source, and the permissions granted to the agent |

### Formats

Use a machine-readable format so the AI-BOM can be generated in CI and checked at the deployment gate. Two open formats cover AI components:

| Format | AI coverage |
|--------|-------------|
| CycloneDX ML-BOM | Represents models, datasets and their dependencies alongside software components. CycloneDX v1.7 is also published as ECMA-424 (2nd edition, December 2025) |
| SPDX 3.0 AI and Dataset profiles | The AI profile's AIPackage class records model type, autonomy type, safety risk assessment, limitations and energy consumption; the Dataset profile describes datasets |

OWASP LLM03:2025 recommends a signed, up-to-date SBOM and suggests starting with OWASP CycloneDX when evaluating AI BOM options. A format does not replace the review: the contents table above sets what must be recorded.

### Maintenance

- AI-BOM updated on every model change, framework upgrade, or dependency update
- Reviewed as part of deployment gate process
- Stored alongside model card and risk assessment
- Retained per audit trail requirements

---

## Decision Framework: Open-Source vs. Commercial API

The decision framework, including security patching and support, is in [open-source model governance](../llm-lifecycle/open-source-model-governance.md#decision-framework-open-source-vs-commercial-api).

---

## Sources

- OWASP, LLM03:2025 Supply Chain: https://genai.owasp.org/llmrisk/llm032025-supply-chain/
- OWASP GenAI Security Project, OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- CycloneDX, Machine Learning Bill of Materials (ML-BOM): https://cyclonedx.org/capabilities/mlbom/
- CycloneDX v1.5 JSON reference (machine-learning-model component type): https://cyclonedx.org/docs/1.5/json/
- Ecma International, ECMA-424 CycloneDX Bill of materials specification: https://ecma-international.org/publications-and-standards/standards/ecma-424/
- SPDX 3.0.1 specification, AI profile: https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/
- SPDX 3.0.1 specification, Dataset profile: https://spdx.github.io/spdx-spec/v3.0.1/model/Dataset/Dataset/
- MITRE ATLAS data, release 2026.10: https://github.com/mitre-atlas/atlas-data/blob/main/dist/v6/ATLAS-2026.10.yaml
