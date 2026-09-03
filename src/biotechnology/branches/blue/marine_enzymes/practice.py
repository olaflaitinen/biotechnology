# =============================================================================
#  biotechnology.branches.blue.marine_enzymes.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by WHICH MARINE ADAPTATION IS BEING BOUGHT, because
#  that is the only grouping that justifies this record existing separately
#  from `white.industrial_enzymes`. An application that buys none of these
#  adaptations is an industrial enzyme application that happens to have a
#  marine source, and belongs in the other record.
#
#  The largest group is heat-lability, which is the property the narrative
#  argues is the real product. The second largest is thermostability, which is
#  its exact opposite and comes from vent organisms rather than from cold
#  water. That a single record contains both extremes is a consequence of the
#  ocean containing both, and it is worth a reader noticing.
#
#  ORGANISMS are source organisms. Most cannot be cultured, so in practice the
#  gene is expressed in a conventional host, which is why this record has
#  products where `blue.marine_natural_products` has a supply problem.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  Grouped by which marine adaptation the application actually buys.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- buying HEAT-LABILITY: the enzyme is destroyed on demand ----------------
    "Cold-active alkaline phosphatase for dephosphorylating DNA, inactivated by "
    "gentle warming rather than by an inhibitor that would then have to be "
    "removed, which deletes a step from thousands of cloning protocols",
    "Heat-labile nucleases and uracil DNA glycosylase used to prevent carryover "
    "contamination and then destroyed before amplification begins",
    "Cold-active proteases and lipases in food processing, allowing enzymatic "
    "treatment at refrigeration temperature and termination by mild heating "
    "without cooking the product",
    "Enzymatic tenderising and flavour development in fish and seafood "
    "processing at chill temperature",
    # -- buying LOW-TEMPERATURE ACTIVITY: the reaction runs where warmth is absent
    "Cold-active enzymes in laundry detergent, contributing to the low "
    "temperature washing that `white.industrial_enzymes` records as its largest "
    "environmental claim",
    "Cold-adapted amylases and cellulases in textile processing where heating "
    "the bath is the dominant energy cost",
    "Enzymatic treatment in refrigerated dairy processing, including lactose "
    "hydrolysis carried out during cold storage rather than as a separate "
    "heated step",
    "Bioremediation in polar and deep-sea conditions, where mesophilic "
    "organisms and their enzymes are inactive",
    # -- buying THERMOSTABILITY: from vents, the opposite extreme -----------------
    "High-fidelity DNA polymerase from a deep-sea hyperthermophile, which made "
    "accurate amplification of long sequences practical and is among the most "
    "widely used reagents in biology",
    "Thermostable ligases and other vent-derived enzymes used in molecular "
    "biology where a reaction must survive repeated heating",
    # -- buying SALT AND SOLVENT TOLERANCE ---------------------------------------
    "Halophilic enzymes for reactions in high ionic strength or in the presence "
    "of organic solvent, which precipitate ordinary proteins",
    "Processing of salted and fermented foods where the substrate itself is a "
    "brine",
    # -- buying MARINE SUBSTRATE SPECIFICITY --------------------------------------
    "Agarases, carrageenases and alginate lyases that degrade seaweed "
    "polysaccharides no terrestrial enzyme addresses, which is the enzymatic "
    "basis of `blue.seaweed_cultivation` processing",
    "Chitinases and chitin deacetylases converting shellfish processing waste "
    "into the materials in `blue.marine_biomaterials`",
    "Enzymes producing defined oligosaccharides from marine polysaccharides for "
    "food and cosmetic use",
    # -- buying an unusual reaction ------------------------------------------------
    "Marine haloperoxidases, which incorporate bromine and chlorine and are the "
    "enzymatic reason marine natural products are so frequently halogenated",
    "Ice-binding and antifreeze proteins used to control ice crystal formation "
    "in frozen food and in cryopreservation",
)


