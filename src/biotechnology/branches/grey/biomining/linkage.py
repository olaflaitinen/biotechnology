# =============================================================================
#  biotechnology.branches.grey.biomining.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `grey.bioremediation` IS FIRST FOR A REASON THAT IS UNIQUE IN THIS LIBRARY:
#  IT IS THE RECORD THAT CLEANS UP AFTER THIS ONE, USING THE SAME BIOLOGY IN
#  REVERSE.
#
#      here      sulphide oxidised, acid generated, metals dissolved
#      there     sulphate reduced, metals precipitated as sulphides again
#
#  Sulphate-reducing bioreactors treating acid mine drainage run the reaction
#  backwards. So the two records are not neighbours by subject matter; they are
#  the forward and reverse directions of one chemistry, and a reader who has
#  seen only one has seen half of a cycle.
#
#  `grey.phytoremediation` follows because the passive treatment of mine
#  drainage is largely a wetland practice, and because nickel phytomining and
#  nickel bioleaching are the same commercial proposition pursued by two
#  communities that rarely cite each other.
#
#  `white.biocatalysis` IS DELIBERATELY NOT LINKED. It would be a plausible
#  edge on the surface, since both records are about biology performing a
#  chemical conversion. But nothing here is a catalyst in that sense: the
#  organisms regenerate a stoichiometric reagent from air and water, and the
#  conversion is inorganic and abiotic. Linking it would blur exactly the
#  mechanism `narrative.py` exists to correct.
#
#  `blue.marine_natural_products` IS ALSO NOT LINKED despite deep sea mining
#  proposals appearing in both literatures, since a shared location is not a
#  shared mechanism.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  THREE, AND THIS RECORD IS THE HARDEST IN THE BRANCH TO ASSIGN, BECAUSE ITS
#  BENEFITS AND ITS HARMS RUN THROUGH THE SAME MECHANISM.
#
#  Goal 12 is claimed and is the strongest. Recovering metal from waste rock,
#  tailings and material below smelting grade is resource efficiency in the
#  plainest sense: it extends what a given quantity of disturbed ground yields.
#
#  Goal 9 is claimed on the industrial process itself, since it produces metals
#  at ambient temperature without the sulphur dioxide emission that made
#  historic smelting notorious, which is a cleaner industrial route rather than
#  a promise of one.
#
#  Goal 6 is claimed with a qualification that the reader deserves: the
#  sulphate-reducing treatment of acid mine drainage genuinely protects water,
#  and this same record's containment failures are among the most persistent
#  water pollution problems there are. It is claimed for the treatment
#  application, not for the extraction.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED, although ambient-temperature processing
#  uses far less energy than smelting. That is a saving relative to an
#  alternative, and a sceptical auditor under rule 12 would note that the
#  technique's net effect is to make more mining economic. The honest position
#  is that the climate accounting is genuinely unsettled, so no goal is
#  claimed on it.
#
#  GOAL 15 IS NOT CLAIMED EITHER, and the reason is worth stating: acid rock
#  drainage from residual heaps is a multi-century land and water liability,
#  and claiming a land goal for a process that creates one would fail the same
#  test.
# =============================================================================
SDGS: Tuple[int, ...] = (
    6,  # Water, for the drainage treatment application specifically
    9,  # Industry, on ambient-temperature processing without sulphur dioxide
    12,  # Responsible production, on metal from waste rock and low-grade ore
)


# =============================================================================
#  GLOSSARY
#  Grouped: the two processes, the chemistry, the operating problems, and the
#  liability.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the two processes that share the name ---------------------------------
    "bioleaching",
    "biooxidation",
    "heap_leaching",
    "dump_leaching",
    "in_situ_leaching",
    "tank_bioleaching",
    "refractory_gold",
    "solvent_extraction_electrowinning",
    # -- the chemistry, which is not biological --------------------------------
    "chemolithotroph",
    "ferric_iron",
    "ferrous_iron",
    "sulphide_mineral",
    "chalcopyrite",
    "pyrite",
    "arsenopyrite",
    "sulphur_oxidation",
    "acidophile",
    "thermophile",
    # -- what stops a heap working ---------------------------------------------
    "passivation",
    "jarosite",
    "channelling",
    "agglomeration",
    "shrinking_core",
    "cut_off_grade",
    # -- and what is left afterwards -------------------------------------------
    "acid_mine_drainage",
    "acid_base_accounting",
    "acid_generation_potential",
    "sulphate_reduction",
    "tailings",
    "mine_closure",
    "financial_assurance",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "bioleaching_industrial_review",
    "acidithiobacillus_isolation",
    "heap_bioleaching_copper_operations",
    "biooxidation_refractory_gold_plants",
    "heap_microbial_community_analysis",
    "chalcopyrite_passivation_mechanisms",
    "acid_rock_drainage_prediction",
    "sulphate_reducing_bioreactor_treatment",
    "mine_closure_liability_assessment",
)


# =============================================================================
#  RELATED
#  FIVE edges, which is the shortest tuple in this branch and is deliberate.
#  Rule 13 permits four to eight, and a sixth was drafted and cut: an edge to
#  `white.biobased_chemicals` on the grounds that both records produce
#  materials. That is a shared category rather than a shared mechanism, and
#  padding to six would have weakened the five that follow.
#
#  The reverse reaction comes first, since it is the record's most important
#  relationship and the one a reader is least likely to anticipate.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same chemistry run backwards, treating what this one produces -----
    "grey.bioremediation",
    # -- wetland treatment of mine drainage, and nickel by the other route -----
    "grey.phytoremediation",
    # -- monitoring drainage, heaps and receiving water over decades -----------
    "grey.environmental_biomonitoring",
    # -- inoculating freshly stacked ore, which has no incumbent community -----
    "grey.bioaugmentation",
    # -- what the acid drainage does to the receiving ecosystem ----------------
    "grey.biodiversity_conservation",
)
