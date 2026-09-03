# =============================================================================
#  biotechnology.sdg
# -----------------------------------------------------------------------------
#  The seventeen Sustainable Development Goals, as adopted by the United
#  Nations General Assembly in Resolution 70/1 of 25 September 2015.
#
#  WHY THIS REGISTRY EXISTS AND WHY IT IS THE FIRST ONE WRITTEN
#  `Subtype.sdg_titles` has always done `from ..sdg import title_of`. The
#  package was an empty directory, so calling that property raised ImportError
#  on any record. It is the smallest of the six registries and the only one
#  that can be completed rather than merely started, because its contents are
#  a fixed, published, seventeen-item list rather than an open corpus.
#
#  THE TITLES ARE THE OFFICIAL SHORT TITLES AND ARE NOT PARAPHRASED
#  Every string in GOALS is the wording from the resolution, reduced to ASCII
#  where the source uses a typographic character and not otherwise altered.
#  These get cited, and a paraphrase that drifted would make a citation wrong
#  in a way nobody would notice.
#
#  WHAT THIS REGISTRY DELIBERATELY DOES NOT CARRY
#  The 169 targets and the 231 indicators. They are the right level for
#  measuring a country's progress and the wrong level for a taxonomy record:
#  a subtype cites "goal 6" because its work bears on clean water, not because
#  it moves indicator 6.3.1. Recording targets here would invite records to
#  claim them, and STYLE_GUIDE.md rule 12 exists precisely to stop that. Where
#  a record's claim really does rest on one target, its linkage facet says so
#  in prose.
#
#  ON RULE 12, WHICH IS WHAT THIS REGISTRY IS ACTUALLY FOR
#  An SDG number attached to a record is the easiest unearned claim in the
#  library. The rule asks whether a sceptical auditor would accept it. This
#  module supplies the vocabulary; it cannot supply the judgement, and it does
#  not pretend to. `themes` groups the goals so a reader can see at a glance
#  when a record has claimed across an implausible spread.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Tuple

from ..core.errors import BiotechnologyError, suggest

__all__ = [
    "Goal",
    "GOALS",
    "KEYS",
    "goals",
    "get",
    "title_of",
    "short_of",
    "exists",
    "themes",
    "by_theme",
    "UnknownGoalError",
]


# =============================================================================
#  ERROR
#
#  A goal number is validated in more than one place, so the failure gets its
#  own type rather than a bare ValueError. It inherits from BiotechnologyError
#  like everything else, so a caller wrapping the library in one except clause
#  still catches it.
# =============================================================================


class UnknownGoalError(BiotechnologyError):
    """Raised when a goal number is not one of the seventeen."""

    def __init__(self, value: object) -> None:
        self.value = value
        super().__init__(
            "unknown Sustainable Development Goal {0!r}; the goals are "
            "numbered 1 to 17".format(value)
        )


# =============================================================================
#  THE RECORD
#
#  A plain frozen carrier. It is not a dataclass because `core.models` owns the
#  dataclass conventions for taxonomy records and this is a lookup table entry,
#  not a record. Keeping the two shapes visibly different is deliberate.
# =============================================================================


class Goal:
    """One Sustainable Development Goal.

    Attributes
    ----------
    number:
        1 to 17.
    short:
        The two or three word label the goals are usually referred to by, for
        a table column or a chart axis.
    title:
        The official short title from Resolution 70/1, verbatim.
    theme:
        Which of the five groupings the resolution's preamble describes this
        goal belongs to. See `themes` for why this is here.
    """

    __slots__ = ("number", "short", "title", "theme")

    def __init__(self, number: int, short: str, title: str, theme: str) -> None:
        self.number = number
        self.short = short
        self.title = title
        self.theme = theme

    def __str__(self) -> str:
        return "SDG {0}: {1}".format(self.number, self.title)

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return "Goal({0}, {1!r})".format(self.number, self.short)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Goal) and other.number == self.number

    def __hash__(self) -> int:
        return hash(("sdg", self.number))

    def to_dict(self) -> Dict[str, object]:
        return {
            "number": self.number,
            "short": self.short,
            "title": self.title,
            "theme": self.theme,
        }


# =============================================================================
#  THE FIVE THEMES
#
#  The resolution's preamble organises the goals under five headings, commonly
#  called the five Ps. They are recorded because they make an unearned claim
#  visible: a record citing goals from all five is almost certainly reaching,
#  and one citing three goals inside a single theme is almost certainly not.
#  That is a reviewer's heuristic rather than a rule, and it is offered as one.
# =============================================================================

PEOPLE = "people"
PLANET = "planet"
PROSPERITY = "prosperity"
PEACE = "peace"
PARTNERSHIP = "partnership"


# =============================================================================
#  THE GOALS
#
#  Titles verbatim from Resolution 70/1, transliterated to ASCII where the
#  source uses a typographic character. Nothing else is altered.
# =============================================================================

