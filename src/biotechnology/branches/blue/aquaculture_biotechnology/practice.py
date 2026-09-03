# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS are grouped by the four areas of the field, in the order a fish
#  passes through them: it is bred, it is fed, it is kept healthy, and it is
#  contained. The last group exists because containment is a biotechnology
#  question here rather than only an engineering one, since sterility and sex
#  control are used specifically to limit what an escape can do.
#
#  ORGANISMS are farmed species, and the note on each gives why it is farmed
#  rather than what it is, because the reasons differ sharply: some are farmed
#  because they convert feed efficiently, one because it does not need fishmeal
#  at all, and one because it is worth a great deal per kilogram.
#
#  A NOTE ON WHERE THE TONNAGE ACTUALLY IS. Salmon dominates the literature and
#  most of this record's documented successes, and it is a small fraction of
#  world aquaculture by weight. Carp, tilapia and molluscs are far larger and
#  far less written about. The applications list names both, and a reader
#  should not mistake the visibility of salmon for its share.
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
#  Grouped by the four areas, in the order a farmed animal passes through them.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- breeding it -----------------------------------------------------------
    "Family-based selective breeding programmes for growth rate, feed "
    "conversion and flesh quality, which have delivered gains per generation "
    "well above those achieved in terrestrial livestock",
    "Genomic selection for disease resistance, particularly against viral "
    "diseases for which no effective vaccine exists",
    "Marker-assisted selection for resistance traits with large effects, which "
    "are more common in these species than in mammals",
    "Breeding programmes for shellfish, including oyster stocks selected for "
    "resistance to the herpesvirus that has caused mass mortality",
    "Broodstock management to maintain genetic diversity in populations founded "
    "from small numbers of wild individuals",
    # -- feeding it -------------------------------------------------------------
    "Reformulation of feed away from fishmeal and fish oil towards plant "
    "proteins, which reduced the wild fish requirement per kilogram of salmon "
    "by a large factor",
    "Algal oils supplying long-chain omega-3 fatty acids directly, which is the "
    "clearest route to removing the remaining marine oil requirement and links "
    "this record to `blue.algal_biotechnology`",
    "Insect meal and single cell protein as feed ingredients",
    "Use of processing trimmings and by-products rather than whole wild fish, "
    "which now supplies much of the remaining marine content",
    "Functional feeds and feed additives intended to support health and reduce "
    "the need for treatment",
    "Live microalgal and rotifer feeds for hatchery stages, which no substitute "
    "has replaced",
    # -- keeping it healthy ------------------------------------------------------
    "Vaccination against bacterial and viral disease, including the oil-adjuvant "
    "injectable vaccines that reduced salmon antibiotic use to a very small "
    "fraction of former levels",
    "Sea lice management by cleaner fish, thermal and mechanical delousing, and "
    "chemical treatment, all of which have limitations recorded in "
    "`CHALLENGES`",
    "Molecular diagnostics and environmental DNA surveillance for pathogens in "
    "and around farms",
    "Biosecurity zoning, fallowing and synchronised production cycles across "
    "farms in a region, which is disease control at a scale no single operator "
    "can achieve alone",
    "Probiotics and microbiome management, particularly in shrimp and hatchery "
    "systems",
    # -- containing it -----------------------------------------------------------
    "Induced triploidy producing sterile fish, which limits the genetic "
    "consequences of escape at some cost to performance and welfare",
    "Monosex population production, used to manage growth uniformity and "
    "unwanted reproduction",
    "Recirculating aquaculture systems, which close the system at substantial "
    "capital and energy cost",
    "Offshore and submersible pen systems, which disperse impact rather than "
    "containing it",
    "Integrated multi-trophic systems pairing fed fish with seaweed and "
    "shellfish that take up dissolved and particulate waste",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the same four areas, then the tools shared across them.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- genetics ---------------------------------------------------------------
    "Genomic selection using single nucleotide polymorphism arrays and "
    "sequence-based genotyping, applied faster in these species than in most "
    "livestock because family sizes are enormous",
    "Pedigree management and genetic marker verification, necessary because "
    "families cannot be kept physically separate for long in water",
    "Genome assembly and reference resources for farmed species, which arrived "
    "only recently for several of them",
    "Genome editing for disease resistance and sterility, demonstrated in "
    "several species and constrained almost entirely by regulation rather than "
    "by technique",
    # ---- reproduction ------------------------------------------------------------
    "Induced spawning by hormonal and photoperiod manipulation, which decouples "
    "production from the natural season",
    "Cryopreservation of milt, which allows breeding programmes to store and "
    "move male genetics",
    "Triploidy induction by pressure or thermal shock",
    "Sex control by hormonal, thermal or genetic means",
    # ---- health ------------------------------------------------------------------
    "Injectable oil-adjuvanted vaccines, and immersion and oral vaccines for "
    "smaller fish, on the terms `green.veterinary_vaccines` sets out",
    "DNA and RNA vaccines, authorised in some jurisdictions for fish before "
    "comparable human products existed",
    "Quantitative PCR and portable sequencing for pathogen detection on site",
    "Cleaner fish production, which is itself an aquaculture operation with its "
    "own welfare and disease problems",
    # ---- nutrition ---------------------------------------------------------------
    "Feed formulation and extrusion technology, which determines digestibility "
    "and how much of the feed reaches the water uneaten",
    "Digestibility and nutrient requirement determination for novel ingredients",
    # ---- the environment around the farm ------------------------------------------
    "Benthic monitoring beneath pens, and modelling of waste dispersal",
    "Environmental DNA and sentinel monitoring of parasites and pathogens in "
    "surrounding waters",
    "Traceability and genetic assignment of escapees to farms of origin, which "
    "is what makes escape enforceable rather than merely regrettable",
)


