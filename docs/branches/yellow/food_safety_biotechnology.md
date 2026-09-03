<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/yellow/food_safety_biotechnology/.
  Edit the source and run `make docs`.
-->

[Yellow Biotechnology](index.md) / **Food Safety Biotechnology**

## Food Safety Biotechnology

`yellow.food_safety_biotechnology`

Molecular detection of pathogens, toxins, allergens and adulteration in food, and the genomic tracing of outbreaks to their source.

### What it is

Food safety biotechnology applies molecular and immunological methods to determining what is in food and where it came from. Its defining achievement is not sensitivity but speed. Culture-based detection requires an organism to grow, which takes days, and for a chilled product with a short shelf life the result arrives after the food has been eaten. Molecular detection returns an answer in hours, while the batch is still under the producer's control. That single change converted testing from a record of what happened into a decision about what to release, and everything else in this record follows from it. Four things are looked for. Pathogens, chiefly Salmonella, Listeria monocytogenes, Campylobacter and Shiga toxin-producing Escherichia coli, are detected by nucleic acid amplification after a short enrichment, since even molecular methods need enough target to find. Toxins including mycotoxins, marine biotoxins and bacterial toxins are measured by immunoassay and mass spectrometry, and matter because a toxin survives the heat that kills the organism producing it. Allergens are quantified by immunoassay and increasingly by mass spectrometry, and their control is a labelling and cleaning problem as much as a detection one. Authenticity testing determines whether a food is what it claims to be, by species, by origin and by composition. Whole genome sequencing produced the second transformation. Comparing isolates at single-nucleotide resolution links cases separated by time and geography that no previous method could connect, which turned outbreak investigation from a matter of interviewing patients about what they ate into a matter of matching genomes between a clinical case and a food sample. Routine sequencing of isolates by public health laboratories detects clusters that were previously invisible, including small outbreaks spread across countries. The constraints are not analytical. Sampling dominates: a pathogen is distributed unevenly through a batch, so a negative result on a few hundred grams says less about a lorry-load than the precision of the method suggests. Molecular methods detect nucleic acid rather than viable organisms, so a positive may reflect a dead cell, which matters after a kill step. And the sensitivity of genomic surveillance creates its own problem: a cluster of three cases in three countries is now detectable and must be interpreted, which is a demand on epidemiological judgement rather than on laboratory capacity.

### In plain language

This is testing food to find out whether it contains something dangerous, and working out where a contaminated batch came from. The important change was not that the tests got better at finding things. It was that they got faster. The old method meant growing bacteria in a laboratory, which takes days, by which time a fresh product has already been sold and eaten. The new methods give an answer in hours, while the food is still in the factory, so a problem can be stopped instead of investigated. The same techniques also show whether food is what it claims to be, which turns out to matter for safety as well as for honesty.

### An analogy

It is the difference between a smoke alarm and a fire report. Both tell you a fire happened; only one tells you while you can still do something. The comparison understates one difficulty. A smoke alarm sits in the room with the smoke, and a food test examines a few hundred grams taken from a consignment of many tonnes, so a clear result means the sample was clean rather than the lorry.

### Why it matters

Foodborne illness affects a very large number of people every year and kills a substantial number of them, most of whom are children, elderly or immunocompromised. Rapid detection stops contaminated product before it ships, which prevents illness rather than documenting it. Genomic surveillance has repeatedly identified outbreaks that no one had noticed were outbreaks, because the cases were few, far apart and separately unremarkable, and linking them located contaminated sites that would otherwise have continued producing. Allergen detection is what makes a may-contain declaration something other than a guess, and for a person with a severe allergy the difference is not academic. Authenticity testing addresses a category of harm that food safety frameworks were not designed for, and the 2008 melamine adulteration, which killed infants and injured many thousands, was an economic crime detected as a safety failure. The costs are worth stating precisely. Sampling remains the weak point and no improvement in analytical sensitivity addresses it. Molecular methods detect nucleic acid rather than live organisms, which produces positives that mean nothing after a kill step and consequent product loss. Testing capacity is very unevenly distributed, so the countries exporting food are frequently not the ones able to test it, and a system that relies on importing-country testing pushes cost and risk in a direction that is not obviously fair. And genomic surveillance identifies clusters faster than public health systems can always act on them, which converts a laboratory advance into a resourcing problem.