GOALS: Tuple[Goal, ...] = (
    Goal(
        1,
        "No poverty",
        "End poverty in all its forms everywhere",
        PEOPLE,
    ),
    Goal(
        2,
        "Zero hunger",
        "End hunger, achieve food security and improved nutrition and promote "
        "sustainable agriculture",
        PEOPLE,
    ),
    Goal(
        3,
        "Good health",
        "Ensure healthy lives and promote well-being for all at all ages",
        PEOPLE,
    ),
    Goal(
        4,
        "Quality education",
        "Ensure inclusive and equitable quality education and promote lifelong "
        "learning opportunities for all",
        PEOPLE,
    ),
    Goal(
        5,
        "Gender equality",
        "Achieve gender equality and empower all women and girls",
        PEOPLE,
    ),
    Goal(
        6,
        "Clean water",
        "Ensure availability and sustainable management of water and "
        "sanitation for all",
        PLANET,
    ),
    Goal(
        7,
        "Affordable energy",
        "Ensure access to affordable, reliable, sustainable and modern energy "
        "for all",
        PROSPERITY,
    ),
    Goal(
        8,
        "Decent work",
        "Promote sustained, inclusive and sustainable economic growth, full "
        "and productive employment and decent work for all",
        PROSPERITY,
    ),
    Goal(
        9,
        "Industry and infrastructure",
        "Build resilient infrastructure, promote inclusive and sustainable "
        "industrialization and foster innovation",
        PROSPERITY,
    ),
    Goal(
        10,
        "Reduced inequalities",
        "Reduce inequality within and among countries",
        PROSPERITY,
    ),
    Goal(
        11,
        "Sustainable cities",
        "Make cities and human settlements inclusive, safe, resilient and "
        "sustainable",
        PROSPERITY,
    ),
    Goal(
        12,
        "Responsible consumption",
        "Ensure sustainable consumption and production patterns",
        PLANET,
    ),
    Goal(
        13,
        "Climate action",
        "Take urgent action to combat climate change and its impacts",
        PLANET,
    ),
    Goal(
        14,
        "Life below water",
        "Conserve and sustainably use the oceans, seas and marine resources "
        "for sustainable development",
        PLANET,
    ),
    Goal(
        15,
        "Life on land",
        "Protect, restore and promote sustainable use of terrestrial "
        "ecosystems, sustainably manage forests, combat desertification, and "
        "halt and reverse land degradation and halt biodiversity loss",
        PLANET,
    ),
    Goal(
        16,
        "Peace and institutions",
        "Promote peaceful and inclusive societies for sustainable development, "
        "provide access to justice for all and build effective, accountable "
        "and inclusive institutions at all levels",
        PEACE,
    ),
    Goal(
        17,
        "Partnerships",
        "Strengthen the means of implementation and revitalize the global "
        "partnership for sustainable development",
        PARTNERSHIP,
    ),
)

#: Index, built once. The keys are integers here rather than strings, which is
#: the one place this registry differs in shape from its five siblings: an SDG
#: is cited by number in every record, and forcing a string key would make
#: every call site convert.
_BY_NUMBER: Dict[int, Goal] = {goal.number: goal for goal in GOALS}

#: Present for symmetry with the other registries, which `check_references.py`
#: and `core.validation` both read by this name.
KEYS: Tuple[int, ...] = tuple(sorted(_BY_NUMBER))


# -----------------------------------------------------------------------------
#  Import-time sanity. Cheap, and it fails loudly rather than producing a
#  registry that is quietly missing a goal.
# -----------------------------------------------------------------------------
if len(GOALS) != 17:  # pragma: no cover - structural
    raise ImportError("expected 17 Sustainable Development Goals, found {0}".format(len(GOALS)))
if KEYS != tuple(range(1, 18)):  # pragma: no cover - structural
    raise ImportError("the goals must be numbered 1 to 17 with no gaps")


# =============================================================================
#  LOOKUP
# =============================================================================


def goals() -> Tuple[Goal, ...]:
    """Every goal, in numerical order."""
    return GOALS


def get(number: int) -> Goal:
    """Resolve a goal by number.

    >>> get(6).short
    'Clean water'
    """
    try:
        return _BY_NUMBER[int(number)]
    except (KeyError, TypeError, ValueError):
        raise UnknownGoalError(number) from None


def title_of(number: int) -> str:
    """The official title of a goal.

    This is the function `Subtype.sdg_titles` calls, and the reason this
    registry was the first one written.

    >>> title_of(13)
    'Take urgent action to combat climate change and its impacts'
    """
    return get(number).title


def short_of(number: int) -> str:
    """The short label, for a table column or a chart axis.

    >>> short_of(15)
    'Life on land'
    """
    return get(number).short


def exists(number: object) -> bool:
    """Whether a value names a goal. Never raises.

    >>> exists(17), exists(18), exists("six")
    (True, False, False)
    """
    try:
        return int(number) in _BY_NUMBER  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return False


# =============================================================================
#  THEMES
# =============================================================================


def themes() -> Tuple[str, ...]:
    """The five groupings, in the order the resolution's preamble uses them."""
    return (PEOPLE, PLANET, PROSPERITY, PEACE, PARTNERSHIP)


def by_theme(theme: str) -> List[Goal]:
    """Goals in one theme.

    Raises
    ------
    UnknownGoalError
        For an unknown theme. The error type is shared rather than multiplied,
        and the message names the valid values, which is the convention every
        lookup in this library follows.
    """
    token = str(theme).strip().lower()
    if token not in themes():
        raise UnknownGoalError(
            "{0} (valid themes: {1})".format(theme, ", ".join(themes()))
        )
    return [goal for goal in GOALS if goal.theme == token]
