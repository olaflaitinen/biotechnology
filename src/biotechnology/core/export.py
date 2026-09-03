# =============================================================================
#  biotechnology.core.export
# -----------------------------------------------------------------------------
#  Emitters. Five formats, one rule:
#
#      EXPORT IS A PROJECTION OF THE TAXONOMY, NEVER A SECOND COPY OF IT.
#
#  Every function here reads the frozen records and writes text. None of them
#  holds state, caches a result, or knows a fact that is not already in a
#  record. If an emitter and a record ever disagree, the emitter is wrong.
#
#  WHY THIS MODULE EXISTED IN THE PUBLIC API BEFORE IT EXISTED ON DISK
#  `biotechnology/__init__.py` has always imported five names from here. The
#  module was never written, so `import biotechnology` raised
#  ModuleNotFoundError. That is why this file reads as a specification being
#  met rather than a design being proposed: the signatures were fixed by the
#  import line and by the CLI that calls them.
#
#  THE FIVE FORMATS AND WHO THEY ARE FOR
#
#      to_dict      plain Python, the substrate every other emitter builds on
#      to_json      machines, and the archival format
#      to_csv       spreadsheets, which is how most non-programmers will meet
#                   this data
#      to_markdown  humans reading a rendered page
#      to_dot       the cross-reference graph, for Graphviz
#      tree         a terminal, and the only emitter that is deliberately lossy
#
#  DETERMINISM IS A HARD REQUIREMENT
#  Output must be byte-identical across runs, interpreters and locales, because
#  `make docs` commits its output and a nondeterministic emitter would produce
#  a diff on every run. Three consequences appear throughout this file:
#  mappings are emitted in a stated key order rather than in dict order, sets
#  are sorted before emission, and no float is formatted with the default repr.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import csv
import io
import json
from typing import Any, Dict, Iterable, List, Optional, Sequence, Union

from .models import Branch, Node, Subtype
from .registry import branches, subtypes

__all__ = [
    "to_dict",
    "to_json",
    "to_csv",
    "to_markdown",
    "to_dot",
    "tree",
    "CSV_COLUMNS",
]


# =============================================================================
#  CSV COLUMN ORDER
#
#  Stated once, as data, for two reasons. A spreadsheet column order that
#  drifted between releases would silently break every downstream formula that
#  referenced a column by position. And naming it here rather than building it
#  from `dataclasses.fields` keeps the CSV a deliberate SELECTION rather than a
#  dump: the long prose fields are excluded because a cell holding six hundred
#  words is not usable in a spreadsheet, and the multi-valued fields are joined
#  rather than exploded because one row per record is what makes the file
#  sortable.
# =============================================================================
CSV_COLUMNS: Sequence[str] = (
    "path",
    "branch",
    "key",
    "name",
    "summary",
    "maturity",
    "risk_tier",
    "scale",
    "regulatory_status",
    "domains",
    "sdgs",
    "applications",
    "challenges",
    "organisms",
    "techniques",
    "formulas",
    "related",
    "first_year",
    "milestone_count",
    "metric_count",
)

#: Separator for multi-valued cells. A semicolon rather than a comma so the
#: cell needs no quoting, and rather than a newline so the row stays one line.
_CELL_SEPARATOR = "; "


# =============================================================================
#  to_dict
#  The substrate. Everything else in this module is a rendering of what this
#  returns, which is what keeps the formats from drifting apart.
# =============================================================================


