# =============================================================================
#  biotechnology.branches.white.cell_free_biomanufacturing.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record's is of an unusual kind: not a failure but a persistent
#  overstatement. Cell-free manufacturing has been described as imminent for
#  half a century, and the honest entry records the gap between the claim and
#  the market rather than any single collapse.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two entries in this timeline are among the most important experiments in the
#  history of biology, and neither was performed in order to manufacture
#  anything.
#
#  Buchner in 1897 showed that fermentation happens without a living cell,
#  which ended vitalism and made the whole idea of biological chemistry outside
#  an organism thinkable. Nirenberg and Matthaei in 1961 used a cell-free
#  extract to crack the genetic code, and they chose the format precisely
#  because a tube can be given a defined instruction and a cell cannot.
#
#  This record's technique was therefore the instrument of two foundational
#  discoveries long before anyone proposed it as a production platform, and
#  that ordering is worth noticing: it explains why the method is so mature
#  scientifically and so immature commercially.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE EXPERIMENT THAT MADE THE IDEA POSSIBLE
    # =========================================================================
    Milestone(
        1897,
        "Buchner shows that cell-free yeast extract ferments sugar",
        note=(
            "The founding experiment of this record and of the branch. "
            "Fermentation had been held to require an intact living cell; it "
            "did not. Everything here follows from the demonstration that "
            "biological chemistry survives the death of the organism."
        ),
    ),
    # =========================================================================
    #  THE EXPERIMENT THAT USED IT TO READ THE GENETIC CODE
    # =========================================================================
    Milestone(
        1961,
        "Nirenberg and Matthaei crack the first codon using a cell-free "
        "extract",
        note=(
            "A synthetic RNA of a single repeated base was added to a bacterial "
            "extract, and the extract made a protein of a single repeated amino "
            "acid. The format was chosen precisely because a tube accepts a "
            "defined instruction and a living cell does not. It is the single "
            "most consequential cell-free experiment ever performed, and it was "
            "an experiment in reading rather than in making."
        ),
    ),
    # =========================================================================
    #  MAKING THE REACTION LAST LONGER
    # =========================================================================
    Milestone(
        1988,
        "Continuous-flow cell-free synthesis extends reactions from minutes to "
        "many hours",
        note=(
            "Feeding substrates and removing inhibitory by-products across a "
            "membrane addressed the fundamental limit of a batch reaction. It "
            "was the moment cell-free synthesis became conceivable as "
            "production rather than only as assay, and it is the ancestor of "
            "every continuous exchange format in `practice.TECHNOLOGIES`."
        ),
    ),
    # =========================================================================
    #  DEFINING EXACTLY WHAT IS SUFFICIENT
    # =========================================================================
    Milestone(
        2001,
        "A fully reconstituted translation system is assembled from purified "
        "components",
        note=(
            "Protein synthesis rebuilt from individually purified parts, "
            "containing nothing that was not deliberately added. It answered "
            "the question of what is sufficient for translation, and it created "
            "the clean, defined, expensive and much less productive alternative "
            "to crude extract that the field has used ever since for questions "
            "rather than for products."
        ),
    ),
    # =========================================================================
    #  MAKING IT AFFORDABLE ENOUGH TO USE
    # =========================================================================
    Milestone(
        2004,
        "Glucose-based energy regeneration replaces phosphorylated energy "
        "substrates",
        note=(
            "Coupling the reaction to residual glycolysis in the crude extract "
            "cut the dominant cost of cell-free synthesis by a large factor. It "
            "is the reason crude extracts rather than reconstituted systems are "
            "used wherever the object is to make something, and it remains the "
            "largest single cost reduction the field has achieved."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: IMMINENT FOR FIFTY YEARS
    # =========================================================================
    Milestone(
        2010,
        "Cell-free manufacturing remains a small share of biological "
        "production despite four decades of expectation",
        note=(
            "Recorded as a setback because the pattern is real and instructive. "
            "The technology has been described as about to displace "
            "fermentation since the 1970s, and it has not, for reasons that are "
            "structural rather than solvable: the substrates are bought rather "
            "than grown, the catalyst is consumed rather than reproducing, and "
            "the extract must itself be made from cultured cells. The correct "
            "conclusion is not that the field failed but that its advantages "
            "are speed, access and portability rather than cost, and that "
            "twenty years of claims to the contrary damaged its credibility "
            "with people who would otherwise have adopted it."
        ),
    ),
    # =========================================================================
    #  THE APPLICATION THAT WAS GENUINELY NEW
    # =========================================================================
    Milestone(
        2014,
        "Complete cell-free reactions are freeze-dried onto paper and "
        "reactivated with water",
        note=(
            "A synthetic gene circuit stored at ambient temperature on a paper "
            "disc, functional after months, started by adding a drop of liquid. "
            "It converted a biological process into a shelf-stable reagent and "
            "created an application that fermentation cannot address at all, "
            "which is the first time the field had one."
        ),
    ),
    Milestone(
        2016,
        "Paper-based cell-free sensors are demonstrated against an outbreak "
        "pathogen in the field",
        note=(
            "Sequence-specific detection with a visible colour change, without "
            "a laboratory, a cold chain or mains power, coupled to isothermal "
            "amplification for sensitivity. It is the clearest justification "
            "for this record's SDG 3 claim and the reason its `governance.py` "
            "must consider deployment outside laboratories."
        ),
    ),
    # =========================================================================
    #  WHERE IT IS GOING
    # =========================================================================
    Milestone(
        2018,
        "Freeze-dried cell-free kits enter classroom use",
        note=(
            "Protein expression made visible without a containment laboratory, "
            "because there is no living modified organism to contain. A "
            "teaching advantage rather than a manufacturing one, and a concrete "
            "illustration of the governance asymmetry recorded in this record."
        ),
    ),
    Milestone(
        2020,
        "On-demand production of biologics from stored templates is "
        "demonstrated at the point of care",
        note=(
            "Storing an instruction rather than a product, and manufacturing "
            "when needed. It addresses cold chain and shelf life rather than "
            "cost, which is consistent with everything else this record has "
            "learned about where the technology actually wins."
        ),
    ),
    Milestone(
        2022,
        "Cell-free glycoprotein synthesis with defined glycans is demonstrated",
        note=(
            "Adding the modification enzymes to the reaction rather than "
            "inheriting whatever a host cell line happens to do. It attacks the "
            "one capability gap that bacterial extracts had, and it does so by "
            "the same open-reaction argument that runs through the whole "
            "record."
        ),
    ),
)
