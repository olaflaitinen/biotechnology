#!/usr/bin/env python3
# =============================================================================
#  tools/check_action_pinning.py
# -----------------------------------------------------------------------------
#  Verify that every GitHub Action called by this repository is governed by
#  .github/action-pins.yml.
#
#  WHY THIS SCRIPT EXISTS
#  A GitHub Action is executable code that runs inside this repository with the
#  repository's own permissions. THREAT_MODEL.md ranks a compromised action as
#  threat T-01, the largest real attack surface here.
#
#  A `uses:` line scattered across seven workflow files is not reviewable. This
#  script makes the rule mechanical: an action that is not written down in the
#  governance file, with a publisher, a justification and a review date, cannot
#  be called.
#
#  WHAT IT CHECKS
#    1. Every `uses:` reference in .github/workflows appears in the pin file.
#    2. The ref used in the workflow matches the ref recorded in the pin file.
#    3. No entry in the pin file is stale beyond the review interval.
#    4. Under --strict, and once policy.require_resolved_sha is true, every
#       entry has a real 40-character commit SHA rather than "unresolved".
#    5. Nothing in the pin file is unused, because an ungoverned entry that
#       nobody calls is a rule nobody is checking.
#
#  WHY IT DOES NOT PARSE YAML WITH A LIBRARY
#  Because this repository has no runtime dependencies and its tooling avoids
#  them where it reasonably can. The two things this script needs from the
#  files, meaning `uses:` lines and a flat list of records, are extracted with
#  anchored regular expressions. If the pin file grows a structure that needs a
#  real parser, add PyYAML to the lint extra and rewrite this honestly rather
#  than making the expressions cleverer.
#
#  USAGE
#      python tools/check_action_pinning.py
#      python tools/check_action_pinning.py --strict
#
#  EXIT CODES
#      0  everything is governed
#      1  a violation was found
#      2  the pin file is missing or unreadable
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"
ACTION_DIR = REPO_ROOT / ".github" / "actions"
PIN_FILE = REPO_ROOT / ".github" / "action-pins.yml"

# -----------------------------------------------------------------------------
#  A `uses:` line looks like one of:
#      uses: actions/checkout@v4
#      uses: "actions/checkout@v4"
#      uses: github/codeql-action/init@v3
#      uses: actions/checkout@a1b2c3...  # v4.1.7
#  Local composite actions look like `uses: ./.github/actions/thing` and are
#  exempt, because they are part of this repository and are reviewed with it.
# -----------------------------------------------------------------------------
USES_RE = re.compile(
    r"""^\s*-?\s*uses:\s*["']?(?P<ref>[^"'\s#]+)["']?""",
    re.MULTILINE,
)

#: A full git commit hash. Anything shorter is not a pin.
SHA_RE = re.compile(r"^[0-9a-f]{40}$")

#: Entries in the pin file. Deliberately simple: a `- name:` starts a record
#: and every following `key: value` at greater indentation belongs to it.
RECORD_START_RE = re.compile(r"""^\s*-\s+name:\s*["']?(?P<name>[^"'\n]+?)["']?\s*$""")
FIELD_RE = re.compile(r"""^\s+(?P<key>[a-z_]+):\s*["']?(?P<value>[^"'\n]*?)["']?\s*$""")


class Pin(NamedTuple):
    """One governed action entry."""

    name: str
    ref: str
    sha: str
    publisher: str
    last_reviewed: str


class Violation(NamedTuple):
    """One problem, with enough context for a contributor to fix it."""

    where: str
    message: str
    remedy: str


# =============================================================================
#  Reading the pin file
# =============================================================================
def read_pins(path: Path) -> Tuple[Dict[str, Pin], Dict[str, str], Set[str]]:
    """Parse the governance file into pins, policy flags and rejected names.

    Returns
    -------
    pins:
        Mapping of action name to its governed record.
    policy:
        The flat key/value pairs under the top-level ``policy:`` block.
    rejected:
        Names recorded under ``rejected:``, which must never be used.
    """
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    pins: Dict[str, Pin] = {}
    policy: Dict[str, str] = {}
    rejected: Set[str] = set()

    section = ""
    current: Dict[str, str] = {}

    def flush() -> None:
        if not current:
            return
        name = current.get("name", "")
        if not name:
            return
        if section == "rejected":
            rejected.add(name)
        elif section == "actions":
            pins[name] = Pin(
                name=name,
                ref=current.get("ref", ""),
                sha=current.get("sha", "unresolved"),
                publisher=current.get("publisher", "unknown"),
                last_reviewed=current.get("last_reviewed", ""),
            )
        current.clear()

    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # A top-level key changes section.
        if not raw.startswith((" ", "\t")) and stripped.endswith(":"):
            flush()
            section = stripped[:-1]
            continue

        if section == "policy":
            m = FIELD_RE.match(raw)
            if m:
                policy[m.group("key")] = m.group("value")
            continue

        start = RECORD_START_RE.match(raw)
        if start:
            flush()
            current["name"] = start.group("name")
            continue

        field = FIELD_RE.match(raw)
        if field and current:
            key = field.group("key")
            # Only keep the scalar fields we care about; list and folded fields
            # are ignored deliberately rather than half-parsed.
            if key in {"ref", "sha", "publisher", "last_reviewed"}:
                current[key] = field.group("value")

    flush()
    return pins, policy, rejected


