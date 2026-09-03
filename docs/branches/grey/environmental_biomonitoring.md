<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/grey/environmental_biomonitoring/.
  Edit the source and run `make docs`.
-->

[Grey Biotechnology](index.md) / **Environmental Biomonitoring**

## Environmental Biomonitoring

`grey.environmental_biomonitoring`

Using organisms and their traces to measure environmental condition, which records exposure over time where a chemical sample records a concentration at an instant.

### What it is

Environmental biomonitoring uses living organisms, and increasingly their genetic traces, to assess the condition of water, soil, sediment and air. Its justification is that it answers a question chemistry cannot. A water sample records what was present at one point at one moment; the community living in that water records what it has been exposed to continuously since whatever last disturbed it. An intermittent discharge, a pesticide pulse after rain, or a mixture whose components are individually below their limits will be invisible to a sampling programme and visible in the invertebrates. Biology also integrates interactions that no list of concentrations captures, and it measures the thing that is actually valued, which is whether the ecosystem is functioning rather than whether a number was exceeded. Four approaches are used and they answer different questions. Indicator and index methods score the community present against what would be expected, using groups whose tolerances are well characterised, and this is what most regulatory assessment of rivers consists of. Bioaccumulation monitoring measures contaminant concentrations in the tissue of organisms that concentrate them from the surrounding medium, which is how persistent substances at undetectable ambient concentrations are found. Biomarker and biosensor methods measure a physiological or molecular response, from enzyme induction in a fish to an engineered bacterium that produces a signal in the presence of a specific compound. And molecular survey methods identify what is present from genetic material, either from the organisms themselves or from the traces they shed. Environmental DNA is the development that changed the field's economics. Every organism sheds cells, mucus and waste, so a filtered water sample contains genetic material from much of what lives upstream, and sequencing it produces a species list without catching, handling or killing anything. It detects rare and cryptic species that netting misses and it detects invasive species early, which is where its practical value is greatest. Its limits are structural rather than technical. It reports that material was present, which is not the same as an organism being there now, since DNA travels downstream and persists for a period after the organism has gone. Read counts do not translate reliably into abundance, so it does not replace a census. It says nothing about age, condition or whether a population is breeding. And it is entirely dependent on reference sequence databases, so a species with no reference entry is invisible no matter how much of its DNA is in the sample. That last point generalises into the field's deepest difficulty and it applies to the traditional methods as well. Every assessment is a comparison against an expectation, and the expectation has to come from somewhere. Reference sites are chosen as the least disturbed available rather than the undisturbed, because in most regions undisturbed sites do not exist. Historical baselines are patchy and were collected for other purposes. So a system judged in good condition is being compared against a standard set after most of the change had already occurred, and each generation of assessors calibrates against the world it inherited.

### In plain language

Instead of testing water for chemicals, you can look at what is living in it. This works because a bottle of water only tells you about the moment it was filled, while the creatures in a river have been sitting in it the whole time. If somebody dumped something at three in the morning, the water sample at noon shows nothing and the missing insects show it for months. Some species can only survive in clean water, so counting which ones are present grades the river. A newer method is remarkable: every animal sheds skin cells and waste, so you can filter a bucket of river water, read the DNA in it, and get a list of what lives upstream without catching anything at all. It finds rare and hidden species and spots invaders early. It cannot tell you how many there are, whether they are breeding, or whether they are still there rather than having passed through last week.

### An analogy

A chemical sample is a photograph and a biological survey is a diary. The photograph is exact about one instant and silent about the night before; the diary is vaguer about any particular hour and tells you how the month went. Environmental DNA is a third thing again: footprints rather than a sighting. They prove something passed, they do not prove it is still there, and they will not tell you how many walked or whether any of them stayed.

### Why it matters

This is the record that makes the rest of the branch accountable. Monitored natural attenuation is only defensible because degradation can be demonstrated rather than asserted. Discharge consents are enforceable because the receiving water is assessed. A remediation is signed off against measurements. Remove this record and grey biotechnology becomes a set of claims about invisible processes. The practical gains are real. Biological indices detect intermittent and mixture effects that no realistic sampling programme catches. Bioaccumulation monitoring finds persistent substances at ambient concentrations below detection. Environmental DNA has reduced the cost and the harm of surveying: a filtered water sample replaces netting, trapping and electrofishing, which means more sites can be covered, more often, without killing the animals being counted, and it detects invasive species early enough for a response to be possible. The limits deserve equal prominence. A biological index tells you something is wrong and rarely what, so it complements chemistry rather than replacing it. Environmental DNA reports presence of material rather than presence of an organism, gives no reliable abundance, and is blind to any species absent from a reference database, which biases results toward well-studied regions and well-studied taxa. Taxonomic expertise for traditional identification is declining faster than molecular methods are replacing it, and the reference databases those methods depend on were built by the same expertise. Long-term monitoring programmes are cut first in a budget round and their value is entirely in their continuity, so a five-year gap devalues thirty years of prior data. And shifting baselines are the quiet structural problem: each assessment generation calibrates against the least disturbed sites available to it, so systems can be certified as in good condition while the standard itself moves.