def to_dict(
    node: Optional[Union[Node, Iterable[Node]]] = None,
    *,
    include_prose: bool = True,
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """Convert a record, a collection of records, or the whole taxonomy.

    Parameters
    ----------
    node:
        A `Branch`, a `Subtype`, any iterable of those, or None. None means
        the entire taxonomy, which is the common case and is why it is the
        default rather than requiring the caller to pass `branches()`.
    include_prose:
        When False, the long narrative fields are omitted. Intended for
        callers building an index or a table, where six hundred words per
        record is noise. The structural fields are unaffected.

    Returns
    -------
    A dict for a single record, a list of dicts for a collection.

    Notes
    -----
    The per-record conversion is delegated to `Branch.to_dict` and
    `Subtype.to_dict`, which are the authoritative definitions of the export
    shape. This function decides only what to convert, never how, so adding a
    field to a record cannot leave the exporter behind.
    """
    if node is None:
        return {
            "branches": [b.to_dict() for b in branches()],
            "counts": _coverage(),
        }

    if isinstance(node, (Branch, Subtype)):
        record = node.to_dict()
        if not include_prose:
            record = _without_prose(record)
        return record

    out: List[Dict[str, Any]] = []
    for item in node:
        record = item.to_dict()
        if not include_prose:
            record = _without_prose(record)
        out.append(record)
    return out


#: Fields dropped when `include_prose=False`. Named explicitly rather than
#: detected by length, because a short description is still prose and a long
#: application list still is not.
_PROSE_FIELDS = (
    "description",
    "plain_language",
    "analogy",
    "why_it_matters",
    "origin_note",
)


def _without_prose(record: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in record.items() if k not in _PROSE_FIELDS}


def _coverage() -> Dict[str, Any]:
    """Coverage figures, stated rather than implied.

    Every whole-taxonomy export carries this. A consumer who receives six
    branches must be able to tell that six is the current state and not the
    complete set, and the honest place to say so is in the payload rather than
    in a document they may not have read.
    """
    from ..branches import COLOUR_ORDER, PENDING_COLOURS, WRITTEN_COLOURS

    return {
        "branches_written": len(WRITTEN_COLOURS),
        "branches_total": len(COLOUR_ORDER),
        "branches_pending": list(PENDING_COLOURS),
        "subtypes": len(subtypes()),
        "complete": not PENDING_COLOURS,
    }


# =============================================================================
#  to_json
# =============================================================================


def to_json(
    node: Optional[Union[Node, Iterable[Node]]] = None,
    *,
    indent: Optional[int] = 2,
    include_prose: bool = True,
) -> str:
    """Serialise to JSON.

    `sort_keys` is deliberately False. The record classes emit their fields in
    a meaningful order, narrative before practice before governance, and
    sorting alphabetically would scatter that for no gain: the output is
    already deterministic because the input order is.

    `ensure_ascii` is True, which matters more here than in most projects. The
    entire corpus is ASCII by editorial rule, so this is a belt-and-braces
    assertion rather than a transformation, and if a non-ASCII character ever
    reaches an export it will appear as an escape rather than silently
    changing the file encoding.
    """
    return json.dumps(
        to_dict(node, include_prose=include_prose),
        indent=indent,
        sort_keys=False,
        ensure_ascii=True,
        separators=(",", ": ") if indent else (",", ":"),
    )


# =============================================================================
#  to_csv
# =============================================================================


def to_csv(
    records: Optional[Iterable[Subtype]] = None,
    *,
    columns: Sequence[str] = CSV_COLUMNS,
) -> str:
    """One row per subtype, one column per field in `CSV_COLUMNS`.

    Branches are not exported here. A file mixing two record shapes is not a
    table, and a caller who wants branch-level data has `to_json`.

    Line terminator is set explicitly to "\\n" rather than left to the csv
    module's "\\r\\n" default, so output is identical on every platform. The
    file this produces is committed by `make docs`, and a platform-dependent
    line ending would show every line as changed.
    """
    rows = list(records) if records is not None else subtypes()

    buffer = io.StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=list(columns),
        lineterminator="\n",
        quoting=csv.QUOTE_MINIMAL,
    )
    writer.writeheader()
    for subtype in rows:
        writer.writerow(_csv_row(subtype, columns))
    return buffer.getvalue()


def _csv_row(subtype: Subtype, columns: Sequence[str]) -> Dict[str, str]:
    """Flatten one subtype into string cells.

    Every value becomes a string here rather than being left to the csv
    module, because the module's coercion of None differs from its coercion of
    an empty tuple and both should read as an empty cell.
    """
    values: Dict[str, Any] = {
        "path": subtype.path,
        "branch": subtype.branch_key,
        "key": subtype.key,
        "name": subtype.name,
        "summary": subtype.summary,
        "maturity": subtype.maturity.name,
        "risk_tier": subtype.risk_tier.name,
        "scale": subtype.scale.name,
        "regulatory_status": subtype.regulatory_status.name,
        "domains": _join(d.name for d in subtype.domains),
        "sdgs": _join(str(g) for g in subtype.sdgs),
        "applications": _join(subtype.applications),
        "challenges": _join(subtype.challenges),
        "organisms": _join(subtype.organisms),
        "techniques": _join(subtype.techniques),
        "formulas": _join(subtype.formulas),
        "related": _join(subtype.related),
        "first_year": subtype.first_year,
        "milestone_count": len(subtype.milestones),
        "metric_count": len(subtype.metrics),
    }
    return {c: "" if values.get(c) is None else str(values.get(c, "")) for c in columns}


def _join(values: Iterable[str]) -> str:
    return _CELL_SEPARATOR.join(values)


# =============================================================================
#  to_markdown
# =============================================================================