### Applications

- Rapid detection of Salmonella, Listeria monocytogenes, Campylobacter and Shiga toxin-producing Escherichia coli by nucleic acid amplification after short enrichment, returning a result while the batch is still on site
- Environmental monitoring of processing surfaces and drains, which finds the resident contamination that will eventually reach product and is more informative than testing the product itself
- Verification of kill steps and of hygiene controls as part of hazard analysis, which is what the results are actually used for
- Testing of ready-to-eat foods against the end-of-shelf-life criteria that `yellow.food_biopreservation` exists to meet
- Whole genome sequencing of clinical and food isolates to link cases that no other method connects, including small clusters spread across countries and across months
- Source attribution tracing a clinical isolate back to a production site, which converts an outbreak investigation from interviewing patients into matching genomes
- Routine sequencing of isolates by public health laboratories, which detects outbreaks nobody had noticed were outbreaks
- Mycotoxin measurement in cereals, nuts, spices and dried fruit, where the toxin persists long after the fungus that produced it has gone
- Marine biotoxin monitoring in shellfish, which is a public health surveillance programme rather than a product test and which closes harvesting areas
- Detection of heat-stable bacterial toxins, which survive cooking and are therefore not addressed by any kill step
- Quantification of milk, egg, peanut, tree nut, gluten and other regulated allergens in product and on cleaned equipment
- Cleaning validation between production runs, which is where allergen control is actually exercised and where a precautionary label is either justified or avoided
- Gluten-free verification against the defined threshold, which is one of the few allergen claims with a numerical legal definition
- Species identification in meat and fish products, which detects substitution that is economic in motive and can be a safety and a religious dietary matter in effect
- Geographical origin determination by stable isotope and elemental profiling, which supports protected designations and detects misdeclaration
- Detection of adulteration in high-value commodities including honey, olive oil, spices and infant formula, the last of which is where adulteration has killed
- Verification of organic, halal, kosher and free-from claims, where the declaration is unverifiable by inspection alone

### Technologies

- Statistically designed sampling plans, which determine what a negative result means and which no analytical improvement substitutes for
- Enrichment culture before molecular detection, still necessary because even sensitive methods require enough target and because it also distinguishes viable organisms from residual nucleic acid
- Sample preparation from difficult matrices, since fat, protein and polyphenols inhibit amplification and food is an unhelpful matrix in ways a clinical sample is not
- Real-time and digital PCR for pathogen detection and quantification
- Immunoassay formats including ELISA and lateral flow for toxins and allergens
- Mass spectrometry for mycotoxins, allergen peptides and adulterants, which is the reference method where an immunoassay result is disputed
- Whole genome sequencing and core genome multilocus typing for isolate comparison, which is what makes outbreak linkage possible
- Metagenomic and 16S profiling of production environments
- Isothermal amplification methods that need no thermal cycler and therefore no laboratory
- Portable sequencing for on-site typing, which shortens the interval between a result and a decision
- Biosensors and lateral flow devices usable by a production operator rather than an analyst
- Freeze-dried cell-free sensors from `white.cell_free_biomanufacturing`, which put a specific molecular test where there is no laboratory at all
- Reference databases and cluster definitions for genomic comparison, without which a sequence difference cannot be called a match
- Blockchain and digital traceability systems, which record where a consignment went and are only as good as the data entered into them
- Predictive modelling linking a detection to a risk decision, since a positive result requires a proportionate response rather than an automatic one

### Challenges

