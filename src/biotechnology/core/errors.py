# =============================================================================
#  biotechnology.core.errors
# -----------------------------------------------------------------------------
#  The complete exception hierarchy of the package.
#
#  DESIGN RULE
#  Every exception raised anywhere in `biotechnology` inherits from
#  :class:`BiotechnologyError`. That single guarantee lets a caller write
#
#      try:
#          ...
#      except biotechnology.BiotechnologyError as exc:
#          log.warning("taxonomy problem: %s", exc)
#
#  and be certain nothing from this library escapes uncaught, while ordinary
#  Python errors (TypeError, MemoryError) still propagate normally.
#
#  SECOND DESIGN RULE
#  An error message must tell the reader how to fix the problem. "unknown
#  branch 'purple biotech'" is useless on its own; "unknown branch
#  'purple biotech'; did you mean 'purple'? valid: red, green, ..." is not.
#  Every class below therefore builds its own message from structured fields
#  and, where it can, offers a suggestion computed with difflib.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

import difflib
from typing import Iterable, List, Optional, Sequence

__all__ = [
    "BiotechnologyError",
    "LookupErrorBase",
    "UnknownBranchError",
    "UnknownSubtypeError",
    "UnknownNodeError",
    "UnknownFormulaError",
    "UnknownOrganismError",
    "UnknownTechniqueError",
    "UnknownTermError",
    "UnknownReferenceError",
    "PathSyntaxError",
    "ValidationError",
    "DuplicateKeyError",
    "BrokenCrossReferenceError",
    "SchemaError",
    "CalculationError",
    "DomainError",
    "ConvergenceError",
    "UnitError",
    "suggest",
]


# =============================================================================
#  Helper: fuzzy suggestion
# =============================================================================
def suggest(
    needle: str,
    candidates: Iterable[str],
    *,
    limit: int = 3,
    cutoff: float = 0.6,
) -> List[str]:
    """Return the closest spellings of ``needle`` found in ``candidates``.

    A thin wrapper over :func:`difflib.get_close_matches` that normalises
    case and separators first, so that ``"Gene-Therapy"`` still matches
    ``"gene_therapy"``.

    Parameters
    ----------
    needle:
        What the user actually typed.
    candidates:
        Every valid token.
    limit:
        Maximum number of suggestions to return.
    cutoff:
        Similarity threshold between 0 and 1. Lower values suggest more but
        risk nonsense; 0.6 is the difflib default and works well for keys of
        this length.

    Examples
    --------
    >>> suggest("gene therapie", ["gene_therapy", "cell_therapy"])
    ['gene_therapy']
    >>> suggest("zzz", ["gene_therapy"])
    []
    """

    def _norm(text: str) -> str:
        return text.strip().lower().replace("-", "_").replace(" ", "_")

    pool = {_norm(c): c for c in candidates}
    matches = difflib.get_close_matches(_norm(needle), list(pool), limit, cutoff)
    return [pool[m] for m in matches]


def _format_message(
    what: str,
    key: str,
    candidates: Sequence[str],
    *,
    max_listed: int = 20,
) -> str:
    """Build a consistent "unknown X" message with suggestions and a list."""
    parts = [f"unknown {what} {key!r}"]
    hints = suggest(key, candidates)
    if hints:
        quoted = " or ".join(repr(h) for h in hints)
        parts.append(f"did you mean {quoted}?")
    if candidates:
        listed = list(candidates)[:max_listed]
        tail = ", ..." if len(candidates) > max_listed else ""
        parts.append(f"valid {what}s: {', '.join(listed)}{tail}")
    return "; ".join(parts)


# =============================================================================
#  Root
# =============================================================================
class BiotechnologyError(Exception):
    """Base class for every error raised by the ``biotechnology`` package."""


# =============================================================================
#  Lookup failures
# =============================================================================
class LookupErrorBase(BiotechnologyError, KeyError):
    """Base class for "I could not find that" errors.

    Inherits from :class:`KeyError` as well so that existing code written
    around ``dict``-style access keeps working:

        try:
            bt.get("red.no_such_thing")
        except KeyError:
            ...

    .. note::
       ``KeyError.__str__`` normally wraps its argument in quotes, which
       mangles a carefully written sentence. ``__str__`` is overridden below
       to return the message verbatim.
    """

    #: Human word used in the generated message; overridden per subclass.
    NOUN = "item"

    def __init__(
        self,
        key: str,
        candidates: Sequence[str] = (),
        message: Optional[str] = None,
    ) -> None:
        self.key = key
        self.candidates = tuple(candidates)
        self.suggestions = tuple(suggest(key, candidates))
        self.message = message or _format_message(self.NOUN, key, self.candidates)
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class UnknownBranchError(LookupErrorBase):
    """Raised when a colour branch key or alias cannot be resolved."""

    NOUN = "branch"


