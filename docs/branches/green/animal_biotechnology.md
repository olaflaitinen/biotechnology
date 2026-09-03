<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/green/animal_biotechnology/.
  Edit the source and run `make docs`.
-->

[Green Biotechnology](index.md) / **Animal Biotechnology**

## Animal Biotechnology

`green.animal_biotechnology`

Reproductive, genomic and genetic technologies applied to livestock to improve productivity, welfare and disease resistance.

### What it is

Animal biotechnology operates in three layers that build on each other: reproductive technology multiplies the influence of chosen parents, genomic technology changes how those parents are chosen, and genetic technology alters the animal directly. Artificial insemination lets one bull sire tens of thousands of calves. Sexed semen, sorted by flow cytometry on the small DNA difference between X-bearing and Y-bearing sperm, biases the calf crop towards the productive sex. Superovulation with embryo transfer, and ovum pick-up with in vitro embryo production, do the same on the female side, where the biological ceiling is far lower. Genomic selection, adopted by the dairy industry from 2009, estimates breeding values from tens of thousands of markers in a newborn calf rather than from the milk records of its adult daughters. That roughly halves the generation interval, and because genetic gain per year is inversely proportional to it, the annual rate of improvement nearly doubled. The statistics are the same as in `green.molecular_plant_breeding`; the biology is different only in generation time and reproductive rate. Genetic technology alters the animal itself: somatic cell nuclear transfer produces a clone of an existing individual, and zygote editing produces defined changes such as knocking out the CD163 receptor that porcine reproductive and respiratory syndrome virus requires, or introducing the POLLED allele so cattle grow no horns. The binding constraint on that last layer is not technical. Editing a zygote is now routine; obtaining regulatory approval to sell the resulting animal, in most jurisdictions, is not.

### In plain language

Farmers have always bred from their best animals. The difference now is speed and precision. A DNA test on a newborn calf can predict how much milk its daughters will give, so that decision no longer waits five years. Embryos can be produced from the best cows and carried by other cows. And in a few cases a single gene can be changed: so that cattle are born without horns and never have to be painfully dehorned as calves, or so that pigs cannot catch a virus that otherwise kills millions of them every year. The animals themselves are ordinary animals. What changed is how much is known about them, and when.

### An analogy

It is the difference between judging a racehorse by watching it race for five seasons and reading a reliable form report on the day it is born. The animals are the same animals; the information arrives much earlier, so far fewer wrong turnings are taken. The comparison has a real limit. A form report is only as good as the races the scout has already seen, which is why these predictions work well within a well-recorded breed and poorly for an animal unlike anything in the reference population.

### Why it matters

Livestock account for a large share of agricultural greenhouse gas emissions and land use, and the fastest way to lower emissions per litre of milk or kilogram of meat is to raise output per animal and cut mortality. Disease resistance is the clearest case: a pig that cannot be infected needs no antibiotics, does not transmit, and does not die, which is simultaneously an economic, an animal welfare and an antimicrobial resistance argument. Hornless cattle avoid a painful procedure performed on millions of calves a year. The costs are equally concrete. Very intense selection through a small number of sires has narrowed the genetic base of the major dairy breeds to an effective population size that would concern a conservation biologist. Selecting hard for production has historically carried fertility, lameness and metabolic disease along with it, and correcting that took a deliberate change in how breeding goals are written. Somatic cell nuclear transfer remains inefficient and produces losses that are real regardless of one's position on cloning. And beneath all of it sits a question this record does not attempt to settle: these are sentient animals, some of these interventions reduce their suffering, some are indifferent to it, and public opinion distinguishes between them in ways the science does not.

### Applications

