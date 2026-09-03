# =============================================================================
#  biotechnology.branches.blue.algal_biotechnology.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two of the same kind separated by twenty-five years,
#  which is what makes them worth recording together.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIELD MADE THE SAME MISTAKE TWICE. A national algal fuel programme ran
#  from 1978 to 1996 and concluded, in a final report that is unusually candid,
#  that the approach could not compete at prevailing oil prices. That
#  conclusion was published and available.
#
#  Roughly a decade later a second and much larger wave of algal fuel
#  investment began, against projections that extrapolated laboratory
#  productivity to open systems in the way the earlier programme had already
#  shown to be unsound. It ended the same way, and most of the companies
#  redirected to the high-value products this record is otherwise about.
#
#  Recording both is more useful than recording either, because the pattern is
#  the lesson: the constraint was known, documented and ignored, and it was
#  ignored because the biology genuinely is impressive and the harvest problem
#  is unglamorous.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  EATEN LONG BEFORE IT WAS CULTIVATED
    # =========================================================================
    Milestone(
        1940,
        "Spirulina is recorded as a traditional food harvested from alkaline "
        "lakes",
        note=(
            "Harvested and eaten around Lake Chad and, historically, from the "
            "lakes of the Valley of Mexico. It is included because it "
            "establishes that the successful organisms in this record were "
            "food before they were biotechnology, and because both grow at a "
            "high pH that few competitors tolerate."
        ),
    ),
    Milestone(
        1952,
        "Systematic mass culture of Chlorella is investigated as a protein "
        "source",
        note=(
            "Post-war interest in feeding a growing population. The "
            "productivity was real and the processing cost was not solved, "
            "which is the first appearance of this record's permanent theme."
        ),
    ),
    # =========================================================================
    #  THE COMMERCIAL SUCCESSES, ALL AT HIGH VALUE
    # =========================================================================
    Milestone(
        1970,
        "Commercial Spirulina production begins",
        note=(
            "Sold as a nutritional supplement rather than as bulk protein, "
            "which is the pattern every subsequent success follows: the product "
            "carries a price that the harvest cost does not overwhelm."
        ),
    ),
    Milestone(
        1985,
        "Commercial beta-carotene production from Dunaliella in hypersaline "
        "ponds",
        note=(
            "The organism tolerates salinity that excludes almost everything "
            "else, so an open pond becomes a selective environment rather than "
            "an invitation to contamination. It is the clearest demonstration "
            "that successful open-pond species are those with a chemical moat."
        ),
    ),
    # =========================================================================
    #  THE FIRST SETBACK, AND ITS UNUSUALLY HONEST CONCLUSION
    # =========================================================================
    Milestone(
        1978,
        "A national programme on algae for fuel begins",
        note=(
            "Prompted by the oil shocks. It ran for nearly two decades, "
            "screened thousands of strains, and built and operated outdoor test "
            "facilities rather than working only in the laboratory."
        ),
    ),
    Milestone(
        1996,
        "The programme closes and its final report concludes that algal fuel "
        "cannot compete at prevailing oil prices",
        note=(
            "The report is unusually candid and remains worth reading. It "
            "identified the constraints that this record still records: low "
            "culture density, harvest and dewatering cost, contamination of "
            "open systems, and the gap between laboratory and outdoor "
            "productivity. It is recorded as a setback whose value was the "
            "documentation it left, and the next entries show what happened to "
            "that documentation."
        ),
    ),
    # =========================================================================
    #  THE SECOND SETBACK: THE SAME MISTAKE, LARGER
    # =========================================================================
    Milestone(
        2008,
        "A second and much larger wave of algal fuel investment begins",
        note=(
            "Substantial public and private funding followed projections built "
            "by extrapolating short-term laboratory productivity to sustained "
            "outdoor operation, which the 1996 report had already shown to be "
            "unsound. High oil prices and climate concern supplied the "
            "motivation, and the earlier findings were available and largely "
            "unused."
        ),
    ),
    Milestone(
        2014,
        "Algal fuel companies redirect towards nutritional, cosmetic and "
        "speciality products",
        note=(
            "The pivot was rational rather than a failure of nerve: the same "
            "organisms, ponds and harvesting equipment produce a compound worth "
            "tens of thousands of euro a tonne just as readily as one worth a "
            "few hundred, and only the former repays the harvest cost. Several "
            "of the companies became profitable after redirecting. It is "
            "recorded as the resolution of the setback rather than as its "
            "continuation."
        ),
    ),
    # =========================================================================
    #  WHERE THE FIELD ACTUALLY WENT
    # =========================================================================
    Milestone(
        2000,
        "Commercial astaxanthin production from Haematococcus establishes "
        "photobioreactors as economically viable",
        note=(
            "A fragile, slow-growing organism producing a very valuable "
            "pigment, which is exactly the combination that justifies closed "
            "cultivation. It demonstrated that the capital cost of a "
            "photobioreactor is affordable when the product carries it."
        ),
    ),
    Milestone(
        2010,
        "Algal long-chain omega-3 oils reach the market, including use in "
        "infant formula",
        note=(
            "Producing the compound directly rather than through the fish that "
            "concentrate it. Much of this production is heterotrophic, grown in "
            "the dark on sugar in conventional fermenters, which sidesteps both "
            "light limitation and low density and is a quiet admission about "
            "where the difficulty lay."
        ),
    ),
    Milestone(
        2016,
        "Genome editing becomes routine in model microalgae",
        note=(
            "Targeted modification of lipid metabolism, photosynthetic antenna "
            "size and product accumulation. It addresses the biology, which was "
            "never the binding constraint, and the harvest problem it does not "
            "touch remains where it was."
        ),
    ),
    Milestone(
        2021,
        "Coupling of algal cultivation to wastewater treatment and industrial "
        "carbon dioxide reaches commercial operation",
        note=(
            "The economics invert favourably when somebody pays for the "
            "treatment or the capture and the biomass is a by-product rather "
            "than the product. It is the most promising direction for low-value "
            "applications precisely because it stops asking the biomass to "
            "carry the cost."
        ),
    ),
)