# =============================================================================
#  TECHNOLOGIES
#  Discovery, then the two problems that stand between a sequence and a
#  product.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- finding candidates ----------------------------------------------------
    "Sequence-based mining of marine metagenomes for enzyme families, which "
    "supplies candidates from organisms nobody has grown",
    "Functional metagenomic screening of expression libraries built from "
    "environmental DNA, which finds activity without needing to recognise the "
    "sequence",
    "Culture of the minority of marine organisms that will grow, still the "
    "route to the best-characterised enzymes",
    "Targeted sampling of habitats that impose the wanted constraint, which is "
    "the oldest heuristic in enzymology and works: look for a cold enzyme where "
    "it is cold",
    # ---- getting the protein to exist at all ------------------------------------
    "Heterologous expression in conventional hosts, which is what removes this "
    "record's supply problem and introduces its folding problem",
    "Low-temperature expression and cold-adapted expression hosts, used because "
    "a protein evolved at four degrees frequently aggregates when made at "
    "thirty-seven",
    "Chaperone co-expression and refolding from inclusion bodies",
    "Codon optimisation for the expression host, since the source organism's "
    "codon usage may be strongly biased",
    # ---- making it usable -------------------------------------------------------
    "Directed evolution and rational design to raise stability without losing "
    "the low-temperature activity that motivated the enzyme, which is the "
    "central engineering tension of this record",
    "Immobilisation, which extends operational lifetime and partially "
    "compensates for inherent instability",
    "Formulation and stabiliser selection for enzymes that are unstable by "
    "design",
    # ---- characterising what was found -------------------------------------------
    "Determination of activity and stability profiles across temperature, which "
    "is the measurement that decides whether an enzyme is genuinely "
    "cold-adapted or merely from a cold place",
    "Structural determination to identify the flexibility features that "
    "underlie cold adaptation",
    "High-pressure assay equipment for piezophilic enzymes, which few "
    "laboratories have and which is why that area remains small",
)


# =============================================================================
#  ORGANISMS
#  Source organisms. Most are not the production host.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "pyrococcus_furiosus",  # vent hyperthermophile, the high-fidelity polymerase
    "colwellia_psychrerythraea",  # psychrophile, a reference cold-adapted genome
    "pseudoalteromonas_haloplanktis",  # cold-adapted, and unusually culturable
    "photobacterium_profundum",  # piezophile, deep-sea pressure adaptation
    "halobacterium_salinarum",  # extreme halophile, salt-tolerant enzymes
    "escherichia_coli",  # the expression host for nearly all of the above
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "protein_expression",
    "metagenomics",
    "chromatography",
    "directed_evolution",
    "x_ray_crystallography",
    "differential_scanning_calorimetry",
    "enzyme_assay",
    "high_throughput_screening",
)


# =============================================================================
#  CHALLENGES
#  The first is the engineering tension that defines the field.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the tension at the centre of the record --------------------------------
    "Improving stability without losing the low-temperature activity that made "
    "the enzyme worth having, since the two properties arise from the same "
    "structural flexibility and engineering one degrades the other",
    "Short operational lifetime, which raises the cost per unit of product "
    "exactly as `white.industrial_enzymes` records for total turnover number, "
    "and which is inherent rather than a defect to be fixed",
    # -- getting the protein at all -----------------------------------------------
    "Insoluble expression, since a protein evolved at four degrees and high "
    "pressure frequently aggregates when produced in a mesophilic host at "
    "thirty-seven",
    "Uncultivability of most source organisms, which moves discovery to "
    "sequence and expression rather than to isolation from the native producer",
    "Candidate sequences accumulating faster than they can be expressed and "
    "characterised, so the bottleneck has moved from finding to testing",
    # -- getting the material -------------------------------------------------------
    "Sampling cost for deep-sea and polar habitats, which limits discovery to "
    "the places a vessel can reach",
    "Absence of high-pressure assay equipment in most laboratories, which is "
    "why piezophilic enzymology remains a small field regardless of its "
    "scientific interest",
    # -- the market ------------------------------------------------------------------
    "Competition from engineered terrestrial enzymes, since a well-understood "
    "mesophilic enzyme evolved in the laboratory towards cold activity may "
    "reach the market faster than a marine one taken from discovery",
    "Narrow application windows, because an enzyme that is destroyed above "
    "forty degrees is excluded from every process that involves heat",
    # -- the law ----------------------------------------------------------------------
    "Access and benefit sharing obligations attaching to the sequence, which "
    "matter more here than in most enzyme work because the product IS the "
    "sequence rather than a physical sample",
    "Uncertain status of sequences obtained from beyond national jurisdiction "
    "before 2023",
)
