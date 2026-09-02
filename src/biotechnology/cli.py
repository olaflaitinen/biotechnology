"""Command line interface: ``biotechnology <command>``."""

from __future__ import annotations

import argparse
import json
import sys
import textwrap
from typing import List, Optional, Sequence

from . import __version__, registry
from .models import Branch, Subtype

_WRAP = textwrap.TextWrapper(width=78, initial_indent="  ", subsequent_indent="  ")


def _wrap(text: str) -> str:
    return _WRAP.fill(" ".join(text.split()))


def _bullets(title: str, items: Sequence[str]) -> List[str]:
    if not items:
        return []
    return [f"  {title}:"] + [f" - {item}" for item in items]


def _render_branch(b: Branch) -> str:
    lines = [f"{b.name}  [{b.key}]  {b.colour}", "", _wrap(b.description), ""]
    if b.aliases:
        lines.append(f"  aliases: {', '.join(b.aliases)}")
    if b.sdgs:
        lines.append(f"  SDGs: {', '.join(str(g) for g in b.sdgs)}")
    lines.append(f"  subtypes ({len(b)}):")
    width = max(len(s.key) for s in b) if len(b) else 0
    for sub in b:
        lines.append(f"    {sub.key.ljust(width)}  {sub.name}")
    return "\n".join(lines)


def _render_subtype(s: Subtype) -> str:
    lines = [
        f"{s.name}  [{s.path}]",
        f"  branch: {s.branch.name}",
        "",
        _wrap(s.description),
        "",
    ]
    lines += _bullets("applications", s.applications)
    lines += _bullets("technologies", s.technologies)
    if s.sdgs:
        lines.append(f"  SDGs: {', '.join(str(g) for g in s.sdgs)}")
    if s.related:
        lines.append(f"  related: {', '.join(s.related)}")
    return "\n".join(lines)


def _render(node) -> str:
    return _render_branch(node) if isinstance(node, Branch) else _render_subtype(node)


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------
def _cmd_list(args: argparse.Namespace) -> int:
    width = max(len(b.key) for b in registry.branches())
    for b in registry.branches():
        print(f"{b.key.ljust(width)}  {b.colour}  {b.name} - {b.summary}")
    return 0


def _cmd_tree(args: argparse.Namespace) -> int:
    print(registry.tree(args.branch or None), end="")
    return 0


def _cmd_show(args: argparse.Namespace) -> int:
    try:
        node = registry.get(args.path)
    except registry.UnknownNodeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(node.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(_render(node))
    return 0


def _cmd_search(args: argparse.Namespace) -> int:
    results = registry.search(
        args.query,
        branch_key=args.branch,
        include_branches=args.include_branches,
        limit=args.limit,
    )
    if not results:
        print(f"no match for {args.query!r}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps([n.to_dict() for n in results], indent=2, ensure_ascii=False))
        return 0
    for node in results:
        path = node.key if isinstance(node, Branch) else node.path
        print(f"{path}\n    {node.name}")
    return 0


def _cmd_sdg(args: argparse.Namespace) -> int:
    results = registry.by_sdg(args.goal)
    if not results:
        print(f"no subtype tagged with SDG {args.goal}", file=sys.stderr)
        return 1
    for sub in results:
        print(f"{sub.path}\n    {sub.name}")
    return 0


def _cmd_export(args: argparse.Namespace) -> int:
    payload = registry.to_json(indent=args.indent)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(payload + "\n")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(payload)
    return 0


# ---------------------------------------------------------------------------
# parser
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="biotechnology",
        description="Explore the colour-coded taxonomy of biotechnology.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list the ten branches")
    p_list.set_defaults(func=_cmd_list)

    p_tree = sub.add_parser("tree", help="print branches with their subtypes")
    p_tree.add_argument("branch", nargs="*", help="limit to these branches")
    p_tree.set_defaults(func=_cmd_tree)

    p_show = sub.add_parser("show", help="show one branch or subtype")
    p_show.add_argument("path", help='e.g. "red" or "red.gene_therapy"')
    p_show.add_argument("--json", action="store_true", help="emit JSON")
    p_show.set_defaults(func=_cmd_show)

    p_search = sub.add_parser("search", help="free-text search of the taxonomy")
    p_search.add_argument("query")
    p_search.add_argument("-b", "--branch", help="restrict to one branch")
    p_search.add_argument("-n", "--limit", type=int, help="maximum results")
    p_search.add_argument(
        "--include-branches",
        action="store_true",
        help="let branches match as well as subtypes",
    )
    p_search.add_argument("--json", action="store_true", help="emit JSON")
    p_search.set_defaults(func=_cmd_search)

    p_sdg = sub.add_parser("sdg", help="subtypes linked to an SDG number")
    p_sdg.add_argument("goal", type=int, help="SDG number, 1-17")
    p_sdg.set_defaults(func=_cmd_sdg)

    p_export = sub.add_parser("export", help="dump the whole taxonomy as JSON")
    p_export.add_argument("-o", "--output", help="write to a file instead of stdout")
    p_export.add_argument("--indent", type=int, default=2)
    p_export.set_defaults(func=_cmd_export)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
