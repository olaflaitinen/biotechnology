# =============================================================================
#  biotechnology.branches.red.antibody_engineering.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The idea that makes this field comprehensible is MODULARITY. A natural
#  antibody is not one thing; it is two functional halves joined together, and
#  almost everything in this record follows from the discovery that the halves
#  can be separated, swapped, duplicated and reattached to things that are not
#  antibodies at all.
#
#  The public register is therefore built around that single idea rather than
#  around immunology. A reader who grasps "the part that finds the target and
#  the part that does something about it are separable" can follow every format
#  in `practice.TECHNOLOGIES` without knowing what an immunoglobulin domain is.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

__all__ = [
    "SUMMARY",
    "DESCRIPTION",
    "PLAIN_LANGUAGE",
    "ANALOGY",
    "WHY_IT_MATTERS",
]


# =============================================================================
#  TECHNICAL REGISTER
# =============================================================================

SUMMARY = (
    "Designing and optimising antibody-derived molecules for affinity, "
    "specificity, half-life and effector function."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the architecture and why it is modular, (b) the discovery and
#  selection loop, (c) what optimisation actually optimises, (d) the binding
#  constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) the architecture
    "A natural immunoglobulin G is a Y-shaped protein whose two arms bind an "
    "antigen and whose stem recruits immune effectors. Antibody engineering "
    "treats that architecture as modular: the binding arms and the effector "
    "stem are encoded separately, fold independently, and can be recombined "
    "with each other or with entirely non-antibody components. "
    # (b) discovery and selection
    "Discovery generates candidate binders from immunised animals, from human "
    "donor B cells, or from synthetic libraries displayed on phage, yeast or "
    "ribosomes. Selection enriches binders through iterative panning against "
    "the target, a directed evolution loop that can search a library of ten "
    "billion variants in a fortnight. "
    # (c) optimisation
    "Optimisation then addresses each property separately, which is what "
    "modularity buys. Affinity maturation improves binding, usually into the "
    "low nanomolar or picomolar range. Humanisation replaces rodent framework "
    "residues to reduce immunogenicity. Fc engineering tunes circulating "
    "half-life through the neonatal Fc receptor and tunes effector recruitment "
    "up or down independently of binding. Developability screening removes "
    "candidates that aggregate, oxidise or express poorly before they consume "
    "years of development. "
    # (d) the binding constraint
    "The binding constraint is delivery to the target, not affinity for it. "
    "A molecule of one hundred and fifty kilodaltons crosses a capillary wall "
    "slowly, penetrates a solid tumour poorly and crosses the blood-brain "
    "barrier hardly at all, which is why most format innovation in the last "
    "two decades has been about size and shape rather than about tighter "
    "binding."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Your immune system makes proteins called antibodies. Each one is shaped to "
    "lock onto a single specific target and nothing else, rather like a key cut "
    "for one lock. An antibody has two working parts: the end that grips the "
    "target, and the tail that calls the rest of the immune system over to deal "
    "with whatever has been gripped. Because those two parts are separate, "
    "scientists can change one without disturbing the other. They can find an "
    "antibody for almost any chosen target, make its grip tighter, make it last "
    "longer in the blood, attach a drug so the drug is delivered only where the "
    "antibody sticks, or join two different grips so that one molecule has to "
    "grab two things at once before anything happens."
)

# -----------------------------------------------------------------------------
#  The courier analogy. Its limit is deliberately visible and is the field's
#  actual problem: a courier can walk up to any door, whereas a large protein
#  cannot reach most of the addresses in the body.
# -----------------------------------------------------------------------------
ANALOGY = (
    "A courier with an exact address. The parcel does not go to the whole city; "
    "it goes to one door. Antibody engineering is address-writing plus vehicle "
    "design: you can make the address more precise, put a different parcel in "
    "the van, or build a van that must visit two addresses on the same trip. "
    "Where the comparison fails is the interesting part. A real courier can "
    "reach any door in the city. These vans are large, the streets inside a "
    "tumour are badly built, and the road into the brain is closed, which is "
    "why so much of the field is about building a smaller van rather than "
    "writing a better address."
)

WHY_IT_MATTERS = (
    "Monoclonal antibodies are the largest class of biologic medicine by "
    "revenue and have changed the outlook in cancer, rheumatoid arthritis, "
    "asthma, migraine, high cholesterol and transplant rejection. They are also "
    "the fastest route to a therapy against a new pathogen: a neutralising "
    "antibody can be isolated from a convalescent donor within weeks, long "
    "before any vaccine campaign can protect a population. The costs are real "
    "and specific. Doses are measured in hundreds of milligrams rather than "
    "milligrams, so manufacturing is expensive and annual treatment costs run "
    "into tens of thousands of euro. The molecules must be injected rather than "
    "swallowed. And because the technology works best against targets that are "
    "easy to reach in the bloodstream, it has advanced fastest for the diseases "
    "of wealthy populations and slowest for those it could most cheaply have "
    "helped."
)
