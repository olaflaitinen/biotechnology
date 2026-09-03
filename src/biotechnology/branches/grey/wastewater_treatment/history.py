# =============================================================================
#  biotechnology.branches.grey.wastewater_treatment.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FOUNDING INSIGHT OF THIS FIELD PREDATES ANY UNDERSTANDING OF WHAT WAS
#  DOING THE WORK.
#
#  Activated sludge was developed in 1914 by observing that aerating sewage and
#  RETURNING THE SETTLED SOLIDS produced far better treatment than aerating it
#  alone. Nobody involved knew which organisms were present, and the organisms
#  in question were not identified for decades. The insight was engineering:
#  keep the biomass, discard the water.
#
#  That is worth stating because it inverts the usual order in this library. In
#  `red` and `white` the science precedes the application. Here a process that
#  now serves most of the urban world was running at scale for eighty years
#  before molecular methods showed what was actually in the tank, and when they
#  did they found that the dominant organisms had never been cultured.
#
#  RULE 8 APPLIES CAREFULLY TO THE 1914 ENTRY. The work is properly credited to
#  a group rather than an individual, it built on earlier aeration experiments
#  by others, and the recognition that returning sludge was the essential step
#  emerged from a sequence of experiments rather than from one moment.
#
#  THE SETBACK IN THIS RECORD IS NOT A TECHNICAL FAILURE. It is that the
#  process was designed for carbon, deployed globally for carbon, and then
#  found to be discharging the nutrients that cause eutrophication. The
#  technology worked exactly as intended and the intention was incomplete.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  SEPARATING SEWAGE FROM DRINKING WATER
    # =========================================================================
    Milestone(
        1854,
        "A London cholera outbreak is traced to a contaminated water supply",
        note=(
            "Not a treatment technology, and the reason every treatment "
            "technology below exists. Establishing that disease travelled in "
            "water rather than in air converted sewage from a nuisance into a "
            "public health emergency, and it created the political will that "
            "built the sewer networks."
        ),
    ),
    Milestone(
        1890,
        "Septic tanks and contact beds provide the first deliberate biological "
        "treatment",
        note=(
            "Retention in a closed tank was found to reduce the offensiveness "
            "of sewage substantially, through anaerobic activity nobody had "
            "characterised. It is the ancestor of the anaerobic digester and "
            "it was adopted for the practical reason that it worked."
        ),
    ),
    # =========================================================================
    #  THE INVENTION, AND IT IS AN ENGINEERING INVENTION
    # =========================================================================
    Milestone(
        1914,
        "Activated sludge is developed by returning settled solids to the "
        "aeration tank",
        note=(
            "The step that made city-scale treatment possible. Aerating sewage "
            "helps; aerating it and returning the settled biomass helps "
            "enormously, because it uncouples how long the organisms stay from "
            "how long the water stays and allows slow-growing organisms to "
            "persist in a fast-flowing system. It was developed by a research "
            "group building on earlier aeration work by others, and it was "
            "understood as an engineering result. Which organisms were "
            "responsible was not known and would not be known for decades."
        ),
    ),
    Milestone(
        1936,
        "Anaerobic digestion of sludge with gas capture is adopted at municipal "
        "scale",
        note=(
            "Digesting the sludge reduced its mass, destroyed pathogens and "
            "produced methane that could run the plant. It made the material "
            "the process generates into a partial answer to the energy the "
            "process consumes, which is still the strongest argument in the "
            "record's economics."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE PROCESS WORKED, AND THE OBJECTIVE WAS INCOMPLETE
    # =========================================================================
    Milestone(
        1965,
        "Eutrophication is attributed to nutrient discharge from treated "
        "effluent",
        note=(
            "Plants built to remove organic carbon were doing so successfully "
            "and discharging nitrogen and phosphorus, which fed algal blooms "
            "and produced the oxygen depletion the treatment was meant to "
            "prevent. Nothing had failed technically. The objective had been "
            "defined too narrowly, and correcting it required rebuilding "
            "process trains worldwide at considerable cost."
        ),
    ),
    Milestone(
        1972,
        "Comprehensive water pollution legislation makes secondary treatment a "
        "legal requirement",
        note=(
            "Treatment became an obligation with numerical discharge limits "
            "rather than a municipal choice. This is the entry that created the "
            "compliance framework the rest of the record operates in, and it "
            "is recorded in `grey.bioremediation` as well for the same reason."
        ),
    ),
    # =========================================================================
    #  ENGINEERING THE NUTRIENT PROBLEM OUT
    # =========================================================================
    Milestone(
        1976,
        "Enhanced biological phosphorus removal is developed by alternating "
        "anaerobic and aerobic conditions",
        note=(
            "Exposing the community to anaerobic and then aerobic conditions in "
            "sequence selects organisms that store phosphorus far in excess of "
            "their own requirement, so the phosphorus leaves in the sludge. It "
            "is the clearest example in the record of the branch's governing "
            "principle: the engineering selects the organisms rather than "
            "supplying them."
        ),
    ),
    Milestone(
        1980,
        "Combined nitrification and denitrification process configurations "
        "enter general use",
        note=(
            "Sequencing anoxic and aerobic zones so that the two contradictory "
            "nitrogen steps can both occur in one plant, with the influent "
            "carbon reserved for the denitrifying step. It solved the nitrogen "
            "problem and it raised the cost of a works substantially, which is "
            "why nutrient removal is the first capability omitted where budgets "
            "are short."
        ),
    ),
    # =========================================================================
    #  FINALLY LOOKING AT WHAT IS IN THE TANK
    # =========================================================================
    Milestone(
        1989,
        "Membrane bioreactors remove the settling constraint on biomass "
        "concentration",
        note=(
            "Holding the biomass behind a membrane rather than settling it "
            "allows far higher concentrations and a much smaller footprint, at "
            "the cost of energy and of fouling. It is the first process in the "
            "record that does not depend on sludge settling, which had been the "
            "binding constraint since 1914."
        ),
    ),
    Milestone(
        1995,
        "Molecular methods reveal that the dominant organisms in activated "
        "sludge had never been cultured",
        note=(
            "Applying fluorescence in situ hybridisation and sequence-based "
            "surveys to mixed liquor showed that the organisms responsible for "
            "phosphorus removal and much else were not the ones the culture "
            "collections contained. A process serving hundreds of millions of "
            "people had been engineered for eighty years without knowing what "
            "performed it, which is the strongest illustration available that "
            "the selection principle works without the identification."
        ),
    ),
    Milestone(
        1999,
        "Anaerobic ammonium oxidation is confirmed in engineered systems",
        note=(
            "Organisms converting ammonium directly to nitrogen gas without the "
            "full oxygen demand or the organic carbon the conventional pair "
            "requires. They grow very slowly, which is why they were missed for "
            "so long and why the processes built on them depend on retaining "
            "biomass extremely well."
        ),
    ),
    # =========================================================================
    #  WHAT IS ASKED OF THE PROCESS NOW
    # =========================================================================
    Milestone(
        2005,
        "Aerobic granular sludge achieves settling and nutrient removal in a "
        "single reactor",
        note=(
            "Biomass that self-aggregates into dense granules settles rapidly "
            "and holds aerobic and anoxic zones within each granule, so one "
            "tank does what a sequence of tanks did. It reduces footprint and "
            "energy together, which is unusual, and it is the most significant "
            "process development of the period."
        ),
    ),
    Milestone(
        2012,
        "Micropollutants and antibiotic resistance genes are documented passing "
        "through conventional treatment",
        note=(
            "Pharmaceuticals, hormones and fluorinated compounds pass a process "
            "designed for carbon and nutrients, and dense mixed communities "
            "concentrate resistance genes rather than destroying them. "
            "Addressing this requires ozonation or activated carbon stages, "
            "which is chemistry added to biology rather than better biology, "
            "and it connects this record to `dark.antimicrobial_resistance`."
        ),
    ),
    Milestone(
        2020,
        "Wastewater surveillance is deployed at population scale for infectious "
        "disease monitoring",
        note=(
            "Sewage was used to track pathogen prevalence across whole "
            "populations, including people never tested individually. It gave "
            "a century-old sanitary system an entirely new function as a public "
            "health instrument, and it is the clearest recent demonstration "
            "that this infrastructure is more than a disposal system."
        ),
    ),
)