### Applications

- Macroinvertebrate index assessment of rivers, which is the backbone of regulatory water quality classification and which detects intermittent discharges that no sampling programme would catch
- Diatom and algal index assessment, which responds to nutrient enrichment faster than invertebrates and is used alongside them for that reason
- Fish community assessment, which integrates conditions over larger areas and longer periods because the animals are mobile and long-lived
- Ecological status classification under water framework legislation, which combines several of the above into the legal judgement of whether a water body is in good condition
- Lichen and moss surveys of air quality, which record cumulative deposition over years in places where no instrument was installed
- Soil invertebrate and microbial community assessment of land condition, including after remediation
- Environmental DNA species surveys from filtered water, which produce a list of what lives upstream without catching, handling or killing anything
- Early detection of invasive species, which is where environmental DNA has its clearest practical advantage, since detection while a population is small is what makes a response possible
- Detection of rare, cryptic and declining species that conventional survey methods miss, including amphibians and species that avoid nets
- Metabarcoding of bulk invertebrate samples, which delivers a community list without a specialist identifying every animal by eye
- Sediment DNA and palaeoecological reconstruction, which recovers the historical baseline the field otherwise lacks
- Bioaccumulation monitoring in mussels and other filter feeders, which concentrate persistent contaminants from water at concentrations no instrument would detect in the water itself
- Caged sentinel deployment at discharge points, in which organisms of known origin are held for a defined period and then analysed, which controls for the history a wild animal brings with it
- Biomarker measurement in fish and invertebrates, including enzyme induction and reproductive endpoints, which shows exposure and effect rather than presence
- Whole effluent toxicity testing, which asks whether a discharge harms test organisms rather than whether it exceeds a list of limits, and therefore captures mixtures
- Whole-cell bacterial biosensors reporting the presence of specific compounds or of general toxicity by producing light or colour
- Functional gene and degrader quantification at remediation sites, which is what establishes whether the capability `grey.bioremediation` relies on is present
- Compound-specific isotope analysis distinguishing degradation from dilution, which is what makes monitored natural attenuation defensible rather than merely plausible
- Tracking of introduced populations after augmentation, which is how the evidence in `grey.bioaugmentation` was actually generated
- Receiving water assessment downstream of treatment works and mine drainage, which is how the discharge consents in the rest of this branch are enforced
- Wastewater-based epidemiology for infectious disease prevalence, which measures a whole population including people who were never tested individually
- Wastewater monitoring of antimicrobial resistance genes, which surveys resistance at community scale rather than in clinical isolates
- Wastewater analysis for pharmaceutical and illicit drug consumption, which is included because it is done and because it is the application that raises the sharpest questions about consent and about what a sewer may be used to learn

### Technologies

- Water filtration and preservation protocols for environmental DNA, where filter pore size, volume and preservation determine what is recovered and are the largest single source of between-study variation
- Contamination control from field to laboratory, including field blanks and dedicated equipment, since a technique sensitive enough to detect a rare species is sensitive enough to detect the previous sample
- Standardised biological sampling methods, including kick sampling and electrofishing, whose comparability depends entirely on being performed identically
- Passive sampling devices, which accumulate contaminants over weeks and give a time-integrated chemical measurement that behaves more like a biological one
- Automated and continuous sampling at fixed stations, which is what converts periodic assessment into a time series
- DNA metabarcoding with universal primers, which identifies many taxa from one sample and whose taxonomic reach is set by the primer choice
- Targeted quantitative PCR and digital PCR for a named species or gene, which is more sensitive and more quantitative than metabarcoding and answers only the question asked
- Portable sequencing for field deployment, which shortens the interval between sampling and result from weeks to hours
- Functional gene arrays and shotgun metagenomics, which describe capability in a community rather than identity
- Compound-specific isotope ratio analysis, which is the technique that separates destruction from dilution
- Whole-cell biosensor construction and deployment, including engineered reporter strains, which are used in contained assays rather than released
- Reference sequence database curation, which is the invisible dependency of every molecular method here and which determines what can be identified at all
- Reference condition modelling and multimetric index construction, which is how a raw community list becomes a classification
- Occupancy modelling accounting for imperfect detection, which is what prevents a non-detection being read as an absence
- Bioinformatic pipelines with defined thresholds for sequence clustering and assignment, whose settings materially change the species list produced from identical data
- Long-term data curation and archiving, which is what gives a monitoring programme its value and is the first thing lost when one is interrupted