- Sampling, since a pathogen is distributed unevenly through a batch and a negative result on a few hundred grams says far less about a consignment than the precision of the method implies, which is a statistical limit rather than an analytical one
- Low prevalence combined with severe consequence, which means the tests that matter most are the ones almost always negative, and a system judged on its negatives is hard to keep sharp
- Detection of nucleic acid rather than viable organisms, so a positive after a kill step may reflect dead cells and cause avoidable product loss
- Matrix inhibition, since fat, protein and polyphenols interfere with amplification and food is a far less cooperative sample than blood
- Interpretation of a genomic cluster, since sequences that are close are not necessarily epidemiologically linked and a difference threshold is a convention rather than a fact
- Proportionate response to a detection, where the alternatives are an expensive recall and an unacceptable risk and the evidence is frequently incomplete
- Public health capacity to act on clusters that surveillance now detects faster than investigators can follow, which turns a laboratory advance into a resourcing problem
- Very uneven distribution of testing capacity, so the countries exporting food are frequently not those able to test it, and a system relying on importing-country testing pushes cost and risk in a direction that is not obviously fair
- Cost per test at the frequency that meaningful sampling requires, which is a constraint on small producers rather than on large ones
- Viruses including norovirus, which cause a large share of foodborne illness, cannot be cultured routinely, and are therefore detected only as nucleic acid with all the viability ambiguity that carries
- Allergen quantification variability between methods, since immunoassays respond differently to processed proteins and a result depends on the kit as well as on the food
- Adulterants designed to defeat the test, as melamine was chosen specifically to raise apparent protein content, which makes authenticity testing an adversarial rather than an analytical problem

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Time to result | `t_result` | hours from sample receipt to reportable answer | 2 - 24 h for molecular methods including enrichment, against 48 - 120 h for culture confirmation | CONSENSUS |
| Enrichment time | `t_enrich` | hours of incubation before detection | 6 - 24 h, and the dominant component of the entry above | CONSENSUS |
| Limit of detection | `LOD` | colony forming units per twenty-five grams of sample | 1 - 10 CFU per 25 g after enrichment | CONSENSUS |
| Diagnostic sensitivity and specificity | `Se_Sp` | per cent, against a reference method on the same matrix | both above 95 % for validated methods | CONSENSUS |
| Probability of detection at a given prevalence | `P_det` | probability that a contaminated lot is detected by the sampling plan | low for the low prevalences that matter, even with a perfect method | CONSENSUS |
| False positive rate | `R_fp` | per cent of positives not confirmed by the reference method | low for validated methods and consequential when it occurs | REVIEWED |
| Viable versus total nucleic acid discrimination | `f_viable` | qualitative, whether the method distinguishes live from dead cells | not distinguished by standard amplification without a viability treatment | CONSENSUS |
| Genomic cluster distance threshold | `d_SNP` | single nucleotide polymorphisms or allele differences between isolates | commonly fewer than 5 to 10 differences taken as evidence of a close epidemiological relationship | REVIEWED |
| Outbreak detection interval | `t_outbreak` | days from first case to cluster identification | substantially shortened by routine genomic surveillance | REVIEWED |
| Allergen quantification limit | `LOQ_allergen` | milligrams of allergen protein per kilogram of food | single-digit mg/kg for validated immunoassays; the gluten-free threshold is 20 mg/kg | CONSENSUS |
| Mycotoxin maximum level | `c_myco` | micrograms per kilogram | set in legislation by toxin and food category, with the tightest limits on infant food | CONSENSUS |
| Species substitution rate in surveys | `f_subst` | per cent of sampled products not matching their declared species | repeatedly found to be substantial in fish and in some meat products | REPORTED |

### History

- **1881** - Pure culture technique establishes the method food microbiology would use for a century
- **1960** - Aflatoxin is identified after a mass poisoning of farmed turkeys
- **1971** - Hazard analysis and critical control points is adopted as a framework for food safety
- **1985** - Polymerase chain reaction makes rapid nucleic acid detection possible
- **1993** - A large Escherichia coli O157 outbreak in undercooked beef changes food safety regulation
- **1996** - Real-time PCR enters routine food testing
- **2008** - Melamine adulteration of milk and infant formula kills infants and injures many thousands
- **2011** - A large Shiga toxin-producing Escherichia coli outbreak is resolved by rapid genome sequencing
- **2013** - The horsemeat incident establishes food authenticity as a mainstream concern
- **2015** - Routine whole genome sequencing of isolates begins in public health surveillance
- **2018** - Metagenomic and culture-independent methods are applied to food testing
- **2020** - Portable sequencing and isothermal methods move testing out of the laboratory
- **2022** - Sampling rather than analytical sensitivity is recognised as the binding constraint

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | POPULATION |
| Regulatory status | AUTHORISED |
| Domains | HEALTH, FOOD, INFORMATION |
| SDGs | 3, 12, 17 |

