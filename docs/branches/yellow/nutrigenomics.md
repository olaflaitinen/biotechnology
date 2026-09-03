<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/yellow/nutrigenomics/.
  Edit the source and run `make docs`.
-->

[Yellow Biotechnology](index.md) / **Nutrigenomics**

## Nutrigenomics

`yellow.nutrigenomics`

The interaction between diet and the genome, where monogenic effects are established and the polygenic personalisation being sold is not.

### What it is

Nutrigenomics covers two questions that are frequently conflated. Nutrigenetics asks how a person's genotype affects their response to food. Nutrigenomics proper asks how food affects gene expression, which is a mechanistic question about regulation rather than a predictive one about individuals. The commercial field concerns the first, and within it the distinction that matters is between monogenic effects, where one variant has a large consequence, and polygenic ones, where many variants each have a small consequence. The monogenic half is established and clinically useful. Phenylketonuria is a single-gene disorder in which dietary phenylalanine causes irreversible neurological damage, it is detected by newborn screening in most health systems, and dietary management prevents the damage entirely. Lactase persistence is a well-characterised variant determining whether an adult digests lactose. Hereditary haemochromatosis alters iron handling with direct dietary and clinical consequences. Coeliac disease risk depends on defined HLA types, and their absence effectively excludes the diagnosis. These are real gene-diet interactions with large effects, and they were understood before the field acquired its name. The polygenic half is what is sold and what the evidence does not support. Common variants associated with body weight, lipid response or caffeine metabolism have small individual effects, and the interaction between such a variant and a dietary component is smaller again. Detecting an interaction reliably requires far larger samples than detecting a main effect, and most published gene-diet interactions have not replicated. The largest controlled trials assigning diets by genotype have found no advantage over assigning them otherwise. What has predicted individual response better than genotype is more interesting than the negative result alone. Studies measuring postprandial glucose and lipid responses have found large and reproducible differences between people eating identical meals, and that those differences are predicted substantially by the gut microbiome, by meal composition, by sleep and by physical activity, with genetics contributing modestly. Personalised nutrition is therefore a defensible idea whose best current basis is not genomic, which is an awkward finding for a field named after genomes.

### In plain language

This is the study of how what you eat interacts with the genes you were born with. Some of it is completely established. A small number of people have a single gene difference that means a particular food genuinely harms them, and newborn babies are tested for one of these because catching it early prevents permanent brain damage. Whether adults can digest milk is also down to one well-understood gene. But the tests sold online promising a diet matched to your DNA are a different matter. When researchers have tested that properly, matching diets to genes has not worked better than not doing so. What does seem to predict how someone responds to a meal is their gut bacteria, their sleep and their activity, more than their genes.

### An analogy

A severe nut allergy is a genuine instruction about what one person must not eat, and nobody doubts it. The claim being sold is that everyone carries a comparable set of instructions, subtler but equally real, waiting to be read from their DNA. The comparison is where the argument breaks: the allergy is a large effect in a few people, and what the tests report is a collection of very small effects in everyone, which is a different kind of thing and not simply a quieter version of the same one.

### Why it matters

The established part of this field prevents severe and permanent harm. Newborn screening for phenylketonuria, followed by dietary management, prevents irreversible intellectual disability, and it is among the clearest demonstrations anywhere that a gene-diet interaction can be identified and acted on. Understanding lactase persistence explains a difference in digestion across populations that was previously described as an abnormality in the majority of the world's adults. Defined HLA types make it possible to exclude coeliac disease rather than only to suspect it. The costs of the unestablished part are real too. Direct-to-consumer tests sell dietary advice on variants whose effects are small and whose interactions with diet have frequently failed to replicate, and the advice given is usually generic advice with a genetic justification attached. That is not harmless: it displaces attention from interventions that work, it risks people restricting foods on weak evidence, and it lends the authority of a genome to a recommendation that did not come from one. The field also carries a genuine privacy exposure, since a dietary test is a genetic test and the data is subject to the concerns `purple.genetic_data_privacy` sets out, frequently without the consent process a clinical test would require. And the most useful recent finding in personalised nutrition, that response is predicted better by the microbiome and by behaviour than by genotype, is one the commercial layer of this field has been slow to absorb.

