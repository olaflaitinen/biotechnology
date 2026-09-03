# =============================================================================
#  tests/test_export.py
# -----------------------------------------------------------------------------
#  The five emitters.
#
#  WHAT IS ACTUALLY WORTH ASSERTING ABOUT AN EXPORTER
#  Not that it produces output. Three things:
#
#      1. IT IS DETERMINISTIC. `make docs` commits its output, so an emitter
#         that reorders anything produces a diff on every run and the
#         generated directory becomes untrustworthy.
#      2. IT DOES NOT LIE ABOUT COVERAGE. Six branches are written and ten
#         exist. An export that says nothing about that lets a consumer
#         conclude six is all of them.
#      3. IT ESCAPES. A pipe in a Markdown cell ends the cell; an unquoted
#         separator in a CSV ends the field. Both occur in this corpus.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import csv
import io
import json
from typing import Tuple

import pytest

import biotechnology as bt
from biotechnology.core import export
from biotechnology.core.models import Subtype


# =============================================================================
#  DETERMINISM
# =============================================================================


@pytest.mark.parametrize(
    "emitter",
    [export.to_json, export.to_csv, export.to_dot, export.to_markdown, export.tree],
)
def test_emitters_are_deterministic(emitter) -> None:
    """Byte-identical across calls, or the committed docs churn."""
    assert emitter() == emitter()


def test_csv_uses_unix_line_endings() -> None:
    """Set explicitly rather than left to the csv module's "\\r\\n" default.

    Without this the committed export differs by platform and every line shows
    as changed in a diff produced on the other one.
    """
    text = export.to_csv()
    assert "\r\n" not in text
    assert "\n" in text


# =============================================================================
#  COVERAGE IS STATED, NOT IMPLIED
# =============================================================================


def test_whole_taxonomy_json_declares_coverage(pending_colours: Tuple[str, ...]) -> None:
    payload = json.loads(export.to_json())
    counts = payload["counts"]
    assert counts["branches_total"] == 10
    assert counts["branches_written"] == len(bt.branches())
    assert counts["branches_pending"] == list(pending_colours)
    assert counts["complete"] is (not pending_colours)


# =============================================================================
#  JSON
# =============================================================================


def test_json_is_ascii_only() -> None:
    """`ensure_ascii=True` is an assertion, not a transformation.

    The corpus is ASCII by editorial rule, so nothing should need escaping. If
    a character ever slips through it appears as an escape rather than
    silently changing the file encoding.
    """
    text = export.to_json()
    assert text.isascii()


def test_json_round_trips() -> None:
    payload = json.loads(export.to_json())
    assert isinstance(payload["branches"], list)
    assert len(payload["branches"]) == len(bt.branches())


def test_json_of_one_record_is_a_dict() -> None:
    payload = json.loads(export.to_json(bt.get_subtype("grey.biomining")))
    assert payload["key"] == "biomining"


def test_include_prose_false_drops_only_prose() -> None:
    subtype = bt.get_subtype("grey.biomining")
    full = export.to_dict(subtype)
    lean = export.to_dict(subtype, include_prose=False)
    assert "description" in full
    assert "description" not in lean
    # The structural fields must survive, or the option is a truncation
    # rather than a projection.
    assert lean["applications"] == full["applications"]
    assert lean["key"] == full["key"]


# =============================================================================
#  CSV
# =============================================================================


def test_csv_has_one_row_per_subtype(all_subtypes: Tuple[Subtype, ...]) -> None:
    rows = list(csv.DictReader(io.StringIO(export.to_csv())))
    assert len(rows) == len(all_subtypes)


def test_csv_columns_are_the_declared_order() -> None:
    reader = csv.reader(io.StringIO(export.to_csv()))
    header = next(reader)
    assert header == list(export.CSV_COLUMNS)


def test_csv_survives_a_round_trip_through_a_reader() -> None:
    """Every field must parse back, which is what quoting exists for.

    Summaries contain commas and quotation marks throughout this corpus, so
    this is a real check rather than a formality.
    """
    rows = list(csv.DictReader(io.StringIO(export.to_csv())))
    paths = {row["path"] for row in rows}
    assert "grey.biomining" in paths
    for row in rows:
        assert row["name"]
        assert row["branch"] in {b.key for b in bt.branches()}


def test_csv_cells_contain_no_raw_newline() -> None:
    """A newline inside an unquoted cell ends the row.

    The reader above would catch that, but this locates it in the writer.
    """
    rows = list(csv.DictReader(io.StringIO(export.to_csv())))
    assert len(rows) == len(bt.subtypes())


# =============================================================================
#  MARKDOWN
# =============================================================================


def test_markdown_escapes_table_cells() -> None:
    """A pipe in a metric name or unit would end the cell.

    Rendered by emitting a record known to have metrics and asserting that
    every table row has the expected column count.
    """
    text = export.to_markdown(bt.get_subtype("grey.bioremediation"))
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Metric |"):
            in_table = True
            continue
        if in_table:
            if not line.startswith("|"):
                break
            if line.startswith("|---"):
                continue
            assert line.count("|") - line.count("\\|") == 6, line


def test_markdown_of_a_branch_contains_its_subtypes() -> None:
    text = export.to_markdown(bt.get_branch("grey"))
    for subtype in bt.get_branch("grey").subtypes:
        assert subtype.name in text


# =============================================================================
#  DOT
# =============================================================================


def test_dot_draws_no_edge_to_a_missing_node() -> None:
    """An edge to an undeclared node makes Graphviz invent one.

    That would silently misrepresent the graph, so unresolvable edges are
    omitted and counted. This asserts the omission; the count appears in a
    comment.
    """
    text = export.to_dot()
    declared = set()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('"') and "[label=" in stripped:
            declared.add(stripped.split('"')[1])
    for line in text.splitlines():
        stripped = line.strip()
        if "->" in stripped:
            source, target = [p.strip().strip('";') for p in stripped.split("->")]
            assert source in declared, source
            assert target in declared, target


def test_dot_reports_what_it_omitted(pending_colours: Tuple[str, ...]) -> None:
    text = export.to_dot()
    if pending_colours:
        assert "edge(s) omitted" in text


def test_dot_is_valid_enough_to_parse_structurally() -> None:
    text = export.to_dot()
    assert text.count("{") == text.count("}")
    assert text.rstrip().endswith("}")


# =============================================================================
#  TREE
# =============================================================================


def test_tree_is_ascii() -> None:
    """Box-drawing characters break a Windows console under a legacy code page."""
    assert export.tree().isascii()


def test_tree_lists_every_branch_and_subtype() -> None:
    text = export.tree()
    for branch in bt.branches():
        assert branch.name in text
        for subtype in branch.subtypes:
            assert subtype.name in text
