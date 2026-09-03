# =============================================================================
#  biotechnology.branches.yellow.nutrigenomics.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires setbacks,
#  and this record has three: a replication failure across the field, a
#  definitive null trial, and a finding that the field's central premise was
#  less predictive than an entirely different variable.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE SHAPE OF THIS TIMELINE IS THE FINDING.
#
#  Its two strongest results, phenylketonuria screening and lactase
#  persistence, are from 1963 and the decades around it. They predate the field
#  acquiring a name in 2000, they are monogenic, and they concern large
#  effects.
#
#  Everything after 2000 divides into mechanistic research that has been
#  productive and made no individual predictions, and a predictive commercial
#  programme that has repeatedly failed to replicate. The field's best results
#  are old, and its marketing is new.
#
#  A NOTE ON ATTRIBUTION. Rule 8 forbids crediting simultaneous discovery to
#  one group, and the 2000 entry is deliberately not attributed: the term and
#  the framing emerged from several groups at once during the sequencing of the
#  human genome, and no single origin is defensible.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  THE STRONGEST RESULTS, AND THEY ARE OLD
    # =========================================================================
    Milestone(
        1934,
        "Phenylketonuria is described as an inherited metabolic disorder",
        note=(
            "A single gene, a single dietary component, and permanent "
            "neurological damage if the two meet. It is the archetype of a "
            "gene-diet interaction and it was identified decades before anyone "
            "used that phrase."
        ),
    ),
    Milestone(
        1963,
        "Newborn screening for phenylketonuria is introduced at population "
        "scale",
        note=(
            "A blood spot taken days after birth, followed by lifelong dietary "
            "management, prevents irreversible intellectual disability "
            "entirely. It remains the clearest demonstration anywhere that a "
            "gene-diet interaction can be identified and acted upon, and it is "
            "sixty years old."
        ),
    ),
    Milestone(
        1965,
        "Lactase persistence is characterised as a genetic trait",
        note=(
            "The recognition that continued lactase production into adulthood "
            "is the derived condition and that most of the world's adults are "
            "the norm rather than the exception. It reframed a supposed "
            "abnormality as a population difference, which is the most useful "
            "thing population genetics has done for nutrition."
        ),
    ),
    # =========================================================================
    #  THE FIELD ACQUIRES A NAME AND A PROMISE
    # =========================================================================
    Milestone(
        2000,
        "Nutrigenomics is named as a field alongside the sequencing of the "
        "human genome",
        note=(
            "The term and its framing emerged from several groups at once and "
            "no single origin is defensible. The promise attached to it was "
            "that the monogenic successes above would generalise into "
            "individualised dietary guidance, which is the proposition the rest "
            "of this timeline tests."
        ),
    ),
    Milestone(
        2004,
        "Direct-to-consumer genetic tests offering dietary advice reach the "
        "market",
        note=(
            "Products appeared years before the evidence base they implied. "
            "Regulatory attention followed, including investigations finding "
            "that recommendations were generic advice with genetic "
            "justification attached rather than conclusions from the genotype."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE INTERACTIONS DO NOT REPLICATE
    # =========================================================================
    Milestone(
        2010,
        "Large-scale replication efforts find that most published gene-diet "
        "interactions do not hold",
        note=(
            "As genome-wide association studies established the discipline of "
            "replication and adequate power, the earlier candidate-gene "
            "interaction literature was tested and largely did not survive. The "
            "reason is arithmetic rather than misconduct: detecting an "
            "interaction requires roughly four times the sample of a main "
            "effect, and gene-diet interactions are smaller than main effects "
            "to begin with. Recorded as a setback because the commercial layer "
            "of the field continued selling results the research layer had "
            "abandoned."
        ),
    ),
    # =========================================================================
    #  THE MECHANISTIC HALF, WHICH KEPT WORKING
    # =========================================================================
    Milestone(
        2008,
        "Epigenetic effects of prenatal nutrition are demonstrated in historical "
        "famine cohorts",
        note=(
            "Differences in DNA methylation decades after prenatal exposure to "
            "famine, in people whose mothers were pregnant during a documented "
            "period of severe undernutrition. It is mechanistic nutrigenomics "
            "at its most convincing, and it makes no prediction about any "
            "individual's diet."
        ),
    ),
    Milestone(
        2014,
        "Mendelian randomisation becomes established for testing dietary causal "
        "hypotheses",
        note=(
            "Using genetic variants as instruments to test whether a dietary "
            "exposure causes an outcome, rather than to personalise advice. It "
            "is the field's most productive use of genetics and it points in "
            "the opposite direction from consumer testing: it uses genotype to "
            "learn about diets in general rather than about individuals."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE TRIAL
    # =========================================================================
    Milestone(
        2018,
        "A large randomised trial finds no advantage to genotype-matched weight "
        "loss diets",
        note=(
            "Participants assigned to low-fat or low-carbohydrate diets by "
            "genotype pattern did no better than those assigned otherwise. "
            "Adequately powered, preregistered, and unambiguous. It is the "
            "clearest single piece of evidence against the commercial premise "
            "of this record, and a null result of this quality is worth more "
            "than a great many positive small studies."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: THE PREMISE WAS THE WRONG ONE
    # =========================================================================
    Milestone(
        2015,
        "Postprandial responses are shown to vary greatly between individuals "
        "and to be predicted substantially by the gut microbiome",
        note=(
            "People eating identical meals showed large and reproducible "
            "differences in glucose response, and predictive models built from "
            "microbiome, meal composition and behavioural features performed "
            "well. It established that personalised nutrition has something "
            "real to personalise. Recorded as a setback for this record "
            "specifically because genetics contributed modestly, which is an "
            "uncomfortable result for a field named after genomes."
        ),
    ),
    Milestone(
        2021,
        "Large personalised nutrition studies confirm that microbiome and "
        "behavioural features predict dietary response better than genotype",
        note=(
            "Consistent with the 2015 finding at larger scale. The research "
            "half of the field has broadly accepted the implication and moved "
            "towards multi-modal prediction; the commercial half has been "
            "slower, and tests sold on DNA alone remain widely available."
        ),
    ),
    # =========================================================================
    #  WHERE THE FIELD STANDS
    # =========================================================================
    Milestone(
        2020,
        "Polygenic score portability across ancestries is documented as a "
        "systematic limitation",
        note=(
            "Scores derived overwhelmingly in European-ancestry cohorts perform "
            "substantially worse in others, so a consumer test is least "
            "informative for the populations least represented in the "
            "underlying research. It is the same equity failure "
            "`gold.genomics_data_analysis` records, reaching consumers "
            "directly."
        ),
    ),
    Milestone(
        2023,
        "Genetic privacy concerns reach consumer nutrition testing",
        note=(
            "A dietary test is a genetic test, and the data is retained, "
            "shared and in some cases sold under commercial terms rather than "
            "clinical ones. Regulatory attention followed data breaches and "
            "changes of corporate ownership in the consumer genomics sector, "
            "which is why `linkage.py` treats "
            "`purple.genetic_data_privacy` as a binding edge rather than a "
            "cross-reference."
        ),
    ),
)
