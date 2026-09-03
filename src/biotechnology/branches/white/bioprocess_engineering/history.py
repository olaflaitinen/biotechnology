# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two of different kinds. One is a strategic error that
#  the whole industry made together and had a decade to regret. The other is a
#  single facility failure that became an international shortage of medicines,
#  and it is the clearest demonstration anywhere in this library that process
#  engineering is a patient safety discipline.
#
#  SUBTYPE-SPECIFIC NOTE
#  This timeline shares its 1943 origin with `white.microbial_fermentation`,
#  and the two records take different things from it. That record takes the
#  cultivation technique; this one takes the fact that a profession had to be
#  invented to build the vessel, because no existing discipline covered a
#  sterile, aerated, heat-generating, mechanically agitated vessel that had to
#  run for a fortnight without failing.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  A PROFESSION IS INVENTED
    # =========================================================================
    Milestone(
        1943,
        "Deep-tank penicillin manufacture requires an engineering discipline "
        "that does not yet exist",
        note=(
            "No existing profession covered a sterile, aerated, "
            "heat-generating, mechanically agitated vessel expected to run for "
            "two weeks without failure. Chemical engineers, microbiologists and "
            "mechanical engineers were assembled into what became bioprocess "
            "engineering. The discipline was created by a manufacturing "
            "emergency rather than by an academic programme."
        ),
    ),
    Milestone(
        1959,
        "Centrifuge scale-up is placed on a rational basis by the sigma factor",
        note=(
            "A geometry-independent way to compare centrifuges, so that "
            "performance on a laboratory machine could predict performance on a "
            "production one. It is the downstream counterpart of the transport "
            "correlations used for vessels, and it made the harvest step "
            "designable rather than empirical."
        ),
    ),
    # =========================================================================
    #  THE TRANSPORT PROBLEMS ARE FORMALISED
    # =========================================================================
    Milestone(
        1960,
        "Oxygen transfer correlations and dimensional analysis become standard "
        "practice in reactor design",
        note=(
            "Scale-up moved from craft to calculation, and in doing so exposed "
            "the paradox recorded in `metrics.py`: once the criteria could be "
            "computed, it became clear that they could not all be satisfied at "
            "once. Formalising the problem is what revealed it had no general "
            "solution."
        ),
    ),
    # =========================================================================
    #  PURIFICATION BECOMES THE MAIN EVENT
    # =========================================================================
    Milestone(
        1968,
        "Affinity chromatography is introduced",
        note=(
            "Separation by specific molecular recognition rather than by bulk "
            "physical property. It eventually made it possible to capture a "
            "protein from a complex broth in one step, which is the single "
            "largest simplification the downstream train has ever received."
        ),
    ),
    Milestone(
        1986,
        "Affinity capture becomes the standard first purification step for "
        "therapeutic antibodies",
        note=(
            "One step removing the great majority of impurities, and it "
            "standardised antibody manufacture to the degree that platform "
            "processes became possible. Its consequence was that a new antibody "
            "could reuse an existing process rather than requiring a new one."
        ),
    ),
    # =========================================================================
    #  THE SETBACK THE WHOLE INDUSTRY SHARED
    # =========================================================================
    Milestone(
        2005,
        "Upstream titres outgrow downstream capacity and create the downstream "
        "bottleneck",
        note=(
            "Cell line and media improvements raised therapeutic protein "
            "titres by roughly two orders of magnitude over about fifteen "
            "years. Downstream capacity did not follow, because chromatography "
            "scales with product mass rather than with broth volume. Facilities "
            "designed for the old ratio could not process what the new cell "
            "lines produced, and the constraint moved from the fermenter to the "
            "purification suite. It is recorded as a setback because it was an "
            "avoidable strategic error: an industry optimised one end of its "
            "own process for a decade without asking what the other end could "
            "absorb."
        ),
    ),
    # =========================================================================
    #  MAKING THE PLANT FLEXIBLE
    # =========================================================================
    Milestone(
        2005,
        "Single-use bioreactors and disposable flow paths enter widespread use",
        note=(
            "Pre-sterilised disposable equipment removed cleaning and cleaning "
            "validation between campaigns, raised facility utilisation and made "
            "multi-product plants practical. The costs are a plastic waste "
            "stream, an extractables and leachables assessment for every "
            "contact surface, and dependence on a small number of suppliers."
        ),
    ),
    Milestone(
        2004,
        "Regulators adopt process analytical technology and quality by design",
        note=(
            "A deliberate move away from testing quality into a finished batch "
            "and towards designing and controlling it in the process. It is the "
            "regulatory origin of the design space concept and of the "
            "measurement technologies in `practice.TECHNOLOGIES`."
        ),
    ),
    # =========================================================================
    #  THE SETBACK THAT REACHED PATIENTS
    # =========================================================================
    Milestone(
        2009,
        "Viral contamination of a single manufacturing plant causes "
        "international shortages of two enzyme replacement therapies",
        note=(
            "A virus entered the cell culture operation at a facility that was "
            "the sole source of two treatments for rare inherited diseases. "
            "Production stopped, patients were rationed, and supply took years "
            "to recover fully. The lessons are structural rather than "
            "technical: raw material and cell culture media are a contamination "
            "route into an otherwise closed process, and single-source "
            "manufacture of a medicine with no substitute converts an "
            "engineering failure directly into patient harm. It is the "
            "strongest argument in this library for treating process "
            "engineering as a patient safety discipline."
        ),
    ),
    # =========================================================================
    #  DOING MORE IN LESS SPACE
    # =========================================================================
    Milestone(
        2015,
        "Continuous and intensified bioprocessing move from proposal to "
        "practice",
        note=(
            "Perfusion culture connected to continuous capture removes hold "
            "tanks and raises volumetric productivity, shrinking the facility "
            "rather than improving the biology. It also raises the batch "
            "definition question recorded in `white.microbial_fermentation`, "
            "which regulators have since addressed explicitly."
        ),
    ),
    Milestone(
        2021,
        "Rapid capacity expansion for pandemic vaccine manufacture tests every "
        "assumption in this record at once",
        note=(
            "Technology transfer between sites, parallel scale-up, and supply "
            "chains for single-use consumables and filters were all stressed "
            "simultaneously. It demonstrated both that transfer can be "
            "compressed dramatically when resources are unlimited, and that "
            "consumable supply chains are a genuine constraint on how fast the "
            "world can manufacture a biological product."
        ),
    ),
)
