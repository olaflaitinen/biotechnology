# =============================================================================
#  biotechnology.branches.grey.environmental_biomonitoring.practice
# -----------------------------------------------------------------------------
#  FACET 2 OF 6:  PRACTICE
#
#  Contract and rules: `red/gene_therapy/practice.py`.
#
#  SUBTYPE-SPECIFIC NOTE
#  APPLICATIONS ARE GROUPED BY WHAT QUESTION IS BEING ASKED, WHICH IS THE ONLY
#  GROUPING THAT KEEPS THE METHODS STRAIGHT.
#
#      IS THE ECOSYSTEM HEALTHY        community indices, regulatory assessment
#      WHAT IS ACTUALLY PRESENT        surveys, rare species, invasives
#      IS A SPECIFIC SUBSTANCE THERE   accumulation, biomarkers, biosensors
#      IS A TREATMENT WORKING          the service to the rest of this branch
#      WHAT IS HAPPENING IN A HUMAN
#      POPULATION                      wastewater surveillance
#
#  The last group is placed last because it is the newest and because it raises
#  questions the rest of the record does not: a sewer measures people, not an
#  ecosystem, and `governance.py` treats that separately.
#
#  A DELIBERATE OMISSION. Sentinel animals held in cages at a discharge point
#  are a real and long-standing method, and they are recorded in the
#  accumulation group with their purpose stated rather than in a separate
#  group, because the question they answer is a substance question.
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
#  By the question being asked.
# =============================================================================
APPLICATIONS: Tuple[str, ...] = (
    # ---- IS THE ECOSYSTEM HEALTHY ----------------------------------------------
    "Macroinvertebrate index assessment of rivers, which is the backbone of "
    "regulatory water quality classification and which detects intermittent "
    "discharges that no sampling programme would catch",
    "Diatom and algal index assessment, which responds to nutrient enrichment "
    "faster than invertebrates and is used alongside them for that reason",
    "Fish community assessment, which integrates conditions over larger areas "
    "and longer periods because the animals are mobile and long-lived",
    "Ecological status classification under water framework legislation, which "
    "combines several of the above into the legal judgement of whether a water "
    "body is in good condition",
    "Lichen and moss surveys of air quality, which record cumulative deposition "
    "over years in places where no instrument was installed",
    "Soil invertebrate and microbial community assessment of land condition, "
    "including after remediation",
    # ---- WHAT IS ACTUALLY PRESENT ----------------------------------------------
    "Environmental DNA species surveys from filtered water, which produce a "
    "list of what lives upstream without catching, handling or killing "
    "anything",
    "Early detection of invasive species, which is where environmental DNA has "
    "its clearest practical advantage, since detection while a population is "
    "small is what makes a response possible",
    "Detection of rare, cryptic and declining species that conventional survey "
    "methods miss, including amphibians and species that avoid nets",
    "Metabarcoding of bulk invertebrate samples, which delivers a community "
    "list without a specialist identifying every animal by eye",
    "Sediment DNA and palaeoecological reconstruction, which recovers the "
    "historical baseline the field otherwise lacks",
    # ---- IS A SPECIFIC SUBSTANCE THERE ------------------------------------------
    "Bioaccumulation monitoring in mussels and other filter feeders, which "
    "concentrate persistent contaminants from water at concentrations no "
    "instrument would detect in the water itself",
    "Caged sentinel deployment at discharge points, in which organisms of known "
    "origin are held for a defined period and then analysed, which controls for "
    "the history a wild animal brings with it",
    "Biomarker measurement in fish and invertebrates, including enzyme "
    "induction and reproductive endpoints, which shows exposure and effect "
    "rather than presence",
    "Whole effluent toxicity testing, which asks whether a discharge harms test "
    "organisms rather than whether it exceeds a list of limits, and therefore "
    "captures mixtures",
    "Whole-cell bacterial biosensors reporting the presence of specific "
    "compounds or of general toxicity by producing light or colour",
    # ---- IS A TREATMENT WORKING, WHICH IS THE SERVICE TO THIS BRANCH ------------
    "Functional gene and degrader quantification at remediation sites, which is "
    "what establishes whether the capability `grey.bioremediation` relies on is "
    "present",
    "Compound-specific isotope analysis distinguishing degradation from "
    "dilution, which is what makes monitored natural attenuation defensible "
    "rather than merely plausible",
    "Tracking of introduced populations after augmentation, which is how the "
    "evidence in `grey.bioaugmentation` was actually generated",
    "Receiving water assessment downstream of treatment works and mine "
    "drainage, which is how the discharge consents in the rest of this branch "
    "are enforced",
    # ---- WHAT IS HAPPENING IN A HUMAN POPULATION -------------------------------
    "Wastewater-based epidemiology for infectious disease prevalence, which "
    "measures a whole population including people who were never tested "
    "individually",
    "Wastewater monitoring of antimicrobial resistance genes, which surveys "
    "resistance at community scale rather than in clinical isolates",
    "Wastewater analysis for pharmaceutical and illicit drug consumption, which "
    "is included because it is done and because it is the application that "
    "raises the sharpest questions about consent and about what a sewer may be "
    "used to learn",
)


