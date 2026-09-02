# =============================================================================
#  biotechnology.branches.green.plant_tissue_culture.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS
#
#  Contract: `red/gene_therapy/metrics.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  One number in this set behaves differently from every other metric in the
#  library, and it is worth stating before the list.
#
#  MULTIPLICATION RATE COMPOUNDS GEOMETRICALLY. A rate of five per cycle sounds
#  unremarkable and is not: five cycles give 3125 plants from one explant, six
#  give 15625, eight give over 390000. A single elite plant becomes a national
#  planting programme inside two years.
#
#  That is the whole commercial case for micropropagation, and it is also the
#  whole risk. The same exponent that turns one good genotype into a million
#  plants turns one undetected somaclonal variant, or one latent endophyte,
#  into a million defective ones. Every quality metric below exists to catch
#  that before the exponent does its work.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  The compounding number. See the header note.
    # -------------------------------------------------------------------------
    Metric(
        name="Multiplication rate",
        symbol="M",
        unit="shoots per explant per subculture cycle",
        typical="3 - 10 per cycle of four to six weeks",
        formula="multiplication_rate",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Compounds geometrically. A rate of five gives 3125 plants after "
            "five cycles and over 390000 after eight. The same exponent "
            "multiplies any undetected defect just as fast, which is why the "
            "subculture cap in the next metric exists."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The cap that limits the exponent. A quality control, not a biological
    #  limit.
    # -------------------------------------------------------------------------
    Metric(
        name="Maximum subculture number",
        symbol="n_sub",
        unit="successive subcultures before restarting from stock",
        typical="8 - 12 in commercial protocols",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "An imposed limit rather than a measured one. Somaclonal variation "
            "accumulates with time in culture, particularly through a callus "
            "phase, so protocols cap the number of divisions and return to "
            "banked stock even though the plants still look healthy."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Regeneration frequency. The number that decides whether a genotype can
    #  be engineered at all.
    # -------------------------------------------------------------------------
    Metric(
        name="Regeneration frequency",
        symbol="RF",
        unit="per cent of explants producing a shoot or embryo",
        typical="10 - 90 %, and below 1 % from protoplasts in most crops",
        formula="regeneration_frequency",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Almost entirely genotype-dependent. This is the number that "
            "decides whether a variety can be transformed or edited, and it is "
            "why a construct is often made in an easily regenerated variety and "
            "crossed into the wanted one afterwards."
        ),
    ),
    # -------------------------------------------------------------------------
    #  The hormone ratio. The lever, expressed as a ratio because only the
    #  ratio matters.
    # -------------------------------------------------------------------------
    Metric(
        name="Auxin to cytokinin ratio",
        symbol="A:C",
        unit="dimensionless ratio of molar concentrations",
        typical="high for roots, low for shoots, intermediate for callus",
        formula="hormone_ratio",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Established by Skoog and Miller in 1957 and still the single most "
            "useful relationship in the field. The absolute concentrations "
            "matter far less than the ratio, which is why a protocol transfers "
            "between laboratories more readily than the concentrations alone "
            "would suggest."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Contamination. The routine failure, and one that is bimodal rather than
    #  gradual.
    # -------------------------------------------------------------------------
    Metric(
        name="Contamination rate",
        symbol="C_rate",
        unit="per cent of cultures lost",
        typical="below 5 % in a well-run laboratory",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Fungal and bacterial contamination appears within days and is "
            "obvious. Endophytic bacteria are the dangerous case: invisible for "
            "months, then emerging across a whole batch at once, which is why "
            "the figure is bimodal rather than a smooth distribution."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Acclimatisation survival. Where plants are lost in bulk, at the last
    #  step, after all the cost has been incurred.
    # -------------------------------------------------------------------------
    Metric(
        name="Acclimatisation survival",
        symbol="S_acc",
        unit="per cent surviving transfer from jar to soil",
        typical="70 - 98 %",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Plantlets grown in saturated humidity have a poorly developed "
            "cuticle and non-functional stomata. Losses here are the most "
            "expensive in the process because they occur after every other cost "
            "has already been paid."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Virus elimination efficiency. What meristem culture actually achieves.
    # -------------------------------------------------------------------------
    Metric(
        name="Virus elimination efficiency",
        symbol="VE_mer",
        unit="per cent of regenerants testing virus-free",
        typical="40 - 95 %, depending on virus and on excised dome size",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Smaller domes give cleaner material and regenerate less readily, "
            "so the protocol trades one against the other. Thermotherapy before "
            "excision pushes the virus front back and improves both. Every "
            "regenerant must still be indexed individually; the technique "
            "raises the odds rather than guaranteeing the outcome."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Genetic fidelity. The check that the copies really are copies.
    # -------------------------------------------------------------------------
    Metric(
        name="Genetic fidelity",
        symbol="F_gen",
        unit="per cent of regenerants matching the mother plant by marker",
        typical="above 95 % expected in a validated protocol",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Assessed with molecular markers, and increasingly with methylation "
            "assays, because the oil palm mantled-fruit abnormality was "
            "epigenetic and invisible to any sequence-based test."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Cryopreservation recovery. Whether the genebank actually works.
    # -------------------------------------------------------------------------
    Metric(
        name="Cryopreservation recovery",
        symbol="R_cryo",
        unit="per cent of shoot tips regrowing after liquid nitrogen",
        typical="40 - 80 % where a protocol exists at all",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Species-specific and slow to develop. The crops that most need "
            "clonal conservation, because their seed cannot be dried and "
            "frozen, are frequently the ones with the least reliable recovery."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  exponential_growth is included because the multiplication rate is the same
#  mathematics as any other geometric process, and medium_osmolality because
#  osmotic potential is what slow-growth storage manipulates.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "multiplication_rate",
    "regeneration_frequency",
    "hormone_ratio",
    "exponential_growth",
    "medium_osmolality",
    "serial_dilution",
    "colony_forming_units",
)
