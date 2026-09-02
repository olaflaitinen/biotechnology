# =============================================================================
#  biotechnology.branches.red.pharmacogenomics.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires that
#  setbacks appear. The setback in this field is unusual and is recorded in the
#  2007 and 2013 entries: the science worked, and the implementation did not.
#
#  SUBTYPE-SPECIFIC NOTE
#  Read the gap between the dates. Debrisoquine polymorphism was described in
#  1977 and characterised molecularly in 1988. Routine pre-emptive panel
#  testing began to appear in European health systems only in the 2020s. Four
#  decades separate a solved scientific problem from a delivered clinical one,
#  and nothing in that gap was a laboratory difficulty.
#
#  That interval is the single most useful thing this timeline conveys, and it
#  is why `narrative.WHY_IT_MATTERS` spends its final paragraph on
#  implementation rather than on biology.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  OBSERVATION BEFORE MECHANISM
    # =========================================================================
    Milestone(
        1957,
        "Motulsky links inherited enzyme variation to adverse drug reactions",
        note=(
            "Assembled from scattered clinical reports of patients who reacted "
            "abnormally to anaesthetics and antimalarials. The pattern was "
            "familial, which was the clue."
        ),
    ),
    Milestone(
        1959,
        "Vogel coins the term pharmacogenetics",
    ),
    Milestone(
        1977,
        "Debrisoquine hydroxylation polymorphism described in a volunteer study",
        note=(
            "One investigator took the drug himself and collapsed with severe "
            "hypotension. The subsequent family study established the "
            "autosomal recessive pattern that CYP2D6 explains."
        ),
    ),
    # =========================================================================
    #  MECHANISM
    # =========================================================================
    Milestone(
        1988,
        "CYP2D6 characterised molecularly, explaining the debrisoquine "
        "phenotype",
        note=(
            "The gene proved to be unusually variable, with deletions, "
            "duplications and hybrid forms. Thirty-five years later that "
            "structural complexity is still the one genuinely hard technical "
            "problem in the field."
        ),
    ),
    Milestone(
        1998,
        "TPMT genotyping introduced before thiopurine therapy",
        note=(
            "One of the first tests adopted because the alternative was "
            "occasionally fatal marrow suppression from a standard dose."
        ),
    ),
    Milestone(
        2003,
        "The Human Genome Project is completed, accelerating candidate "
        "discovery",
    ),
    # =========================================================================
    #  PROOF THAT IT WORKS
    # =========================================================================
    Milestone(
        2008,
        "HLA-B*57:01 screening before abacavir becomes standard of care",
        note=(
            "A randomised trial showed screening eliminated immunologically "
            "confirmed hypersensitivity entirely. It remains the field's "
            "cleanest demonstration: one allele, one drug, one severe reaction, "
            "abolished."
        ),
    ),
    Milestone(
        2011,
        "The Clinical Pharmacogenetics Implementation Consortium publishes its "
        "first prescribing guidelines",
        note=(
            "Deliberately framed as what to do with a result you already have, "
            "rather than as advice on whether to test. That reframing is what "
            "made the guidelines usable inside a health system."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE SCIENCE WORKED AND THE DELIVERY DID NOT
    # =========================================================================
    Milestone(
        2007,
        "A warfarin dosing label change is issued, and changes very little",
        note=(
            "Genotype-guided dosing was added to the product label and adoption "
            "remained minimal. Later trials gave mixed results against careful "
            "conventional management. The lesson was that a label change "
            "without a workflow change does not alter prescribing, and it is "
            "still the most cited cautionary example in the field."
        ),
    ),
    Milestone(
        2013,
        "Two large warfarin trials report conflicting results",
        note=(
            "One found benefit against a fixed-dose comparator, the other none "
            "against careful clinical dosing. The disagreement was largely "
            "about the comparator rather than about the genetics, and it "
            "delayed adoption across the whole field by years."
        ),
    ),
    # =========================================================================
    #  IMPLEMENTATION, AT LAST
    # =========================================================================
    Milestone(
        2020,
        "Pre-emptive panel testing enters routine use in several European "
        "health systems",
        note=(
            "The change was to test before anyone is ill, storing the result "
            "for every future prescription. That inverts the economics, because "
            "one test then serves decades of prescribing."
        ),
    ),
    Milestone(
        2023,
        "A multicentre trial reports a reduction in clinically relevant adverse "
        "drug reactions from a twelve-gene pre-emptive panel",
        note=(
            "The first large prospective demonstration that panel testing, "
            "rather than single gene-drug pairs, changes outcomes at the level "
            "of a health system. Sixty-six years after Motulsky."
        ),
    ),
)
