# =============================================================================
#  biotechnology.branches.white.biofuels.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  This record has three, which is more than any other in the library, and that
#  is not an editorial choice but an accurate reflection of the field.
#
#  SUBTYPE-SPECIFIC NOTE
#  The timeline shows a pattern worth naming. Biofuel expansion has repeatedly
#  been driven by ENERGY SECURITY rather than by climate: 1975 in Brazil after
#  the oil shock, 2005 in the United States, and again after 2022. Climate
#  arguments were attached afterwards. That ordering explains why several
#  policies mandated volumes without first establishing whether the volumes
#  were achievable, and why the resulting fuels were then judged against a
#  criterion they had not been designed for.
#
#  The three setbacks are of three kinds: a policy that mandated more than the
#  technology could deliver, a technology that was funded far ahead of its
#  evidence, and a scientific finding that reversed a widely held assumption.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  IT WAS THERE AT THE BEGINNING
    # =========================================================================
    Milestone(
        1900,
        "Diesel demonstrates a compression ignition engine running on peanut "
        "oil",
        note=(
            "Vegetable oil fuel is as old as the engine itself. Petroleum won "
            "on cost and availability rather than on any technical merit, which "
            "is worth remembering when biofuels are described as a new idea."
        ),
    ),
    Milestone(
        1908,
        "The Ford Model T is designed to run on ethanol as well as petrol",
        note=(
            "Early vehicles were fuel-agnostic. The infrastructure, not the "
            "engine, is what eventually made petroleum the only practical "
            "option, and it is still the infrastructure that constrains this "
            "record through the blend limit."
        ),
    ),
    # =========================================================================
    #  ENERGY SECURITY BUILDS AN INDUSTRY
    # =========================================================================
    Milestone(
        1975,
        "Brazil launches a national programme to substitute sugarcane ethanol "
        "for imported petrol",
        note=(
            "Motivated entirely by the oil shock and the balance of payments, "
            "not by emissions. It produced the only large-scale, decades-long "
            "demonstration that a substantial share of a national light vehicle "
            "fleet can run on a biofuel, and it did so on the one feedstock "
            "whose energy return is not seriously disputed."
        ),
    ),
    Milestone(
        2003,
        "The European Union adopts its first biofuels directive with "
        "indicative targets",
        note=(
            "The beginning of a policy sequence that would repeatedly have to "
            "be revised as the land use consequences became clearer."
        ),
    ),
    Milestone(
        2005,
        "The United States establishes a renewable fuel standard with "
        "volumetric mandates",
        note=(
            "Guaranteed demand by law rather than by price. It built a very "
            "large maize ethanol industry quickly, and it also created the "
            "conditions for the first setback below, by mandating volumes of a "
            "fuel that did not yet exist at scale."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A FINDING THAT CHANGED THE QUESTION
    # =========================================================================
    Milestone(
        2008,
        "Indirect land use change is quantified and the case for crop-based "
        "fuels is substantially weakened",
        note=(
            "Analyses showed that accounting only for emissions at the field "
            "and the plant omitted the largest term: land converted elsewhere "
            "when displaced food production moves. Under some estimates a "
            "crop-based fuel offered no benefit at all. The finding is "
            "contested in magnitude and accepted in principle, and it reversed "
            "the policy direction of an entire sector. It is recorded as a "
            "setback because the field had been expanding for years on an "
            "assumption that had not been tested."
        ),
    ),
    Milestone(
        2008,
        "Food price spikes bring the food and fuel argument into public "
        "politics",
        note=(
            "The contribution of biofuel demand to the price rise is disputed "
            "among economists and was decisive in public perception regardless. "
            "After this, crop-based fuel had to defend itself on a question it "
            "had not previously been asked."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: FUNDED FAR AHEAD OF THE EVIDENCE
    # =========================================================================
    Milestone(
        2009,
        "Algal biofuel attracts major investment and largely fails to deliver "
        "fuel",
        note=(
            "Substantial public and private funding followed projections of "
            "very high areal productivity. Sustained large-scale cultivation "
            "proved far harder than the laboratory suggested, harvesting a "
            "dilute suspension is expensive, and lipid extraction consumed much "
            "of the energy gained. Most programmes redirected towards "
            "nutritional and specialty products, where "
            "`blue.algal_biotechnology` records their genuine successes. The "
            "lesson is about extrapolating laboratory productivity to open "
            "systems, not about algae being useless."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A MANDATE THE TECHNOLOGY COULD NOT MEET
    # =========================================================================
    Milestone(
        2014,
        "Commercial cellulosic ethanol plants open, and most are idled or "
        "closed within a few years",
        note=(
            "Several flagship facilities were built against mandated volumes. "
            "They ran, and they did not run economically: enzyme cost stayed "
            "high, pretreatment inhibitors depressed fermentation, titres were "
            "low so distillation energy was high, and feedstock collection over "
            "a wide radius was expensive. Mandated volumes were repeatedly "
            "written down, by orders of magnitude in some years. It is the "
            "clearest case in this library of policy mandating an outcome that "
            "the underlying science could not supply on the schedule assumed, "
            "and the capital that followed the mandate was largely lost."
        ),
    ),
    # =========================================================================
    #  WHERE THE FIELD ACTUALLY WENT
    # =========================================================================
    Milestone(
        2018,
        "European policy caps crop-based fuels and prioritises wastes and "
        "residues",
        note=(
            "A direct legislative response to the 2008 finding. It redirected "
            "the sector from crops towards used cooking oil, animal fats, "
            "residues and wastes, which is where the growth has since been."
        ),
    ),
    Milestone(
        2016,
        "A global market-based measure for international aviation emissions is "
        "agreed",
        note=(
            "Created durable demand for sustainable aviation fuel, and with it "
            "the field's strongest remaining case: aviation cannot electrify "
            "easily, so a liquid fuel that is not fossil is genuinely required "
            "rather than merely preferable."
        ),
    ),
    Milestone(
        2022,
        "Gas fermentation of industrial off-gas to ethanol reaches commercial "
        "operation",
        note=(
            "A feedstock that competes with nothing: carbon monoxide from steel "
            "and refinery exhaust that would otherwise be flared. It sidesteps "
            "the land argument entirely rather than answering it, which after "
            "the three setbacks above is a reasonable strategy."
        ),
    ),
)
