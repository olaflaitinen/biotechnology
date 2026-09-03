# =============================================================================
#  biotechnology.branches.grey.bioaugmentation.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY HOW WELL THE EVIDENCE SUPPORTS THEM, WHICH IS
#  NOT HOW THIS FACET IS ORGANISED ANYWHERE ELSE IN THE LIBRARY.
#
#      GROUP 1  works, and the mechanism explains why
#      GROUP 2  plausible in a defined niche, evidence thinner
#      GROUP 3  sold widely, controlled comparisons do not support it
#
#  Rule 6 forbids listing aspirations as applications. In a normal record that
#  means omitting the unproven ones. Here it would mean omitting most of the
#  commercial market, which would leave a reader unable to recognise the
#  products they are actually being sold. So the weak group is INCLUDED and
#  LABELLED, which serves the reader better than silence would.
#
#  THE ORGANISING PRINCIPLE ACROSS ALL THREE GROUPS IS THE SAME QUESTION:
#  WAS THERE AN INCUMBENT COMMUNITY? Group 1 entries either face no incumbent
#  or supply a capability the incumbent genuinely lacks. Group 3 entries add
#  organisms to a functioning community that is already doing the job.
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
#  By strength of evidence, strongest first, with the weak group labelled.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- GROUP 1: works, and the mechanism explains why ------------------------
    "Dechlorinating consortium addition to aquifers contaminated with "
    "trichloroethene and tetrachloroethene, which is the field's clean success "
    "because many sites genuinely lack the organisms that complete the "
    "reaction and stall at a more toxic intermediate without them",
    "Seeding new anaerobic digesters with inoculum from an operating one, "
    "which works because there is no incumbent community to compete with and "
    "which is standard practice rather than an enhancement",
    "Recovery of a wastewater plant whose biomass has been killed by a toxic "
    "or hydraulic shock, where reseeding restores treatment in days rather "
    "than the weeks a community takes to regrow",
    "Nitrifier addition to activated sludge during cold-weather startup and "
    "after washout, targeted at the slowest-growing group in the plant and "
    "used as a bridge rather than as a permanent measure",
    "Inoculation of engineered bioreactors and biofilters at commissioning, "
    "where the vessel is sterile at the start and the operator chooses what "
    "colonises it",
    # ---- GROUP 2: defensible in a defined niche, evidence thinner ---------------
    "Addition of specialised degraders for compounds that are genuinely rare "
    "in the environment, such as certain pesticides and energetic compounds, "
    "where the argument that the capability is absent is at least plausible",
    "Carrier-immobilised or encapsulated cultures, which protect the "
    "introduced organisms from predation and desiccation and which improve "
    "survival measurably without yet demonstrating a matching improvement in "
    "treatment outcome",
    "Repeated dosing to sustain a population that will not establish, which is "
    "an honest admission that the organisms are being consumed rather than "
    "colonising and which is economic only where the treatment window is "
    "short",
    "Consortium rather than single-strain addition, on the reasoning that a "
    "community brings its own interactions and is less easily displaced",
    # ---- GROUP 3: SOLD WIDELY, CONTROLLED COMPARISONS DO NOT SUPPORT IT ---------
    "Commercial microbial products for routine soil hydrocarbon treatment, "
    "which repeatedly fail to outperform supplying oxygen alone in side-by-side "
    "field comparisons",
    "Grease trap, drain and septic system dosing products sold to households "
    "and food businesses, where the resident community is already established "
    "and already degrading the substrate",
    "Odour control and general performance additives for operating wastewater "
    "plants, marketed on plant-scale before-and-after observations that lack a "
    "control and are confounded by every other operational change",
    "Compost and manure inoculants intended to accelerate decomposition, "
    "against which the residents in the material are already numerous and "
    "already adapted",
    "General-purpose pond, lagoon and aquarium clarifier cultures, which are "
    "the same proposition sold at consumer scale",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by the problem each is trying to solve, which is almost always
