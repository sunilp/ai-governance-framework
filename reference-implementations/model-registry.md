# Model Registry Tagging Pattern

**Purpose:** Tie each deployable model version in a registry such as MLflow or Vertex AI Model Registry to its governance state, so a deployment tool can refuse an ungoverned version and an auditor can go from the running version to its evidence in one step. The pattern is generic; field names are a suggestion.

---

## Fields

Write these on the model version, not only on the registered model: governance state belongs to a version. The pipeline writes them from `gate-result.json` after the [governance gate](README.md#governance-gate) passes, so nobody types them by hand.

| Field | Value | Control |
|---|---|---|
| `governance.system_id` | AI inventory ID | RA-006 |
| `governance.tier` | T1 to T4, from the approved risk assessment | RA-001, RA-004 |
| `governance.model_card` | Model card location and version | DE-001 |
| `governance.gate_result` | `pass` or `fail` | DA-003 |
| `governance.gate_result_ref` | Where the stored `gate-result.json` is | DA-003 |
| `governance.evidence_pack_sha256` | `evidence_pack_sha256` from `gate-result.json` | DA-001 |
| `governance.controls_evidenced` | Count of controls evidenced, excepted and claimed not applicable (the full list stays in `gate-result.json`) | DA-001 |
| `governance.eval_report_sha256` | `evaluation.report_sha256` from `gate-result.json` | EV-001 |
| `governance.framework_ref` | Framework tag or commit the gate used, and its digest | Traceability |
| `governance.approval_ref` | Deployment approval record ID | DA-002 |
| `governance.exceptions` | Open exception IDs with expiry dates, or `none` | GV-004 |
| `governance.change_ref` | Material change assessment ID, for a version that replaces another | RV-003 |
| `governance.status` | `candidate`, `approved`, `production`, `retired` | DR-003, DR-004 |

## Promotion Rule

The deployment tool resolves a named reference (an alias such as `production`) to a version. Move that reference only when the target version has:

- `governance.gate_result` = `pass` and a `gate_result_ref` that resolves;
- an `approval_ref`;
- a `tier` that matches the inventory entry;
- no exception in `governance.exceptions` past its expiry.

Run the same check in the deployment job, not only at promotion, so a version whose exception has expired since promotion is caught. A new version created by a material change carries no governance fields until its own gate run, so it cannot take the alias by accident.

## Platform Notes

**MLflow.** The Model Registry supports tags (key-value pairs) on registered models and on model versions, and aliases: mutable, named references to a version. Put the fields above on the version and use an alias for the version the deployment tool resolves.

**Vertex AI Model Registry.** Model version details include labels and a description. A version alias is unique within a model ("an alias can only be assigned to a single version, by model, at a time"), and the default alias marks the version used when none is named. Labels have character and length limits, so check the current Google Cloud label requirements before you store long values: a SHA-256 or a URI may not fit. Put short values (tier, gate result, status) in labels and long ones in the version description or an external metadata store keyed by version.

**Systems on vendor APIs.** A system that calls an external model, such as the [customer service chatbot](../examples/customer-service-chatbot/model-card.yaml), has no model artifact of its own to register. Register the release instead: model ID, prompt version, retrieval and guardrail configuration as one versioned entry, with the same fields. If the registry cannot hold that, put the fields on the deployment record.

## Retirement

At retirement (DR-003, DR-004), remove the alias, set `governance.status` to `retired`, and archive the version with its fields and the referenced `gate-result.json` for the governance record retention period in [tiers.yaml](../policy/tiers.yaml). The registry entry is then the index into the archived evidence.
