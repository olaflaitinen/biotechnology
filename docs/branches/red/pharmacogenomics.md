<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/pharmacogenomics/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Pharmacogenomics**

## Pharmacogenomics

`red.pharmacogenomics`

Using inherited genetic variation to predict drug response, dose requirement and adverse-reaction risk.

### What it is

Pharmacogenomics studies how inherited variation changes what a drug does to a patient and what the patient does to the drug. The boundary that matters is germline against somatic: variation inherited from a parent belongs here, while variation acquired by a tumour and used to select a targeted therapy belongs to `red.molecular_diagnostics`. Most actionable variation sits in three places: genes encoding drug-metabolising enzymes, chiefly the cytochrome P450 family and a small number of transferases; genes encoding transporters such as SLCO1B1 that govern how much drug reaches a tissue; and immune loci such as HLA, where a single allele can turn an ordinary medicine into a life-threatening hypersensitivity reaction. Variation is described using star allele nomenclature, where a haplotype such as CYP2C19*2 denotes a defined set of variants with a known functional consequence. The two inherited alleles form a diplotype, which is translated into an activity score and then into a phenotype: poor, intermediate, normal, rapid or ultrarapid metaboliser. Guidelines from the Clinical Pharmacogenetics Implementation Consortium and the Dutch Pharmacogenetics Working Group map that phenotype to a prescribing action, and regulators increasingly place the mapping in the product label. The binding constraint is implementation, not discovery. A result that does not reach the prescriber inside the electronic health record, at the moment of prescribing, in a form that requires no interpretation, changes nothing at all.

### In plain language

Your liver breaks medicines down using a set of tiny chemical tools, and the instructions for building those tools are written in your genes. Some people inherit a fast version of a tool, some a slow one, and some none at all. A fast processor may clear a drug before it has time to work. A slow processor may build up a dangerous amount from an ordinary dose. A few people carry a version that makes their immune system attack a particular medicine outright. A single cheek swab or blood test can show which versions you carry, and the result does not change during your life, so it only needs to be done once.

### An analogy

Two people drink the same two glasses of wine. One is fine, the other is unwell for the evening. Nobody finds this surprising, because we all accept that bodies process alcohol at different speeds. Medicines are no different; pharmacogenomics simply measures the speed in advance instead of discovering it by accident. The comparison has a useful limit: how you handle wine also depends on your weight, what you ate and what else you have taken, and the same is true of medicines. A genetic result narrows the right dose. It does not by itself determine it.

### Why it matters

Adverse drug reactions are among the leading causes of hospital admission in high-income countries, and a substantial fraction are predictable from a handful of well-characterised genes. Screening for HLA-B*57:01 before abacavir has essentially eliminated a life-threatening hypersensitivity reaction. Screening for DPYD before fluoropyrimidine chemotherapy prevents deaths from a drug that is otherwise routine. These are not futuristic claims; they are standard of care in several European health systems today. The uncomfortable part is that the science has been settled far longer than the practice has existed. The variants were characterised in the 1980s and 1990s, the guidelines are free to read, and the test costs less than one day in a hospital bed, yet most patients in most countries are still prescribed as though everyone metabolised identically. The obstacles are electronic health records, reimbursement rules and clinical workflow, none of which is a scientific problem. There is a second problem: the reference data are drawn overwhelmingly from people of European ancestry, so the populations with the least evidence behind their results are the ones already least well served.

### Applications

- HLA-B*57:01 screening before abacavir, which has essentially eliminated a life-threatening hypersensitivity syndrome
- HLA-B*15:02 screening before carbamazepine in populations where the allele is common
- HLA-B*58:01 screening before allopurinol
- DPYD screening before fluorouracil and capecitabine chemotherapy
- TPMT and NUDT15 screening before thiopurine therapy
- UGT1A1 genotyping before irinotecan
- CYP2C19-guided antiplatelet therapy in acute coronary syndrome, where a poor metaboliser does not activate clopidogrel
- CYP2D6-guided use of codeine and tramadol, which are prodrugs and are therefore ineffective in poor metabolisers and dangerous in ultrarapid ones
- CYP2D6 and CYP2C19-guided dosing of antidepressants
- CYP2D6-guided use of tamoxifen
- SLCO1B1 genotyping and statin-associated muscle symptom risk
- VKORC1 and CYP2C9 informed warfarin dosing algorithms
- Pre-emptive panel testing at first contact with a health system, so that the result is already present when any future prescription is written

### Technologies

- Targeted genotyping arrays covering pharmacogene star alleles
- Long-read sequencing to resolve CYP2D6 copy number, hybrid genes and structural rearrangements that short reads cannot phase
- Extraction from saliva or buccal swab, avoiding a blood draw
- Star-allele calling software with curated allele definition tables
- Diplotype-to-activity-score translation, then activity score to phenotype
- Population allele frequency reference databases
- Clinical decision support fired at the moment of prescribing rather than reported to a file
- Structured storage of the result so that it survives a change of care provider or of records system
- Therapeutic drug monitoring as an orthogonal check where the stakes are high

### Challenges