#  survival rather than degradation.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- deciding whether to augment at all, which comes first -----------------
    "Molecular screening of the site for the relevant organisms and functional "
    "genes before purchase, which is the single most valuable technology in "
    "this record because it distinguishes an absent capability from an underfed "
    "one",
    "Side-by-side microcosm testing of augmented and unaugmented site material, "
    "which is the only design that can detect an effect against the residents",
    # ---- selecting and producing the culture ------------------------------------
    "Enrichment culture derivation from contaminated site material, which "
    "selects organisms already adapted to the conditions rather than to a "
    "laboratory",
    "Characterised commercial consortium production under quality control, "
    "which is what distinguishes the dechlorinating cultures from an undefined "
    "mixture in a bottle",
    "Fermentation and preservation of cultures, including freeze-drying and "
    "cold chain, which determine how many organisms are alive on arrival",
    # ---- keeping the organisms alive long enough to matter ----------------------
    "Encapsulation and carrier immobilisation in alginate, biochar or polymer "
    "supports, which shields introduced cells from predation and desiccation",
    "Biofilm-associated and granular delivery, on the reasoning that an "
    "aggregate resists grazing better than a suspension",
    "Acclimation of the culture to site temperature, pH and salinity before "
    "release, which addresses part of the shock and none of the competition",
    "Co-delivery of substrate or electron donor, which supports the introduced "
    "population and equally supports the residents",
    # ---- getting them into the ground -------------------------------------------
    "Injection well and direct-push delivery, and the distribution problem that "
    "an injected culture reaches only where the water goes",
    "Recirculation systems that move the culture through the treatment zone "
    "rather than leaving it at the injection point",
    # ---- finding out whether anything established --------------------------------
    "Quantitative tracking of the introduced strain by strain-specific markers, "
    "which is what turned this field from opinion into measurement",
    "Functional gene monitoring over time, distinguishing a population that "
    "established from one that was merely detected on the day it was added",
)


# =============================================================================
#  ORGANISMS
#  The first entry is the one that justifies the whole practice.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "dehalococcoides_mccartyi",  # the case where augmentation is genuinely right
    "pseudomonas_putida",  # the most-sold degrader, and the most-refuted
    "rhodococcus_erythropolis",  # unusually persistent, which is the rare virtue
    "nitrosomonas_europaea",  # slow-growing nitrifier, the plant startup case
    "bacillus_subtilis",  # spore-forming, survives the bottle rather than the site
    "methanosarcina_barkeri",  # digester seeding, where there is no incumbent
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "enrichment_culture",
    "qpcr",
    "metagenomics",
    "microcosm_testing",
    "cell_immobilisation",
    "freeze_drying",
    "fluorescence_in_situ_hybridisation",
    "statistical_experimental_design",
)


# =============================================================================
#  CHALLENGES
#  The first four are the mechanism of failure, in the order it happens.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- the mechanism of failure, step by step --------------------------------
    "Competition from the resident community, which is present because it is "
    "adapted to those conditions and which outnumbers an introduced population "
    "by many orders of magnitude on the day of application",
    "Predation by protozoa and bacteriophage, which removes introduced cells "
    "preferentially because they are not embedded in the existing biofilm "
    "structure",
    "Physiological shock on transfer from a rich laboratory medium to a cold, "
    "nutrient-poor, contaminated matrix",
    "Rapid population decline, commonly by orders of magnitude within weeks, "
    "regardless of how competent a degrader the strain is in pure culture",
    # -- why improving the product does not fix it -------------------------------
    "Selection in the laboratory optimising the wrong variable, since strains "
    "are screened for degradation rate in the absence of competitors and the "
    "binding constraint in the field is survival",
    "Absence of a mechanism by which a better degrader would establish better, "
    "which is the reason forty years of product improvement has not changed "
    "the field comparisons",
    # -- getting there at all -----------------------------------------------------
    "Physical delivery through a heterogeneous subsurface, where an injected "
    "culture follows the permeable paths and never reaches the low-permeability "
    "material holding most of the contaminant",
    "Viability losses in production, storage and transport, so the count on the "
    "label is not the count that arrives",
    # -- and why nobody notices --------------------------------------------------
    "Evidence quality in the commercial literature, which is dominated by "
    "uncontrolled before-and-after observations at plant scale where every "
    "other operating variable changed at the same time",
    "Undefined product composition, since a bottle labelled as a consortium may "
    "not be characterised and its contents may not be verifiable by the buyer",
    "Attribution of natural attenuation to the product, because contamination "
    "concentrations fall over time whether or not anything was added",
    "Regulatory approval for releasing non-indigenous or engineered organisms, "
    "which forecloses the one route by which a genuinely superior degrader "
    "might be deployed",
)
