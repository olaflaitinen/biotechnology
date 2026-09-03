<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/green/molecular_plant_breeding/.
  Edit the source and run `make docs`.
-->

[Green Biotechnology](index.md) / **Molecular Plant Breeding**

## Molecular Plant Breeding

`green.molecular_plant_breeding`

Accelerating conventional breeding with DNA markers and genomic prediction so that selection happens at the seedling stage.

### What it is

Classical breeding evaluates a plant by growing it. Phenotype is observed, superior individuals are crossed, and the cycle repeats once per season. Every wrong candidate occupies field space, water and a year. Molecular breeding replaces part of that observation with genotyping. Marker-assisted selection works where a trait is controlled by one or a few large-effect loci: a DNA marker tightly linked to the favourable allele is scored in a seedling, and unwanted individuals are discarded before they reach the field. Marker-assisted backcrossing additionally selects against the donor genome elsewhere, recovering the recurrent parent in three generations rather than six. Most traits of economic value are polygenic, and for those genomic selection is used instead. A training population is both genotyped and phenotyped; a statistical model estimates the effect of every marker simultaneously rather than testing them one at a time; the model then predicts a genomic estimated breeding value for candidates that have never been grown. No individual marker needs to reach significance, which is what makes the method work for traits controlled by thousands of loci of tiny effect. Combined with speed breeding under extended photoperiod, this compresses the breeding cycle from years to months. The quantity being optimised is not accuracy but genetic gain per unit time, and shortening the cycle raises it even when prediction accuracy falls, which is why breeders will trade one for the other deliberately.

### In plain language

Breeding a better wheat variety used to mean planting thousands of seedlings, waiting a whole season, measuring which ones did best, and starting again. Now a tiny piece of leaf from a two-week-old seedling can be tested and its DNA read like a form guide. The plants unlikely to perform are removed before they take up space, and only the promising ones are grown on. The plants themselves are entirely ordinary. Nothing has been added to them and nothing has been changed; every one of them could have been produced by a farmer with a paintbrush and enough patience. What changed is the speed of choosing between them.

### An analogy

It is the difference between auditioning every candidate for a full season and reading their references first. The audition still happens, but only for the shortlist, so the same effort covers far more candidates. The comparison has an honest limit: references are only useful if the referee has seen people like this candidate before. Predict for a plant unrelated to anything in the training set and the accuracy collapses, which is the central practical weakness of the method.

### Why it matters

Almost all of the yield improvement in the world's staple crops over the last thirty years came from breeding, not from transgenes, and molecular tools roughly doubled the rate at which breeders can deliver it. Because nothing foreign is introduced, the resulting varieties face no special regulatory hurdle anywhere in the world. That makes this the most transferable technology in the green branch: national programmes and CGIAR centres use it as routinely as multinationals do, and a genotyping service costs a few euro per sample rather than tens of millions per event. The costs are real but different in kind. Genotyping has become cheap enough that phenotyping is now the bottleneck, and measuring a thousand plots accurately is expensive and unglamorous work that funders do not like paying for. Prediction models trained on elite material perform badly on landraces and wild relatives, which risks narrowing the genetic base further at exactly the moment climate variability makes breadth most valuable. And the public and private sectors both hold data they will not share, so the largest single improvement available to the field, meaning bigger and more diverse training populations, is blocked by something that is not a scientific problem at all.

### Applications

- Marker-assisted backcrossing of rust resistance genes into elite wheat
- Submergence-tolerant rice carrying the SUB1A locus, which survives two weeks under floodwater and is now grown by millions of smallholders
- Pyramiding several bacterial blight resistance genes into one rice variety, which is impossible to select for by phenotype because one gene masks another
- Downy mildew and virus resistance in vegetable crops
- Male sterility and restorer systems for hybrid seed production
- Genomic selection in hybrid maize breeding programmes
- Genomic prediction of grain yield and quality in wheat and barley
- Genomic selection in perennial and tree crops, where a single generation can take a decade and the saving is correspondingly larger
- Selection for baking and malting quality, which conventionally requires destroying a sample and running a full process test
- Selection for root architecture, which cannot be measured without digging the plant up
- Speed breeding under extended photoperiod, delivering up to six generations a year in wheat instead of one or two
- Doubled-haploid production, reaching complete homozygosity in one step rather than six generations of selfing
- Pre-breeding from landraces and crop wild relatives, using markers to track a useful allele through the linkage drag that surrounds it
- Purity and identity verification of commercial seed lots

### Technologies

- Single nucleotide polymorphism genotyping arrays
- Genotyping-by-sequencing and skim sequencing, which cost less per sample and give a different set of markers each time
- Targeted amplicon panels for a defined set of known loci
- Imputation from a low-density panel to a high-density reference
- Quantitative trait locus mapping in biparental populations
- Genome-wide association studies in diversity panels
- Haplotype-based analysis, which uses linked blocks rather than single markers
- Genomic best linear unbiased prediction and the Bayesian alphabet
- Machine-learning predictors for non-additive effects
- Multi-environment models incorporating weather and soil covariates, which is how genotype-by-environment interaction is handled rather than ignored
- High-throughput field phenotyping with drones and multispectral imaging
- Automated glasshouse imaging platforms
- Near-infrared spectroscopy for grain composition without destroying the sample
- Speed breeding under extended photoperiod and early seed harvest
- Doubled-haploid production by anther culture or haploid inducer lines
- Off-season nurseries in a counter-seasonal location

### Challenges

