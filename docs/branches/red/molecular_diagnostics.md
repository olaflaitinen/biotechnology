<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/red/molecular_diagnostics/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Molecular Diagnostics**

## Molecular Diagnostics

`red.molecular_diagnostics`

Detecting disease, pathogens and genetic variation by reading nucleic acids and proteins rather than by culture or morphology.

### What it is

Molecular diagnostics identifies a specific nucleic acid or protein sequence in a clinical specimen, rather than inferring it from how an organism grows or how a cell looks. Nucleic-acid amplification, of which the polymerase chain reaction is the archetype, doubles a target region each cycle so that a handful of starting copies becomes a detectable signal within about forty cycles. Quantitative PCR reads fluorescence in real time and reports a quantification cycle that is inversely proportional to the logarithm of the starting copy number. Digital PCR partitions the reaction into thousands of droplets and counts positives against a Poisson model, giving absolute quantification without a standard curve. Isothermal methods such as loop-mediated amplification remove the need for thermal cycling and therefore for laboratory hardware. Sequencing-based diagnostics moves from asking about one target to reading many: targeted panels for oncology, exome and genome sequencing for rare disease, and untargeted metagenomics for infection of unknown cause. CRISPR-based detection couples a programmable nuclease to a reporter and has pushed instrument-free sensitivity into the attomolar range. The binding constraint is interpretation, not detection. Modern assays find things reliably; deciding whether a detected sequence explains a patient's illness, or is colonisation, contamination or an incidental variant of unknown consequence, is where the difficulty now sits.

### In plain language

Every living thing, including every germ, carries its own genetic text. A molecular test looks for one specific sentence from that text in a swab, a drop of blood or a sample of saliva. Because there is usually far too little to see, the machine first makes millions of copies of that sentence if it is present, and then detects the copies. If nothing was there to copy, nothing appears. That copying is what makes these tests so sensitive, and it is also why a laboratory has to be scrupulous: a single stray fragment from a previous sample would be copied just as faithfully.

### An analogy

It is a search-and-photocopy operation. You suspect one particular sentence is hidden somewhere in a library. Rather than reading every book, you use a machine that finds that exact sentence and photocopies it over and over until the stack is tall enough to see from the door. No sentence, no stack. The weakness of the comparison is the useful part: the machine cannot tell a sentence from one that is almost identical, which is why a test designed for one virus can sometimes be fooled by its close relative.

### Why it matters

Culture-based microbiology takes one to five days; a molecular test takes one to four hours. That difference decides whether a patient with sepsis gets the right antibiotic on day zero or on day three. In cancer care the same technology decides which targeted therapy a tumour will respond to, turning a statistical guess into a match. In an outbreak it is the only thing that can say what is spreading while there is still time to act. The cost is a kind of certainty these tests cannot deliver and are routinely assumed to: when a disease is rare, most positive results from even a very accurate test are false, because there are so many more healthy people to be wrong about. Screening a whole population with a good test can therefore cause more anxiety and more unnecessary follow-up than it prevents illness, which is why screening programmes are argued about rather than simply rolled out.

### Applications

- Reverse-transcription PCR detection of respiratory and gastrointestinal viruses
- Rapid detection of antimicrobial resistance genes directly from a sample
- Blood-borne virus screening of donated blood
- Companion diagnostics that select a targeted cancer therapy
- Liquid biopsy for circulating tumour DNA and minimal residual disease
- Cervical screening by human papillomavirus testing rather than cytology
- Non-invasive prenatal testing from cell-free DNA in maternal plasma
- Newborn screening panels for treatable inherited disorders
- Exome and genome sequencing for undiagnosed rare disease
- Metagenomic sequencing for infection of unknown origin
- Point-of-care isothermal testing in clinics without laboratory hardware
- Self-administered tests taken at home
- Wastewater surveillance for community-level pathogen circulation

### Technologies

- Quantitative real-time PCR with hydrolysis probes
- Multiplex panels detecting twenty or more targets in one reaction
- Droplet and chip-based digital PCR, counted against a Poisson model
- Loop-mediated isothermal amplification and recombinase polymerase amplification
- Lateral flow immunoassay strips
- CRISPR-Cas12 and Cas13 collateral-cleavage reporters
- Targeted next-generation sequencing panels with unique molecular identifiers
- Untargeted shotgun metagenomic sequencing
- Nanopore sequencing for long reads at the point of need
- Automated nucleic acid extraction platforms
- Sample-to-answer cartridge systems with no manual pipetting
- Internal amplification controls that detect inhibition
- Bioinformatic variant calling and clinical interpretation pipelines
- Curated variant databases with expert classification panels

### Challenges

