# =============================================================================
#  biotechnology.branches.grey.air_biotreatment.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IN THIS FACET IS A PROPERTY OF THE COMPOUND, NOT OF THE
#  PLANT.
#
#  Every other record in this branch opens with something the operator
#  influences. Here the opening number is the Henry's law constant, which is
#  fixed by chemistry and temperature and which decides in advance whether the
#  technique can work at all. A designer reads it before sizing anything,
#  because no amount of bed, biomass or residence time compensates for a
#  compound that will not enter the water.
#
#      SOLUBILITY IS THE SPECIFICATION. EVERYTHING ELSE IS THE DESIGN.
#
#  THE SECOND ORGANISING IDEA IS THAT PERCENTAGE REMOVAL IS THE WRONG FIGURE TO
#  COMPARE PLANTS ON, AND IT IS THE ONE ALWAYS QUOTED. A bed removing a high
#  percentage of a very dilute stream may be destroying less mass per cubic
#  metre than a bed removing a modest percentage of a concentrated one.
#  Elimination capacity, which is mass destroyed per volume of bed per hour, is
#  what actually sizes equipment, so it is placed above the percentage.
#
#  A THIRD POINT, AND IT IS UNUSUAL FOR THIS LIBRARY. THE COMPLIANCE METRIC IS
#  A HUMAN PANEL. Odour concentration is defined as the dilution at which half
#  a trained panel can just detect the sample. It is a real, standardised,
#  reproducible measurement and its unit is a person.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  THE PROPERTY THAT DECIDES WHETHER THE TECHNIQUE APPLIES
    # =========================================================================
    Metric(
        name="Henry's law constant",
        symbol="H",
        unit="dimensionless gas to liquid partition ratio",
        formula="henry_law",
        typical="low for hydrogen sulphide, ammonia and alcohols, which are "
        "treatable; high for methane and chlorinated solvents, which are not",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Placed first because it is read before anything is designed and "
            "because it is not a property of the plant. It states how a "
            "compound distributes between gas and water at equilibrium, and "
            "therefore whether the organisms will ever be presented with it. No "
            "quantity of bed, biomass or residence time compensates for an "
            "unfavourable value, which is why this record's scope is a list of "
            "compounds rather than a list of concentrations."
        ),
    ),
    Metric(
        name="Empty bed residence time",
        symbol="EBRT",
        unit="seconds",
        typical="seconds, which is what makes treating very large air volumes "
        "practical",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The bed volume divided by the gas flow, and the primary design "
            "variable. It is quoted on the empty bed rather than the void space "
            "because it is the number that sizes the vessel and the land it "
            "stands on. Extending it is the standard response to poor "
            "performance and it helps only when the limitation is reaction rate "
            "rather than partitioning."
        ),
    ),
    # =========================================================================
    #  WHAT THE BED ACTUALLY DESTROYS, WHICH IS NOT A PERCENTAGE
    # =========================================================================
    Metric(
        name="Elimination capacity",
        symbol="EC",
        unit="grams of contaminant destroyed per cubic metre of bed per hour",
        formula="mass_balance",
        typical="compound specific, and highest for readily soluble compounds "
        "such as hydrogen sulphide",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The figure that sizes equipment and the fair basis for comparing "
            "installations, which is why it is placed above the removal "
            "efficiency below. A bed treating a very dilute stream can report "
            "excellent percentage removal while destroying very little mass per "
            "unit volume."
        ),
    ),
    Metric(
        name="Removal efficiency",
        symbol="eta",
        unit="per cent of inlet load removed",
        typical="high for soluble compounds; poor for compounds with an "
        "unfavourable partition ratio regardless of bed condition",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The figure always quoted and the one that misleads when quoted "
            "alone. It is meaningful only alongside the inlet load, since the "
            "same percentage means entirely different things at different "
            "concentrations. Read together with the entry above it is "
            "informative; read alone it is marketing."
        ),
    ),
    Metric(
        name="Critical load",
        symbol="L_crit",
        unit="grams per cubic metre of bed per hour at which removal begins to "
        "fall",
        typical="the design ceiling, and the point at which thermal treatment "
        "becomes the correct choice",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The loading beyond which the bed can no longer keep pace and "
            "removal efficiency drops. It is the practical boundary between "
            "this record and combustion, and it is the number a designer checks "
            "against the peak load rather than the average one, because peaks "
            "are what a bed fails on."
        ),
    ),
    # =========================================================================
    #  THE COMPLIANCE MEASUREMENT, WHOSE UNIT IS A PERSON
    # =========================================================================
    Metric(
        name="Odour concentration",
        symbol="c_od",
        unit="European odour units per cubic metre",
        typical="expressed as the dilution at which half a trained panel can "
        "just detect the sample",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Defined by a standardised procedure using trained human panels "
            "under EN 13725, which makes it reproducible without making it "
            "instrumental. It is the acceptance criterion that actually decides "
            "compliance, and it is why a plant can satisfy every chemical "
            "specification and still fail: the compounds that offend a nose do "
            "so far below instrumental detection limits."
        ),
    ),
    Metric(
        name="Hedonic tone and odour annoyance",
        symbol="H_tone",
        unit="qualitative scale from pleasant to unpleasant, assessed by panel",
        typical="assessed alongside concentration where a complaint has been "
        "made",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Recorded because concentration alone does not predict complaint. "
            "The same odour unit value from a bakery and from a rendering plant "
            "produces very different responses, so a purely quantitative "
            "criterion misdescribes the problem the plant was built to solve."
        ),
    ),
    # =========================================================================
    #  KEEPING THE BED ALIVE, WHICH IS WHERE OPERATION ACTUALLY GOES
    # =========================================================================
    Metric(
        name="Bed moisture content",
        symbol="w_bed",
        unit="per cent by mass",
        typical="a narrow window, below which the biofilm dies and above which "
        "the bed becomes anaerobic and blocks",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The variable that most operator attention goes to, because both "
            "directions fail. Drying kills the biofilm from the inlet end, "
            "which is why incoming air is humidified; waterlogging closes the "
            "void space and turns the bed anaerobic, which produces the odour "
            "the plant exists to remove."
        ),
    ),
    Metric(
        name="Pressure drop across the bed",
        symbol="dP",
        unit="pascals",
        typical="rises over the life of the packing as it compacts and biomass "
        "accumulates",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The whole of the running cost, since fan power is what this "
            "technique consumes. A rising trend is also the clearest early "
            "signal that the packing is compacting or overgrown, and the point "
            "at which the fan can no longer deliver design flow is effectively "
            "the end of the media life."
        ),
    ),
    Metric(
        name="Bed pH",
        symbol="pH",
        unit="dimensionless",
        typical="falls where sulphur or chlorine compounds are degraded, unless "
        "the products are washed out",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Included because the degradation produces the acid that then "
            "destroys the community performing it, which is a self-limiting "
            "process rather than an external upset. It is the specific reason "
            "sulphide treatment uses a trickling configuration with "
            "recirculated liquid rather than a simple compost bed."
        ),
    ),
    Metric(
        name="Media service life",
        symbol="t_media",
        unit="years",
        typical="a few years for organic packings, considerably longer for "
        "structured inert media",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The recurring capital cost that comparisons against thermal "
            "treatment routinely omit. Organic packing compacts, degrades and "
            "channels, and replacing it is a plant outage as well as a "
            "purchase. Including it is the difference between an honest whole "
            "life comparison and a favourable one."
        ),
    ),
    # =========================================================================
    #  AND THE COMPARISON THAT JUSTIFIES THE TECHNIQUE
    # =========================================================================
    Metric(
        name="Energy consumption per volume of air treated",
        symbol="E_air",
        unit="kilowatt hours per thousand cubic metres",
        typical="far below thermal oxidation for dilute streams, since only fan "
        "power is required",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The reason the technique exists. Thermal oxidation must heat a gas "
            "stream that is almost entirely nitrogen; this runs at ambient "
            "temperature on fan power alone. It is one of the few places in "
            "this library where the biological option wins on energy by an "
            "order of magnitude rather than by a margin."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Partitioning first, because it is the constraint, then transfer and kinetics.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "henry_law",
    "mass_transfer_coefficient",
    "monod_equation",
    "mass_balance",
    "first_order_decay",
    "pressure_drop",
)
