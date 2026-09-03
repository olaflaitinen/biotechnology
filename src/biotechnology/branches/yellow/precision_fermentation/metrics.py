# =============================================================================
#  biotechnology.branches.yellow.precision_fermentation.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST METRIC IS A PRICE, AND IN THIS RECORD THAT IS CORRECT RATHER THAN
#  CRUDE.
#
#  The technology is solved. Making a specific protein in an engineered
#  microorganism has been routine since 1982. What decides whether a product in
#  this record exists is whether it can be made for a price a food ingredient
#  can bear, and that price is set by an agricultural commodity rather than by
#  anything in the process. Opening with titre, as a fermentation facet
#  normally would, would describe an interesting problem that is not the
#  binding one.
#
#  A COMPARISON WORTH CARRYING: the same protein made to pharmaceutical
#  standards can cost two orders of magnitude more per kilogram than the food
#  target allows. Nothing about the biology differs. The difference is
#  purification burden and scale, which is why the downstream metrics here
#  matter more than the upstream ones.
#
#  A NOTE ON FUNCTIONALITY. Sequence identity is necessary and not sufficient.
#  The functional metrics below exist because a protein can be chemically
#  correct and behave wrongly in a food, and a record that measured only
#  identity would miss the reason several products are still not on sale.
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
    #  THE NUMBER THAT DECIDES WHETHER A PRODUCT EXISTS
    # =========================================================================
    Metric(
        name="Production cost per kilogram",
        symbol="C_kg",
        unit="euro per kilogram of purified protein",
        typical="must approach commodity dairy and egg protein prices; "
        "pharmaceutical-grade production of the same protein is orders of "
        "magnitude higher",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Placed first because the technology is solved and this is not. "
            "The target is set by an agricultural commodity produced at "
            "enormous scale and frequently subsidised, which is a benchmark no "
            "pharmaceutical protein has ever had to meet. Graded REPORTED "
            "because companies do not publish it and published estimates vary "
            "widely with assumed scale."
        ),
    ),
    Metric(
        name="Secreted titre",
        symbol="T_sec",
        unit="grams of target protein per litre of broth",
        typical="single digits to tens of grams per litre in optimised hosts",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The main lever on the entry above, and the reason secreting hosts "
            "dominate this record. A protein that must be recovered by breaking "
            "cells open carries a purification cost that a food ingredient "
            "cannot bear, so the choice of host is an economic decision before "
            "it is a biological one."
        ),
    ),
    Metric(
        name="Downstream cost share",
        symbol="f_dsp",
        unit="per cent of total production cost in recovery and purification",
        typical="a large share, and the principal difference between food and "
        "pharmaceutical economics for the same molecule",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The same pattern `white.bioprocess_engineering` records for "
            "therapeutic proteins, applied to a product worth a thousandth as "
            "much per kilogram. Food grade requires less purification than "
            "pharmaceutical grade, which is the only reason the economics can "
            "close at all."
        ),
    ),
    Metric(
        name="Product yield on substrate",
        symbol="Y_ps",
        unit="grams of protein per gram of sugar consumed",
        formula="product_yield",
        typical="the term that determines feedstock cost per kilogram of "
        "product",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Feedstock is a substantial input at food-scale margins, and this "
            "figure also underlies the land use question: the sugar is grown on "
            "farmland, so a poor yield converts directly into hectares and "
            "weakens the environmental case."
        ),
    ),
    # =========================================================================
    #  IS IT ACTUALLY THE SAME PROTEIN
    # =========================================================================
    Metric(
        name="Sequence identity to the animal protein",
        symbol="I_seq",
        unit="per cent of residues matching the reference sequence",
        typical="100 % is the claim and the expectation",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The basis of the whole proposition and the easiest thing in this "
            "facet to demonstrate. It is necessary and not sufficient: the "
            "metrics below exist because identical sequence does not guarantee "
            "identical behaviour, and because the regulatory dossier turns on "
            "characterisation rather than on sequence alone."
        ),
    ),
    Metric(
        name="Glycosylation profile",
        symbol="P_glyc",
        unit="distribution of glycan structures on the expressed protein",
        typical="differs from the animal protein in most microbial hosts",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Where identity usually breaks. A yeast glycosylates differently "
            "from a mammal and a bacterium does not glycosylate at all, so a "
            "protein with the correct sequence may carry different sugars. It "
            "can affect solubility, heat stability and, in principle, "
            "immunogenicity, and it is what a regulator examines most closely."
        ),
    ),
    Metric(
        name="Host cell protein and DNA residue",
        symbol="c_hcp",
        unit="parts per million of total protein",
        typical="food-grade limits, less stringent than pharmaceutical ones",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The specification that separates this record's economics from a "
            "pharmaceutical process making the same molecule. Food grade "
            "tolerates more residue, which permits a shorter purification "
            "train, which is a large part of why the cost target is reachable "
            "at all."
        ),
    ),
    # =========================================================================
    #  DOES IT BEHAVE LIKE FOOD
    # =========================================================================
    Metric(
        name="Gelation temperature and strength",
        symbol="T_gel",
        unit="degrees Celsius and kilopascals at stated concentration",
        typical="must match the animal protein for the application to work",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "One of the functional properties that decides whether an "
            "ingredient works. A whey protein that will not gel correctly "
            "cannot make the products whey protein makes, however identical its "
            "sequence, and this is where several candidates have failed "
            "quietly."
        ),
    ),
    Metric(
        name="Foaming and emulsifying capacity",
        symbol="C_foam",
        unit="per cent overrun or emulsion stability index",
        typical="benchmarked against the animal-derived ingredient",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The properties that matter for egg protein applications in "
            "particular, where the function being replaced is mechanical rather "
            "than nutritional. Benchmarking against the real ingredient rather "
            "than against a specification is the only meaningful test."
        ),
    ),
    Metric(
        name="Heat stability in the food matrix",
        symbol="S_heat",
        unit="per cent of function retained after a stated thermal process",
        typical="tested against the actual process the food undergoes",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "A protein that performs at room temperature and denatures during "
            "pasteurisation is not an ingredient. This is where glycosylation "
            "differences most often show up as a practical problem rather than "
            "an analytical one."
        ),
    ),
    # =========================================================================
    #  WHAT IT CLAIMS TO SAVE, AND WHAT IT CANNOT REMOVE
    # =========================================================================
    Metric(
        name="Cradle-to-gate greenhouse gas intensity",
        symbol="GWP",
        unit="kilograms of carbon dioxide equivalent per kilogram of protein",
        formula="carbon_intensity",
        typical="compared against a named dairy or egg benchmark, and "
        "favourable in most published assessments",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "Graded REPORTED because most published assessments are produced by "
            "or for the companies concerned, assume future scale, and choose "
            "their benchmark. The direction is plausible and the magnitude "
            "should be read with the assumptions stated."
        ),
    ),
    Metric(
        name="Land use per kilogram of protein",
        symbol="A_land",
        unit="square metres per kilogram",
        typical="lower than dairy and egg production, and not zero",
        evidence=EvidenceLevel.REPORTED,
        note=(
            "The honest form of the animal-free claim. Sugar feedstock is grown "
            "on farmland, so land use is reduced rather than removed, and a "
            "claim of no land use is wrong. It is the metric that most often "
            "goes unstated in promotional material about this record."
        ),
    ),
    Metric(
        name="Allergenic equivalence",
        symbol="A_eq",
        unit="qualitative, established by sequence and immunological testing",
        typical="equivalent to the animal protein by design",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Recorded as a metric because it is a required regulatory "
            "determination and because it is the point the field communicates "
            "least well. An identical protein is an identical allergen. The "
            "product is animal-free and is not allergy-free, and the two are "
            "routinely conflated."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Production economics first, then the assessment relationships.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "product_yield",
    "space_time_yield",
    "overall_step_yield",
    "carbon_intensity",
    "life_cycle_impact",
    "mass_balance",
)