- Distinguishing infection from colonisation, since a sensitive test finds organisms that are present but not causing the illness
- Variants of uncertain significance in clinical sequencing, which are found faster than expert panels can classify them
- Detecting fragments of a pathogen for weeks after it has stopped being infectious, which makes a positive result hard to act on
- Contamination and false positives, an inherent risk of any method that amplifies a single molecule into a visible signal
- Inhibitors in clinical material, particularly stool and blood, which can produce a false negative that looks exactly like a true one
- Reference ranges and variant databases skewed towards European ancestry, so a benign variant common in an under-represented population is more likely to be misclassified as pathogenic
- Reimbursement pathways that lag years behind the technology, so a test that works is not a test that is paid for
- The regulatory transition from laboratory-developed tests to certified devices, which improves oversight and simultaneously removes rare-disease assays that no manufacturer will ever certify

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Quantification cycle | `Cq` | amplification cycles | 15 - 40 cycles | CONSENSUS |
| Amplification efficiency | `E` | dimensionless fraction | 0.90 - 1.10, reported as 90 - 110 per cent | CONSENSUS |
| Limit of detection | `LoD` | copies per millilitre of original specimen | 10 - 1000 copies/mL | REVIEWED |
| Diagnostic sensitivity | `Se` | fraction of true cases correctly identified | 0.90 - 0.999 | CONSENSUS |
| Diagnostic specificity | `Sp` | fraction of true non-cases correctly cleared | 0.95 - 0.9999 | CONSENSUS |
| Positive predictive value | `PPV` | probability, dimensionless | prevalence-dependent, from below 0.05 to above 0.99 | CONSENSUS |
| Positive likelihood ratio | `LR+` | dimensionless | > 10 is considered strong evidence | CONSENSUS |
| Turnaround time | `TAT` | hours from sample receipt to reported result | 0.5 h at the point of care to 72 h for a sequencing panel | REVIEWED |

### History

- **1975** - Southern describes transfer and hybridisation for detecting specific DNA sequences
- **1983** - Mullis conceives the polymerase chain reaction
- **1988** - Thermostable Taq polymerase from Thermus aquaticus makes PCR automatable
- **1996** - Real-time quantitative PCR instruments become commercially available
- **2005** - Massively parallel sequencing platforms reach the market
- **2007** - A PCR-defined pertussis outbreak at a United States hospital is later found not to have occurred
- **2011** - Non-invasive prenatal testing enters clinical use
- **2015** - Consensus variant interpretation guidelines published for clinical sequencing
- **2017** - CRISPR-based detection demonstrated at attomolar sensitivity without an instrument
- **2020** - Molecular testing scaled to billions of assays worldwide within a year
- **2022** - Wastewater surveillance adopted as routine public health infrastructure in several countries

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | BENCH |
| Regulatory status | AUTHORISED |
| Domains | HEALTH, INFORMATION |
| SDGs | 3, 9 |

### Regulations

- EU Regulation (EU) 2017/746 on in vitro diagnostic medical devices, which replaced a self-certification regime with risk-classified conformity assessment and brought most laboratory-developed tests into scope
- US FDA 510(k) clearance and De Novo classification pathways
- US FDA Emergency Use Authorization, the mechanism by which outbreak assays reach clinics before full clearance
- US Clinical Laboratory Improvement Amendments certification
- National medical laboratory licensing regimes, which vary widely
- GDPR Article 9, which treats health and genetic data as a special category requiring an explicit legal basis
- GDPR Article 22 on decisions based solely on automated processing, which reaches algorithmic interpretation of a sequencing result
- EU Regulation (EU) 2024/1689 on artificial intelligence, where a diagnostic interpretation model is a high-risk system
- Council of Europe Convention on Human Rights and Biomedicine, Article 12, restricting predictive genetic testing to health purposes

### Standards

- ISO 15189 medical laboratories, requirements for quality and competence
- ISO 15190 medical laboratories, requirements for safety
- External quality assessment and proficiency testing schemes, which are the only routine check that a laboratory's answers are actually right
- ISO 13485 medical devices, quality management systems
- ISO 14971 application of risk management to medical devices
- MIQE guidelines, minimum information for publication of quantitative real-time PCR experiments
- dMIQE guidelines for digital PCR
- CLSI EP17 evaluation of detection capability
- CLSI EP12 user protocol for evaluation of qualitative test performance
- ACMG and AMP standards for the interpretation of sequence variants
- Human Genome Variation Society sequence variant nomenclature
- ISO 20387 biobanking, for the reference materials everything is calibrated against

### Related records

- `red.pharmacogenomics`
- `gold.genomics_data_analysis`
- `gold.multi_omics_integration`
- `yellow.food_safety_biotechnology`
- `grey.environmental_biomonitoring`
- `blue.marine_genomics`
- `dark.biosurveillance`
- `purple.genetic_data_privacy`

### Cross-references

- [red.pharmacogenomics](pharmacogenomics.md)
- `gold.genomics_data_analysis` (branch not written yet)
- `gold.multi_omics_integration` (branch not written yet)
- [yellow.food_safety_biotechnology](../yellow/food_safety_biotechnology.md)
- [grey.environmental_biomonitoring](../grey/environmental_biomonitoring.md)
- [blue.marine_genomics](../blue/marine_genomics.md)
- `dark.biosurveillance` (branch not written yet)
- `purple.genetic_data_privacy` (branch not written yet)