# =============================================================================
#  TECHNOLOGIES
#  Grouped by where the difficulty is: getting the sample, reading it, and
#  deciding what the reading means.
# =============================================================================
TECHNOLOGIES: Tuple[str, ...] = (
    # ---- getting the sample, which is where most error enters ------------------
    "Water filtration and preservation protocols for environmental DNA, where "
    "filter pore size, volume and preservation determine what is recovered and "
    "are the largest single source of between-study variation",
    "Contamination control from field to laboratory, including field blanks and "
    "dedicated equipment, since a technique sensitive enough to detect a rare "
    "species is sensitive enough to detect the previous sample",
    "Standardised biological sampling methods, including kick sampling and "
    "electrofishing, whose comparability depends entirely on being performed "
    "identically",
    "Passive sampling devices, which accumulate contaminants over weeks and "
    "give a time-integrated chemical measurement that behaves more like a "
    "biological one",
    "Automated and continuous sampling at fixed stations, which is what "
    "converts periodic assessment into a time series",
    # ---- reading the sample ------------------------------------------------------
    "DNA metabarcoding with universal primers, which identifies many taxa from "
    "one sample and whose taxonomic reach is set by the primer choice",
    "Targeted quantitative PCR and digital PCR for a named species or gene, "
    "which is more sensitive and more quantitative than metabarcoding and "
    "answers only the question asked",
    "Portable sequencing for field deployment, which shortens the interval "
    "between sampling and result from weeks to hours",
    "Functional gene arrays and shotgun metagenomics, which describe capability "
    "in a community rather than identity",
    "Compound-specific isotope ratio analysis, which is the technique that "
    "separates destruction from dilution",
    "Whole-cell biosensor construction and deployment, including engineered "
    "reporter strains, which are used in contained assays rather than released",
    # ---- deciding what the reading means -----------------------------------------
    "Reference sequence database curation, which is the invisible dependency of "
    "every molecular method here and which determines what can be identified at "
    "all",
    "Reference condition modelling and multimetric index construction, which is "
    "how a raw community list becomes a classification",
    "Occupancy modelling accounting for imperfect detection, which is what "
    "prevents a non-detection being read as an absence",
    "Bioinformatic pipelines with defined thresholds for sequence clustering "
    "and assignment, whose settings materially change the species list produced "
    "from identical data",
    "Long-term data curation and archiving, which is what gives a monitoring "
    "programme its value and is the first thing lost when one is interrupted",
)


# =============================================================================
#  ORGANISMS
#  Chosen as instruments. Each is listed for what its presence or condition
#  reports.
# =============================================================================
ORGANISMS: Tuple[str, ...] = (
    "ephemeroptera_group",  # mayflies, intolerant of organic pollution
    "plecoptera_group",  # stoneflies, the most oxygen-demanding indicator group
    "chironomus_riparius",  # tolerant midge, its dominance is itself the signal
    "mytilus_edulis",  # mussel, filter feeder used for accumulation monitoring
    "danio_rerio",  # zebrafish, the standard laboratory toxicity test organism
    "aliivibrio_fischeri",  # bioluminescent bacterium, general toxicity assay
)


# =============================================================================
#  TECHNIQUES
# =============================================================================
TECHNIQUES: Tuple[str, ...] = (
    "metabarcoding",
    "qpcr",
    "dna_sequencing",
    "isotope_ratio_analysis",
    "mass_spectrometry",
    "bioassay",
    "microscopy",
    "statistical_experimental_design",
)


# =============================================================================
#  CHALLENGES
#  Interpretation first, because the measurements are more reliable than the
#  conclusions drawn from them.
# =============================================================================
CHALLENGES: Tuple[str, ...] = (
    # -- what the reading does not tell you ------------------------------------
    "Shifting baselines, since reference sites are the least disturbed "
    "available rather than the undisturbed, so each generation calibrates "
    "against the world it inherited and a system can be certified in good "
    "condition while the standard moves",
    "Detection of material rather than of an organism in environmental DNA, "
    "since genetic traces travel downstream and persist after the animal has "
    "gone",
    "Absence of reliable abundance information from sequence read counts, so "
    "the method describes composition rather than population size",
    "Silence on age, condition and breeding status, which are precisely what a "
    "conservation decision needs",
    "Biological indices indicating that something is wrong without indicating "
    "what, which is why they complement chemistry rather than replacing it",
    # -- the dependency nobody sees ---------------------------------------------
    "Reference database incompleteness, which makes any species without a "
    "reference sequence invisible regardless of how much of its DNA is present, "
    "and which biases results toward well-studied regions and taxa",
    "Decline of taxonomic expertise, which is falling faster than molecular "
    "methods are replacing it and which built the reference databases those "
    "methods depend on",
    "Bioinformatic threshold choices that materially change the species list "
    "produced from identical raw data",
    # -- getting a comparable sample ---------------------------------------------
    "Contamination between samples, since a method sensitive enough to detect a "
    "rare species detects the previous sample equally well",
    "Method variation in filtration, preservation and extraction, which is the "
    "largest source of disagreement between studies of the same water",
    "Spatial and temporal variability, so a single sample from a heterogeneous "
    "system supports a much weaker conclusion than its precision suggests",
    "Imperfect detection, where a non-detection is routinely reported as an "
    "absence without the occupancy modelling that would justify it",
    # -- and the programme itself -------------------------------------------------
    "Long-term programme funding, since the entire value of a time series is "
    "its continuity and a gap devalues decades of prior data",
    "Attribution of an observed change to a specific cause, which a community "
    "index cannot supply on its own",
    "Consent and proportionality in wastewater surveillance, where a "
    "population is measured without any individual agreeing to it, and where "
    "the method extends readily from disease to substances a community did not "
    "expect to be monitored for",
)
