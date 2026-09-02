# =============================================================================
#  biotechnology.branches.red.vaccine_development.narrative
# -----------------------------------------------------------------------------
#  FACET 1 OF 6:  NARRATIVE
#
#  Contract and editorial rules: `red/gene_therapy/narrative.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  Vaccination is the single intervention with the largest measured effect on
#  human mortality after clean water, and it is also the subject of more public
#  misunderstanding than any other record in this taxonomy. The public register
#  below is written with that second fact in mind: it explains the mechanism
#  before it explains the benefit, because a reader who does not understand how
#  a vaccine works cannot evaluate a claim about one.
#
#  The fire drill analogy is chosen because it makes the memory property
#  obvious, which is the part people miss. It also has a visible limit: a fire
#  drill teaches people a route, whereas immunity is a physical change in the
#  body, and the text does not depend on that distinction being hidden.
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
    "Design, manufacture and evaluation of prophylactic and therapeutic "
    "vaccines across live, subunit and nucleic-acid platforms."
)

# -----------------------------------------------------------------------------
#  Structure: (a) definition, (b) the platforms, (c) how antigen design works
#  in practice, (d) the constraint that shapes the field.
# -----------------------------------------------------------------------------
DESCRIPTION = (
    # (a) definition
    "A vaccine presents the adaptive immune system with an antigen under "
    "conditions that generate immunological memory without causing disease. "
    # (b) the platforms
    "Platforms differ in how the antigen is supplied. Live attenuated vaccines "
    "use a weakened replicating organism and give the broadest and "
    "longest-lasting response, but cannot be given to everyone. Inactivated "
    "whole-organism vaccines are safer and weaker. Subunit, recombinant protein "
    "and virus-like particle vaccines present only the relevant antigen and "
    "depend on an adjuvant for potency. Conjugate vaccines couple a bacterial "
    "polysaccharide to a carrier protein to recruit T-cell help, which is what "
    "makes them work in infants. Viral vector vaccines use a "
    "replication-defective virus to deliver the antigen gene. Nucleic-acid "
    "vaccines deliver messenger RNA in a lipid nanoparticle, so that the "
    "recipient's own cells transiently make the antigen. "
    # (c) modern antigen design
    "Modern antigen design is increasingly structure-guided: stabilising a "
    "viral fusion protein in its prefusion conformation can raise neutralising "
    "titres by an order of magnitude relative to the wild-type sequence, which "
    "is a design gain rather than a manufacturing one. "
    # (d) the binding constraint
    "The binding constraint is not immunogenicity but deployment. A vaccine "
    "that works is only useful once it has been made in the hundreds of "
    "millions of doses, kept cold across a continent, and accepted by the "
    "people it is offered to."
)


# =============================================================================
#  PUBLIC REGISTER
# =============================================================================

PLAIN_LANGUAGE = (
    "Your immune system learns by experience. Once it has met a germ it "
    "remembers the encounter and responds much faster the next time. A vaccine "
    "arranges that first meeting safely. It shows the body a piece of the germ, "
    "or instructions for making one harmless piece of it, so the immune system "
    "builds its memory without you ever being ill. Some vaccines use a weakened "
    "version of the germ itself. Newer ones send a short message that your cells "
    "read once and then break down, leaving nothing behind except the memory."
)

# -----------------------------------------------------------------------------
#  The fire drill. Its limit is deliberately visible: a drill teaches a route,
#  while immunity is a physical change. Nothing in the text depends on the
#  reader missing that.
# -----------------------------------------------------------------------------
ANALOGY = (
    "It is a fire drill. Nobody sets the building alight; everyone simply walks "
    "the escape route once, in calm conditions, so that when smoke does appear "
    "the response is automatic instead of improvised. The comparison breaks "
    "down in one useful way: a drill only teaches people what to do, whereas a "
    "vaccine physically changes what the body is able to do."
)

WHY_IT_MATTERS = (
    "Smallpox killed an estimated three hundred million people in the twentieth "
    "century alone and no longer exists outside two freezers. Routine childhood "
    "immunisation is credited with preventing several million deaths a year. "
    "During the COVID-19 pandemic the interval between publishing a viral "
    "sequence and dosing the first trial participant fell to sixty-three days, "
    "which permanently changed what counts as a realistic response time to a "
    "new pathogen. Against that: doses reached high-income countries roughly a "
    "year before they reached low-income ones, cold chain requirements still "
    "exclude the places with the weakest health systems, and organised "
    "misinformation has pushed measles coverage below the level that stops "
    "transmission in several countries that had eliminated it."
)
