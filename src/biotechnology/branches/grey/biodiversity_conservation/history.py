# =============================================================================
#  biotechnology.branches.grey.biodiversity_conservation.history
# -----------------------------------------------------------------------------
#  FACET 4 OF 6:  HISTORY
#
#  Editorial rules: `red/gene_therapy/history.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE FIELD'S TWO DEFINING EPISODES ARE BOTH ABOUT THE SAME QUESTION, ASKED
#  TWENTY YEARS APART, AND THEY GOT OPPOSITE ANSWERS.
#
#      1987  the dusky seaside sparrow goes extinct while a hybridisation
#            programme is argued over. Caution cost the taxon.
#      1995  Texas panthers are introduced into the inbred Florida population.
#            It works. The Florida panther is no longer purely what it was.
#
#  The question in both cases is whether to mix a failing population with a
#  related one. In the first, the delay was fatal. In the second, the
#  intervention succeeded and permanently altered the thing it saved. Neither
#  case makes the other wrong, and reading them together is the most useful
#  thing this timeline offers.
#
#  RULE 1 REQUIRES SETBACKS AND THE 1987 ENTRY IS A GENUINE ONE. It is recorded
#  as a failure of decision-making under uncertainty rather than as anyone's
#  incompetence: the objection to hybridisation was a legitimate one about
#  taxonomic integrity, and while it was resolved the last animals died.
#
#  A SECOND SETBACK IS RECORDED FOR 2003. The first cloning of an extinct
#  subspecies produced an animal that lived for minutes, and it is included
#  because the coverage it received bore no relation to what had been achieved,
#  which is a pattern this record's `narrative.py` identifies as the field's
#  deepest problem of attention.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.models import Milestone

__all__ = ["MILESTONES"]