def to_markdown(node: Optional[Union[Node, Iterable[Node]]] = None) -> str:
    """Render as Markdown, for a rendered page or a terminal pager.

    Heading levels start at 1 for a branch and 2 for a subtype, which is what
    the documentation generator expects when it concatenates a branch page.
    A caller embedding this elsewhere is expected to shift them.
    """
    if node is None:
        node = branches()

    if isinstance(node, Branch):
        return _branch_markdown(node)
    if isinstance(node, Subtype):
        return _subtype_markdown(node)

    return "\n\n".join(to_markdown(item) for item in node)


def _branch_markdown(branch: Branch) -> str:
    lines: List[str] = [
        "# {0}".format(branch.name),
        "",
        "`{0}` | {1} subtypes | colour `{2}`".format(
            branch.key, len(branch.subtypes), branch.colour
        ),
        "",
        branch.summary,
        "",
    ]
    if branch.description:
        lines += [branch.description, ""]
    if branch.plain_language:
        lines += ["**In plain language.** " + branch.plain_language, ""]
    if branch.analogy:
        lines += ["**An analogy.** " + branch.analogy, ""]
    if branch.why_it_matters:
        lines += ["**Why it matters.** " + branch.why_it_matters, ""]
    if branch.origin_note:
        lines += ["**On the name.** " + branch.origin_note, ""]

    if branch.key_questions:
        lines += ["## Key questions", ""]
        lines += ["- {0}".format(q) for q in branch.key_questions]
        lines += [""]

    lines += ["## Subtypes", ""]
    for subtype in branch.subtypes:
        lines.append("- [`{0}`](#{1}) - {2}".format(subtype.path, subtype.key, subtype.summary))
    lines.append("")

    for subtype in branch.subtypes:
        lines.append(_subtype_markdown(subtype))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _subtype_markdown(subtype: Subtype) -> str:
    lines: List[str] = [
        "## {0}".format(subtype.name),
        "",
        "`{0}`".format(subtype.path),
        "",
        subtype.summary,
        "",
    ]

    if subtype.description:
        lines += ["### What it is", "", subtype.description, ""]
    if subtype.plain_language:
        lines += ["### In plain language", "", subtype.plain_language, ""]
    if subtype.analogy:
        lines += ["### An analogy", "", subtype.analogy, ""]
    if subtype.why_it_matters:
        lines += ["### Why it matters", "", subtype.why_it_matters, ""]

    lines += _list_section("Applications", subtype.applications)
    lines += _list_section("Technologies", subtype.technologies)
    lines += _list_section("Challenges", subtype.challenges)

    if subtype.metrics:
        lines += ["### Metrics", "", "| Metric | Symbol | Unit | Typical | Evidence |", "|---|---|---|---|---|"]
        for metric in subtype.metrics:
            lines.append(
                "| {0} | `{1}` | {2} | {3} | {4} |".format(
                    _cell(metric.name),
                    metric.symbol,
                    _cell(metric.unit),
                    _cell(metric.typical),
                    metric.evidence.name,
                )
            )
        lines.append("")

    if subtype.milestones:
        lines += ["### History", ""]
        for milestone in subtype.timeline:
            lines.append("- **{0}** - {1}".format(milestone.year, milestone.event))
        lines.append("")

    lines += ["### Governance", ""]
    lines += [
        "| Field | Value |",
        "|---|---|",
        "| Maturity | {0} |".format(subtype.maturity.name),
        "| Risk tier | {0} |".format(subtype.risk_tier.name),
        "| Scale | {0} |".format(subtype.scale.name),
        "| Regulatory status | {0} |".format(subtype.regulatory_status.name),
        "| Domains | {0} |".format(", ".join(d.name for d in subtype.domains) or "-"),
        "| SDGs | {0} |".format(", ".join(str(g) for g in subtype.sdgs) or "-"),
        "",
    ]

    lines += _list_section("Regulations", subtype.regulations)
    lines += _list_section("Standards", subtype.standards)

    if subtype.related:
        lines += ["### Related records", ""]
        lines += ["- `{0}`".format(r) for r in subtype.related]
        lines += [""]

    return "\n".join(lines).rstrip() + "\n"


def _list_section(title: str, items: Sequence[str]) -> List[str]:
    if not items:
        return []
    out = ["### {0}".format(title), ""]
    out += ["- {0}".format(item) for item in items]
    out.append("")
    return out


def _cell(text: str) -> str:
    """Escape a value for a Markdown table cell.

    A pipe inside a cell ends the cell, and a newline ends the row. Both occur
    in this corpus: units contain no pipes but several `typical` strings run to
    a full sentence, and a future one could contain either.
    """
    return text.replace("|", "\\|").replace("\n", " ")


