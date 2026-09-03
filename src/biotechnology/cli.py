# =============================================================================
#  biotechnology.cli
# -----------------------------------------------------------------------------
#  The command line interface. Eleven subcommands, documented in README.md and
#  reachable as `biotechnology ...` or `python -m biotechnology ...`.
#
#  WHY THIS FILE WAS REWRITTEN RATHER THAN REPAIRED
#  The previous version imported a layer that no longer exists:
#
#      cli.py       -> biotechnology/registry.py
#      registry.py  -> biotechnology/data.py     <- never existed
#      cli.py       -> biotechnology/models.py   <- an 8-field Subtype, where
#                                                   the real one has 28
#
#  So the console script declared in `pyproject.toml` and the `python -m`
#  entry point were both broken, and `make validate`, which runs
#  `python -m biotechnology validate --strict`, could never have run. The
#  stale trio is deleted in the same commit as this rewrite; nothing else
#  imported it.
#
#  EXIT CODES ARE PUBLIC API
#  GOVERNANCE.md 3.6 treats CLI exit codes as a compatibility surface, because
#  scripts branch on them. They are named constants here rather than integer
#  literals scattered through the handlers, so that the contract is stated in
#  one place and cannot drift:
#
#      0  success
#      1  the command ran and the answer was negative: validation found
#         errors, a search matched nothing, a lookup found no record
#      2  the command could not run: bad arguments, unknown subcommand
#      3  the feature exists but its data does not yet, which currently means
#         the formula registry
#
#  Three rather than folding into two matters for a caller. "No results" and
#  "not implemented yet" demand different responses from a script, and
#  collapsing them would make the difference undiscoverable.
#
#  OUTPUT IS PLAIN TEXT AND ASCII
#  No colour, no box drawing, no progress indicator. Output is piped more often
#  than it is read, the project forbids non-ASCII, and a Windows console under
#  a legacy code page mangles anything else. Machine-readable output is what
#  `export` is for.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

from . import __version__
from .core import enums, export, registry, search as search_module, validation
from .core.errors import BiotechnologyError

__all__ = ["main", "build_parser", "EXIT_OK", "EXIT_NO_RESULT", "EXIT_USAGE", "EXIT_UNAVAILABLE"]


# =============================================================================
#  EXIT CODES
# =============================================================================

EXIT_OK = 0
EXIT_NO_RESULT = 1
EXIT_USAGE = 2
EXIT_UNAVAILABLE = 3


# =============================================================================
#  SMALL OUTPUT HELPERS
#
#  Every handler writes through these rather than calling print directly, so
#  that stream choice is consistent: results to stdout, diagnostics to stderr.
#  A caller piping `biotechnology list` into a file should not receive a
#  warning in the middle of the data.
# =============================================================================


def _out(text: str = "") -> None:
    print(text, file=sys.stdout)


def _err(text: str) -> None:
    print(text, file=sys.stderr)


def _rule(width: int = 74) -> str:
    return "-" * width


def _wrap(text: str, width: int = 78, indent: str = "") -> str:
    """Wrap prose for a terminal.

    `textwrap` is used through a thin helper rather than directly so that the
    indent convention is applied in one place. Long records are the norm here,
    and an unwrapped six hundred word field is unreadable in a terminal.
    """
    import textwrap

    if not text:
        return ""
    return textwrap.fill(
        text, width=width, initial_indent=indent, subsequent_indent=indent
    )


# =============================================================================
#  SUBCOMMAND: list
# =============================================================================


def cmd_list(args: argparse.Namespace) -> int:
    """List the branches, and say plainly which are not written yet."""
    from .branches import COLOUR_ORDER, PENDING_COLOURS

    for branch in registry.branches():
        _out(
            "{0:8} {1:26} {2:>2} subtypes  {3}".format(
                branch.key, branch.name, len(branch.subtypes), branch.colour
            )
        )

    if PENDING_COLOURS and not args.quiet:
        _out()
        _out(
            "{0} of {1} branches written. Pending: {2}.".format(
                len(COLOUR_ORDER) - len(PENDING_COLOURS),
                len(COLOUR_ORDER),
                ", ".join(PENDING_COLOURS),
            )
        )
    return EXIT_OK


# =============================================================================
#  SUBCOMMAND: tree
# =============================================================================


def cmd_tree(args: argparse.Namespace) -> int:
    if args.branch:
        try:
            node = registry.get_branch(args.branch)
        except BiotechnologyError as exc:
            _err(str(exc))
            return EXIT_NO_RESULT
        _out(export.tree(node, show_summary=args.summary).rstrip())
        return EXIT_OK

    _out(export.tree(show_summary=args.summary).rstrip())
    return EXIT_OK


