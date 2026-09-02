#!/usr/bin/env python3
# =============================================================================
#  tools/check_workflow_permissions.py
# -----------------------------------------------------------------------------
#  Verify that every GitHub Actions workflow follows the least-privilege rules
#  this project commits to in SECURITY.md section 3.3.
#
#  WHY IT MATTERS
#  A workflow job runs with a GITHUB_TOKEN whose scope is whatever the workflow
#  asks for. The default, if a workflow says nothing, is a broad read and write
#  token. Any action running in that job, and any code it executes, inherits
#  that reach.
#
#  THREAT_MODEL.md ranks a compromised action as threat T-01 and a malicious
#  pull request as T-02. Both are bounded almost entirely by the permissions
#  the job holds. A workflow that declares `permissions: {}` at the top and
#  grants each job only what it needs turns a full compromise into a nuisance.
#
#  THE FIVE RULES
#    1. Every workflow declares a top-level `permissions:` block. Silence means
#       the repository default, which is too broad.
#    2. That top-level block is empty, meaning `permissions: {}`. Deny by
#       default; each job re-grants.
#    3. Every job declares its own `permissions:` block.
#    4. No job requests `write-all`, and no workflow-level block grants write.
#    5. Every checkout step sets `persist-credentials: false`, so the token is
#       not left in .git/config for a later step to read.
#
#  Rule 5 catches the most commonly missed one. The credential is written to
#  the working tree by default, and every subsequent step in that job can read
#  it, including a step that only meant to run a linter.
#
#  WHY IT DOES NOT USE A YAML LIBRARY
#  The tooling in this repository avoids third-party imports where it
#  reasonably can, for the same reason the package itself does. The structures
#  checked here are shallow and anchored, and the failure mode of the parsing
#  is a false positive that a human reads, not a silent pass. If the workflows
#  grow structure that needs a real parser, add PyYAML to the lint extra and
#  rewrite this honestly rather than making the expressions cleverer.
#
#  USAGE
#      python tools/check_workflow_permissions.py
#
#  EXIT CODES
#      0  every workflow complies
#      1  at least one violation
#      2  the workflow directory is missing
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, NamedTuple

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"

# -----------------------------------------------------------------------------
#  A top-level key sits at column zero. A job key sits at exactly two spaces
#  under `jobs:`. Anchoring on indentation is what lets this work without a
#  parser, and it is why the workflows in this repository are formatted
#  consistently.
# -----------------------------------------------------------------------------
TOP_LEVEL_PERMISSIONS_RE = re.compile(r"^permissions:\s*(?P<value>.*)$", re.MULTILINE)
JOBS_BLOCK_RE = re.compile(r"^jobs:\s*$", re.MULTILINE)
JOB_KEY_RE = re.compile(r"^  (?P<job>[A-Za-z_][A-Za-z0-9_-]*):\s*$")
JOB_PERMISSIONS_RE = re.compile(r"^    permissions:\s*(?P<value>.*)$")
USES_CHECKOUT_RE = re.compile(r"""uses:\s*["']?actions/checkout@""")
PERSIST_RE = re.compile(r"persist-credentials:\s*false")
WRITE_ALL_RE = re.compile(r"permissions:\s*write-all")


class Violation(NamedTuple):
    workflow: str
    rule: int
    message: str
    remedy: str


