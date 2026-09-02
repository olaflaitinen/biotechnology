# =============================================================================
#  biotechnology.core.paths
# -----------------------------------------------------------------------------
#  Parsing and normalisation of dotted addresses.
#
#  WHAT IS A PATH?
#  Everything in this library has an address written with dots:
#
#      "red"                     a branch
#      "red.gene_therapy"        a subtype inside that branch
#
#  That is the whole grammar. There is no third level, no wildcards and no
#  escaping, and this module exists to keep it that way. Centralising the
#  parsing means that the CLI, the search engine, the exporters and the
#  documentation generator all agree on exactly what a path is, including the
#  awkward cases: trailing whitespace, mixed case, a hyphen typed instead of
#  an underscore, a stray trailing dot pasted out of a Markdown link.
#
#  NORMALISATION RULES (applied in this order)
#      1. strip surrounding whitespace
#      2. lower-case
#      3. convert spaces and hyphens to underscores
#      4. collapse repeated underscores
#
#  So "  Red / Gene-Therapy " is not accepted (the slash is illegal) but
#  " Red.Gene-Therapy " resolves to "red.gene_therapy".
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import re
from typing import NamedTuple, Optional, Tuple

from .errors import PathSyntaxError

__all__ = [
    "ParsedPath",
    "normalise_token",
    "parse_path",
    "join_path",
    "is_branch_path",
    "is_subtype_path",
    "slugify",
    "SEGMENT_PATTERN",
    "MAX_SEGMENTS",
]

# -----------------------------------------------------------------------------
#  A legal segment is a lowercase identifier: letters, digits and underscores,
#  starting with a letter. Keys such as `crispr_cas9` and `sdg_14` are legal;
#  `9_things` and `gene.therapy.extra` are not.
# -----------------------------------------------------------------------------
SEGMENT_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")

#: The taxonomy is deliberately only two levels deep.
MAX_SEGMENTS = 2

_MULTI_UNDERSCORE = re.compile(r"_{2,}")
_ILLEGAL = re.compile(r"[^a-z0-9_.]")


class ParsedPath(NamedTuple):
    """The result of :func:`parse_path`.

    Attributes
    ----------
    branch:
        The first segment, always present.
    subtype:
        The second segment, or ``None`` for a branch-level path.
    raw:
        Exactly what the caller passed in, kept for error messages so that
        the user sees their own typing echoed back rather than a normalised
        version they do not recognise.
    """

    branch: str
    subtype: Optional[str]
    raw: str

    @property
    def is_branch(self) -> bool:
        """True when the path names a branch and not a subtype."""
        return self.subtype is None

    @property
    def normalised(self) -> str:
        """The canonical dotted string this path represents."""
        return self.branch if self.subtype is None else f"{self.branch}.{self.subtype}"

    @property
    def segments(self) -> Tuple[str, ...]:
        """The path as a tuple of one or two segments."""
        return (self.branch,) if self.subtype is None else (self.branch, self.subtype)


def normalise_token(token: str) -> str:
    """Apply the normalisation rules to a single segment.

    >>> normalise_token("  Gene-Therapy ")
    'gene_therapy'
    >>> normalise_token("Plant  Tissue  Culture")
    'plant_tissue_culture'
    """
    cleaned = token.strip().lower().replace("-", "_").replace(" ", "_")
    return _MULTI_UNDERSCORE.sub("_", cleaned).strip("_")


def parse_path(path: str) -> ParsedPath:
    """Parse a dotted path into its segments, or explain why it is malformed.

    This function never consults the registry, so it cannot tell you whether
    ``"red.unicorns"`` exists - only that it is *shaped* like a valid path.
    Existence is checked by :func:`biotechnology.core.registry.get`.

    Raises
    ------
    PathSyntaxError
        For an empty string, a path with more than two segments, an empty
        segment (``"red."`` or ``".gene_therapy"`` or ``"red..x"``), or a
        segment containing characters outside ``[a-z0-9_]``.

    Examples
    --------
    >>> parse_path("red").normalised
    'red'
    >>> parse_path(" Red . Gene-Therapy ").normalised
    'red.gene_therapy'
    >>> parse_path("red.gene_therapy").is_branch
    False
    """
    if path is None:
        raise PathSyntaxError("", "path is None")

    raw = str(path)
    if not raw.strip():
        raise PathSyntaxError(raw, "path is empty")

    # Normalise the whole string first so that separators inside segments are
    # handled uniformly, then split on the one structural character we allow.
    working = raw.strip().lower().replace("-", "_").replace(" ", "")
    illegal = _ILLEGAL.findall(working)
    if illegal:
        found = "".join(sorted(set(illegal)))
        raise PathSyntaxError(raw, f"illegal character(s) {found!r}")

    parts = working.split(".")
    if len(parts) > MAX_SEGMENTS:
        raise PathSyntaxError(
            raw,
            f"the taxonomy is only {MAX_SEGMENTS} levels deep, "
            f"got {len(parts)} segments",
        )

    cleaned = []
    for index, part in enumerate(parts):
        token = _MULTI_UNDERSCORE.sub("_", part).strip("_")
        if not token:
            position = "first" if index == 0 else "second"
            raise PathSyntaxError(raw, f"the {position} segment is empty")
        if not SEGMENT_PATTERN.match(token):
            raise PathSyntaxError(
                raw, f"segment {token!r} must start with a letter and contain only a-z, 0-9, _"
            )
        cleaned.append(token)

    branch = cleaned[0]
    subtype = cleaned[1] if len(cleaned) == 2 else None
    return ParsedPath(branch=branch, subtype=subtype, raw=raw)


def join_path(branch: str, subtype: Optional[str] = None) -> str:
    """Build a normalised path from parts.

    >>> join_path("Red", "Gene Therapy")
    'red.gene_therapy'
    >>> join_path("blue")
    'blue'
    """
    head = normalise_token(branch)
    if subtype is None:
        return head
    return f"{head}.{normalise_token(subtype)}"


def is_branch_path(path: str) -> bool:
    """True when ``path`` is shaped like a branch address. Never raises.

    >>> is_branch_path("red"), is_branch_path("red.gene_therapy")
    (True, False)
    >>> is_branch_path("!!")
    False
    """
    try:
        return parse_path(path).is_branch
    except PathSyntaxError:
        return False


def is_subtype_path(path: str) -> bool:
    """True when ``path`` is shaped like a subtype address. Never raises."""
    try:
        return not parse_path(path).is_branch
    except PathSyntaxError:
        return False


def slugify(text: str) -> str:
    """Turn arbitrary text into a URL- and filename-safe slug.

    Used by the documentation generator to name pages and anchors. Unlike
    :func:`normalise_token` this accepts anything at all and simply discards
    what it cannot use.

    >>> slugify("CRISPR-Cas9 & prime editing")
    'crispr-cas9-prime-editing'
    >>> slugify("  Multiple   spaces  ")
    'multiple-spaces'
    """
    lowered = text.strip().lower()
    kept = re.sub(r"[^a-z0-9]+", "-", lowered)
    return kept.strip("-")