# =============================================================================
#  SUBCOMMAND: show
# =============================================================================


def cmd_show(args: argparse.Namespace) -> int:
    try:
        node = registry.get(args.path)
    except BiotechnologyError as exc:
        _err(str(exc))
        return EXIT_NO_RESULT

    if args.json:
        _out(export.to_json(node))
        return EXIT_OK

    if args.markdown:
        _out(export.to_markdown(node).rstrip())
        return EXIT_OK

    if args.plain:
        return _show_plain(node)

    return _show_full(node)


def _show_plain(node: object) -> int:
    """The public register only.

    A deliberate view rather than a truncation. The whole point of carrying two
    registers is that a non-specialist can read one of them without wading
    through the other, and a `--plain` that merely shortened the technical text
    would defeat that.
    """
    _out(getattr(node, "name", ""))
    _out(_rule())
    for label, field in (
        ("", "plain_language"),
        ("An analogy.", "analogy"),
        ("Why it matters.", "why_it_matters"),
    ):
        value = getattr(node, field, "")
        if not value:
            continue
        _out()
        if label:
            _out(label)
        _out(_wrap(value))
    return EXIT_OK


def _show_full(node: object) -> int:
    name = getattr(node, "name", "")
    path = getattr(node, "path", getattr(node, "key", ""))

    _out("{0}  [{1}]".format(name, path))
    _out(_rule())
    _out(_wrap(getattr(node, "summary", "")))

    for title, field in (
        ("DESCRIPTION", "description"),
        ("IN PLAIN LANGUAGE", "plain_language"),
        ("AN ANALOGY", "analogy"),
        ("WHY IT MATTERS", "why_it_matters"),
        ("ON THE NAME", "origin_note"),
    ):
        value = getattr(node, field, "")
        if value:
            _out()
            _out(title)
            _out(_wrap(value))

    for title, field in (
        ("APPLICATIONS", "applications"),
        ("TECHNOLOGIES", "technologies"),
        ("CHALLENGES", "challenges"),
        ("REGULATIONS", "regulations"),
        ("STANDARDS", "standards"),
        ("KEY QUESTIONS", "key_questions"),
    ):
        values = getattr(node, field, ())
        if values:
            _out()
            _out(title)
            for item in values:
                _out("  - " + item)

    metrics = getattr(node, "metrics", ())
    if metrics:
        _out()
        _out("METRICS")
        for metric in metrics:
            _out(
                "  {0:38} {1:12} {2}".format(
                    metric.name[:38], metric.symbol[:12], metric.unit
                )
            )

    milestones = getattr(node, "timeline", ()) or getattr(node, "milestones", ())
    if milestones:
        _out()
        _out("HISTORY")
        for milestone in milestones:
            _out("  {0:>6}  {1}".format(milestone.year, milestone.event))

    if hasattr(node, "maturity"):
        _out()
        _out("GOVERNANCE")
        _out("  maturity          {0}".format(node.maturity.name))
        _out("  risk tier         {0}".format(node.risk_tier.name))
        _out("  scale             {0}".format(node.scale.name))
        _out("  regulatory status {0}".format(node.regulatory_status.name))
        _out("  domains           {0}".format(", ".join(d.name for d in node.domains) or "-"))
        _out("  SDGs              {0}".format(", ".join(str(g) for g in node.sdgs) or "-"))

    related = getattr(node, "related", ())
    if related:
        _out()
        _out("RELATED")
        for item in related:
            _out("  " + item)

    return EXIT_OK


# =============================================================================
#  SUBCOMMAND: search
# =============================================================================


def cmd_search(args: argparse.Namespace) -> int:
    results = search_module.search_scored(args.query, limit=args.number)
    if not results:
        _err("no match for {0!r}".format(args.query))
        return EXIT_NO_RESULT

    for node, score in results:
        path = getattr(node, "path", node.key)
        line = "{0:34} {1}".format(path, node.name)
        if args.scores:
            line = "{0:5}  {1}".format(score, line)
        _out(line)
    return EXIT_OK


# =============================================================================
#  SUBCOMMAND: sdg
# =============================================================================


def cmd_sdg(args: argparse.Namespace) -> int:
    if not 1 <= args.goal <= 17:
        _err("SDG {0} does not exist; the goals are numbered 1 to 17".format(args.goal))
        return EXIT_USAGE

    matches = registry.by_sdg(args.goal)
    if not matches:
        _err("no record cites SDG {0}".format(args.goal))
        return EXIT_NO_RESULT

    for subtype in matches:
        _out("{0:34} {1}".format(subtype.path, subtype.name))
    return EXIT_OK


# =============================================================================
#  SUBCOMMAND: vocab
# =============================================================================


