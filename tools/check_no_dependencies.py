#!/usr/bin/env python3
# =============================================================================
#  tools/check_no_dependencies.py
# -----------------------------------------------------------------------------
#  Assert that this package has no runtime dependencies, and that nothing in
#  the shipped source imports a third-party module.
#
#  WHY THIS IS A SCRIPT AND NOT A CONVENTION
#  "Zero runtime dependencies" is stated as a hard constraint in three places:
#  pyproject.toml, GOVERNANCE.md section 3.3, and SECURITY.md section 1.2. It
#  is also the single most valuable security property this project has, because
#  it removes an entire risk class rather than mitigating it: there is no
#  transitive dependency to be compromised, no version to resolve, and no
#  advisory to track. THREAT_MODEL.md section 2 lists it first for that reason.
#
#  A constraint that is only checked by a human reading a diff is a constraint
#  that will be broken, quietly, by a well-meaning contributor who needs one
#  small thing from one small library. This script runs in the pre-commit
#  hooks, in CI, in the daily security audit and in dependency review, so that
#  the breach is caught in the minute it happens rather than in the release
#  that ships it.
#
#  WHAT IT CHECKS
#    1. The `dependencies` list in pyproject.toml is literally empty.
#    2. No module under src/ imports anything outside the standard library and
#       this package itself.
#    3. Optional extras exist and are declared, so that development tooling is
#       not smuggled into the runtime list instead.
#
#  Check 2 matters because check 1 alone is insufficient: a module could import
#  a package that happens to be installed in the developer environment, work
#  perfectly in CI, and fail for a user with a clean install. That failure mode
#  is not hypothetical; it is one of the most common ways a "no dependencies"
#  claim quietly stops being true.
#
#  USAGE
#      python tools/check_no_dependencies.py
#
#  EXIT CODES
#      0  the constraint holds
#      1  the constraint is broken
#      2  pyproject.toml is missing or unparseable
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import List, NamedTuple, Set

REPO_ROOT = Path(__file__).resolve().parent.parent
PYPROJECT = REPO_ROOT / "pyproject.toml"
SRC = REPO_ROOT / "src" / "biotechnology"

#: The package's own top-level name, which is obviously permitted.
SELF = "biotechnology"

# -----------------------------------------------------------------------------
#  Standard library module names.
#
#  sys.stdlib_module_names exists from Python 3.10. On 3.9 it does not, and
#  rather than shipping a hand-maintained list that will rot, the script falls
#  back to a conservative set and says so. Continuous integration runs this on
#  3.12, so the strict path is the one that gates a merge.
# -----------------------------------------------------------------------------
_STDLIB_FALLBACK = {
    "abc", "argparse", "ast", "base64", "bisect", "builtins", "calendar",
    "collections", "colorsys", "contextlib", "copy", "csv", "dataclasses",
    "datetime", "decimal", "difflib", "enum", "errno", "fnmatch",
    "fractions", "functools", "gettext", "glob", "gzip", "hashlib", "heapq",
    "html", "importlib", "inspect", "io", "itertools", "json", "keyword",
    "locale", "logging", "math", "numbers", "operator", "os", "pathlib",
    "platform", "pprint", "random", "re", "shutil", "statistics", "string",
    "textwrap", "time", "tomllib", "types", "typing", "unicodedata",
    "warnings", "zipfile", "zoneinfo",
}


def stdlib_names() -> Set[str]:
    """Every standard library top-level module name available to us."""
    names = getattr(sys, "stdlib_module_names", None)
    if names:
        return set(names)
    return set(_STDLIB_FALLBACK)


class Violation(NamedTuple):
    where: str
    message: str
    remedy: str


