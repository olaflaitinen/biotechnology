# =============================================================================
#  biotechnology.branches.grey.bioaugmentation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD SITS AT THE CENTRE OF THE MOST IMPORTANT CROSS-BRANCH PATTERN
#  IN THE LIBRARY, AND THE RELATED EDGES ARE CHOSEN TO MAKE IT TRACEABLE.
#
#      grey.bioaugmentation            introduced strains in soil and water
#      green.biofertilisers            introduced strains in agricultural soil
#      yellow.probiotics_and_prebiotics  introduced strains in the human gut
#
#  Three fields, in three different colours of this taxonomy, separated by
#  decades and by discipline, each independently establishing that an
#  established microbial community resists invasion and that introduced
#  organisms are cleared. Each field learned it the expensive way, and each
#  learned it without much reference to the others.
#
#  A reader who follows only one edge from this record should follow one of
#  those two, which is why they are placed first and second after the sibling.
#
#  `purple.synthetic_biology` is included for a reason that is easy to state
#  and important: it is now possible to build degraders no natural isolate can
#  match, and this record is the evidence that capability was never the binding
#  constraint. A better organism still has to survive the site. That is the
#  most useful thing this record has to say to a field that is not its own.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  TWO, AND THIS IS DELIBERATELY THE SHORTEST SDG TUPLE IN THE BRANCH.
#
#  Rule 12 asks whether a sceptical auditor would accept the claim. For a
#  practice whose central proposition usually fails controlled comparison, a
#  long list of development goals would be exactly the padding that rule
#  exists to catch. A technique that does not reliably work cannot claim broad
#  contributions on the basis of what it would achieve if it did.
#
#  Goal 6 is claimed on the applications that ARE supported: dechlorination
#  augmentation resolves groundwater plumes that would otherwise stall at a
#  more toxic intermediate, and reseeding restores a failed wastewater plant.
#  Both are real water outcomes with evidence behind them.
#
#  Goal 12 is claimed on a narrower and slightly unusual basis: the record's
#  finding redirects spending away from products that do not work, which is
#  responsible consumption in the plainest sense. It is claimed for the
#  evidence rather than for the technique.
#
#  GOALS 3, 11, 14 AND 15 ARE NOT CLAIMED, although the parent record
#  `grey.bioremediation` claims several of them. The difference is that this
#  record describes an ADDITION to that practice whose incremental benefit is
#  usually undetectable, and inheriting the parent's goals would credit this
#  record with outcomes the residents produced.
# =============================================================================
SDGS: Tuple[int, ...] = (
    6,  # Water, on the dechlorination and plant recovery cases specifically
    12,  # Responsible consumption, on not buying what does not work
)


# =============================================================================
#  GLOSSARY
#  Grouped: the practice, the ecology that defeats it, the exception, and the
#  evidence vocabulary a buyer needs.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the practice and its alternative --------------------------------------
    "bioaugmentation",
    "biostimulation",
    "inoculum",
    "microbial_consortium",
    "enrichment_culture",
    "seeding",
    "carrier_immobilisation",
    "encapsulation",
    # -- the ecology that defeats it -------------------------------------------
    "colonisation_resistance",
    "competitive_exclusion",
    "niche_occupancy",
    "protozoan_grazing",
    "bacteriophage_predation",
    "population_decline",
    "establishment",
    "acclimation",
    "indigenous_community",
    # -- the exception ---------------------------------------------------------
    "reductive_dechlorination",
    "vinyl_chloride",
    "functional_gene_marker",
    "capability_gap",
    # -- and what a buyer needs to be able to ask ------------------------------
    "control_plot",
    "incremental_benefit",
    "statistical_power",
    "confounding",
    "viable_count",
    "efficacy_evidence",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "bioaugmentation_field_evidence_review",
    "colonisation_resistance_soil_communities",
    "exxon_valdez_shoreline_bioremediation",
    "dehalococcoides_dechlorination",
    "dechlorinating_consortium_field_application",
    "introduced_strain_survival_soil",
    "activated_sludge_bioaugmentation_trials",
    "microbial_invasion_ecology",
)


# =============================================================================
#  RELATED
#  Six edges. The sibling first, then the two records that learned the same
#  lesson in other branches, then the alternative and the caution.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the practice this is an optional step within --------------------------
    "grey.bioremediation",
    # -- the same finding in agricultural soil ---------------------------------
    "green.biofertilisers",
    # -- the same finding in the human gut -------------------------------------
    "yellow.probiotics_and_prebiotics",
    # -- where seeding is uncontested, because there is no incumbent -----------
    "grey.wastewater_treatment",
    # -- how anyone knows whether the introduced population survived -----------
    "grey.environmental_biomonitoring",
    # -- better organisms are now buildable, and survival is still the limit ---
    "purple.synthetic_biology",
)
