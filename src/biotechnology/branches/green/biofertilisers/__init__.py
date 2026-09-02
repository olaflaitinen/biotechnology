# =============================================================================
#  biotechnology.branches.green.biofertilisers
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  GREEN BIOTECHNOLOGY  ->  BIOFERTILISERS AND
#                                               PLANT-GROWTH-PROMOTING MICROBES
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Some soil microbes pull nitrogen out of the air or unlock phosphate the
#  plant cannot reach, and feed it to the roots. Biofertilisers are those
#  microbes, packaged and applied deliberately.
#
#  THE OLDEST COMMERCIAL BIOTECHNOLOGY IN THIS TAXONOMY
#  Nitragin, a living microbial product, went on sale to farmers in 1895. That
#  is thirty-three years before penicillin was noticed and eighty-seven before
#  the first recombinant medicine.
#
#  THE NUMBER THAT FRAMES THE WHOLE RECORD
#  Manufacturing synthetic nitrogen by the Haber-Bosch process consumes one to
#  two per cent of global primary energy and supplies the nitrogen in roughly
#  half the protein eaten by humanity. Any biological substitution therefore
#  matters at planetary scale even where it replaces only part of the load.
#  Read the 1888 and 1913 entries in `history.py` together: biology could fix
#  nitrogen, and twenty-five years later chemistry could do it faster.
#  Everything since has been an argument about the terms of that trade.
#
#  THE DISTINCTION THIS RECORD INSISTS ON
#  A VIABLE CELL COUNT IS NOT AN EFFECT. Colony forming units per gram measure
#  how many living organisms are in the bag. They say nothing about whether
#  those organisms will survive sowing, colonise a root, outcompete the native
#  population, or fix any nitrogen at all. A product can meet its label
#  specification perfectly and do nothing in a field. `metrics.py` is ordered
#  from what is easy to measure and weakly informative to what actually matters
#  and is hardest, for exactly that reason.
#
#  WHY THE FIELD'S REPUTATION IS WORSE THAN ITS SCIENCE
#  The binding constraint is establishment against an incumbent native
#  community, which is a competition problem rather than a biochemical one, and
#  it is why glasshouse results routinely fail in the field. On top of that,
#  independent testing has repeatedly found products with far fewer viable
#  cells than labelled, the wrong organism, or nothing living at all. A farmer
#  who buys a dead product once does not buy a live one afterwards.
#
#  THE BOUNDARY WITH BIOPESTICIDES IS LEGAL, NOT BIOLOGICAL
#  The same Bacillus strain is a biofertiliser when sold for root growth and a
#  plant protection product when sold with a pathogen-suppression claim, at one
#  to two orders of magnitude more dossier cost. `governance.py` and
#  `linkage.py` both say so, because the split between these two records
#  reflects a regulatory line the microbiology does not respect.
#
#  PACKAGE LAYOUT
#      narrative.py    the tenant analogy, whose failure mode is the real one
#      practice.py     applications ordered by how well established the effect is
#      metrics.py      eight metrics, ordered easy-and-weak to hard-and-decisive
#      history.py      300 BCE to 2019, including the market's self-inflicted wound
#      governance.py   a century with no regulator, and the 2019 category that
#                      finally created one
#      linkage.py      the legal boundary, and the same operation in grey
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
KEY = "biofertilisers"

NAME = "Biofertilisers and Plant-Growth-Promoting Microbes"

# "biofertilizer" is included because the US spelling is at least as common in
# the literature as the British one used for the key. "biostimulant" is the EU
# regulatory term and increasingly the commercial one, and "rhizobium" and
# "mycorrhiza" are what a farmer or gardener is most likely to search for.
ALIASES = (
    "biofertilizer",
    "microbial inoculant",
    "inoculant",
    "rhizobium",
    "mycorrhiza",
    "pgpr",
    "biostimulant",
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
