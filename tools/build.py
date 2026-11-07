#!/usr/bin/env python3
"""Regenerate the Markdown tables that are built from controls/*.yaml and policy/*.yaml.

Each generated table sits between a pair of markers:

    <!-- BEGIN GENERATED: NAME. Edit SOURCE, then run python tools/build.py -->
    ...
    <!-- END GENERATED: NAME -->

Usage:
    python tools/build.py           rewrite every generated block in place
    python tools/build.py --check   exit 1 if any generated block is out of date
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TIERS = ("T1", "T2", "T3", "T4")

# A control ID is two capital letters, a hyphen and three digits. Tokens preceded by a
# letter, digit or hyphen (for example AR-2026-RA-001) are document IDs, not control IDs.
CONTROL_ID_RE = re.compile(r"(?<![A-Za-z0-9-])([A-Z]{2}-\d{3})(?![0-9])")

REGISTER = "framework/governance-operations/control-register.md"
ROLES_DOC = "framework/operating-model/roles-responsibilities.md"
CADENCE_DOC = "framework/operating-model/review-cadence.md"
AUDIT_TRAIL_DOC = "framework/compliance/prompt-audit-trail.md"
EVAL_DOC = "framework/llm-lifecycle/evaluation-governance.md"
ESCALATION_DOC = "framework/operating-model/escalation-paths.md"

# Regulatory mapping documents scanned for control IDs in the Traceability section.
MAPPING_DOCS = (
    ("EU AI Act", "framework/compliance/eu-ai-act-mapping.md"),
    ("NIST AI RMF", "framework/compliance/nist-ai-rmf-mapping.md"),
    ("ISO/IEC 42001", "framework/compliance/iso-42001-mapping.md"),
    ("Multi-jurisdictional", "framework/compliance/multi-jurisdictional-guide.md"),
)

LINE_OF_DEFENCE = {1: "First", 2: "Second", 3: "Third"}


class BuildError(Exception):
    pass


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load_yaml(rel: str):
    path = ROOT / rel
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise BuildError(f"{rel}: file not found")
    except yaml.YAMLError as exc:
        raise BuildError(f"{rel}: invalid YAML: {exc}")


def control_files() -> list[str]:
    return sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "controls").glob("*.yaml"))


def load_controls() -> list[dict]:
    """All controls in file order, each with a _file key naming its source file."""
    out = []
    for rel in control_files():
        data = load_yaml(rel) or {}
        for c in data.get("controls") or []:
            item = dict(c)
            item["_file"] = rel
            out.append(item)
    return out


def role_labels(roles_doc: dict) -> dict:
    return {r["id"]: r.get("label", r["name"]) for r in roles_doc.get("roles", [])}


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

def cell(value) -> str:
    text = "" if value is None else str(value)
    text = " ".join(text.split())
    return text.replace("|", "\\|")


def table(header: list[str], seps: list[str], rows: list[list]) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join(seps) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(cell(c) for c in row) + " |")
    return "\n".join(lines)


def rel_link(from_doc: str, target: str) -> str:
    return os.path.relpath(ROOT / target, (ROOT / from_doc).parent).replace(os.sep, "/")


def owner_cell(control: dict, labels: dict) -> str:
    if control.get("owner_text"):
        return control["owner_text"]
    owners = control.get("owner")
    owners = owners if isinstance(owners, list) else [owners]
    return " / ".join(labels.get(o, str(o)) for o in owners)


def suite_cell(value) -> str:
    if value is None:
        return "N/A"
    if isinstance(value, int):
        return f"{value}+"
    if value.get("text"):
        return value["text"]
    if value.get("min") is not None:
        return f"{value['min']}+"
    return "N/A"


def threshold_cell(metric: dict, tier: str) -> str:
    value = (metric.get("thresholds") or {}).get(tier)
    if value is None:
        return (metric.get("tier_text") or {}).get(tier, "N/A")
    sign = "≥" if metric["direction"] == "min" else "≤"
    unit = "%" if metric.get("unit", "percent") == "percent" else ""
    number = f"{value:g}"
    return f"{sign} {number}{unit}"


# ---------------------------------------------------------------------------
# Block renderers
# ---------------------------------------------------------------------------

REGISTER_HEADER = ["Control ID", "Control", "Applies To", "Owner", "Evidence", "Frequency", "Escalation if Failed"]
REGISTER_SEPS = ["---"] * 7


def render_stage(stage: int, group: str | None):
    def render() -> str:
        labels = role_labels(load_yaml("policy/roles.yaml"))
        rows = []
        for c in load_controls():
            if c.get("stage") != stage or c.get("group") != group:
                continue
            rows.append([c["id"], c["title"], c["applies_to"]["text"], owner_cell(c, labels),
                         c["evidence"], c["frequency"], c["on_fail"]])
        if not rows:
            raise BuildError(f"no controls found for stage {stage}" + (f", group {group}" if group else ""))
        return table(REGISTER_HEADER, REGISTER_SEPS, rows)
    return render


def mapping_citations() -> dict:
    """Map each mapping document path to the set of control IDs it cites."""
    out = {}
    for _, rel in MAPPING_DOCS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        out[rel] = set(CONTROL_ID_RE.findall(text))
    return out


def source_labels(paths: set[str]) -> dict:
    """Link text for each source path: the file name, or parent/file name when two
    sources share a file name (for example the two monitoring.md files)."""
    names: dict[str, set] = {}
    for p in paths:
        names.setdefault(Path(p).name, set()).add(p)
    return {p: (Path(p).name if len(names[Path(p).name]) == 1 else "/".join(Path(p).parts[-2:])) for p in paths}


def render_traceability() -> str:
    cites = mapping_citations()
    controls = load_controls()
    labels = source_labels({s for c in controls for s in c.get("sources") or []})
    header = ["Control", "Source documents"] + [f"[{name}]({rel_link(REGISTER, rel)})" for name, rel in MAPPING_DOCS]
    seps = ["---"] * len(header)
    rows, uncited = [], []
    for c in controls:
        sources = ", ".join(f"[{labels[s]}]({rel_link(REGISTER, s)})" for s in c.get("sources") or [])
        flags = ["Yes" if c["id"] in cites[rel] else "" for _, rel in MAPPING_DOCS]
        if not any(flags):
            uncited.append(c["id"])
        rows.append([c["id"], sources] + flags)
    out = table(header, seps, rows)
    if uncited:
        out += "\n\nControls cited by no regulatory mapping: " + ", ".join(uncited) + "."
    else:
        out += "\n\nEvery control is cited by at least one regulatory mapping."
    return out


def render_roles() -> str:
    rows = []
    for r in load_yaml("policy/roles.yaml")["roles"]:
        lod = r.get("line_of_defence_text")
        if not lod:
            lod = " or ".join(LINE_OF_DEFENCE[n] for n in r["line_of_defence"])
            lod = lod[0] + lod[1:].lower()
        rows.append([f"**{r['name']}**", r["description"], lod])
    return table(["Role", "Definition", "Line of defence"], ["------", "------------", "-----------------"], rows)


def render_approvals() -> str:
    doc = load_yaml("policy/tiers.yaml")
    rows = []
    for d in doc["approval_decisions"]:
        if d.get("in_approvals_table", True) is False:
            continue
        rows.append([d["label"]] + [doc["tiers"][t]["approvers"][d["id"]]["text"] for t in TIERS])
    return table(["Decision", "T1", "T2", "T3", "T4"], ["----------", "----", "----", "----", "----"], rows)


def render_cadence() -> str:
    tiers = load_yaml("policy/tiers.yaml")["tiers"]
    reassess = [tiers[t]["risk_reassessment"] for t in TIERS]
    reassess = [reassess[0]] + ["Same" if v == reassess[0] else v for v in reassess[1:]]
    rows = [
        ["Formal governance review (RV-001)"] + [tiers[t]["review_cadence"]["text"] for t in TIERS],
        ["Metrics review (operational)"] + [tiers[t]["metrics_review"] for t in TIERS],
        ["Revalidation (independent for T1/T2)"] + [tiers[t]["independent_revalidation"]["text"] for t in TIERS],
        ["Risk re-assessment (re-tiering check)"] + reassess,
    ]
    return table(["Activity", "T1", "T2", "T3", "T4"], ["----------", "----", "----", "----", "----"], rows)


def render_retention() -> str:
    tiers = load_yaml("policy/tiers.yaml")["tiers"]
    rows = []
    for t in TIERS:
        n = tiers[t]["interaction_log_retention_years"]
        rows.append([t, f"{n} year" + ("" if n == 1 else "s")])
    return table(["Tier", "Retention Period"], ["------", "-----------------"], rows)


def render_eval_types() -> str:
    rows = []
    for e in load_yaml("policy/thresholds.yaml")["eval_types"]:
        if e.get("in_table", True) is False:
            continue
        rows.append([e["name"], e["tests"], e["when"]] + [suite_cell(e["suite"].get(t)) for t in TIERS])
    return table(["Eval Type", "What It Tests", "When", "T1 Suite Size", "T2", "T3", "T4"],
                 ["-----------", "--------------", "------", ":---:", ":---:", ":---:", ":---:"], rows)


def render_thresholds() -> str:
    rows = []
    for m in load_yaml("policy/thresholds.yaml")["metrics"]:
        rows.append([m.get("label", m["name"])] + [threshold_cell(m, t) for t in TIERS])
    return table(["Metric", "T1", "T2", "T3", "T4"], ["--------", ":---:", ":---:", ":---:", ":---:"], rows)


def render_metric_definitions() -> str:
    rows = [[m["name"], m["definition"]] for m in load_yaml("policy/thresholds.yaml")["metrics"] if m.get("definition")]
    return table(["Metric", "Definition"], ["--------", "-----------"], rows)


def render_severity() -> str:
    rows = [[f"{s['id']} {s['name']}", s["definition"], s["response_sla"]] for s in load_yaml("policy/severity.yaml")["severities"]]
    return table(["Severity", "Definition", "Response SLA"], ["----------", "------------", "--------------"], rows)


def render_follow_up() -> str:
    rows = [[s["id"], s["root_cause"], s["post_mortem"]] for s in load_yaml("policy/severity.yaml")["severities"]]
    return table(["Severity", "Root cause", "Post-mortem"], ["----------", "-----------", "-------------"], rows)


def render_alert_mapping() -> str:
    groups: list[list] = []
    for p in load_yaml("policy/severity.yaml")["alert_priorities"]:
        key = (p["acknowledgement"], p["usual_severity"])
        if groups and groups[-1][0] == key:
            groups[-1][1].append(p["id"])
        else:
            groups.append([key, [p["id"]]])
    rows = [[", ".join(ids), ack, sev] for (ack, sev), ids in groups]
    return table(["Alert priority", "Acknowledgement", "Incident severity if one is declared"],
                 ["----------------", "-----------------", "--------------------------------------"], rows)


# (document, block name, source shown in the marker, renderer)
STAGE_FILES = {
    2: "controls/stage-02-risk-assessment.yaml",
    3: "controls/stage-03-architecture.yaml",
    4: "controls/stage-04-development.yaml",
    5: "controls/stage-05-evaluation.yaml",
    6: "controls/stage-06-security.yaml",
    7: "controls/stage-07-deployment.yaml",
    8: "controls/stage-08-operations.yaml",
    9: "controls/stage-09-review.yaml",
    10: "controls/stage-10-retirement.yaml",
}

BLOCKS = []
for _stage, _src in STAGE_FILES.items():
    BLOCKS.append((REGISTER, f"controls-stage-{_stage:02d}", _src, render_stage(_stage, None)))
    if _stage == 8:
        BLOCKS.append((REGISTER, "controls-stage-08-incident-response", _src, render_stage(8, "Incident Response")))
BLOCKS += [
    (REGISTER, "traceability", "controls/*.yaml", render_traceability),
    (ROLES_DOC, "role-definitions", "policy/roles.yaml", render_roles),
    (ROLES_DOC, "approvals-by-tier", "policy/tiers.yaml", render_approvals),
    (CADENCE_DOC, "cadence-by-tier", "policy/tiers.yaml", render_cadence),
    (AUDIT_TRAIL_DOC, "interaction-log-retention", "policy/tiers.yaml", render_retention),
    (EVAL_DOC, "evaluation-types", "policy/thresholds.yaml", render_eval_types),
    (EVAL_DOC, "threshold-definitions", "policy/thresholds.yaml", render_thresholds),
    (EVAL_DOC, "metric-definitions", "policy/thresholds.yaml", render_metric_definitions),
    (ESCALATION_DOC, "severity-classification", "policy/severity.yaml", render_severity),
    (ESCALATION_DOC, "severity-follow-up", "policy/severity.yaml", render_follow_up),
    (ESCALATION_DOC, "alert-priority-mapping", "policy/severity.yaml", render_alert_mapping),
]


# ---------------------------------------------------------------------------
# Marker handling
# ---------------------------------------------------------------------------

BLOCK_RE = re.compile(
    r"<!-- BEGIN GENERATED: (?P<name>[A-Za-z0-9._-]+)\..*?-->\n"
    r"(?P<body>.*?)"
    r"<!-- END GENERATED: (?P=name) -->",
    re.S,
)
BEGIN_RE = re.compile(r"<!-- BEGIN GENERATED: ([A-Za-z0-9._-]+)\.")


def begin_marker(name: str, source: str) -> str:
    return f"<!-- BEGIN GENERATED: {name}. Edit {source}, then run python tools/build.py -->"


def block_text(name: str, source: str, content: str) -> str:
    return f"{begin_marker(name, source)}\n\n{content.rstrip()}\n\n<!-- END GENERATED: {name} -->"


def build(check: bool = False) -> tuple[list[str], list[str]]:
    """Render all blocks. Returns (problems, changed_files).

    In check mode nothing is written; every out-of-date block is a problem.
    Otherwise out-of-date files are rewritten and only structural errors are problems.
    """
    problems: list[str] = []
    changed: list[str] = []
    by_doc: dict[str, list] = {}
    for doc, name, source, render in BLOCKS:
        by_doc.setdefault(doc, []).append((name, source, render))

    for doc, blocks in by_doc.items():
        path = ROOT / doc
        try:
            original = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            problems.append(f"{doc}: file not found")
            continue
        text = original
        expected_names = {name for name, _, _ in blocks}
        for found in BEGIN_RE.findall(text):
            if found not in expected_names:
                problems.append(f"{doc}: unknown generated block '{found}' (not defined in tools/build.py)")
        for name, source, render in blocks:
            matches = [m for m in BLOCK_RE.finditer(text) if m.group("name") == name]
            if len(matches) != 1:
                problems.append(f"{doc}: expected one '{name}' block with BEGIN and END markers, found {len(matches)}")
                continue
            try:
                content = render()
            except BuildError as exc:
                problems.append(f"{doc}: block '{name}': {exc}")
                continue
            except (KeyError, TypeError, AttributeError, ValueError) as exc:
                problems.append(f"{doc}: block '{name}': cannot render from {source} ({type(exc).__name__}: {exc}); run python tools/check.py for schema errors")
                continue
            new_block = block_text(name, source, content)
            m = matches[0]
            if m.group(0) != new_block:
                if check:
                    problems.append(f"{doc}: generated block '{name}' is out of date with {source}; run python tools/build.py")
                text = text[:m.start()] + new_block + text[m.end():]
        if text != original:
            changed.append(doc)
            if not check:
                path.write_text(text, encoding="utf-8")
    return problems, changed


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report out-of-date blocks without writing")
    args = parser.parse_args(argv)
    try:
        problems, changed = build(check=args.check)
    except BuildError as exc:
        print(f"build.py: {exc}", file=sys.stderr)
        return 1
    for p in problems:
        print(p, file=sys.stderr)
    if args.check:
        if problems:
            print(f"build.py --check: {len(problems)} problem(s)", file=sys.stderr)
            return 1
        print(f"build.py --check: {len(BLOCKS)} generated blocks are up to date")
        return 0
    for doc in changed:
        print(f"updated {doc}")
    if problems:
        return 1
    if not changed:
        print(f"build.py: {len(BLOCKS)} generated blocks already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