### Applications

- Newborn screening for phenylketonuria followed by lifelong dietary phenylalanine restriction, which prevents irreversible intellectual disability and is among the clearest gene-diet interactions ever acted on
- Dietary management of other inherited metabolic disorders detected by newborn screening, including galactosaemia and maple syrup urine disease
- HLA typing to exclude coeliac disease, where the absence of defined types effectively rules out the diagnosis and prevents unnecessary lifelong restriction
- Hereditary haemochromatosis genotyping, which identifies people whose iron handling makes dietary and therapeutic iron management necessary
- Familial hypercholesterolaemia identification, where the genetic diagnosis changes management from dietary advice to pharmacological treatment
- Lactase persistence genotyping, which explains rather than guides, since a person generally knows whether milk troubles them without a test
- Alcohol dehydrogenase and aldehyde dehydrogenase variants, which have large effects on alcohol metabolism and known health consequences
- Caffeine metabolism genotype, which is the most defensible of the common consumer test claims and still has modest predictive value for any individual outcome
- Transcriptomic and epigenetic studies of how specific nutrients regulate gene expression, which is nutrigenomics proper and is legitimate mechanistic science
- Investigation of early-life and prenatal nutrition effects on later metabolic health, including the epigenetic work following historical famine cohorts
- Nutrient regulation of transcription factors and metabolic pathways in model systems
- Population-level explanation of dietary adaptation, including lactase persistence, amylase copy number and variants associated with historical diets, which is evolutionary biology rather than dietary advice
- Direct-to-consumer genetic tests offering diet recommendations from panels of common variants, which is the commercial bulk of the field and which controlled trials have not shown to outperform generic advice
- Genotype-matched weight loss diets, which the largest controlled trials found no better than diets assigned without genotype
- Polygenic scores for nutrition-related traits, which have research value and insufficient individual predictive power for dietary prescription
- Personalised nutrition based on postprandial glucose and lipid response, the gut microbiome, sleep and activity, which has outperformed genotype in the studies that compared them and which is where the defensible version of personalisation now sits

### Technologies

- Targeted genotyping of defined clinically actionable variants, which is what the established applications use and is cheap and reliable
- Genotyping arrays and whole genome sequencing for research cohorts
- Polygenic score construction, with the discipline of validating in an ancestry-matched population, since scores derived in one population transfer poorly to another
- Transcriptomics to measure how a nutrient changes expression, which is mechanistic and makes no individual prediction
- Epigenetic profiling including DNA methylation, used in the early-life nutrition work
- Metabolomics and lipidomics, which measure what a person's metabolism is actually doing rather than what their genome permits
- Continuous glucose monitoring for postprandial response, which produced the finding that individual responses to identical meals differ far more than expected
- Gut microbiome profiling as a predictor of dietary response, which outperformed genotype in the studies that compared them and connects this record to `yellow.probiotics_and_prebiotics`
- Wearable and dietary intake measurement, which supplies the behavioural variables that carried much of the predictive power
- Interaction analysis with adequate power, which requires far larger samples than main-effect analysis and is the methodological reason most published gene-diet interactions have not replicated
- Mendelian randomisation, which uses genetic variants to test whether a dietary exposure causes an outcome rather than to personalise advice, and is the field's most productive genetic method
- Preregistration and replication in independent cohorts, which is the practice whose absence produced the field's replication problem

### Challenges

