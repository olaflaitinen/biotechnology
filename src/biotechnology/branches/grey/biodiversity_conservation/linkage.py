# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE EDGES OUT OF THIS RECORD RUN MOSTLY TO OTHER BRANCHES, WHICH IS UNUSUAL
#  AND IS CORRECT.
#
#  This is the last record in the grey branch and it is the one least like the
#  others. The rest of grey biotechnology treats a stream, a site or a plume.
#  This one manages populations, and the methods it uses belong to plant
#  breeding, animal reproduction and clinical genomics rather than to
#  environmental engineering. Linking mostly inside the branch would have been
#  tidy and would have misdescribed where the work actually comes from.
#
#  `green.animal_biotechnology` IS FIRST AND IT IS THE STRONGEST EDGE IN THE
#  RECORD. Artificial insemination, embryo transfer, cryopreservation and
#  somatic cell nuclear transfer were all developed for livestock, for
#  commercial reasons, on species with reproductive biology that had been
#  studied for decades. Conservation inherited them and applies them to animals
#  whose reproductive biology is largely unknown, which is exactly why the
#  success rates in `metrics.py` are what they are.
#
#  `purple.access_benefit_sharing` IS NOT A COURTESY EDGE. It is the constraint
#  under which the entire field operates, and `governance.py` argues that the
#  permitting burden researchers experience as friction is a deliberate
#  correction of a century of one-directional material flow.
#
#  `grey.biomining` IS DELIBERATELY NOT LINKED FROM HERE even though that
#  record links to this one. The relationship is real and asymmetric: acid
#  drainage damages the ecosystems this record protects, which is a reason for
#  that record to point here and not a reason for this record's six edges to
#  include a pollution source. Rule 13 asks for the most useful edges, not for
#  reciprocity.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  THREE, AND THE RESTRAINT IS THE POINT.
#
#  This record could plausibly reach for a long list, since biodiversity
#  touches food, water, health and climate. Under rule 12 almost all of that
#  would fail, because the record's own `narrative.py` states that habitat loss
#  drives extinction and that nothing here addresses it. A field that manages
#  consequences should not claim credit for outcomes that depend on causes it
#  does not touch.
#
#  Goal 15 is the record's home and is claimed without qualification. Halting
#  biodiversity loss and preventing extinction of threatened species is what
#  every application here is directed at.
#
#  Goal 14 is claimed on the marine equivalent, since biobanking, population
#  genomics and environmental DNA survey apply to marine species and the
#  legal instruments differ.
#
#  Goal 16 is the unusual one and it is earned. Wildlife trade forensics
#  supports enforcement against organised trafficking, and the access and
#  benefit sharing framework in `governance.py` is an equity instrument
#  concerning who benefits from genetic resources. Both are institutional
#  rather than ecological outcomes.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED despite assisted gene flow being a
#  climate adaptation measure. Helping a few populations track a changing
#  climate is not a climate contribution, and a sceptical auditor would say so.
#
#  GOAL 2 IS NOT CLAIMED either, although crop wild relatives held in genebanks
#  underpin food security. That material is held under the plant genetic
#  resources treaty and belongs to `green.molecular_plant_breeding`, which uses
#  it.
# =============================================================================
SDGS: Tuple[int, ...] = (
    14,  # Oceans, on marine species survey, banking and population genetics
    15,  # Land, on halting biodiversity loss and preventing extinction
    16,  # Institutions, on trade enforcement and on equitable access
)


# =============================================================================
#  GLOSSARY
#  Grouped: the population genetics, the preservation, the interventions, and
#  the governance vocabulary.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the population genetics -----------------------------------------------
    "effective_population_size",
    "genetic_diversity",
    "heterozygosity",
    "inbreeding_depression",
    "outbreeding_depression",
    "genetic_load",
    "genetic_drift",
    "gene_flow",
    "bottleneck",
    "runs_of_homozygosity",
    "fixation_index",
    # -- what is being protected, and how it is defined ------------------------
    "conservation_unit",
    "evolutionarily_significant_unit",
    "population_viability_analysis",
    "red_list_category",
    "hybridisation",
    "introgression",
    # -- keeping material ------------------------------------------------------
    "biobank",
    "cryopreservation",
    "germplasm",
    "cell_line",
    "post_thaw_viability",
    "reference_genome",
    "museum_specimen_dna",
    # -- the interventions -----------------------------------------------------
    "genetic_rescue",
    "translocation",
    "assisted_gene_flow",
    "assisted_reproduction",
    "somatic_cell_nuclear_transfer",
    "gene_drive",
    "de_extinction",
    # -- and the governance ----------------------------------------------------
    "access_and_benefit_sharing",
    "prior_informed_consent",
    "digital_sequence_information",
    "wildlife_forensics",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "conservation_genomics_review",
    "florida_panther_genetic_rescue",
    "inbreeding_depression_captive_populations",
    "effective_population_size_estimation",
    "frozen_zoo_biobanking",
    "museum_specimen_genetic_baselines",
    "conservation_unit_misclassification",
    "gene_drive_governance_gap",
    "de_extinction_conservation_critique",
    "access_benefit_sharing_genomics",
)


# =============================================================================
#  RELATED
#  Six edges. Mostly outward, because that is where the methods and the
#  constraints actually come from.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- where every reproductive technology in this record was developed ------
    "green.animal_biotechnology",
    # -- the constraint the whole field operates under -------------------------
    "purple.access_benefit_sharing",
    # -- survey without capture, and the reference database dependency ---------
    "grey.environmental_biomonitoring",
    # -- the same sequencing and the same false negative problem ---------------
    "red.molecular_diagnostics",
    # -- genebank variation, and the parallel case of preserving options -------
    "green.molecular_plant_breeding",
    # -- the editing and drive constructs, and the governance gap they open ----
    "purple.synthetic_biology",
)
