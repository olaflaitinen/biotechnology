# =============================================================================
#  biotechnology.branches.yellow.food_biopreservation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two: the emergence of resistance to an antimicrobial the
#  food industry had treated as permanent, and a food safety crisis that
#  revealed the gap this record exists to fill.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 1980s LISTERIA OUTBREAKS ARE THE ENTRY THAT EXPLAINS THE FIELD.
#
#  Before them, food microbiology was organised around organisms that grow at
#  warm temperatures and are killed by cooking. Listeria monocytogenes does
#  neither: it grows at refrigeration temperature and it contaminates food
#  AFTER the kill step, in slicing, packing and handling. Chilling, which was
#  the industry's principal safety measure, does not stop it.
#
#  That left a specific gap: something that acts in the finished, packaged,
#  chilled product over its whole shelf life. Heat cannot, because the product
#  is already made. Most chemical preservatives were being reduced rather than
#  added. Biopreservation is the answer that was available, and the field's
#  shape follows from the organism.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE AGENT ARRIVES BEFORE THE PROBLEM DOES
    # =========================================================================
    Milestone(
        1928,
        "An inhibitory substance produced by lactic streptococci is described",
        note=(
            "The observation that would become nisin. It was noticed as a "
            "nuisance, since a culture inhibiting other cultures is a problem "
            "in a dairy, which is a recurring pattern in this record: several "
            "of its agents were first encountered as interference."
        ),
    ),
    Milestone(
        1951,
        "Nisin is characterised and proposed for food preservation",
        note=(
            "A ribosomally synthesised peptide from a food organism, active "
            "against Gram-positive bacteria including clostridia. Its "
            "limitation was apparent from the start and has not changed: the "
            "outer membrane of Gram-negative bacteria excludes it."
        ),
    ),
    Milestone(
        1969,
        "Nisin is accepted internationally as a food additive",
        note=(
            "Assessed by the joint expert committee and permitted with defined "
            "limits, initially for processed cheese. It remains the most widely "
            "permitted bacteriocin and the only one with a genuinely long "
            "regulatory history, which is why every later agent is measured "
            "against it."
        ),
    ),
    # =========================================================================
    #  THE FRAMEWORK THAT MAKES SENSE OF ALL OF IT
    # =========================================================================
    Milestone(
        1976,
        "Hurdle technology is articulated as a framework for food preservation",
        note=(
            "Leistner's formulation: several sublethal barriers combine into "
            "control that none achieves alone. It is the correct frame for "
            "everything in this record, and it is why presenting any single "
            "biopreservative as a standalone preservative misdescribes the "
            "field."
        ),
    ),
    # =========================================================================
    #  THE SETBACK THAT DEFINED THE FIELD'S PURPOSE
    # =========================================================================
    Milestone(
        1985,
        "Major listeriosis outbreaks establish Listeria monocytogenes as a "
        "food safety priority",
        note=(
            "Outbreaks linked to soft cheese and other ready-to-eat products, "
            "with high case fatality. The organism grows at refrigeration "
            "temperature and contaminates after cooking, so the industry's two "
            "principal controls, heat and chilling, do not address it. It is "
            "recorded as a setback because it revealed a gap rather than a "
            "failure of any existing measure, and the gap is what this record "
            "exists to fill."
        ),
    ),
    # =========================================================================
    #  THE RESPONSE
    # =========================================================================
    Milestone(
        1990,
        "Protective cultures are introduced commercially for chilled foods",
        note=(
            "Live organisms selected to compete with pathogens without "
            "acidifying or flavouring the product, which is a harder selection "
            "than for a starter culture because the requirement is that nothing "
            "perceptible happens."
        ),
    ),
    Milestone(
        1995,
        "Bacteriocin-producing starter cultures enter use in fermented meats",
        note=(
            "Generating the antimicrobial in place during fermentation rather "
            "than adding a purified preparation, which also avoids the additive "
            "status that a purified bacteriocin carries. It is a regulatory "
            "solution as much as a technical one."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE AGENT IS AN ANTIMICROBIAL LIKE ANY OTHER
    # =========================================================================
    Milestone(
        1999,
        "Nisin resistance is documented in Listeria monocytogenes",
        note=(
            "Resistant variants arise through changes to the cell envelope, at "
            "frequencies that make them a practical concern rather than a "
            "curiosity. It should not have been surprising and it was treated "
            "as such: the food industry had used nisin for thirty years as "
            "though it were a permanent property of the world. Recorded as a "
            "setback because the field was slower than clinical microbiology to "
            "say plainly that these agents are antimicrobials subject to the "
            "same evolutionary pressure as any other."
        ),
    ),
    # =========================================================================
    #  A NEW AGENT, AND A NEW CONSUMER PROBLEM
    # =========================================================================
    Milestone(
        2006,
        "A Listeria-specific bacteriophage preparation is approved for use on "
        "ready-to-eat foods",
        note=(
            "The first phage product permitted in food. Its specificity is both "
            "the advantage, since the resident and starter flora are untouched, "
            "and the limitation, since one preparation addresses one species. "
            "It also introduced a communication problem no other agent here "
            "has, because the product is a virus deliberately added to food."
        ),
    ),
    Milestone(
        2011,
        "Regulatory criteria formalise the requirement that Listeria not "
        "exceed defined limits at the end of shelf life in ready-to-eat foods",
        note=(
            "The shift from a kill requirement to a growth-control requirement, "
            "which is what a chilled ready-to-eat product actually needs. It "
            "made challenge testing routine and gave biopreservation a defined "
            "role rather than a general one."
        ),
    ),
    # =========================================================================
    #  WHERE THE COMMERCIAL PRESSURE COMES FROM NOW
    # =========================================================================
    Milestone(
        2015,
        "Nitrite reduction in cured meat becomes a commercial and regulatory "
        "priority",
        note=(
            "Public and regulatory pressure on nitrite created demand for "
            "partial replacements, and biopreservation supplies one. It is the "
            "clearest current driver of the field, and it is a hurdle argument: "
            "removing one barrier requires strengthening another rather than "
            "removing it altogether."
        ),
    ),
    Milestone(
        2020,
        "Clean label reformulation drives adoption, and collides with additive "
        "declaration",
        note=(
            "Manufacturers replaced chemical preservatives with biological "
            "agents to shorten ingredient lists, and discovered that several of "
            "those agents are themselves additives requiring declaration. The "
            "tension is unresolved and is recorded as a challenge rather than "
            "presented as a success."
        ),
    ),
)