# =============================================================================
#  Reading the workflows
# =============================================================================
def collect_uses() -> Dict[str, List[Tuple[Path, str]]]:
    """Map action name to the files and refs where it is called."""
    found: Dict[str, List[Tuple[Path, str]]] = {}

    candidates: List[Path] = []
    if WORKFLOW_DIR.is_dir():
        candidates.extend(sorted(WORKFLOW_DIR.glob("*.yml")))
        candidates.extend(sorted(WORKFLOW_DIR.glob("*.yaml")))
    if ACTION_DIR.is_dir():
        candidates.extend(sorted(ACTION_DIR.rglob("action.yml")))

    for path in candidates:
        text = path.read_text(encoding="utf-8")
        for match in USES_RE.finditer(text):
            ref = match.group("ref")

            # A local composite action lives in this repository and is reviewed
            # with it. Nothing to govern.
            if ref.startswith((".", "/")):
                continue
            # A container action is a different trust model and is not used
            # here; flag it explicitly rather than silently skipping.
            if ref.startswith("docker://"):
                found.setdefault(ref, []).append((path, ""))
                continue

            name, _, version = ref.partition("@")
            found.setdefault(name, []).append((path, version))

    return found


# =============================================================================
#  The checks
# =============================================================================
def check(strict: bool) -> List[Violation]:
    """Run every check and return the violations found."""
    violations: List[Violation] = []

    if not PIN_FILE.exists():
        print(f"error: {PIN_FILE.relative_to(REPO_ROOT)} is missing", file=sys.stderr)
        raise SystemExit(2)

    pins, policy, rejected = read_pins(PIN_FILE)
    used = collect_uses()

    require_resolved = policy.get("require_resolved_sha", "false").lower() == "true"
    try:
        interval = int(policy.get("review_interval_days", "90"))
    except ValueError:
        interval = 90

    # -- 1. every called action is governed -----------------------------------
    for name, callers in sorted(used.items()):
        if name in rejected:
            for path, _ in callers:
                violations.append(
                    Violation(
                        where=f"{path.relative_to(REPO_ROOT)}",
                        message=f"{name} is on the rejected list in action-pins.yml",
                        remedy="Remove the call, or move the entry out of `rejected:` with a written reason.",
                    )
                )
            continue

        if name not in pins:
            for path, _ in callers:
                violations.append(
                    Violation(
                        where=f"{path.relative_to(REPO_ROOT)}",
                        message=f"{name} is not governed by .github/action-pins.yml",
                        remedy=(
                            "Add an entry with publisher, permissions_needed, "
                            "justification and last_reviewed, in the same pull "
                            "request that adds the uses: line."
                        ),
                    )
                )
            continue

        # -- 2. the ref matches ----------------------------------------------
        governed = pins[name]
        for path, version in callers:
            if not version:
                violations.append(
                    Violation(
                        where=f"{path.relative_to(REPO_ROOT)}",
                        message=f"{name} is used without any version reference",
                        remedy="Pin it. An unpinned action follows a moving branch.",
                    )
                )
                continue
            if version != governed.ref and not SHA_RE.match(version):
                violations.append(
                    Violation(
                        where=f"{path.relative_to(REPO_ROOT)}",
                        message=(
                            f"{name}@{version} does not match the governed ref "
                            f"{governed.ref!r}"
                        ),
                        remedy="Update the workflow, or update the pin file and record why.",
                    )
                )

    # -- 3. review freshness --------------------------------------------------
    today = _dt.date.today()
    for name, pin in sorted(pins.items()):
        if not pin.last_reviewed:
            violations.append(
                Violation(
                    where=".github/action-pins.yml",
                    message=f"{name} has no last_reviewed date",
                    remedy="Add one. An unreviewed pin is an unexamined trust decision.",
                )
            )
            continue
        try:
            reviewed = _dt.date.fromisoformat(pin.last_reviewed)
        except ValueError:
            violations.append(
                Violation(
                    where=".github/action-pins.yml",
                    message=f"{name} has an unparseable last_reviewed {pin.last_reviewed!r}",
                    remedy="Use ISO 8601, for example 2026-09-02.",
                )
            )
            continue
        age = (today - reviewed).days
        if age > interval:
            violations.append(
                Violation(
                    where=".github/action-pins.yml",
                    message=f"{name} was last reviewed {age} days ago, interval is {interval}",
                    remedy="Re-check the publisher and the ref, then update last_reviewed.",
                )
            )

    # -- 4. resolved SHAs, once the policy demands them ----------------------
    if strict and require_resolved:
        for name, pin in sorted(pins.items()):
            if not SHA_RE.match(pin.sha):
                violations.append(
                    Violation(
                        where=".github/action-pins.yml",
                        message=f"{name} has sha {pin.sha!r}, not a 40-character commit hash",
                        remedy="Run `make pin-actions` from a network-connected environment.",
                    )
                )

    # -- 5. unused governance entries ----------------------------------------
    for name in sorted(set(pins) - set(used)):
        violations.append(
            Violation(
                where=".github/action-pins.yml",
                message=f"{name} is governed but never called",
                remedy="Remove the entry. An unused rule is a rule nobody is checking.",
            )
        )

    return violations


# =============================================================================
#  Entry point
# =============================================================================
def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify that every GitHub Action is governed by .github/action-pins.yml.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also require a resolved commit SHA, once the pin file asks for it.",
    )
    args = parser.parse_args(argv)

    violations = check(strict=args.strict)

    if not violations:
        pins, _, _ = read_pins(PIN_FILE)
        used = collect_uses()
        print(
            f"OK: {len(used)} action reference(s) across the workflows, "
            f"all governed by {len(pins)} pin entries."
        )
        return 0

    print(f"{len(violations)} action pinning violation(s):\n", file=sys.stderr)
    for v in violations:
        print(f"  {v.where}", file=sys.stderr)
        print(f"    problem: {v.message}", file=sys.stderr)
        print(f"    remedy:  {v.remedy}\n", file=sys.stderr)
    print(
        "See THREAT_MODEL.md threat T-01 for why this rule exists.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
