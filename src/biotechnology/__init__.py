# =============================================================================
#  biotechnology
# -----------------------------------------------------------------------------
#  A machine-readable, dual-register taxonomy of the ten colour-coded branches
#  of biotechnology.
#
#  Ten branches. Eighty-five subtypes. Every record written twice - once in a
#  technical register for specialists, once in plain language for the
#  parliamentary committees, procurement officers, journalists, teachers and
#  students who make or shape decisions about the field without practising it.
#
#      >>> import biotechnology as bt
#      >>> bt.RED.name
#      'Red Biotechnology'
#      >>> bt.RED["gene_therapy"].summary
#      "Treating disease by adding, silencing, replacing or editing genetic material inside a patient's cells."
#      >>> len(bt.branches()), len(bt.subtypes())
#      (10, 85)
#
#  WHAT THIS FILE IS
#  The public API surface, and nothing else. It contains no logic and no data:
#  it re-exports names from `core` and binds the ten branch constants. Everything
#  a user is meant to touch appears in `__all__` below; anything not listed is
#  internal and may change without a major version bump.
#
#  THE HARD CONSTRAINT
#  Zero runtime dependencies. Nothing below imports anything outside the
#  standard library and this package. See GOVERNANCE.md section 3.3.
#
#  A NOTE ON THE DARK BRANCH
#  `bt.DARK` covers biosafety, biosecurity governance, dual-use research
#  oversight, gene synthesis screening, biosurveillance, medical
#  countermeasures, microbial forensics and biological arms control. It is
#  documented exclusively from the protective side and contains no operational
#  information about causing harm. See SECURITY.md section 2.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

# -----------------------------------------------------------------------------
#  Controlled vocabularies. Re-exported at the top level because filtering is
#  a first-class use of this library and `from biotechnology import Maturity`
#  should just work.
# -----------------------------------------------------------------------------
from .core.enums import (
    Domain,
    EvidenceLevel,
    Maturity,
    RegulatoryStatus,
    RiskTier,
    Scale,
    vocabularies,
)

# -----------------------------------------------------------------------------
#  The exception hierarchy. Every error this package raises inherits from
#  `BiotechnologyError`, so a caller can wrap the whole library in one except
#  clause while ordinary Python errors still propagate.
# -----------------------------------------------------------------------------
from .core.errors import (
    BiotechnologyError,
    BrokenCrossReferenceError,
    CalculationError,
    DomainError,
    DuplicateKeyError,
    LookupErrorBase,
    PathSyntaxError,
    SchemaError,
    UnitError,
    UnknownBranchError,
    UnknownFormulaError,
    UnknownNodeError,
    UnknownSubtypeError,
    ValidationError,
)

# -----------------------------------------------------------------------------
#  Record types.
# -----------------------------------------------------------------------------
from .core.models import Branch, Metric, Milestone, Node, Subtype

# -----------------------------------------------------------------------------
#  Path helpers. Useful to callers validating user input before a lookup.
# -----------------------------------------------------------------------------
from .core.paths import is_branch_path, is_subtype_path, parse_path, slugify

# -----------------------------------------------------------------------------
#  The registry: lookup, listing, filtering, graph traversal.
# -----------------------------------------------------------------------------
from .core.registry import (
    branch_keys,
    branches,
    by_domain,
    by_maturity,
    by_risk_tier,
    by_scale,
    by_sdg,
    counts,
    exists,
    get,
    get_branch,
    get_subtype,
    iter_nodes,
    related_to,
    resolve,
    subtype_paths,
    subtypes,
    timeline,
)

__version__ = "0.1.0"

__author__ = "Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov"
__email__ = "yunus.imanov@metropolia.fi"
__license__ = "EUPL-1.2"
__url__ = "https://github.com/olaflaitinen/biotechnology"


# =============================================================================
#  BRANCH CONSTANTS
#
#  Bound once, at import, from the registry. These are the primary entry point
#  for most users: `bt.RED` reads better than `bt.get_branch("red")` and is
#  discoverable by autocompletion, which matters for a library whose users are
#  frequently not habitual programmers.
# =============================================================================

#: Medicine, health care and pharmaceuticals.
RED = get_branch("red")