def cmd_vocab(args: argparse.Namespace) -> int:
    available = enums.vocabularies()

    if args.name:
        wanted = args.name.strip().lower()
        match = {k.lower(): v for k, v in available.items()}.get(wanted)
        if match is None:
            _err(
                "unknown vocabulary {0!r}; valid: {1}".format(
                    args.name, ", ".join(sorted(available))
                )
            )
            return EXIT_NO_RESULT
        _print_vocabulary(args.name, match)
        return EXIT_OK

    for name in sorted(available):
        _print_vocabulary(name, available[name])
        _out()
    return EXIT_OK


def _print_vocabulary(name: str, members: object) -> None:
    _out(name.upper())
    for member in members:  # type: ignore[union-attr]
        explanation = getattr(member, "explanation", "") or getattr(member, "label", "")
        _out("  {0:14} {1}".format(member.name, explanation))


# =============================================================================
#  SUBCOMMAND: stats
# =============================================================================


def cmd_stats(args: argparse.Namespace) -> int:
    from .branches import COLOUR_ORDER, PENDING_COLOURS

    counts = registry.counts()
    _out("branches written   {0} of {1}".format(len(registry.branches()), len(COLOUR_ORDER)))
    if PENDING_COLOURS:
        _out("branches pending   {0}".format(", ".join(PENDING_COLOURS)))
    _out("subtypes           {0}".format(len(registry.subtypes())))

    for key in sorted(counts):
        if key in {"branches", "subtypes"}:
            continue
        value = counts[key]
        if isinstance(value, dict):
            _out()
            _out(key.replace("_", " "))
            for inner in sorted(value):
                _out("  {0:20} {1}".format(inner, value[inner]))
        elif isinstance(value, list):
            _out("{0:18} {1}".format(key.replace("_", " "), ", ".join(str(v) for v in value)))
        else:
            _out("{0:18} {1}".format(key.replace("_", " "), value))

    _out()
    _out("registry coverage (referenced keys that resolve)")
    for name, figures in sorted(validation.registry_coverage().items()):
        _out(
            "  {0:12} {1:5} of {2:5}".format(
                name, figures["resolved"], figures["referenced"]
            )
        )
    return EXIT_OK


# =============================================================================
#  SUBCOMMAND: validate
# =============================================================================


def cmd_validate(args: argparse.Namespace) -> int:
    findings = validation.validate(strict=args.strict, raise_on_error=False)
    errors = [f for f in findings if f.is_error]
    warnings = [f for f in findings if not f.is_error]

    show = findings if (args.warnings or args.strict) else errors
    for finding in show:
        _out(str(finding))

    if show:
        _out()
    _out(
        "{0} error(s), {1} warning(s) across {2} record(s).".format(
            len(errors), len(warnings), len(registry.subtypes())
        )
    )
    if warnings and not args.warnings and not args.strict:
        _out("Re-run with --warnings to see them.")

    return EXIT_NO_RESULT if errors else EXIT_OK


# =============================================================================
#  SUBCOMMAND: export
# =============================================================================


def cmd_export(args: argparse.Namespace) -> int:
    emitters = {
        "json": lambda: export.to_json(),
        "csv": lambda: export.to_csv(),
        "dot": lambda: export.to_dot(),
        "markdown": lambda: export.to_markdown(),
    }
    emit = emitters.get(args.format)
    if emit is None:  # pragma: no cover - argparse restricts the choices
        _err("unknown format {0!r}".format(args.format))
        return EXIT_USAGE

    text = emit()
    if args.output:
        # Written with an explicit newline translation so the committed file
        # is byte-identical on every platform, matching the emitters' own
        # determinism guarantee.
        with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        _err("wrote {0} ({1} bytes)".format(args.output, len(text)))
    else:
        _out(text.rstrip())
    return EXIT_OK


# =============================================================================
#  SUBCOMMANDS: formula, compute
#
#  Both depend on `biotechnology.formulas`, which is not written. They exit 3
#  rather than raising, so a script can distinguish "this data does not exist
#  yet" from "your query matched nothing". Implementing them against a missing
#  registry, or removing them from the parser, would each be worse: the first
#  crashes, and the second makes a documented command vanish without saying
#  why.
# =============================================================================


def _formula_registry_or_none() -> Optional[object]:
    try:
        from . import formulas  # type: ignore[attr-defined]
    except Exception:
        return None
    return formulas if getattr(formulas, "KEYS", None) else None


def cmd_formula(args: argparse.Namespace) -> int:
    module = _formula_registry_or_none()
    if module is None:
        _err(
            "the formula registry is not written yet, so {0!r} cannot be "
            "explained. The 181 formula keys referenced by the taxonomy are "
            "listed by `biotechnology stats`.".format(args.key)
        )
        return EXIT_UNAVAILABLE
    _err("formula lookup is not implemented")
    return EXIT_UNAVAILABLE