MILESTONES: Tuple[Milestone, ...] = (
    # =========================================================================
    #  NOTICING THAT SMALL POPULATIONS FAIL FOR GENETIC REASONS
    # =========================================================================
    Milestone(
        1973,
        "Endangered species legislation creates a legal framework for listing "
        "and protection",
        note=(
            "Not a biotechnology, and the reason most of what follows has "
            "funding and legal standing. It also created the definitional "
            "problem this record repeatedly returns to, since protecting a "
            "listed unit requires deciding what the unit is, and that turned "
            "out to be a genetic question."
        ),
    ),
    Milestone(
        1979,
        "Inbreeding depression is documented in captive populations of "
        "ungulates",
        note=(
            "Systematic comparison of zoo records found that inbred offspring "
            "survived less well than outbred ones across many species. It "
            "established that small populations fail for genetic reasons "
            "independently of their habitat, which is the observation the whole "
            "field rests on."
        ),
    ),
    Milestone(
        1983,
        "The first frozen zoo cell line collections are established",
        note=(
            "Systematic banking of cultured cell lines from threatened species, "
            "begun before there was any application for the material. It is the "
            "clearest case in this library of preserving an option rather than "
            "using one, and the material collected then is being sequenced and "
            "used now for purposes nobody anticipated."
        ),
    ),
    # =========================================================================
    #  THE SETBACK: CAUTION COST THE TAXON
    # =========================================================================
    Milestone(
        1987,
        "The dusky seaside sparrow becomes extinct while a hybridisation "
        "programme is contested",
        note=(
            "The last individuals were males, and a proposal to cross them with "
            "a closely related subspecies was contested on the grounds that the "
            "result would not be the protected taxon. The objection was "
            "legitimate. While it was being resolved the animals died, and the "
            "opportunity closed permanently. It is recorded as a failure of "
            "decision-making under uncertainty rather than as anyone's error, "
            "and it changed how the field weighs the cost of delay."
        ),
    ),
    # =========================================================================
    #  THE CHEAPEST INTERVENTION IN THE RECORD: FINDING OUT WHAT THE UNIT IS
    # =========================================================================
    Milestone(
        1994,
        "Molecular markers begin resolving conservation units and revealing "
        "misclassification",
        note=(
            "Sequence data showed repeatedly that protected units were defined "
            "wrongly: populations assumed distinct were not, and populations "
            "assumed connected were separate species. Correcting a designation "
            "is among the cheapest interventions available and it redirected "
            "substantial effort, which makes it a larger contribution than most "
            "of the laboratory work in this record."
        ),
    ),
    # =========================================================================
    #  THE ANSWER GOING THE OTHER WAY
    # =========================================================================
    Milestone(
        1995,
        "Genetic rescue of the Florida panther by introducing individuals from "
        "a Texas population",
        note=(
            "A population reduced to a few dozen animals showed heart defects, "
            "reproductive failure and other signs of severe inbreeding. Eight "
            "females from the closest surviving population were released, and "
            "the population subsequently grew and the defects declined. It is "
            "the field's clearest demonstrated success, and the population that "
            "recovered is not genetically what was there before, which is the "
            "cost the decision accepted."
        ),
    ),
    # =========================================================================
    #  THE SECOND SETBACK: AN ANIMAL THAT LIVED FOR MINUTES
    # =========================================================================
    Milestone(
        2003,
        "An extinct wild goat subspecies is cloned and the animal dies shortly "
        "after birth",
        note=(
            "Somatic cell nuclear transfer using preserved tissue produced a "
            "live birth, and the animal died within minutes from a lung defect. "
            "It is the only case of an extinct taxon being briefly restored, "
            "and it is included because the coverage it received bore little "
            "relation to what had been achieved. A single animal that cannot "
            "breathe is not a recovered species, and the gap between the result "
            "and its reception is the attention problem this record's narrative "
            "identifies."
        ),
    ),
    # =========================================================================
    #  THE TOOLS GET CHEAP, AND THAT CHANGES WHAT IS POSSIBLE
    # =========================================================================
    Milestone(
        2008,
        "Environmental DNA is demonstrated for aquatic species detection",
        note=(
            "Recorded here as well as in `grey.environmental_biomonitoring` "
            "because it changed conservation practice more than any laboratory "
            "technique in this record. Survey without capture made it possible "
            "to look for rare species affordably and to detect invaders early, "
            "which is where an intervention can still work."
        ),
    ),
    Milestone(
        2010,
        "Population genomics becomes affordable for species with no prior "
        "genomic resources",
        note=(
            "Reduced representation sequencing brought genome-scale data within "
            "reach for animals that had never been studied genetically. It "
            "replaced inference from a handful of markers with direct "
            "measurement of inbreeding, relatedness and gene flow, and it "
            "turned the metrics in this record from estimates into "
            "observations."
        ),
    ),
    Milestone(
        2014,
        "Museum specimen sequencing recovers pre-decline genetic baselines",
        note=(
            "Sequencing historical specimens supplies the value of genetic "
            "diversity before a population collapsed, which no contemporary "
            "sample can provide. It is the direct answer in this record to the "
            "shifting baseline problem that "
            "`grey.environmental_biomonitoring` records as structural."
        ),
    ),
    # =========================================================================
    #  THE PROPOSALS THAT ARE NOT YET PRACTICE
    # =========================================================================
    Milestone(
        2016,
        "Gene drive suppression of invasive island populations is proposed and "
        "the governance problem is recognised as unresolved",
        note=(
            "Self-propagating genetic elements could in principle remove "
            "invasive rodents from islands where poisoning is impractical. No "
            "such release has occurred. The unresolved question is that a drive "
            "does not respect a property boundary or a national one, and the "
            "self-limiting and reversal designs developed since exist because "
            "the field recognises the problem rather than because it has solved "
            "it."
        ),
    ),
    Milestone(
        2020,
        "Blight-resistant American chestnut reaches regulatory review",
        note=(
            "A tree engineered to tolerate an introduced fungal pathogen, "
            "submitted for approval to be planted in wild forests. It is the "
            "furthest any engineered organism has advanced toward deliberate "
            "release for a conservation purpose, and it raises the question "
            "squarely: restoring a functionally extinct species requires "
            "releasing an organism that is not quite the one that was lost."
        ),
    ),
    Milestone(
        2021,
        "Cloning from decades-old banked cell lines produces live individuals "
        "of endangered species",
        note=(
            "Animals were produced from cell lines frozen in the 1980s, "
            "reintroducing genetic variation that had been absent from the "
            "living population for a generation. It is the first substantial "
            "return on the banking begun in 1983, and it vindicates preserving "
            "material before there is any use for it."
        ),
    ),
)
