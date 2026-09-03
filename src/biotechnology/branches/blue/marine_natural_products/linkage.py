# =============================================================================
#  biotechnology.branches.blue.marine_natural_products.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Every edge here is a route out of the supply problem, and reading them that
#  way is the most useful thing this facet can offer.
#
#      blue.marine_genomics            finds the symbiont that actually makes
#                                      the compound, which redirects the supply
#                                      effort from farming an animal to
#                                      culturing a bacterium.
#      white.biocatalysis              supplies the enzymatic steps that make a
#                                      semisynthetic route economic, which is
#                                      how the field's most cited success is
#                                      manufactured.
#      white.metabolic_engineering     expresses the biosynthetic cluster in a
#                                      host that will grow, turning an
#                                      uncultivable symbiont into a
#                                      fermentation.
#      red.pharmaceutical_biotechnology  takes the compound once supply is
#                                      solved and it becomes an ordinary
#                                      manufacturing question.
#
#  `purple.access_benefit_sharing` is not a governance footnote. `governance.py`
#  sets out that a medicine takes longer to develop than the interval over
#  which the access rules themselves changed, so a company may hold a library
#  assembled under three successive legal regimes. That is a live obstacle
#  rather than a compliance detail.
#
#  `grey.biodiversity_conservation` records the cost side. The screening
#  programmes of the 1970s and 1980s damaged the habitats they sampled, and a
#  reader who takes only the medicines from this record has taken half of it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and each is claimed narrowly.
#
#  Goal 3 is the primary claim and it is specific rather than general: this
#  record has produced treatments for conditions where alternatives are poor or
#  absent, including a pain therapy for patients who respond to nothing else.
#  It is not claimed on the strength of the search, only on the compounds that
#  reached patients.
#
#  Goal 14 is claimed with an unusual justification. It is not a benefit the
#  field delivers; it is a constraint the field has learned to accept. The
#  argument is that sustainable sourcing, symbiont culture and synthetic supply
#  exist substantially because collection at scale proved destructive, so the
#  record's own history is evidence for the goal rather than against it. A
#  sceptical auditor should press on this one.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on the specific medicines that reached patients
    9,  # Industry and innovation, on the synthesis and supply engineering
    14,  # Life below water, on sustainable sourcing rather than on benefit
)


# =============================================================================
#  GLOSSARY
#  Grouped: the search, the chemistry, the supply problem and its solutions,
#  then the law that shaped the field.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the search ------------------------------------------------------------
    "natural_product",
    "secondary_metabolite",
    "bioprospecting",
    "bioassay_guided_fractionation",
    "dereplication",
    "molecular_networking",
    "chemical_space",
    # -- the chemistry ---------------------------------------------------------
    "macrolide",
    "polyketide",
    "nonribosomal_peptide",
    "alkaloid",
    "terpenoid",
    "halogenation",
    "stereocentre",
    "pharmacophore",
    # -- the supply problem and the ways out -----------------------------------
    "total_synthesis",
    "semisynthesis",
    "analogue",
    "biosynthetic_gene_cluster",
    "heterologous_expression",
    "symbiont",
    "silent_gene_cluster",
    # -- how the compound is judged --------------------------------------------
    "cytotoxicity",
    "half_maximal_inhibitory_concentration",
    "therapeutic_index",
    "antibody_drug_conjugate",
    # -- the law ---------------------------------------------------------------
    "access_and_benefit_sharing",
    "prior_informed_consent",
    "voucher_specimen",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "marine_natural_products_review",
    "bergmann_sponge_nucleosides",
    "trabectedin_semisynthesis",
    "eribulin_analogue_development",
    "ziconotide_clinical_review",
    "bryostatin_supply_problem",
    "symbiont_origin_of_invertebrate_metabolites",
    "marine_genome_mining_review",
    "natural_products_industry_withdrawal",
    "nagoya_protocol",
)


# =============================================================================
#  RELATED
#  Seven edges. The first three are the routes out of the supply problem.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- finds who actually makes the compound ---------------------------------
    "blue.marine_genomics",
    # -- makes a semisynthetic route economic ----------------------------------
    "white.biocatalysis",
    # -- expresses the cluster in something that grows -------------------------
    "white.metabolic_engineering",
    # -- where the compound goes once supply is solved -------------------------
    "red.pharmaceutical_biotechnology",
    # -- the same chemistry read as a defence rather than a drug ---------------
    "blue.marine_biofouling_control",
    # -- what the screening programmes cost the habitats -----------------------
    "grey.biodiversity_conservation",
    # -- three legal regimes, none retroactive ---------------------------------
    "purple.access_benefit_sharing",
)
