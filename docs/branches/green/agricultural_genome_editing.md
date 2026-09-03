<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/green/agricultural_genome_editing/.
  Edit the source and run `make docs`.
-->

[Green Biotechnology](index.md) / **Agricultural Genome Editing**

## Agricultural Genome Editing

`green.agricultural_genome_editing`

Making targeted, often transgene-free edits in crop and livestock genomes rather than inserting foreign genes.

### What it is

Genome editing introduces a double-strand break, a single-strand nick or a direct chemical conversion at a chosen genomic position, and lets the cell's own repair machinery produce the change. The tool supplies the address; the cell supplies the edit. Three classes are distinguished in the policy literature and increasingly in law. A site-directed nuclease type 1 edit is a small insertion or deletion produced by error-prone non-homologous end joining, typically knocking a gene out. Type 2 uses a short repair template to make a precise substitution, often copying an allele that already exists elsewhere in the species and could in principle have been introduced by crossing. Type 3 inserts a whole cassette and is, biologically and legally, transgenesis. Almost every regulatory dispute in this field is an argument about where to draw the line between type 1, type 2 and type 3. Delivery to plants may use Agrobacterium, in which case the editing machinery is present in the genome and is segregated away in later generations, leaving an edited plant carrying no foreign DNA. Or it may use preassembled ribonucleoprotein complexes delivered directly into protoplasts, which leaves no foreign DNA at any stage. Base editors convert one base pair into another without a double-strand break; prime editors write short defined sequences from an attached template. In livestock, editing is applied in zygotes. The binding constraint is regeneration and regulation rather than editing. Cutting the genome is now reliable; recovering a whole plant from the edited cell is not, and knowing which of thirty jurisdictions will treat the result as conventional is not either.

### In plain language

All plants and animals accumulate small random changes in their DNA over generations, and that is where the variety in every crop originally came from. Plant breeders have deliberately increased that randomness for a century, using chemicals and radiation to scramble genes and then selecting whichever results turned out useful. Genome editing does the same kind of thing, but aimed. It makes one small change at one chosen place, usually switching off a gene that was causing a problem. In most cases nothing from another species remains in the finished plant, and nothing distinguishes it from a change that could have happened on its own.

### An analogy

Older breeding methods were a spelling change made by shaking the whole book until a letter fell out somewhere, then reading the result to see whether it had improved. Genome editing is using find-and-replace on one word you have already identified. The finished book reads the same either way; the difference is how many other pages were disturbed on the way. The comparison has an honest limit: find-and-replace can also match somewhere you did not intend, which is why edited lines are sequenced to look for changes at similar-looking sites elsewhere in the genome.

### Why it matters

Editing collapses the cost and the timeline of crop improvement. A trait that took a decade of backcrossing can be produced in two generations, and because no foreign gene is present the product may escape the regulatory burden that made conventional genetic modification viable only for four global commodity crops. That opens improvement to minor crops, to public-sector breeders and to national programmes, which is the single most consequential difference between this record and `green.plant_genetic_engineering`. The costs are equally specific. The regulatory divergence fragments trade: a shipment that is conventional grain in one port is an unauthorised genetically modified organism in the next. Because a type 1 edit leaves no unique sequence to detect, enforcement of that divergence may be impossible in practice, which is an uncomfortable position for every side of the argument. And the tools themselves are covered by a patent thicket dense enough that the freedom to operate, rather than the biology, decides what a small breeder can attempt.

### Applications

- Non-browning mushrooms, produced by knocking out a polyphenol oxidase gene, and the first edited organism cleared without regulation in the United States
- Powdery-mildew resistant wheat, by knocking out all six copies of the MLO susceptibility gene
- Bacterial-blight resistant rice, by editing the promoters the pathogen hijacks rather than the genes themselves
- Reduced-gluten wheat lines for people who cannot tolerate conventional wheat
- Low-acrylamide and bruise-resistant potato
- Waxy maize with an altered starch profile
- Herbicide-tolerant oilseed rape carrying a substitution found in natural populations
- High-oleic soybean produced by precise base changes in fatty acid desaturase genes
- High-GABA tomato, the first edited food sold in Japan, produced by truncating an autoinhibitory domain
- Hornless dairy cattle carrying the POLLED allele, avoiding painful disbudding
- Pigs resistant to porcine reproductive and respiratory syndrome virus, by editing the CD163 receptor the virus requires
- Heat-tolerant cattle carrying a slick-coat allele from tropical breeds
- Haploid inducer lines that carry editing machinery and deliver it during crossing, leaving an edited but machinery-free progeny

