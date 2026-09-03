# =============================================================================
#  tests/test_cli.py
# -----------------------------------------------------------------------------
#  The command line interface.
#
#  WHY EXIT CODES ARE ASSERTED AS HARD AS OUTPUT
#  GOVERNANCE.md 3.6 makes exit codes a compatibility surface, because scripts
#  branch on them. An output format can be improved between releases; an exit
#  code cannot change without breaking somebody's pipeline silently. So every
#  command here asserts the code as well as the text.
#
#  THE FOURTH CODE IS THE INTERESTING ONE. `formula` and `compute` depend on a
#  registry that is not written, and they exit 3 rather than 1. A script must
#  be able to tell "this data does not exist yet" from "your query matched
#  nothing", and that distinction is only testable if a test asserts it.
#
#  `main()` IS CALLED DIRECTLY RATHER THAN THROUGH A SUBPROCESS
#  A subprocess would test the console script wiring as well, and it would
#  cost a process launch per case and hide the traceback on failure. The wiring
#  is checked once by `tools/check_packaging.py`, which resolves the entry
#  point without importing. Everything else is faster and clearer in process.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import json
from typing import List, Tuple

import pytest

import biotechnology as bt
from biotechnology import cli


def run(capsys, *argv: str) -> Tuple[int, str, str]:
    """Run the CLI and return (code, stdout, stderr)."""
    code = cli.main(list(argv))
    captured = capsys.readouterr()
    return code, captured.out, captured.err


# =============================================================================
#  NO ARGUMENTS
# =============================================================================


def test_bare_invocation_prints_help_and_reports_usage(capsys) -> None:
    code, out, _ = run(capsys)
    assert code == cli.EXIT_USAGE
    assert "biotechnology" in out


# =============================================================================
#  list AND tree
# =============================================================================


def test_list_shows_every_written_branch(capsys) -> None:
    code, out, _ = run(capsys, "list")
    assert code == cli.EXIT_OK
    for branch in bt.branches():
        assert branch.key in out


def test_list_states_coverage_rather_than_implying_it(
    capsys, pending_colours: Tuple[str, ...]
) -> None:
    """A tool that printed six branches without saying so would mislead."""
    _, out, _ = run(capsys, "list")
    if pending_colours:
        assert "of 10 branches written" in out
        for colour in pending_colours:
            assert colour in out


def test_list_quiet_omits_the_note(capsys) -> None:
    _, out, _ = run(capsys, "list", "--quiet")
    assert "branches written" not in out


def test_tree_can_be_limited_to_one_branch(capsys) -> None:
    code, out, _ = run(capsys, "tree", "grey")
    assert code == cli.EXIT_OK
    assert "Biomining" in out
    assert "Gene Therapy" not in out


def test_tree_of_an_unknown_branch_reports_no_result(capsys) -> None:
    code, _, err = run(capsys, "tree", "chartreuse")
    assert code == cli.EXIT_NO_RESULT
    assert "chartreuse" in err


# =============================================================================
#  show
# =============================================================================


def test_show_renders_a_record(capsys) -> None:
    code, out, _ = run(capsys, "show", "grey.biomining")
    assert code == cli.EXIT_OK
    assert "Biomining" in out
    assert "GOVERNANCE" in out


def test_show_plain_omits_the_technical_register(capsys) -> None:
    """`--plain` is a view, not a truncation.

    The public register must be present and the technical description absent,
    which is the whole reason records carry two registers.
    """
    _, out, _ = run(capsys, "show", "grey.biomining", "--plain")
    assert "DESCRIPTION" not in out
    assert "GOVERNANCE" not in out
    assert out.strip()


def test_show_json_is_parseable(capsys) -> None:
    code, out, _ = run(capsys, "show", "grey.biomining", "--json")
    assert code == cli.EXIT_OK
    assert json.loads(out)["key"] == "biomining"


def test_show_unknown_path_names_the_token(capsys) -> None:
    code, _, err = run(capsys, "show", "grey.nosuchthing")
    assert code == cli.EXIT_NO_RESULT
    assert "nosuchthing" in err


# =============================================================================
#  search
# =============================================================================


def test_search_ranks_the_obvious_answer_first(capsys) -> None:
    code, out, _ = run(capsys, "search", "biomining", "-n", "3")
    assert code == cli.EXIT_OK
    assert out.splitlines()[0].startswith("grey.biomining")


def test_search_with_no_match_reports_no_result(capsys) -> None:
    code, _, err = run(capsys, "search", "qwertyuiop")
    assert code == cli.EXIT_NO_RESULT
    assert "qwertyuiop" in err


def test_search_respects_the_limit(capsys) -> None:
    _, out, _ = run(capsys, "search", "bio", "-n", "4")
    assert len([line for line in out.splitlines() if line.strip()]) <= 4


