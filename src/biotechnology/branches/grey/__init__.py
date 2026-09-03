# =============================================================================
#  biotechnology.branches.grey
# -----------------------------------------------------------------------------
#  GREY BIOTECHNOLOGY - environment, waste and ecological balance.
#
#  WHAT THIS PACKAGE DOES
#  It imports the nine subtype packages beside it and assembles `BRANCH`.
#  Branch-level material only lives here; the substance is in the packages.
#
#  ORDER OF SUBTYPES
#  The order runs from cleaning up contamination, through treating the streams
#  that would become contamination, to measuring whether any of it worked:
#
#      1. clean the ground   bioremediation, bioaugmentation, phytoremediation
#      2. treat the streams  wastewater_treatment, biowaste_treatment,
#                            air_biotreatment
#      3. recover the metal  biomining
#      4. measure it         environmental_biomonitoring
#      5. conserve it        biodiversity_conservation
#
#  THIS IS THE BRANCH THAT CLEANS UP AFTER THE OTHERS
#  Every colour in this library produces a waste stream, and most of them are
#  treated by something in this one. A fermentation plant's spent broth, a
#  mine's drainage, a city's sewage and a farm's run-off all arrive here. That
#  position makes grey biotechnology the most widely deployed branch by volume
#  and the least visible, since success looks like nothing happening.
#
#  THE TRADE THAT DEFINES IT
#
#      BIOLOGICAL TREATMENT IS CHEAP, SLOW AND NARROW.
#      PHYSICAL AND CHEMICAL TREATMENT IS FAST, EXPENSIVE AND GENERAL.
#
#  Biology wins where time is available and the contaminant is something an
#  organism will eat. It loses where the contaminant is a metal, which cannot
#  be destroyed by anything, where the concentration is toxic to the organisms
#  themselves, or where the site must be cleared by a date. Excavation always
#  works and always costs more.
#
#  THE FINDING THAT RECURS ACROSS THE BRANCH
#  Adding organisms to an environment usually does not work. The resident
#  community is there because it is adapted to those conditions, and an
#  introduced strain is generally outcompeted within weeks. That result appears
#  in `grey.bioaugmentation` in full, and the same pattern is recorded in
#  `green.biofertilisers` for soil and `yellow.probiotics_and_prebiotics` for
#  the gut. Three fields, three decades apart, one lesson.
#
#  AND ONE IDEA THAT BELONGS TO NO OTHER BRANCH
#  Monitored natural attenuation is a recognised remediation strategy in which
#  the intervention is measurement. Where the contamination is degrading on its
#  own and nobody is exposed, documenting that is the correct response. It is
#  the only place in this library where doing nothing, carefully, is an
#  approved technology.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ...core.enums import Domain
from ...core.models import Branch, Milestone

from . import (
    air_biotreatment,
    bioaugmentation,
    biodiversity_conservation,
    biomining,
    bioremediation,
    biowaste_treatment,
    environmental_biomonitoring,
    phytoremediation,
    wastewater_treatment,
)

__all__ = ["BRANCH"]