### Technologies

- CRISPR-Cas9, the workhorse nuclease
- CRISPR-Cas12a, which recognises a different sequence motif and so reaches targets Cas9 cannot
- Multiplexed guide RNA arrays, essential in polyploid crops where the same gene exists in three or six copies that must all be hit
- Guide RNA design software scoring on-target activity and predicted off-target sites
- Cytosine and adenine base editors, which convert one base pair chemically and make no double-strand break
- Prime editors, which write a short defined sequence from an attached template
- Agrobacterium delivery followed by segregation of the transgene in later generations
- Ribonucleoprotein delivery into protoplasts, which introduces no DNA at any point
- Biolistic delivery of ribonucleoprotein into immature embryos
- Haploid induction mediated editing, which delivers the machinery through a cross
- Zygote electroporation and microinjection in livestock
- Protoplast regeneration, which is the limiting step in most species
- Developmental regulators that make recalcitrant genotypes regenerable
- Amplicon sequencing of the target site to quantify editing outcomes
- Whole-genome sequencing for off-target and structural change assessment
- PCR screening to confirm absence of the editing construct

### Challenges

- The regeneration bottleneck, since an edited cell is worthless until it becomes a plant, and elite genotypes are frequently the hardest to regenerate
- Editing efficiency in polyploid crops such as bread wheat, where the same gene exists in three genomes and every copy must be hit before the phenotype appears
- Regulatory divergence that fragments international trade, so the same grain is conventional in one port and unauthorised in the next
- Detection and traceability where no foreign DNA remains, which makes enforcement of that divergence arguably impossible and leaves every side of the argument uncomfortable
- Patent thickets over the editing tools themselves, so freedom to operate rather than biology decides what a small breeder may attempt
- Public consultation processes that have run years behind deployment, so products reached markets before the conversation about them had happened
- An evidence base still dominated by the first decade of the technology, with little long-term field data on edited lines under commercial cultivation

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Editing efficiency | `indel%` | per cent of alleles carrying the intended edit | 5 - 90 %, falling sharply in polyploid species | REVIEWED |
| Off-target editing rate | `OT` | detectable unintended edits per genome | 0 - 5 sites in a screened line | REVIEWED |
| Guide RNA on-target score | `S_guide` | dimensionless, scaled 0 to 1 | design threshold around 0.6 | REPORTED |
| Homology-directed repair fraction | `HDR%` | per cent of edits using the supplied template | 0.1 - 10 % in plant cells | REVIEWED |
| Transgene-free recovery rate | `TFR` | per cent of edited lines free of editing machinery | 10 - 50 % after one or two generations of segregation | REVIEWED |
| Generations to a clean edited line | `G_clean` | generations | 1 - 3, against 6 or more for introgression by backcrossing | CONSENSUS |
| Protoplast regeneration efficiency | `RE` | per cent of protoplasts yielding a plantlet | below 1 % in most crop species | REVIEWED |
| Segregation ratio | `chi2` | observed against expected Mendelian ratio | 3:1 in a selfed heterozygous progeny | CONSENSUS |

### History

