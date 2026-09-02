# =============================================================================
#  biotechnology.branches.green.agricultural_genome_editing.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The setback in this timeline is not a laboratory failure. It is the 2018
#  Court of Justice ruling, which is recorded as a setback for the field
#  without any implication that the court decided wrongly. The court was asked
#  to interpret a 2001 directive written before the technology existed, and it
#  did so consistently: mutagenesis techniques that had not been in use with a
#  long safety record in 2001 fall inside the GMO regime.
#
#  The consequence for European public-sector plant breeding was severe, and
#  the consequence for the coherence of the law is a live argument that the
#  European Commission's 2023 proposal exists to resolve. Both facts are
#  recorded; neither is adjudicated here.
#
#  Rule 3 also applies: programmable nucleases were developed by several groups
#  and the 2012 Jinek paper sits among closely contemporaneous work. The entry
#  says so.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  PROGRAMMABLE CUTTING, BEFORE IT WAS EASY
    # =========================================================================
    Milestone(
        1996,
        "Zinc finger nucleases demonstrated as programmable DNA cutters",
        note=(
            "Targeting required protein engineering for every new site, which "
            "took months and often failed. The idea was right and the "
            "ergonomics were prohibitive."
        ),
    ),
    Milestone(
        2011,
        "TALEN editing applied to rice bacterial blight resistance",
        note=(
            "Easier to design than zinc fingers and still one protein per "
            "target. The first genome-edited disease resistance in a crop."
        ),
    ),
    # =========================================================================
    #  THE TOOL THAT CHANGED THE ECONOMICS
    # =========================================================================
    Milestone(
        2012,
        "CRISPR-Cas9 described as a programmable RNA-guided DNA endonuclease",
        note=(
            "Targeting became a matter of ordering a short RNA rather than "
            "engineering a protein. Several groups reached adjacent results "
            "within months, and the plant applications followed within a year. "
            "The change was in cost and speed, not in what was possible."
        ),
    ),
    Milestone(
        2013,
        "CRISPR editing demonstrated in rice, wheat and Arabidopsis",
    ),
    # =========================================================================
    #  THE FIRST REGULATORY ANSWERS, AND THEY DISAGREE
    # =========================================================================
    Milestone(
        2015,
        "Argentina issues Resolution 173/2015, the first framework written "
        "specifically for new breeding techniques",
        note=(
            "A case-by-case determination of whether a novel combination of "
            "genetic material is present. If not, the product is handled as "
            "conventional. Several Latin American countries adopted the same "
            "approach."
        ),
    ),
    Milestone(
        2016,
        "A non-browning mushroom is cleared without regulation in the United "
        "States",
        note=(
            "A knockout of a polyphenol oxidase gene, containing no foreign "
            "DNA. USDA APHIS concluded it fell outside its jurisdiction because "
            "no plant pest was involved. The first edited organism to reach "
            "that answer anywhere."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A COURT READS A DIRECTIVE WRITTEN BEFORE THE TECHNOLOGY
    # =========================================================================
    Milestone(
        2018,
        "The Court of Justice of the European Union rules that organisms from "
        "directed mutagenesis fall under the GMO Directive",
        note=(
            "Case C-528/16. The court interpreted Directive 2001/18/EC as "
            "written: the exemption for mutagenesis covers techniques with a "
            "long safety record of use, and directed mutagenesis is not among "
            "them. Legally coherent, and it placed a four-base deletion under "
            "the same regime as a transgene. European public-sector breeding "
            "programmes shut down or relocated. Recorded as a setback for the "
            "field without implying the court decided wrongly."
        ),
    ),
    # =========================================================================
    #  DEPLOYMENT ELSEWHERE
    # =========================================================================
    Milestone(
        2016,
        "PRRS-resistant pigs produced by editing the CD163 receptor",
        note=(
            "The animals cannot be infected by a virus that kills millions of "
            "pigs a year. A welfare, economic and antimicrobial argument in one "
            "edit, and still awaiting approval in most jurisdictions."
        ),
    ),
    Milestone(
        2019,
        "Japan establishes a notification pathway for edits leaving no foreign "
        "DNA",
        note=(
            "Developers notify the authorities and supply information; no "
            "premarket approval is required where no foreign DNA remains."
        ),
    ),
    Milestone(
        2021,
        "High-GABA tomato goes on sale in Japan",
        note=(
            "The first edited food sold to consumers anywhere, and notable for "
            "carrying a consumer-facing health claim rather than an agronomic "
            "trait, which is the opposite of how transgenic crops were "
            "introduced."
        ),
    ),
    Milestone(
        2022,
        "England legislates for precision breeding, separating edited organisms "
        "from the retained GMO regime",
    ),
    # =========================================================================
    #  THE ATTEMPT TO RESOLVE THE DIVERGENCE
    # =========================================================================
    Milestone(
        2023,
        "The European Commission proposes a separate category for plants "
        "obtained by new genomic techniques",
        note=(
            "A proposal to treat edits that could have arisen conventionally "
            "differently from transgenesis, four and a half years after the "
            "court ruling that made the question urgent."
        ),
    ),
)
