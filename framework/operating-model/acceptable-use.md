# Acceptable Use of AI Tools

## Purpose

This standard sets what employees and contractors may and may not do with AI tools at work: public chatbots, enterprise AI assistants, AI coding assistants, and AI features embedded in the SaaS products the organisation already uses. It also sets how unapproved AI use is detected and what happens when it is found. It is the source document for control GV-003.

Building an AI system follows the [governance workflow](../governance-operations/governance-workflow.md). This standard covers using AI tools. The line between the two matters: a person who wires an AI tool into an automated workflow that acts in production systems or sends output to customers is building an AI system, and the workflow applies.

For a T4 GenAI system, this standard is the guardrail the [GenAI risk matrix](../risk-classification/genai-risk-matrix.md#governance-requirements-by-tier-genai-specific) refers to: its users are bound by it and have attested to it, and the system's permitted data classes are set on the approved tools list.

| Item | Owner |
|---|---|
| This standard and the approved tools list | CISO, with AI Risk, Compliance, Legal and the DPO |
| Shadow AI detection | Security |
| Staff attestation and training | Head of AI, through the [AI literacy](ai-literacy.md) all-staff module (GV-002) |

---

## Scope

- **People:** all employees, contractors and third parties with access to the organisation's systems or data.
- **Tools:** any AI tool used for work, on any device and under any account, including personal accounts and free consumer versions used for a work task.

---

## Approved Tools List

Security publishes and maintains the approved tools list. Each entry states the tool and edition (enterprise or consumer), its inventory ID, the data classes it is approved for, the uses it is approved for, and any conditions (for example logging on, retention off, training on customer data contractually excluded).

A tool goes on the list only after:

1. It has an [inventory](../governance-operations/ai-inventory.md) entry (GV-006).
2. The vendor has been assessed at the depth for its tier ([assessment depth by tier](../compliance/third-party-model-risk.md#assessment-depth-by-tier); AR-005 for T1 to T3).
3. Legal and the DPO have reviewed the terms and the data processing agreement: whether the vendor trains on the organisation's data, retention, processing regions, sub-processors (including the model provider behind the tool), and notice of changes.
4. Security has reviewed it: authentication through the organisation's identity provider, admin controls, logging, data loss prevention coverage.
5. Where the organisation deploys the tool to staff, the rollout has been tiered through the workflow as an AI system. An enterprise assistant that staff can give Confidential data to will usually score High on data exposure.

Staff request a new tool through intake. Until it is approved, the answer is no.

---

## Data Rules

Data classes are those in the [residency standard](../compliance/cross-border-data-governance.md#residency-requirements-by-data-classification).

| Data | Approved tool | Unapproved or consumer tool |
|---|---|---|
| Public | Yes | Yes |
| Internal | Yes, if the tool is approved for Internal | No |
| Confidential (including source code, unpublished financials, strategy) | Only if the tool is approved for Confidential | Never |
| Personal data (customers, employees, anyone else) | Only if the tool is approved for personal data, with a DPA in place and the DPIA position confirmed by the DPO | Never |
| MNPI | Only tools approved for MNPI, which in practice means self-hosted or private deployments | Never |
| Regulated data (credit, AML, sanctions, banking secrecy) | Only if the tool is approved for it after legal review | Never |
| Credentials, secrets, private keys, access tokens | Never, in any tool | Never |

The default for an unapproved tool is Public data only. Removing a name from a document does not make it Public: anonymise or use synthetic data, or use an approved tool.

---

## What You May and May Not Do

**You may:**
- Use approved tools for drafting, summarising, research, analysis, translation and coding, within the data classes each tool is approved for.
- Use AI output as a starting point for your own work.

**You must:**
- Check output before you rely on it, send it or act on it. You are accountable for what you send, whether or not AI drafted it.
- Disclose AI use where the [transparency standards](../responsible-ai/transparency-standards.md) or the law require it, for example in customer communications.
- Report a mistake, a data exposure or a tool behaving unexpectedly as soon as you notice it ([escalation paths](escalation-paths.md)).

**You must not:**
- Put data into a tool above the class it is approved for.
- Use a personal account or a consumer edition for work data.
- Use AI output as the basis of a decision about a customer or an employee, unless that use is an approved AI system that went through the governance workflow. Regulated decisions and employment decisions are automatic T1 ([override item 1](../risk-classification/genai-risk-matrix.md#tier-override-rules)).
- Build an automation or agent on an AI tool that acts in production systems, changes records, moves money or contacts customers, outside the governance workflow.
- Install AI browser extensions, plug-ins, desktop apps or tool connectors that are not on the approved list.
- Use AI for anything on the prohibited-use list ([Step 0 screen](../risk-classification/genai-risk-matrix.md#step-0-prohibited-use-screen)), such as inferring the emotions of colleagues.
- Generate images, audio or video of real people, or text presented as written by a real person, without approval and labelling.
- Try to get around an enterprise tool's guardrails or content filters.
- Record or transcribe a meeting with an AI tool without telling the participants.

---

## AI Coding Assistants

Coding assistants see source code and often configuration, so they get their own rules. They apply to chat assistants, code completion and agentic coding tools that edit files or run commands.

| Rule | Requirement |
|---|---|
| Approved assistants only | Enterprise edition, connected to the organisation's identity provider, with retention and training on the organisation's code switched off contractually and in settings. Repositories the assistant may read are set by admins |
| A human reviews every change | AI-generated code goes through normal code review before merge. The author is accountable for it as if they wrote it. An agentic tool may open a pull request; it never merges to a protected branch or deploys |
| Secret scanning | Pre-commit and CI secret scanning on every repository. Secret files (environment files, key stores) are excluded from the assistant's context. Secrets are never pasted into a prompt |
| Licence scanning | Software composition analysis and licence scanning on all code, AI-generated or not. Turn on the assistant's public-code matching filter or reference tracking where it has one. Code that matches open-source under a licence Legal has not approved is removed or licensed ([open-source licensing](../llm-lifecycle/open-source-model-governance.md)) |
| No customer data in prompts | No production data, customer data or personal data in prompts, test fixtures or logs sent to an assistant unless the assistant is approved for that class. Use synthetic test data |
| Provenance | Mark AI-assisted changes, for example with a commit trailer or pull request label naming the tool, so they can be found later if a tool or model is found to have a defect |
| Dependencies | Check that every package the assistant suggests exists, is the intended package and passes the usual dependency checks before installing it. Assistants can suggest package names that do not exist, which attackers can then register |
| Security testing | AI-generated code goes through the same static analysis, dependency scanning and, for T1 and T2 systems, the Stage 6 security review as any other code |
| Agentic coding tools | Run in a sandbox or development environment with no production credentials, a command allowlist and restricted network egress. A tool that runs commands or changes systems is an agentic AI system: register it and tier it through the workflow ([override item 6](../risk-classification/genai-risk-matrix.md#tier-override-rules) makes it at least T2) |
| Tool connectors | Plug-ins, extensions and tool servers that give an assistant access to other systems come from the approved list only |

---

## AI Features Embedded in SaaS

Vendors add AI features to products the organisation already uses, often switched on by default in a release. Treat each one as vendor AI:

1. **Default off.** New AI features stay disabled in the tenant until steps 2 to 4 are done. Application owners watch release notes and admin consoles for new features; the SaaS admin console is also a reconciliation source for GV-006.
2. **Inventory entry.** Register the feature if it meets the [material AI feature criteria](../governance-operations/ai-inventory.md#material-ai-features-in-bought-products).
3. **Third-party assessment.** Assess the vendor's AI feature at the depth for its tier ([assessment depth by tier](../compliance/third-party-model-risk.md#assessment-depth-by-tier)). The model provider behind the feature is a sub-processor and a fourth-party dependency; record it.
4. **Terms and DPA review.** Legal and the DPO confirm whether the vendor uses the organisation's data to train or improve models, retention, processing regions, sub-processors, whether the feature can be disabled per user or group, and how the vendor gives notice of new AI features and model changes.
5. **Workflow where it applies.** A feature that makes or influences a regulated or employment decision, reaches customers, or takes actions in other systems goes through the governance workflow and the override list like any other AI system.

---

## Shadow AI Detection

Security runs detection continuously and reports monthly. Sources:

- Proxy, secure web gateway, CASB and DNS logs for traffic to AI services.
- Endpoint management for desktop AI apps and browser extensions.
- SaaS admin consoles and OAuth grants for third-party apps with AI features that have access to mail, files or chat.
- Data loss prevention alerts on uploads to AI services.
- Expense claims and corporate card spend on AI subscriptions.
- Code scanning for AI service API keys and calls to AI SDKs.

| Finding | Response |
|---|---|
| Unapproved tool, no sensitive data involved | Contact the user, point to the approved alternative, block the tool where an approved alternative exists |
| A real business need with no approved tool | Route to intake; block or allow with conditions while it is assessed |
| Confidential data, personal data, MNPI or regulated data sent to an unapproved tool | Raise an incident and assess severity ([severity classification](escalation-paths.md#severity-classification)); involve the DPO for personal data; request deletion from the vendor where possible |
| An automation or agent built on an unapproved tool | Stop it, register it, and follow [Retroactive Governance](../governance-operations/governance-workflow.md#retroactive-governance) if it must keep running |

### Amnesty route

People use unapproved tools because they help. Finding that use matters more than punishing it. Framework default:

- When this standard is first published, run an amnesty window (for example 90 days) for staff to declare AI tools they use and anything they have built on them.
- After that, a standing self-report route stays open. Use declared before it is detected is not treated as a breach, provided the person cooperates with registration and any data clean-up.
- Amnesty does not cover deliberate exfiltration, use after a specific instruction to stop, or repeat breaches.

---

## Consequences

Breaches are handled under the organisation's disciplinary policy, in proportion to intent and impact. A first, unintentional breach with no sensitive data usually means coaching and a block. Deliberate or repeated breaches, or breaches that expose customer data or MNPI, are disciplinary matters and may trigger regulatory notification duties, for example for a personal data breach.

---

## Review and Evidence (GV-003)

The CISO reviews this standard annually with AI Risk, Compliance, Legal and the DPO. The approved tools list is updated whenever a tool is added, changed or withdrawn. Staff attest to the standard on joining and annually as part of the all-staff literacy module.

| Evidence | Held by |
|---|---|
| Approved standard with its review date | CISO |
| Approved tools list with inventory ID and permitted data classes for each tool | Security |
| Staff attestation records | HR or Learning and Development |
| Monthly shadow AI detection reports, with the outcome of each finding | Security |
| Incidents raised from detection findings | AI Operations or Security, per [escalation paths](escalation-paths.md) |
