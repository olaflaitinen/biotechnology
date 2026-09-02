# =============================================================================
#  biotechnology.branches.red.cell_therapy.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Cell therapy and gene therapy are the two records in this library most
#  often confused with each other, including by people who work in the field.
#  The DESCRIPTION below therefore opens by fixing the boundary explicitly -
#  the medicine is the cell, not the DNA - and the ANALOGY is chosen to make
#  the "living, dividing, persisting" property vivid, because that property is
#  what separates a cell therapy from every other kind of medicine ever made.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
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
    "Using living cells as the therapeutic agent, autologous or allogeneic, "
    "often after genetic modification to redirect their function."
)

DESCRIPTION = (
    # (a) the boundary
    "In a cell therapy the medicine is a population of living cells. The "
    "source may be autologous, harvested from the patient who will receive "
    "them, or allogeneic, taken from a healthy donor. Where the cells are also "
    "gene-modified the product is regulated as a gene therapy medicinal "
    "product in the European Union, which is why the two fields are so often "
    "conflated; the distinction kept here is that this record concerns the "
    "sourcing, expansion, potency and delivery of the cells themselves. "
    # (b) the three families
    "Three families dominate clinical practice. Haematopoietic stem cell "
    "transplantation, in use since the 1950s, replaces a patient's entire "
    "blood-forming system. Adoptive immune cell transfer arms T cells or "
    "natural killer cells against a chosen antigen, most famously through a "
    "chimeric antigen receptor that fuses an antibody binding domain to "
    "intracellular signalling domains. Stromal and progenitor cell products, "
    "typically mesenchymal, act mainly by secreting immunomodulatory factors "
    "rather than by engrafting at all. "
    # (c) what makes manufacture unlike anything else
    "The manufacturing problem is unlike that of any other medicine: an "
    "autologous product is a batch of one, made under time pressure for a "
    "named patient whose disease is progressing, and every release assay must "
    "complete before the cells lose potency. "
    # (d) where the field is going
    "Allogeneic and induced pluripotent stem cell derived products aim to "
    "convert this bespoke model into a conventional inventory one, at the "
    "cost of having to suppress or engineer away immune rejection."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Doctors take living cells - usually white blood cells drawn from the "
    "patient - and treat them in a laboratory so that they can recognise and "
    "attack a disease they previously ignored. The cells are grown until "
    "there are enough of them and then infused back into the same person, "
    "where they keep working, dividing and hunting for as long as they "
    "survive. The treatment is a living thing rather than a chemical, which "
    "is why it can keep acting for years after a single infusion, and also "
    "why it cannot simply be made in advance and kept on a shelf."
)

ANALOGY = (
    "It is closer to retraining a police force than to spraying a pesticide. "
    "The officers already exist and already patrol the streets; they simply "
    "were not looking for this particular offender. Cell therapy sends them "
    "on a course and returns them to the same streets, where they continue "
    "working, recruit colleagues, and remain on duty long after the training "
    "budget has been spent."
)

WHY_IT_MATTERS = (
    "For some blood cancers that had exhausted every other option, a single "
    "CAR-T infusion produces lasting remission in roughly four out of ten "
    "patients. No chemical drug had achieved a result in that category. The "
    "counterweight is cost and access: manufacturing is bespoke and cannot "
    "benefit from ordinary economies of scale, the list price sits in the "
    "high hundreds of thousands of euro, and treatment can only be given at "
    "accredited centres, so geography decides eligibility as much as biology "
    "does. Solid tumours, which are most cancers, remain largely out of reach."
)
