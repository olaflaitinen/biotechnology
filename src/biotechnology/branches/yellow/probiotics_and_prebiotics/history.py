# =============================================================================
#  biotechnology.branches.yellow.probiotics_and_prebiotics.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has two of the same kind at twenty years' distance: a
#  regulatory judgement that the evidence did not support the claims, and a
#  scientific finding that the mechanism was not what the field assumed.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE 2012 ENTRY IS THE MOST CONSEQUENTIAL AND IS RARELY PRESENTED AS WHAT IT
#  IS.
#
#  European regulators assessed the health claims submitted for probiotics and
#  authorised none of them. That is not a procedural obstacle or a case of
#  regulators failing to understand the science. It is a systematic finding, on
#  a large number of submissions, that the evidence offered did not support the
#  claims being made.
#
#  The field's usual account is that the requirements were too strict for food
#  products. The stronger reading, and the one this record takes, is that the
#  assessment revealed how much of the market rested on evidence generated for
#  a different strain, on surrogate endpoints, or on trials too small to
#  conclude anything. The response, which was to sell on implication instead,
#  is recorded here rather than passed over.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE IDEA, AND ITS OVERSTATEMENT AT THE START
    # =========================================================================
    Milestone(
        1907,
        "Metchnikoff proposes that lactic acid bacteria in fermented milk "
        "explain longevity in Bulgarian populations",
        note=(
            "The origin of the probiotic idea, and it began as it continued: a "
            "plausible mechanism attached to an observation that would not "
            "support it. The specific claim about longevity was wrong. The "
            "underlying suggestion, that ingested bacteria might affect health, "
            "was worth pursuing and took most of a century to test properly."
        ),
    ),
    Milestone(
        1965,
        "The term probiotic is introduced",
        note=(
            "Coined as the opposite of antibiotic, for substances promoting "
            "rather than inhibiting microbial growth. The definition has been "
            "revised repeatedly since, and each revision has tightened it, "
            "which is a reasonable summary of the field's direction."
        ),
    ),
    # =========================================================================
    #  THE SCIENCE ARRIVES
    # =========================================================================
    Milestone(
        1995,
        "The prebiotic concept is defined",
        note=(
            "A substrate selectively used by host microorganisms. It shifted "
            "attention from introducing organisms to feeding the ones already "
            "present, which turned out to be the more reproducible of the two "
            "approaches because it does not depend on anything establishing."
        ),
    ),
    Milestone(
        2001,
        "An expert consultation establishes the working definition of a "
        "probiotic",
        note=(
            "Live microorganisms which, when administered in adequate amounts, "
            "confer a health benefit on the host. Every element is a "
            "requirement: alive, adequate dose, demonstrated benefit. Most "
            "products on sale do not meet the third, which the definition makes "
            "checkable rather than arguable."
        ),
    ),
    Milestone(
        2008,
        "Large-scale human microbiome sequencing projects begin",
        note=(
            "Culture-independent characterisation of the gut community at "
            "population scale, using the methods `blue.marine_genomics` records "
            "for seawater. It transformed what could be observed and, as the "
            "2013 entry records, some of what it revealed was unwelcome to the "
            "field."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE EVIDENCE DID NOT SUPPORT THE CLAIMS
    # =========================================================================
    Milestone(
        2012,
        "European authorities reject essentially all submitted probiotic health "
        "claims",
        note=(
            "Hundreds of claims assessed and none authorised. The field's usual "
            "account is that the requirements were unsuited to foods. The "
            "stronger reading is that the assessment revealed how much of the "
            "market rested on evidence generated for a different strain, on "
            "surrogate endpoints, or on trials too small to support a "
            "conclusion. Products were subsequently sold on implication rather "
            "than assertion, and the word probiotic itself was restricted in "
            "several member states because it implies a benefit. It is the most "
            "consequential entry in this record."
        ),
    ),
    # =========================================================================
    #  THE INTERVENTION THAT WORKED, AND IT IS NOT A CONSUMER PRODUCT
    # =========================================================================
    Milestone(
        2013,
        "A randomised trial establishes faecal microbiota transplantation as "
        "highly effective against recurrent Clostridioides difficile infection",
        note=(
            "Stopped early because the transplant arm so clearly outperformed "
            "antibiotic treatment. It proved beyond argument that the gut "
            "community can be manipulated therapeutically, which is the premise "
            "the entire record rests on, and it did so with an undefined "
            "community transferred between people rather than with any product."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE MECHANISM WAS NOT WHAT THE FIELD ASSUMED
    # =========================================================================
    Milestone(
        2018,
        "Sequencing studies show that probiotic colonisation is transient and "
        "highly individual",
        note=(
            "Direct sampling of the gut, rather than of stool, showed that "
            "administered strains colonised some people and not others, that "
            "the difference was determined by the resident community, and that "
            "detection ceased within days to weeks of stopping. It contradicted "
            "the intuitive account most consumers hold and much marketing "
            "implies. Recorded as a setback because the field had been selling "
            "colonisation for decades without establishing it."
        ),
    ),
    # =========================================================================
    #  WHAT THE FIELD DID NEXT
    # =========================================================================
    Milestone(
        2019,
        "Postbiotics are defined as a category",
        note=(
            "Inactivated microorganisms and their components. The scientific "
            "rationale is real, since some effects do not require live "
            "organisms. It also removes the stability, viability and shelf life "
            "problems that the live requirement imposes, and a reader should "
            "notice that a definitional change solved several commercial "
            "difficulties at once."
        ),
    ),
    Milestone(
        2022,
        "Defined bacterial consortia are approved as licensed medicines for "
        "recurrent Clostridioides difficile infection",
        note=(
            "Faecal transplantation made reproducible, characterised and "
            "manufacturable, and regulated as a medicine with the trial "
            "evidence that implies. It is the field's most significant recent "
            "development and it went through the pharmaceutical route rather "
            "than the food one, which is informative about where the evidence "
            "bar sits."
        ),
    ),
    Milestone(
        2021,
        "Human milk oligosaccharides produced by fermentation are authorised "
        "for infant formula",
        note=(
            "Prebiotic compounds that formula previously lacked entirely, "
            "supplied by `yellow.precision_fermentation`. Recorded here because "
            "it is the clearest case of a prebiotic intervention with a defined "
            "compound, a defined population and a defined rationale, which is "
            "what much of the rest of the record lacks."
        ),
    ),
    Milestone(
        2023,
        "Attention shifts towards next-generation strains from the healthy gut "
        "rather than from dairy fermentation",
        note=(
            "The traditional probiotic species were selected because they "
            "survive in fermented food, not because they are prominent members "
            "of the human gut. Organisms such as Akkermansia muciniphila are "
            "abundant residents and are being developed deliberately, which is "
            "a more coherent starting point than the historical one and remains "
            "to be demonstrated clinically."
        ),
    ),
)
