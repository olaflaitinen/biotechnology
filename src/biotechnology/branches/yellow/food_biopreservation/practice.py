# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped BY THE TARGET ORGANISM rather than by food
#  category, because in this record the agent is chosen for what it kills and
#  the food is a matrix problem afterwards. A reader who learns that nisin acts
#  on Gram-positive organisms can predict most of where it appears.
#
#  The Listeria group is placed first and is the largest, which reflects the
#  field honestly: Listeria monocytogenes grows at refrigeration temperature,
#  contaminates ready-to-eat food after any kill step, and has a high case
#  fatality rate. It is the organism this record exists to address.
#
#  ORGANISMS include both the protective cultures and the TARGETS, which is
#  unusual for this facet and is correct here. A record about controlling
#  pathogens that listed only its friendly organisms would omit half the
#  subject.
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
#  By target organism. The first group is why the field exists.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- against Listeria, which is the point -----------------------------------
    "Nisin in ready-to-eat meats and in cheese to control Listeria "
    "monocytogenes, which grows at refrigeration temperature and contaminates "
    "food after cooking rather than before",
    "Protective cultures applied to the surface of sliced cold cuts, smoked "
    "fish and soft cheese, which are the products where post-process "
    "contamination is most consequential",
    "Listeria-specific bacteriophage preparations applied to ready-to-eat "
    "products and to food contact surfaces",
    "Bacteriocin-producing cultures in fermented sausage, where the "
    "antimicrobial is generated in place during the fermentation itself",
    # -- against Clostridium, where the alternative is nitrite --------------------
    "Nisin in processed cheese to control Clostridium spores, which is its "
    "oldest permitted use and dates from the 1950s",
    "Nisin and protective cultures in cured meat as part of nitrite reduction "
    "strategies, where the biological agent replaces part of a chemical "
    "preservative under public and regulatory pressure",
    "Control of late blowing in hard cheese caused by clostridial spores "
    "surviving pasteurisation",
    # -- against Gram-negative pathogens, where the tools are weaker ---------------
    "Bacteriophage preparations against Salmonella and Escherichia coli in "
    "produce, poultry and processing environments, which is one of the few "
    "biological options because bacteriocins largely do not act on "
    "Gram-negative organisms",
    "Lactoperoxidase system for raw milk preservation where refrigeration is "
    "unavailable, which is a specific and important application in regions "
    "without a reliable cold chain",
    # -- against spoilage, which is the commercial volume ---------------------------
    "Protective cultures against yeast and mould spoilage in fermented dairy, "
    "which extends shelf life without any change the consumer perceives",
    "Cultures and their metabolites against spoilage flora in fresh pasta, "
    "salads, dressings and bakery products",
    "Antifungal cultures in bread and baked goods as an alternative to "
    "propionate preservatives",
    # -- outside the food itself -----------------------------------------------------
    "Phage and bacteriocin treatment of food contact surfaces and processing "
    "environments, which addresses the reservoir rather than the product",
    "Biopreservation in packaging films and coatings, releasing the agent at "
    "the surface where contamination actually occurs",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the four agents, then by how they are actually deployed.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- the four agents --------------------------------------------------------
    "Protective culture selection for antimicrobial production without flavour "
    "or acid formation, since a culture that changes the food has failed even "
    "if it protects it",
    "Bacteriocin production and purification, chiefly nisin, supplied as a "
    "standardised preparation with a declared activity",
    "In situ bacteriocin production by a culture added to the food, which "
    "avoids the additive status that a purified preparation carries",
    "Bacteriophage cocktail formulation, using several phages against one "
    "species to delay the emergence of resistance",
    "Antimicrobial enzyme systems including lysozyme and the lactoperoxidase "
    "system",
    # ---- making them work in a real food ------------------------------------------
    "Hurdle combination design, in which the biological agent is one barrier "
    "among pH, water activity, salt, chilling and atmosphere, and which is the "
    "correct frame for everything in this record",
    "Matrix compatibility testing, since fat and protein bind antimicrobial "
    "peptides and a solid matrix restricts diffusion, so broth results predict "
    "food performance poorly",
    "Surface application by spraying, dipping or in packaging, targeting where "
    "post-process contamination actually lands rather than treating the bulk",
    "Encapsulation and controlled release, so that the agent is available over "
    "the shelf life rather than consumed in the first days",
    # ---- proving it works and keeps working ----------------------------------------
    "Challenge testing, in which the food is deliberately inoculated with the "
    "target pathogen and the barrier is shown to control it, which is the only "
    "acceptable evidence for a safety claim",
    "Predictive microbiology and shelf life modelling under the intended "
    "storage conditions and under reasonable abuse",
    "Resistance monitoring for bacteriocins and phages, which the field has "
    "been slower to institutionalise than it should have been",
    "Whole genome sequencing of protective cultures to exclude transferable "
    "antimicrobial resistance and toxin genes",
)


