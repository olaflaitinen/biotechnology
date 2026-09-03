# =============================================================================
#  biotechnology.branches.grey.bioremediation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two: an engineered organism that was patented, famous
#  and never used, and a decade of overpromising that a regulatory report
#  eventually had to correct.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 1980 PATENT IS THE MOST FAMOUS EVENT IN THIS RECORD AND THE LEAST
#  CONSEQUENTIAL TECHNICALLY.
#
#  A court held that a genetically modified oil-degrading bacterium was
#  patentable subject matter, which established that living organisms may be
#  patented and underpins a great deal of what `purple.biotechnology_patents`
#  covers. The organism itself was never deployed. It could not compete with
#  the indigenous communities already present at contaminated sites, which is
#  the finding `grey.bioaugmentation` documents in general.
#
#  So the landmark case of biotechnology patent law rests on an organism whose
#  own field concluded was unnecessary. Recording that plainly is more useful
#  than recording the case alone, and it is the earliest instance of this
#  branch's recurring lesson: the residents are already there and they are
#  already adapted.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE CAPABILITY IS NOTICED
    # =========================================================================
    Milestone(
        1946,
        "Microbial degradation of hydrocarbons is documented systematically",
        note=(
            "The observation that organisms in ordinary soil and seawater "
            "consume petroleum. It was studied initially as a nuisance, since "
            "the same activity spoils stored fuel, which is a recurring pattern "
            "in this branch: several of its capabilities were first met as "
            "problems."
        ),
    ),
    Milestone(
        1972,
        "Comprehensive water pollution legislation makes biological treatment "
        "a legal requirement",
        note=(
            "Recorded here as well as in `grey.wastewater_treatment` because it "
            "created the regulatory environment in which contaminated site "
            "cleanup became an obligation rather than a choice, and therefore "
            "created a market for anything cheaper than excavation."
        ),
    ),
    # =========================================================================
    #  THE FAMOUS CASE, AND THE ORGANISM THAT WAS NEVER USED
    # =========================================================================
    Milestone(
        1980,
        "A court holds that a genetically modified oil-degrading bacterium is "
        "patentable subject matter",
        note=(
            "The decision established that living organisms may be patented and "
            "underpins much of `purple.biotechnology_patents`. The organism "
            "itself was never deployed at any site: it could not compete with "
            "the indigenous communities already present, which is the general "
            "finding `grey.bioaugmentation` documents. The landmark of "
            "biotechnology patent law rests on an organism its own field "
            "concluded was unnecessary."
        ),
    ),
    # =========================================================================
    #  THE FIELD'S DEFINING DEMONSTRATION
    # =========================================================================
    Milestone(
        1989,
        "Shoreline bioremediation is deployed at scale after a major oil spill "
        "in Alaska",
        note=(
            "Fertiliser was applied to oiled shorelines to relieve the nitrogen "
            "limitation on indigenous hydrocarbon degraders. Treated areas "
            "cleared measurably faster than untreated controls, and the work "
            "was studied carefully enough to constitute evidence rather than "
            "anecdote. It is the field's founding public demonstration, and "
            "what it demonstrated was BIOSTIMULATION rather than the addition "
            "of organisms."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A DECADE OF OVERPROMISING
    # =========================================================================
    Milestone(
        1993,
        "Regulatory and technical reviews find that field bioremediation "
        "performance falls well short of laboratory expectations",
        note=(
            "Following the enthusiasm of the late 1980s, systematic assessment "
            "found treatments stalling above target concentrations, timescales "
            "several times longer than projected, and vendors offering "
            "proprietary cultures with no demonstrated advantage. The cause was "
            "not fraud but a category error: laboratory microcosms measure "
            "degradability and field sites are limited by bioavailability. It "
            "is recorded as a setback because the field's credibility took "
            "years to recover and because the same overstatement recurs "
            "whenever a new contaminant class is proposed."
        ),
    ),
    # =========================================================================
    #  THE IDEA THAT DOING NOTHING CAN BE AN INTERVENTION
    # =========================================================================
    Milestone(
        1995,
        "Monitored natural attenuation is accepted as a remediation strategy",
        note=(
            "Regulators accepted that where indigenous degradation exceeds "
            "plume migration and nobody is exposed, documenting that is an "
            "appropriate response. It is the only approved technology in this "
            "library whose intervention is measurement. It also demanded "
            "evidence rather than assertion, which is what drove the adoption "
            "of the isotope methods below."
        ),
    ),
    Milestone(
        1997,
        "Reductive dechlorination by Dehalococcoides is characterised",
        note=(
            "Organisms that use chlorinated solvents as electron acceptors "
            "rather than as food, and the only known genus capable of "
            "completing the sequence to harmless ethene. Where that genus is "
            "absent, the process stalls at vinyl chloride, which is more toxic "
            "than the parent compound. It is the one case in this record where "
            "adding organisms is genuinely the right answer."
        ),
    ),
    # =========================================================================
    #  PROVING IT RATHER THAN CLAIMING IT
    # =========================================================================
    Milestone(
        2000,
        "Compound-specific isotope analysis enters routine site assessment",
        note=(
            "Degradation enriches the heavier isotope in the remaining "
            "contaminant and dilution does not, so the two can finally be "
            "distinguished. It converted monitored natural attenuation from a "
            "plausible claim into a demonstrable one, and it is the single most "
            "useful analytical development in this record."
        ),
    ),
    Milestone(
        2005,
        "Molecular biological tools quantifying degrader genes become standard "
        "site assessment",
        note=(
            "Establishing whether the organisms and genes are present before "
            "designing a treatment, which distinguishes a site needing "
            "biostimulation from one genuinely lacking the capability. It made "
            "the choice between the two strategies evidential rather than a "
            "matter of vendor preference."
        ),
    ),
    # =========================================================================
    #  THE UNPLANNED FIELD EXPERIMENT
    # =========================================================================
    Milestone(
        2010,
        "A deep-water oil release tests hydrocarbon degradation under "
        "conditions nobody had studied",
        note=(
            "Oil released at great depth into cold water, with dispersants "
            "applied at the wellhead. Indigenous psychrophilic hydrocarbon "
            "degraders bloomed and degraded a substantial fraction of the "
            "dispersed hydrocarbons, faster than expected at those "
            "temperatures. The interpretation remains debated, particularly the "
            "effect of the dispersants and the fate of the material that "
            "reached the sea floor, and it is recorded with that qualification."
        ),
    ),
    # =========================================================================
    #  THE CONTAMINANT BIOLOGY CANNOT REACH
    # =========================================================================
    Milestone(
        2019,
        "Per- and polyfluoroalkyl substances are recognised as a contamination "
        "class biological treatment does not address",
        note=(
            "The carbon-fluorine bond is among the strongest in organic "
            "chemistry, and no established biological treatment mineralises "
            "these compounds. They are widespread, mobile and persistent. "
            "Recorded here rather than omitted because a record describing what "
            "bioremediation can do should be explicit about a major "
            "contemporary contaminant it cannot, and because the field's "
            "instinct to promise a biological answer is exactly what the 1993 "
            "entry warns against."
        ),
    ),
)
