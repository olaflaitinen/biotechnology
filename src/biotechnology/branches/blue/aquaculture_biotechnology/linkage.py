# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  `green.animal_biotechnology` and `green.veterinary_vaccines` are the two
#  edges that matter most, and both are comparisons rather than references.
#
#  Against `green.animal_biotechnology`: the same discipline, applied to
#  animals domesticated fifty years ago rather than ten thousand. That single
#  difference explains the gains recorded in this record's `metrics.py`, since
#  a population close to wild has variation still available that a long-selected
#  one does not. It also explains the risk: these populations were founded from
#  small numbers of individuals and their effective population size is
#  correspondingly small.
#
#  Against `green.veterinary_vaccines`: the salmon vaccination result is the
#  strongest single piece of evidence for that record's central argument, that
#  vaccination is an antimicrobial resistance intervention. Antibiotic use fell
#  to a very small fraction of former levels while production grew. And the sea
#  lice story is the same argument in reverse, since no comparable vaccine
#  exists and thirty years of chemistry produced resistance instead.
#
#  `blue.seaweed_cultivation` and `blue.algal_biotechnology` are both suppliers
#  and both mitigations. Algae supply the omega-3 oils and the pigment that
#  reduce this record's draw on wild fish; seaweed grown beside fed fish takes
#  up the dissolved nutrients this record discharges.
#
#  `grey.environmental_biomonitoring` carries the surveillance that decides
#  whether a farm is meeting its conditions, which for an open system is not a
#  formality.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and Goal 14 is claimed with a qualification that has to be explicit.
#
#  Life below water is the goal this sector most wants to claim and the one it
#  can least claim simply. Farming does relieve pressure on wild stocks, and
#  the feed reformulation recorded in `metrics.py` has reduced the draw on wild
#  fish by a large factor. Against that, farms transmit parasites to wild
#  populations, escapees dilute local adaptation, and effluent alters the
#  seabed beneath them.
#
#  The claim is therefore made on the specific mechanism of substitution for
#  capture and on reduced feed dependence, and NOT as a general environmental
#  benefit. A sceptical auditor should read it alongside this record's
#  `CHALLENGES`, which is where the other side is recorded at equal length.
#
#  Goal 3 is claimed on antimicrobial stewardship, the same basis
#  `green.veterinary_vaccines` uses, and Goal 12 on feed conversion, which is
#  genuinely favourable against terrestrial livestock even after the
#  qualifications in `metrics.py`.
# =============================================================================
SDGS: Tuple[int, ...] = (
    2,  # Zero hunger, on protein supply and on coastal livelihoods
    3,  # Good health, on antibiotic use avoided through vaccination
    12,  # Responsible production, on feed conversion efficiency
    14,  # Life below water, on substitution for capture, with qualification
)


# =============================================================================
#  GLOSSARY
#  Grouped: the sector, the genetics, the health problem, and what leaves the
#  farm.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the sector ------------------------------------------------------------
    "aquaculture",
    "mariculture",
    "net_pen",
    "recirculating_aquaculture_system",
    "integrated_multi_trophic_aquaculture",
    "broodstock",
    "hatchery",
    "smolt",
    # -- the genetics ----------------------------------------------------------
    "selective_breeding",
    "genomic_selection",
    "heritability",
    "breeding_value",
    "effective_population_size",
    "triploidy",
    "monosex_population",
    "domestication",
    # -- keeping them alive ------------------------------------------------------
    "sea_lice",
    "cleaner_fish",
    "fallowing",
    "biosecurity",
    "vaccination",
    "withdrawal_period",
    "antimicrobial_resistance",
    # -- feed and what leaves the farm -------------------------------------------
    "feed_conversion_ratio",
    "fishmeal",
    "fish_oil",
    "fish_in_fish_out",
    "escapement",
    "introgression",
    "eutrophication",
    "stocking_density",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "fao_aquaculture_report",
    "salmon_breeding_programme_history",
    "salmon_vaccination_antibiotic_reduction",
    "sea_lice_resistance_review",
    "fish_in_fish_out_methodology_debate",
    "farmed_wild_salmon_introgression",
    "oyster_herpesvirus_resistance_breeding",
    "genomic_selection_aquaculture_review",
    "fish_welfare_evidence_review",
    "recirculating_aquaculture_assessment",
)


# =============================================================================
#  RELATED
#  Seven edges. The first two are comparisons that explain this record.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the same discipline on animals domesticated ten thousand years earlier -
    "green.animal_biotechnology",
    # -- where the vaccination argument is made in full ------------------------
    "green.veterinary_vaccines",
    # -- supplies the oils and pigment that reduce the draw on wild fish -------
    "blue.algal_biotechnology",
    # -- grown beside the pens, taking up their dissolved waste ----------------
    "blue.seaweed_cultivation",
    # -- the pathogen detection this record depends on -------------------------
    "red.molecular_diagnostics",
    # -- monitoring whether an open system meets its conditions ----------------
    "grey.environmental_biomonitoring",
    # -- what may be done to an animal that can suffer -------------------------
    "purple.bioethics",
)
