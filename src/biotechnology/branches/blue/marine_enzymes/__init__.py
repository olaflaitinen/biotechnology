# =============================================================================
#  biotechnology.branches.blue.marine_enzymes
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  BLUE BIOTECHNOLOGY  ->  MARINE ENZYMES
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Catalysts taken from sea creatures that had to work in permanent cold, under
#  crushing pressure, or in salt strong enough to destroy ordinary proteins.
#
#  WHY THIS IS NOT SIMPLY PART OF `white.industrial_enzymes`
#  Provenance alone would not justify a separate record. An enzyme is not
#  interesting because it came from the sea; it is interesting when the sea
#  imposed a constraint terrestrial life never faced and the enzyme solved it.
#
#  THE INVERSION THIS RECORD IS BUILT ON
#  Most of the ocean by volume sits between about minus one and four degrees.
#  Enzymes that work there are not warm enzymes running slowly: they are
#  structurally distinct, more flexible, with lower activation energy, higher
#  rates in the cold and much lower thermal stability.
#
#  That is usually described as a trade in which stability is sacrificed for
#  activity. INDUSTRIALLY, THE DESCRIPTION IS BACKWARDS. The instability is the
#  product.
#
#      An enzyme that works at 4 degrees and is destroyed at 40 can be added to
#      a reaction, allowed to act, and then switched off by gentle warming.
#      No inhibitor. No separation step. No heat damage to the product.
#
#  So `metrics.py` deliberately inverts the ordering of
#  `white.industrial_enzymes`, which puts durability first. Here the
#  inactivation temperature is a product specification. The SAME physical
#  quantity is a virtue in one record and a selling point in the opposite
#  direction in the other, and nothing about the enzymology differs. The
#  application decides which end of the scale is wanted.
#
#  `narrative.ANALOGY` is a chisel made of ice, and its stated limit is the
#  honest half: for most work it is useless, and cold-adapted enzymes are
#  likewise excluded from every process involving heat.
#
#  THE RECORD CONTAINS BOTH TEMPERATURE EXTREMES
#  `metrics.py` records melting temperatures from roughly forty degrees to
#  above one hundred. That is not a range for marine enzymes; it is TWO
#  POPULATIONS. Permanently cold water gives one, hydrothermal vents give the
#  other, and the ocean contains both.
#
#  THE BRANCH'S LARGEST COMMERCIAL SUCCESS, STATED ACCURATELY
#  A high-fidelity proofreading polymerase from a deep-sea vent archaeon is in
#  most molecular biology laboratories in the world, and it supplies the
#  sequencing that `blue.marine_genomics` depends on.
#
#  It is routinely confused with the polymerase that made PCR practical, which
#  came from a TERRESTRIAL hot spring. `history.py` separates them in its 1976
#  and 1991 entries deliberately, because overstating the marine claim would be
#  easy and wrong. The marine contribution was proofreading and therefore
#  fidelity, which is a different and later capability.
#
#  WHY THIS RECORD HAS PRODUCTS AND ITS NEIGHBOUR HAS A SUPPLY PROBLEM
#  Read alongside `blue.marine_natural_products` and the branch becomes clear.
#  Both search the same organisms.
#
#      a molecule   must be made. A gram per tonne of animal is a supply
#                   problem, and SCALE there is BENCH.
#      an enzyme    is a gene. Once read it is expressed in a conventional host
#                   and fermented at ordinary scale, and SCALE here is
#                   INDUSTRIAL.
#
#  THE GOVERNANCE PROBLEM AT ITS SHARPEST
#  Because THE PRODUCT IS THE SEQUENCE, nothing physical need ever cross a
#  border. A gene read from another country's waters can be synthesised
#  anywhere and sold as a protein with no further reference to its origin.
#  That is exactly the case the digital sequence information debate exists
#  about, and it is why this record's obligations attach to information rather
#  than to material.
#
#  Downstream, the product is ordinary: an enzyme regulated as a chemical, with
#  food and feed authorisation on the same terms as any other. Marine origin
#  earns no concession. The whole governance difference sits upstream of the
#  fermenter.
#
#  TWO SETBACKS
#  In 1997, disputes over enzymes collected in protected areas made access and
#  benefit sharing a commercial question rather than a diplomatic one, and the
#  field's most valuable products predate any framework for sharing what they
#  earned. In 2012, sequence mining began producing candidates far faster than
#  they could be expressed, because proteins evolved for cold and pressure
#  frequently aggregate in mesophilic hosts. The bottleneck moved from finding
#  to obtaining a working protein, and it has stayed there.
#
#  PACKAGE LAYOUT
#      narrative.py    why fragility is the feature, and the ice chisel
#      practice.py     applications by WHICH ADAPTATION is being bought
#      metrics.py      eleven metrics, inverting the industrial ordering
#      history.py      1969 to 2023, separating the marine polymerase from the
#                      terrestrial one it is confused with
#      governance.py   why the product being a sequence sharpens everything
#      linkage.py      why SDG 14 is deliberately not claimed
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
KEY = "marine_enzymes"

NAME = "Marine Enzymes"

# "extremozymes" is the term the field uses for itself and is broader than
# marine, but a reader searching it is looking for this record. "cold active
# enzymes" and "psychrophilic enzymes" name the largest group by application.
ALIASES = (
    "extremozymes",
    "cold active enzymes",
    "psychrophilic enzymes",
    "marine biocatalysts",
    "deep sea enzymes",
    "halophilic enzymes",
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