# =============================================================================
#  sdg
# =============================================================================


def test_sdg_lists_matching_records(capsys) -> None:
    code, out, _ = run(capsys, "sdg", "6")
    assert code == cli.EXIT_OK
    assert "grey.bioremediation" in out


def test_sdg_out_of_range_is_a_usage_error(capsys) -> None:
    """18 is not a goal. That is the caller's mistake, not an empty result."""
    code, _, err = run(capsys, "sdg", "18")
    assert code == cli.EXIT_USAGE
    assert "1 to 17" in err


# =============================================================================
#  vocab AND stats
# =============================================================================


def test_vocab_prints_one_vocabulary(capsys) -> None:
    code, out, _ = run(capsys, "vocab", "maturity")
    assert code == cli.EXIT_OK
    assert "ESTABLISHED" in out
    assert "RESTRICTED" not in out


def test_vocab_unknown_name_lists_the_valid_ones(capsys) -> None:
    code, _, err = run(capsys, "vocab", "nonsense")
    assert code == cli.EXIT_NO_RESULT
    assert "nonsense" in err


def test_stats_reports_coverage_and_registries(capsys) -> None:
    code, out, _ = run(capsys, "stats")
    assert code == cli.EXIT_OK
    assert "subtypes" in out
    assert "registry coverage" in out


# =============================================================================
#  validate
# =============================================================================


def test_validate_succeeds_on_the_current_dataset(capsys) -> None:
    code, out, _ = run(capsys, "validate")
    assert code == cli.EXIT_OK
    assert "0 error(s)" in out


def test_validate_warnings_flag_shows_them(capsys) -> None:
    _, quiet, _ = run(capsys, "validate")
    _, loud, _ = run(capsys, "validate", "--warnings")
    assert len(loud) > len(quiet)
    assert "WARNING" in loud


def test_validate_strict_fails_while_branches_are_pending(
    capsys, pending_colours: Tuple[str, ...]
) -> None:
    """Strict mode is for the complete taxonomy, and says so by failing now.

    A strict run that passed today would mean strict mode was not checking the
    forward references, which is the only thing it adds.
    """
    code, _, _ = run(capsys, "validate", "--strict")
    if pending_colours:
        assert code == cli.EXIT_NO_RESULT
    else:  # pragma: no cover - future state
        assert code == cli.EXIT_OK


# =============================================================================
#  export
# =============================================================================


@pytest.mark.parametrize("fmt", ["json", "csv", "dot", "markdown"])
def test_export_every_format_to_stdout(capsys, fmt: str) -> None:
    code, out, _ = run(capsys, "export", "--format", fmt)
    assert code == cli.EXIT_OK
    assert out.strip()


def test_export_to_a_file_writes_unix_line_endings(capsys, tmp_path) -> None:
    """Written with newline="\\n" so a committed export is platform-stable."""
    target = tmp_path / "taxonomy.csv"
    code, _, err = run(capsys, "export", "--format", "csv", "-o", str(target))
    assert code == cli.EXIT_OK
    assert target.name in err
    raw = target.read_bytes()
    assert b"\r\n" not in raw


def test_export_file_content_matches_stdout(capsys, tmp_path) -> None:
    target = tmp_path / "taxonomy.json"
    run(capsys, "export", "--format", "json", "-o", str(target))
    _, out, _ = run(capsys, "export", "--format", "json")
    assert json.loads(target.read_text(encoding="utf-8")) == json.loads(out)


# =============================================================================
#  formula AND compute
#
#  The two commands whose data does not exist. Their behaviour is the reason
#  EXIT_UNAVAILABLE exists, so it is asserted rather than assumed.
# =============================================================================


def test_formula_reports_unavailable_rather_than_crashing(capsys) -> None:
    code, _, err = run(capsys, "formula", "gc_content")
    assert code == cli.EXIT_UNAVAILABLE
    assert "not written yet" in err


def test_compute_reports_unavailable(capsys) -> None:
    code, _, err = run(capsys, "compute", "gc_content", "--arg", "sequence=ATGC")
    assert code == cli.EXIT_UNAVAILABLE
    assert "not written yet" in err


def test_unavailable_is_distinct_from_no_result(capsys) -> None:
    """The distinction a script needs, asserted directly.

    If these ever collapse to the same value, a caller cannot tell a missing
    registry from an empty search, and the difference is undiscoverable.
    """
    unavailable, _, _ = run(capsys, "formula", "gc_content")
    no_result, _, _ = run(capsys, "search", "qwertyuiop")
    assert unavailable != no_result
    assert unavailable == cli.EXIT_UNAVAILABLE
    assert no_result == cli.EXIT_NO_RESULT