- Artificial insemination in dairy and beef cattle, which is near universal in developed dairy systems
- Sexed semen, sorting sperm by the DNA difference between X-bearing and Y-bearing cells to bias the calf crop
- Superovulation with embryo flushing and transfer
- Ovum pick-up with in vitro embryo production, which multiplies the female side where the biological ceiling is far lower than the male
- Cryopreservation of semen, oocytes and embryos, which also underpins rare breed conservation
- Genomic selection in dairy cattle, which roughly halved the generation interval and nearly doubled annual genetic gain
- Genomic selection in pigs, poultry and salmon
- Genomic management of inbreeding, using relationship matrices to constrain mating decisions rather than only to rank animals
- Parentage verification and traceability from genotype
- POLLED cattle carrying a naturally occurring hornless allele, avoiding disbudding of calves with a hot iron
- PRRS-resistant pigs produced by editing the CD163 receptor the virus requires, approved in the United States in 2025 and pending elsewhere
- Heat-tolerant cattle carrying the slick-coat allele from tropical breeds
- Cloning of elite breeding animals by somatic cell nuclear transfer, used commercially in a small number of species
- Transgenic animals as protein bioreactors, secreting a therapeutic protein into milk or egg white
- Fast-growing farmed salmon carrying a growth hormone construct, approved for sale in the United States and Canada
- Cryobanking and assisted reproduction for rare and endangered breeds

### Technologies

- Semen collection, extension and cryopreservation
- Flow-cytometric sperm sexing
- Oestrus synchronisation and fixed-time insemination protocols
- Superovulation, embryo flushing and non-surgical transfer
- Ovum pick-up, in vitro maturation, fertilisation and culture
- Vitrification of oocytes and embryos
- Single nucleotide polymorphism chips designed for each livestock species
- Genomic estimated breeding value pipelines using single-step evaluation that combines genotyped and ungenotyped animals
- International genetic evaluation across national datasets
- Sensor-based phenotyping of feed intake, rumination, activity and health, which addresses the phenotyping bottleneck this field shares with plant breeding
- Relationship-matrix constrained mate allocation to manage inbreeding
- Somatic cell nuclear transfer
- CRISPR editing of zygotes by microinjection or electroporation
- Editing of primordial germ cells, particularly in poultry where the zygote is difficult to access
- Genotype screening of edited founders for off-target and mosaic outcomes
- Surrogate sire technology, in which a germline-ablated recipient carries donor spermatogonia

### Challenges

- Loss of genetic diversity through very intense sire selection, which has driven the effective population size of major dairy breeds to levels that would concern a conservation biologist
- Unfavourable correlated responses, where selecting hard on production historically carried fertility, lameness and metabolic disease with it, and correcting that required deliberately rewriting the breeding goal rather than any new technology
- Prediction accuracy that falls sharply outside the reference population, so the breeds and regions with the least recording benefit least
- Low efficiency and high loss rates in somatic cell nuclear transfer, including large offspring syndrome and placental abnormality
- Mosaicism in edited founders, where an embryo edited after the first division carries a mixture of edited and unedited cells and must be bred out
- Public acceptance, which distinguishes sharply between an edit that reduces suffering and one that increases output, in a way the underlying science does not
- Concentration of livestock genetics in a very small number of multinational suppliers, which narrows both the gene pool and the market
- Regulatory uncertainty for edited food animals, which is the binding constraint on the whole third layer: editing a zygote is routine, and obtaining approval to sell the animal in most jurisdictions is not

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Genomic estimated breeding value | `GEBV` | trait units, as a deviation from a defined base population | expressed per trait, and combined into a selection index | CONSENSUS |
| Generation interval | `L` | years, as the average age of parents when progeny are born | 1.5 - 2 years in genomic dairy schemes, against 5 or more under progeny testing | CONSENSUS |
| Genetic gain per year | `dG/t` | genetic standard deviations or trait units per year | roughly doubled in dairy cattle after 2009 | REVIEWED |
| Reliability of genomic prediction | `r2` | squared correlation with true breeding value, dimensionless | 0.4 - 0.75 for a genomic young bull, above 0.9 for a progeny-tested one | CONSENSUS |
| Selection intensity | `i` | standard deviations of the selection differential | above 2.5 on the sire side, near 0.5 on the dam side | CONSENSUS |
| Rate of inbreeding per generation | `dF` | proportional increase in inbreeding coefficient | below 0.01 recommended; observed rates have exceeded it in some breeds | CONSENSUS |
| Effective population size | `Ne` | idealised breeding individuals | 50 - 150 in major commercial dairy breeds | REVIEWED |
| Conception rate per insemination | `CR` | per cent of inseminations resulting in a pregnancy | 30 - 60 %, and lower with sexed semen | REVIEWED |
| Cloning efficiency | `E_scnt` | per cent of reconstructed embryos yielding a live healthy birth | 1 - 10 % | REVIEWED |

