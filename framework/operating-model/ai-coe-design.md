# AI Center of Excellence — Design and Evolution

## Overview

An AI Center of Excellence (CoE) is a transitional organizational structure that centralizes AI capability, standards, and governance expertise. It is useful in the early stages of AI adoption. It does not scale.

This document defines how to design an effective AI CoE, when to use it, and how to evolve it into a distributed AI operating model as organizational maturity increases.

---

## CoE Mandate

The AI CoE exists to do three things:

1. **Establish standards** — governance frameworks, development practices, evaluation methods, deployment patterns
2. **Build shared capability** — platforms, tools, templates, training programs
3. **Enable domain teams** — not to build AI for them, but to make them capable of building AI themselves

If the CoE becomes the team that "does AI" for the organization, it has failed. It will become a bottleneck, and shadow AI will grow around it.

---

## CoE Structure

### Core Functions

| Function | Responsibility | Headcount Guidance |
|----------|---------------|-------------------|
| AI Platform Engineering | Shared infrastructure: model serving, evaluation pipelines, monitoring, guardrails | 3–6 engineers |
| AI Governance & Risk | Risk framework, compliance mapping, validation oversight, audit coordination | 2–4 specialists |
| Prompt Engineering & LLM Ops | Prompt standards, model evaluation, vendor management, operational support | 2–4 engineers |
| AI Enablement & Training | Training programs, best practices, domain team support, community building | 1–3 specialists |

### Reporting Structure

The CoE should report to a senior leader with both technical authority and business influence:
- **Preferred:** CTO, Chief Data Officer, or Chief AI Officer
- **Acceptable:** VP Engineering, VP Data & Analytics
- **Avoid:** Reporting to a single business unit — this limits cross-organizational mandate

### Staffing Model

| Role | Profile |
|------|---------|
| CoE Lead | Senior leader with AI strategy, governance, and engineering experience |
| Platform Engineers | ML engineers with infrastructure and DevOps skills |
| AI Risk Analysts | Risk professionals with AI/ML expertise or technologists with risk management training |
| Prompt Engineers | Applied AI practitioners with evaluation and production deployment experience |
| Enablement Lead | Experienced practitioner with communication and training skills |

---

## Operating Model Maturity Stages

### Stage 1: Centralized CoE (Months 0–12)

The CoE does everything: builds use cases, defines standards, operates platforms, advises domain teams.

**Characteristics:**
- Small team (5–10 people)
- Direct involvement in every AI use case
- Establishing foundational standards and tooling
- High demand, limited capacity

**Exit criteria for Stage 1:**
- Risk framework published and adopted
- Shared platform operational
- At least 3 domain teams trained and using the platform
- Development and deployment standards established

### Stage 2: Hub-and-Spoke (Months 12–24)

The CoE retains standards and platform ownership. Domain teams start building their own AI capability with embedded AI engineers.

**Characteristics:**
- CoE focuses on platform, governance, and enablement
- Domain teams hire or upskill data scientists and ML engineers
- Domain teams build use cases using CoE standards and tooling
- CoE provides consulting and review but does not build for domain teams

**Exit criteria for Stage 2:**
- ≥ 5 domain teams independently building and deploying AI
- CoE spending < 30% of time on direct use case delivery
- Governance processes running without CoE bottleneck
- Platform self-service adoption > 70%

### Stage 3: Distributed Operating Model (Month 24+)

The CoE dissolves into permanent organizational functions. AI capability is distributed.

**Characteristics:**
- Platform team operates independently (part of Engineering/Infrastructure)
- Governance function operates independently (part of Risk/Compliance)
- Enablement function may merge with broader L&D or engineering excellence
- Domain teams are fully self-sufficient in AI development
- Standards are embedded in tooling, not enforced by a central team

---

## Anti-Patterns

| Anti-Pattern | Symptom | Remedy |
|-------------|---------|--------|
| The bottleneck CoE | All AI work queues through the CoE; domain teams wait months for capacity | Shift to enablement model; embed capability in domain teams |
| The ivory tower CoE | CoE publishes standards nobody uses because they weren't developed with practitioners | Co-create standards with domain teams; embed CoE members in domain teams periodically |
| The demo factory CoE | CoE builds impressive demos that never reach production | Focus on productionization standards; measure deployments, not demos |
| The governance-only CoE | CoE creates governance overhead without providing engineering value | Balance governance with platform and tooling that makes compliance easy |
| The permanent CoE | CoE persists as an org chart fixture long after it should have evolved | Set explicit maturity milestones and sunset plan |

---

## Success Metrics

| Metric | Stage 1 Target | Stage 2 Target | Stage 3 Target |
|--------|---------------|---------------|---------------|
| AI use cases in production | 3–5 | 10–20 | 20+ |
| Domain teams with AI capability | 1–3 | 5–10 | All relevant units |
| Time from use case approval to production | 6+ months | 3–4 months | 1–3 months |
| CoE involvement in each use case | 100% | 30–50% | < 10% (governance review only) |
| Platform self-service adoption | Establishing | 50–70% | > 90% |
| Governance compliance rate | Establishing standards | 80%+ | 95%+ |
