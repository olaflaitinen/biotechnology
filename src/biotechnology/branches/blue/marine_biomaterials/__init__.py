# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  MARINE BIOMATERIALS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Turning crab shells, fish skins and seaweed into wound dressings, surgical
#  materials and gels, using what the seafood industry pays to throw away.
#
#  THIS RECORD ESCAPES THE CONSTRAINT THAT DEFINES ITS BRANCH
#  `blue.marine_natural_products` is governed by supply: a gram of compound per
#  tonne of animal, from creatures that cannot be farmed. This record has the
#  opposite position.
#
#      ITS RAW MATERIALS ARE WASTE. Crustacean shell from seafood processing,
#      skin and scale from filleting, seaweed from an industry already landing
#      tens of millions of tonnes. Abundant, cheap, and currently discarded at
#      cost.
#
#  So the constraint is not getting the material. It is that THE MATERIAL IS
#  VARIABLE.
#
#  WHY `metrics.py` OPENS WITH COMPOSITION RATHER THAN PERFORMANCE
#  Degree of deacetylation, uronic acid ratio and sulphation pattern are not
#  quality measures. They are statements of WHICH MATERIAL IS IN THE CONTAINER.
#
#      two chitosans differing in deacetylation   different solubility, charge
#                                                 and biological behaviour,
#                                                 sold under one name
#      two alginates differing in M/G ratio       one gives a stiff brittle gel,
#                                                 the other soft and elastic
#
#  A performance figure quoted without these parameters is not reproducible.
#  That single fact is why this field's regulated applications are so much
#  harder to reach than its laboratory results suggest, and why reviews have
#  identified standardisation as the principal barrier for two decades without
#  the reference materials being produced.
#
#  `narrative.ANALOGY` is reclaimed timber: abundant, cheap and already there,
#  and every plank a different age and density. For a fence that hardly
#  matters. For anything certified, every plank must be measured, and the
#  measuring costs more than the timber.
#
#  THE OTHER HALF: STRUCTURES RATHER THAN SUBSTANCES
#  Nacre is calcium carbonate plus a little protein, arranged in layers, and it
#  is orders of magnitude tougher than the mineral alone. Sponge biosilica
#  forms at seawater temperature where industrial silica needs great heat.
#  Mussels bond to wet rock, which synthetic adhesives do badly.
#
#  In each case the interest is in the ARRANGEMENT, so the work is biomimetic
#  rather than extractive. Which is fortunate, because harvesting the organism
#  is neither scalable nor acceptable.
#
#  THE CORAL CASE, WHERE THAT ARGUMENT WAS SETTLED IN PRACTICE
#  Coral skeleton has a pore structure close enough to human cancellous bone to
#  guide ingrowth, and clinically it worked. It was being cut from reefs. The
#  response was not to abandon the property but to reproduce it: first by
#  converting coral to hydroxyapatite, then by fully synthetic scaffolds with
#  the same architecture.
#
#      THE STRUCTURE WAS THE PRODUCT. THE ORGANISM WAS ONLY ITS FIRST
#      MANUFACTURER.
#
#  THE GOVERNANCE SHAPE FOUND NOWHERE ELSE IN THE LIBRARY
#  The raw material arrives from the wrong direction: shell and skin are not
#  raw materials in law, they are ANIMAL BY-PRODUCTS, governed by rules written
#  to keep unfit material out of the food chain. Establishments must be
#  approved, categories determine permitted uses, and a device-grade material
#  must be traceable to a species and a consignment that a fish market does not
#  document.
#
#  And the same molecule meets four regimes: chitosan is a medical device as a
#  haemostat, a food additive in a drink, a fertilising product as a
#  biostimulant, and a registered chemical as a flocculant. One substance, four
#  authorisations, and a manufacturer must choose early.
#
#  WHAT THESE MATERIALS DO THAT SYNTHETICS DO BADLY
#      alginate    gels on contact with the calcium in wound fluid, so a
#                  dressing conforms and lifts off without tearing new tissue
#      chitosan    stops bleeding by a mechanism independent of the patient's
#                  own clotting, so it works under anticoagulation
#      agarose     underpins molecular biology
#      collagen    avoids mammalian sourcing, and its disease and religious
#                  objections
#
#  PACKAGE LAYOUT
#      narrative.py    waste as an advantage, variability as the price, and the
#                      reclaimed timber analogy
#      practice.py     applications BY MATERIAL CLASS, with the biomimetic
#                      group separated because it is not extractive
#      metrics.py      thirteen metrics opening with composition, since that is
#                      what decides which material you have
#      history.py      1811 to 2020, centred on the coral case
#      governance.py   the raw material as an animal by-product
#      linkage.py      the opposite constraint at the other end of the branch
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
KEY = "marine_biomaterials"

NAME = "Marine Biomaterials"

# "chitosan" and "alginate" are included as aliases because most readers arrive
# looking for a specific material rather than the category. "marine polymers"
# and "biomimetic materials" name the two halves of the record.
ALIASES = (
    "marine polymers",
    "chitosan",
    "alginate",
    "marine collagen",
    "biomimetic materials",
    "seafood waste valorisation",
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
