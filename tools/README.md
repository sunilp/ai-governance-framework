# Tools

Several framework tables are generated from YAML. The YAML files are the source of truth. The Markdown tables are a rendering of them, and CI fails when the two drift apart.

## Source files

| File | What it holds | Generates |
|---|---|---|
| [controls/](../controls/) `stage-NN-*.yaml` | The register controls, one file per workflow stage. Besides the register columns, each control records `type` (preventive, detective or corrective), `automation`, `key_control`, `test` (how the second line or internal audit tests that it operates) and `sources` (the framework documents that define it). | Stage tables and the Traceability section in [control-register.md](../framework/governance-operations/control-register.md) |
| [policy/roles.yaml](../policy/roles.yaml) | Roles, line of defence and descriptions. Control owners and tier approvers refer to these ids. | Role Definitions in [roles-responsibilities.md](../framework/operating-model/roles-responsibilities.md) |
| [policy/tiers.yaml](../policy/tiers.yaml) | Per tier: review cadence, metrics review, revalidation, approvers, retention, production evaluation rates and red-team depth. | Approvals by Tier, [Cadence by Tier](../framework/operating-model/review-cadence.md), [interaction log retention](../framework/compliance/prompt-audit-trail.md) |
| [policy/thresholds.yaml](../policy/thresholds.yaml) | Metric thresholds per tier with their definitions, and evaluation suite sizes. | Evaluation Types, Threshold Definitions by Tier and Metric Definitions in [evaluation-governance.md](../framework/llm-lifecycle/evaluation-governance.md) |
| [policy/severity.yaml](../policy/severity.yaml) | Incident severities S1 to S4 and alert priorities P1 to P4. | Severity, follow-up and alert mapping tables in [escalation-paths.md](../framework/operating-model/escalation-paths.md) |
| [schemas/](../schemas/) | JSON Schema (draft 2020-12) for each file above and for the two model card templates. | |

## Changing a control or a threshold

1. Edit the YAML file. Do not edit a generated table: everything between a `BEGIN GENERATED` marker and its `END GENERATED` marker is overwritten.
2. Run `python tools/build.py` to regenerate the tables.
3. Run `python tools/check.py` and fix every error.
4. Commit the YAML and the regenerated Markdown together.

A new control needs an owner from `policy/roles.yaml` and at least one existing source document. A new generated table needs a renderer and an entry in `BLOCKS` in `build.py`, plus the BEGIN and END markers in the document.

Setup: Python 3.10 or later, then `pip install -r tools/requirements.txt`.

## What CI enforces

[.github/workflows/validate.yml](../.github/workflows/validate.yml) runs `python tools/check.py` on every push and pull request. The run fails when:

- a control file, policy file or example model card does not match its schema;
- a control ID cited in `framework/`, `templates/`, `examples/`, `controls/`, `policy/` or a top-level Markdown file is not defined in `controls/` (a token preceded by a letter, digit or hyphen, such as `AR-2026-RA-001`, is a document ID and is ignored);
- a control owner or tier approver is not a role in `policy/roles.yaml`, or a source path does not exist;
- red-team depth differs between `tiers.yaml` and `thresholds.yaml`, or the RV-001 frequency no longer matches the review cadence in `tiers.yaml`;
- a relative link or heading anchor in a Markdown file outside `docs/` does not resolve (GitHub anchor rules, case-sensitive paths);
- a generated table is out of date with its YAML;
- an example GenAI model card breaks the rules for its tier: a metric threshold looser than `thresholds.yaml`, a metric value that misses its threshold with no exception ID (`EXC-YYYY-NNN`) anywhere in the card, a hallucination tolerance above the tier cap, a pre-release, red-team or offline re-run suite smaller than the tier minimum, a production result that breaches a threshold without being recorded as a failure, or a T1 customer-facing system that does not use human-in-the-loop or human-over-the-loop (over-the-loop also needs the `human_oversight_safeguards` block with safeguards a to e);
- a T1 or T2 card metric does not record `n` and `failures` (proportion metrics) or `n`, `lower_bound` and `interval_method` (mean metrics), or its one-sided 95% bound misses the threshold under the [statistical pass rule](../framework/llm-lifecycle/evaluation-governance.md#statistical-pass-rule); the check recomputes Clopper-Pearson bounds from `n` and `failures`;
- a T1 or T2 suite minimum in `thresholds.yaml` is too small for zero failures to demonstrate the cap;
- a T1 or T2 segment with 100 or more cases (`segment_results`) misses the threshold, a counterfactual attribute (`attribute_results`) misses it, human evaluation (`human_evaluation`) double-rates less than 20% of items or reports agreement below 0.6, or a guardrail false positive threshold is above the framework default ceiling;
- a `Status as of <Month YYYY>` line in `framework/` is more than 180 days old, counted from the first day of that month. After 90 days it is a warning.

Warnings report checks that could not run, for example a framework metric that a card does not record. They do not fail the run. Notes record passes that depend on an exception or a recorded failure.

How the card checks read a GenAI model card: metric names match the ids in `thresholds.yaml` (`hallucination_rate`, `faithfulness`, `safety_pass_rate`, `retrieval_precision_at_5`, and `counterfactual_consistency` from `bias_evaluation`). Card values are fractions, so 0.01 means 1%. Other metrics are treated as higher-is-better unless the metric sets `direction: max`. `adversarial_testing.test_type` says whether `test_suite_size` counts a red-team or a prompt-change regression set. Traditional ML cards are checked against their schema only.
