# =============================================================================
#  biotechnology.branches.grey.biowaste_treatment.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THIS RECORD'S TIMELINE IS DRIVEN BY TAX POLICY MORE THAN BY SCIENCE, AND
#  PRETENDING OTHERWISE WOULD MISDESCRIBE IT.
#
#  The microbiology was essentially settled by the middle of the twentieth
#  century. Nothing discovered after that point explains why the sector grew.
#  What explains it is a sequence of policy decisions: a landfill directive
#  with diversion targets, a landfill tax, a renewable energy tariff. Where
#  those exist, plants are built. Where they lapse, plants close.
#
#      THE DEFINING EVENTS IN THIS RECORD ARE LEGISLATIVE.
#
#  That is unusual enough in this library to state plainly, and it is the
#  reason `governance.py` carries more weight here than in most records.
#
#  THE SETBACK IS ALSO NOT A TECHNICAL ONE. Germany's crop-fed digestion boom
#  worked exactly as designed and produced an outcome nobody intended: maize
#  grown deliberately to feed digesters, displacing food production and
#  concentrating maize in rotations. A subsidy aimed at waste treatment had
#  been claimed by an activity that was not waste treatment. It is the clearest
#  case in the branch of an incentive rewarding the measured thing rather than
#  the intended thing.
#
#  A SECOND SETBACK IS RECORDED FOR 2018: quality protocols had to be written
#  because digestate was carrying plastic on to farmland, which is a recycling
#  process functioning as a contamination pathway.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE CHEMISTRY, LONG BEFORE ANY APPLICATION
    # =========================================================================
    Milestone(
        1776,
        "Combustible gas is identified rising from decomposing matter in "
        "marshes",
        note=(
            "The observation that rotting organic material under water produces "
            "a flammable gas. It is the entire chemistry of this record, noticed "
            "two centuries before anyone built a vessel to exploit it, and it "
            "is the reason landfills emit methane whether or not anybody "
            "intends them to."
        ),
    ),
    Milestone(
        1895,
        "Gas from a covered sewage tank is used for street lighting",
        note=(
            "The first recorded deliberate use of biogas as a fuel. It "
            "established that the gas could be collected and burned usefully, "
            "and it happened at a sewage works, which is why this record and "
            "`grey.wastewater_treatment` share the same process."
        ),
    ),
    Milestone(
        1930,
        "The four-stage microbiology of anaerobic digestion is characterised",
        note=(
            "Hydrolysis, acidogenesis, acetogenesis and methanogenesis "
            "identified as sequential steps performed by different organisms "
            "with very different growth rates. This is the understanding that "
            "explains the characteristic overfeeding failure, and essentially "
            "nothing discovered after this point explains the sector's later "
            "growth."
        ),
    ),
    Milestone(
        1950,
        "Small-scale digesters are deployed widely in rural households in Asia",
        note=(
            "Simple unheated digesters producing cooking gas from manure and "
            "domestic waste, deployed in very large numbers. It is the largest "
            "count of digesters ever built and it is routinely omitted from "
            "accounts of the field, which tend to begin with industrial plants "
            "in Europe decades later."
        ),
    ),
    # =========================================================================
    #  THE ARCHAEA TURN OUT NOT TO BE BACTERIA
    # =========================================================================
    Milestone(
        1977,
        "Methanogens are recognised as archaea, a domain distinct from bacteria",
        note=(
            "The organisms performing the final and rate-limiting step of this "
            "process were found to belong to a separate domain of life. It "
            "reframed the digester community as an association between two "
            "domains rather than a bacterial consortium, and it is one of the "
            "few entries here that is a genuine scientific landmark rather than "
            "a policy event."
        ),
    ),
    # =========================================================================
    #  AND FROM HERE THE DRIVER IS LEGISLATION
    # =========================================================================
    Milestone(
        1999,
        "A landfill directive sets binding targets for diverting biodegradable "
        "waste from landfill",
        note=(
            "The decision that created the sector. Requiring member states to "
            "reduce the biodegradable waste sent to landfill gave organic waste "
            "a disposal cost, and a disposal cost is what makes a digester pay. "
            "Every subsequent entry in this timeline follows from it."
        ),
    ),
    Milestone(
        2000,
        "Renewable energy tariffs make crop-fed digestion commercially "
        "attractive in Germany",
        note=(
            "Guaranteed prices for electricity from biogas produced very rapid "
            "construction. The policy worked on its own terms and the sector "
            "grew faster here than anywhere, which is what makes the "
            "consequence below instructive rather than merely unfortunate."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE INCENTIVE REWARDED THE MEASURED THING
    # =========================================================================
    Milestone(
        2012,
        "Crop-fed digestion is found to be displacing food production, and "
        "support is restructured",
        note=(
            "Maize was being grown deliberately to feed digesters rather than "
            "people or livestock, concentrating maize in rotations and "
            "competing for farmland. A subsidy intended for waste treatment had "
            "been claimed by an activity that was not waste treatment, because "
            "the payment was made for the gas rather than for the diversion. "
            "Support was restructured toward waste and residue feedstock. It is "
            "the clearest case in this branch of an incentive rewarding what it "
            "measured instead of what it intended."
        ),
    ),
    # =========================================================================
    #  UPGRADING CHANGES WHAT THE PRODUCT IS
    # =========================================================================
    Milestone(
        2010,
        "Biomethane upgrading and gas grid injection reach commercial scale",
        note=(
            "Removing carbon dioxide to produce gas of natural gas quality "
            "turned biogas from a site-bound fuel into a tradeable commodity "
            "and solved the wasted-heat problem for plants with a grid "
            "connection. It changed what a digester is for, from generating "
            "electricity on site to supplying a network."
        ),
    ),
    Milestone(
        2015,
        "Separate food waste collection becomes mandatory in a growing number "
        "of jurisdictions",
        note=(
            "The policy that determines feedstock quality, and therefore plant "
            "performance, more reliably than any process variable. It is "
            "recorded as a technical milestone because a decision about kitchen "
            "caddies governs what a digester can achieve, which is an "
            "uncomfortable and accurate thing for a process discipline to admit."
        ),
    ),
    # =========================================================================
    #  THE SECOND SETBACK: RECYCLING AS A CONTAMINATION PATHWAY
    # =========================================================================
    Milestone(
        2018,
        "Digestate quality protocols are tightened after plastic contamination "
        "is documented on agricultural land",
        note=(
            "Plastic entering with packaged and poorly separated food waste "
            "passed through the process and was spread on fields with the "
            "digestate. A route intended as nutrient recycling was delivering "
            "microplastic to soil. Quality protocols set limits on physical "
            "contaminants, which raised the cost of accepting mixed feedstock "
            "and made source separation an economic necessity as well as a good "
            "idea."
        ),
    ),
    # =========================================================================
    #  MEASURING WHAT THE SECTOR HAD BEEN ASSUMING
    # =========================================================================
    Milestone(
        2020,
        "Methane leakage measurement campaigns find emissions higher than "
        "reported at operating plants",
        note=(
            "Direct measurement at working sites found losses from vessels, "
            "storage and upgrading exceeding the assumed values used in "
            "reporting. Because methane is a far stronger greenhouse gas than "
            "the carbon dioxide from burning it, a small percentage loss "
            "cancels a large share of the benefit. The sector's headline "
            "climate figures had rested on an estimate, and measuring it "
            "remains the exception rather than the rule."
        ),
    ),
)