# =============================================================================
#  ORGANISMS
#  Farmed species, with why each is farmed rather than what it is.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "salmo_salar",  # high value, intensively bred, and where most research sits
    "oreochromis_niloticus",  # tilapia; robust, herbivorous, farmed everywhere warm
    "cyprinus_carpio",  # carp; the largest freshwater tonnage, low input, low profile
    "penaeus_vannamei",  # shrimp; high value, disease-prone, drove mangrove loss
    "crassostrea_gigas",  # oyster; needs no feed at all, filters its own
    "lepeophtheirus_salmonis",  # the sea louse, this record's principal antagonist
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "selective_breeding",
    "genomic_selection",
    "vaccination",
    "pcr",
    "cryopreservation",
    "next_generation_sequencing",
    "environmental_monitoring",
    "feed_formulation",
)


# =============================================================================
#  CHALLENGES
#  The first four all follow from the system being open to the sea.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- everything that follows from an open system ---------------------------
    "Sea lice transmission between farmed and wild populations, which is the "
    "single most contested impact of salmon farming and which no operator can "
    "solve alone because the parasite moves between farms",
    "Resistance in sea lice to successive chemical treatments, which has "
    "repeatedly removed a control option and driven the move to thermal, "
    "mechanical and biological methods that carry their own welfare costs",
    "Escape of farmed fish and interbreeding with wild populations, diluting "
    "local adaptation accumulated over many generations and irreversible once "
    "it has happened",
    "Pathogen exchange in both directions between farms and wild stocks, and "
    "between neighbouring farms in the same water body",
    # -- what the farm puts into the water --------------------------------------
    "Nutrient and organic waste loading beneath and around pens, which alters "
    "the seabed community and limits how densely an area can be farmed",
    "Release of treatment chemicals and antifoulants into the surrounding "
    "water",
    # -- what the farm takes out of it --------------------------------------------
    "Continued dependence on wild fish for feed, much reduced and not "
    "eliminated, with the substitutes carrying land, water and fertiliser costs "
    "of their own",
    # -- what can destroy a year's production ------------------------------------
    "Disease outbreaks capable of removing a substantial share of national "
    "production in a single year, as shrimp and oyster industries have both "
    "experienced",
    "Absence of effective vaccines for several important viral diseases, which "
    "leaves breeding for resistance as the only durable answer",
    "Marine heatwaves, harmful algal blooms and jellyfish incursions, which "
    "kill stock in enclosures that cannot be moved",
    # -- the animal itself ---------------------------------------------------------
    "Welfare in a species group whose sentience is now much better evidenced "
    "than the regulation covering it, with stocking density, handling, "
    "delousing procedures and slaughter method all unresolved",
    "Welfare of cleaner fish, which are farmed animals used as a treatment and "
    "which have historically suffered high mortality in that role",
    # -- structural ------------------------------------------------------------------
    "Habitat conversion, particularly the mangrove clearance for shrimp ponds "
    "that removed coastal protection as well as habitat",
    "Regulatory divergence on genome editing, which is what prevents "
    "demonstrated disease-resistance traits from reaching production rather "
    "than any technical obstacle",
)
