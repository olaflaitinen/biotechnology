# =============================================================================
#  biotechnology.branches.white.bioprocess_engineering
# -----------------------------------------------------------------------------
#  SUBTYPE ECOSYSTEM:  WHITE BIOTECHNOLOGY  ->  BIOPROCESS ENGINEERING
# -----------------------------------------------------------------------------
#
#  IN ONE SENTENCE, FOR ANYONE
#  Turning something that works in a laboratory flask into something a factory
#  can make the same way every time, including all the separating and
#  purifying that happens after the tank has finished.
#
#  THE THIRD LEG OF A THREE-WAY DIVISION
#      metabolic_engineering   builds the strain      measures the strain
#      microbial_fermentation  grows the strain       measures the culture
#      bioprocess_engineering  builds the plant       measures the process
#
#  The boundary with the middle record is a single quantity. Oxygen transfer
#  appears in both and means opposite things: kLa is what the VESSEL can
#  supply, the oxygen uptake rate is what the ORGANISM demands, and a process
#  works when the first exceeds the second. Two records because, in a real
#  plant, two engineers.
#
#  THE SCALE-UP PARADOX
#  There is no such thing as simply building a bigger vessel. Under geometric
#  similarity the four things an engineer would want to hold constant are
#  mutually incompatible:
#
#      hold power per volume    -> tip speed RISES, and shear-sensitive cells
#                                  are punished by the choice that protects
#                                  their oxygen supply
#      hold tip speed           -> power per volume COLLAPSES, and with it
#                                  oxygen transfer
#      hold mixing time         -> impossible; the power required exceeds what
#                                  is mechanically and thermally feasible
#
#  So mixing time always lengthens with scale, and cells in a large tank
#  circulate through gradients in oxygen, substrate and pH rather than sitting
#  in an average. They respond to the journey, not to the mean. Scale-up is
#  choosing which insult the organism tolerates least. `metrics.py` is ordered
#  so a reader watches this contradiction assemble itself entry by entry.
#
#  THE PART EVERYONE FORGETS: MOST OF THE COST IS AFTER THE TANK
#  For a biological product, purification typically exceeds cultivation in the
#  cost of goods. `practice.APPLICATIONS` lists the unit operations in process
#  order for exactly this reason: count how few concern the fermenter. Buffer
#  preparation and storage frequently size a facility more than the bioreactor
#  does, which is the least discussed constraint in the field.
#
#  THE ARITHMETIC THAT SHAPES EVERY DESIGN
#  Step yields MULTIPLY. Ten steps at ninety per cent give thirty-five per
#  cent, not ninety. Removing an operation is therefore usually worth more than
#  improving one, and a titre gain upstream can be worth less than a single
#  purification step deleted downstream. This one multiplication does more to
#  shape process design than any transport correlation in the record.
#
#  TWO SETBACKS OF DIFFERENT KINDS
#  The first was strategic and shared by an entire industry. Upstream titres
#  for therapeutic proteins rose roughly a hundredfold over fifteen years while
#  downstream capacity did not follow, because chromatography scales with
#  product mass rather than broth volume. Facilities built for the old ratio
#  could not process what the new cell lines made. An industry optimised one
#  end of its own process for a decade without asking what the other end could
#  absorb.
#
#  The second reached patients. In 2009 a virus entered the cell culture
#  operation at a plant that was the sole source of two enzyme replacement
#  therapies for rare inherited diseases. Production stopped and patients were
#  rationed for years. Raw materials are a contamination route into an
#  otherwise closed process, and single-source manufacture of a medicine with
#  no substitute converts an engineering failure directly into patient harm.
#  It is the strongest argument in this library for treating process
#  engineering as a patient safety discipline.
#
#  THE GOVERNANCE IDEA THAT DEFINES THE FIELD
#  FOR A BIOLOGICAL PRODUCT, THE PROCESS IS THE PRODUCT. A small molecule can
#  be fully characterised, so two batches made by different routes can be shown
#  identical. A large biological molecule cannot: glycosylation, charge
#  variants, aggregation and higher order structure depend on how the cells
#  were grown and how the molecule was purified, and no analytical panel fully
#  enumerates what may differ.
#
#  So a process change is treated as a potential product change and must be
#  supported by a comparability exercise. A plant can end up running a process
#  it knows how to improve, because proving the better one equivalent costs
#  more than the improvement returns. This is why the record is REGULATED where
#  its two neighbours are CONTROLLED, and AUTHORISED where they are VARIES.
#
#  PACKAGE LAYOUT
#      narrative.py    the paradox, and why the interesting part is not the
#                      fermenter; the kitchen-to-canteen analogy
#      practice.py     unit operations in PROCESS ORDER, so the count of steps
#                      after the vessel is visible
#      metrics.py      thirteen metrics; the first four are the four that
#                      cannot all be held constant
#      history.py      1943 to 2021, with a strategic setback and a human one
#      governance.py   the process is the product, and what follows from it
#      linkage.py      the three-way division, stated from the last side
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
KEY = "bioprocess_engineering"

NAME = "Bioprocess Engineering"

# "downstream processing" is included because it is where most of the cost and
# most of the equipment sits, and a reader searching for it should arrive here
# rather than assume it belongs to a record about fermentation. "biochemical
# engineering" is the older academic name for the same discipline.
ALIASES = (
    "biochemical engineering",
    "downstream processing",
    "bioprocessing",
    "biomanufacturing engineering",
    "scale up",
    "process development",
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
