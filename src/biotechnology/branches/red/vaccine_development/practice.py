# =============================================================================
#  biotechnology.branches.red.vaccine_development.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  The technology list below is grouped by platform rather than by process
#  stage, because in vaccinology the platform choice determines almost
#  everything downstream: the manufacturing plant, the cold chain, the
#  regulatory dossier and the price per dose all follow from it.
#
#  The challenges list is unusually weighted towards the non-technical. That is
#  not padding. For most vaccine-preventable disease the scientific problem was
#  solved decades ago and the remaining deaths are caused by distribution, cost
#  and acceptance.
#
#  SPDX-License-Identifier: EUPL-1.2
# =============================================================================

from __future__ import annotations

from typing import Tuple

__all__ = [
    "APPLICATIONS",
    "TECHNOLOGIES",
    "ORGANISMS",
    "TECHNIQUES",
    "CHALLENGES",
]


# =============================================================================
#  APPLICATIONS
#  Ordered by the platform generation each represents, oldest first, so that a
#  reader can see the field's technical history in the list itself.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # -- classical platforms, still the backbone of routine immunisation ------
    "Live attenuated measles, mumps and rubella vaccination",
    "Inactivated and oral poliovirus vaccination",
    # -- recombinant subunit, from 1986 --------------------------------------
    "Recombinant hepatitis B surface antigen vaccine",
    "Human papillomavirus virus-like particle vaccines",
    # -- conjugates, which made bacterial vaccines work in infants -----------
    "Conjugate vaccines against pneumococcus, meningococcus and Haemophilus",
    # -- annually reformulated ------------------------------------------------
    "Seasonal and pandemic influenza strain updates",
    # -- vectored -------------------------------------------------------------
    "Viral-vector vaccines against Ebola virus disease",
    # -- nucleic acid, from 2020 ----------------------------------------------
    "Messenger RNA vaccines against respiratory viruses",
    # -- newest routine additions ---------------------------------------------
    "Malaria vaccination in children in endemic regions",
    "Respiratory syncytial virus vaccination in older adults",
    # -- therapeutic rather than prophylactic ---------------------------------
    "Therapeutic cancer vaccines and individualised neoantigen platforms",
    # -- protecting one person by vaccinating another --------------------------
    "Maternal immunisation to protect newborns before they can be vaccinated",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by platform, because the platform determines the plant, the cold
#  chain, the dossier and the price.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- nucleic acid --------------------------------------------------------
    "In vitro transcription of messenger RNA with modified nucleosides",
    "Ionisable lipid nanoparticle formulation",
    "Self-amplifying RNA constructs at lower dose",
    # ---- protein and particle ------------------------------------------------
    "Recombinant protein expression in yeast, insect and mammalian cells",
    "Virus-like particle self-assembly",
    "Nanoparticle scaffolds displaying multiple antigen copies",
    # ---- classical -----------------------------------------------------------
    "Egg-based, cell-culture and recombinant influenza production",
    "Attenuation by serial passage or by rational gene deletion",
    "Polysaccharide-protein conjugation chemistry",
    # ---- vectored ------------------------------------------------------------
    "Replication-defective adenoviral and vesicular stomatitis virus vectors",
    # ---- making any of them work ---------------------------------------------
    "Structure-based prefusion antigen stabilisation",
    "Adjuvant systems based on squalene emulsion or TLR agonists",
    "Reverse vaccinology from pathogen genome sequences",
    # ---- getting them to people ----------------------------------------------
    "Lyophilisation and thermostable formulation for warm climates",
    "Microneedle patches and needle-free delivery",
)


# =============================================================================
#  ORGANISMS
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "homo_sapiens",  # the recipient, and the source of convalescent B cells
    "saccharomyces_cerevisiae",  # hepatitis B surface antigen production
    "escherichia_coli",  # carrier proteins and plasmid supply
    "gallus_gallus",  # embryonated eggs, still the influenza workhorse
    "spodoptera_frugiperda",  # insect cell expression of particle antigens
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "cell_culture",
    "fermentation",
    "elisa",
    "pcr",
    "next_generation_sequencing",
    "chromatography",
    "electron_microscopy",
    "cryo_electron_microscopy",
    "flow_cytometry",
)


# =============================================================================
#  CHALLENGES
#  Two technical, then six that are logistical, economic or social. For most
#  vaccine-preventable disease the science was settled decades ago and the
#  remaining deaths are caused by everything below the first two lines.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- biological ------------------------------------------------------------
    "Antigenic drift and shift, which force annual reformulation for influenza "
    "and leave every candidate chasing a moving target",
    "Correlates of protection are unknown for several major pathogens, so a "
    "candidate cannot be evaluated without a full efficacy trial",
    # -- logistical ------------------------------------------------------------
    "Cold chain and last-mile delivery, which fail first in exactly the places "
    "with the highest disease burden",
    "Manufacturing capacity concentrated in a handful of countries, so a surge "
    "in demand is met in order of wealth rather than in order of need",
    # -- economic --------------------------------------------------------------
    "A commercial model that rewards chronic therapy over a product given once "
    "or twice in a lifetime at a few euro per dose",
    # -- social ----------------------------------------------------------------
    "Vaccine hesitancy and coordinated misinformation, which have pushed "
    "measles coverage below the elimination threshold in countries that had "
    "previously eliminated it",
    "Reactogenicity that is medically trivial but reduces uptake of second and "
    "subsequent doses",
    # -- political --------------------------------------------------------------
    "Equitable global allocation during a surge, which no existing mechanism "
    "has yet delivered",
)
