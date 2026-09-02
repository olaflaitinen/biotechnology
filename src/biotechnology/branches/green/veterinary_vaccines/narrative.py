# =============================================================================
#  biotechnology.branches.green.veterinary_vaccines.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record is the clearest instance of One Health in the taxonomy, and the
#  public register is built around that rather than around veterinary
#  medicine. Roughly three quarters of emerging human infectious diseases
#  originate in animals, so an outbreak stopped in a poultry shed is an
#  outbreak that never reaches a hospital.
#
#  The record also carries a fact that surprises most readers and belongs
#  early: vaccinating animals is one of the largest levers on human
#  antimicrobial resistance. An animal that does not become ill needs no
#  antibiotic, and veterinary antimicrobial sales in the European Union have
#  more than halved since 2011, largely through vaccination and husbandry
#  rather than through prohibition.
#
#  The smoke detector analogy is chosen because it captures the externality
#  precisely: the benefit accrues to people who did not pay for it.
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
    "Vaccines, diagnostics and therapeutics for farm and companion animals, "
    "central to controlling zoonoses and reducing antibiotic use."
)

# -----------------------------------------------------------------------------
#  Structure: (a) the shared platforms and the different constraints,
#  (b) the DIVA requirement, which has no human equivalent, (c) what else the
#  field covers, (d) the binding constraint.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) same platforms, different constraints
    "Veterinary vaccinology shares its platform technologies with human "
    "vaccinology and operates under entirely different constraints. Cost per "
    "dose is measured in cents rather than euro. Administration must work on "
    "thousands of animals an hour, which favours drinking water, spray, in-ovo "
    "and needle-free routes over individual injection. And the endpoint is "
    "usually transmission control across a herd or flock rather than protection "
    "of an individual, so a vaccine that reduces shedding without preventing "
    "infection can still be exactly what is wanted. "
    # (b) DIVA
    "One requirement has no human equivalent and shapes the whole field. A "
    "country with disease-free trading status loses it if its animals test "
    "positive, and a conventional vaccine makes vaccinated animals "
    "indistinguishable from infected ones. DIVA vaccines, meaning "
    "differentiating infected from vaccinated animals, solve this by deleting a "
    "non-essential antigen from the vaccine strain and testing for antibodies "
    "against it. Vaccinated animals lack that response; infected ones have it. "
    "This is a technical solution to a trade problem, and without it many "
    "countries would rather cull than vaccinate. "
    # (c) the rest of the field
    "Beyond vaccines the field covers herd-level molecular diagnostics, "
    "autogenous vaccines made from an isolate taken on the affected farm, "
    "parasite control, and the alternatives to antibiotic growth promoters that "
    "have displaced routine medication across Europe. "
    # (d) the constraint
    "The binding constraint is economic rather than immunological. A product "
    "must be developed, licensed and manufactured for a market that will pay a "
    "few cents a dose, and the diseases with the greatest global burden are "
    "concentrated in the countries least able to pay. Technical feasibility is "
    "rarely what decides whether a veterinary vaccine exists."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Farm animals are vaccinated for the same reason children are: it is "
    "cheaper and kinder to prevent an illness than to treat it. There are two "
    "extra reasons on a farm. First, a sick herd is a food supply problem, not "
    "only an animal problem. Second, most new human diseases start in animals, "
    "so stopping an infection in a poultry shed can stop it ever reaching "
    "people. Vaccinating animals also means fewer antibiotics are used, and "
    "that matters to everyone, because the more antibiotics are used anywhere "
    "the faster bacteria learn to survive them."
)

# -----------------------------------------------------------------------------
#  The smoke detector analogy. Chosen because the externality is the point:
#  the benefit is largely captured by people who did not pay for it, which is
#  exactly why this field is chronically underfunded.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is fitting smoke detectors in every flat of a building rather than only "
    "in your own. The fire that never starts next door is the one that never "
    "spreads to you. The comparison carries the awkward part too: most of the "
    "benefit goes to neighbours who paid nothing, which is precisely why "
    "somebody has to organise it collectively and why individual farmers cannot "
    "be expected to fund it alone."
)

WHY_IT_MATTERS = (
    "Rinderpest, a cattle disease that caused famines across Africa and Asia "
    "for centuries, was eradicated in 2011 by vaccination. It is the second "
    "disease of any species ever eradicated, and the first was smallpox. Avian "
    "influenza control in poultry is the front line against a virus with "
    "pandemic potential in humans. And veterinary antimicrobial use, which in "
    "some countries once exceeded human use by weight, has more than halved "
    "across the European Union since 2011, largely because vaccination and "
    "better husbandry replaced routine medication. The costs are structural. "
    "Trade rules in several disease categories penalise vaccination by removing "
    "disease-free status, so countries cull healthy animals rather than "
    "vaccinate them, which is expensive, wasteful and hard to defend on welfare "
    "grounds. Cold chains fail first in the places with the highest disease "
    "burden. Wildlife reservoirs cannot be reached by any vaccination "
    "programme aimed at livestock. And because the benefit is largely a public "
    "good captured by people who did not pay for it, the field is "
    "systematically underfunded relative to what it prevents."
)
