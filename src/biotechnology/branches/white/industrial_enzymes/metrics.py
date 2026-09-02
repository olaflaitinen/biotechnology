# =============================================================================
#  biotechnology.branches.white.industrial_enzymes.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This is the most quantitative record in the white branch, and one
#  distinction has to be made before the list or the numbers mislead.
#
#  THE TEXTBOOK METRICS ARE NOT THE COMMERCIAL ONES. A biochemistry course
#  measures an enzyme by k_cat and K_M, and those are recorded below because
#  they are the vocabulary. An industrial buyer measures the same enzyme by
#  total turnover number, which is how many molecules it converts before it
#  dies, and by cost per kilogram of product. A variant with twice the k_cat
#  and half the operational lifetime is a worse product, and this record is
#  ordered to make that visible: the process metrics come first, the kinetic
#  ones after.
#
#  A NOTE ON k_cat/K_M. The ratio, not either term alone, is the specificity
#  constant and is what should be compared between enzymes or variants. Its
#  upper bound is set by how fast substrate can diffuse to the active site,
#  around 10^8 to 10^9 per molar per second. An enzyme at that bound is called
#  catalytically perfect, and no amount of engineering improves it further,
#  because the chemistry is no longer the slow step.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # =========================================================================
    #  WHAT DECIDES WHETHER THE PROCESS IS BOUGHT
    # =========================================================================
    Metric(
        name="Total turnover number",
        symbol="TTN",
        unit="moles of product per mole of enzyme, dimensionless",
        typical="10^4 - 10^6 for a viable industrial biocatalyst",
        formula="total_turnover_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The single most commercially important number in this record, and "
            "the one a kinetics textbook does not emphasise. It is how much "
            "product one unit of catalyst delivers over its whole working life, "
            "so it combines speed with survival. A faster enzyme that dies "
            "sooner has a lower TTN and is the worse product."
        ),
    ),
    Metric(
        name="Biocatalyst cost contribution",
        symbol="C_cat",
        unit="euro per kilogram of product",
        typical="below 1 % of product value for bulk, higher for fine chemicals",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The commercial acceptance criterion. It follows directly from TTN "
            "and enzyme price, and it is the reason immobilisation matters: "
            "recovering and reusing the catalyst across batches divides this "
            "number by the number of reuses."
        ),
    ),
    Metric(
        name="Space-time yield",
        symbol="STY",
        unit="grams of product per litre of reactor per hour",
        typical="10 - 500 g/L/h depending on product value",
        formula="space_time_yield",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "How hard the vessel is working. It sets how much capital equipment "
            "a given output requires, and it is the metric on which biological "
            "processes most often lose to chemical ones, because an enzyme "
            "works in dilute aqueous solution."
        ),
    ),
    # =========================================================================
    #  WHY THE CATALYST STOPS WORKING
    # =========================================================================
    Metric(
        name="Operational half-life",
        symbol="t_half",
        unit="hours of retained activity under process conditions",
        typical="100 - 5000 h",
        formula="enzyme_half_life",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Must be measured under process conditions, not in a buffer. An "
            "enzyme that is stable in a cuvette and unstable in the presence of "
            "substrate, shear and its own product has no industrial value, and "
            "the discrepancy between the two figures is a common source of "
            "disappointment in scale-up."
        ),
    ),
    Metric(
        name="Melting temperature",
        symbol="T_m",
        unit="degrees Celsius",
        typical="50 - 105 degrees C depending on source and engineering",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The unfolding midpoint, and the standard proxy for stability "
            "because it is quick to measure. It is a proxy rather than the "
            "answer: irreversible inactivation by oxidation, aggregation or "
            "proteolysis often occurs well below T_m and is what actually ends "
            "the run."
        ),
    ),
    # =========================================================================
    #  THE KINETIC VOCABULARY
    # =========================================================================
    Metric(
        name="Turnover number",
        symbol="k_cat",
        unit="per second",
        typical="1 - 10^5 s^-1",
        formula="michaelis_menten",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Molecules converted per active site per second at saturation. "
            "Reported alone it is close to meaningless for a process, because "
            "industrial reactions are frequently run well below saturation."
        ),
    ),
    Metric(
        name="Michaelis constant",
        symbol="K_M",
        unit="millimolar",
        typical="0.01 - 100 mM",
        formula="michaelis_menten",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The substrate concentration giving half maximal rate. Widely and "
            "wrongly read as binding affinity: it equals the dissociation "
            "constant only when the chemical step is much slower than substrate "
            "release, which for a good enzyme is exactly when it is not."
        ),
    ),
    Metric(
        name="Specificity constant",
        symbol="k_cat/K_M",
        unit="per molar per second",
        typical="10^3 - 10^8 M^-1 s^-1",
        formula="catalytic_efficiency",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The correct figure for comparing enzymes or variants, since it "
            "governs rate under the dilute conditions industry actually uses. "
            "Its ceiling is diffusion, around 10^8 to 10^9, and an enzyme at "
            "that limit is called catalytically perfect: further engineering "
            "cannot help, because the chemistry is no longer rate-limiting."
        ),
    ),
    # =========================================================================
    #  WHAT IS SOLD, AND WHAT IS WASTED
    # =========================================================================
    Metric(
        name="Specific activity",
        symbol="A_sp",
        unit="units per milligram of protein",
        typical="1 - 10^4 U/mg",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The commercial unit of sale, and the reason enzyme prices cannot "
            "be compared by mass. One unit converts one micromole of substrate "
            "per minute under stated conditions, and those conditions differ "
            "between suppliers, so two quoted activities are only comparable "
            "when the assay is."
        ),
    ),
    Metric(
        name="Secreted titre",
        symbol="T_sec",
        unit="grams of enzyme per litre of fermentation broth",
        typical="1 - 100 g/L in optimised industrial hosts",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The manufacturing lever, and usually a larger commercial gain than "
            "improving the enzyme itself. Doubling titre halves the cost of "
            "goods; doubling specific activity does not, because the "
            "fermentation still costs the same."
        ),
    ),
    Metric(
        name="Environmental factor",
        symbol="E_factor",
        unit="kilograms of waste per kilogram of product",
        typical="under 5 for bulk chemistry, 25 - 100 for pharmaceuticals",
        formula="e_factor",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The green chemistry metric that biocatalysis is usually adopted to "
            "improve, and it counts water as waste. Pharmaceutical manufacture "
            "has by far the worst figure of any chemical sector, which is why "
            "enzymatic route replacement has been pursued hardest there despite "
            "the small tonnages involved."
        ),
    ),
    Metric(
        name="Enantiomeric excess",
        symbol="ee",
        unit="per cent",
        typical="above 99 % required for a pharmaceutical intermediate",
        formula="enantiomeric_excess",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The property that most often makes an enzymatic route the only "
            "practical one. Chemical catalysis frequently produces both mirror "
            "images and then discards half the output; an enzyme, being chiral "
            "itself, typically makes one. In a medicine the wrong mirror image "
            "is at best inert and at worst harmful."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Ordered to match the metric groups above: the process figures, then the
#  kinetics, then the green chemistry measures.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "total_turnover_number",
    "space_time_yield",
    "enzyme_half_life",
    "michaelis_menten",
    "catalytic_efficiency",
    "arrhenius_equation",
    "e_factor",
    "atom_economy",
    "enantiomeric_excess",
)
