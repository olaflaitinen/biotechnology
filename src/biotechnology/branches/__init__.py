# =============================================================================
#  biotechnology.branches
# -----------------------------------------------------------------------------
#  The ten colour-coded branches of biotechnology.
#
#  WHY COLOURS AT ALL?
#  The colour scheme is not a formal standard issued by any body. It grew out
#  of European science-policy writing in the late 1990s and early 2000s, where
#  "red" (medical) and "green" (agricultural) biotechnology were contrasted in
#  public debate, and was extended colour by colour as other application areas
#  needed names. Because it grew rather than being designed, the boundaries
#  overlap: an enzyme used in a washing powder is white, the same enzyme in a
#  cheese vat is yellow, and the algorithm that designed it is gold. This
#  library records the conventional assignment and then makes the overlaps
#  navigable through explicit cross-references rather than pretending they do
#  not exist.
#
#  PACKAGE LAYOUT
#  Each colour is a package. Each subtype inside it is a single module holding
#  exactly one `SUBTYPE` object:
#
#      branches/
#        red/
#          __init__.py            assembles BRANCH from the modules below
#          gene_therapy.py        -> SUBTYPE
#          cell_therapy.py        -> SUBTYPE
#          ...
#
#  One file per subtype is deliberate. Eighty-five records in ten files would
#  make every correction a merge conflict; eighty-five files make a correction
#  a one-file pull request that a domain expert can review without reading
#  anything else.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Dict, Tuple

from ..core.models import Branch
from . import (
    blue,
    brown,
    dark,
    gold,
    green,
    grey,
    purple,
    red,
    white,
    yellow,
)

__all__ = ["ALL_BRANCHES", "BRANCH_MODULES", "COLOUR_ORDER"]

# -----------------------------------------------------------------------------
#  Presentation order.
#
#  This is the order used by every listing, table and chart in the project. It
#  follows the rough historical order in which the colours entered common use
#  (red and green first, then the industrial and marine colours, then the
#  cross-cutting ones), which reads more naturally than alphabetical order and
#  keeps the two governance branches - dark and purple - together at the end
#  where they belong, since they apply to everything above them.
# -----------------------------------------------------------------------------
COLOUR_ORDER: Tuple[str, ...] = (
    "red",
    "green",
    "white",
    "blue",
    "yellow",
    "grey",
    "brown",
    "gold",
    "dark",
    "purple",
)

# -----------------------------------------------------------------------------
#  Module registry: colour key -> the package that defines it.
#  Kept as data so that tooling can walk the packages without hard-coding a
#  second copy of the list.
# -----------------------------------------------------------------------------
BRANCH_MODULES: Dict[str, object] = {
    "red": red,
    "green": green,
    "white": white,
    "blue": blue,
    "yellow": yellow,
    "grey": grey,
    "brown": brown,
    "gold": gold,
    "dark": dark,
    "purple": purple,
}

# -----------------------------------------------------------------------------
#  The assembled tuple every other module imports.
#
#  Built from COLOUR_ORDER rather than from dict order so that the presentation
#  order is stated once and cannot drift.
# -----------------------------------------------------------------------------
ALL_BRANCHES: Tuple[Branch, ...] = tuple(
    BRANCH_MODULES[key].BRANCH for key in COLOUR_ORDER  # type: ignore[attr-defined]
)

# -----------------------------------------------------------------------------
#  Import-time sanity checks.
#
#  These are cheap and they fail loudly. A branch package whose BRANCH.key does
#  not match its directory name would otherwise produce a taxonomy that looks
#  fine until someone tries to resolve a path.
# -----------------------------------------------------------------------------
for _key, _module in BRANCH_MODULES.items():
    _branch = _module.BRANCH  # type: ignore[attr-defined]
    if _branch.key != _key:
        raise ImportError(
            f"branch package {_key!r} defines BRANCH.key = {_branch.key!r}; "
            f"the package directory and the branch key must match"
        )
    if not _branch.subtypes:
        raise ImportError(f"branch package {_key!r} defines no subtypes")

if len(ALL_BRANCHES) != len(COLOUR_ORDER):
    raise ImportError("COLOUR_ORDER and BRANCH_MODULES disagree about the branch list")

del _key, _module, _branch
