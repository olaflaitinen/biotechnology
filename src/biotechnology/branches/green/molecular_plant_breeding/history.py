# =============================================================================
#  biotechnology.branches.green.molecular_plant_breeding.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks.
#  This field's setback is unusual and is recorded in the 1990s entry: two
#  decades of quantitative trait locus mapping produced a large literature and
#  very few varieties, because the method was answering a question breeders had
#  not asked.
#
#  SUBTYPE-SPECIFIC NOTE
#  The oldest entry in this record predates genetics itself, and that is the
#  point. Selection has been practised for ten thousand years; Mendel explained
#  why it works; Fisher and Lush made it quantitative; markers made it fast.
#  Nothing in this timeline changes what a plant is. It changes only how
#  quickly a breeder can decide which plant to keep.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  BEFORE GENETICS
    # =========================================================================
    Milestone(
        -9000,
        "Domestication of wheat, barley and rice begins",
        note=(
            "Selection without any theory of inheritance, sustained for "
            "millennia. Every crop in this record is the product of it, and the "
            "genetic changes involved dwarf anything in "
            "`green.plant_genetic_engineering`."
        ),
    ),
    # =========================================================================
    #  THE THEORY
    # =========================================================================
    Milestone(
        1866,
        "Mendel publishes the laws of inheritance",
        note=(
            "Ignored for thirty-four years, then rediscovered independently by "
            "three groups in 1900. It explained why selection had worked all "
            "along."
        ),
    ),
    Milestone(
        1908,
        "Hardy and Weinberg independently describe allele frequency equilibrium",
        note="Two people, two countries, the same year. The names are joined for a reason.",
    ),
    Milestone(
        1918,
        "Fisher reconciles Mendelian inheritance with continuous variation",
        note=(
            "Showed that many genes of small effect produce a continuous "
            "distribution. This is the theoretical basis of everything that "
            "genomic selection later did in practice."
        ),
    ),
    Milestone(
        1936,
        "Lush formalises the breeder's equation",
        note=(
            "R = h2 * S. Ninety years later it is still the equation every "
            "breeding programme is designed around."
        ),
    ),
    # =========================================================================
    #  THE FIRST MARKERS, AND THE DISAPPOINTMENT
    # =========================================================================
    Milestone(
        1980,
        "Restriction fragment length polymorphism markers introduced",
        note="The first DNA markers usable across a whole genome.",
    ),
    Milestone(
        1989,
        "Quantitative trait locus mapping becomes routine in crops",
        note=(
            "A method for finding where a trait's genes are. Two decades of "
            "intensive use produced thousands of publications and remarkably "
            "few varieties. The loci found in one population often failed to "
            "replicate in another, and effects estimated in small populations "
            "were systematically overstated. The technique was answering a "
            "question about genetic architecture, and breeders needed a "
            "prediction."
        ),
    ),
    # =========================================================================
    #  THE SUCCESSES THAT DID WORK
    # =========================================================================
    Milestone(
        1996,
        "First large-scale marker-assisted selection programmes in cereals",
        note=(
            "Successful precisely where quantitative trait locus mapping had "
            "not been: single large-effect disease resistance genes, where a "
            "marker replaces an inoculation test."
        ),
    ),
    # =========================================================================
    #  THE REFRAMING
    # =========================================================================
    Milestone(
        2001,
        "Meuwissen, Hayes and Goddard propose genomic selection",
        note=(
            "The insight was to stop looking for significant markers. Fit all "
            "of them at once, accept that no individual effect is estimable, "
            "and predict the total. It was proposed for livestock, adopted "
            "there first, and moved into crops within a decade. It is the "
            "single most important paper in this record."
        ),
    ),
    Milestone(
        2006,
        "The SUB1A submergence tolerance locus is transferred into rice "
        "mega-varieties by marker-assisted backcrossing",
        note=(
            "Rice that survives two weeks underwater, in varieties farmers were "
            "already growing, delivered by public-sector programmes and "
            "distributed without royalty. Now grown by millions of smallholders "
            "in South Asia. The clearest demonstration that the highest-impact "
            "work in this branch attracts none of the argument."
        ),
    ),
    # =========================================================================
    #  SHORTENING THE CYCLE
    # =========================================================================
    Milestone(
        2009,
        "Genotyping-by-sequencing brings marker cost below the price of a field "
        "plot",
        note=(
            "The moment genotyping stopped being the expensive half of the "
            "decision. Phenotyping has been the bottleneck ever since."
        ),
    ),
    Milestone(
        2018,
        "Speed breeding protocols published for the major cereals",
        note=(
            "Up to six wheat generations a year under extended photoperiod. "
            "Attacks the denominator of genetic gain per year directly, which "
            "is worth more than an equivalent improvement in prediction "
            "accuracy."
        ),
    ),
    Milestone(
        2020,
        "Genomic selection becomes standard practice in commercial maize, wheat "
        "and barley breeding",
    ),
)