### History

- **1780** - Spallanzani reports the first successful artificial insemination, in a dog
- **1936** - Lush formalises the breeder's equation, working on livestock
- **1949** - Glycerol is found to protect sperm through freezing
- **1951** - First calf born from embryo transfer
- **1975** - Best linear unbiased prediction becomes the standard method for national genetic evaluation
- **1985** - First transgenic livestock produced by pronuclear microinjection
- **1995** - Declining fertility in high-producing dairy cattle is recognised as a correlated response to decades of selection on milk yield
- **1996** - Dolly the sheep is cloned from an adult somatic cell
- **2001** - Meuwissen, Hayes and Goddard propose genomic selection
- **2009** - Genomic selection is adopted across the dairy industry
- **2016** - PRRS-resistant pigs produced by editing the CD163 receptor
- **2019** - Plasmid sequences are found integrated in hornless cattle that had been reported as free of foreign DNA
- **2020** - The first genome-edited food animal is approved for sale in the United States
- **2025** - PRRS-resistant pigs receive United States approval for food use

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | FIELD |
| Regulatory status | VARIES |
| Domains | FOOD, HEALTH |
| SDGs | 2, 3, 13 |

### Regulations

- EU Directive 98/58/EC concerning the protection of animals kept for farming purposes
- EU Directive 2010/63/EU on the protection of animals used for scientific purposes, which governs the research stage of every technique here
- EU Regulation (EC) No 1099/2009 on the protection of animals at the time of killing
- EU Regulation (EU) 2016/429, the Animal Health Law
- National provisions on disbudding, castration and other routine procedures, which are the specific practices some edits in this record are designed to make unnecessary
- EU Regulation (EU) 2016/1012 on zootechnical and genealogical conditions for breeding, trade and entry of purebred breeding animals, which regulates breed societies, herd books and the publication of breeding values rather than any authorised product
- National herd book and breeding programme approvals
- US FDA guidance on intentional genomic alterations in animals, under which the alteration is regulated as a new animal drug
- EU Directive 2001/18/EC and Regulation (EC) No 1829/2003, under which an edited animal is a genetically modified organism and its products require authorisation
- Cartagena Protocol on Biosafety, governing transboundary movement of living modified animals
- National cloning provisions, several of which restrict food from clones or require labelling
- WOAH Terrestrial Animal Health Code, including the chapters on collection and processing of semen and embryos
- EU Regulation (EU) 2020/692 on entry into the Union of animals and germinal products
- Nagoya Protocol and the FAO Global Plan of Action for Animal Genetic Resources, where breeds and germplasm cross borders

### Standards

- ICAR guidelines for performance recording, which define how milk yield, weight and health events must be recorded to be usable in an evaluation
- Interbull international genetic evaluation standards, which convert national breeding values onto a common scale and are the reason a bull ranked in one country can be bought in another
- ISO 24631 series on radio frequency identification of animals, which is how an animal is tied to its own record
- International Embryo Technology Society manual for sanitary handling and processing of embryos
- Certified Semen Services standards for bull stud health and semen quality
- Welfare Quality assessment protocols for cattle, pigs and poultry
- AWIN welfare assessment protocols
- FAO Guidelines on cryoconservation of animal genetic resources
- FAO Domestic Animal Diversity Information System reporting, which is how the effective population size figures in `metrics.py` are tracked
- Whole-genome sequencing based characterisation of edited founders, expected rather than encouraged since the 2019 episode recorded in `history.py`

### Related records

- `green.molecular_plant_breeding`
- `green.veterinary_vaccines`
- `green.agricultural_genome_editing`
- `red.regenerative_medicine`
- `blue.aquaculture_biotechnology`
- `yellow.alternative_proteins`
- `purple.bioethics`

### Cross-references

- [green.molecular_plant_breeding](molecular_plant_breeding.md)
- [green.veterinary_vaccines](veterinary_vaccines.md)
- [green.agricultural_genome_editing](agricultural_genome_editing.md)
- [red.regenerative_medicine](../red/regenerative_medicine.md)
- [blue.aquaculture_biotechnology](../blue/aquaculture_biotechnology.md)
- [yellow.alternative_proteins](../yellow/alternative_proteins.md)
- `purple.bioethics` (branch not written yet)