def cmd_compute(args: argparse.Namespace) -> int:
    module = _formula_registry_or_none()
    if module is None:
        _err(
            "the formula registry is not written yet, so {0!r} cannot be "
            "computed.".format(args.key)
        )
        return EXIT_UNAVAILABLE
    _err("formula evaluation is not implemented")
    return EXIT_UNAVAILABLE


# =============================================================================
#  PARSER
# =============================================================================


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="biotechnology",
        description=(
            "A machine-readable taxonomy of the ten colour-coded branches of "
            "biotechnology."
        ),
        epilog="Exit codes: 0 success, 1 no result, 2 usage, 3 data not yet written.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")

    p_list = sub.add_parser("list", help="list the branches")
    p_list.add_argument("-q", "--quiet", action="store_true", help="omit the coverage note")
    p_list.set_defaults(handler=cmd_list)

    p_tree = sub.add_parser("tree", help="print branches with their subtypes")
    p_tree.add_argument("branch", nargs="?", help="limit to one branch")
    p_tree.add_argument("-s", "--summary", action="store_true", help="append summaries")
    p_tree.set_defaults(handler=cmd_tree)

    p_show = sub.add_parser("show", help="show one branch or subtype")
    p_show.add_argument("path", help="a branch key or a dotted subtype path")
    p_show.add_argument("--plain", action="store_true", help="public register only")
    p_show.add_argument("--json", action="store_true", help="emit JSON")
    p_show.add_argument("--markdown", action="store_true", help="emit Markdown")
    p_show.set_defaults(handler=cmd_show)

    p_search = sub.add_parser("search", help="free-text search of the taxonomy")
    p_search.add_argument("query")
    p_search.add_argument("-n", "--number", type=int, default=10, help="maximum results")
    p_search.add_argument("--scores", action="store_true", help="show relevance scores")
    p_search.set_defaults(handler=cmd_search)

    p_sdg = sub.add_parser("sdg", help="records linked to a Sustainable Development Goal")
    p_sdg.add_argument("goal", type=int, help="goal number, 1 to 17")
    p_sdg.set_defaults(handler=cmd_sdg)

    p_vocab = sub.add_parser("vocab", help="the controlled vocabularies")
    p_vocab.add_argument("name", nargs="?", help="one vocabulary, or all of them")
    p_vocab.set_defaults(handler=cmd_vocab)

    p_stats = sub.add_parser("stats", help="headline counts and coverage")
    p_stats.set_defaults(handler=cmd_stats)

    p_validate = sub.add_parser("validate", help="run the integrity suite")
    p_validate.add_argument(
        "--strict", action="store_true", help="promote warnings to errors"
    )
    p_validate.add_argument(
        "--warnings", action="store_true", help="show warnings as well as errors"
    )
    p_validate.set_defaults(handler=cmd_validate)

    p_export = sub.add_parser("export", help="emit the taxonomy in another format")
    p_export.add_argument(
        "--format", choices=("json", "csv", "dot", "markdown"), default="json"
    )
    p_export.add_argument("-o", "--output", help="write to a file instead of stdout")
    p_export.set_defaults(handler=cmd_export)

    p_formula = sub.add_parser("formula", help="explain a formula")
    p_formula.add_argument("key")
    p_formula.add_argument("--explain", action="store_true", help="show the derivation")
    p_formula.set_defaults(handler=cmd_formula)

    p_compute = sub.add_parser("compute", help="evaluate a formula")
    p_compute.add_argument("key")
    p_compute.add_argument("--arg", action="append", default=[], metavar="NAME=VALUE")
    p_compute.set_defaults(handler=cmd_compute)

    return parser


# =============================================================================
#  ENTRY POINT
# =============================================================================


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the command line interface.

    Returns an exit code rather than calling `sys.exit`, so that the function
    is testable and so that `python -m biotechnology` and the console script
    can share it.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "handler", None):
        parser.print_help()
        return EXIT_USAGE

    try:
        return int(args.handler(args))
    except BiotechnologyError as exc:
        # Every error this library raises inherits from BiotechnologyError, so
        # one clause covers the lot while an ordinary Python error still
        # produces a traceback. A user-facing tool should not print a
        # traceback for a mistyped path; a maintainer debugging a genuine bug
        # should still get one.
        _err(str(exc))
        return EXIT_NO_RESULT
    except BrokenPipeError:  # pragma: no cover - depends on the consumer
        # `biotechnology tree | head` closes the pipe early. That is normal
        # use, not an error, and it should not produce a traceback.
        return EXIT_OK


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
