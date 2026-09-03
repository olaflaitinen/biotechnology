# =============================================================================
#  biotechnology.branches.blue.marine_biomaterials.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIRST THREE METRICS ARE COMPOSITIONAL PARAMETERS, NOT PERFORMANCE
#  FIGURES, and that ordering is the argument of the whole record.
#
#  Degree of deacetylation, the uronic acid ratio and sulphation pattern are
#  not quality measures. They are DESCRIPTIONS OF WHICH MATERIAL YOU ACTUALLY
#  HAVE. Two batches of chitosan differing in deacetylation are different
#  materials with different solubility, charge and biological behaviour, sold
#  under one name. Two alginates differing in uronic acid ratio give a stiff
#  brittle gel and a soft elastic one respectively.
#
#  A performance figure quoted without these parameters is therefore not
#  reproducible, and that single fact is why this field's regulated
#  applications are so much harder to reach than its laboratory results
#  suggest. `narrative.py` puts it as reclaimed timber: every plank must be
#  measured first, and the measuring costs more than the timber.
#
#  A NOTE ON MOLECULAR WEIGHT. It is quoted as a distribution rather than a
#  value for these polymers, because extraction cleaves chains unevenly. A
#  single average conceals whether a material is uniform or a mixture of long
#  and short chains behaving differently, and the dispersity matters as much as
#  the mean.
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
    #  WHICH MATERIAL DO YOU ACTUALLY HAVE
    # =========================================================================
    Metric(
        name="Degree of deacetylation",
        symbol="DD",
        unit="per cent of acetyl groups removed",
        typical="70 - 95 % for commercial chitosan; the boundary with chitin "
        "is conventionally placed near 50 %",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Not a quality measure but a statement of which polymer is in the "
            "container. It governs solubility, charge density, antimicrobial "
            "activity and degradation rate, and the name chitosan covers a "
            "range of materials that behave differently. A result reported "
            "without it cannot be reproduced."
        ),
    ),
    Metric(
        name="Mannuronic to guluronic acid ratio",
        symbol="M/G",
        unit="ratio of the two uronic acid residues, dimensionless",
        typical="varying by species, by season and by part of the plant",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Determines the mechanical character of an alginate gel directly: "
            "guluronic-rich alginate gives stiff brittle gels and "
            "mannuronic-rich gives soft elastic ones. It varies within a single "
            "seaweed between stipe and blade, so even one harvest is not one "
            "material unless it is sorted."
        ),
    ),
    Metric(
        name="Degree and position of sulphation",
        symbol="DS",
        unit="sulphate groups per sugar residue",
        typical="the defining variable for carrageenan type and for fucoidan "
        "activity",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "The hardest of the three to control and the one that carries most "
            "of the biological activity attributed to these polymers. It is why "
            "fucoidan results are difficult to compare between studies: two "
            "groups working on fucoidan may be working on materials that share "
            "a name and little else."
        ),
    ),
    # =========================================================================
    #  HOW LONG THE CHAINS ARE
    # =========================================================================
    Metric(
        name="Weight average molecular weight",
        symbol="M_w",
        unit="kilodaltons",
        typical="tens to hundreds of kilodaltons, and reduced by extraction",
        formula="molecular_weight_average",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Governs viscosity, gel strength and degradation rate. Extraction "
            "conditions cleave chains, so the figure describes the process as "
            "much as the organism, and a gentler extraction yields a higher "
            "molecular weight at lower recovery."
        ),
    ),
    Metric(
        name="Dispersity",
        symbol="D_m",
        unit="ratio of weight to number average molecular weight, "
        "dimensionless",
        typical="broad for extracted natural polymers",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Recorded because a single average conceals whether a material is "
            "uniform or a mixture of long and short chains behaving "
            "differently. For a natural polymer the distribution is broad by "
            "default, and narrowing it requires fractionation that most "
            "commercial grades do not receive."
        ),
    ),
    # =========================================================================
    #  WHAT THE MATERIAL DOES
    # =========================================================================
    Metric(
        name="Gel strength",
        symbol="S_gel",
        unit="grams per square centimetre or kilopascals at stated "
        "concentration",
        typical="the primary functional specification for gelling "
        "polysaccharides",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Meaningful only with concentration, temperature, ionic conditions "
            "and the compositional parameters above all stated. It is the "
            "figure a buyer purchases against and the figure most often quoted "
            "without the context that would make it comparable."
        ),
    ),
    Metric(
        name="Swelling ratio",
        symbol="Q_s",
        unit="grams of fluid absorbed per gram of dry material",
        typical="high for alginate and chitosan hydrogels",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The property that makes an alginate dressing work: it absorbs "
            "exudate and gels, conforming to the wound rather than adhering to "
            "it. It is measured in a defined fluid, since absorption differs "
            "between water, saline and a solution containing the calcium that "
            "crosslinks alginate."
        ),
    ),
    Metric(
        name="Degradation rate in physiological conditions",
        symbol="t_deg",
        unit="days to substantial loss of mass or mechanical integrity",
        typical="days to months, and difficult to specify tightly",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Must match the biological process the material is supporting, and "
            "specifying it tightly is genuinely hard when molecular weight "
            "distribution is itself broad and variable. It is one of the "
            "clearest places where the variability constraint blocks a "
            "regulated application."
        ),
    ),
    # =========================================================================
    #  WHAT SEPARATES A MEDICAL GRADE FROM AN INDUSTRIAL ONE
    # =========================================================================
    Metric(
        name="Endotoxin content",
        symbol="c_endo",
        unit="endotoxin units per gram",
        typical="tightly limited for implantable and injectable applications",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Frequently the specification that decides whether a polymer can be "
            "used in a device at all. The same chemical entity is sold as a "
            "food additive, a technical flocculant and a medical grade, and the "
            "difference between them is purification rather than chemistry."
        ),
    ),
    Metric(
        name="Residual protein content",
        symbol="c_prot",
        unit="per cent by weight",
        typical="low limits for medical grades",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Directly relevant to the shellfish allergen question. The protein "
            "responsible for shellfish allergy is not chitosan, so a thoroughly "
            "deproteinised material should not carry the risk, and this metric "
            "is how that argument is actually evidenced rather than asserted."
        ),
    ),
    Metric(
        name="Extraction yield",
        symbol="Y_ext",
        unit="per cent of dry raw material recovered as purified polymer",
        typical="varies widely by material and by how gentle the process is",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Matters less here than in most records, because the raw material "
            "is waste and effectively free. The relevant trade is not yield "
            "against cost but yield against quality: harsher extraction "
            "recovers more polymer of lower molecular weight."
        ),
    ),
    # =========================================================================
    #  THE STRUCTURAL MATERIALS, WHICH ARE MEASURED DIFFERENTLY
    # =========================================================================
    Metric(
        name="Fracture toughness of biomineralised composites",
        symbol="K_IC",
        unit="megapascal root metre",
        typical="orders of magnitude above the constituent mineral alone for "
        "nacre",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "The number that makes nacre worth studying. Calcium carbonate is "
            "brittle; arranged in layers with a small protein fraction it "
            "resists cracking to a degree the mineral cannot approach. The "
            "property belongs to the ARRANGEMENT, which is why the work here is "
            "biomimetic rather than extractive."
        ),
    ),
    Metric(
        name="Wet adhesion strength",
        symbol="sigma_adh",
        unit="megapascals",
        typical="substantial for mussel adhesive proteins on wet substrates "
        "where synthetic adhesives fail",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Measured wet, which is the entire point. Conventional adhesives "
            "are compared dry and lose most of their strength on a wet surface, "
            "so a comparison that does not state the condition understates the "
            "marine material by a wide margin."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Characterisation first, matching the facet's argument, then the mechanics.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "molecular_weight_average",
    "degree_of_polymerisation",
    "swelling_ratio",
    "youngs_modulus",
    "fracture_toughness",
    "mass_balance",
    "product_yield",
)