class UnknownSubtypeError(LookupErrorBase):
    """Raised when a subtype key cannot be resolved inside a known branch."""

    NOUN = "subtype"

    def __init__(
        self,
        key: str,
        candidates: Sequence[str] = (),
        branch_key: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:
        self.branch_key = branch_key
        if message is None and branch_key:
            message = _format_message(f"subtype in branch {branch_key!r}", key, candidates)
        super().__init__(key, candidates, message)


class UnknownNodeError(LookupErrorBase):
    """Raised when a dotted path resolves to neither a branch nor a subtype.

    Kept as a distinct, broad class so callers who do not care whether the
    missing thing was a branch or a subtype can catch just this one. Both
    :class:`UnknownBranchError` and :class:`UnknownSubtypeError` are *not*
    subclasses of it; catch :class:`LookupErrorBase` to get all three.
    """

    NOUN = "node"


class UnknownFormulaError(LookupErrorBase):
    """Raised when a formula key is not present in the formula registry."""

    NOUN = "formula"


class UnknownOrganismError(LookupErrorBase):
    """Raised when an organism key is not present in the organism registry."""

    NOUN = "organism"


class UnknownTechniqueError(LookupErrorBase):
    """Raised when a technique key is not present in the technique registry."""

    NOUN = "technique"


class UnknownTermError(LookupErrorBase):
    """Raised when a glossary term cannot be found."""

    NOUN = "glossary term"


class UnknownReferenceError(LookupErrorBase):
    """Raised when a citation key is not present in the bibliography."""

    NOUN = "reference"


class PathSyntaxError(BiotechnologyError, ValueError):
    """Raised when a dotted path is malformed rather than merely unknown.

    Malformed means the *shape* is wrong - an empty string, a leading dot, two
    dots in a row, more than two segments - as opposed to a well-formed path
    that simply names something that does not exist.
    """

    def __init__(self, path: str, reason: str) -> None:
        self.path = path
        self.reason = reason
        super().__init__(f"malformed path {path!r}: {reason}")


# =============================================================================
#  Data-integrity failures
# =============================================================================
class ValidationError(BiotechnologyError):
    """Base class for problems found while checking the taxonomy itself.

    These are author errors, not user errors: they mean a data module in this
    repository is inconsistent. The validation suite in
    :mod:`biotechnology.core.validation` raises them, and continuous
    integration fails the build.
    """

    def __init__(self, message: str, location: Optional[str] = None) -> None:
        self.location = location
        self.message = message
        super().__init__(f"{location}: {message}" if location else message)


class DuplicateKeyError(ValidationError):
    """Raised when two records inside one namespace share a key."""

    def __init__(self, key: str, namespace: str) -> None:
        self.key = key
        self.namespace = namespace
        super().__init__(f"duplicate key {key!r}", location=namespace)


class BrokenCrossReferenceError(ValidationError):
    """Raised when a record points at a path that does not exist.

    The taxonomy is a graph: subtypes cite formulas, organisms, techniques,
    glossary terms and other subtypes. Every one of those edges is checked at
    build time so that documentation never renders a dead link.
    """

    def __init__(self, source: str, target: str, kind: str = "related") -> None:
        self.source = source
        self.target = target
        self.kind = kind
        super().__init__(
            f"{kind} cross-reference points at missing {target!r}", location=source
        )


class SchemaError(ValidationError):
    """Raised when a record is missing a required field or has a wrong type."""

    def __init__(self, field: str, expected: str, got: object, location: str) -> None:
        self.field = field
        self.expected = expected
        self.got = got
        super().__init__(
            f"field {field!r} should be {expected}, got {type(got).__name__}",
            location=location,
        )


# =============================================================================
#  Calculation failures (raised by biotechnology.formulas)
# =============================================================================
class CalculationError(BiotechnologyError):
    """Base class for anything that goes wrong inside a formula."""


class DomainError(CalculationError, ValueError):
    """Raised when an argument lies outside the valid domain of a formula.

    Example: a negative optical density, a pH of 20, a dilution factor of
    zero. The message always names the offending parameter, the value given
    and the accepted range, because a bare "math domain error" from the
    standard library is impossible to debug in a long pipeline.
    """

    def __init__(
        self,
        parameter: str,
        value: object,
        expected: str,
        formula: Optional[str] = None,
    ) -> None:
        self.parameter = parameter
        self.value = value
        self.expected = expected
        self.formula = formula
        prefix = f"{formula}: " if formula else ""
        super().__init__(
            f"{prefix}parameter {parameter!r} = {value!r} is out of range; expected {expected}"
        )


class ConvergenceError(CalculationError, RuntimeError):
    """Raised when an iterative solver fails to converge in time."""

    def __init__(self, formula: str, iterations: int, residual: float) -> None:
        self.formula = formula
        self.iterations = iterations
        self.residual = residual
        super().__init__(
            f"{formula}: no convergence after {iterations} iterations "
            f"(residual {residual:.3g})"
        )


class UnitError(CalculationError, ValueError):
    """Raised when incompatible units are combined or an unknown unit is used."""

    def __init__(self, message: str, unit: Optional[str] = None) -> None:
        self.unit = unit
        super().__init__(message if unit is None else f"{message} (unit {unit!r})")
