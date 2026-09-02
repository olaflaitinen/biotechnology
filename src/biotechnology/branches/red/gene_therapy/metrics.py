# =============================================================================
#  biotechnology.branches.red.gene_therapy.metrics
# -----------------------------------------------------------------------------
#  FACET 3 OF 6:  METRICS -  the numbers, and the formulas that produce them.
# -----------------------------------------------------------------------------
#
#  WHAT A METRIC IS FOR
#  This library is not only a description of biotechnology; it is meant to be
#  usable. A METRIC entry is the bridge between the descriptive half of the
#  package and the computational half. It states:
#
#      name        what practitioners call the quantity
#      symbol      the symbol used in the literature, written in ASCII
#      unit        the unit, written out rather than abbreviated where the
#                  abbreviation would be ambiguous
#      typical     a representative range, as free text, never a single number
#      formula     an optional key into biotechnology.formulas, so that a
#                  reader who wants the number can compute it rather than
#                  look it up
#      evidence    how solid the range is (see core.enums.EvidenceLevel)
#      note        the caveat that stops the number being misused
#
#  WHY `typical` IS A STRING AND NOT A PAIR OF FLOATS
#  Because almost every real range in biology is conditional. "1e11 to 2e14
#  vector genomes per kilogram" is only meaningful once you know the route of
#  administration, and encoding it as (1e11, 2e14) would invite a user to
#  average it, plot it or compare it across routes, all of which are wrong.
#  The string form forces the reader to read the note.
#
#  WHY ASCII SYMBOLS
#  "mu" rather than the Greek letter, "t_half" rather than a subscript. The
#  same string has to render correctly in a terminal, a CSV opened in a
#  spreadsheet with the wrong encoding, a LaTeX document and an HTML page. The
#  pretty form is generated at render time from a lookup table in
#  `biotechnology.core.text`, never stored here.
#
#  THE FORMULAS TUPLE
#  FORMULAS lists every calculation a practitioner in this subtype is likely
#  to need, including ones not tied to a specific metric above. Each key must
#  resolve in `biotechnology.formulas`, and the integrity test enforces it.
#
#  SPDX-License-Identifier: EUPL-1.2
#  Copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
# =============================================================================

from __future__ import annotations

from typing import Tuple

from ....core.enums import EvidenceLevel
from ....core.models import Metric

__all__ = ["METRICS", "FORMULAS"]


# =============================================================================
#  METRICS
# =============================================================================
METRICS: Tuple[Metric, ...] = (
    # -------------------------------------------------------------------------
    #  Dose. The single number that determines both efficacy and toxicity, and
    #  the one where the range spans three orders of magnitude depending on
    #  route. Systemic infusion for a muscle indication sits at the top; a
    #  subretinal injection into an immune-privileged compartment sits at the
    #  bottom and needs far less material.
    # -------------------------------------------------------------------------
    Metric(
        name="Vector genome dose",
        symbol="vg/kg",
        unit="vector genomes per kilogram body weight",
        typical="1e11 - 2e14 vg/kg",
        formula="vector_genome_dose",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Systemic adeno-associated virus doses sit at the top of this "
            "range; subretinal and intrathecal routes are orders of magnitude "
            "lower because the target compartment is small and "
            "immunologically quiet. Doses above roughly 1e14 vg/kg have been "
            "associated with serious hepatotoxicity and complement activation."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Vector copy number. A release specification for ex vivo products, and a
    #  two-sided one: too low and the product is under-dosed, too high and the
    #  insertional mutagenesis risk assessment changes materially.
    # -------------------------------------------------------------------------
    Metric(
        name="Vector copy number per cell",
        symbol="VCN",
        unit="copies per diploid genome",
        typical="0.3 - 4 copies/genome",
        formula="vector_copy_number",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Measured by digital PCR against a single-copy reference gene. "
            "Below about 0.3 the product is usually under-dosed; above "
            "roughly 4 regulators generally require additional justification."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Transduction efficiency. What fraction of the intended cells actually
    #  received the payload. Reported from flow cytometry against a reporter
    #  or a surface marker.
    # -------------------------------------------------------------------------
    Metric(
        name="Transduction efficiency",
        symbol="TE",
        unit="per cent of target cells",
        typical="10 - 90 %",
        formula="transduction_efficiency",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Highly dependent on cell type, vector serotype and multiplicity "
            "of infection. A figure quoted without all three is not "
            "interpretable."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Editing efficiency. Note that the clinically meaningful threshold is a
    #  property of the disease, not of the technology: roughly 20 % edited
    #  haematopoietic stem cells suffices in sickle cell disease because the
    #  corrected cells have a survival advantage.
    # -------------------------------------------------------------------------
    Metric(
        name="Editing efficiency",
        symbol="indel%",
        unit="per cent of alleles carrying the intended edit",
        typical="20 - 90 %",
        formula="editing_efficiency",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Quantified by amplicon sequencing. The clinically meaningful "
            "threshold depends entirely on the disease and on whether edited "
            "cells outcompete unedited ones in vivo."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Full-to-empty capsid ratio. Empty capsids deliver no therapeutic genome
    #  but still present antigen, so they contribute to immune response
    #  without contributing to effect. Regulators cap the empty fraction.
    # -------------------------------------------------------------------------
    Metric(
        name="Full-to-empty capsid ratio",
        symbol="F:E",
        unit="dimensionless",
        typical="> 0.7 full",
        formula="full_empty_ratio",
        evidence=EvidenceLevel.REVIEWED,
        note=(
            "Determined by analytical ultracentrifugation or by comparing "
            "capsid ELISA titre with genome titre by digital PCR."
        ),
    ),
    # -------------------------------------------------------------------------
    #  Multiplicity of infection. The ex vivo process parameter that connects
    #  vector supply to transduction efficiency, and therefore the main lever
    #  on cost of goods in a lentiviral process.
    # -------------------------------------------------------------------------
    Metric(
        name="Multiplicity of infection",
        symbol="MOI",
        unit="transducing units per cell",
        typical="1 - 100 TU/cell",
        formula="multiplicity_of_infection",
        evidence=EvidenceLevel.CONSENSUS,
        note=(
            "Lentiviral vector is frequently the single largest line item in "
            "an ex vivo cost model, so MOI optimisation is an economic "
            "exercise as much as a biological one."
        ),
    ),
)


# =============================================================================
#  FORMULAS
#  Calculations relevant to this subtype, including several not attached to a
#  metric above. `hardy_weinberg` appears because carrier frequency drives the
#  eligible population size for a recessive indication, which is the first
#  number any programme needs.
# =============================================================================
FORMULAS: Tuple[str, ...] = (
    "vector_genome_dose",
    "vector_copy_number",
    "transduction_efficiency",
    "editing_efficiency",
    "multiplicity_of_infection",
    "full_empty_ratio",
    "hardy_weinberg",
    "serial_dilution",
    "off_target_rate",
)