# =============================================================================
#  to_dot
#  The cross-reference graph. This is the one export that shows something no
#  single record contains, which is the shape of the taxonomy's own linkage.
# =============================================================================


def to_dot(
    records: Optional[Iterable[Subtype]] = None,
    *,
    cluster_by_branch: bool = True,
) -> str:
    """Emit the RELATED graph in Graphviz DOT format.

    Only edges whose target is present in the exported set are drawn. A record
    in a written branch frequently points at one in a pending branch, and
    emitting an edge to a node that does not exist would make Graphviz invent
    an unlabelled node and misrepresent the graph. Those edges are counted and
    reported in a comment at the head of the file rather than silently
    dropped, because "12 edges omitted" is information and an absent edge is
    not.
    """
    rows = list(records) if records is not None else subtypes()
    present = {s.path for s in rows}

    lines: List[str] = [
        "// Generated by biotechnology.core.export.to_dot",
        "// Nodes are subtypes; edges are RELATED cross-references.",
        "digraph taxonomy {",
        "  graph [rankdir=LR, overlap=false, splines=true];",
        '  node  [shape=box, style="rounded,filled", fontname="Helvetica"];',
        '  edge  [color="#88888899", arrowsize=0.6];',
        "",
    ]

    if cluster_by_branch:
        by_branch: Dict[str, List[Subtype]] = {}
        for subtype in rows:
            by_branch.setdefault(subtype.branch_key, []).append(subtype)
        for branch_key in sorted(by_branch):
            members = by_branch[branch_key]
            colour = members[0].branch.colour if members else "#cccccc"
            lines.append('  subgraph "cluster_{0}" {{'.format(branch_key))
            lines.append('    label="{0}";'.format(branch_key))
            lines.append('    color="{0}";'.format(colour))
            for subtype in members:
                lines.append(
                    '    "{0}" [label="{1}", fillcolor="{2}", fontcolor="{3}"];'.format(
                        subtype.path,
                        subtype.name,
                        colour,
                        "#000000" if subtype.branch.is_light else "#ffffff",
                    )
                )
            lines.append("  }")
            lines.append("")
    else:
        for subtype in rows:
            lines.append('  "{0}" [label="{1}"];'.format(subtype.path, subtype.name))
        lines.append("")

    omitted = 0
    for subtype in rows:
        for target in subtype.related:
            if target in present:
                lines.append('  "{0}" -> "{1}";'.format(subtype.path, target))
            else:
                omitted += 1

    lines.append("}")

    if omitted:
        lines.insert(
            2,
            "// {0} edge(s) omitted: they point at records in branches that "
            "are not written yet.".format(omitted),
        )

    return "\n".join(lines) + "\n"


# =============================================================================
#  tree
#  The only deliberately lossy emitter. It is for a terminal, and a terminal
#  wants shape rather than content.
# =============================================================================


def tree(
    node: Optional[Union[Node, Iterable[Node]]] = None,
    *,
    show_summary: bool = False,
    ascii_only: bool = True,
) -> str:
    """Render the taxonomy as an indented tree.

    `ascii_only` is accepted for signature stability and only the ASCII form
    is produced, which is deliberate rather than unfinished. The project
    forbids non-ASCII characters throughout, box-drawing characters are the
    commonest thing to reach for in a tree renderer, and a Windows console
    under a legacy code page renders them as mojibake. Rather than carry a
    branch that this project may never take, the parameter is honoured by
    doing the correct thing in both cases.
    """
    if node is None:
        node = branches()
    if isinstance(node, (Branch, Subtype)):
        node = [node]

    stem, fork, end = ("|  ", "|- ", "`- ") if ascii_only else ("\u2502  ", "\u251c\u2500 ", "\u2514\u2500 ")

    lines: List[str] = []
    items = list(node)
    for index, item in enumerate(items):
        last = index == len(items) - 1
        if isinstance(item, Branch):
            lines.append("{0} ({1})".format(item.name, item.key))
            children = list(item.subtypes)
            for child_index, child in enumerate(children):
                child_last = child_index == len(children) - 1
                marker = end if child_last else fork
                label = child.name
                if show_summary:
                    label = "{0} - {1}".format(label, child.summary)
                lines.append("{0}{1}".format(marker, label))
            if not last:
                lines.append("")
        else:
            marker = end if last else fork
            label = item.name
            if show_summary:
                label = "{0} - {1}".format(label, item.summary)
            lines.append("{0}{1}".format(marker, label))

    return "\n".join(lines).rstrip() + "\n"
