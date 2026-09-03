# =============================================================================
#  biotechnology.branches.white.biobased_chemicals.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record's principal setback is unusual in kind: an entire research
#  agenda was organised around a list, the list was scientifically sound, and
#  the commercial predictions drawn from it were wrong.
#
#  SUBTYPE-SPECIFIC NOTE
#  The timeline opens with a correction that matters. The chemical industry
#  BEGAN biobased. Ethanol, acetone, butanol, citric acid and glycerol were all
#  fermentation products before they were petrochemical ones, and the switch to
#  petroleum happened in the middle of the twentieth century on cost, not on
#  chemistry. This field is therefore not inventing something new. It is
#  reversing a substitution that already happened once, in the other direction,
#  against an incumbent that has since had seventy years to optimise.
#
#  Understanding that ordering explains the field's characteristic
#  disappointment. The petrochemical route is not the naive option; it is the
#  one that already won a competition on cost.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE INDUSTRY BEGAN HERE AND LEFT
    # =========================================================================
    Milestone(
        1916,
        "Acetone and butanol are produced industrially by fermentation",
        note=(
            "For a period this was the principal industrial route to both "
            "solvents. It was displaced by petrochemical production after the "
            "Second World War purely on cost, which is the substitution this "
            "entire record is attempting to reverse."
        ),
    ),
    Milestone(
        1923,
        "Citric acid fermentation displaces extraction from citrus fruit",
        note=(
            "A biobased chemical that won and stayed won, a century before the "
            "term existed. It succeeded because the alternative was "
            "agricultural extraction rather than petrochemistry, which is the "
            "condition under which this field has always done best."
        ),
    ),
    Milestone(
        1950,
        "Petrochemical feedstocks displace fermentation across the bulk "
        "chemical industry",
        note=(
            "Cheap and abundant oil made hydrocarbon routes cheaper for almost "
            "everything. Recording this as a milestone rather than as "
            "background is deliberate: the incumbent this record competes with "
            "is not a default, it is a previous winner."
        ),
    ),
    # =========================================================================
    #  THE FIELD IS DELIBERATELY RESTARTED
    # =========================================================================
    Milestone(
        1990,
        "Enzymatic acrylamide production replaces the copper catalysed route",
        note=(
            "One of the first modern demonstrations that a biological route "
            "could displace an established petrochemical one on merit rather "
            "than on subsidy. It succeeded because the enzyme avoided a "
            "catalyst separation and a by-product, not because it was "
            "biological."
        ),
    ),
    Milestone(
        2004,
        "A national laboratory publishes a list of top value-added chemicals "
        "from biomass",
        note=(
            "Twelve platform molecules identified as priorities for research "
            "funding. The chemistry was sound and the influence was enormous: "
            "it set the agenda for two decades of academic and industrial work "
            "and is the origin of the platform chemical framing used "
            "throughout this record."
        ),
    ),
    Milestone(
        2006,
        "Commercial production of 1,3-propanediol from glucose begins",
        note=(
            "A biobased monomer for a polyester fibre with properties differing "
            "from the petrochemical alternative. It is the field's clearest "
            "success and the reason is instructive: it competed on performance "
            "rather than on being renewable, and its target is oxygen-rich, so "
            "biology started most of the way there."
        ),
    ),
    Milestone(
        2009,
        "Bio-based monoethylene glycol enters large-scale use in beverage "
        "packaging",
        note=(
            "A drop-in molecule, chemically identical to its petrochemical "
            "equivalent, adopted because a consumer-facing brand was willing to "
            "pay for the attribute. It demonstrated both that drop-in "
            "substitution can work at scale and that it usually requires "
            "somebody downstream who cares."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A SOUND LIST AND A WRONG PREDICTION
    # =========================================================================
    Milestone(
        2012,
        "Four companies build commercial biobased succinic acid capacity",
        note=(
            "Succinic acid was among the most prominent platform molecules on "
            "the 2004 list. The chemistry was correct: it is oxygen-rich, "
            "fermentable at good yield, and a plausible route to many "
            "downstream products. Several plants were financed and built."
        ),
    ),
    Milestone(
        2019,
        "Most commercial biobased succinic acid capacity has been closed or "
        "sold",
        note=(
            "The plants ran. The downstream market did not appear. Derivative "
            "capacity that would have consumed the platform was never built, "
            "the incumbent maleic anhydride route stayed cheap, and oil prices "
            "fell during the scale-up window. Companies exited or entered "
            "insolvency. The lesson is precise and applies well beyond this "
            "molecule: BEING A GOOD CHEMICAL PLATFORM IS NOT THE SAME AS "
            "HAVING A MARKET, and a list of promising building blocks says "
            "nothing about whether anyone has built the capacity to consume "
            "them."
        ),
    ),
    # =========================================================================
    #  WHERE THE FIELD FOUND ITS FOOTING
    # =========================================================================
    Milestone(
        2013,
        "Commercial 1,4-butanediol production begins by a designed pathway",
        note=(
            "A route assembled from enzymes of unrelated organisms and present "
            "in no natural cell, producing an established commodity "
            "intermediate. Notable because it proved a designed pathway could "
            "reach commercial operation for a molecule with an existing market, "
            "which is the combination the succinic acid case lacked."
        ),
    ),
    Milestone(
        2016,
        "Fuel-oriented fermentation companies redirect to speciality and "
        "cosmetic ingredients",
        note=(
            "Producers of terpene hydrocarbons found that the same molecules "
            "commanded far higher prices as cosmetic ingredients than as fuel. "
            "It is recorded as a milestone rather than a retreat because it "
            "identified where fermentation actually competes: high value per "
            "tonne, modest volume, and a customer who cares about the "
            "attribute."
        ),
    ),
    Milestone(
        2021,
        "Regulatory attention turns to substantiating environmental claims",
        note=(
            "Rules against unsupported green marketing made an unverified "
            "biobased claim a liability rather than an asset. The effect on "
            "this record is direct: life cycle assessment and radiocarbon "
            "content moved from voluntary marketing support to evidentiary "
            "requirement."
        ),
    ),
    Milestone(
        2022,
        "Gas fermentation and carbon dioxide derived chemicals reach "
        "commercial operation",
        note=(
            "Chemical feedstock from steel mill off-gas rather than from a "
            "field, which removes the land argument rather than answering it. "
            "It is the most significant open direction in this record, and it "
            "reaches chemicals before fuels precisely because chemicals are "
            "worth more per tonne."
        ),
    ),
)