- Small effect sizes for common variants, and smaller effects still for their interaction with a dietary component, so an interaction requires far larger samples to detect reliably than a main effect does
- Widespread failure to replicate published gene-diet interactions, which follows directly from the point above combined with flexible analysis and selective reporting
- Absence of trial evidence that genotype-matched diets outperform alternatives, which is the finding the commercial layer of the field has not absorbed
- Dietary intake measurement error, since self-reported intake is systematically inaccurate and an interaction cannot be estimated more precisely than the exposure it involves
- Confounding by ancestry, since both genotype and dietary pattern vary with population structure and an uncontrolled association may reflect neither biology nor diet
- Overwhelming derivation of polygenic scores from European-ancestry cohorts, so they transfer poorly to other populations, which makes this field's equity problem the same one `gold.genomics_data_analysis` records
- Direct-to-consumer tests giving generic dietary advice with a genetic justification attached, which lends the authority of a genome to a recommendation that did not come from one
- Displacement of attention from interventions with strong evidence towards personalisation with weak evidence, which is the practical harm of an otherwise ineffective product
- Risk of unnecessary dietary restriction based on a variant with a small effect, particularly where a consumer interprets a risk score as a diagnosis
- Genetic privacy, since a dietary test is a genetic test and the resulting data is frequently collected without the consent process a clinical test would require, and is retained and shared under commercial terms
- Incidental findings of clinical significance in a test sold for dietary purposes, with no clinical pathway to interpret or act on them
- The finding that microbiome and behaviour predict dietary response better than genotype, which is a problem for a field named after genomes and which the research half has accepted faster than the commercial half

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Effect size of a common variant | `beta` | trait units per risk allele, or odds ratio | odds ratios commonly between 1.05 and 1.20 for common variants in nutrition-related traits | CONSENSUS |
| Sample size required to detect an interaction | `N_int` | participants | roughly four times the sample needed for a main effect of the same magnitude, and gene-diet interactions are smaller to begin with | CONSENSUS |
| Replication rate of published gene-diet interactions | `f_repl` | per cent of reported interactions confirmed in independent cohorts | low | REPORTED |
| Variance explained by a polygenic score | `R2_PGS` | per cent of trait variance explained | single digits for most nutrition-related traits | CONSENSUS |
| Portability of a polygenic score across ancestries | `P_anc` | relative predictive performance in a non-matched population | substantially reduced outside the ancestry the score was derived in | CONSENSUS |
| Number needed to genotype | `NNG` | people tested per person whose management changes | very small for clinically actionable monogenic variants and very large for common variant panels | REVIEWED |
| Penetrance of a monogenic variant | `f_pen` | per cent of carriers showing the phenotype | essentially complete for phenylketonuria; variable for hereditary haemochromatosis | CONSENSUS |
| Newborn screening coverage | `f_screen` | per cent of births screened for treatable metabolic disorders | high in health systems with an established programme, and absent in many others | REVIEWED |
| Interindividual variability in postprandial response | `CV_pp` | coefficient of variation in glucose or lipid response to an identical meal | large, and considerably greater than variability within one person on repeat testing | REVIEWED |
| Predictive contribution of the microbiome relative to genotype | `f_micro` | relative contribution to a predictive model of dietary response | microbiome and behavioural features have contributed more than genetic features in the studies that compared them | REPORTED |
| Difference in outcome between genotype-matched and unmatched diets | `dOutcome` | difference in weight, lipid or glycaemic outcome | no significant advantage found in the largest controlled trials | REVIEWED |
| Adherence to the assigned diet | `f_adhere` | per cent of participants following the assigned diet | the dominant determinant of outcome in dietary trials, exceeding any genotype effect | CONSENSUS |

### History

- **1934** - Phenylketonuria is described as an inherited metabolic disorder
- **1963** - Newborn screening for phenylketonuria is introduced at population scale
- **1965** - Lactase persistence is characterised as a genetic trait
- **2000** - Nutrigenomics is named as a field alongside the sequencing of the human genome
- **2004** - Direct-to-consumer genetic tests offering dietary advice reach the market
- **2008** - Epigenetic effects of prenatal nutrition are demonstrated in historical famine cohorts
- **2010** - Large-scale replication efforts find that most published gene-diet interactions do not hold
- **2014** - Mendelian randomisation becomes established for testing dietary causal hypotheses
- **2015** - Postprandial responses are shown to vary greatly between individuals and to be predicted substantially by the gut microbiome
- **2018** - A large randomised trial finds no advantage to genotype-matched weight loss diets
- **2020** - Polygenic score portability across ancestries is documented as a systematic limitation
- **2021** - Large personalised nutrition studies confirm that microbiome and behavioural features predict dietary response better than genotype
- **2023** - Genetic privacy concerns reach consumer nutrition testing

