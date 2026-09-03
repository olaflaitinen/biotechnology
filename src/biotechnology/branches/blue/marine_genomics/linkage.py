# =============================================================================
#  biotechnology.branches.blue.marine_genomics.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record sits upstream of most of its own branch, and the edges are best
#  read as a supply relationship rather than as a reading list.
#
#  `blue.marine_natural_products` and `blue.marine_enzymes` both search a space
#  that this record defines. You cannot look for a cold-adapted enzyme in
#  organisms nobody knows exist, and the biosynthetic gene cluster counts in
#  this record's `metrics.py` are the bridge: a predicted cluster is a
#  hypothesis about chemistry that the natural products record then has to
#  test. The two downstream records inherit this one's coverage bias as well as
#  its catalogues, which is worth a reviewer's attention.
#
#  `gold.genomics_data_analysis` holds the methods. The distinction is that
#  this record is about what is specific to marine material: low biomass, poor
#  reference databases, pervasive symbiosis, and samples that cost more to
#  collect than to sequence. The assembly and binning algorithms themselves are
#  not marine and belong there.
#
#  `purple.access_benefit_sharing` is not a governance footnote here. It is the
#  branch's defining legal problem, and this record is where it bites hardest,
#  because a sequence can be published and downloaded anywhere while a physical
#  sample can be tracked.
#
#  `grey.environmental_biomonitoring` is where environmental DNA becomes a
#  regulatory instrument rather than a research method, which is a different
#  activity with different evidential requirements.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and the omission is deliberate.
#
#  Goal 14 is the primary claim and the strongest: this record supplies the
#  baseline against which marine change is measured, and environmental DNA has
#  become a working monitoring tool rather than a proposal.
#
#  GOAL 3 IS DELIBERATELY NOT CLAIMED, although the catalogues this field
#  produces are the search space for marine medicines. The benefit is real and
#  it is indirect: this record makes a search possible and does not itself
#  produce a treatment. `blue.marine_natural_products` claims Goal 3 for the
#  medicines, and claiming it here as well would count the same contribution
#  twice, which is exactly what rule 12 exists to prevent.
# =============================================================================
SDGS: Tuple[int, ...] = (
    9,  # Industry and innovation, on the research infrastructure itself
    14,  # Life below water, the primary and best-supported claim
    17,  # Partnerships, on shared expeditions, open data and capacity building
)


# =============================================================================
#  GLOSSARY
#  Grouped: what makes marine sequencing distinct, the methods, what comes out,
#  and the legal vocabulary the field cannot avoid.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the problem this record solves ----------------------------------------
    "unculturable_majority",
    "great_plate_count_anomaly",
    "microbial_dark_matter",
    "rare_biosphere",
    # -- the methods -----------------------------------------------------------
    "metagenomics",
    "metatranscriptomics",
    "single_cell_genomics",
    "environmental_dna",
    "amplicon_sequencing",
    "shotgun_sequencing",
    "long_read_sequencing",
    # -- what comes out --------------------------------------------------------
    "metagenome_assembled_genome",
    "binning",
    "assembly_contiguity",
    "genome_completeness",
    "biosynthetic_gene_cluster",
    "reference_database",
    "dna_barcode",
    "operational_taxonomic_unit",
    # -- the habitats that make it worth doing ---------------------------------
    "hydrothermal_vent",
    "symbiosis",
    "holobiont",
    "psychrophile",
    "piezophile",
    # -- the law it cannot avoid -----------------------------------------------
    "digital_sequence_information",
    "access_and_benefit_sharing",
    "areas_beyond_national_jurisdiction",
    "prior_informed_consent",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "great_plate_count_anomaly",
    "uncultured_marine_archaea_discovery",
    "prochlorococcus_description",
    "sargasso_sea_metagenome",
    "tara_oceans_survey",
    "environmental_dna_review",
    "marine_microbial_dark_matter_review",
    "bbnj_agreement",
    "nagoya_protocol",
    "genomic_standards_consortium_mixs",
)


# =============================================================================
#  RELATED
#  Six edges. The first two are the records this one supplies.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- what the catalogues are searched for ----------------------------------
    "blue.marine_natural_products",
    "blue.marine_enzymes",
    # -- the methods, which are not themselves marine --------------------------
    "gold.genomics_data_analysis",
    # -- where eDNA becomes a regulatory instrument ----------------------------
    "grey.environmental_biomonitoring",
    # -- the populations and habitats being measured ---------------------------
    "grey.biodiversity_conservation",
    # -- who owns a sequence taken from water belonging to no country ----------
    "purple.access_benefit_sharing",
)
