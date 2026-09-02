# =============================================================================
#  biotechnology.branches.red.vaccine_development.linkage
# -----------------------------------------------------------------------------
#  FACET 6 OF 6:  LINKAGE
#
#  Contract and rules for RELATED: `red/gene_therapy/linkage.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  This record has the widest cross-branch reach in the red branch, and the
#  edges are the point rather than decoration.
#
#  The edge to `green.veterinary_vaccines` is the One Health edge: roughly
#  three-quarters of emerging human infectious diseases originate in animals,
#  so an outbreak stopped in a poultry shed is an outbreak that never reaches a
#  hospital. A reader who understands human vaccinology and not veterinary
#  vaccinology understands half of the subject.
#
#  The edge to `dark.biodefence_countermeasures` is the reason this record
#  carries the SECURITY domain: the same platforms, the same plants and often
#  the same people produce routine immunisation and national medical
#  countermeasure stockpiles.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = ["SDGS", "GLOSSARY", "REFERENCES", "RELATED"]


# =============================================================================
#  SDGS
#  Three, and each survives the sceptical-auditor test on its own terms.
# =============================================================================
SDGS: Tuple[int, ...] = (
    3,  # Good health and well-being. The clearest claim in the whole taxonomy.
    10,  # Reduced inequalities. Engaged, and currently on the wrong side of it:
    #     doses reached high-income countries roughly a year before low-income
    #     ones during the last pandemic. narrative.WHY_IT_MATTERS says so.
    17,  # Partnerships for the goals. Not padding: Gavi, COVAX and WHO
    #     prequalification are the mechanisms through which vaccines actually
    #     reach most of the world, and they are partnership instruments.
)


# =============================================================================
#  GLOSSARY
#  Grouped so that a reader meets the vocabulary in the order the DESCRIPTION
#  uses it: what is presented, how it is made stronger, what happens in the
#  body, and how it is measured and delivered.
# =============================================================================
GLOSSARY: Tuple[str, ...] = (
    # ---- what is presented to the immune system -------------------------------
    "antigen",
    "epitope",
    "attenuation",
    "virus_like_particle",
    "conjugate_vaccine",
    # ---- what makes the response stronger --------------------------------------
    "adjuvant",
    "prefusion_conformation",
    # ---- what happens in the recipient ------------------------------------------
    "neutralising_antibody",
    "seroconversion",
    "correlate_of_protection",
    "reactogenicity",
    # ---- what happens in the population -----------------------------------------
    "herd_immunity",
    "antigenic_drift",
    "ring_vaccination",
    # ---- how it reaches people ----------------------------------------------------
    "cold_chain",
    "prequalification",
)


# =============================================================================
#  REFERENCES
#  The founding demonstration, the founding attenuation, the standard modern
#  review, the trial that defined the messenger RNA era, and the governing
#  technical guidance.
# =============================================================================
REFERENCES: Tuple[str, ...] = (
    "jenner1798",  # the founding demonstration
    "pasteur1881",  # attenuation as a deliberate technique
    "plotkin2020",  # the standard modern review of correlates of protection
    "polack2020",  # the trial that opened the nucleic-acid era
    "who_trs_vaccines",  # the governing technical guidance
)


# =============================================================================
#  RELATED
#  Ordered from nearest to furthest. Five of the seven cross a branch boundary,
#  which is what rule 13 asks for.
# =============================================================================
RELATED: Tuple[str, ...] = (
    # ---- how a candidate is evaluated and how an outbreak is detected ---------
    "red.molecular_diagnostics",
    # ---- the other way to supply protection: give the antibody directly ------
    "red.antibody_engineering",
    # ---- where the doses are actually made -------------------------------------
    "red.pharmaceutical_biotechnology",
    # ---- the One Health edge; see the header note -------------------------------
    "green.veterinary_vaccines",
    # ---- the defensive application of the same platforms ------------------------
    "dark.biodefence_countermeasures",
    "dark.biosurveillance",
    # ---- the ethics of trialling and allocating a population-scale product ------
    "purple.clinical_trial_ethics",
)