### Challenges

- Shifting baselines, since reference sites are the least disturbed available rather than the undisturbed, so each generation calibrates against the world it inherited and a system can be certified in good condition while the standard moves
- Detection of material rather than of an organism in environmental DNA, since genetic traces travel downstream and persist after the animal has gone
- Absence of reliable abundance information from sequence read counts, so the method describes composition rather than population size
- Silence on age, condition and breeding status, which are precisely what a conservation decision needs
- Biological indices indicating that something is wrong without indicating what, which is why they complement chemistry rather than replacing it
- Reference database incompleteness, which makes any species without a reference sequence invisible regardless of how much of its DNA is present, and which biases results toward well-studied regions and taxa
- Decline of taxonomic expertise, which is falling faster than molecular methods are replacing it and which built the reference databases those methods depend on
- Bioinformatic threshold choices that materially change the species list produced from identical raw data
- Contamination between samples, since a method sensitive enough to detect a rare species detects the previous sample equally well
- Method variation in filtration, preservation and extraction, which is the largest source of disagreement between studies of the same water
- Spatial and temporal variability, so a single sample from a heterogeneous system supports a much weaker conclusion than its precision suggests
- Imperfect detection, where a non-detection is routinely reported as an absence without the occupancy modelling that would justify it
- Long-term programme funding, since the entire value of a time series is its continuity and a gap devalues decades of prior data
- Attribution of an observed change to a specific cause, which a community index cannot supply on its own
- Consent and proportionality in wastewater surveillance, where a population is measured without any individual agreeing to it, and where the method extends readily from disease to substances a community did not expect to be monitored for

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Reference condition | `E_ref` | expected community composition for the water body type | derived from the least disturbed available sites, from historical records, or from a model | REVIEWED |
| Ecological quality ratio | `EQR` | observed value divided by the reference value, scaled from zero to one | banded into classes, with a threshold defining good status | CONSENSUS |
| Detection probability | `p_det` | probability of detecting a species given that it is present | well below one for rare, cryptic and seasonally active species | CONSENSUS |
| Sampling effort required for confident absence | `n_eff` | number of samples or replicates | rises steeply as detection probability falls | CONSENSUS |
| Biotic index score | `BI` | weighted score derived from the pollution tolerance of taxa present | high where sensitive groups persist, low where only tolerant groups remain | CONSENSUS |
| Taxonomic richness and diversity | `H` | number of taxa, or a diversity index value | falls under most forms of disturbance, and not always | CONSENSUS |
| Community composition dissimilarity | `d_beta` | dissimilarity between observed and reference community composition | the basis of molecular assessment, where taxonomy may be incomplete | REVIEWED |
| Bioconcentration factor | `BCF` | ratio of tissue concentration to ambient concentration | high for persistent lipophilic compounds in filter feeders | CONSENSUS |
| Biomarker response | `R_bio` | fold induction of an enzyme or other physiological endpoint | responds within days of exposure and before any community change is visible | REVIEWED |
| Whole effluent toxicity | `EC50` | dilution at which half of the test organisms show the measured effect | reported for a defined species and exposure duration | CONSENSUS |
| Environmental DNA concentration | `c_eDNA` | target copies per litre of filtered water | varies with shedding rate, flow, temperature and degradation | REVIEWED |
| Environmental DNA persistence and transport distance | `L_eDNA` | hours of persistence, and metres to kilometres of downstream transport | hours to days, over distances that are substantial in flowing water | REVIEWED |
| Reference database coverage | `f_ref` | per cent of expected regional taxa with a reference sequence | high for well-studied groups in well-studied regions, and poor otherwise | REPORTED |
| Functional gene abundance | `N_gene` | gene copies per gram or per litre | the standard evidence for degradation capability at a remediation site | CONSENSUS |

### History

- **1908** - The saprobic system classifies river condition by the organisms present
- **1955** - Lichen surveys are used to map air quality across industrial regions
- **1964** - Standardised biotic indices for river invertebrates are adopted for regulatory assessment
- **1976** - Mussel watch programmes establish bioaccumulation monitoring of coastal contaminants
- **1985** - Biomarker methods enter environmental assessment
- **1990** - Whole effluent toxicity testing is incorporated into discharge permitting
- **1995** - The shifting baseline syndrome is described in fisheries science
- **2000** - Water framework legislation makes ecological status a legal classification
- **2008** - Environmental DNA is demonstrated for detecting aquatic species from water samples
- **2012** - Metabarcoding extends environmental DNA from single species to whole communities
- **2016** - Environmental DNA is accepted in regulatory survey and invasive species programmes
- **2020** - Wastewater surveillance is deployed at population scale for infectious disease
- **2022** - Taxonomic expertise decline is identified as a constraint on molecular monitoring

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | CONTROLLED |
| Scale | POPULATION |
| Regulatory status | NOTIFIED |
| Domains | ENVIRONMENT, HEALTH, INFORMATION |
| SDGs | 3, 6, 14, 15 |