# =============================================================================
#  Check 1: the declared dependency list
# =============================================================================
def check_declared() -> List[Violation]:
    """The `dependencies` array in pyproject.toml must be empty."""
    violations: List[Violation] = []

    if not PYPROJECT.exists():
        print("error: pyproject.toml is missing", file=sys.stderr)
        raise SystemExit(2)

    text = PYPROJECT.read_text(encoding="utf-8")

    # tomllib is available from 3.11. Where it is, parse properly; otherwise
    # fall back to a targeted expression rather than guessing at TOML.
    parsed = None
    try:
        import tomllib

        parsed = tomllib.loads(text)
    except ImportError:
        parsed = None
    except Exception as exc:  # noqa: BLE001 - a malformed file is a hard stop
        print(f"error: pyproject.toml does not parse: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc

    if parsed is not None:
        deps = parsed.get("project", {}).get("dependencies", None)
        if deps is None:
            violations.append(
                Violation(
                    where="pyproject.toml",
                    message="the [project] table declares no `dependencies` key at all",
                    remedy="Add `dependencies = []` explicitly, so the constraint is visible.",
                )
            )
        elif deps:
            violations.append(
                Violation(
                    where="pyproject.toml",
                    message=f"runtime dependencies were added: {deps}",
                    remedy=(
                        "Build the feature against the standard library, put it "
                        "behind an optional extra, or ship it as a separate "
                        "package. See GOVERNANCE.md section 3.3."
                    ),
                )
            )
        if not parsed.get("project", {}).get("optional-dependencies"):
            violations.append(
                Violation(
                    where="pyproject.toml",
                    message="no optional-dependencies table found",
                    remedy="Development tooling belongs in extras, not in the runtime list.",
                )
            )
        return violations

    # Fallback for 3.9 and 3.10.
    block = re.search(r"^dependencies\s*=\s*\[(.*?)\]", text, re.M | re.S)
    if block is None:
        violations.append(
            Violation(
                where="pyproject.toml",
                message="no `dependencies` key found",
                remedy="Add `dependencies = []` explicitly.",
            )
        )
    elif block.group(1).strip():
        violations.append(
            Violation(
                where="pyproject.toml",
                message=f"runtime dependencies were added: {block.group(1).strip()}",
                remedy="See GOVERNANCE.md section 3.3.",
            )
        )
    return violations


# =============================================================================
#  Check 2: what the source actually imports
# =============================================================================
def check_imports() -> List[Violation]:
    """No module under src/ may import a third-party package."""
    violations: List[Violation] = []
    allowed = stdlib_names() | {SELF, "__future__"}

    if not SRC.is_dir():
        return violations

    for path in sorted(SRC.rglob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            violations.append(
                Violation(
                    where=str(path.relative_to(REPO_ROOT)),
                    message=f"does not parse: {exc}",
                    remedy="Fix the syntax error.",
                )
            )
            continue

        for node in ast.walk(tree):
            names: List[str] = []
            if isinstance(node, ast.Import):
                names = [alias.name.split(".")[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                # A relative import has level > 0 and is always internal.
                if node.level and node.level > 0:
                    continue
                if node.module:
                    names = [node.module.split(".")[0]]

            for name in names:
                if name and name not in allowed:
                    violations.append(
                        Violation(
                            where=f"{path.relative_to(REPO_ROOT)}:{node.lineno}",
                            message=f"imports third-party module {name!r}",
                            remedy=(
                                "The shipped package imports only the standard "
                                "library. If this is genuinely needed, it belongs "
                                "in an optional extra with a guarded import."
                            ),
                        )
                    )

    return violations


# =============================================================================
#  Entry point
# =============================================================================
def main() -> int:
    violations = check_declared() + check_imports()

    if not violations:
        module_count = len(list(SRC.rglob("*.py"))) if SRC.is_dir() else 0
        print(
            "OK: runtime dependency list is empty, and "
            f"{module_count} source module(s) import only the standard library."
        )
        return 0

    print(f"{len(violations)} dependency constraint violation(s):\n", file=sys.stderr)
    for v in violations:
        print(f"  {v.where}", file=sys.stderr)
        print(f"    problem: {v.message}", file=sys.stderr)
        print(f"    remedy:  {v.remedy}\n", file=sys.stderr)
    print(
        "Zero runtime dependencies is a hard constraint. See GOVERNANCE.md "
        "section 3.3 and THREAT_MODEL.md section 2.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
