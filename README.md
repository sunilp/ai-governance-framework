# AI Governance Framework

**Practical governance patterns for AI systems in regulated industries**

---

## Philosophy

Governance is enablement, not gatekeeping. The goal is not to slow down AI adoption — it is to make AI adoption durable, defensible, and scalable across a regulated organization.

This framework provides opinionated, field-tested patterns for governing AI systems in financial services, healthcare, and other industries where model risk, data privacy, and regulatory compliance are non-negotiable.

## Who This Is For

- **Chief Risk Officers** who need confidence that AI systems meet regulatory expectations
- **CTOs and Engineering VPs** who need repeatable standards for AI productionization
- **AI/ML leads** who need clear guardrails without bureaucratic overhead
- **Compliance teams** who need to map AI controls to regulatory requirements

## Framework Components

### Risk Classification
Define how AI systems are tiered by risk and what governance intensity each tier requires.
- [Risk Matrix](framework/risk-classification/risk-matrix.md) — tiering criteria and decision matrix
- [Assessment Template](framework/risk-classification/assessment-template.yaml) — structured risk assessment

### Model Lifecycle
Standards and gates across the full model lifecycle — from development through production monitoring.
- [Development Standards](framework/model-lifecycle/development.md)
- [Validation Requirements](framework/model-lifecycle/validation.md)
- [Deployment Gates](framework/model-lifecycle/deployment.md)
- [Production Monitoring](framework/model-lifecycle/monitoring.md)

### Compliance Mapping
How framework controls map to specific regulatory requirements.
- [EU AI Act Mapping](framework/compliance/eu-ai-act-mapping.md)
- [Responsible AI Checklist](framework/compliance/responsible-ai-checklist.md)
- [Audit Trail Requirements](framework/compliance/audit-trail-requirements.md)

### Operating Model
Who does what, when, and how decisions escalate.
- [Roles & Responsibilities (RACI)](framework/operating-model/roles-responsibilities.md)
- [Review Cadence](framework/operating-model/review-cadence.md)
- [Escalation Paths](framework/operating-model/escalation-paths.md)

## Templates
Ready-to-use templates for immediate adoption:
- [Model Card Template](templates/model-card-template.yaml)
- [Impact Assessment Template](templates/impact-assessment-template.md)
- [Incident Report Template](templates/incident-report-template.md)

## Worked Examples
See the framework applied to real-world use cases:
- [Credit Scoring Model](examples/credit-scoring-model/) — high-risk, heavily regulated
- [Fraud Detection System](examples/fraud-detection/) — real-time, high-autonomy

## Adoption Approach

This framework is designed for phased rollout:

1. **Phase 1 (Week 1–2):** Adopt the risk classification matrix. Tier your existing AI systems.
2. **Phase 2 (Month 1):** Apply model lifecycle standards to one high-risk system as a pilot.
3. **Phase 3 (Month 2–3):** Roll out templates (model cards, impact assessments) org-wide.
4. **Phase 4 (Ongoing):** Establish the operating model — governance cadence, escalation paths, RACI.

Start where the risk is highest. Expand as the organization builds muscle memory.

## Regulatory Alignment

This framework has been designed with explicit alignment to:

| Regulation | Coverage |
|---|---|
| **EU AI Act** | High-risk system requirements (Articles 6–15), transparency obligations, conformity assessment |
| **SR 11-7 (Fed/OCC)** | Model risk management — development, validation, governance |
| **MAS FEAT** | Fairness, Ethics, Accountability, Transparency principles for AI in financial services |
| **BCBS 239** | Risk data aggregation and reporting — data lineage, quality, timeliness |
| **DORA** | Digital operational resilience — ICT risk management for AI systems |

## Contributing

Contributions are welcome. If you work in regulated industries and have governance patterns worth sharing, open a PR. Practical experience matters more than theoretical frameworks.

## License

Apache 2.0 — see [LICENSE](LICENSE).