# =============================================================================
#  ORGANISMS
#  Both the protective cultures and the targets. See the module header.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "lactococcus_lactis",  # produces nisin, the oldest permitted bacteriocin
    "latilactobacillus_sakei",  # protective culture for meat, active when chilled
    "carnobacterium_maltaromaticum",  # protective culture for fish and cold cuts
    "listeria_monocytogenes",  # the target; grows cold, contaminates after cooking
    "clostridium_botulinum",  # the target nisin was first permitted against
    "salmonella_enterica",  # Gram-negative target, reached by phage rather than nisin
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "challenge_testing",
    "predictive_microbiology",
    "bioassay",
    "chromatography",
    "next_generation_sequencing",
    "shelf_life_testing",
    "ph_measurement",
    "sensory_analysis",
)


# =============================================================================
#  CHALLENGES
#  The narrowness of each agent first, since it is what makes hurdles
#  necessary.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- every agent is narrow ---------------------------------------------------
    "Narrow spectrum, since bacteriocins including nisin act on Gram-positive "
    "organisms and are excluded by the outer membrane of Gram-negative ones, "
    "leaving Salmonella and Escherichia coli largely untouched",
    "Species-specific action of bacteriophages, which is their principal "
    "advantage and means a single preparation cannot cover the several "
    "pathogens a food may carry",
    "Dependence on time and temperature for protective cultures, which do "
    "nothing quickly and are ineffective if the food is consumed before they "
    "have acted",
    # -- the food itself defeats laboratory results --------------------------------
    "Matrix effects, since fat and protein bind antimicrobial peptides and a "
    "solid food restricts diffusion, so a result in broth may overstate "
    "performance in a sausage by a wide margin",
    "Uneven distribution in a solid food, where contamination is a surface "
    "event and the agent must be where the organism lands",
    # -- the evolutionary problem the field understates ------------------------------
    "Resistance development to bacteriocins and to bacteriophages, which is the "
    "ordinary consequence of applying an antimicrobial and which this field has "
    "been slower to acknowledge than clinical microbiology was",
    "Cross-resistance considerations between food bacteriocins and clinically "
    "used antimicrobials, which is a live question rather than a settled one",
    # -- the regulatory picture --------------------------------------------------------
    "Divergent classification between jurisdictions and between agents, with "
    "nisin permitted as an additive for decades and phage preparations treated "
    "variously as processing aids, additives or outside the framework entirely",
    "Additive declaration requirements, which sit awkwardly with the clean "
    "label positioning that drives much of the commercial interest",
    # -- and the honest limit on what it can replace --------------------------------------
    "Misuse as a substitute for hygiene, refrigeration or a kill step, which is "
    "the failure mode a hurdle framing is meant to prevent and which the "
    "commercial framing of these agents as natural preservatives encourages",
    "Consumer perception of added bacteria and viruses in food, which is a "
    "communication problem for phage products in particular and has no "
    "technical answer",
)
