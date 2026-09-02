# =============================================================================
#  biotechnology.branches.red.regenerative_medicine
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  RED BIOTECHNOLOGY  ->  REGENERATIVE MEDICINE AND
#                                             TISSUE ENGINEERING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Rather than replacing a failing body part with metal or plastic, this field
#  tries to persuade the body to grow a working replacement out of living
#  tissue.
#
#  THE NUMBER THAT EXPLAINS THE WHOLE RECORD
#  Oxygen diffuses roughly one hundred to two hundred micrometres through
#  living tissue before it is exhausted. Anything thicker dies in the middle
#  unless it carries its own plumbing.
#
#  That is a physical bound, not a biological difficulty. It does not improve
#  with better cells, better media or better technique. It is why skin,
#  cartilage and cornea reached patients in the early 1980s and a liver has
#  not, why `practice.APPLICATIONS` is ordered by tissue thickness, and why
#  four decades of extraordinary tool development have not moved the limit.
#
#  A reader who does not know this will assume the obstacle is cell biology and
#  will misjudge every claim ever made about grown organs.
#
#  THE THREE-LEGGED STOOL
#  Every construct combines cells that do the work, a scaffold that holds them
#  in shape, and signals that tell them what to become. Remove one leg and it
#  fails. Note that scaffold stiffness is itself a signal: identical stem cells
#  become bone on a hard substrate and nerve on a soft one, so a scaffold with
#  the wrong modulus produces the wrong tissue rather than merely a weak one.
#
#  WHY IT IS THE ONLY RED-BRANCH RECORD WITH THE MATERIALS DOMAIN
#  Because a tissue construct fails as a material long before it fails as a
#  biological object, and because the scaffolds come from `white.biopolymers`
#  and `blue.marine_biomaterials`: alginate from seaweed, chitosan from
#  crustacean shells, collagen from bovine and marine sources. Follow those
#  edges in `linkage.py`.
#
#  WHAT THIS RECORD SAYS THAT THE FIELD USUALLY DOES NOT
#  Unproven stem cell clinics sell unregulated injections to desperate
#  patients. Three women were permanently blinded by intraocular injections
#  marketed as stem cell therapy. That is recorded in `history.py` as a
#  milestone and in `practice.CHALLENGES` as a challenge to this field, not as
#  somebody else's problem, because the clinics trade on the credibility of the
#  legitimate work.
#
#  PACKAGE LAYOUT
#      narrative.py    states the diffusion limit in plain language
#      practice.py     applications ordered by thickness, which is the point
#      metrics.py      materials science as much as biology
#      history.py      1975 to 2021, including a retraction and a blinding
#      governance.py   medicine, device and human tissue at once
#      linkage.py      the two materials edges that are easy to miss
#
#  The full facet contract is documented in
#  `branches/red/gene_therapy/__init__.py` and is identical for all eighty-five
#  subtype packages in this library.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ....core.models import Subtype

from . import governance, history, linkage, metrics, narrative, practice

__all__ = ["SUBTYPE"]


# =============================================================================
#  IDENTITY
# =============================================================================
KEY = "regenerative_medicine"

NAME = "Regenerative Medicine and Tissue Engineering"

# "stem cell therapy" is included with some reluctance. It is what most people
# search for, and it is also the phrase the unregulated clinic sector uses.
# Resolving it here, to a record that states plainly what the field can and
# cannot do, is better than leaving the term to point nowhere.
ALIASES = (
    "tissue engineering",
    "regenerative medicine",
    "bioprinting",
    "organoid",
    "stem cell therapy",
    "biofabrication",
)


# =============================================================================
#  ASSEMBLY
# =============================================================================
SUBTYPE = Subtype(
    # -- identity --------------------------------------------------------------
    key=KEY,
    name=NAME,
    aliases=ALIASES,
    # -- narrative.py ----------------------------------------------------------
    summary=narrative.SUMMARY,
    description=narrative.DESCRIPTION,
    plain_language=narrative.PLAIN_LANGUAGE,
    analogy=narrative.ANALOGY,
    why_it_matters=narrative.WHY_IT_MATTERS,
    # -- practice.py -----------------------------------------------------------
    applications=practice.APPLICATIONS,
    technologies=practice.TECHNOLOGIES,
    organisms=practice.ORGANISMS,
    techniques=practice.TECHNIQUES,
    challenges=practice.CHALLENGES,
    # -- metrics.py ------------------------------------------------------------
    metrics=metrics.METRICS,
    formulas=metrics.FORMULAS,
    # -- history.py ------------------------------------------------------------
    milestones=history.MILESTONES,
    # -- governance.py ---------------------------------------------------------
    maturity=governance.MATURITY,
    risk_tier=governance.RISK_TIER,
    scale=governance.SCALE,
    domains=governance.DOMAINS,
    regulatory_status=governance.REGULATORY_STATUS,
    regulations=governance.REGULATIONS,
    standards=governance.STANDARDS,
    # -- linkage.py ------------------------------------------------------------
    sdgs=linkage.SDGS,
    glossary=linkage.GLOSSARY,
    references=linkage.REFERENCES,
    related=linkage.RELATED,
)
