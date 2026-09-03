# =============================================================================
#  biotechnology.branches.white.biocatalysis.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two of an unusual kind: neither is an accident or a
#  harm, both are cases where the field promised more than it delivered and
#  had to correct its own account.
#
#  SUBTYPE-SPECIFIC NOTE
#  The timeline has a long flat stretch and then a sharp turn. From 1858 to the
#  1980s, biocatalysis was a small set of transformations that happened to work
#  and could not be improved, because an enzyme was whatever nature supplied.
#  Directed evolution changed the enzyme from a fixed input into an engineering
#  variable, and the 2010 sitagliptin process is the moment the change became
#  undeniable to process chemists who had no interest in enzymology.
#
#  The 2010 entry is the longest in this record and is meant to be. It is the
#  case that changed how routes are planned across an industry.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE DISCOVERY THAT MOLECULES ARE HANDED
    # =========================================================================
    Milestone(
        1858,
        "Pasteur resolves a racemic tartrate using a mould that consumes only "
        "one enantiomer",
        note=(
            "The first biocatalytic kinetic resolution, performed before anyone "
            "knew what an enzyme was. It is also the experiment that "
            "established molecular handedness as a physical fact, which is the "
            "property this entire record is organised around."
        ),
    ),
    Milestone(
        1894,
        "Fischer proposes the lock and key model of enzyme specificity",
        note=(
            "An explanation for why the mould in 1858 could tell the two "
            "tartrates apart. Superseded in detail by induced fit, and still "
            "the image most people carry."
        ),
    ),
    # =========================================================================
    #  THE FIRST INDUSTRIAL TRANSFORMATIONS
    # =========================================================================
    Milestone(
        1952,
        "Microbial hydroxylation of steroids is introduced into cortisone "
        "manufacture",
        note=(
            "A single fungal step replaced a long sequence of chemical "
            "operations and cut the cost of cortisone by orders of magnitude. "
            "The transformation, hydroxylation at an unactivated carbon, is one "
            "conventional chemistry still performs badly, which is why this "
            "process survives."
        ),
    ),
    Milestone(
        1969,
        "Immobilised aminoacylase enters continuous industrial operation for "
        "amino acid resolution",
        note=(
            "The first continuous industrial process using an immobilised "
            "enzyme. It established the packed-bed pattern that "
            "`practice.TECHNOLOGIES` still lists as the answer to poor "
            "space-time yield."
        ),
    ),
    Milestone(
        1973,
        "Penicillin acylase replaces the chemical route to 6-aminopenicillanic "
        "acid",
        note=(
            "The chemical route ran below minus thirty degrees and used "
            "dichloromethane and phosphorus pentachloride. The enzymatic one "
            "runs in water near room temperature. It is the largest tonnage "
            "biocatalytic process in the world and the field's standing proof "
            "that a green route can also be the cheap one."
        ),
    ),
    # =========================================================================
    #  THE FIRST OVERPROMISE
    # =========================================================================
    Milestone(
        1984,
        "Enzymes are shown to function in nearly anhydrous organic solvents",
        note=(
            "A genuine and surprising result that opened reactions water made "
            "impossible, including ester synthesis rather than hydrolysis. It "
            "is recorded as a partial setback because the surrounding "
            "enthusiasm was not borne out: activity in organic media is "
            "routinely several orders of magnitude below activity in water, "
            "and the general-purpose solvent-tolerant biocatalysis that was "
            "anticipated did not arrive. What survived is a set of specific "
            "and useful cases, chiefly lipases, rather than a new paradigm."
        ),
    ),
    # =========================================================================
    #  THE ENZYME BECOMES AN ENGINEERING VARIABLE
    # =========================================================================
    Milestone(
        1993,
        "Directed evolution turns the enzyme from a fixed input into a "
        "designable one",
        note=(
            "Before this, a route either had a suitable natural enzyme or it "
            "did not. Afterwards, an enzyme that is nearly right can be made "
            "right. Every entry below depends on it."
        ),
    ),
    Milestone(
        1998,
        "The twelve principles of green chemistry give the field its economic "
        "argument",
        note=(
            "Catalysis, atom economy and safer solvents are named as design "
            "goals. This supplied the vocabulary, and eventually the corporate "
            "targets, in which a biocatalytic route redesign could be "
            "justified to management rather than to chemists."
        ),
    ),
    # =========================================================================
    #  THE SECOND OVERPROMISE
    # =========================================================================
    Milestone(
        2008,
        "Computationally designed enzymes for reactions with no natural "
        "counterpart are reported",
        note=(
            "The designs catalysed the intended reactions and were slower than "
            "natural enzymes by many orders of magnitude, requiring extensive "
            "directed evolution afterwards to reach useful rates. Recorded as "
            "a setback in the same spirit as 1984: the result was real, the "
            "claim that rational design had replaced evolution was not."
        ),
    ),
    # =========================================================================
    #  THE CASE THAT CHANGED HOW ROUTES ARE PLANNED
    # =========================================================================
    Milestone(
        2010,
        "An engineered transaminase replaces metal-catalysed asymmetric "
        "hydrogenation in sitagliptin manufacture",
        note=(
            "The starting enzyme did not accept the substrate at all. Rounds "
            "of directed evolution produced a variant that performed the "
            "transformation at manufacturing concentrations in an organic "
            "cosolvent. The new route raised yield, removed a high-pressure "
            "hydrogenation and its specialised equipment, eliminated the "
            "rhodium catalyst and the heavy metal removal step that followed "
            "it, and reduced total waste substantially. It is recorded at "
            "length because of what it proved rather than what it made: that "
            "an enzyme can be engineered to fit a route chosen for other "
            "reasons, rather than the route being bent to fit an available "
            "enzyme. That inversion is why process chemists with no interest "
            "in enzymology began treating biocatalytic steps as ordinary "
            "retrosynthetic options."
        ),
    ),
    # =========================================================================
    #  BEYOND WHAT NATURE DOES
    # =========================================================================
    Milestone(
        2013,
        "Engineered haem enzymes are shown to perform carbene transfer, a "
        "reaction with no biological precedent",
        note=(
            "Existing protein scaffolds were redirected to chemistry that "
            "evolution never invented, including cyclopropanation. It moved "
            "the field's ambition from imitating natural transformations to "
            "borrowing nature's scaffolds for chemistry of our own choosing."
        ),
    ),
    Milestone(
        2019,
        "A multi-enzyme cascade produces the nucleoside analogue islatravir in "
        "a small number of vessels without protecting groups",
        note=(
            "Nine enzymes, several of them engineered, operating in sequence "
            "with no isolation of intermediates. It demonstrated that "
            "biocatalysis had moved from replacing a single step to designing "
            "the whole route, which is what `practice.APPLICATIONS` means by "
            "cascade design."
        ),
    ),
    Milestone(
        2022,
        "Machine learning models trained on sequence and activity data enter "
        "routine use in enzyme selection for new routes",
        note=(
            "Candidate selection and variant proposal accelerated. Recorded "
            "with the caution the two setbacks above earned: prediction of "
            "activity in a real process medium at manufacturing substrate "
            "loading remains unreliable, and screening is still what settles "
            "it."
        ),
    ),
)