### Regulations

- The Water Framework Directive 2000/60/EC and national equivalents, which define ecological status as a legal classification in biological terms and require member states to achieve good status
- Marine Strategy Framework Directive 2008/56/EC descriptor monitoring, which extends the same logic to marine waters
- Habitats Directive 92/43/EEC and Birds Directive 2009/147/EC surveillance obligations, which require the condition of designated species and habitats to be reported periodically
- Discharge consent monitoring and reporting conditions, which is how the measurements in this record become enforcement evidence against the installations in the rest of this branch
- Remediation verification and completion certification requirements, which specify what evidence will be accepted before a site is signed off
- Sampling licences and permits to take, disturb or handle protected species, which apply to exactly the rare species a survey is designed to find
- Animal welfare legislation governing procedures on protected animals, including Directive 2010/63/EU, which applies to electrofishing, netting and caged sentinel deployment and makes the organisms subjects rather than instruments
- Access and benefit sharing obligations under the Nagoya Protocol, which apply to genetic material collected in another jurisdiction and therefore to environmental DNA sampling across borders
- Biosecurity and equipment disinfection requirements between sites, since a survey team moving between catchments is itself a vector
- Data protection law applied to wastewater surveillance, including the General Data Protection Regulation, where a catchment small enough to identify a building or an institution makes an aggregate measurement personal in effect
- Research ethics and institutional review requirements for population-level wastewater studies, which are the only place consent is considered at all since no individual in a sewershed agreed to be measured
- Public health surveillance mandates and reporting obligations, which authorise disease monitoring and do not by themselves authorise the measurement of anything else a population excretes
- Restrictions on the secondary use of wastewater data, which is the unresolved question, since nothing technical prevents extending the method from pathogens to drug use to any other marker
- Environmental information access legislation, including the Aarhus Convention, which gives the public a right to the monitoring data that regulators hold
- Sequence data deposit requirements and database access conditions, which govern the reference resources every molecular method here depends on

### Standards

- Intercalibration exercises establishing that class boundaries mean the same thing between countries and laboratories, which is what allows a classification to be compared across a shared river basin
- ISO 17025 laboratory accreditation for analysis intended for enforcement use
- Ring test and proficiency scheme participation for taxonomic and molecular identification
- Reference condition derivation guidance, which is the documented basis for a judgement that `metrics.py` places first and identifies as a judgement
- Standardised field sampling protocols including kick sampling, electrofishing and net specification, whose comparability depends entirely on identical execution
- Environmental DNA sampling and filtration protocols specifying volume, pore size, preservation and field blanks, which are the largest source of between-study variation when unspecified
- Contamination control practice from field through laboratory, since a method sensitive enough to detect a rare species detects the previous sample as readily
- Survey design and statistical power conventions, including the replication needed before an absence may be reported as an absence
- Bioinformatic pipeline specification including clustering and assignment thresholds, which materially change the species list produced from identical raw data and must therefore be reported
- Occupancy modelling conventions accounting for imperfect detection
- Multimetric index construction and validation guidance
- Reference sequence database curation standards, which are the invisible dependency of every molecular result and which rest on taxonomic work the field is losing
- Long-term data archiving, versioning and custody arrangements, which are what make a time series valuable and what a funding interruption destroys retrospectively
- Open data and FAIR data practice for environmental sequence and monitoring records
- Metadata standards for sample provenance, which determine whether a result can be reinterpreted years later against a better database
- Ethical review practice for wastewater surveillance study design, including catchment size thresholds below which a result should not be reported

### Related records

- `grey.biodiversity_conservation`
- `red.molecular_diagnostics`
- `grey.bioremediation`
- `grey.bioaugmentation`
- `grey.wastewater_treatment`
- `grey.biomining`

### Cross-references

- [grey.biodiversity_conservation](biodiversity_conservation.md)
- [red.molecular_diagnostics](../red/molecular_diagnostics.md)
- [grey.bioremediation](bioremediation.md)
- [grey.bioaugmentation](bioaugmentation.md)
- [grey.wastewater_treatment](wastewater_treatment.md)
- [grey.biomining](biomining.md)