- **1996** - Zinc finger nucleases demonstrated as programmable DNA cutters
- **2011** - TALEN editing applied to rice bacterial blight resistance
- **2012** - CRISPR-Cas9 described as a programmable RNA-guided DNA endonuclease
- **2013** - CRISPR editing demonstrated in rice, wheat and Arabidopsis
- **2015** - Argentina issues Resolution 173/2015, the first framework written specifically for new breeding techniques
- **2016** - A non-browning mushroom is cleared without regulation in the United States
- **2016** - PRRS-resistant pigs produced by editing the CD163 receptor
- **2018** - The Court of Justice of the European Union rules that organisms from directed mutagenesis fall under the GMO Directive
- **2019** - Japan establishes a notification pathway for edits leaving no foreign DNA
- **2021** - High-GABA tomato goes on sale in Japan
- **2022** - England legislates for precision breeding, separating edited organisms from the retained GMO regime
- **2023** - The European Commission proposes a separate category for plants obtained by new genomic techniques

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | CONTROLLED |
| Scale | FIELD |
| Regulatory status | VARIES |
| Domains | FOOD, ENVIRONMENT |
| SDGs | 2, 13, 15 |

### Regulations

- EU Directive 2001/18/EC on the deliberate release of genetically modified organisms, written in 2001 and therefore before this technology existed
- Court of Justice of the EU Case C-528/16, judgment of 25 July 2018, which held that organisms obtained by directed mutagenesis fall within the Directive because the mutagenesis exemption covers only techniques with a long safety record of use
- EU proposal of July 2023 on plants obtained by certain new genomic techniques, which would create a separate category for edits achievable by conventional breeding
- New Zealand Hazardous Substances and New Organisms Act, applied on a similarly process-based reading
- Canadian Plants with Novel Traits regime, which assesses the trait rather than the technique and so captures some conventionally bred varieties the EU regime does not
- Argentina Resolution 173/2015, the first framework written for these techniques, asking case by case whether a novel combination of genetic material is present
- Brazil CTNBio Normative Resolution 16/2018, following a comparable case-by-case approach
- Japan notification pathway under the Cartagena Act, requiring notification but no premarket approval where no foreign DNA remains
- US SECURE rule, 7 CFR Part 340, exempting modifications that could have been achieved by conventional breeding
- England Genetic Technology (Precision Breeding) Act 2023, separating precision-bred organisms from the retained GMO regime
- Cartagena Protocol on Biosafety, which governs transboundary movement and under which parties reach different conclusions about whether an edited organism is a living modified organism at all
- EU Regulation (EU) 2016/2031 on plant health, and national variety registration and seed marketing law, which apply to any new variety however it was bred

### Standards

- ISO 21569 and ISO 21570 GMO detection methods, which rely on a unique inserted sequence and therefore cannot identify a type 1 edit that leaves no such sequence behind
- European Network of GMO Laboratories reports on the detectability of products of new genomic techniques, which conclude that an edit indistinguishable from a natural mutation cannot be identified as edited without prior knowledge of the event
- OECD consensus documents on new plant breeding techniques
- OECD consensus documents on the biology of individual crop species, which define the conventional counterpart every comparative assessment needs
- Codex Alimentarius principles for the risk analysis of foods derived from modern biotechnology
- EFSA opinions on the applicability of existing guidance to plants obtained by targeted mutagenesis and cisgenesis
- Whole-genome sequencing based off-target assessment protocols
- Amplicon sequencing conventions for reporting editing outcomes
- UPOV distinctness, uniformity and stability testing, which applies to an edited variety exactly as to any other
- ISTA rules for seed testing

### Related records

- `green.plant_genetic_engineering`
- `green.molecular_plant_breeding`
- `green.plant_tissue_culture`
- `green.animal_biotechnology`
- `red.gene_therapy`
- `brown.drought_tolerance_engineering`
- `purple.biosafety_law`
- `purple.biotechnology_patents`

### Cross-references

- [green.plant_genetic_engineering](plant_genetic_engineering.md)
- [green.molecular_plant_breeding](molecular_plant_breeding.md)
- [green.plant_tissue_culture](plant_tissue_culture.md)
- [green.animal_biotechnology](animal_biotechnology.md)
- [red.gene_therapy](../red/gene_therapy.md)
- `brown.drought_tolerance_engineering` (branch not written yet)
- `purple.biosafety_law` (branch not written yet)
- `purple.biotechnology_patents` (branch not written yet)
