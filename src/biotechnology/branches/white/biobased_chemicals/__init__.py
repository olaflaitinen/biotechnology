# =============================================================================
#  biotechnology.branches.white.biobased_chemicals
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  BIOBASED CHEMICALS
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Making the chemicals behind plastics, fibres, solvents and coatings from
#  plants, sugar and waste instead of from oil.
#
#  THE PRINCIPLE THAT EXPLAINS THIS WHOLE RECORD
#
#      SUGAR IS ALREADY OXYGENATED. PETROLEUM IS NOT.
#
#  Glucose carries roughly one oxygen per carbon; a hydrocarbon carries none.
#  So a petrochemical route to an oxygen-rich molecule, a diacid or a diol,
#  must ADD oxygen through several selective oxidation steps, each losing yield.
#  A biological route starts most of the way there. And the reverse holds:
#  making a pure hydrocarbon from sugar means stripping out oxygen the feedstock
#  is full of, wasting carbon as carbon dioxide.
#
#  That one asymmetry predicts, with uncomfortable accuracy, which biobased
#  chemicals succeeded and which did not. `metrics.py` therefore opens with a
#  property of the TARGET MOLECULE rather than of the process: checking the
#  oxygen to carbon ratio takes a minute and has more predictive power about
#  commercial outcome than a year of strain improvement.
#
#  IT ALSO EXPLAINS WHY THIS RECORD READS BETTER THAN `white.biofuels`
#  The two share feedstocks, organisms, vessels and most of the engineering.
#  They differ only in the target, and a fuel is a hydrocarbon, which is the
#  worst possible target for a route that begins with sugar. Chemicals are also
#  a much smaller share of petroleum use and worth several times more per
#  tonne, so the same hectare of land displaces far more fossil carbon. And a
#  carbon atom that ends up in a material is displaced permanently rather than
#  burned.
#
#  A CORRECTION THE HISTORY FACET OPENS WITH
#  The chemical industry BEGAN biobased. Acetone, butanol, ethanol, citric acid
#  and glycerol were fermentation products before they were petrochemical ones,
#  and the switch happened mid-century on cost alone. This field is not
#  inventing something new; it is reversing a substitution that already
#  happened once, against an incumbent that has since had seventy years to
#  optimise. The petrochemical route is not the naive option. It is the
#  previous winner.
#
#  THE SETBACK, WHICH IS OF AN UNUSUAL KIND
#  In 2004 a national laboratory published a list of top value-added chemicals
#  from biomass. The chemistry was sound and the influence enormous. Succinic
#  acid was among the most prominent entries: oxygen-rich, fermentable at good
#  yield, a plausible route to many products. Four companies built commercial
#  capacity from 2012. By 2019 most had closed, sold or entered insolvency.
#
#  The plants ran. The downstream market did not appear, the incumbent maleic
#  anhydride route stayed cheap, and oil prices fell during the scale-up
#  window. The lesson is precise and travels far beyond this molecule: BEING A
#  GOOD CHEMICAL PLATFORM IS NOT THE SAME AS HAVING A MARKET.
#
#  THE GOVERNANCE FACT NEWCOMERS GET WRONG
#  A biobased chemical is regulated as a chemical, with no concession for being
#  biological. An identical molecule carries the same registration, hazard class
#  and exposure limits, because the origin of the carbon changes nothing about
#  the toxicology. And a NOVEL biobased molecule is WORSE off than the
#  incumbent: it needs its own registration and toxicological dossier, paid for
#  by a new entrant, while the product it competes with was registered decades
#  ago. The system is not hostile to biobased chemistry; it is indifferent, and
#  indifference favours whoever is already there.
#
#  ONE ADVANTAGE OVER THE FUELS RECORD
#  The biobased claim here can be VERIFIED ON THE PRODUCT. Radiocarbon has
#  decayed away in fossil carbon and is present in recently fixed carbon, so
#  biobased content is a physical measurement. Contrast `white.biofuels`, where
#  a litre of ethanol carries no evidence of how its crop was grown and
#  compliance must be audited through the supply chain instead.
#
#  PACKAGE LAYOUT
#      narrative.py    the oxygen principle, and the half-built analogy that
#                      carries it without chemistry
#      practice.py     applications ordered BY THAT PRINCIPLE, oxygen-rich
#                      first and hydrocarbons last, so it is demonstrated
#                      rather than asserted
#      metrics.py      eleven metrics, opening with a property of the target
#                      molecule; economics before environment, which is the
#                      honest description of how the field decides
#      history.py      1916 to 2022, opening with the industry leaving and
#                      centring on the succinic acid case
#      governance.py   regulated as a chemical, with no concession
#      linkage.py      the biofuels edge read as a comparison
#
#  The full facet contract is documented in
#  `branches/red/gene_therapy/__init__.py` and is identical for all eighty-five
#  subtype packages in this library.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from ....core.models import Subtype

from . import governance, history, linkage, metrics, narrative, practice

__all__ = ["SUBTYPE"]


# =============================================================================
#  IDENTITY
# =============================================================================
KEY = "biobased_chemicals"

NAME = "Biobased Chemicals"

# "renewable chemicals" is the commercial term and "green chemicals" the
# marketing one; both should resolve here. "biorefinery" is included because a
# reader searching for the integrated feedstock-to-products concept belongs in
# this record rather than in the fuels one.
ALIASES = (
    "renewable chemicals",
    "green chemicals",
    "bio-based chemicals",
    "platform chemicals",
    "biorefinery",
    "industrial biochemicals",
)


# =============================================================================
#  ASSEMBLY
# =============================================================================
SUBTYPE = Subtype(
    # -- identity --------------------------------------------------------------
    key=KEY,
    name=NAME,
    aliases=ALIASES,
    # -- narrative.py ----------------------------------------------------------
    summary=narrative.SUMMARY,
    description=narrative.DESCRIPTION,
    plain_language=narrative.PLAIN_LANGUAGE,
    analogy=narrative.ANALOGY,
    why_it_matters=narrative.WHY_IT_MATTERS,
    # -- practice.py -----------------------------------------------------------
    applications=practice.APPLICATIONS,
    technologies=practice.TECHNOLOGIES,
    organisms=practice.ORGANISMS,
    techniques=practice.TECHNIQUES,
    challenges=practice.CHALLENGES,
    # -- metrics.py ------------------------------------------------------------
    metrics=metrics.METRICS,
    formulas=metrics.FORMULAS,
    # -- history.py ------------------------------------------------------------
    milestones=history.MILESTONES,
    # -- governance.py ---------------------------------------------------------
    maturity=governance.MATURITY,
    risk_tier=governance.RISK_TIER,
    scale=governance.SCALE,
    domains=governance.DOMAINS,
    regulatory_status=governance.REGULATORY_STATUS,
    regulations=governance.REGULATIONS,
    standards=governance.STANDARDS,
    # -- linkage.py ------------------------------------------------------------
    sdgs=linkage.SDGS,
    glossary=linkage.GLOSSARY,
    references=linkage.REFERENCES,
    related=linkage.RELATED,
)
