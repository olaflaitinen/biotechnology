# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The applications are grouped by WHO IS BEING PROTECTED, because that is the
#  distinction that decides who pays and therefore whether a product exists at
#  all. A vaccine that protects the farmer's own animals is a commercial
#  proposition. A vaccine that protects the human population from a zoonosis,
#  or that protects a neighbouring country's trade, is a public good, and the
#  economics are completely different.
#
#  The technologies group is unusual in this library for how much of it is
#  about DELIVERY rather than about immunology. Vaccinating fifty thousand
#  broilers is a logistics problem before it is a biological one, and the
#  in-ovo and drinking-water routes exist for that reason alone.
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
#  Grouped by who is protected, because that decides who pays.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- protecting the animals, and the farmer pays ---------------------------
    "Newcastle disease vaccination by drinking water and coarse spray, which is "
    "how tens of billions of birds are vaccinated each year",
    "Marek's disease vaccination in ovo at day eighteen of incubation, before "
    "the chick has hatched",
    "Clostridial and respiratory vaccination in cattle and sheep",
    "Fish vaccines delivered by immersion or by automated injection in salmon "
    "aquaculture, which largely eliminated antibiotic use in that industry",
    "Autogenous vaccines produced from an isolate taken on the affected farm, "
    "for pathogens too variable for a commercial product",
    # -- protecting the national herd and the trade position -------------------
    "Foot-and-mouth disease vaccination and strategic antigen banks held "
    "against an incursion",
    "Classical swine fever and porcine reproductive and respiratory syndrome "
    "control programmes",
    "Bluetongue vaccination campaigns following vector range expansion",
    # -- protecting people ------------------------------------------------------
    "Avian influenza vaccination in poultry, the front line against a virus "
    "with pandemic potential in humans",
    "Oral rabies vaccination of wild foxes and raccoon dogs by aerial bait "
    "distribution, which eliminated fox rabies from western Europe",
    "Brucellosis and anthrax vaccination in livestock, both of which are "
    "principally human disease control measures",
    "Rift Valley fever and Japanese encephalitis vaccination in animal "
    "reservoirs",
    # -- protecting the antibiotic supply ----------------------------------------
    "Vaccination programmes deployed explicitly to replace routine antibiotic "
    "medication in intensive pig and poultry production",
    # -- companion animals -------------------------------------------------------
    "Core companion animal vaccination against rabies, parvovirus and "
    "distemper",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the problem each solves. Note how much is delivery rather than
#  immunology.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- solving the trade problem -------------------------------------------
    "DIVA vaccine design by deletion of a non-essential antigen, paired with a "
    "companion serological test for antibodies against it",
    "Marker vaccines based on subunit antigens that provoke a narrower response "
    "than infection does",
    # ---- the platforms ---------------------------------------------------------
    "Live attenuated vaccines, attenuated by passage or by rational gene "
    "deletion",
    "Inactivated whole-organism vaccines in oil-adjuvanted emulsions, which are "
    "cheap and give long duration at the cost of injection-site reaction",
    "Herpesvirus of turkeys vectored constructs, which express antigens from "
    "other pathogens and can be given in ovo",
    "Recombinant subunit and virus-like particle vaccines",
    "Reverse vaccinology from pathogen genomes",
    # ---- delivering to thousands an hour ----------------------------------------
    "In-ovo injection at day eighteen, automated at tens of thousands of eggs "
    "per hour",
    "Drinking water and coarse spray mass administration",
    "Immersion vaccination for fish, and automated injection lines",
    "Oral bait formulation for wildlife, dropped from aircraft over defined "
    "grids",
    "Needle-free transdermal injectors, which also remove broken-needle risk in "
    "the food chain",
    # ---- keeping it usable in the field -------------------------------------------
    "Thermostable and freeze-dried formulation for distribution without a cold "
    "chain",
    "Multivalent combination products, since each additional handling of an "
    "animal costs more than the vaccine",
    # ---- knowing whether it worked -------------------------------------------------
    "Herd-level pooled PCR and serological surveillance",
    "Sequence-based strain matching to select the vaccine antigen against "
    "circulating field strains",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "gallus_gallus",  # poultry, the largest vaccinated population on earth
    "bos_taurus",  # cattle, foot-and-mouth and brucellosis
    "sus_scrofa",  # pigs, classical swine fever and PRRS
    "ovis_aries",  # sheep, clostridial disease and bluetongue
    "salmo_salar",  # salmon, where vaccination displaced antibiotics entirely
    "escherichia_coli",  # antigen expression and a target pathogen in its own right
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "elisa",
    "pcr",
    "next_generation_sequencing",
    "chromatography",
    "fermentation",
    "bioassay",
    "field_trial",
)


# =============================================================================
#  CHALLENGES
#  Two biological, then six that are economic, regulatory or structural. The
#  third is the one that most often prevents vaccination being used at all.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- biological -------------------------------------------------------------
    "Antigenic variability in foot-and-mouth disease and avian influenza, which "
    "requires strain matching and antigen banks rather than a single product",
    "Wildlife reservoirs that no livestock vaccination programme can reach, so "
    "control succeeds in the farmed population and the pathogen persists",
    # -- the trade rule that discourages the intervention ------------------------
    "Trade rules that remove disease-free status from a vaccinating country, so "
    "healthy animals are culled rather than vaccinated. DIVA vaccines exist to "
    "solve exactly this, and adoption still lags the technology",
    # -- economics ----------------------------------------------------------------
    "Extreme price sensitivity, with a development and licensing cost that must "
    "be recovered at a few cents per dose",
    "A benefit that is largely a public good captured by people who did not pay "
    "for it, which leaves the field structurally underfunded relative to what "
    "it prevents",
    # -- logistics ------------------------------------------------------------------
    "Cold chain and delivery to extensive and smallholder systems, which fail "
    "first in exactly the regions with the highest disease burden",
    # -- regulation --------------------------------------------------------------------
    "Fragmented national approval, so a product licensed in one country must be "
    "re-registered in the next, at a cost the market frequently cannot repay",
    # -- surveillance ---------------------------------------------------------------------
    "Weak surveillance in many of the places where zoonotic spillover is most "
    "likely, so an outbreak is often detected in people before it is detected "
    "in animals",
)
