# Reference Implementations

**Purpose:** Runnable patterns that turn the [control register](../framework/governance-operations/control-register.md) into automatic evidence collection and deployment gates. They are starting points to adapt to your tooling, not products. Each one reads the framework's machine-readable files ([`controls/`](../controls/), [`policy/`](../policy/)), so a change to a control or a threshold reaches the gate without a code change.

| Pattern | What it is for | Controls it evidences or enforces |
|---|---|---|
| [Governance gate](#governance-gate) ([`governance-gate/`](governance-gate/)) | A GitHub Action and Python script that a system's repository runs before deployment. Blocks the release when evidence is missing, an evaluation misses its threshold, or an exception is invalid | Produces DA-001 (automated evidence checklist) and DA-003 evidence (`gate-result.json`). Checks evidence for every applicable control in stages 2 to 7 and the pre-go-live controls of stage 8. Re-tests EV-001, EV-002, EV-004, EV-005, EV-008, EV-009, SR-001 and SR-002 from the eval report, and exceptions against GV-004 rules |
| [GitHub features as evidence](#github-features-as-evidence) | Branch protection, CODEOWNERS, environments and artifacts set up so the platform records the approvals | DE-002, DE-003, DA-002, EV-001, EV-002 |
| [Ticketing workflow](ticketing-workflow.md) | Jira or ServiceNow states, required attachments and transition rules that mirror the governance workflow | RA-004, DA-001, DA-002, GV-004, RV-003 |
| [Model registry tagging](model-registry.md) | Tags on MLflow or Vertex AI model versions that tie a deployable artifact to its tier, gate result and evidence pack | DE-001, DA-003, RV-003, DR-003 |
| [Audit logging with OpenTelemetry](audit-logging-otel.md) | Mapping of the per-request and agent action audit records to the OpenTelemetry GenAI semantic conventions | PM-007; supports PM-001 and incident reconstruction for IR-004 |

---

## Governance Gate

The gate runs in the system's pipeline before deployment. It reads `governance.yaml` from the system's repository, works out which controls apply, and fails the job unless each one has evidence or a valid exception and the evaluation results pass under the [statistical pass rule](../framework/llm-lifecycle/evaluation-governance.md#statistical-pass-rule).

Files: [`gate.py`](governance-gate/gate.py) (Python 3.10 or later, PyYAML only, no network), [`action.yml`](governance-gate/action.yml) (composite action), [`governance.template.yaml`](governance-gate/governance.template.yaml), [`tests/`](governance-gate/tests/test_gate.py). Worked example: [the customer service chatbot's governance.yaml](../examples/customer-service-chatbot/governance.yaml) and its [evidence set](../examples/customer-service-chatbot/evidence/).

### What It Checks

| Check | Fails when | Can an exception cover it? |
|---|---|---|
| Evidence | An applicable control has no evidence path, or a path is missing, empty or a URL | Yes, unless the control is non-waivable |
| Not-applicable claims | A claim names a control whose Applies To has no condition beyond tier and system type, or a non-waivable control | No |
| Exceptions | Expired; more than 90 days from start to expiry; approver is not `approvers.exception` for the tier in [tiers.yaml](../policy/tiers.yaml) (one level higher for a renewal); raised against a non-waivable control; duplicate ID | No |
| Metric thresholds | A metric misses its [thresholds.yaml](../policy/thresholds.yaml) threshold: T1/T2 on the one-sided 95% bound (Clopper-Pearson for proportions, the reported lower bound for means), T3/T4 on the point estimate. A threshold in the report looser than the framework's also fails | Yes, an exception on the eval type's control |
| Suite sizes | A metric's `n` is below the tier minimum for its eval type, or `n` is missing | Yes, as above |
| Required metrics | A metric with a threshold at the tier is absent, where its control applies (RAG metrics only for RAG systems, agent metrics only for agentic systems) | Yes, as above |
| Segments and human evaluation | At T1/T2, a segment of 100 or more cases misses a threshold; double-rating share or agreement below the protocol minimum | Yes, an exception on EV-001 or the metric's control |
| Red-team depth (SR-001) | Fewer cases than `red_team.min_cases` for the tier, or no manual testing where the tier depth requires it | Yes |
| Open findings (SR-002) | Any open Critical finding, or the count is missing | **No** (non-waivable) |
| Open findings (SR-002) | Any open High finding | Yes (at T3/T4 this exception is the recorded risk acceptance) |
| Consistency | The eval report is for another system or tier; an agentic system is tiered below T2 | No |

The non-waivable list comes from [Exceptions and Risk Acceptance](../framework/governance-operations/governance-workflow.md#exceptions-and-risk-acceptance): RA-007, PM-006, PM-007, the Critical part of SR-002, and RA-005 where a DPIA is legally required (`dpia_legally_required`, default true for personal-data systems). The gate reads that section at run time and warns if its control IDs no longer match the list in `gate.py`.

### Control Matching Rule

A control is **required** for the system when all of these hold:

1. **Stage.** Stages 2 to 7, plus the stage 8 controls in the [minimum evidence pack](../framework/governance-operations/governance-workflow.md#minimum-evidence-pack-by-tier): PM-001 to PM-007, IR-001 and IR-002. Programme controls (stage 1), ongoing review (stage 9), retirement (stage 10) and per-incident controls are outside the gate.
2. **Tier.** The system's tier is in `applies_to.tiers`. A tier in `applies_to.recommended` makes the control recommended: reported, never blocking.
3. **System type.** `applies_to.systems` contains `all`, or at least one of the system's declared types. `rag` and `agentic` imply `genai`.
4. **Per-type tier limits.** Where the Applies To text narrows the tier by type, the gate applies it. Today that is PM-006: T1 for customer-facing systems, every tier for agentic systems.
5. **Conditions.** Controls whose Applies To carries a condition the YAML cannot express (EU AI Act scope, disclosure, marking, retrieval permissions, decision notices, model or prompt change, automated evaluation, guardrails) apply unless `governance.yaml` claims them not applicable with a reason. The list is `CONDITIONAL` in `gate.py`. EV-009 cannot be claimed not applicable while DE-004 applies. Every accepted claim is shown to the approver.

A control added to `controls/` later is picked up automatically and treated as unconditional until it is added to `CONDITIONAL`, so the gate fails closed.

### Use It in GitHub Actions

Pin `uses:` to a full commit SHA of the framework release you adopted. GitHub downloads the action's repository at that ref, and when `governance.yaml` sets no `framework.path`, the gate reads `controls/` and `policy/` from that copy. The controls you gate against change only when you move the pin, and `gate-result.json` records the ref and a digest of the framework files.

```yaml
# .github/workflows/deploy.yml in the system's repository
name: deploy
on:
  push:
    tags: ["v*"]
permissions:
  contents: read

jobs:
  governance-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
      - id: gate
        uses: your-org/ai-governance-framework/reference-implementations/governance-gate@<full-commit-sha>
        with:
          governance-file: governance.yaml
          phase: pre-approval            # approvers sign after the gate passes (DA-002 below)
      - if: always()
        uses: actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9 # v7.0.2
        with:
          name: governance-evidence-${{ github.ref_name }}
          path: |
            gate-result.json
            governance/evidence/eval-report.json

  approve-ai-risk-committee:            # one job per signer; see "Deployment approval" below
    needs: governance-gate
    runs-on: ubuntu-latest
    environment: t1-ai-risk-committee
    steps:
      - run: echo "Deployment approved for ${{ github.ref_name }}"

  approve-ciso:
    needs: governance-gate
    runs-on: ubuntu-latest
    environment: t1-ciso
    steps:
      - run: echo "Deployment approved for ${{ github.ref_name }}"

  deploy:
    needs: [approve-ai-risk-committee, approve-ciso]
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo "deploy here"
```

Action inputs: `governance-file`, `framework-path` (overrides `framework.path`), `phase` (`pre-deploy` or `pre-approval`), `output`, `today`, `setup-python`, `python-version`. Outputs: `result` (`pass` or `fail`) and `result-file`. The step fails when the gate fails, after writing the job summary and `gate-result.json`.

### governance.yaml

| Field | Content |
|---|---|
| `system.id`, `system.name` | Inventory ID (RA-006) and name |
| `system.tier` | T1 to T4, from the approved risk assessment |
| `system.types` | Any of `ml`, `genai`, `rag`, `agentic`, `fine-tuned`, `external-model`, `open-source`, `personal-data`, `external-data-flow`, `customer-facing` (the `systems` values in [the controls schema](../schemas/controls.schema.json)) |
| `system.dpia_legally_required` | Optional. Defaults to true for personal-data systems; true makes RA-005 non-waivable |
| `framework.path`, `framework.ref` | Optional. A vendored copy of this framework and its tag or commit. Leave out to use the copy the action downloaded |
| `eval_report` | Path to the evaluation report (JSON, below) |
| `evidence` | Control ID to a path or a list of paths. A file may be the record or a pointer to it in the records system (document ID, version, SHA-256). A directory counts if it holds a file |
| `not_applicable` | List of `{control, reason}` for conditional controls |
| `exceptions` | List of `{id, control, approver, start, expiry, reason, compensating_controls}`, copied from the [exception register](../templates/exception-register.md). `approver` is a role id from [roles.yaml](../policy/roles.yaml). Optional `renewal: true`, and `metrics: [...]` to limit an evaluation exception to named metrics |

Paths are relative to `governance.yaml`. The gate is offline, so evidence held in a document system is represented in the repository by a pointer file. Start from the [template](governance-gate/governance.template.yaml).

### Eval Report

A JSON file produced by the evaluation pipeline. Values are fractions (0.01 means 1%). Metric ids match [thresholds.yaml](../policy/thresholds.yaml) and the model card.

```json
{
  "system_id": "cs-assistant-retail-v1.2",
  "tier": "T1",
  "metrics": [
    {"id": "hallucination_rate", "n": 500, "failures": 1, "threshold": 0.01},
    {"id": "faithfulness", "value": 0.94, "n": 500, "lower_bound": 0.933, "interval_method": "t-interval"},
    {"id": "counterfactual_consistency", "attribute": "gender", "n": 200, "failures": 9},
    {"id": "domain_accuracy", "kind": "proportion", "direction": "min", "threshold": 0.95, "gate": "bound", "n": 500, "failures": 12}
  ],
  "segments": [{"segment": "channel: mobile app", "n": 310, "results": {"hallucination_rate": 0.003}}],
  "human_evaluation": {"double_rated_share": 0.20, "agreement": 0.84},
  "red_team": {"report": "RT-2025-CS-001", "cases": 200, "manual_testing": true},
  "security_findings": {"critical_open": 0, "high_open": 0}
}
```

- **Proportion metrics** record `n` and `failures`; `value` is optional and must agree with them. **Mean metrics** record `value`, `n`, `lower_bound` and `interval_method` (`bootstrap`, or `t-interval` when n is at least 100).
- **`threshold`** is optional. It may be stricter than the framework's (a use-case target from the risk assessment), never looser. Metrics with no framework threshold at the tier (such as agent task success) need one.
- **Use-case metrics** outside thresholds.yaml are tested against their own threshold on the point estimate, or on the bound at T1/T2 when they set `kind` and `gate: bound`.
- **`security_findings`** is required wherever SR-002 applies, which is every tier. `high_open` counts High findings neither remediated nor covered by an SR-002 exception.

### Outputs

- **`gate-result.json`**: result, phase, system, framework path, ref and digest, SHA-256 of `governance.yaml`, the status and evidence hashes of every control checked, each metric with its bound and threshold, exceptions, failures and warnings, and `evidence_pack_sha256` over all evidence hashes. Store it with the release as DA-003 evidence and tag the model version with it ([model registry](model-registry.md)).
- **Markdown summary**: written to `$GITHUB_STEP_SUMMARY` when set, and to stdout. It lists failures first, then the not-applicable claims for the approver to confirm, the metric table and the full control list.
- **Exit code**: 0 when the gate passes, 1 otherwise, including when the gate cannot run.

### What the Gate Does Not Do

- **It checks presence, not adequacy.** A file named for RA-001 passes whether or not the risk assessment is any good. People judge the content: the DA-001 evidence checklist review, the approvers, and the second-line test of each control.
- **It does not check dates or signatures.** "Before development" ordering (RA-001, RA-004), evidence age, red-team recency and who signed a record stay with the reviewers and with GV-004 and RV-001.
- **It trusts the eval report.** It recomputes Clopper-Pearson bounds from `n` and `failures` but takes mean lower bounds as reported. Generate the report in the evaluation pipeline, not by hand.
- **Traditional ML.** [thresholds.yaml](../policy/thresholds.yaml) holds GenAI metrics. For an `ml` system the gate checks evidence and any metric the report records against the report's own threshold.

### Run It Locally and Test It

From the repository root, with PyYAML installed:

```bash
python reference-implementations/governance-gate/gate.py examples/customer-service-chatbot/governance.yaml --output /tmp/gate-result.json
python -m unittest discover -s reference-implementations/governance-gate/tests -v
```

The 25 tests build a small synthetic framework, so they do not move when the real thresholds change. They cover a pass, missing and empty evidence, a valid exception, an expired exception, a wrong-tier approver, a renewal approver, an exception over 90 days, a non-waivable control with an exception (still fails), an open Critical finding with an exception (still fails), an open High finding with an exception (passes), a T1 metric that fails on the bound while passing on the point estimate, the same counts passing at T3, a use-case metric gated on the bound, an undersized suite, a missing required metric, the PM-006 tier limit, the agentic tier floor, not-applicable claims, the pre-approval phase, a report for another system, the job summary, and the non-waivable list read from the workflow. The last test runs the gate on the chatbot example against the real framework.

### Example Run: Customer Service Chatbot

Run on 2026-11-07 against this repository (v1.2.0 release, T1):

```bash
python reference-implementations/governance-gate/gate.py examples/customer-service-chatbot/governance.yaml
```

Output, with the collapsed list of all 47 controls and their evidence paths left out:

```markdown
## AI governance gate: PASS

System `cs-assistant-retail-v1.2` (Retail Banking Customer Service Assistant), tier T1, types: customer-facing, external-data-flow, external-model, genai, personal-data, rag. Phase: pre-deploy. As of 2026-11-07. Gate 1.0.0.

| Check | Count |
|---|---|
| Controls required for this system | 47 |
| Evidenced | 44 |
| Not applicable (claimed, reason recorded) | 3 |
| Covered by an exception | 0 |
| Pending sign-off | 0 |
| Missing | 0 |
| Metrics checked | 14 (0 failing) |
| Failures | 0 |
| Warnings | 0 |

### Not-applicable claims for the approver to confirm

| Control | Condition | Reason given |
|---|---|---|
| RA-009 | the organisation is a deployer in scope of EU AI Act Art. 27 | Not an Annex III system. The assistant gives information only and makes no decision about customers (decision_type informational in the model card). |
| DE-008 | the RAG sources carry access restrictions | The RAG sources are customer-facing documents with no per-user access restrictions (rag_configuration.document_sources in the model card). Account data comes from a read-only API scoped to the authenticated customer, not from the index. |
| DE-009 | the system makes or assists decisions about people where a notice duty applies | Makes and assists no decisions about people. Credit, complaints, fraud disputes and account changes are out of scope and routed to human agents. |

### Evaluation

| Metric | Control | n | Failures | Value | Bound | Threshold | Rule | Result |
|---|---|---|---|---|---|---|---|---|
| hallucination_rate | EV-001 | 500 | 1 | 0.002 | 0.95% upper | 0.01 | confidence-bound | pass |
| faithfulness | EV-001 | 500 |  | 0.94 | 0.933 lower | 0.9 | confidence-bound | pass |
| safety_pass_rate | EV-002 | 500 | 1 | 0.998 | 0.95% upper | 0.99 | confidence-bound | pass |
| retrieval_precision_at_5 | EV-004 | 200 |  | 0.88 | 0.861 lower | 0.85 | confidence-bound | pass |
| guardrail_false_negative_rate | EV-009 | 300 | 0 | 0 | 0.99% upper | 0.01 | confidence-bound | pass |
| guardrail_false_positive_rate | EV-009 | 300 | 6 | 0.02 | 3.91% upper | 0.05 | confidence-bound | pass |
| counterfactual_consistency (gender) | EV-005 | 200 | 9 | 0.955 | 7.72% upper | 0.9 | confidence-bound | pass |
| counterfactual_consistency (age_group) | EV-005 | 200 | 10 | 0.95 | 8.33% upper | 0.9 | confidence-bound | pass |
| counterfactual_consistency (nationality) | EV-005 | 200 | 11 | 0.945 | 8.94% upper | 0.9 | confidence-bound | pass |
| counterfactual_consistency (language_preference) | EV-005 | 200 | 10 | 0.95 | 8.33% upper | 0.9 | confidence-bound | pass |
| relevance | EV-001 |  |  | 0.91 |  | 0.85 | point-estimate | pass |
| correctness | EV-001 |  |  | 0.96 |  | 0.95 | point-estimate | pass |
| format_compliance | EV-001 |  |  | 0.99 |  | 0.95 | point-estimate | pass |
| escalation_appropriateness | EV-001 |  |  | 0.93 |  | 0.9 | point-estimate | pass |

- Red-team (SR-001): 200 cases against a T1 minimum of 200: pass
- Open findings (SR-002): 0 Critical, 0 High: pass
- Segments: 3 of 6 large enough to gate; 0 failing
```

The run ends with `governance gate: PASS (0 failures, 0 warnings)` and exit code 0.

The evidence files are placeholders that point into the [case file](../examples/customer-service-chatbot/governance-case-file.md), [risk assessment](../examples/customer-service-chatbot/risk-assessment.md) and [model card](../examples/customer-service-chatbot/model-card.yaml). The eval report numbers are the model card's v1.2.0 evaluation. Nine placeholders say "Gap in this example": the case file does not cover RA-006, RA-007, RA-008, AR-007, DE-006 or DE-007, and does not show the EV-006 dataset version, the latest EV-007 calibration or the PM-007 completeness checks. The gate passes because it checks presence; a reviewer reading those files would send them back. That is the limit described above, shown on purpose.

---

## GitHub Features as Evidence

Set the repository up so the platform records the approvals the framework asks for. Then export what it records into the evidence store: platform logs and artifacts are not kept for the governance record retention period in [tiers.yaml](../policy/tiers.yaml) (at T1, the life of the system plus 7 years after retirement).

### Prompt Review: CODEOWNERS and Branch Protection (DE-002, DE-003)

Keep prompts in a `prompts/` directory, so the commit history is the prompt version history (DE-002). Assign owners in `.github/CODEOWNERS`:

```text
/prompts/ @your-org/prompt-engineering-leads
```

Then protect the default branch (branch protection rule or ruleset): require a pull request, require review from Code Owners, dismiss stale approvals when new commits are pushed, and set the required approvals by tier from `approvers.prompt_review` in [tiers.yaml](../policy/tiers.yaml):

| Tier | Prompt review | Repository setting |
|---|---|---|
| T1 | Peer review + prompt engineering lead + security review + AI Risk sign-off | 2 approvals including a code owner, plus the security and AI Risk sign-offs in the prompt review record |
| T2 | Peer review + prompt engineering lead | 2 approvals including a code owner |
| T3 | Peer review | 1 approval |
| T4 | Self-review | Pull request recorded; no approval required |

GitHub accepts an approval from any one of the owners listed for a path, so CODEOWNERS cannot require two different teams on the same file. At T1, record the security review and AI Risk sign-off in the [prompt review checklist](../templates/prompt-review-checklist.md) and list it as DE-003 evidence; the pull request URL goes in the same record. Code owners need write access, and the CODEOWNERS file must be on the pull request's base branch.

### Deployment Approval: Environments With Required Reviewers (DA-002)

Create one environment per signing role, add the role's people or team as required reviewers, and turn on "Prevent self-review". GitHub lets any one of an environment's required reviewers approve, so a co-signed tier needs one environment, and one approval job, per signer. The approval jobs run after the gate, so run the gate with `phase: pre-approval`.

| Tier | Environments (from `approvers.deployment` in [tiers.yaml](../policy/tiers.yaml)) |
|---|---|
| T1 | AI Risk Committee; CISO; DPO when personal data is processed |
| T2 | Head of AI; Business Unit Head |
| T3 | Team lead; business owner |
| T4 | Team lead |

A committee does not click buttons. The committee secretary or chair approves after the decision and puts the minute reference in the approval comment. Restrict each environment's deployment branches or tags to the release refs. Export the approval record (approver, time, comment, run URL) to the evidence store as DA-002 evidence. Environment protection rules for private repositories depend on the GitHub plan; check yours before relying on them.

### Evaluation Reports: Workflow Artifacts (EV-001, EV-002)

Have the evaluation job write the eval report and the per-case results, upload them as workflow artifacts, and pass the report path to the gate. Artifact retention is capped by the repository, organisation or enterprise setting, so copy the report to the evidence store in the same job. The gate records the report's SHA-256 in `gate-result.json`, which lets an auditor confirm that the stored copy is the one the gate judged.