- Structural variation in CYP2D6, including gene deletions, duplications and hybrid genes, which short-read sequencing cannot resolve and which affects one of the most clinically important genes in the panel
- Allele frequencies and clinical evidence drawn overwhelmingly from people of European ancestry, so the populations least well served by existing medicine are also those with the weakest evidence behind their results
- Getting the result in front of the prescriber at the moment of decision, which is an electronic health record problem rather than a genetic one
- Alert fatigue, where a decision support system that fires too often is switched off entirely and takes the useful alerts with it
- Reimbursement designed for reactive testing of one gene against one drug, rather than for pre-emptive panel testing whose benefit accrues over decades and to a different budget
- Result portability over a lifetime, across providers, systems and countries, for data that never changes and should therefore never need regenerating
- Direct-to-consumer reports that outrun the underlying evidence, offering actionable-sounding conclusions from variants with no established clinical consequence

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Activity score | `AS` | dimensionless, summed across two alleles | 0 to 3, occasionally higher with gene duplication | CONSENSUS |
| Metaboliser phenotype | `PM/IM/NM/RM/UM` | ordered category | poor, intermediate, normal, rapid, ultrarapid | CONSENSUS |
| Apparent oral clearance | `CL/F` | litres per hour | drug- and genotype-specific | CONSENSUS |
| Area under the concentration-time curve | `AUC` | milligram hours per litre | drug-specific | CONSENSUS |
| Elimination half-life | `t_half` | hours | 1 - 100 h | CONSENSUS |
| Allele frequency | `f` | fraction of chromosomes in a population | 0.001 - 0.40, varying sharply between ancestries | REVIEWED |
| Number needed to genotype | `NNG` | patients tested per adverse event prevented | 15 to several hundred | REVIEWED |
| Therapeutic index | `TI` | ratio of toxic to effective dose | < 3 for the drugs where genotyping matters most | CONSENSUS |

### History

- **1957** - Motulsky links inherited enzyme variation to adverse drug reactions
- **1959** - Vogel coins the term pharmacogenetics
- **1977** - Debrisoquine hydroxylation polymorphism described in a volunteer study
- **1988** - CYP2D6 characterised molecularly, explaining the debrisoquine phenotype
- **1998** - TPMT genotyping introduced before thiopurine therapy
- **2003** - The Human Genome Project is completed, accelerating candidate discovery
- **2007** - A warfarin dosing label change is issued, and changes very little
- **2008** - HLA-B*57:01 screening before abacavir becomes standard of care
- **2011** - The Clinical Pharmacogenetics Implementation Consortium publishes its first prescribing guidelines
- **2013** - Two large warfarin trials report conflicting results
- **2020** - Pre-emptive panel testing enters routine use in several European health systems
- **2023** - A multicentre trial reports a reduction in clinically relevant adverse drug reactions from a twelve-gene pre-emptive panel

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | POPULATION |
| Regulatory status | AUTHORISED |
| Domains | HEALTH, INFORMATION |
| SDGs | 3, 10 |

### Regulations

- EU Regulation (EU) 2017/746 on in vitro diagnostic medical devices, under which a companion diagnostic is class C
- US FDA premarket review of companion diagnostics, and enforcement discretion over direct-to-consumer pharmacogenomic reports
- US Clinical Laboratory Improvement Amendments certification of the performing laboratory
- EU Directive 2001/83/EC, under which pharmacogenomic information is placed in the summary of product characteristics
- EMA Guideline on the use of pharmacogenetic methodologies in the pharmacokinetic evaluation of medicinal products
- US FDA Table of Pharmacogenetic Associations and pharmacogenomic biomarker labelling
- ICH E15 definitions for genomic biomarkers and sample coding categories
- GDPR Article 9, which classes genetic data as a special category requiring an explicit legal basis
- GDPR Article 22 on decisions based solely on automated processing, which reaches an automated dose recommendation
- Council of Europe Convention on Human Rights and Biomedicine, Article 12, restricting predictive genetic testing to health purposes
- National genetic non-discrimination provisions governing insurance and employment, which vary sharply between countries

### Standards

- CPIC clinical practice guidelines, freely published, regularly updated, and the de facto genotype-to-action mapping used worldwide
- Dutch Pharmacogenetics Working Group recommendations, the other major guideline set, which occasionally differs from CPIC and says so
- PharmVar star allele nomenclature, the reference definition of what each allele designation means
- Human Genome Variation Society sequence variant nomenclature
- HL7 FHIR Genomics implementation guide, which is how a result survives a change of records system
- ISO 20428 health informatics, structure of genomic sequencing report data
- ISO 15189 medical laboratories, requirements for quality and competence
- Pharmacogenetics external quality assessment schemes
- ACMG technical standards for pharmacogenomic testing

### Related records

- `red.molecular_diagnostics`
- `red.pharmaceutical_biotechnology`
- `gold.genomics_data_analysis`
- `gold.multi_omics_integration`
- `gold.machine_learning_in_biology`
- `purple.genetic_data_privacy`
- `yellow.nutrigenomics`

### Cross-references

- [red.molecular_diagnostics](molecular_diagnostics.md)
- [red.pharmaceutical_biotechnology](pharmaceutical_biotechnology.md)
- `gold.genomics_data_analysis` (branch not written yet)
- `gold.multi_omics_integration` (branch not written yet)
- `gold.machine_learning_in_biology` (branch not written yet)
- `purple.genetic_data_privacy` (branch not written yet)
- [yellow.nutrigenomics](../yellow/nutrigenomics.md)
