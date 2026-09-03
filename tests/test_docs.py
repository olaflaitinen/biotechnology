# =============================================================================
#  tests/test_docs.py
# -----------------------------------------------------------------------------
#  The documentation generator.
#
#  WHAT IS WORTH ASSERTING ABOUT A GENERATOR WHOSE OUTPUT IS COMMITTED
#  Three things, and none of them is "it produced files".
#
#      1. THE COMMITTED TREE IS CURRENT. If `docs/` and the taxonomy disagree,
#         the published site is wrong and nobody finds out until a reader does.
#      2. IT IS DETERMINISTIC. A generator that reorders anything produces a
#         diff on every run, and a tree that always looks changed stops being
#         reviewed.
#      3. IT DOES NOT DESTROY AUTHORED PAGES. The guide is prose that cannot
#         be derived from the data, and a regeneration that flattened it would
#         be a bug rather than a rebuild.
#
#  These run the generator into a temporary directory rather than over `docs/`,
#  so a test run never modifies the working tree.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple

import pytest

import biotechnology as bt
from biotechnology.core.models import Subtype

ROOT = Path(__file__).resolve().parent.parent
GENERATOR = ROOT / "tools" / "generate_docs.py"
DOCS = ROOT / "docs"


def generate(into: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--output", str(into)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    assert result.returncode == 0, result.stderr


@pytest.fixture(scope="session")
def generated(tmp_path_factory) -> Path:
    out = tmp_path_factory.mktemp("docs")
    generate(out)
    return out


# =============================================================================
#  DETERMINISM
# =============================================================================


@pytest.mark.slow
def test_two_runs_are_identical(tmp_path: Path) -> None:
    first = tmp_path / "one"
    second = tmp_path / "two"
    generate(first)
    generate(second)

    files = sorted(p.relative_to(first) for p in first.rglob("*.md"))
    assert files == sorted(p.relative_to(second) for p in second.rglob("*.md"))
    for relative in files:
        assert (first / relative).read_bytes() == (second / relative).read_bytes(), relative


def test_output_uses_unix_line_endings(generated: Path) -> None:
    """The tree is committed, so a platform-dependent newline shows every
    line as changed in a diff produced on the other platform."""
    for page in generated.rglob("*.md"):
        assert b"\r\n" not in page.read_bytes(), page.name


# =============================================================================
#  COMPLETENESS
# =============================================================================


def test_every_written_record_has_a_page(
    generated: Path, all_subtypes: Tuple[Subtype, ...]
) -> None:
    for subtype in all_subtypes:
        page = generated / "branches" / subtype.branch_key / "{0}.md".format(subtype.key)
        assert page.exists(), subtype.path


def test_every_colour_has_an_index_even_when_pending(
    generated: Path, colour_order: Tuple[str, ...]
) -> None:
    """A pending branch gets a page saying so.

    Omitting it would leave a dead entry in the mkdocs navigation, which is a
    build failure under `--strict` and a broken link without it.
    """
    for key in colour_order:
        assert (generated / "branches" / key / "index.md").exists(), key


def test_every_page_mkdocs_navigates_exists(generated: Path) -> None:
    """The navigation and the tree must agree.

    Read out of `mkdocs.yml` rather than duplicated here, so adding a page to
    the navigation without generating it fails this test rather than the site
    build.
    """
    nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    pages = re.findall(r'"([a-z0-9/\-]+\.md)"', nav)
    assert pages
    missing = [p for p in pages if not (generated / p).exists()]
    assert not missing, "navigated but not generated: {0}".format(missing)


# =============================================================================
#  HONESTY
# =============================================================================


def test_index_pages_state_coverage(
    generated: Path, pending_colours: Tuple[str, ...]
) -> None:
    """A reader arriving from a search engine never sees the home page.

    So the coverage note is repeated on every index rather than centralised,
    and a tree that presented six branches without saying there are ten would
    mislead by omission.
    """
    if not pending_colours:  # pragma: no cover - future state
        pytest.skip("the taxonomy is complete")
    for page in ("index.md", "branches/index.md"):
        text = (generated / page).read_text(encoding="utf-8")
        assert "of 10 branches" in text
        for colour in pending_colours:
            assert colour in text


def test_unwritten_registries_list_what_they_owe(generated: Path) -> None:
    """A placeholder page carries the work item rather than an apology.

    The keys the taxonomy references are the specification of what the
    registry has to contain, and this is the only place a contributor can see
    the whole list.
    """
    text = (generated / "registries" / "organisms.md").read_text(encoding="utf-8")
    assert "Not written yet" in text
    assert "pseudomonas_putida" in text


def test_generated_pages_are_marked_as_generated(generated: Path) -> None:
    """The first thing anyone does with a docs tree is edit a page in it."""
    text = (generated / "branches" / "grey" / "biomining.md").read_text(encoding="utf-8")
    assert "GENERATED FILE" in text
    assert "generate_docs.py" in text


# =============================================================================
#  AUTHORED PAGES ARE NOT DESTROYED
# =============================================================================


def test_guide_pages_survive_regeneration(tmp_path: Path) -> None:
    out = tmp_path / "docs"
    generate(out)

    page = out / "guide" / "getting-started.md"
    assert page.exists()
    page.write_text("# Mine\n\nHand written.\n", encoding="utf-8", newline="\n")

    generate(out)
    assert page.read_text(encoding="utf-8") == "# Mine\n\nHand written.\n"


# =============================================================================
#  THE COMMITTED TREE
# =============================================================================


@pytest.mark.slow
def test_committed_docs_are_current(tmp_path: Path) -> None:
    """`docs/` must match what the generator produces today.

    If this fails, someone changed a record and did not run `make docs`, and
    the published site is describing a taxonomy that no longer exists.
    """
    if not DOCS.exists():  # pragma: no cover - fresh checkout
        pytest.skip("docs/ has not been generated")

    fresh = tmp_path / "fresh"
    generate(fresh)

    stale = []
    for page in fresh.rglob("*.md"):
        relative = page.relative_to(fresh)
        if relative.parts[0] == "guide":
            continue  # authored, deliberately not regenerated
        committed = DOCS / relative
        if not committed.exists() or committed.read_bytes() != page.read_bytes():
            stale.append(str(relative))

    assert not stale, "run `make docs`; out of date: {0}".format(sorted(stale)[:10])
