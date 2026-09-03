# =============================================================================
#  biotechnology.branches.grey.air_biotreatment.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  THE TWO FIRST EDGES ARE THE FACILITIES THIS RECORD EXISTS TO KEEP OPEN.
#
#  A wastewater works and a digester have to be near the population whose waste
#  they take, and both smell. Odour abatement is regularly the planning
#  condition on which permission rests. So this record is not merely adjacent
#  to those two: it is frequently the reason they are allowed to be where they
#  are, which is a stronger relationship than the process similarity that
#  usually justifies an edge.
#
#  `grey.bioremediation` is linked through a direct physical connection rather
#  than an analogy. Soil vapour extraction strips volatile contaminant out of
#  the ground and produces a contaminated air stream, and this record is what
#  treats it. The two are stages of one operation.
#
#  `white.bioprocess_engineering` is the methods edge. Gas-liquid mass transfer
#  is the governing physics of both records, approached from opposite
#  directions: that record works to get oxygen INTO a liquid where organisms
#  are, and this one works to get a contaminant OUT of a gas and into the water
#  film where organisms are. The same coefficient limits both.
#
#  `blue.marine_biofouling_control` IS DELIBERATELY NOT LINKED despite both
#  records being about biofilms on surfaces. One is trying to grow a film and
#  the other to prevent one, which is a shared noun rather than a shared
#  problem, and rule 13 does not accept that as an edge.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  THREE, AND THIS IS A DELIBERATELY SHORT TUPLE FOR A RECORD THAT COULD EASILY
#  HAVE CLAIMED MORE.
#
#  Goal 11 is the strongest and it is claimed on the specific target concerning
#  air quality and waste management in cities. Odour abatement is what allows
#  waste and wastewater infrastructure to exist near the people it serves,
#  which is an urban outcome in the plainest sense.
#
#  Goal 3 is claimed narrowly, on the toxicant applications rather than on the
#  odour work: hydrogen sulphide is acutely toxic, and ammonia and solvent
#  vapours have occupational and ambient limits. Odour itself is an amenity
#  matter and is not claimed as health, which `governance.py` sets out.
#
#  Goal 12 is claimed because this record is the emission control step for the
#  waste treatment processes in the two records beside it, and a recovery
#  process that could not control its own emissions would not be permitted to
#  operate.
#
#  GOAL 13 IS DELIBERATELY NOT CLAIMED. A sceptical auditor would ask about the
#  landfill methane biocovers, and the honest answer is that they work at low
#  flux, cannot handle a concentrated stream, and are a partial measure on a
#  large problem. Claiming a climate goal on that would fail rule 12. The
#  energy saving against thermal oxidation is likewise a saving relative to an
#  alternative rather than a climate outcome delivered.
#
#  GOAL 7 IS NOT CLAIMED for the same reason `governance.py` declines the
#  ENERGY domain: consuming less than the alternative is not an energy
#  contribution.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Health, on hydrogen sulphide, ammonia and solvent exposure
    11,  # Cities, on air quality and on siting waste infrastructure
    12,  # Responsible production, as the emission control step for recovery
)


# =============================================================================
#  GLOSSARY
#  Grouped: the configurations, the physics that limits them, the operating
#  variables, and the odour vocabulary.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # -- the configurations ----------------------------------------------------
    "biofilter",
    "biotrickling_filter",
    "bioscrubber",
    "two_phase_partitioning_bioreactor",
    "packing_material",
    "biofilm",
    "landfill_biocover",
    "micro_aeration",
    # -- the physics that decides the scope ------------------------------------
    "henry_law_constant",
    "gas_liquid_partitioning",
    "mass_transfer_coefficient",
    "solubility",
    "empty_bed_residence_time",
    "elimination_capacity",
    "critical_load",
    "channelling",
    "pressure_drop",
    # -- what is being removed -------------------------------------------------
    "hydrogen_sulphide",
    "ammonia",
    "volatile_organic_compound",
    "mercaptan",
    "methanotroph",
    "sulphur_oxidiser",
    "bioaerosol",
    # -- and how anyone judges the result --------------------------------------
    "odour_unit",
    "olfactometry",
    "odour_threshold",
    "hedonic_tone",
    "dispersion_modelling",
    "statutory_nuisance",
)


# =============================================================================
#  REFERENCES
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "biofiltration_waste_gas_review",
    "biotrickling_filter_hydrogen_sulphide",
    "gas_liquid_partitioning_biofiltration_limits",
    "two_phase_partitioning_bioreactor_review",
    "dynamic_olfactometry_standard",
    "landfill_biocover_methane_oxidation",
    "biofilter_bioaerosol_emission",
    "odour_management_waste_facilities",
)


# =============================================================================
#  RELATED
#  Six edges. The two facilities this record keeps open, then the process
#  connections.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # -- the odour source whose planning permission depends on this ------------
    "grey.wastewater_treatment",
    # -- the other one, and the gas engines sulphide removal protects ----------
    "grey.biowaste_treatment",
    # -- soil vapour extraction produces the air stream this treats ------------
    "grey.bioremediation",
    # -- the same gas-liquid transfer problem, approached from the other side --
    "white.bioprocess_engineering",
    # -- the community in the bed is selected rather than supplied, and this
    #    record holds the evidence for why that is the right approach ---------
    "grey.bioaugmentation",
    # -- measuring an emission and proving it fell -----------------------------
    "grey.environmental_biomonitoring",
)
