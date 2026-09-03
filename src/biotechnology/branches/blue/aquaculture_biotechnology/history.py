# =============================================================================
#  biotechnology.branches.blue.aquaculture_biotechnology.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has three of different kinds: an environmental one, a
#  disease one, and a regulatory one in which a technology worked and was not
#  permitted to be used.
#
#  SUBTYPE-SPECIFIC NOTE
#  The 1979 and 2010 entries are the pair worth reading together, because they
#  are the same lesson from opposite directions.
#
#  Vaccination against furunculosis and vibriosis, developed and adopted
#  through the 1980s and 1990s, took salmon farming from heavy antibiotic use
#  to almost none. It is the clearest success in this record and it happened
#  because a vaccine existed for the pathogen that mattered.
#
#  Sea lice went the other way. There is no comparably effective vaccine, so
#  control depended on chemicals, and resistance removed each option in turn.
#  The industry ended up with thermal and mechanical delousing, which works and
#  which injures fish. Where a vaccine existed the problem was solved; where
#  one did not, thirty years of chemistry produced resistance and a welfare
#  cost.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  ANCIENT PRACTICE, RECENT SCIENCE
    # =========================================================================
    Milestone(
        -2000,
        "Carp culture is practised in China",
        note=(
            "Aquaculture is among the oldest forms of animal husbandry, and "
            "carp remains one of the largest farmed tonnages in the world. It "
            "is recorded to make clear that this record documents the "
            "biotechnology of a very old activity rather than the activity "
            "itself."
        ),
    ),
    Milestone(
        1971,
        "Systematic family-based selective breeding of Atlantic salmon begins "
        "in Norway",
        note=(
            "The start of genuine domestication. Because these animals were "
            "essentially wild in 1971, the gains available were enormous, and "
            "the programme has delivered improvements per generation well above "
            "anything achieved in terrestrial livestock. Salmon is a domestic "
            "animal younger than most of the people reading this."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: WHAT THE INDUSTRY DID TO THE COAST
    # =========================================================================
    Milestone(
        1979,
        "Rapid expansion of shrimp farming begins, driving extensive mangrove "
        "clearance",
        note=(
            "Ponds were cut into mangrove forest across South and Southeast "
            "Asia and Latin America. The habitat lost was nursery ground for "
            "wild fisheries and physical protection for the coast behind it, so "
            "the damage extended well past the ecosystem itself. Many ponds "
            "were then abandoned within a decade as disease and soil "
            "acidification accumulated, which left the coast without either the "
            "mangroves or the industry."
        ),
    ),
    # =========================================================================
    #  THE SUCCESS: A VACCINE EXISTED
    # =========================================================================
    Milestone(
        1988,
        "Oil-adjuvanted injectable vaccines against furunculosis and vibriosis "
        "enter routine use in salmon farming",
        note=(
            "Antibiotic use in Norwegian salmon production fell to a very small "
            "fraction of its former level within a few years, while production "
            "continued to grow. It is among the clearest demonstrations "
            "anywhere in this library that vaccination is an antimicrobial "
            "resistance intervention, and it is the same argument "
            "`green.veterinary_vaccines` makes at length."
        ),
    ),
    # =========================================================================
    #  THE FEED PROBLEM, AND THE RESPONSE
    # =========================================================================
    Milestone(
        1997,
        "The demand of farmed carnivorous fish on wild fish stocks becomes a "
        "central criticism of the sector",
        note=(
            "The objection was that an industry presented as relieving pressure "
            "on wild fisheries was consuming them through feed. It was well "
            "founded at the time and it drove two decades of reformulation "
            "towards plant proteins, trimmings and, later, algal oils."
        ),
    ),
    Milestone(
        2014,
        "Aquaculture production overtakes capture fisheries as the source of "
        "fish for human consumption",
        note=(
            "A reversal of very long standing, and it passed with little public "
            "notice. Most seafood now reaches a plate by farming rather than "
            "fishing, which changes what questions about seafood are actually "
            "about."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: WHERE NO VACCINE EXISTED
    # =========================================================================
    Milestone(
        2010,
        "Sea lice resistance to successive chemical treatments becomes "
        "widespread",
        note=(
            "Each chemical class in turn lost effectiveness as resistance "
            "spread, in a sequence familiar from every other field where a "
            "single control agent is applied at scale. The industry moved to "
            "thermal and mechanical delousing and to cleaner fish, which avoid "
            "chemical residues and impose their own welfare costs on both the "
            "salmon and the cleaner fish. Read against the 1988 entry, the "
            "lesson is direct: where a vaccine existed the problem was solved, "
            "and where one did not, thirty years of chemistry produced "
            "resistance."
        ),
    ),
    Milestone(
        2008,
        "Mass mortality events from a herpesvirus devastate oyster production "
        "in Europe",
        note=(
            "Very high juvenile mortality across producing regions. The durable "
            "response was breeding for resistance rather than treatment, since "
            "a filter-feeding animal in open water cannot be medicated, and "
            "resistant stocks are now the basis of production in affected "
            "areas."
        ),
    ),
    # =========================================================================
    #  GENOMICS ARRIVES, AND THEN MEETS REGULATION
    # =========================================================================
    Milestone(
        2015,
        "Genomic selection becomes standard in major aquaculture breeding "
        "programmes",
        note=(
            "Applied faster here than in most terrestrial livestock, because "
            "enormous family sizes make the statistics favourable and because "
            "disease resistance, which is difficult to select for by "
            "observation, is exactly what genomic prediction handles well."
        ),
    ),
    Milestone(
        2015,
        "A fast-growing genetically modified salmon is approved for food after "
        "roughly two decades of review",
        note=(
            "Recorded as a setback of the regulatory kind. The technical work "
            "was completed in the early 1990s and approval took about twenty "
            "years, followed by further delays over labelling and by limited "
            "market acceptance. Whatever one concludes about the product, a "
            "twenty-year review is a statement about the regulatory system "
            "rather than about the fish, and it deterred investment in the "
            "whole area for a generation."
        ),
    ),
    Milestone(
        2018,
        "Genome editing for disease resistance is demonstrated in farmed "
        "species",
        note=(
            "Resistance to viral disease shown in more than one species. "
            "Deployment is constrained by regulatory classification rather than "
            "by technique, which is the same position "
            "`green.agricultural_genome_editing` records for crops and with the "
            "same unresolved divergence between jurisdictions."
        ),
    ),
    Milestone(
        2020,
        "Land-based recirculating aquaculture reaches commercial scale for "
        "salmon",
        note=(
            "Closing the system removes escape, sea lice exchange and effluent "
            "discharge at once, which addresses most of this record's "
            "challenges simultaneously. It costs a great deal in capital and "
            "energy, and several early ventures failed, so it is recorded as a "
            "real but unsettled direction rather than as the answer."
        ),
    ),
)