def check_workflow(path: Path) -> List[Violation]:
    """Apply the five rules to one workflow file."""
    violations: List[Violation] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    name = path.name

    # -- rule 1 and 2: a top-level, empty permissions block --------------------
    top = TOP_LEVEL_PERMISSIONS_RE.search(text)
    if top is None:
        violations.append(
            Violation(
                workflow=name,
                rule=1,
                message="no top-level permissions block",
                remedy=(
                    "Add `permissions: {}` at the top level. Without it the job "
                    "inherits the repository default, which is broader than any "
                    "job here needs."
                ),
            )
        )
    else:
        value = top.group("value").strip()
        if value not in {"{}", ""}:
            violations.append(
                Violation(
                    workflow=name,
                    rule=2,
                    message=f"top-level permissions is {value!r} rather than empty",
                    remedy=(
                        "Use `permissions: {}` and grant each job what it needs. "
                        "A workflow-level grant applies to every job including "
                        "the ones that do not need it."
                    ),
                )
            )
        elif value == "":
            # `permissions:` followed by an indented mapping is a grant, not a
            # denial. Look at the next non-blank line to tell them apart.
            start = text[: top.start()].count("\n")
            for following in lines[start + 1 :]:
                if not following.strip():
                    continue
                if following.startswith(("  ", "\t")):
                    violations.append(
                        Violation(
                            workflow=name,
                            rule=2,
                            message="top-level permissions grants scopes to every job",
                            remedy="Use `permissions: {}` and move the grants into the jobs that need them.",
                        )
                    )
                break

    # -- rule 4: never write-all ---------------------------------------------
    for line_no, line in enumerate(lines, start=1):
        if WRITE_ALL_RE.search(line):
            violations.append(
                Violation(
                    workflow=f"{name}:{line_no}",
                    rule=4,
                    message="write-all requested",
                    remedy="Name the individual scopes. write-all is never necessary here.",
                )
            )

    # -- rule 3: every job declares permissions -------------------------------
    jobs_match = JOBS_BLOCK_RE.search(text)
    if jobs_match:
        jobs_start = text[: jobs_match.start()].count("\n") + 1
        current_job = ""
        job_start_line = 0
        job_has_permissions = False

        def close_job() -> None:
            if current_job and not job_has_permissions:
                violations.append(
                    Violation(
                        workflow=f"{name}:{job_start_line}",
                        rule=3,
                        message=f"job {current_job!r} declares no permissions block",
                        remedy=(
                            "Add an explicit `permissions:` to the job, even if it "
                            "is `permissions: {}`. Explicit least privilege is "
                            "reviewable; inheritance is not."
                        ),
                    )
                )

        for offset, line in enumerate(lines[jobs_start:], start=jobs_start + 1):
            # A new top-level key ends the jobs block.
            if line and not line.startswith((" ", "\t")) and line.rstrip().endswith(":"):
                break
            job = JOB_KEY_RE.match(line)
            if job:
                close_job()
                current_job = job.group("job")
                job_start_line = offset
                job_has_permissions = False
                continue
            if current_job and JOB_PERMISSIONS_RE.match(line):
                job_has_permissions = True
        close_job()

    # -- rule 5: persist-credentials on every checkout ------------------------
    for line_no, line in enumerate(lines, start=1):
        if not USES_CHECKOUT_RE.search(line):
            continue
        # Look ahead through the step's `with:` block. Ten lines is generous;
        # a checkout step with more than that is doing something unusual and
        # deserves a manual look anyway.
        window = "\n".join(lines[line_no : line_no + 10])
        if not PERSIST_RE.search(window):
            violations.append(
                Violation(
                    workflow=f"{name}:{line_no}",
                    rule=5,
                    message="checkout does not set persist-credentials: false",
                    remedy=(
                        "Add `with: { persist-credentials: false }`. By default "
                        "the token is written into .git/config where every later "
                        "step in the job can read it."
                    ),
                )
            )

    return violations


def main() -> int:
    if not WORKFLOW_DIR.is_dir():
        print(f"error: {WORKFLOW_DIR} does not exist", file=sys.stderr)
        return 2

    paths = sorted(
        [*WORKFLOW_DIR.glob("*.yml"), *WORKFLOW_DIR.glob("*.yaml")]
    )
    if not paths:
        print("error: no workflow files found", file=sys.stderr)
        return 2

    violations: List[Violation] = []
    for path in paths:
        violations.extend(check_workflow(path))

    if not violations:
        print(f"OK: {len(paths)} workflow(s) follow least privilege.")
        return 0

    print(f"{len(violations)} workflow permission violation(s):\n", file=sys.stderr)
    for v in violations:
        print(f"  {v.workflow}  [rule {v.rule}]", file=sys.stderr)
        print(f"    problem: {v.message}", file=sys.stderr)
        print(f"    remedy:  {v.remedy}\n", file=sys.stderr)
    print(
        "The five rules are documented at the top of this script and in "
        "SECURITY.md section 3.3.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
