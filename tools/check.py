#!/usr/bin/env python3
"""Validate the framework repository.

Checks:
  1. Schema validation of controls/*.yaml, policy/*.yaml and every example model card.
  2. Referential integrity: control IDs cited anywhere exist, owners and approvers resolve
     to roles, source paths exist, and cross-file values agree.
  3. Relative links and heading anchors in all Markdown outside docs/ (GitHub slug rules).
  4. Generated Markdown blocks are up to date (same as python tools/build.py --check).
  5. Example GenAI model cards conform to policy/thresholds.yaml for their tier.
  6. "Status as of <Month YYYY>" lines in framework/ are no older than 90 days
     (warning) or 180 days (error).

Usage:
    python tools/check.py [--today YYYY-MM-DD]

Exit code 1 if any error is found. Warnings are printed separately and do not fail the run.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import datetime as dt  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
from pathlib import Path  # noqa: E402

import yaml  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = build.ROOT
TIERS = build.TIERS
CONTROL_ID_RE = build.CONTROL_ID_RE
EXC_RE = re.compile(r"EXC-\d{4}-\d{3}")
SKIP_DIRS = {".git", "docs", "node_modules", "venv", ".venv", "__pycache__"}

# Pattern 3 safeguards a to e, by the field names the example cards use.
SAFEGUARD_FIELDS = ("sampled_review", "risk_based_routing", "scope_guardrails", "kill_switch", "hallucination_monitoring")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def error(self, area: str, msg: str) -> None:
        self.errors.append(f"[{area}] {msg}")

    def warn(self, area: str, msg: str) -> None:
        self.warnings.append(f"[{area}] {msg}")

    def note(self, area: str, msg: str) -> None:
        self.notes.append(f"[{area}] {msg}")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load(path: Path, rep: Report):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        rep.error("yaml", f"{rel(path)}: invalid YAML: {exc}")
    except OSError as exc:
        rep.error("yaml", f"{rel(path)}: {exc}")
    return None


def walk_files(suffixes: tuple[str, ...], roots: list[Path] | None = None):
    for base in roots or [ROOT]:
        if base.is_file():
            if base.suffix in suffixes:
                yield base
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if not (Path(dirpath) == ROOT and d in SKIP_DIRS) and d not in {".git", "__pycache__", "node_modules"})
            for f in sorted(filenames):
                if Path(f).suffix in suffixes:
                    yield Path(dirpath) / f


def model_card_paths() -> list[Path]:
    return sorted(p for p in (ROOT / "examples").rglob("*.yaml") if "model-card" in p.name)


def is_genai_card(card: dict) -> bool:
    details = card.get("model_details") if isinstance(card, dict) else None
    return isinstance(card, dict) and ("prompt_governance" in card or (isinstance(details, dict) and "model_id" in details))


# ---------------------------------------------------------------------------
# 1. Schema validation
# ---------------------------------------------------------------------------

def check_schemas(data: dict, cards: dict, rep: Report) -> None:
    try:
        import jsonschema
    except ImportError:
        msg = "jsonschema is not installed; schema validation skipped (pip install -r tools/requirements.txt)"
        if os.environ.get("CI"):
            rep.error("schema", msg)
        else:
            rep.warn("schema", msg)
        return

    schemas = {}
    for path in sorted((ROOT / "schemas").glob("*.schema.json")):
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            jsonschema.Draft202012Validator.check_schema(schema)
            schemas[path.name] = jsonschema.Draft202012Validator(schema)
        except (json.JSONDecodeError, jsonschema.SchemaError) as exc:
            rep.error("schema", f"{rel(path)}: invalid schema: {exc}")

    def validate(instance, schema_name: str, label: str) -> None:
        validator = schemas.get(schema_name)
        if validator is None:
            rep.error("schema", f"{label}: schema {schema_name} missing or invalid")
            return
        for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
            where = "/".join(str(p) for p in err.absolute_path) or "(root)"
            rep.error("schema", f"{label}: {where}: {err.message}")

    for path_str, doc in data["control_files"].items():
        validate(doc, "controls.schema.json", path_str)
    for name in ("roles", "tiers", "thresholds", "severity"):
        if data[name] is not None:
            validate(data[name], f"{name}.schema.json", f"policy/{name}.yaml")
    for path_str, card in cards.items():
        schema = "llm-model-card.schema.json" if is_genai_card(card) else "model-card.schema.json"
        validate(card, schema, f"{path_str} (against {schema})")


# ---------------------------------------------------------------------------
# 2. Referential integrity
# ---------------------------------------------------------------------------

def check_references(data: dict, rep: Report) -> set[str]:
    area = "refs"
    roles = data["roles"] or {}
    role_list = roles.get("roles") or []
    role_ids = {r.get("id") for r in role_list}
    labels = {r.get("id"): r.get("label", r.get("name", "")) for r in role_list}
    names = {r.get("id"): r.get("name", "") for r in role_list}
    seen_role = set()
    for r in role_list:
        if r.get("id") in seen_role:
            rep.error(area, f"policy/roles.yaml: duplicate role id {r.get('id')}")
        seen_role.add(r.get("id"))

    controls = []
    for path_str, doc in data["control_files"].items():
        if not isinstance(doc, dict):
            continue
        m = re.match(r"controls/stage-(\d+)-", path_str)
        if not m:
            rep.error(area, f"{path_str}: file name must start with stage-NN-")
        elif doc.get("stage") != int(m.group(1)):
            rep.error(area, f"{path_str}: stage {doc.get('stage')} does not match the file name")
        for c in doc.get("controls") or []:
            if not isinstance(c, dict):
                continue
            if c.get("stage") != doc.get("stage"):
                rep.error(area, f"{path_str}: {c.get('id')} has stage {c.get('stage')}, file stage is {doc.get('stage')}")
            controls.append((path_str, c))

    ids: dict[str, str] = {}
    prefix_stage: dict[str, set] = {}
    for path_str, c in controls:
        cid = c.get("id")
        if cid in ids:
            rep.error(area, f"duplicate control id {cid} in {ids[cid]} and {path_str}")
        ids[cid] = path_str
        if isinstance(cid, str):
            prefix_stage.setdefault(cid[:2], set()).add(c.get("stage"))

        owners = c.get("owner")
        owners = owners if isinstance(owners, list) else [owners]
        for o in owners:
            if o not in role_ids:
                rep.error(area, f"{path_str}: {cid} owner '{o}' is not a role id in policy/roles.yaml")
        if c.get("owner_text"):
            for o in owners:
                if o in role_ids and labels[o].lower() not in c["owner_text"].lower() and names[o].lower() not in c["owner_text"].lower():
                    rep.error(area, f"{path_str}: {cid} owner_text does not mention owner '{labels[o]}'")

        at = c.get("applies_to") or {}
        overlap = set(at.get("tiers") or []) & set(at.get("recommended") or [])
        if overlap:
            rep.error(area, f"{path_str}: {cid} lists {sorted(overlap)} as both required and recommended")

        for s in c.get("sources") or []:
            if not (ROOT / s).is_file() or not exists_exact_case(ROOT / s):
                rep.error(area, f"{path_str}: {cid} source '{s}' does not exist")

    for prefix, stages in prefix_stage.items():
        if len(stages) > 1:
            rep.error(area, f"control prefix {prefix} is used in more than one stage: {sorted(stages)}")

    # Approvers in tiers.yaml.
    tiers_doc = data["tiers"] or {}
    decisions = [d.get("id") for d in tiers_doc.get("approval_decisions") or []]
    for t, tier in (tiers_doc.get("tiers") or {}).items():
        approvers = (tier or {}).get("approvers") or {}
        for d in decisions:
            if d not in approvers:
                rep.error(area, f"policy/tiers.yaml: {t} has no approver for '{d}'")
        for d, entry in approvers.items():
            if d not in decisions:
                rep.error(area, f"policy/tiers.yaml: {t} approver '{d}' is not listed in approval_decisions")
            entry = entry or {}
            for role in [entry.get("accountable")] + list(entry.get("co_sign") or []):
                if role is not None and role not in role_ids:
                    rep.error(area, f"policy/tiers.yaml: {t} {d} role '{role}' is not a role id in policy/roles.yaml")

    # Severity mapping.
    sev_doc = data["severity"] or {}
    sev_ids = {s.get("id") for s in sev_doc.get("severities") or []}
    for p in sev_doc.get("alert_priorities") or []:
        for s in p.get("severities") or []:
            if s not in sev_ids:
                rep.error(area, f"policy/severity.yaml: {p.get('id')} maps to unknown severity {s}")

    # Controls named in thresholds.yaml.
    for e in (data["thresholds"] or {}).get("eval_types") or []:
        if e.get("control") and e["control"] not in ids:
            rep.error(area, f"policy/thresholds.yaml: eval type {e.get('id')} names unknown control {e['control']}")

    check_cross_file(data, {c.get("id"): c for _, c in controls}, rep)
    check_control_tokens(set(ids), rep)
    return set(ids)


def check_cross_file(data: dict, controls: dict, rep: Report) -> None:
    area = "consistency"
    tiers = ((data["tiers"] or {}).get("tiers")) or {}
    eval_types = {e.get("id"): e for e in (data["thresholds"] or {}).get("eval_types") or []}
    red = (eval_types.get("red_team") or {}).get("suite") or {}
    for t in TIERS:
        rt = (tiers.get(t) or {}).get("red_team") or {}
        s = red.get(t)
        s_min = s if isinstance(s, int) else (s or {}).get("min")
        s_text = build.suite_cell(s) if s is not None else None
        if rt and s_min != rt.get("min_cases"):
            rep.error(area, f"{t} red-team minimum differs: policy/tiers.yaml {rt.get('min_cases')}, policy/thresholds.yaml {s_min}")
        if rt and s_text != rt.get("depth"):
            rep.error(area, f"{t} red-team depth text differs: policy/tiers.yaml '{rt.get('depth')}', policy/thresholds.yaml '{s_text}'")
        s_required = True if isinstance(s, int) else (s or {}).get("required", True)
        if rt and s_required != rt.get("required"):
            rep.error(area, f"{t} red-team required flag differs between policy/tiers.yaml and policy/thresholds.yaml")

    rv = controls.get("RV-001")
    if rv:
        freq = rv.get("frequency", "").lower()
        for t in TIERS:
            cadence = ((tiers.get(t) or {}).get("review_cadence") or {}).get("text", "")
            if f"{cadence.lower()} ({t.lower()})" not in freq:
                rep.error(area, f"RV-001 frequency does not state '{cadence} ({t})' from policy/tiers.yaml")


def check_control_tokens(known: set[str], rep: Report) -> None:
    roots = [ROOT / "framework", ROOT / "templates", ROOT / "examples", ROOT / "controls", ROOT / "policy",
             ROOT / "tools" / "README.md"] + sorted(ROOT.glob("*.md"))
    for path in walk_files((".md", ".yaml", ".yml"), [p for p in roots if p.exists()]):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for token in CONTROL_ID_RE.findall(line):
                if token not in known:
                    rep.error("refs", f"{rel(path)}:{lineno}: control ID {token} is not defined in controls/*.yaml")


# ---------------------------------------------------------------------------
# 3. Links and anchors
# ---------------------------------------------------------------------------

LINK_RE = re.compile(r"(?<!\!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
_heading_cache: dict[Path, set] = {}


def github_slug(heading: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # link text only
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set:
    if path in _heading_cache:
        return _heading_cache[path]
    counts: dict[str, int] = {}
    out = set()
    in_code = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if FENCE_RE.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m:
            slug = github_slug(m.group(2))
            if slug in counts:
                counts[slug] += 1
                out.add(f"{slug}-{counts[slug]}")
            else:
                counts[slug] = 0
                out.add(slug)
    _heading_cache[path] = out
    return out


def exists_exact_case(path: Path) -> bool:
    """True if path exists with exactly this capitalisation (CI runs on a case-sensitive filesystem)."""
    try:
        parts = path.resolve().relative_to(ROOT).parts
    except ValueError:
        return path.exists()
    current = ROOT
    for part in parts:
        if part in ("", "."):
            continue
        try:
            if part not in os.listdir(current):
                return False
        except (NotADirectoryError, FileNotFoundError):
            return False
        current = current / part
    return True


def check_links(rep: Report) -> int:
    total = 0
    for path in walk_files((".md",)):
        in_code = False
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE_RE.match(line):
                in_code = not in_code
                continue
            if in_code:
                continue
            for m in LINK_RE.finditer(INLINE_CODE_RE.sub("", line)):
                target = m.group(2)
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                total += 1
                file_part, _, anchor = target.partition("#")
                full = (path.parent / file_part).resolve() if file_part else path
                where = f"{rel(path)}:{lineno}"
                if not full.exists() or not exists_exact_case(full):
                    rep.error("links", f"{where}: '{target}' points to a missing file")
                    continue
                if anchor:
                    if full.is_dir() or full.suffix != ".md":
                        rep.error("links", f"{where}: '{target}' has an anchor on a non-Markdown target")
                    elif anchor not in anchors(full):
                        rep.error("links", f"{where}: '{target}' anchor #{anchor} not found")
    return total


# ---------------------------------------------------------------------------
# 4. Generated blocks
# ---------------------------------------------------------------------------

def check_generated(rep: Report) -> None:
    try:
        problems, _ = build.build(check=True)
    except build.BuildError as exc:
        rep.error("generated", str(exc))
        return
    for p in problems:
        rep.error("generated", p)


# ---------------------------------------------------------------------------
# 5. Example GenAI model card conformance
# ---------------------------------------------------------------------------

def iter_strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield str(k)
            yield from iter_strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from iter_strings(v)


def as_fraction(metric: dict, tier: str):
    value = (metric.get("thresholds") or {}).get(tier)
    if value is None:
        return None
    return value / 100 if metric.get("unit", "percent") == "percent" else value


def passes(value: float, threshold: float, direction: str) -> bool:
    eps = 1e-9
    return value >= threshold - eps if direction == "min" else value <= threshold + eps


def suite_min(eval_type: dict | None, tier: str):
    """(minimum, required) for an eval type at a tier; minimum is None when no number applies."""
    if not eval_type:
        return None, False
    s = (eval_type.get("suite") or {}).get(tier)
    if s is None:
        return None, False
    if isinstance(s, int):
        return s, True
    return s.get("min"), s.get("required", True)


def conform_genai_card(path_str: str, card: dict, thresholds: dict, rep: Report) -> None:
    area = path_str
    details = card.get("model_details") or {}
    tier = details.get("risk_tier")
    if tier not in TIERS:
        rep.error(area, f"model_details.risk_tier is {tier!r}; expected one of T1-T4")
        return
    metrics_fw = {m["id"]: m for m in thresholds.get("metrics") or []}
    eval_types = {e["id"]: e for e in thresholds.get("eval_types") or []}
    exc_ids = sorted(set(EXC_RE.findall(" ".join(iter_strings(card)))))
    rag_cfg = ((card.get("system_architecture") or {}).get("rag_configuration")) or {}
    is_rag = rag_cfg.get("enabled") is True

    evaluation = card.get("evaluation")
    if not isinstance(evaluation, dict):
        rep.warn(area, "no evaluation block; threshold and suite-size checks could not run")
        return

    # Collect metrics: evaluation.metrics plus bias_evaluation.counterfactual_consistency.
    metric_rows = []
    for i, m in enumerate(evaluation.get("metrics") or []):
        if isinstance(m, dict):
            metric_rows.append((f"evaluation.metrics[{i}]", m.get("name"), m.get("value"), m.get("threshold"), m.get("direction")))
    bias = evaluation.get("bias_evaluation") or {}
    names_seen = {row[1] for row in metric_rows}
    if "counterfactual_consistency" in bias and "counterfactual_consistency" not in names_seen:
        metric_rows.append(("evaluation.bias_evaluation", "counterfactual_consistency", bias.get("counterfactual_consistency"), None, None))

    failing = []
    for where, name, value, card_thr, card_dir in metric_rows:
        fw = metrics_fw.get(name)
        direction = fw["direction"] if fw else (card_dir or "min")
        fw_thr = as_fraction(fw, tier) if fw else None
        if fw and fw_thr is not None:
            if card_thr is None:
                if where.startswith("evaluation.metrics"):
                    rep.warn(area, f"{where} {name} has no threshold; value tested against the {tier} threshold {fw_thr:g}")
            elif not passes(card_thr, fw_thr, direction):
                rep.error(area, f"{where} {name} threshold {card_thr:g} is looser than the {tier} threshold {fw_thr:g} in policy/thresholds.yaml")
        effective = card_thr if card_thr is not None else fw_thr
        if value is None:
            rep.warn(area, f"{where} {name} has no value; its threshold could not be tested")
            continue
        if effective is None:
            if fw is None:
                rep.warn(area, f"{where} {name} has no threshold to test its value against")
            continue
        if not passes(value, effective, direction):
            failing.append(f"{name} {value:g} vs threshold {effective:g}")

    if failing:
        if exc_ids:
            rep.note(area, f"metrics below threshold ({'; '.join(failing)}) are covered by exception reference {', '.join(exc_ids)}")
        else:
            rep.error(area, f"metrics below threshold with no exception reference (EXC-YYYY-NNN): {'; '.join(failing)}")

    # Framework metrics with a threshold at this tier that the card does not record.
    present = {row[1] for row in metric_rows}
    for mid, fw in metrics_fw.items():
        if as_fraction(fw, tier) is None or mid in present:
            continue
        if fw.get("applies_to") == "rag" and not is_rag:
            continue
        rep.warn(area, f"{mid} is not recorded in the card; the {tier} threshold for it could not be checked")

    # Use-case hallucination tolerance must not exceed the tier cap.
    tolerance = (card.get("safety") or {}).get("hallucination_tolerance")
    cap = as_fraction(metrics_fw["hallucination_rate"], tier) if "hallucination_rate" in metrics_fw else None
    if tolerance and cap is not None:
        m = re.search(r"(?:≤|<=)\s*([0-9.]+)\s*%", str(tolerance))
        if not m:
            rep.warn(area, f"safety.hallucination_tolerance '{tolerance}' is not in the form '≤ N%'; not compared with the tier cap")
        elif float(m.group(1)) / 100 > cap + 1e-9:
            rep.error(area, f"safety.hallucination_tolerance '{tolerance}' exceeds the {tier} cap of {cap * 100:g}%")

    # Suite sizes.
    pre_min, _ = suite_min(eval_types.get("pre_release"), tier)
    size = evaluation.get("evaluation_dataset_size")
    if pre_min is not None:
        if size is None:
            rep.warn(area, "evaluation.evaluation_dataset_size is missing; pre-release suite size could not be checked")
        elif size < pre_min:
            rep.error(area, f"evaluation.evaluation_dataset_size {size} is below the {tier} pre-release minimum of {pre_min}")

    red_min, red_required = suite_min(eval_types.get("red_team"), tier)
    adv = evaluation.get("adversarial_testing")
    if isinstance(adv, dict):
        test_type = adv.get("test_type")
        adv_size = adv.get("test_suite_size")
        if test_type == "prompt-change-regression":
            pc_min, _ = suite_min(eval_types.get("prompt_change_adversarial_regression"), tier)
            if adv_size is not None and pc_min is not None and adv_size < pc_min:
                rep.error(area, f"adversarial_testing.test_suite_size {adv_size} is below the {tier} prompt-change regression minimum of {pc_min}")
            if red_required:
                rep.warn(area, "adversarial_testing records a prompt-change regression set, not a red-team; the red-team suite size is not in the card and could not be checked")
        else:
            if test_type is None:
                rep.warn(area, "adversarial_testing.test_type is not set; test_suite_size treated as the red-team suite")
            if adv_size is None:
                if red_required:
                    rep.warn(area, "adversarial_testing.test_suite_size is missing; red-team suite size could not be checked")
            elif red_min is not None and adv_size < red_min:
                msg = f"adversarial_testing.test_suite_size {adv_size} is below the {tier} red-team minimum of {red_min}"
                rep.error(area, msg) if red_required else rep.warn(area, msg + " (recommended at this tier)")
    elif red_required:
        rep.warn(area, "no adversarial_testing block; red-team suite size could not be checked")

    # Production evaluations.
    for i, pe in enumerate(evaluation.get("production_evaluations") or []):
        if not isinstance(pe, dict):
            continue
        where = f"evaluation.production_evaluations[{i}]"
        if pe.get("activity") == "offline-suite-rerun" and pe.get("dataset_size") is not None and pre_min is not None and pe["dataset_size"] < pre_min:
            rep.error(area, f"{where} offline re-run dataset_size {pe['dataset_size']} is below the {tier} pre-release minimum of {pre_min}")
        outcome = str(pe.get("outcome") or "")
        for key, value in (pe.get("results") or {}).items():
            mid = next((m for m in metrics_fw if key == m or key.startswith(m + "_")), None)
            if mid is None or value is None:
                continue
            card_thr = next((r[3] for r in metric_rows if r[1] == mid and r[3] is not None), None)
            thr = card_thr if card_thr is not None else as_fraction(metrics_fw[mid], tier)
            if thr is None or passes(value, thr, metrics_fw[mid]["direction"]):
                continue
            if outcome.lower().startswith("fail") or EXC_RE.search(outcome):
                rep.note(area, f"{where} {key} {value:g} breaches threshold {thr:g}; recorded as: {outcome[:80]}")
            else:
                rep.error(area, f"{where} {key} {value:g} breaches threshold {thr:g} but the outcome is not recorded as a failure or exception")

    # Human oversight for T1 customer-facing systems.
    use = card.get("intended_use") or {}
    if tier == "T1" and use.get("customer_facing") is True:
        pattern = use.get("human_oversight_pattern")
        if pattern not in ("human-in-the-loop", "human-over-the-loop"):
            rep.error(area, f"T1 customer-facing system uses '{pattern}'; it must use human-in-the-loop or human-over-the-loop")
        if pattern == "human-over-the-loop":
            safeguards = use.get("human_oversight_safeguards")
            if not isinstance(safeguards, dict) or not safeguards:
                rep.error(area, "T1 customer-facing human-over-the-loop needs an intended_use.human_oversight_safeguards block (Pattern 3 safeguards a to e)")
            else:
                missing = [f for f in SAFEGUARD_FIELDS if not safeguards.get(f)]
                if missing:
                    rep.error(area, f"human_oversight_safeguards is missing: {', '.join(missing)}")


def check_cards(cards: dict, thresholds: dict | None, rep: Report) -> None:
    if not thresholds:
        rep.error("conformance", "policy/thresholds.yaml could not be loaded; card conformance not checked")
        return
    for path_str, card in cards.items():
        if not isinstance(card, dict):
            rep.error(path_str, "model card is not a YAML mapping")
            continue
        if is_genai_card(card):
            try:
                conform_genai_card(path_str, card, thresholds, rep)
            except (KeyError, TypeError, AttributeError, ValueError) as exc:
                rep.error(path_str, f"conformance check could not read the card ({type(exc).__name__}: {exc})")


# ---------------------------------------------------------------------------
# 6. Staleness of regulatory status lines
# ---------------------------------------------------------------------------

MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 1)}
STATUS_RE = re.compile(r"Status as of (" + "|".join(MONTHS) + r") (\d{4})")


def check_staleness(today: dt.date, rep: Report) -> int:
    found = 0
    for path in walk_files((".md",), [ROOT / "framework"]):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for month, year in STATUS_RE.findall(line):
                found += 1
                stated = dt.date(int(year), MONTHS[month], 1)
                age = (today - stated).days
                where = f"{rel(path)}:{lineno}"
                if age > 180:
                    rep.error("staleness", f"{where}: 'Status as of {month} {year}' is {age} days old (limit 180); review the regulatory content")
                elif age > 90:
                    rep.warn("staleness", f"{where}: 'Status as of {month} {year}' is {age} days old (review due after 90)")
    return found


# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--today", help="date used for the staleness check (YYYY-MM-DD); default is today")
    args = parser.parse_args(argv)
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    rep = Report()
    data = {
        "control_files": {rel(p): load(p, rep) for p in sorted((ROOT / "controls").glob("*.yaml"))},
        "roles": load(ROOT / "policy/roles.yaml", rep),
        "tiers": load(ROOT / "policy/tiers.yaml", rep),
        "thresholds": load(ROOT / "policy/thresholds.yaml", rep),
        "severity": load(ROOT / "policy/severity.yaml", rep),
    }
    cards = {rel(p): load(p, rep) for p in model_card_paths()}

    check_schemas(data, cards, rep)
    control_ids = check_references(data, rep)
    link_count = check_links(rep)
    check_generated(rep)
    check_cards(cards, data["thresholds"], rep)
    status_count = check_staleness(today, rep)

    genai = sum(1 for c in cards.values() if isinstance(c, dict) and is_genai_card(c))
    print(f"Checked {len(control_ids)} controls, {len((data['roles'] or {}).get('roles') or [])} roles, "
          f"{len(cards)} model cards ({genai} GenAI), {link_count} relative links, "
          f"{len(build.BLOCKS)} generated blocks, {status_count} status lines (as of {today.isoformat()}).")
    if rep.notes:
        print(f"\nNotes ({len(rep.notes)}):")
        for n in rep.notes:
            print(f"  {n}")
    if rep.warnings:
        print(f"\nWarnings ({len(rep.warnings)}):")
        for w in rep.warnings:
            print(f"  {w}")
    if rep.errors:
        print(f"\nErrors ({len(rep.errors)}):")
        for e in rep.errors:
            print(f"  {e}")
    print(f"\ncheck.py: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
