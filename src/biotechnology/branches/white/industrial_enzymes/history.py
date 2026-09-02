# =============================================================================
#  biotechnology.branches.white.industrial_enzymes.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks;
#  the setback here is 1969, and it is a serious one that permanently changed
#  how the products are made.
#
#  SUBTYPE-SPECIFIC NOTE
#  Two threads run through this timeline and are worth watching separately.
#
#  THE FIRST is that this field repeatedly proved general scientific points as
#  a side effect of commercial work. Buchner's 1897 cell-free extract ended
#  vitalism. Sumner's 1926 urease crystals ended the argument about whether
#  enzymes are proteins. Neither man set out to settle a philosophical
#  question.
#
#  THE SECOND is that engineering ran ahead of theory. Directed evolution in
#  1993 improved enzymes without any understanding of why the improvements
#  worked, and it remains more reliable than rational design for most targets.
#  The 2018 Nobel citation is explicit that the method succeeds by copying
#  evolution rather than by out-thinking it.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  ESTABLISHING WHAT AN ENZYME IS
    # =========================================================================
    Milestone(
        1833,
        "Payen and Persoz isolate diastase from malt",
        note=(
            "The first enzyme preparation obtained from a living source and "
            "used deliberately. The suffix -ase in every enzyme name since "
            "comes from this one."
        ),
    ),
    Milestone(
        1897,
        "Buchner shows that cell-free yeast extract still ferments sugar",
        note=(
            "Fermentation had been held to require an intact living cell. It "
            "did not. This single experiment separated biochemistry from "
            "vitalism and made the whole idea of a purified industrial catalyst "
            "thinkable."
        ),
    ),
    Milestone(
        1913,
        "Michaelis and Menten publish the kinetic treatment of enzyme action",
        note=(
            "The equation still used to characterise every enzyme in this "
            "record, and the source of both k_cat and K_M in `metrics.py`."
        ),
    ),
    Milestone(
        1926,
        "Sumner crystallises urease and demonstrates that enzymes are proteins",
        note=(
            "Disputed for years afterwards, because the prevailing view held "
            "that proteins were merely carriers for some smaller active "
            "principle. Establishing that the protein IS the catalyst is what "
            "made protein engineering conceivable."
        ),
    ),
    # =========================================================================
    #  THE FIRST INDUSTRIAL USES
    # =========================================================================
    Milestone(
        1913,
        "Rohm patents a laundry product containing pancreatic enzymes",
        note=(
            "Sold as Burnus. Commercially modest and technically premature, "
            "because pancreatic enzymes are unstable in an alkaline detergent, "
            "but it is the origin of what is now the largest enzyme market."
        ),
    ),
    Milestone(
        1960,
        "Bacterial alkaline proteases are introduced into detergents",
        note=(
            "The key difference from 1913: a protease from an alkaliphilic "
            "Bacillus survives detergent conditions. Sourcing the enzyme from "
            "an organism that already lives in similar conditions is the "
            "oldest heuristic in the field and still works."
        ),
    ),
    # =========================================================================
    #  THE SETBACK
    # =========================================================================
    Milestone(
        1969,
        "Occupational asthma among detergent factory workers halts the enzyme "
        "detergent boom",
        note=(
            "Inhaled enzyme dust is a respiratory sensitiser. Workers and, in "
            "some reports, consumers developed allergic reactions, sales "
            "collapsed, and the industry very nearly ended. The response was "
            "encapsulation and granulation of every enzyme product, which is "
            "why detergent enzymes are sold as coated granules today. It is "
            "recorded here because it is the clearest case in the branch of a "
            "safety failure that a formulation change solved, and because the "
            "hazard is real rather than historical."
        ),
    ),
    # =========================================================================
    #  MAKING THE CATALYST REUSABLE AND MAKING IT RECOMBINANT
    # =========================================================================
    Milestone(
        1973,
        "Immobilised glucose isomerase enters commercial high fructose syrup "
        "production",
        note=(
            "The demonstration that immobilisation transforms the economics. "
            "The same catalyst bed runs for months, dividing the enzyme cost by "
            "the number of reuses, and this remains the largest immobilised "
            "enzyme process in the world."
        ),
    ),
    Milestone(
        1988,
        "Fermentation-produced chymosin is approved for cheesemaking",
        note=(
            "Among the first recombinant products accepted into the food "
            "supply, and it replaced an enzyme previously extracted from the "
            "stomachs of slaughtered calves. It attracted little of the "
            "opposition later directed at genetically modified crops, largely "
            "because the enzyme itself is purified away from the organism."
        ),
    ),
    # =========================================================================
    #  ENGINEERING WITHOUT UNDERSTANDING
    # =========================================================================
    Milestone(
        1993,
        "Directed evolution of enzymes is demonstrated",
        note=(
            "Iterated random mutagenesis and screening improved enzymes without "
            "any mechanistic understanding of why the mutations helped. It "
            "worked better than rational design did then, and for many targets "
            "it still does. The field's central method is an admission that "
            "protein theory is incomplete."
        ),
    ),
    Milestone(
        2003,
        "Enzymatic bleaching and biopolishing become standard in pulp and "
        "textile processing",
        note=(
            "Adopted because it reduced chlorine chemistry and effluent load, "
            "which is a regulatory cost as much as an environmental one. Most "
            "industrial enzyme adoption has this shape: an environmental "
            "improvement that pays for itself."
        ),
    ),
    Milestone(
        2010,
        "Computationally designed enzymes for reactions with no natural "
        "counterpart are reported",
        note=(
            "The designs worked but were orders of magnitude slower than "
            "natural enzymes, and required directed evolution afterwards to "
            "become useful. Recorded honestly: design supplies the starting "
            "point, evolution still supplies the performance."
        ),
    ),
    Milestone(
        2018,
        "The Nobel Prize in Chemistry is awarded for directed evolution of "
        "enzymes and for phage display",
        note=(
            "The citation is explicit that the method succeeds by imitating "
            "evolution rather than by out-thinking it, which is an unusual "
            "thing for a chemistry prize to say."
        ),
    ),
    Milestone(
        2021,
        "Deep learning structure prediction becomes routinely available for "
        "enzyme engineering",
        note=(
            "A predicted structure for any sequence removes the "
            "crystallography bottleneck from semi-rational design. It does not "
            "predict activity, stability or the effect of a mutation, so the "
            "screening step in `practice.CHALLENGES` remains the limit."
        ),
    ),
)