BRANCH = Branch.build(
    key="grey",
    name="Grey Biotechnology",
    colour="#607D8B",
    aliases=(
        "environmental",
        "environmental biotechnology",
        "remediation",
        "waste treatment",
        "pollution control",
        "ecological",
    ),
    domains=(Domain.ENVIRONMENT, Domain.HEALTH, Domain.MATERIALS),
    summary="Environmental cleanup, waste treatment, monitoring and the "
    "biological maintenance of ecological balance.",
    description=(
        "Grey biotechnology uses organisms to remove contamination, treat "
        "waste streams, recover materials and measure environmental condition. "
        "It is the most widely deployed branch in this library by volume and "
        "the least noticed, because every city treats its sewage biologically "
        "and almost nobody thinks of that as biotechnology. Its central trade "
        "is between biological treatment, which is cheap, slow and works only "
        "on what an organism will consume, and physical or chemical treatment, "
        "which is fast, expensive and works on anything. Biology therefore "
        "wins where time is available and the contaminant is degradable, and "
        "loses where a deadline exists, where the concentration is toxic to "
        "the organisms themselves, or where the contaminant is a metal, which "
        "no organism can destroy and which can only be moved, concentrated or "
        "immobilised. The branch also contains the clearest demonstration in "
        "the library that introducing organisms into an established community "
        "usually fails, and one strategy found nowhere else: monitored natural "
        "attenuation, in which the approved intervention is measurement."
    ),
    plain_language=(
        "Grey biotechnology is using living things to clean up. Bacteria eat "
        "the sewage from every city on Earth, which is probably the largest "
        "and least appreciated use of biology anywhere. Other organisms break "
        "down spilled fuel in soil, pull metals out of contaminated ground, "
        "turn food waste into gas that can be burned for energy, and strip the "
        "smell out of air leaving a factory. The same techniques are used to "
        "check whether an environment is healthy, by looking at what is living "
        "in it or by finding traces of DNA in water. It is slow and cheap, "
        "which is the opposite of digging contaminated soil up and taking it "
        "somewhere else."
    ),
    analogy=(
        "It is composting rather than incineration. Both deal with the waste; "
        "one is quick, expensive and works on anything, and the other takes "
        "months, costs very little and only handles what will actually rot. "
        "The choice between them is almost never about which is better in "
        "principle. It is about whether there is time, and whether the thing "
        "in question is the sort of thing that rots at all."
    ),
    why_it_matters=(
        "Biological wastewater treatment protects the water supply of most of "
        "the urban world and is among the largest public health interventions "
        "ever deployed, older than antibiotics and still running. Anaerobic "
        "digestion turns a disposal cost into energy. Bioremediation cleans "
        "contaminated land at a fraction of the cost of excavation, which is "
        "frequently the difference between a site being cleaned and being "
        "fenced off. Biomining recovers copper and other metals from ores too "
        "poor for smelting, without the sulphur dioxide a smelter produces. "
        "And environmental DNA has made it possible to survey what lives in a "
        "river without catching anything. The limits are equally definite. "
        "Metals cannot be destroyed, only relocated, so a metal remediation "
        "produces contaminated biomass that must then be dealt with. "
        "Introduced organisms usually fail to establish. Treatment is slow "
        "enough that a regulatory deadline frequently forces a physical "
        "method. The same acid-generating bacteria that make biomining work "
        "cause acid mine drainage, which is among the most persistent "
        "industrial pollution problems there is. And the branch carries a "
        "structural unfairness: contamination and inadequate treatment fall "
        "hardest on people with the least ability to move away from them."
    ),
    origin_note=(
        "Grey entered the colour scheme for environmental applications, and it "
        "collides with an older usage in which grey denoted INDUSTRIAL "
        "biotechnology, now called white. That collision is recorded in the "
        "white branch's aliases as well as here, because a reader working from "
        "older literature may find the two colours exchanged."
    ),
    key_questions=(
        "When is biological treatment genuinely cheaper than digging it up?",
        "Why does adding organisms to an environment so rarely work?",
        "What is done with a metal that cannot be destroyed?",
        "When is measuring and waiting the correct intervention?",
        "Who lives next to the contamination that is not cleaned up?",
    ),
    milestones=(
        Milestone(1914, "Activated sludge treatment is developed, and becomes "
                        "the process protecting the water supply of most of "
                        "the urban world"),
        Milestone(1947, "The bacteria responsible for acid mine drainage are "
                        "identified, and later turned into a mining technology"),
        Milestone(1972, "Comprehensive water pollution legislation makes "
                        "biological treatment a legal requirement rather than "
                        "a municipal choice"),
        Milestone(1980, "A patent on an oil-degrading bacterium establishes "
                        "that a living organism may be patented"),
        Milestone(1989, "Shoreline bioremediation is deployed at scale after a "
                        "major oil spill"),
        Milestone(1995, "Monitored natural attenuation is accepted as a "
                        "remediation strategy, making measurement an approved "
                        "intervention"),
        Milestone(2010, "Deep-water oil release tests bioremediation under "
                        "conditions nobody had planned for"),
        Milestone(2016, "Environmental DNA becomes an accepted method for "
                        "surveying what lives in a body of water"),
    ),
    sdgs=(6, 12, 14, 15),
    references=(
        "activated_sludge_centenary",
        "bioremediation_field_review",
        "environmental_dna_review",
    ),
    subtypes=(
        # -- clean the ground --------------------------------------------------
        bioremediation.SUBTYPE,
        bioaugmentation.SUBTYPE,
        phytoremediation.SUBTYPE,
        # -- treat the streams -------------------------------------------------
        wastewater_treatment.SUBTYPE,
        biowaste_treatment.SUBTYPE,
        air_biotreatment.SUBTYPE,
        # -- recover the metal -------------------------------------------------
        biomining.SUBTYPE,
        # -- measure it --------------------------------------------------------
        environmental_biomonitoring.SUBTYPE,
        # -- conserve it -------------------------------------------------------
        biodiversity_conservation.SUBTYPE,
    ),
)
