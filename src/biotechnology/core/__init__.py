# =============================================================================
#  biotechnology.core
# -----------------------------------------------------------------------------
#  The machinery layer. Everything here is about SHAPE rather than SUBSTANCE:
#  what a record is, what a vocabulary may contain, how a path is parsed, how
#  a lookup fails. No biological fact lives in this package. Those are in
#  `biotechnology.branches` and in the registries beside it.
#
#  WHY THIS FILE EXISTS AT ALL, AND WHY ITS ABSENCE WAS A RELEASE BLOCKER
#  This file was missing, and the consequence was not cosmetic.
#
#  `pyproject.toml` discovers packages with the default setuptools directive:
#
#      [tool.setuptools.packages.find]
#      where = ["src"]
#
#  That directive finds REGULAR packages, and a regular package is a directory
#  containing `__init__.py`. Without this file, `setuptools.find_packages`
#  returned 58 packages and `biotechnology.core` was not among them, so the
#  built wheel shipped `biotechnology/__init__.py` without the package that
#  file imports from on its very first line:
#
#      from .core.enums import Domain, EvidenceLevel, Maturity, ...
#
#  An installed copy therefore raised `ModuleNotFoundError` on `import
#  biotechnology`. It worked in a source checkout only because an editable
#  install and a bare `sys.path` entry both fall back to implicit namespace
#  packages, which is exactly the case that hides the defect from the person
#  most likely to notice it.
#
#  `tools/check_packaging.py` now asserts that every directory containing a
#  module is discoverable, so this cannot recur silently.
#
#  WHAT THIS FILE RE-EXPORTS
#  The union of the five core modules' public names, so that `from
#  biotechnology.core import Subtype` works as readily as reaching into
#  `biotechnology.core.models`. The top-level `biotechnology` package re-exports
#  a curated subset of the same names; this one is deliberately complete,
#  because a caller who has descended to `core` is asking for the machinery.
#
#  IMPORT ORDER MATTERS HERE AND IS NOT ALPHABETICAL
#  `registry` builds its indexes eagerly at import time and depends on every
#  other module in this package, so it is imported last. The four before it are
#  ordered by dependency: enums and errors depend on nothing, models depends on
#  enums, paths depends on errors.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

# -----------------------------------------------------------------------------
#  Controlled vocabularies. Six closed sets, plus the base class they share and
#  the introspection helper that lists them.
# -----------------------------------------------------------------------------
from .enums import (
    DescribedEnum,
    Domain,
    EvidenceLevel,
    Maturity,
    RegulatoryStatus,
    RiskTier,
    Scale,
    vocabularies,
)

# -----------------------------------------------------------------------------
#  The exception hierarchy, rooted at `BiotechnologyError`.
#
#  Note that four of these name registry entries that do not exist yet:
#  `UnknownOrganismError`, `UnknownTechniqueError`, `UnknownTermError` and
#  `UnknownReferenceError`. They are exported anyway, because the errors module
#  defines them and hiding a defined public name behind a missing registry
#  would be a worse inconsistency than exporting one that nothing raises yet.
# -----------------------------------------------------------------------------
from .errors import (
    BiotechnologyError,
    BrokenCrossReferenceError,
    CalculationError,
    ConvergenceError,
    DomainError,
    DuplicateKeyError,
    LookupErrorBase,
    PathSyntaxError,
    SchemaError,
    UnitError,
    UnknownBranchError,
    UnknownFormulaError,
    UnknownNodeError,
    UnknownOrganismError,
    UnknownReferenceError,
    UnknownSubtypeError,
    UnknownTechniqueError,
    UnknownTermError,
    ValidationError,
    suggest,
)

# -----------------------------------------------------------------------------
#  Record types. All frozen, all hashable, all typed.
# -----------------------------------------------------------------------------
from .models import Branch, Metric, Milestone, Node, Subtype

# -----------------------------------------------------------------------------
#  The dotted-address grammar.
# -----------------------------------------------------------------------------
from .paths import (
    MAX_SEGMENTS,
    SEGMENT_PATTERN,
    ParsedPath,
    is_branch_path,
    is_subtype_path,
    join_path,
    normalise_token,
    parse_path,
    slugify,
)

# -----------------------------------------------------------------------------
#  The registry. Imported last: it walks every branch package and builds its
#  indexes at import time, so it depends on everything above.
# -----------------------------------------------------------------------------
from .registry import (
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

__all__ = [
    # -- enums ----------------------------------------------------------------
    "DescribedEnum",
    "Domain",
    "EvidenceLevel",
    "Maturity",
    "RegulatoryStatus",
    "RiskTier",
    "Scale",
    "vocabularies",
    # -- errors ---------------------------------------------------------------
    "BiotechnologyError",
    "BrokenCrossReferenceError",
    "CalculationError",
    "ConvergenceError",
    "DomainError",
    "DuplicateKeyError",
    "LookupErrorBase",
    "PathSyntaxError",
    "SchemaError",
    "UnitError",
    "UnknownBranchError",
    "UnknownFormulaError",
    "UnknownNodeError",
    "UnknownOrganismError",
    "UnknownReferenceError",
    "UnknownSubtypeError",
    "UnknownTechniqueError",
    "UnknownTermError",
    "ValidationError",
    "suggest",
    # -- models ---------------------------------------------------------------
    "Branch",
    "Metric",
    "Milestone",
    "Node",
    "Subtype",
    # -- paths ----------------------------------------------------------------
    "MAX_SEGMENTS",
    "SEGMENT_PATTERN",
    "ParsedPath",
    "is_branch_path",
    "is_subtype_path",
    "join_path",
    "normalise_token",
    "parse_path",
    "slugify",
    # -- registry -------------------------------------------------------------
    "branch_keys",
    "branches",
    "by_domain",
    "by_maturity",
    "by_risk_tier",
    "by_scale",
    "by_sdg",
    "counts",
    "exists",
    "get",
    "get_branch",
    "get_subtype",
    "iter_nodes",
    "related_to",
    "resolve",
    "subtype_paths",
    "subtypes",
    "timeline",
]