### Governance

| Field | Value |
|---|---|
| Maturity | EMERGING |
| Risk tier | REGULATED |
| Scale | POPULATION |
| Regulatory status | VARIES |
| Domains | HEALTH, FOOD, INFORMATION |
| SDGs | 3 |

### Regulations

- Regulation (EU) 2017/746 on in vitro diagnostic medical devices, which brought many genetic tests within scope regardless of the claim made and which narrowed the wellness exemption considerably
- Requirements for genetic counselling and informed consent attached to predictive genetic testing in several member states, which apply to the clinical route and frequently not to the consumer one
- United States regulation of laboratory developed tests and of direct-to-consumer genetic health risk reports, whose scope has been contested and repeatedly revised
- Regulation (EC) No 1924/2006 on nutrition and health claims, under which the dietary claims attached to these tests have no authorisation, so products are sold on implication in the same way `yellow.probiotics_and_prebiotics` records
- Directive 2005/29/EC on unfair commercial practices, which is the instrument actually used against overstated personalisation claims
- Regulation (EU) 2016/679, under which genetic data is a special category requiring explicit consent and heightened protection, and which applies whether the test was sold as clinical or as wellness
- National genetic non-discrimination provisions restricting the use of genetic information in insurance and employment, which vary widely and are absent in many jurisdictions
- Cross-border data transfer rules, which matter because consumer genomics is concentrated in a small number of companies operating internationally
- Accreditation requirements for genetic testing laboratories, which govern whether a reported genotype is accurate and say nothing about whether the advice attached to it follows from it
- Regulation (EU) No 536/2014 on clinical trials and equivalent frameworks, which govern the dietary intervention studies this record's claims should rest on
- Research ethics approval and biobank governance for the cohorts the field depends on

### Standards

- Preregistration of analysis plans and replication in independent cohorts, which is the practice whose absence produced the interaction literature that did not survive testing
- Reporting guidelines for genetic association and gene-environment interaction studies, including explicit power calculation for the interaction rather than for the main effect
- CONSORT reporting for dietary intervention trials, and registration before enrolment
- ACMG and equivalent variant classification frameworks, which distinguish pathogenic variants from those of uncertain significance and which consumer reports frequently do not apply
- Conventions requiring polygenic scores to be reported with the ancestry they were derived in and their performance in the population being tested
- Requirements to report effect sizes alongside associations, since an association reported without its magnitude conveys the existence of an effect and not its irrelevance
- ISO 15189 accreditation for medical laboratories
- Consent, retention, secondary use and deletion conventions for consumer genetic data, which are set by contract rather than by standard and which have changed with corporate ownership
- Dietary guideline development conventions, which is what the established evidence actually supports and which this record's commercial layer positions itself against
- Multi-modal personalisation reporting, covering microbiome, behavioural and continuous monitoring inputs alongside any genetic ones, which is where the defensible version of personalised nutrition now sits

### Related records

- `yellow.probiotics_and_prebiotics`
- `gold.genomics_data_analysis`
- `purple.genetic_data_privacy`
- `yellow.biofortification`
- `red.pharmacogenomics`
- `red.molecular_diagnostics`

### Cross-references

- [yellow.probiotics_and_prebiotics](probiotics_and_prebiotics.md)
- `gold.genomics_data_analysis` (branch not written yet)
- `purple.genetic_data_privacy` (branch not written yet)
- [yellow.biofortification](biofortification.md)
- [red.pharmacogenomics](../red/pharmacogenomics.md)
- [red.molecular_diagnostics](../red/molecular_diagnostics.md)
