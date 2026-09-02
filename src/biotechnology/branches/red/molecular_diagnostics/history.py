# =============================================================================
#  biotechnology.branches.red.molecular_diagnostics.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`. Rule 1 requires that
#  setbacks appear; here that is the 2007 pertussis episode, in which a highly
#  sensitive test produced a hospital outbreak that had never happened.
#
#  SUBTYPE-SPECIFIC NOTE
#  This timeline shows a field whose limiting factor moved twice. Until 1983
#  the problem was detection: there was no way to find a single molecule. From
#  1983 to roughly 2005 the problem was throughput and cost. Since then the
#  problem has been interpretation, and the 2007 and 2011 entries are both
#  about that rather than about chemistry.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  BEFORE AMPLIFICATION
    # =========================================================================
    Milestone(
        1975,
        "Southern describes transfer and hybridisation for detecting specific "
        "DNA sequences",
        note=(
            "The first way to ask a question about one sequence among many. It "
            "needed microgram quantities of material, which is why it never "
            "became a clinical test for a scarce target."
        ),
    ),
    # =========================================================================
    #  AMPLIFICATION: THE FIELD BECOMES POSSIBLE
    # =========================================================================
    Milestone(
        1983,
        "Mullis conceives the polymerase chain reaction",
        note=(
            "The insight was that a single molecule could be turned into a "
            "detectable quantity by repeated doubling. Everything in this "
            "record descends from it."
        ),
    ),
    Milestone(
        1988,
        "Thermostable Taq polymerase from Thermus aquaticus makes PCR "
        "automatable",
        note=(
            "Before this, fresh enzyme had to be added by hand after every "
            "heating step. A thermostable enzyme turned a manual procedure into "
            "a machine, which is what made clinical use conceivable."
        ),
    ),
    Milestone(
        1996,
        "Real-time quantitative PCR instruments become commercially available",
        note=(
            "Reading fluorescence during the reaction rather than analysing the "
            "product afterwards removed the post-amplification handling step "
            "that had been the main source of laboratory contamination."
        ),
    ),
    # =========================================================================
    #  THROUGHPUT: THE FIELD BECOMES CHEAP
    # =========================================================================
    Milestone(
        2005,
        "Massively parallel sequencing platforms reach the market",
        note=(
            "Cost per base fell faster than computing cost per operation over "
            "the following decade, which is unusual enough that it changed what "
            "counted as a reasonable diagnostic question."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: SENSITIVITY WITHOUT INTERPRETATION
    # =========================================================================
    Milestone(
        2007,
        "A PCR-defined pertussis outbreak at a United States hospital is later "
        "found not to have occurred",
        note=(
            "Thousands of staff were treated and furloughed on the basis of a "
            "highly sensitive assay. Culture and serology found almost no real "
            "cases. It is the standard teaching example of a test outrunning "
            "the ability to interpret it, and it is why confirmatory testing "
            "and pre-test probability are now part of every molecular "
            "diagnostic guideline."
        ),
    ),
    # =========================================================================
    #  INTERPRETATION BECOMES THE PROBLEM
    # =========================================================================
    Milestone(
        2011,
        "Non-invasive prenatal testing enters clinical use",
        note=(
            "Technically excellent and immediately misread. Marketed and often "
            "reported as diagnostic, it is a screening test, and for rare "
            "conditions most of its positive results are false. The gap between "
            "its sensitivity and its predictive value became the clearest "
            "public example of the arithmetic in metrics.py."
        ),
    ),
    Milestone(
        2015,
        "Consensus variant interpretation guidelines published for clinical "
        "sequencing",
        note=(
            "An admission that finding variants had become easier than deciding "
            "what they mean, and an attempt to make classification reproducible "
            "between laboratories."
        ),
    ),
    # =========================================================================
    #  DECENTRALISATION
    # =========================================================================
    Milestone(
        2017,
        "CRISPR-based detection demonstrated at attomolar sensitivity without "
        "an instrument",
    ),
    Milestone(
        2020,
        "Molecular testing scaled to billions of assays worldwide within a year",
        note=(
            "Capacity that had taken decades to build in high-income countries "
            "was replicated in months. It also exposed how unevenly that "
            "capacity was distributed, and how much of it depended on a small "
            "number of reagent suppliers."
        ),
    ),
    Milestone(
        2022,
        "Wastewater surveillance adopted as routine public health "
        "infrastructure in several countries",
        note=(
            "A diagnostic technique applied to a population rather than a "
            "patient, and one of the few surveillance methods that does not "
            "depend on anyone deciding to seek care."
        ),
    ),
)