- Prediction accuracy collapses across unrelated germplasm, because a model trained on elite material has never seen anything like a landrace and cannot extrapolate to it
- Genotype-by-environment interaction under climate variability, where the best variety in one season is not the best in the next and the training data describe a climate that is receding
- Non-additive effects, meaning dominance and epistasis, which most prediction models handle badly or not at all
- Phenotyping, not genotyping, is now the bottleneck. Reading DNA costs a few euro; measuring a thousand plots accurately costs far more and attracts far less funding
- A narrow elite germplasm base in several major crops, which molecular selection can reinforce by making it easier to select within what is already there than to bring in something new
- Data sharing between public and private breeding programmes, where the single largest available improvement, meaning larger and more diverse training populations, is blocked by commercial confidentiality rather than by any scientific difficulty
- Capacity, since the method needs a statistician and a data pipeline as much as a breeder, and national programmes often have the field sites and not the analysts

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Narrow-sense heritability | `h2` | fraction of phenotypic variance that is additive genetic | 0.1 for grain yield to 0.9 for plant height | CONSENSUS |
| Response to selection | `R` | trait units gained per cycle | crop-, trait- and programme-specific | CONSENSUS |
| Genetic gain per year | `dG/t` | per cent of the trait mean per year | 0.5 - 2.5 %/year in well-resourced programmes | REVIEWED |
| Prediction accuracy | `r_gy` | correlation between predicted and true breeding value | 0.3 - 0.7 within a training population, far lower outside it | REVIEWED |
| Selection intensity | `i` | standard deviations of the selection differential | 1.0 to 2.7, corresponding to selecting 20 % down to 1 % | CONSENSUS |
| Generation interval | `L` | years per breeding cycle | 0.2 years under speed breeding to 10 years in tree crops | CONSENSUS |
| Linkage disequilibrium decay distance | `r2_LD` | kilobases at which r-squared falls below 0.2 | 1 kb in outcrossing maize to over 100 kb in selfing wheat | CONSENSUS |
| Recurrent parent genome recovery | `RPG` | per cent of the genome matching the recurrent parent | 99 % in three backcrosses with markers, six without | CONSENSUS |

### History

- **-9000** - Domestication of wheat, barley and rice begins
- **1866** - Mendel publishes the laws of inheritance
- **1908** - Hardy and Weinberg independently describe allele frequency equilibrium
- **1918** - Fisher reconciles Mendelian inheritance with continuous variation
- **1936** - Lush formalises the breeder's equation
- **1980** - Restriction fragment length polymorphism markers introduced
- **1989** - Quantitative trait locus mapping becomes routine in crops
- **1996** - First large-scale marker-assisted selection programmes in cereals
- **2001** - Meuwissen, Hayes and Goddard propose genomic selection
- **2006** - The SUB1A submergence tolerance locus is transferred into rice mega-varieties by marker-assisted backcrossing
- **2009** - Genotyping-by-sequencing brings marker cost below the price of a field plot
- **2018** - Speed breeding protocols published for the major cereals
- **2020** - Genomic selection becomes standard practice in commercial maize, wheat and barley breeding

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | ROUTINE |
| Scale | FIELD |
| Regulatory status | UNREGULATED |
| Domains | FOOD, INFORMATION |
| SDGs | 2, 15 |

### Regulations

- UPOV Convention 1991 on the protection of new varieties of plants, and the breeder's exemption permitting a protected variety to be used as a parent
- EU Regulation (EC) No 2100/94 on Community plant variety rights
- Farmers' privilege provisions on farm-saved seed, which differ sharply between jurisdictions and are the most contested part of the regime
- EU marketing directives for cereal, vegetable and fodder seed, and the national variety catalogues they establish
- National variety registration requiring value for cultivation and use testing in several jurisdictions
- EU Regulation (EU) 2016/2031 on protective measures against plant pests, which governs movement of breeding material across borders
- Nagoya Protocol on Access and Benefit-sharing, which applies whenever breeding starts from material collected in another country and is the reason pre-breeding from landraces carries paperwork
- EU Regulation (EU) No 511/2014 implementing Nagoya user compliance
- International Treaty on Plant Genetic Resources for Food and Agriculture, whose multilateral system and standard material transfer agreement is the route most crop breeding actually uses
- GDPR, where phenotype and genotype data are linked to identifiable farmers or growers in participatory breeding programmes

### Standards

- UPOV distinctness, uniformity and stability testing, designed for morphological characters and now confronted by markers that can distinguish visually identical varieties
- UPOV guidance on essentially derived varieties, which exists to prevent a cosmetic change being used to escape another breeder's rights
- UPOV TGP/15 guidance on the use of biochemical and molecular markers in DUS examination
- ISTA International Rules for Seed Testing
- OECD seed schemes for varietal certification in international trade
- Molecular variety identification protocols for purity and identity
- FAO and Bioversity crop descriptor lists, which standardise how a trait is recorded so that two programmes can pool data
- Multi-Crop Passport Descriptors for germplasm accessions
- MIAPPE, minimum information about a plant phenotyping experiment, which is what makes a phenotype dataset reusable rather than merely archived
- FAO Genebank Standards for Plant Genetic Resources for Food and Agriculture

### Related records

- `green.animal_biotechnology`
- `green.plant_genetic_engineering`
- `green.agricultural_genome_editing`
- `green.plant_tissue_culture`
- `brown.arid_land_crops`
- `gold.machine_learning_in_biology`
- `gold.genomics_data_analysis`

### Cross-references

- [green.animal_biotechnology](animal_biotechnology.md)
- [green.plant_genetic_engineering](plant_genetic_engineering.md)
- [green.agricultural_genome_editing](agricultural_genome_editing.md)
- [green.plant_tissue_culture](plant_tissue_culture.md)
- `brown.arid_land_crops` (branch not written yet)
- `gold.machine_learning_in_biology` (branch not written yet)
- `gold.genomics_data_analysis` (branch not written yet)
