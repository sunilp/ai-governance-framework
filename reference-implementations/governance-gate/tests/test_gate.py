"""Tests for gate.py. Plain unittest, no dependencies beyond PyYAML.

Run from the repository root:
    python -m unittest discover -s reference-implementations/governance-gate/tests -v

Most tests build a small synthetic framework in a temporary directory, so they do not change
when the real controls or thresholds change. The last test runs the gate on the customer
service chatbot example against the real framework.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import contextlib  # noqa: E402
import io  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import tempfile  # noqa: E402
import textwrap  # noqa: E402
import unittest  # noqa: E402
from pathlib import Path  # noqa: E402

import yaml  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import gate  # noqa: E402

REPO = HERE.parents[2]
TODAY = "2026-11-07"


def control(cid, stage, tiers, systems, recommended=None):
    applies = {"text": "test", "tiers": tiers, "systems": systems}
    if recommended:
        applies["recommended"] = recommended
    return {"id": cid, "title": f"{cid} title", "stage": stage, "applies_to": applies, "owner": "product-owner",
            "evidence": "x", "frequency": "x", "on_fail": "x", "type": "preventive", "automation": "manual",
            "key_control": True, "test": "x", "sources": ["x.md"]}


ALL = ["T1", "T2", "T3", "T4"]
CONTROLS = {
    2: [control("RA-001", 2, ALL, ["all"]), control("RA-007", 2, ALL, ["all"])],
    5: [control("EV-001", 5, ALL, ["all"]), control("EV-002", 5, ALL, ["genai"]),
        control("EV-003", 5, ["T1", "T2"], ["all"], recommended=["T3"])],
    6: [control("SR-002", 6, ALL, ["all"])],
    8: [control("PM-006", 8, ["T1", "T2"], ["customer-facing", "agentic"])],
    9: [control("RV-001", 9, ALL, ["all"])],
}


def approvers(role):
    return {"exception": {"text": role, "accountable": role}}


TIERS_YAML = {"tiers": {
    "T1": {"approvers": approvers("ai-risk-committee"), "red_team": {"min_cases": 200, "depth": "200+, including manual testing"}},
    "T2": {"approvers": approvers("ai-risk"), "red_team": {"min_cases": 100, "depth": "100+"}},
    "T3": {"approvers": approvers("head-of-ai"), "red_team": {"min_cases": 50, "depth": "50"}},
    "T4": {"approvers": approvers("team-lead"), "red_team": {"min_cases": 20, "depth": "20"}},
}}

THRESHOLDS_YAML = {
    "pass_rule": {"confidence": 0.95, "tiers": {"T1": "confidence-bound", "T2": "confidence-bound",
                                                 "T3": "point-estimate", "T4": "point-estimate"},
                  "mean_methods": {"bootstrap": {"resamples": 10000}, "t-interval": {"min_n": 100}},
                  "segments": {"tiers": ["T1", "T2"], "min_cases": 100}},
    "metrics": [
        {"id": "hallucination_rate", "kind": "proportion", "eval_type": "pre_release", "direction": "max",
         "unit": "percent", "thresholds": {"T1": 1, "T2": 3, "T3": 5, "T4": 10}},
        {"id": "safety_pass_rate", "kind": "proportion", "eval_type": "safety", "direction": "min",
         "unit": "percent", "thresholds": {"T1": 99, "T2": 97, "T3": 95, "T4": 90}},
    ],
    "eval_types": [
        {"id": "pre_release", "control": "EV-001", "suite": {"T1": 300, "T2": 100, "T3": 50, "T4": 20}},
        {"id": "safety", "control": "EV-002", "suite": {"T1": 300, "T2": 100, "T3": 50, "T4": 20}},
    ],
}

WORKFLOW_MD = textwrap.dedent("""\
    # Governance Workflow

    ## Exceptions and Risk Acceptance

    **Non-waivable.** These cannot be excepted at any tier:
    - A DPIA where it is legally required
    - Checks against prohibited uses (RA-007)
    - Zero unresolved Critical red-team findings (the Critical part of SR-002)
    - A kill switch for T1 customer-facing systems and for all agentic systems (PM-006)
    - Audit logging (PM-007)

    Any other control can be excepted through this process.
    """)


class GateTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        fw = self.root / "framework-copy"
        (fw / "controls").mkdir(parents=True)
        (fw / "policy").mkdir()
        (fw / "framework" / "governance-operations").mkdir(parents=True)
        for stage, items in CONTROLS.items():
            doc = {"stage": stage, "name": f"Stage {stage}", "controls": items}
            (fw / "controls" / f"stage-{stage:02d}-test.yaml").write_text(yaml.safe_dump(doc), encoding="utf-8")
        (fw / "policy" / "tiers.yaml").write_text(yaml.safe_dump(TIERS_YAML), encoding="utf-8")
        (fw / "policy" / "thresholds.yaml").write_text(yaml.safe_dump(THRESHOLDS_YAML), encoding="utf-8")
        (fw / gate.WORKFLOW_DOC).write_text(WORKFLOW_MD, encoding="utf-8")

        self.sys_dir = self.root / "system"
        (self.sys_dir / "evidence").mkdir(parents=True)
        for cid in ("RA-001", "RA-007", "EV-001", "EV-002", "EV-003", "SR-002", "PM-006"):
            (self.sys_dir / "evidence" / f"{cid}.md").write_text(f"{cid} record\n", encoding="utf-8")
        self.report = {
            "system_id": "sys-1", "tier": "T1",
            "metrics": [{"id": "hallucination_rate", "n": 500, "failures": 1},
                        {"id": "safety_pass_rate", "n": 500, "failures": 1}],
            "security_findings": {"critical_open": 0, "high_open": 0},
        }
        self.gov = {
            "schema_version": 1,
            "system": {"id": "sys-1", "tier": "T1", "types": ["genai", "customer-facing"]},
            "framework": {"path": "../framework-copy"},
            "eval_report": "evidence/eval-report.json",
            "evidence": {cid: f"evidence/{cid}.md" for cid in ("RA-001", "RA-007", "EV-001", "EV-002", "EV-003", "SR-002", "PM-006")},
            "exceptions": [],
        }

    def tearDown(self):
        self.tmp.cleanup()

    def run_gate(self, *extra):
        (self.sys_dir / "evidence" / "eval-report.json").write_text(json.dumps(self.report), encoding="utf-8")
        gov_path = self.sys_dir / "governance.yaml"
        gov_path.write_text(yaml.safe_dump(self.gov, sort_keys=False), encoding="utf-8")
        out = self.root / "gate-result.json"
        with contextlib.redirect_stdout(io.StringIO()):
            code = gate.main([str(gov_path), "--output", str(out), "--today", TODAY, "--quiet", *extra])
        result = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(code, 0 if result["result"] == "pass" else 1)
        return code, result

    def messages(self, result):
        return " | ".join(f["message"] for f in result["failures"])

    def status(self, result, cid):
        return next(c["status"] for c in result["controls"] if c["id"] == cid)

    # -- the cases the gate exists for ---------------------------------------

    def test_pass(self):
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))
        self.assertEqual(result["result"], "pass")
        self.assertEqual({c["id"] for c in result["controls"]},
                         {"RA-001", "RA-007", "EV-001", "EV-002", "EV-003", "SR-002", "PM-006"})  # RV-001 is stage 9
        self.assertTrue(all(c["status"] == "evidenced" for c in result["controls"]))
        self.assertEqual(len(result["evidence_pack_sha256"]), 64)

    def test_missing_evidence(self):
        (self.sys_dir / "evidence" / "RA-001.md").unlink()
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("RA-001 evidence missing", self.messages(result))
        self.assertEqual(self.status(result, "RA-001"), "missing")

    def test_empty_evidence_file_counts_as_missing(self):
        (self.sys_dir / "evidence" / "RA-001.md").write_text("", encoding="utf-8")
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("is empty", self.messages(result))

    def test_valid_exception_covers_missing_evidence(self):
        (self.sys_dir / "evidence" / "RA-001.md").unlink()
        self.gov["exceptions"] = [{"id": "EXC-2026-001", "control": "RA-001", "approver": "ai-risk-committee",
                                   "start": "2026-10-01", "expiry": "2026-12-15", "reason": "test"}]
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))
        self.assertEqual(self.status(result, "RA-001"), "excepted")
        self.assertTrue(result["exceptions"][0]["used"])

    def test_expired_exception_fails(self):
        (self.sys_dir / "evidence" / "RA-001.md").unlink()
        self.gov["exceptions"] = [{"id": "EXC-2026-002", "control": "RA-001", "approver": "ai-risk-committee",
                                   "start": "2026-08-01", "expiry": "2026-10-30"}]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("expired on 2026-10-30", self.messages(result))
        self.assertEqual(self.status(result, "RA-001"), "missing")

    def test_expired_exception_fails_even_when_evidence_exists(self):
        self.gov["exceptions"] = [{"id": "EXC-2026-003", "control": "RA-001", "approver": "ai-risk-committee",
                                   "start": "2026-08-01", "expiry": "2026-10-30"}]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("expired", self.messages(result))

    def test_wrong_tier_approver_fails(self):
        (self.sys_dir / "evidence" / "RA-001.md").unlink()
        self.gov["exceptions"] = [{"id": "EXC-2026-004", "control": "RA-001", "approver": "head-of-ai",
                                   "start": "2026-10-01", "expiry": "2026-12-15"}]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("the T1 exception approver is 'ai-risk-committee'", self.messages(result))

    def test_renewal_needs_approver_one_level_higher(self):
        self.gov["system"]["tier"] = "T3"
        self.report["tier"] = "T3"
        (self.sys_dir / "evidence" / "RA-001.md").unlink()
        exc = {"id": "EXC-2026-005", "control": "RA-001", "start": "2026-10-01", "expiry": "2026-12-15", "renewal": True}
        self.gov["exceptions"] = [dict(exc, approver="head-of-ai")]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("one level higher (T2) is 'ai-risk'", self.messages(result))
        self.gov["exceptions"] = [dict(exc, approver="ai-risk")]
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))

    def test_exception_longer_than_90_days_fails(self):
        (self.sys_dir / "evidence" / "RA-001.md").unlink()
        self.gov["exceptions"] = [{"id": "EXC-2026-006", "control": "RA-001", "approver": "ai-risk-committee",
                                   "start": "2026-10-01", "expiry": "2027-03-01"}]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("the maximum is 90", self.messages(result))

    def test_non_waivable_control_with_exception_still_fails(self):
        (self.sys_dir / "evidence" / "RA-007.md").unlink()
        self.gov["exceptions"] = [{"id": "EXC-2026-007", "control": "RA-007", "approver": "ai-risk-committee",
                                   "start": "2026-10-01", "expiry": "2026-12-15"}]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        msgs = self.messages(result)
        self.assertIn("RA-007 is non-waivable and cannot be excepted", msgs)
        self.assertIn("no exception can cover it", msgs)
        self.assertEqual(self.status(result, "RA-007"), "missing")

    def test_open_critical_finding_cannot_be_excepted(self):
        self.report["security_findings"] = {"critical_open": 1, "high_open": 0}
        self.gov["exceptions"] = [{"id": "EXC-2026-008", "control": "SR-002", "approver": "ai-risk-committee",
                                   "start": "2026-10-01", "expiry": "2026-12-15"}]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("open Critical finding", self.messages(result))

    def test_open_high_finding_can_be_excepted(self):
        self.report["security_findings"] = {"critical_open": 0, "high_open": 1}
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.gov["exceptions"] = [{"id": "EXC-2026-009", "control": "SR-002", "approver": "ai-risk-committee",
                                   "start": "2026-10-01", "expiry": "2026-12-15"}]
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))
        self.assertEqual(result["evaluation"]["security_findings"]["result"], "excepted")

    def test_t1_metric_fails_on_bound_but_passes_on_point_estimate(self):
        # 1 failure in 300: point estimate 0.33%, within the 1% cap; upper bound about 1.58%, above it.
        self.report["metrics"][0] = {"id": "hallucination_rate", "n": 300, "failures": 1}
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        msgs = self.messages(result)
        self.assertIn("failure-rate upper bound", msgs)
        self.assertIn("although the point estimate 0.33% is within it", msgs)
        metric = result["evaluation"]["metrics"][0]
        self.assertGreater(metric["bound"], 0.01)
        self.assertEqual(metric["rule"], "confidence-bound")

    def test_same_counts_pass_at_t3_on_point_estimate(self):
        self.gov["system"]["tier"] = "T3"
        self.report["tier"] = "T3"
        self.report["metrics"][0] = {"id": "hallucination_rate", "n": 300, "failures": 1}
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))
        self.assertEqual(result["evaluation"]["metrics"][0]["rule"], "point-estimate")

    def test_use_case_metric_gates_on_bound_when_declared(self):
        row = {"id": "domain_accuracy", "kind": "proportion", "direction": "min", "threshold": 0.99, "n": 300, "failures": 1}
        self.report["metrics"].append(dict(row))
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))   # no gate field: point estimate 0.9967 passes
        self.report["metrics"][-1] = dict(row, gate="bound")
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("domain_accuracy: failure-rate upper bound", self.messages(result))

    def test_undersized_suite_fails(self):
        # Zero failures, but 200 cases is below the T1 pre-release minimum of 300.
        self.report["metrics"][0] = {"id": "hallucination_rate", "n": 200, "failures": 0}
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("n 200 is below the T1 pre_release suite minimum of 300", self.messages(result))

    # -- matching rule --------------------------------------------------------

    def test_missing_required_metric_fails(self):
        del self.report["metrics"][1]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("safety_pass_rate is not in the eval report", self.messages(result))

    def test_kill_switch_applies_to_t1_customer_facing_not_t2(self):
        self.gov["system"]["tier"] = "T2"
        self.report["tier"] = "T2"
        self.report["metrics"] = [{"id": "hallucination_rate", "n": 100, "failures": 0},
                                  {"id": "safety_pass_rate", "n": 100, "failures": 0}]
        del self.gov["evidence"]["PM-006"]
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))
        self.assertNotIn("PM-006", {c["id"] for c in result["controls"]})
        self.gov["system"]["types"] = ["genai", "agentic"]
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("PM-006 evidence missing", self.messages(result))

    def test_agentic_below_t2_fails(self):
        self.gov["system"]["types"] = ["agentic"]
        self.gov["system"]["tier"] = "T3"
        self.report["tier"] = "T3"
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("every agentic system is at least T2", self.messages(result))

    def test_not_applicable_claims(self):
        # EV-003 is conditional (model or prompt change), so a reasoned claim is accepted.
        del self.gov["evidence"]["EV-003"]
        self.gov["not_applicable"] = [{"control": "EV-003", "reason": "First release; no previous version."}]
        code, result = self.run_gate()
        self.assertEqual(code, 0, self.messages(result))
        self.assertEqual(self.status(result, "EV-003"), "not-applicable")
        # RA-001 has no condition beyond tier and system type, so the claim is refused.
        self.gov["not_applicable"].append({"control": "RA-001", "reason": "Not needed."})
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("RA-001 cannot be claimed not applicable", self.messages(result))

    def test_pre_approval_phase_allows_pending_sign_off(self):
        CONTROLS[7] = [control("DA-002", 7, ALL, ["all"])]
        try:
            self.tmp.cleanup()
            self.setUp()
            code, result = self.run_gate()
            self.assertEqual(code, 1)
            self.assertIn("DA-002 evidence missing", self.messages(result))
            code, result = self.run_gate("--phase", "pre-approval")
            self.assertEqual(code, 0, self.messages(result))
            self.assertEqual(self.status(result, "DA-002"), "pending-sign-off")
        finally:
            del CONTROLS[7]

    def test_report_for_another_system_fails(self):
        self.report["system_id"] = "other-system"
        code, result = self.run_gate()
        self.assertEqual(code, 1)
        self.assertIn("does not match system.id", self.messages(result))

    def test_writes_step_summary(self):
        summary = self.root / "summary.md"
        os.environ["GITHUB_STEP_SUMMARY"] = str(summary)
        try:
            self.run_gate()
        finally:
            del os.environ["GITHUB_STEP_SUMMARY"]
        self.assertIn("## AI governance gate: PASS", summary.read_text(encoding="utf-8"))

    def test_non_waivable_list_read_from_workflow(self):
        fw = gate.Framework(self.root / "framework-copy")
        ids, dpia = fw.documented_non_waivable()
        self.assertEqual(ids, {"RA-007", "SR-002", "PM-006", "PM-007"})
        self.assertTrue(dpia)


class ChatbotExampleTest(unittest.TestCase):
    """The flagship example passes against the real framework."""

    def test_chatbot_example_passes(self):
        gov = REPO / "examples" / "customer-service-chatbot" / "governance.yaml"
        if not gov.is_file():
            self.skipTest("chatbot example not present")
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "gate-result.json"
            with contextlib.redirect_stdout(io.StringIO()):
                code = gate.main([str(gov), "--output", str(out), "--quiet"])
            result = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(code, 0, " | ".join(f["message"] for f in result["failures"]))
        self.assertEqual(result["system"]["tier"], "T1")


if __name__ == "__main__":
    unittest.main()
