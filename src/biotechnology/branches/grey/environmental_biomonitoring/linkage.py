# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD IS LINKED TO BY MORE OF THE BRANCH THAN IT LINKS TO, WHICH IS
#  CORRECT FOR AN INSTRUMENT.
#
#  Every other grey record needs this one to demonstrate that it worked:
#  bioremediation needs isotope and functional gene evidence, bioaugmentation
#  needs strain tracking, wastewater treatment needs receiving water
#  assessment, biomining needs drainage monitoring. The edges below are chosen
#  to represent that relationship rather than to reciprocate every inbound
#  link, since listing all of them would be a directory rather than a set of
#  edges.
#
#  `grey.biodiversity_conservation` IS FIRST, and it is the strongest edge in
#  the record. That is where environmental DNA has changed practice most, and
#  the dependency runs both ways: conservation decisions rest on survey data,
#  and survey methods rest on the taxonomy that conservation science maintains.
#
#  `red.molecular_diagnostics` IS THE METHODS EDGE AND IT IS A REAL ONE, NOT AN
#  ANALOGY. The same sequencing, the same quantitative PCR, the same detection
#  limit and false negative problems, applied to a river rather than a patient.
#  Wastewater surveillance makes the two records touch directly: it is a
#  diagnostic assay run on a population through its sewer.
#
#  `blue.marine_genomics` IS DELIBERATELY NOT LINKED. Both records sequence
#  environmental samples, and that record is about discovering biology while
#  this one is about assessing condition. Shared instrumentation is not a
#  shared question, and rule 13 does not accept it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Four, and this record's claims rest on a different footing from the rest of
#  the branch: it does not improve anything, it establishes whether anything
#  improved. That is a genuine contribution and it has to be claimed carefully.
#
#  Goal 6 is claimed on target 6.3 concerning water quality, since ecological
#  status classification is the mechanism by which water quality is defined,
#  measured and enforced in law.
#
#  Goal 14 and goal 15 are claimed on the same basis for marine and terrestrial
#  systems: species and habitat condition reporting is what makes a
#  conservation obligation checkable rather than aspirational.
#
#  Goal 3 is claimed on wastewater surveillance, which gives population-level
#  disease signal ahead of clinical reporting and which is a public health
#  instrument in the plainest sense.
#
#  GOAL 12 IS DELIBERATELY NOT CLAIMED. A sceptical auditor under rule 12 would
#  ask what material flow this record changes, and the honest answer is none.
#  Measuring a system does not make its production more responsible, and every
#  neighbouring record that does claim the goal has a material flow to point
#  at.
#
#  GOAL 13 IS NOT CLAIMED EITHER, although monitoring underpins climate
#  reporting. That would be a claim on the use somebody else makes of the data,
#  which is exactly the kind of second-hand attribution rule 12 exists to
#  catch.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on population-scale wastewater surveillance
    6,  # Water, on ecological status as the legal definition of water quality
    14,  # Oceans, on marine condition assessment and reporting
    15,  # Land, on species and habitat condition reporting
)


# =============================================================================
#  GLOSSARY
#  Grouped: the approaches, the molecular methods, the interpretation
#  vocabulary, and the words for what goes wrong.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the approaches --------------------------------------------------------
    "biomonitoring",
    "bioindicator",
    "biotic_index",
    "saprobic_system",
    "ecological_status",
    "bioaccumulation",
    "sentinel_organism",
    "biomarker",
    "biosensor",
    "whole_effluent_toxicity",
    # -- reading traces --------------------------------------------------------
    "environmental_dna",
    "metabarcoding",
    "reference_database",
    "primer_bias",
    "sequence_read_count",
    "functional_gene_marker",
    "compound_specific_isotope_analysis",
    # -- turning readings into judgements --------------------------------------
    "reference_condition",
    "ecological_quality_ratio",
    "detection_probability",
    "occupancy_model",
    "sampling_effort",
    "intercalibration",
    "time_series",
    # -- and what goes wrong ---------------------------------------------------
    "shifting_baseline",
    "false_negative",
    "cross_contamination",
    "confounding",
    "taxonomic_expertise",
    "wastewater_epidemiology",
    "sewershed",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "environmental_dna_review",
    "saprobic_system_origin",
    "biotic_index_regulatory_assessment",
    "shifting_baseline_syndrome",
    "metabarcoding_community_assessment",
    "edna_detection_probability",
    "reference_database_coverage_gaps",
    "wastewater_based_epidemiology",
    "mussel_watch_time_series",
    "taxonomic_expertise_decline",
)


# =============================================================================
#  RELATED
#  Six edges. Conservation first, since that is where the methods changed
#  practice most, then the records that depend on this one for their evidence.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- where environmental DNA changed practice most, in both directions -----
    "grey.biodiversity_conservation",
    # -- the same assays on a river instead of a patient, and the sewer edge ---
    "red.molecular_diagnostics",
    # -- monitored natural attenuation is only defensible on evidence from here
    "grey.bioremediation",
    # -- strain tracking is how that record's evidence was generated -----------
    "grey.bioaugmentation",
    # -- receiving water assessment, and the sewer as a population instrument --
    "grey.wastewater_treatment",
    # -- drainage and closure monitoring over a multi-century liability --------
    "grey.biomining",
)
