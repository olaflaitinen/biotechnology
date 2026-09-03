# =============================================================================
#  biotechnology.branches.white.metabolic_engineering.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record's principal setback is one of the most instructive in the
#  entire library, because the science worked perfectly and the project failed
#  anyway.
#
#  SUBTYPE-SPECIFIC NOTE
#  The timeline makes a point that the field's own literature tends to soften.
#  The two most commercially important entries, glutamate in 1957 and lysine
#  soon after, PREDATE the discipline's name by more than thirty years and were
#  achieved by mutagenesis and selection with no molecular biology at all.
#  Rational, model-guided design arrived later and has not yet displaced the
#  older approach for the largest products.
#
#  A reader should come away understanding that this field's history is not a
#  clean progression from crude to rational. Adaptive laboratory evolution, an
#  explicitly non-rational method, is in routine industrial use today.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE INDUSTRY EXISTED BEFORE THE DISCIPLINE
    # =========================================================================
    Milestone(
        1957,
        "Glutamate fermentation by Corynebacterium glutamicum is "
        "commercialised",
        note=(
            "Achieved by isolating an organism that leaked glutamate and then "
            "improving it by mutagenesis and selection, with no molecular "
            "biology whatsoever. It became one of the largest fermentation "
            "products in the world and is the reason this field's economics "
            "were established decades before its theory."
        ),
    ),
    Milestone(
        1961,
        "Jacob and Monod describe operon regulation and feedback inhibition",
        note=(
            "The explanation for why cells resist overproduction: they evolved "
            "specific machinery to prevent it. Every deregulated enzyme variant "
            "used in an amino acid strain today is a deliberate defeat of what "
            "was described here."
        ),
    ),
    # =========================================================================
    #  THE THEORETICAL RESULT THAT GOVERNS THE FIELD
    # =========================================================================
    Milestone(
        1973,
        "Metabolic control analysis establishes that flux control is "
        "distributed",
        note=(
            "Kacser and Burns, and independently Heinrich and Rapoport, showed "
            "that control over pathway flux is shared among enzymes and that "
            "the flux control coefficients sum to one. The practical "
            "consequence is blunt: there is usually no single rate-limiting "
            "step, and removing the apparent bottleneck moves control rather "
            "than eliminating it. It is the most useful and most ignored result "
            "in the discipline."
        ),
    ),
    # =========================================================================
    #  THE DISCIPLINE ACQUIRES A NAME AND A METHOD
    # =========================================================================
    Milestone(
        1991,
        "Metabolic engineering is named and defined as a discipline",
        note=(
            "Bailey's framing separated purposeful, quantitative modification "
            "of metabolic networks from both classical strain improvement and "
            "single-gene genetic engineering. Naming it mattered more than it "
            "sounds: it made the network rather than the gene the unit of "
            "design."
        ),
    ),
    Milestone(
        1994,
        "Flux balance analysis is applied to predict metabolic behaviour from "
        "stoichiometry alone",
        note=(
            "A whole network could be analysed without knowing a single kinetic "
            "parameter, using only reaction stoichiometry and an assumed "
            "objective. That tractability is why constraint-based modelling, "
            "rather than kinetic modelling, became the field's working tool."
        ),
    ),
    Milestone(
        1999,
        "The first genome-scale metabolic reconstruction is published",
        note=(
            "Every known reaction in an organism assembled into one "
            "computable model. Reconstructions now exist for thousands of "
            "organisms and are the starting point of most design work in "
            "`practice.TECHNOLOGIES`."
        ),
    ),
    # =========================================================================
    #  DESIGNED PATHWAYS REACH THE MARKET
    # =========================================================================
    Milestone(
        2006,
        "Engineered Escherichia coli enters commercial production of "
        "1,3-propanediol from glucose",
        note=(
            "A pathway assembled across organism boundaries, replacing a "
            "petrochemical route for a polymer feedstock. The first "
            "large-volume demonstration that a designed pathway could compete "
            "commercially rather than only work."
        ),
    ),
    Milestone(
        2013,
        "Commercial production begins for 1,4-butanediol by a pathway that "
        "exists in no natural organism",
        note=(
            "The route was found computationally, assembled from enzymes drawn "
            "from unrelated organisms, and optimised into a strain. It is the "
            "clearest statement the field has made that metabolism can be "
            "designed rather than merely optimised."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: A TECHNICAL TRIUMPH THAT FAILED COMMERCIALLY
    # =========================================================================
    Milestone(
        2006,
        "Engineered yeast is shown to produce artemisinic acid, the precursor "
        "to the antimalarial artemisinin",
        note=(
            "A landmark: a complex plant terpenoid pathway reconstructed in "
            "yeast and improved by orders of magnitude. It was widely and "
            "reasonably presented as the case that would prove the field's "
            "public value."
        ),
    ),
    Milestone(
        2013,
        "Semi-synthetic artemisinin reaches the market and then fails to "
        "displace the agricultural supply",
        note=(
            "The most instructive failure in this record, because nothing went "
            "wrong scientifically. The strain worked, the process worked, and "
            "the product met specification. It lost to farmers growing sweet "
            "wormwood at a price the fermentation route could not match, "
            "particularly once plant supply and prices responded. Production "
            "was largely idled within a few years. The lessons are recorded "
            "plainly: a working pathway is not a viable product, an "
            "agricultural supply chain with millions of low-cost growers is "
            "harder to displace than it appears, and the value that remained "
            "was as a supply and price buffer rather than as a replacement."
        ),
    ),
    # =========================================================================
    #  EVOLUTION AS A TOOL RATHER THAN AN ADVERSARY
    # =========================================================================
    Milestone(
        2016,
        "Growth-coupled design and adaptive laboratory evolution become "
        "standard industrial practice",
        note=(
            "Strains are designed so that making the product is necessary for "
            "growing, which turns the selective pressure that degrades "
            "engineered strains into the force that maintains them. It is the "
            "field's answer to the genetic stability metric, and it is a "
            "deliberately non-rational method in a discipline that defined "
            "itself by rationality."
        ),
    ),
    Milestone(
        2018,
        "Automated design, build, test and learn foundries operate at hundreds "
        "of strains per cycle",
        note=(
            "Construction stopped being the bottleneck. Measurement and design "
            "quality became it, which is the situation `practice.CHALLENGES` "
            "records and the reason carbon-13 flux analysis matters more now "
            "than it did when strains were built one at a time."
        ),
    ),
    Milestone(
        2022,
        "Gas fermentation of industrial off-gas to ethanol and acetone reaches "
        "commercial operation",
        note=(
            "Carbon monoxide and carbon dioxide as feedstock rather than sugar, "
            "which addresses the food and land competition listed as a "
            "challenge in this record. It is early, and it is the most "
            "significant open direction the field has."
        ),
    ),
)
