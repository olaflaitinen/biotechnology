# =============================================================================
#  biotechnology.branches.red.pharmaceutical_biotechnology.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules for milestones: see `red/gene_therapy/history.py`.
#  Rule 1 in particular - include the setbacks - is honoured below by the 1985
#  entry, which is the reason the entire industry abandoned human-derived
#  starting material.
#
#  SUBTYPE-SPECIFIC NOTE
#  This timeline is also, in effect, the founding timeline of the modern
#  biotechnology industry as a commercial sector. The 1980 Diamond v.
#  Chakrabarty decision and the 1980 Bayh-Dole Act are included even though
#  neither is a laboratory result, because without them the venture financing
#  that built the sector would not have existed.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  PRE-RECOMBINANT ERA - extraction from animals
    # =========================================================================
    Milestone(
        1922,
        "Insulin extracted from animal pancreas is first used to treat a patient",
        note=(
            "For sixty years insulin was harvested from slaughterhouse "
            "material: roughly two tonnes of pancreas per kilogram of "
            "insulin, with supply tied to meat production."
        ),
    ),
    # =========================================================================
    #  THE ENABLING SCIENCE
    # =========================================================================
    Milestone(
        1973,
        "Cohen and Boyer demonstrate recombinant DNA in bacteria",
        note="The single experiment from which the entire industry descends.",
    ),
    Milestone(
        1975,
        "Asilomar conference agrees voluntary safety guidelines for recombinant DNA",
        note=(
            "Scientists paused their own field and wrote the containment "
            "rules themselves. It remains the standard example cited whenever "
            "self-governance of a new technology is proposed."
        ),
    ),
    Milestone(
        1978,
        "Human insulin gene expressed in Escherichia coli",
    ),
    # =========================================================================
    #  THE LEGAL AND FINANCIAL FOUNDATIONS
    # =========================================================================
    Milestone(
        1980,
        "Diamond v. Chakrabarty establishes that living organisms may be patented",
        note=(
            "Not a laboratory result, but the decision that made venture "
            "investment in biotechnology rational."
        ),
    ),
    Milestone(
        1980,
        "Bayh-Dole Act allows universities to patent federally funded inventions",
        note="The mechanism by which academic discoveries became companies.",
    ),
    # =========================================================================
    #  PRODUCTS
    # =========================================================================
    Milestone(
        1982,
        "Humulin approved: the first recombinant medicine anywhere",
        note=(
            "Approved in under two years, faster than most conventional drugs "
            "of the period, because the molecule was already well understood."
        ),
    ),
    Milestone(
        1985,
        "Growth hormone from human pituitary extract withdrawn after "
        "Creutzfeldt-Jakob transmission",
        note=(
            "The setback that ended human-derived starting material as an "
            "acceptable practice, and made recombinant production not merely "
            "cheaper but ethically obligatory."
        ),
    ),
    Milestone(
        1986,
        "Muromonab-CD3 approved: the first therapeutic monoclonal antibody",
    ),
    Milestone(
        1997,
        "Rituximab approved, establishing antibodies as a mainstream modality",
    ),
    # =========================================================================
    #  THE COPY MARKET AND MODERN MANUFACTURE
    # =========================================================================
    Milestone(
        2006,
        "European Union creates the first biosimilar regulatory pathway",
        note=(
            "Europe led the world by roughly nine years, and the resulting "
            "price competition is why several biologics are affordable in EU "
            "health systems and not elsewhere."
        ),
    ),
    Milestone(
        2015,
        "First biosimilar approved in the United States",
    ),
    Milestone(
        2021,
        "Single-use and continuous processing reach routine commercial scale",
        note=(
            "Stainless steel plants costing hundreds of millions gave way to "
            "modular single-use facilities buildable in eighteen months, "
            "which changed who can enter the industry."
        ),
    ),
)