#: Agriculture, livestock and primary food production.
GREEN = get_branch("green")

#: Industrial processes, biofuels and biomaterials.
WHITE = get_branch("white")

#: Marine and aquatic resources.
BLUE = get_branch("blue")

#: Food production, fermentation and nutrition.
YELLOW = get_branch("yellow")

#: Environmental protection, waste management and ecological balance.
GREY = get_branch("grey")

#: US-spelling alias of :data:`GREY`. The same object, not a copy.
GRAY = GREY

#: Arid zones, deserts and degraded land.
BROWN = get_branch("brown")

#: Bioinformatics, computation, data analysis and nanobiotechnology.
GOLD = get_branch("gold")

#: Biosecurity, biosafety and the governance of misuse risk. Defensive only.
DARK = get_branch("dark")

#: Law, ethics, patents and intellectual property.
PURPLE = get_branch("purple")

#: Every branch, in colour-wheel order. Same objects as the constants above.
ALL_BRANCHES = branches()


# =============================================================================
#  CONVENIENCE RE-EXPORTS
#  Deferred imports, because these subpackages are larger than most callers
#  need and there is no reason to pay for them on `import biotechnology`.
# =============================================================================
def __getattr__(name: str) -> object:
    """Lazily expose the heavier subpackages as attributes.

    ``bt.formulas``, ``bt.organisms``, ``bt.techniques``, ``bt.glossary``,
    ``bt.refs`` and ``bt.sdg`` are importable as attributes without being
    loaded eagerly. This keeps a bare ``import biotechnology`` cheap for the
    common case of navigating the taxonomy.
    """
    if name in {"formulas", "organisms", "techniques", "glossary", "refs", "sdg"}:
        import importlib

        module = importlib.import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


# =============================================================================
#  Search and export.
#  Imported after the branch constants because `core.search` reads the registry
#  at import time to build its ranking tables.
# =============================================================================
from .core.export import to_csv, to_dict, to_dot, to_json, to_markdown  # noqa: E402
from .core.search import search  # noqa: E402
from .core.validation import validate  # noqa: E402

# `tree` lives in export but is used often enough to deserve a short name.
from .core.export import tree  # noqa: E402


__all__ = [
    # -- metadata -------------------------------------------------------------
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__url__",
    # -- record types ---------------------------------------------------------
    "Branch",
    "Subtype",
    "Metric",
    "Milestone",
    "Node",
    # -- controlled vocabularies ----------------------------------------------
    "Maturity",
    "RiskTier",
    "Scale",
    "EvidenceLevel",
    "Domain",
    "RegulatoryStatus",
    "vocabularies",
    # -- branch constants -----------------------------------------------------
    "RED",
    "GREEN",
    "WHITE",
    "BLUE",
    "YELLOW",
    "GREY",
    "GRAY",
    "BROWN",
    "GOLD",
    "DARK",
    "PURPLE",
    "ALL_BRANCHES",
    # -- listing --------------------------------------------------------------
    "branches",
    "branch_keys",
    "subtypes",
    "subtype_paths",
    "iter_nodes",
    "counts",
    # -- lookup ---------------------------------------------------------------
    "get",
    "get_branch",
    "get_subtype",
    "resolve",
    "exists",
    # -- filtering and traversal ----------------------------------------------
    "search",
    "by_sdg",
    "by_domain",
    "by_maturity",
    "by_risk_tier",
    "by_scale",
    "related_to",
    "timeline",
    # -- paths ----------------------------------------------------------------
    "parse_path",
    "is_branch_path",
    "is_subtype_path",
    "slugify",
    # -- export ---------------------------------------------------------------
    "to_dict",
    "to_json",
    "to_csv",
    "to_markdown",
    "to_dot",
    "tree",
    "validate",
    # -- errors ---------------------------------------------------------------
    "BiotechnologyError",
    "LookupErrorBase",
    "UnknownBranchError",
    "UnknownSubtypeError",
    "UnknownNodeError",
    "UnknownFormulaError",
    "PathSyntaxError",
    "ValidationError",
    "SchemaError",
    "DuplicateKeyError",
    "BrokenCrossReferenceError",
    "CalculationError",
    "DomainError",
    "UnitError",
]
