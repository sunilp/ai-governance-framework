#!/usr/bin/env python3
"""Pre-deployment governance gate for one AI system.

Reads the system's governance.yaml, resolves which framework controls apply from
controls/*.yaml, and fails the run when:

  - an applicable pre-deployment control has no evidence file and no valid exception;
  - an exception is expired, longer than 90 days, approved by the wrong role for the tier,
    or raised against a non-waivable control;
  - the evaluation report misses a threshold in policy/thresholds.yaml under the
    statistical pass rule (T1/T2 on the one-sided 95% bound, T3/T4 on the point
    estimate), records a suite smaller than the tier minimum, or leaves out a metric
    the tier requires;
  - the red-team depth is below the tier minimum, or any Critical finding is open.

Writes gate-result.json and a Markdown summary (to $GITHUB_STEP_SUMMARY when set).
Exit code 0 when the gate passes, 1 otherwise.

Python 3.10 or later. Needs PyYAML only. No network access.

Usage:
    python gate.py [governance.yaml] [--framework DIR] [--output gate-result.json]
                   [--phase pre-deploy|pre-approval] [--today YYYY-MM-DD]

See reference-implementations/README.md for the governance.yaml and eval report formats.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import datetime as dt  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
from pathlib import Path  # noqa: E402

import yaml  # noqa: E402

GATE_VERSION = "1.0.0"
TIERS = ("T1", "T2", "T3", "T4")
WORKFLOW_DOC = "framework/governance-operations/governance-workflow.md"

# System types a governance.yaml may declare: the systems enum in schemas/controls.schema.json,
# less "all" and the lifecycle states "replaced" and "retired" (stage 10, outside this gate).
SYSTEM_TYPES = {"ml", "genai", "rag", "agentic", "fine-tuned", "external-model", "open-source",
                "personal-data", "external-data-flow", "customer-facing"}
# A RAG system and an agentic system are GenAI systems, so GenAI controls apply to them.
IMPLIED_TYPES = {"rag": {"genai"}, "agentic": {"genai"}}

# Controls the gate checks: stages 2 to 7, plus the stage 8 controls in the minimum evidence
# pack (governance-workflow.md "Minimum Evidence Pack by Tier": rows 14 and 15, and PM-006 and
# PM-007 in the paragraph below the table). Stage 1 is programme-level; stages 9 and 10 and the
# per-incident controls run after go-live.
GATED_STAGES = range(2, 8)
PRE_GO_LIVE_STAGE8 = {"PM-001", "PM-002", "PM-003", "PM-004", "PM-005", "PM-006", "PM-007", "IR-001", "IR-002"}

# The sign-off itself. With --phase pre-approval the gate runs before approvers sign, so DA-002
# is reported as pending instead of missing.
SIGN_OFF_CONTROL = "DA-002"

# Per-type tier limits that the Applies To text sets and the YAML cannot express.
# PM-006 applies to T1 customer-facing systems and to all agentic systems.
TIER_BY_SYSTEM = {"PM-006": {"customer-facing": ("T1",)}}

# Controls whose Applies To text carries a condition beyond tier and system type. The gate cannot
# evaluate these conditions, so governance.yaml may record them under not_applicable with a
# reason, which the summary shows to the deployment approver. Any other control cannot be
# claimed not applicable. Add an entry here when the framework adds a conditional control.
CONDITIONAL = {
    "RA-008": "the system is in scope of the EU AI Act (Art. 2(1))",
    "RA-009": "the organisation is a deployer in scope of EU AI Act Art. 27",
    "DE-006": "the system interacts directly with people and the interaction is not obvious (Art. 50(1)), "
              "or performs emotion recognition or biometric categorisation (Art. 50(3))",
    "DE-007": "the organisation provides a system that generates synthetic text, image, audio or video "
              "(Art. 50(2)), or publishes deep fakes or public-interest text (Art. 50(4))",
    "DE-008": "the RAG sources carry access restrictions",
    "DE-009": "the system makes or assists decisions about people where a notice duty applies",
    "EV-003": "the release changes the model or a prompt of a system already in production",
    "EV-007": "the system uses automated evaluation (LLM-as-judge)",
    "EV-009": "the system has guardrails",
}
# A not-applicable claim is refused while the named control applies (DE-004 requires guardrails
# for T1/T2 GenAI, so their guardrail evaluation cannot be skipped).
NA_BLOCKED_BY = {"EV-009": "DE-004"}

# Non-waivable items, from governance-workflow.md#exceptions-and-risk-acceptance. The gate also
# reads that section at run time and warns if its list of control IDs differs from this one.
#   full      no exception, no not-applicable claim
#   critical  SR-002: open Critical findings cannot be excepted; open High findings can
#   dpia      RA-005: non-waivable where a DPIA is legally required (dpia_legally_required)
NON_WAIVABLE = {"RA-007": "full", "PM-006": "full", "PM-007": "full", "SR-002": "critical", "RA-005": "dpia"}

MAX_EXCEPTION_DAYS = 90  # governance-workflow.md "Duration"
EXC_ID_RE = re.compile(r"^EXC-\d{4}-\d{3}$")
CONTROL_ID_RE = re.compile(r"(?<![A-Za-z0-9-])([A-Z]{2}-\d{3})(?![0-9])")


class GateError(Exception):
    """A configuration problem that stops the gate from running."""


# ---------------------------------------------------------------------------
# Statistical pass rule, ported from tools/build.py so the gate does not need the
# framework's tools/ directory (evaluation-governance.md "Statistical Pass Rule").
# ---------------------------------------------------------------------------

def binom_cdf(x: int, n: int, p: float) -> float:
    """P(X <= x) for X ~ Binomial(n, p)."""
    if x < 0:
        return 0.0
    if x >= n or p <= 0.0:
        return 1.0
    if p >= 1.0:
        return 0.0
    lp, lq = math.log(p), math.log1p(-p)
    base = math.lgamma(n + 1)
    total = 0.0
    for k in range(x + 1):
        total += math.exp(base - math.lgamma(k + 1) - math.lgamma(n - k + 1) + k * lp + (n - k) * lq)
    return min(total, 1.0)


def cp_upper(failures: int, n: int, confidence: float = 0.95) -> float:
    """One-sided Clopper-Pearson upper confidence bound on a failure rate."""
    if n <= 0 or failures < 0 or failures > n:
        raise ValueError(f"invalid count: {failures} failures in {n}")
    alpha = 1.0 - confidence
    if failures == n:
        return 1.0
    if failures == 0:
        return 1.0 - alpha ** (1.0 / n)
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if binom_cdf(failures, n, mid) > alpha:
            lo = mid
        else:
            hi = mid
    return hi


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_yaml(path: Path):
    try:
        with open(path, encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    except OSError as exc:
        raise GateError(f"cannot read {path}: {exc}") from exc
    except yaml.YAMLError as exc:
        raise GateError(f"{path} is not valid YAML: {exc}") from exc


def to_date(value):
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_tree(path: Path) -> tuple[str, int]:
    """Digest of every file under a directory (relative path and content), and the file count."""
    h = hashlib.sha256()
    count = 0
    for f in sorted(p for p in path.rglob("*") if p.is_file()):
        h.update(f.relative_to(path).as_posix().encode())
        h.update(sha256_file(f).encode())
        count += 1
    return h.hexdigest(), count


def is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def passes(value: float, threshold: float, direction: str) -> bool:
    eps = 1e-9
    return value >= threshold - eps if direction == "min" else value <= threshold + eps


def as_fraction(metric: dict, tier: str):
    value = (metric.get("thresholds") or {}).get(tier)
    if value is None:
        return None
    return value / 100 if metric.get("unit", "percent") == "percent" else value


def suite_min(eval_type: dict | None, tier: str):
    """(minimum, required, present) for an eval type at a tier."""
    if not eval_type:
        return None, False, False
    s = (eval_type.get("suite") or {}).get(tier)
    if s is None:
        return None, False, False
    if isinstance(s, int):
        return s, True, True
    return s.get("min"), s.get("required", True), True


def fmt(value, digits: int = 4) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.{digits}g}"
    return str(value)


def pct(value) -> str:
    return "" if value is None else f"{value * 100:.2f}%"


def cell(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


# ---------------------------------------------------------------------------
# Framework
# ---------------------------------------------------------------------------

class Framework:
    def __init__(self, root: Path):
        self.root = root
        cdir, pdir = root / "controls", root / "policy"
        if not cdir.is_dir() or not (pdir / "tiers.yaml").is_file() or not (pdir / "thresholds.yaml").is_file():
            raise GateError(f"{root} does not hold the framework's controls/ and policy/ (tiers.yaml, thresholds.yaml)")
        self.controls: dict[str, dict] = {}
        files = sorted(cdir.glob("stage-*.yaml"))
        if not files:
            raise GateError(f"no controls/stage-*.yaml files under {root}")
        for f in files:
            doc = load_yaml(f) or {}
            for c in doc.get("controls") or []:
                if isinstance(c, dict) and c.get("id"):
                    self.controls[c["id"]] = c
        tiers_doc = load_yaml(pdir / "tiers.yaml") or {}
        self.tiers = tiers_doc.get("tiers") or {}
        self.thresholds = load_yaml(pdir / "thresholds.yaml") or {}
        self.metrics = {m["id"]: m for m in self.thresholds.get("metrics") or [] if isinstance(m, dict) and m.get("id")}
        self.eval_types = {e["id"]: e for e in self.thresholds.get("eval_types") or [] if isinstance(e, dict) and e.get("id")}
        self.pass_rule = self.thresholds.get("pass_rule") or {}
        wf = root / WORKFLOW_DOC
        self.workflow_text = wf.read_text(encoding="utf-8") if wf.is_file() else None

        h = hashlib.sha256()
        for f in files + sorted(pdir.glob("*.yaml")) + ([wf] if wf.is_file() else []):
            h.update(f.relative_to(root).as_posix().encode())
            h.update(sha256_file(f).encode())
        self.digest = h.hexdigest()

    def documented_non_waivable(self):
        """Control IDs listed under **Non-waivable.** in the governance workflow, and whether a
        DPIA line is present. None when the document or the section is missing."""
        if not self.workflow_text:
            return None
        lines = self.workflow_text.splitlines()
        start = next((i for i, line in enumerate(lines) if "**Non-waivable.**" in line), None)
        if start is None:
            return None
        ids, dpia, in_list = set(), False, False
        for line in lines[start + 1:]:
            stripped = line.strip()
            if stripped.startswith(("- ", "* ")):
                in_list = True
                ids.update(CONTROL_ID_RE.findall(stripped))
                dpia = dpia or "DPIA" in stripped
            elif stripped == "" and not in_list:
                continue
            else:
                break
        return ids, dpia


# ---------------------------------------------------------------------------
# The gate
# ---------------------------------------------------------------------------

class Gate:
    def __init__(self, gov_path: Path, framework_override: Path | None, framework_ref: str | None,
                 phase: str, today: dt.date):
        self.gov_path = gov_path.resolve()
        self.base = self.gov_path.parent
        self.phase = phase
        self.today = today
        self.failures: list[dict] = []
        self.warnings: list[str] = []
        self.excepted: list[dict] = []
        self.exception_used: set[str] = set()
        self.required: set[str] = set()
        self.valid_exceptions: dict[str, list[dict]] = {}
        self.exception_rows: list[dict] = []
        self.non_waivable = dict(NON_WAIVABLE)

        if not self.gov_path.is_file():
            raise GateError(f"governance file not found: {gov_path}")
        gov = load_yaml(self.gov_path)
        if not isinstance(gov, dict):
            raise GateError(f"{gov_path} must be a mapping")
        self.gov = gov

        fw_cfg = gov.get("framework") or {}
        if not isinstance(fw_cfg, dict):
            raise GateError("framework must be a mapping with path and ref")
        if framework_override is not None:
            fw_root = framework_override
        elif fw_cfg.get("path"):
            fw_root = self.base / str(fw_cfg["path"])
        else:
            fw_root = Path(__file__).resolve().parents[2]   # the repository this gate ships in
        self.fw = Framework(fw_root.resolve())
        # --framework-ref describes the --framework directory or the gate's own repository; a
        # framework.path from governance.yaml carries its own framework.ref.
        from_gov = framework_override is None and bool(fw_cfg.get("path"))
        self.fw_ref = fw_cfg.get("ref") if from_gov else (framework_ref or fw_cfg.get("ref"))

        system = gov.get("system")
        if not isinstance(system, dict):
            raise GateError("governance.yaml needs a system block (id, tier, types)")
        self.system = system
        self.system_id = system.get("id")
        if not self.system_id:
            raise GateError("system.id is missing")
        self.tier = system.get("tier")
        if self.tier not in TIERS:
            raise GateError(f"system.tier is {self.tier!r}; expected one of {', '.join(TIERS)}")
        if self.tier not in self.fw.tiers:
            raise GateError(f"policy/tiers.yaml has no entry for {self.tier}")
        raw_types = system.get("types") or []
        if not isinstance(raw_types, list):
            raise GateError("system.types must be a list")
        unknown = sorted(set(map(str, raw_types)) - SYSTEM_TYPES)
        if unknown:
            raise GateError(f"unknown system types {unknown}; use {sorted(SYSTEM_TYPES)}")
        types = set(raw_types)
        for t in list(types):
            types |= IMPLIED_TYPES.get(t, set())
        self.declared_types = sorted(set(raw_types))
        self.types = types
        dpia_flag = system.get("dpia_legally_required")
        self.dpia_legally_required = ("personal-data" in types) if dpia_flag is None else bool(dpia_flag)

        known = {"schema_version", "system", "framework", "evidence", "eval_report", "not_applicable", "exceptions"}
        for key in sorted(set(gov) - known):
            self.warn(f"governance.yaml: unknown key '{key}' ignored")

    # -- reporting -----------------------------------------------------------

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def fail(self, control: str | None, msg: str) -> None:
        self.failures.append({"control": control, "message": msg})

    def finding(self, control: str, msg: str, waivable: bool = True, metric: str | None = None) -> str:
        """A check failed against a control. Waivable findings are covered by a valid exception;
        findings against a control that is not required at this tier are warnings.
        Returns 'fail', 'excepted' or 'not-gated'."""
        if waivable:
            exc = self.covering_exception(control, metric)
            if exc:
                self.excepted.append({"control": control, "exception": exc["id"], "message": msg})
                self.exception_used.add(exc["id"])
                return "excepted"
            if control not in self.required:
                self.warn(f"{control} (not required at {self.tier}, not gated): {msg}")
                return "not-gated"
        self.fail(control, msg)
        return "fail"

    # -- applicability -------------------------------------------------------

    def applicability(self, control: dict):
        """'required', 'recommended' or None for this system, from tiers and system types."""
        cid = control["id"]
        at = control.get("applies_to") or {}
        systems = at.get("systems") or []
        req_tiers = at.get("tiers") or []
        rec_tiers = at.get("recommended") or []
        if "all" in systems:
            matching = None
        else:
            matching = [s for s in systems if s in self.types]
            if not matching:
                return None
        if self.tier in req_tiers:
            refine = TIER_BY_SYSTEM.get(cid)
            if refine and matching is not None and not any(self.tier in refine.get(s, req_tiers) for s in matching):
                return None
            return "required"
        if self.tier in rec_tiers:
            return "recommended"
        return None

    @staticmethod
    def in_scope(control: dict) -> bool:
        return control.get("stage") in GATED_STAGES or control["id"] in PRE_GO_LIVE_STAGE8

    def non_waivable_kind(self, cid: str):
        kind = self.non_waivable.get(cid)
        if kind == "dpia":
            return "full" if self.dpia_legally_required else None
        return kind

    # -- exceptions ----------------------------------------------------------

    def load_exceptions(self) -> None:
        raw = self.gov.get("exceptions") or []
        if not isinstance(raw, list):
            self.fail(None, "exceptions must be a list")
            return
        tier_index = TIERS.index(self.tier)
        approver = ((self.fw.tiers[self.tier].get("approvers") or {}).get("exception") or {}).get("accountable")
        renewal_tier = TIERS[max(tier_index - 1, 0)]
        renewal_approver = ((self.fw.tiers.get(renewal_tier, {}).get("approvers") or {}).get("exception") or {}).get("accountable")
        seen = set()
        for i, exc in enumerate(raw):
            if not isinstance(exc, dict):
                self.fail(None, f"exceptions[{i}] must be a mapping")
                continue
            eid = str(exc.get("id") or f"exceptions[{i}]")
            row = {"id": eid, "control": exc.get("control"), "approver": exc.get("approver"),
                   "start": str(exc.get("start") or ""), "expiry": str(exc.get("expiry") or ""),
                   "renewal": bool(exc.get("renewal")), "status": "valid", "problems": []}
            self.exception_rows.append(row)
            problems = row["problems"]
            if eid in seen:
                problems.append("duplicate exception id")
            seen.add(eid)
            if not EXC_ID_RE.match(eid):
                self.warn(f"exception {eid}: id is not in the EXC-YYYY-NNN form used by the exception register")
            for field in ("id", "control", "approver", "expiry"):
                if not exc.get(field):
                    problems.append(f"missing {field}")
            cid = exc.get("control")
            if cid and cid not in self.fw.controls:
                problems.append(f"control {cid} is not defined in controls/")
            kind = self.non_waivable_kind(cid) if cid else None
            if kind == "full":
                problems.append(f"{cid} is non-waivable and cannot be excepted")
            expiry = to_date(exc.get("expiry"))
            start = to_date(exc.get("start")) if exc.get("start") else None
            if exc.get("expiry") and expiry is None:
                problems.append("expiry is not a YYYY-MM-DD date")
            if exc.get("start") and start is None:
                problems.append("start is not a YYYY-MM-DD date")
            if expiry and expiry < self.today:
                problems.append(f"expired on {expiry.isoformat()}")
                row["status"] = "expired"
            if start and expiry:
                if expiry < start:
                    problems.append("expiry is before start")
                elif (expiry - start).days > MAX_EXCEPTION_DAYS:
                    problems.append(f"runs {(expiry - start).days} days; the maximum is {MAX_EXCEPTION_DAYS}")
            elif expiry and not start:
                self.warn(f"exception {eid}: no start date, so the {MAX_EXCEPTION_DAYS}-day limit could not be checked")
            if exc.get("approver"):
                expected = renewal_approver if row["renewal"] else approver
                if exc["approver"] != expected:
                    what = f"a renewal is approved one level higher ({renewal_tier})" if row["renewal"] else f"the {self.tier} exception approver"
                    problems.append(f"approved by '{exc['approver']}'; {what} is '{expected}' (policy/tiers.yaml)")
            if problems:
                if row["status"] == "valid":
                    row["status"] = "invalid"
                self.fail(cid, f"exception {eid}: " + "; ".join(problems))
                continue
            if cid == "SR-002":
                row["note"] = "covers open High findings only; open Critical findings cannot be excepted"
            scope = exc.get("metrics")
            if scope is not None and not (isinstance(scope, list) and all(isinstance(m, str) for m in scope)):
                self.fail(cid, f"exception {eid}: metrics must be a list of metric ids")
                row["status"] = "invalid"
                continue
            row["metrics"] = scope
            self.valid_exceptions.setdefault(cid, []).append(dict(exc, id=eid))

    def covering_exception(self, control: str, metric: str | None):
        for exc in self.valid_exceptions.get(control, []):
            scope = exc.get("metrics")
            if scope is None or (metric is not None and metric in scope):
                return exc
        return None

    # -- evidence ------------------------------------------------------------

    def evidence_paths(self) -> dict[str, list[str]]:
        raw = self.gov.get("evidence") or {}
        if not isinstance(raw, dict):
            self.fail(None, "evidence must map control IDs to a path or a list of paths")
            return {}
        out = {}
        for cid, value in raw.items():
            cid = str(cid)
            if cid not in self.fw.controls:
                self.fail(cid, f"evidence is listed for {cid}, which is not defined in controls/")
                continue
            paths = [value] if isinstance(value, str) else value
            if not isinstance(paths, list) or not all(isinstance(p, str) and p for p in paths):
                self.fail(cid, f"evidence for {cid} must be a path or a list of paths")
                continue
            out[cid] = paths
        return out

    def check_paths(self, cid: str, paths: list[str]):
        """(present entries, problems) for the evidence paths of one control."""
        present, problems = [], []
        for p in paths:
            if "://" in p:
                problems.append(f"{p} is a URL; the gate runs offline, so commit a pointer file with the record ID, location and SHA-256")
                continue
            if Path(p).is_absolute():
                problems.append(f"{p} is absolute; use a path relative to governance.yaml")
                continue
            full = (self.base / p).resolve()
            try:
                full.relative_to(self.base)
            except ValueError:
                self.warn(f"{cid}: evidence {p} is outside the governance.yaml directory")
            if full.is_file():
                size = full.stat().st_size
                if size == 0:
                    problems.append(f"{p} is empty")
                else:
                    present.append({"path": p, "sha256": sha256_file(full), "bytes": size})
            elif full.is_dir():
                digest, count = sha256_tree(full)
                if count == 0:
                    problems.append(f"{p} is an empty directory")
                else:
                    present.append({"path": p, "sha256": digest, "files": count})
            else:
                problems.append(f"{p} not found")
        return present, problems

    # -- main run ------------------------------------------------------------

    def run(self) -> dict:
        if "agentic" in self.types and self.tier in ("T3", "T4"):
            self.fail(None, "every agentic system is at least T2 (override item 6 in the GenAI risk matrix); "
                            f"system.tier is {self.tier}")
        self.check_non_waivable_list()
        self.load_exceptions()

        controls = sorted(self.fw.controls.values(), key=lambda c: (c.get("stage", 0), c["id"]))
        applic = {c["id"]: self.applicability(c) for c in controls}
        in_scope = [c for c in controls if self.in_scope(c) and applic[c["id"]]]

        na_raw = self.gov.get("not_applicable") or []
        na: dict[str, str] = {}
        if not isinstance(na_raw, list):
            self.fail(None, "not_applicable must be a list of {control, reason}")
            na_raw = []
        for i, item in enumerate(na_raw):
            if not isinstance(item, dict) or not item.get("control") or not str(item.get("reason") or "").strip():
                self.fail(None, f"not_applicable[{i}] needs a control and a reason")
                continue
            na[str(item["control"])] = str(item["reason"]).strip()

        # Required controls before not-applicable claims; used for NA_BLOCKED_BY.
        required_raw = {c["id"] for c in in_scope if applic[c["id"]] == "required"}
        self.required: set[str] = set()
        accepted_na: dict[str, str] = {}
        for cid, reason in na.items():
            if cid not in self.fw.controls:
                self.fail(cid, f"not_applicable names {cid}, which is not defined in controls/")
                continue
            control = self.fw.controls[cid]
            if not self.in_scope(control) or applic[cid] is None:
                self.warn(f"{cid} is claimed not applicable but does not apply to a {self.tier} system with these types; claim ignored")
                continue
            if applic[cid] == "recommended":
                accepted_na[cid] = reason
                continue
            if cid not in CONDITIONAL:
                self.fail(cid, f"{cid} cannot be claimed not applicable: it applies to every {self.tier} system with these types "
                               f"('{control['applies_to'].get('text', '')}')")
                continue
            if self.non_waivable_kind(cid) == "full":
                self.fail(cid, f"{cid} is non-waivable and cannot be claimed not applicable")
                continue
            blocker = NA_BLOCKED_BY.get(cid)
            if blocker and blocker in required_raw:
                self.fail(cid, f"{cid} cannot be claimed not applicable while {blocker} applies")
                continue
            accepted_na[cid] = reason
        self.required = required_raw - set(accepted_na)

        evidence = self.evidence_paths()
        rows, pack = [], []
        for c in in_scope:
            cid, level = c["id"], applic[c["id"]]
            row = {"id": cid, "title": c.get("title", ""), "stage": c.get("stage"), "owner": c.get("owner"),
                   "applies_to": (c.get("applies_to") or {}).get("text", ""), "level": level, "evidence": []}
            rows.append(row)
            if cid in accepted_na:
                row["status"] = "not-applicable"
                row["reason"] = accepted_na[cid]
                row["condition"] = CONDITIONAL.get(cid, "recommended only at this tier")
                continue
            present, problems = self.check_paths(cid, evidence.get(cid, []))
            row["evidence"] = present
            pack.extend({"control": cid, **p} for p in present)
            if not evidence.get(cid):
                problems = ["no evidence listed in governance.yaml"]
            if level == "recommended":
                row["status"] = "recommended-evidenced" if present and not problems else "recommended"
                continue
            if not problems:
                row["status"] = "evidenced"
                continue
            row["problems"] = problems
            if cid == SIGN_OFF_CONTROL and self.phase == "pre-approval":
                row["status"] = "pending-sign-off"
                continue
            kind = self.non_waivable_kind(cid)
            if kind in ("full", "critical"):
                row["status"] = "missing"
                why = "zero open Critical findings cannot be shown without it" if kind == "critical" else "it is non-waivable"
                self.fail(cid, f"{cid} evidence missing ({'; '.join(problems)}); no exception can cover it: {why}")
                continue
            exc = self.covering_exception(cid, None)
            if exc:
                row["status"] = "excepted"
                row["exception"] = exc["id"]
                self.exception_used.add(exc["id"])
                self.excepted.append({"control": cid, "exception": exc["id"], "message": "; ".join(problems)})
                continue
            row["status"] = "missing"
            self.fail(cid, f"{cid} evidence missing: {'; '.join(problems)}")

        in_scope_ids = {c["id"] for c in in_scope}
        for cid in sorted(set(evidence) - in_scope_ids):
            if cid in self.fw.controls:
                self.warn(f"evidence listed for {cid}, which the gate does not check for this system (not applicable or outside the pre-deployment stages)")

        evaluation = self.check_evaluation()

        for exc_list in self.valid_exceptions.values():
            for exc in exc_list:
                if exc["id"] not in self.exception_used:
                    self.warn(f"exception {exc['id']} ({exc.get('control')}) covers nothing that fails; close it in the exception register")
        for row in self.exception_rows:
            if row["status"] == "valid":
                row["used"] = row["id"] in self.exception_used

        pack_hash = hashlib.sha256(json.dumps(sorted((p["control"], p["path"], p["sha256"]) for p in pack)).encode()).hexdigest()
        return {
            "gate": {"name": "governance-gate", "version": GATE_VERSION},
            "result": "fail" if self.failures else "pass",
            "phase": self.phase,
            "as_of": self.today.isoformat(),
            "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "system": {"id": self.system_id, "name": self.system.get("name"), "tier": self.tier,
                       "types": self.declared_types, "effective_types": sorted(self.types),
                       "dpia_legally_required": self.dpia_legally_required},
            "governance_file": {"path": self.gov_path.name, "sha256": sha256_file(self.gov_path)},
            "framework": {"path": os.path.relpath(self.fw.root, self.base), "ref": self.fw_ref, "digest": self.fw.digest},
            "evidence_pack_sha256": pack_hash,
            "controls": rows,
            "evaluation": evaluation,
            "exceptions": self.exception_rows,
            "excepted_findings": self.excepted,
            "failures": self.failures,
            "warnings": self.warnings,
        }

    def check_non_waivable_list(self) -> None:
        documented = self.fw.documented_non_waivable()
        if documented is None:
            self.warn(f"could not read the non-waivable list from {WORKFLOW_DOC}; using the list built into the gate")
            return
        ids, dpia = documented
        built_in = {cid for cid in self.non_waivable if cid != "RA-005"}
        for cid in sorted(ids - built_in):
            self.non_waivable[cid] = "full"
            self.warn(f"{WORKFLOW_DOC} lists {cid} as non-waivable; the gate treats it as fully non-waivable")
        for cid in sorted(built_in - ids):
            self.warn(f"the gate treats {cid} as non-waivable but {WORKFLOW_DOC} no longer lists it; update gate.py")
        if not dpia:
            self.warn(f"{WORKFLOW_DOC} no longer lists the DPIA as non-waivable; update gate.py")

    # -- evaluation report ---------------------------------------------------

    def check_evaluation(self) -> dict:
        out: dict = {"report": None, "metrics": [], "segments": [], "red_team": None, "security_findings": None}
        path = self.gov.get("eval_report")
        report = None
        if not path:
            self.finding("EV-001", "governance.yaml names no eval_report")
        else:
            full = (self.base / str(path)).resolve()
            out["report"] = str(path)
            if not full.is_file():
                self.finding("EV-001", f"eval report {path} not found")
            else:
                out["report_sha256"] = sha256_file(full)
                try:
                    report = json.loads(full.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError) as exc:
                    self.finding("EV-001", f"eval report {path} is not valid JSON: {exc}")
                if report is not None and not isinstance(report, dict):
                    self.finding("EV-001", f"eval report {path} must be a JSON object")
                    report = None
        if report is None:
            if "SR-002" in self.required:
                self.finding("SR-002", "no readable eval report, so zero open Critical findings cannot be shown", waivable=False)
            return out

        if report.get("system_id") != self.system_id:
            self.fail(None, f"eval report system_id {report.get('system_id')!r} does not match system.id {self.system_id!r}")
        if report.get("tier") is not None and report.get("tier") != self.tier:
            self.fail(None, f"eval report tier {report.get('tier')!r} does not match system.tier {self.tier}")
        out.update({k: report.get(k) for k in ("release", "evaluation_date") if k in report})

        rows = report.get("metrics") or []
        if not isinstance(rows, list):
            self.finding("EV-001", "eval report metrics must be a list")
            rows = []
        effective_thresholds: dict[str, float] = {}
        recorded = set()
        for i, r in enumerate(rows):
            if not isinstance(r, dict) or not r.get("id"):
                self.finding("EV-001", f"eval report metrics[{i}] needs an id")
                continue
            recorded.add(r["id"])
            result = self.check_metric(r, effective_thresholds)
            out["metrics"].append(result)

        if "genai" in self.types:
            self.check_required_metrics(recorded)
        out["segments"] = self.check_segments(report, effective_thresholds)
        self.check_human_evaluation(report, rows)
        out["red_team"] = self.check_red_team(report)
        out["security_findings"] = self.check_security_findings(report)
        return out

    def metric_control(self, fw_metric: dict | None) -> str:
        if fw_metric and fw_metric.get("eval_type"):
            ctl = (self.fw.eval_types.get(fw_metric["eval_type"]) or {}).get("control")
            if ctl:
                return ctl
        return "EV-001"

    def default_ceiling(self, fw_metric: dict):
        ceiling = fw_metric.get("default_ceiling") or {}
        if self.tier not in (ceiling.get("tiers") or []):
            return None, None
        audience = "customer_facing" if "customer-facing" in self.types else "internal"
        value = ceiling.get(audience)
        return (value / 100 if value is not None else None), audience.replace("_", "-")

    def check_metric(self, r: dict, effective_thresholds: dict) -> dict:
        tier = self.tier
        mid = r["id"]
        attr = r.get("attribute")
        label = f"{mid} ({attr})" if attr else mid
        fw = self.fw.metrics.get(mid)
        control = self.metric_control(fw)
        direction = fw.get("direction", "min") if fw else r.get("direction", "min")
        et = fw.get("eval_type") if fw else None
        conf = self.fw.pass_rule.get("confidence", 0.95)
        rule = (self.fw.pass_rule.get("tiers") or {}).get(tier, "point-estimate")
        if fw:
            kind = fw.get("kind")
        else:
            # Use-case metrics: the risk assessment states the kind and whether the metric gates on
            # the bound or the point estimate (evaluation-governance.md "Statistical Pass Rule").
            kind = r.get("kind")
            if r.get("gate") != "bound":
                rule = "point-estimate"
        if kind not in ("proportion", "mean"):
            rule = "point-estimate"
        res = {"id": mid, "attribute": attr, "control": control, "n": r.get("n"), "failures": r.get("failures"),
               "value": r.get("value"), "rule": rule, "threshold": None, "bound": None, "result": "pass", "detail": ""}

        def bad(msg: str) -> None:
            outcome = self.finding(control, f"{label}: {msg}", metric=mid)
            rank = {"pass": 0, "reported": 0, "not-gated": 1, "excepted": 2, "fail": 3}
            if rank[outcome] > rank.get(res["result"], 0):
                res["result"] = outcome
            res["detail"] = (res["detail"] + "; " if res["detail"] else "") + msg

        fw_thr = as_fraction(fw, tier) if fw else None
        rep_thr = r.get("threshold")
        if rep_thr is not None and not is_number(rep_thr):
            bad("threshold must be a number (a fraction, 0.01 means 1%)")
            rep_thr = None
        if fw and fw_thr is None:
            limit, audience = self.default_ceiling(fw)
            if limit is not None:
                if rep_thr is None:
                    fw_thr = limit
                elif not passes(rep_thr, limit, direction):
                    bad(f"threshold {fmt(rep_thr)} is looser than the framework default ceiling {fmt(limit)} for {audience} systems")
        if fw and fw_thr is not None and rep_thr is not None and not passes(rep_thr, fw_thr, direction):
            bad(f"threshold {fmt(rep_thr)} is looser than the {tier} threshold {fmt(fw_thr)} in policy/thresholds.yaml")
        effective = rep_thr if rep_thr is not None else fw_thr
        res["threshold"] = effective
        if effective is None:
            text = ((fw or {}).get("tier_text") or {}).get(tier)
            if fw and text not in (None, "N/A") and control in self.required:
                bad("needs a threshold from the risk assessment (use-case specific at this tier)")
            else:
                res["result"] = "reported"
                res["detail"] = "no threshold at this tier; reported, not gated"
            return res
        if not attr:
            effective_thresholds.setdefault(mid, effective)

        n = r.get("n")
        if et:
            s_min, _, _ = suite_min(self.fw.eval_types.get(et), tier)
            if s_min is not None:
                if not isinstance(n, int) or isinstance(n, bool):
                    bad(f"record n; the {tier} {et} suite minimum is {s_min}")
                    return res
                if n < s_min:
                    bad(f"n {n} is below the {tier} {et} suite minimum of {s_min}")

        if rule == "confidence-bound" and kind == "proportion":
            f = r.get("failures")
            if not (isinstance(n, int) and n > 0 and isinstance(f, int) and 0 <= f <= n):
                bad(f"record n and failures; the {tier} pass rule judges the {conf:.0%} confidence bound")
                return res
            from_counts = (1 - f / n) if direction == "min" else f / n
            if is_number(r.get("value")) and abs(r["value"] - from_counts) > 0.005 + 1e-9:
                bad(f"value {fmt(r['value'])} does not match {f} failures in {n}")
            if res["value"] is None:
                res["value"] = from_counts
            cap = (1 - effective) if direction == "min" else effective
            if cap <= 1e-12:
                res["detail"] = "any failure fails"
                if f != 0:
                    bad(f"{f} of {n} cases failed; any failure fails at this threshold")
                return res
            ub = cp_upper(f, n, conf)
            res["bound"] = ub
            res["bound_label"] = "failure-rate upper bound"
            if ub > cap + 1e-9:
                point_ok = f / n <= cap + 1e-9
                bad(f"failure-rate upper bound {pct(ub)} ({f} failures in {n}) exceeds the {pct(cap)} cap"
                    + (f" although the point estimate {pct(f / n)} is within it" if point_ok else ""))
            return res

        if rule == "confidence-bound" and kind == "mean":
            lb, method, value = r.get("lower_bound"), r.get("interval_method"), r.get("value")
            if not (isinstance(n, int) and n > 0 and is_number(lb)):
                bad(f"record n and lower_bound; the {tier} pass rule judges the {conf:.0%} confidence bound")
                return res
            methods = self.fw.pass_rule.get("mean_methods") or {}
            t_min = (methods.get("t-interval") or {}).get("min_n", 100)
            if method not in methods:
                bad(f"interval_method must be one of {', '.join(methods)}")
            elif method == "t-interval" and n < t_min:
                bad(f"a t-interval needs n of at least {t_min}; use the bootstrap")
            if direction != "min":
                bad("a lower bound applies only to higher-is-better mean metrics")
                return res
            if is_number(value) and lb > value + 1e-9:
                bad(f"lower_bound {fmt(lb)} is above the value {fmt(value)}")
            res["bound"] = lb
            res["bound_label"] = "lower bound"
            if not passes(lb, effective, "min"):
                point = f" although the point estimate {fmt(value)} meets it" if is_number(value) and passes(value, effective, "min") else ""
                bad(f"lower bound {fmt(lb)} is below the threshold {fmt(effective)}{point}")
            return res

        value = r.get("value")
        if value is None and kind == "proportion" and isinstance(n, int) and n > 0 and isinstance(r.get("failures"), int):
            value = (1 - r["failures"] / n) if direction == "min" else r["failures"] / n
            res["value"] = value
        if not is_number(value):
            bad("no value recorded")
            return res
        if not passes(value, effective, direction):
            bad(f"value {fmt(value)} misses the threshold {fmt(effective)} ({'at least' if direction == 'min' else 'at most'})")
        return res

    def check_required_metrics(self, recorded: set) -> None:
        tier = self.tier
        for mid, fw in self.fw.metrics.items():
            et = fw.get("eval_type")
            if not et or mid in recorded:
                continue
            control = self.metric_control(fw)
            if control not in self.required:
                continue
            _, required, present = suite_min(self.fw.eval_types.get(et), tier)
            if not present or not required:
                continue
            scope = fw.get("applies_to")
            if (scope == "rag" and "rag" not in self.types) or (scope == "agent" and "agentic" not in self.types):
                continue
            limit, _ = self.default_ceiling(fw)
            text = (fw.get("tier_text") or {}).get(tier)
            if as_fraction(fw, tier) is None and limit is None and text in (None, "N/A"):
                continue
            self.finding(control, f"{mid} is not in the eval report; {control} requires it at {tier}", metric=mid)

    def check_segments(self, report: dict, effective_thresholds: dict) -> list:
        seg_cfg = self.fw.pass_rule.get("segments") or {}
        segments = report.get("segments") or []
        results = []
        if self.tier not in (seg_cfg.get("tiers") or []) or not isinstance(segments, list):
            return results
        min_cases = seg_cfg.get("min_cases", 100)
        for i, seg in enumerate(segments):
            if not isinstance(seg, dict):
                continue
            name, n = seg.get("segment", f"segments[{i}]"), seg.get("n")
            entry = {"segment": name, "n": n, "gated": isinstance(n, int) and n >= min_cases, "result": "pass"}
            results.append(entry)
            if not isinstance(n, int):
                entry["result"] = "fail"
                self.finding("EV-001", f"segment '{name}' has no case count n")
                continue
            if n < min_cases:
                entry["result"] = "reported"
                continue
            for mid, value in (seg.get("results") or {}).items():
                fw = self.fw.metrics.get(mid)
                thr = effective_thresholds.get(mid)
                if fw is None or thr is None or not is_number(value):
                    continue
                if not passes(value, thr, fw.get("direction", "min")):
                    entry["result"] = "fail"
                    self.finding(self.metric_control(fw), f"segment '{name}' (n {n}) {mid} {fmt(value)} misses the threshold {fmt(thr)}", metric=mid)
        return results

    def check_human_evaluation(self, report: dict, rows: list) -> None:
        cfg = self.fw.pass_rule.get("human_evaluation") or {}
        if self.tier not in (cfg.get("tiers") or []):
            return
        he = report.get("human_evaluation")
        human = any(isinstance(r, dict) and r.get("method") in ("human-eval", "hybrid") for r in rows)
        if he is None:
            if human:
                self.warn("human-rated metrics but no human_evaluation block; double-rating share and agreement not checked")
            return
        if not isinstance(he, dict) or not is_number(he.get("double_rated_share")) or not is_number(he.get("agreement")):
            self.finding("EV-001", "human_evaluation needs double_rated_share and agreement")
            return
        share_min = cfg.get("double_rated_share", 20) / 100
        agree_min = cfg.get("min_agreement", 0.6)
        if he["double_rated_share"] < share_min - 1e-9:
            self.finding("EV-001", f"human_evaluation double_rated_share {fmt(he['double_rated_share'])} is below {fmt(share_min)}")
        if he["agreement"] < agree_min - 1e-9:
            self.finding("EV-001", f"human_evaluation agreement {fmt(he['agreement'])} is below {fmt(agree_min)}; human-rated results are not accepted")

    def check_red_team(self, report: dict):
        if "SR-001" not in self.required:
            return None
        rt = report.get("red_team")
        tier_rt = self.fw.tiers[self.tier].get("red_team") or {}
        min_cases, depth = tier_rt.get("min_cases"), str(tier_rt.get("depth") or "")
        if not isinstance(rt, dict):
            self.finding("SR-001", "eval report has no red_team block (report, cases, manual_testing)")
            return None
        cases = rt.get("cases")
        out = {"report": rt.get("report"), "cases": cases, "min_cases": min_cases, "depth": depth, "result": "pass"}
        if not isinstance(cases, int) or isinstance(cases, bool):
            out["result"] = "fail"
            self.finding("SR-001", "red_team.cases is missing")
        elif min_cases is not None and cases < min_cases:
            out["result"] = "fail"
            self.finding("SR-001", f"red-team ran {cases} cases; the {self.tier} depth is {depth}")
        if "manual" in depth.lower() and rt.get("manual_testing") is not True:
            out["result"] = "fail"
            self.finding("SR-001", f"the {self.tier} red-team depth ({depth}) needs manual testing; set red_team.manual_testing")
        return out

    def check_security_findings(self, report: dict):
        if "SR-002" not in self.required:
            return None
        sf = report.get("security_findings")
        if not isinstance(sf, dict) or not isinstance(sf.get("critical_open"), int):
            self.finding("SR-002", "eval report has no security_findings.critical_open, so zero open Critical findings cannot be shown", waivable=False)
            return None
        out = {"critical_open": sf["critical_open"], "high_open": sf.get("high_open"), "result": "pass"}
        if sf["critical_open"] > 0:
            out["result"] = "fail"
            self.finding("SR-002", f"{sf['critical_open']} open Critical finding(s); this cannot be excepted", waivable=False)
        high = sf.get("high_open")
        if not isinstance(high, int):
            out["result"] = "fail"
            self.finding("SR-002", "security_findings.high_open is missing")
        elif high > 0:
            out["result"] = self.finding("SR-002", f"{high} open High finding(s) with no remediation", metric="high")
        return out


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

STATUS_LABEL = {"evidenced": "Evidenced", "excepted": "Excepted", "not-applicable": "Not applicable (claimed)",
                "missing": "**Missing**", "pending-sign-off": "Pending sign-off", "recommended": "Recommended (no evidence)",
                "recommended-evidenced": "Recommended (evidenced)"}


def render_markdown(res: dict) -> str:
    sysd = res["system"]
    controls = res["controls"]
    gated = [c for c in controls if c["level"] == "required"]
    count = lambda status: sum(1 for c in gated if c.get("status") == status)  # noqa: E731
    metrics = (res.get("evaluation") or {}).get("metrics") or []
    failing_metrics = sum(1 for m in metrics if m["result"] == "fail")
    lines = [f"## AI governance gate: {res['result'].upper()}", ""]
    name = f" ({sysd['name']})" if sysd.get("name") else ""
    lines.append(f"System `{sysd['id']}`{name}, tier {sysd['tier']}, types: {', '.join(sysd['types']) or 'none'}. "
                 f"Phase: {res['phase']}. As of {res['as_of']}. Gate {res['gate']['version']}.")
    lines += ["", "| Check | Count |", "|---|---|",
              f"| Controls required for this system | {len(gated)} |",
              f"| Evidenced | {count('evidenced')} |",
              f"| Not applicable (claimed, reason recorded) | {count('not-applicable')} |",
              f"| Covered by an exception | {count('excepted')} |",
              f"| Pending sign-off | {count('pending-sign-off')} |",
              f"| Missing | {count('missing')} |",
              f"| Metrics checked | {len(metrics)} ({failing_metrics} failing) |",
              f"| Failures | {len(res['failures'])} |",
              f"| Warnings | {len(res['warnings'])} |", ""]
    if res["failures"]:
        lines += ["### Failures", ""]
        lines += [f"- {('**' + f['control'] + '**: ') if f['control'] else ''}{f['message']}" for f in res["failures"]]
        lines.append("")
    if res.get("excepted_findings"):
        lines += ["### Covered by exceptions", ""]
        lines += [f"- {e['control']} ({e['exception']}): {e['message']}" for e in res["excepted_findings"]]
        lines.append("")
    na = [c for c in controls if c.get("status") == "not-applicable"]
    if na:
        lines += ["### Not-applicable claims for the approver to confirm", "", "| Control | Condition | Reason given |", "|---|---|---|"]
        lines += [f"| {c['id']} | {cell(c['condition'])} | {cell(c['reason'])} |" for c in na]
        lines.append("")
    if metrics:
        lines += ["### Evaluation", "", "| Metric | Control | n | Failures | Value | Bound | Threshold | Rule | Result |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for m in metrics:
            label = f"{m['id']} ({m['attribute']})" if m.get("attribute") else m["id"]
            bound = ""
            if m.get("bound") is not None:
                bound = pct(m["bound"]) + " upper" if m.get("bound_label") == "failure-rate upper bound" else fmt(m["bound"]) + " lower"
            result = {"fail": "**FAIL**", "not-gated": "fail, not gated"}.get(m["result"], m["result"])
            lines.append(f"| {label} | {m['control']} | {fmt(m.get('n'))} | {fmt(m.get('failures'))} | {fmt(m.get('value'))} | "
                         f"{bound} | {fmt(m.get('threshold'))} | {m['rule']} | {result} |")
        lines.append("")
    ev = res.get("evaluation") or {}
    extra = []
    if ev.get("red_team"):
        rt = ev["red_team"]
        extra.append(f"- Red-team (SR-001): {rt.get('cases')} cases against a {sysd['tier']} minimum of {rt.get('min_cases')}: {rt['result']}")
    if ev.get("security_findings"):
        sf = ev["security_findings"]
        extra.append(f"- Open findings (SR-002): {sf.get('critical_open')} Critical, {sf.get('high_open')} High: {sf['result']}")
    segs = ev.get("segments") or []
    if segs:
        gated_segs = [s for s in segs if s.get("gated")]
        extra.append(f"- Segments: {len(gated_segs)} of {len(segs)} large enough to gate; "
                     f"{sum(1 for s in gated_segs if s['result'] == 'fail')} failing")
    if extra:
        lines += extra + [""]
    if res["exceptions"]:
        lines += ["### Exceptions", "", "| ID | Control | Approver | Expiry | Status |", "|---|---|---|---|---|"]
        for e in res["exceptions"]:
            status = e["status"] + ("" if e["status"] != "valid" else (", used" if e.get("used") else ", unused"))
            lines.append(f"| {cell(e['id'])} | {cell(e.get('control') or '')} | {cell(e.get('approver') or '')} | {e.get('expiry')} | {status} |")
        lines.append("")
    if res["warnings"]:
        lines += ["### Warnings", ""] + [f"- {w}" for w in res["warnings"]] + [""]
    lines += ["<details><summary>Controls checked</summary>", "", "| Control | Stage | Status | Evidence or reason |", "|---|---|---|---|"]
    for c in controls:
        detail = c.get("reason") or ", ".join(e["path"] for e in c.get("evidence") or []) or "; ".join(c.get("problems") or [])
        lines.append(f"| {c['id']} {cell(c['title'])} | {c['stage']} | {STATUS_LABEL.get(c.get('status'), c.get('status'))} | {cell(detail)} |")
    lines += ["", "</details>", ""]
    return "\n".join(lines)


def error_result(message: str, phase: str, today: dt.date) -> dict:
    return {"gate": {"name": "governance-gate", "version": GATE_VERSION}, "result": "fail", "phase": phase,
            "as_of": today.isoformat(), "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "failures": [{"control": None, "message": message}], "warnings": []}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Pre-deployment governance gate for one AI system.")
    ap.add_argument("governance", nargs="?", default="governance.yaml", help="path to the system's governance.yaml")
    ap.add_argument("--framework", help="directory holding the framework's controls/ and policy/ (overrides governance.yaml)")
    ap.add_argument("--framework-ref", help="framework version to record, such as a tag or commit")
    ap.add_argument("--output", default="gate-result.json", help="where to write the machine-readable result")
    ap.add_argument("--summary", help="also write the Markdown summary to this file")
    ap.add_argument("--phase", choices=("pre-deploy", "pre-approval"), default="pre-deploy",
                    help="pre-approval runs before sign-off, so the DA-002 approval record may be pending")
    ap.add_argument("--today", help="date to judge exception expiry against (YYYY-MM-DD); default is today (UTC)")
    ap.add_argument("--quiet", action="store_true", help="print only the one-line result")
    args = ap.parse_args(argv)

    today = to_date(args.today) if args.today else dt.datetime.now(dt.timezone.utc).date()
    if today is None:
        print(f"governance gate: error: --today {args.today!r} is not a YYYY-MM-DD date", file=sys.stderr)
        return 1
    try:
        gate = Gate(Path(args.governance), Path(args.framework).resolve() if args.framework else None,
                    args.framework_ref, args.phase, today)
        result = gate.run()
        summary = render_markdown(result)
    except GateError as exc:
        result = error_result(str(exc), args.phase, today)
        summary = f"## AI governance gate: FAIL\n\nThe gate could not run: {exc}\n"

    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.summary:
        Path(args.summary).write_text(summary, encoding="utf-8")
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write(summary + "\n")
    if not args.quiet:
        print(summary)
    print(f"governance gate: {result['result'].upper()} ({len(result['failures'])} failures, "
          f"{len(result.get('warnings') or [])} warnings); result written to {args.output}")
    return 0 if result["result"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