### Regulations

- Regulation (EC) No 178/2002 general food law, whose withdrawal and notification duties turn a positive result into a legal obligation rather than information to be weighed, and which establishes the Rapid Alert System for Food and Feed
- Regulation (EC) No 2073/2005 on microbiological criteria for foodstuffs, which sets food safety criteria and process hygiene criteria, and which states that meeting a criterion verifies control rather than demonstrating safety
- Regulation (EC) No 852/2004 on hygiene, under which testing sits inside hazard analysis rather than replacing it
- Regulation (EU) 2017/625 on official controls, which designates official laboratories, requires accreditation and establishes the reference laboratory network that arbitrates method disputes
- Method validation requirements against reference standards, without which a result cannot be used for official control however good the method
- Regulation (EC) No 1881/2006 setting maximum levels for contaminants including mycotoxins and marine biotoxins, with the tightest limits on food for infants
- Regulation (EU) No 1169/2011 on food information, whose Annex II fixes the allergens that must be declared and therefore what must be detectable
- Implementing rules on gluten-free labelling, which set the twenty milligrams per kilogram threshold that makes the claim measurable
- Regulation (EU) 2017/625 provisions on fraudulent and deceptive practices, which brought food fraud explicitly within official control
- Regulation (EU) No 1151/2012 on quality schemes, whose protected designations are enforced partly by the origin testing in this record
- Regulation (EU) 2016/679, applicable where clinical isolate sequences from identified patients are shared across borders for outbreak investigation, which is a genuine tension between surveillance and data protection

### Standards

- ISO 6579 for Salmonella, ISO 11290 for Listeria monocytogenes and the related horizontal methods, which are the reference methods alternatives must be validated against
- ISO 16140 for method validation and verification, which is the standard that decides whether a rapid method may substitute for a reference one
- AOAC and equivalent certification schemes for commercial test kits
- ISO/IEC 17025 accreditation, without which a result carries no official weight regardless of its accuracy
- Proficiency testing and interlaboratory comparison schemes, which is how a laboratory demonstrates that its results agree with everyone else's
- Measurement uncertainty estimation and reporting, which matters because a result close to a legal limit is a decision about uncertainty rather than about a number
- Codex Alimentarius sampling plans and the two-class and three-class attribute plans, which define what a negative result actually means
- Environmental monitoring programme design, which samples the problem rather than the product and which the 2022 recognition in `history.py` pushed to the centre
- Core genome multilocus sequence typing schemes and agreed cluster thresholds, which make sequences comparable between laboratories and countries
- Sequence data sharing conventions and public repositories, which are what make cross-border outbreak detection possible and which run into the data protection tension noted above
- Codex Alimentarius general principles of food hygiene and HACCP
- GFSI-recognised certification schemes including FSSC 22000, BRCGS and IFS, which impose testing requirements beyond the legal minimum and are what a retailer actually audits against

### Related records

- `red.molecular_diagnostics`
- `yellow.food_biopreservation`
- `dark.biosurveillance`
- `yellow.food_fermentation`
- `green.veterinary_vaccines`
- `purple.genetic_data_privacy`

### Cross-references

- [red.molecular_diagnostics](../red/molecular_diagnostics.md)
- [yellow.food_biopreservation](food_biopreservation.md)
- `dark.biosurveillance` (branch not written yet)
- [yellow.food_fermentation](food_fermentation.md)
- [green.veterinary_vaccines](../green/veterinary_vaccines.md)
- `purple.genetic_data_privacy` (branch not written yet)
