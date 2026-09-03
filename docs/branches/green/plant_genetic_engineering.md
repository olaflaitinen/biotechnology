<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/green/plant_genetic_engineering/.
  Edit the source and run `make docs`.
-->

[Green Biotechnology](index.md) / **Plant Genetic Engineering**

## Plant Genetic Engineering

`green.plant_genetic_engineering`

Introducing defined genes into crop genomes to confer traits such as insect resistance, herbicide tolerance or enhanced nutrition.

### What it is

Plant genetic engineering inserts one or more defined transgenes into a plant genome, together with the promoter and terminator sequences that control when and where they are expressed. The insert is characterised to a level no conventional breeding programme approaches: its exact sequence, its insertion site, its copy number, its inheritance across generations, and the absence of unintended open reading frames across the junctions. Two delivery routes dominate. Agrobacterium tumefaciens, a soil bacterium that naturally transfers DNA into plant cells and causes crown gall disease, is disarmed and loaded with the construct of interest; it is efficient in dicotyledons and, with modification, in cereals. Biolistic delivery coats gold or tungsten microparticles with DNA and fires them into tissue, which works in species Agrobacterium will not infect. Transformed cells are selected on a marker and regenerated into whole plants through tissue culture, which is why `green.plant_tissue_culture` is a prerequisite rather than a neighbour. A single successful insertion with acceptable characteristics is called an event, and the commercial product is that one event, backcrossed into hundreds of locally adapted varieties. The binding constraint is regulatory cost per event, not biology. Assembling a dossier runs into tens of millions of euro and takes years, which only high-acreage commodity crops repay. That single fact explains why the deployed trait set has remained essentially unchanged for three decades and why no public-sector programme has brought a transgenic crop to market at scale.

### In plain language

Every living thing carries instructions written in DNA, and the chemical alphabet is the same in a bacterium, a fish and a maize plant. That means an instruction that works in one can often be copied into another. Genetic engineering copies a specific, known instruction into a crop. One common example is an instruction from a soil bacterium for making a protein that certain caterpillars cannot digest, so the plant defends itself without being sprayed. The change is small and precisely documented: one or two known genes, in a known place. The plant is then grown and tested for years before anyone is allowed to sell it.

### An analogy

Conventional breeding is shuffling two whole decks of cards together and hoping for a good hand: tens of thousands of genes move at once and nobody records which. Genetic engineering takes one named card out of one deck and places it, face up, into the other. It is the smaller change of the two, and unlike the shuffle it is fully documented. The comparison has a real limit: a card placed into a deck still lands somewhere, and where it lands can matter, which is exactly why every commercial event has its insertion site sequenced and disclosed.

### Why it matters

Bt cotton and Bt maize cut insecticide applications substantially wherever they were adopted, which matters most for smallholders who spray by hand without protective equipment. Virus-resistant papaya saved the Hawaiian industry from a disease that had no other remedy. Golden Rice was designed for populations where vitamin A deficiency blinds and kills children. Against that, the technology concentrated seed supply into very few companies, herbicide-tolerant systems selected for resistant weeds and in some regions increased total herbicide volume, and public trust in Europe never recovered from the way the first products were introduced without any consumer benefit to offer. All of those statements are true at the same time. The most consequential fact is the least discussed: the regulatory cost of bringing one event to market excludes every crop that is not planted across millions of hectares, so cassava, sorghum, cowpea and banana, the crops eaten by the people with the least food security, have benefited least from a technology often justified by their needs.

### Applications

- Bt insect-resistant cotton, maize and aubergine
- Glyphosate- and glufosinate-tolerant soybean, maize and canola
- Stacked events combining insect resistance and herbicide tolerance
- Drought-tolerant maize events for water-limited environments
- Virus-resistant papaya, which rescued the Hawaiian crop from ringspot virus
- Virus-resistant summer squash
- Low-acrylamide potato, reducing a compound formed during frying
- Altered oil-profile soybean giving a more stable frying oil without hydrogenation
- Non-browning apple, reducing waste from cosmetic rejection
- Provitamin-A biofortified rice, approved for cultivation in 2021, twenty-one years after the prototype
- Plants as production platforms for pharmaceutical proteins
- Blue-flowered ornamentals expressing a pathway absent from the species

### Technologies

- Agrobacterium tumefaciens mediated transformation using a disarmed Ti plasmid
- Biolistic particle bombardment with DNA-coated gold or tungsten
- Floral dip transformation, which avoids tissue culture entirely in a few species
- Chloroplast transformation, which gives very high expression and maternal inheritance that limits pollen-mediated spread
- Constitutive, tissue-specific and inducible promoters
- Codon optimisation for plant expression
- Matrix attachment regions to reduce position effects
- Antibiotic and herbicide selectable markers
- Marker-free systems using co-transformation and segregation, or site-specific recombinase excision
- Visual reporters for non-destructive screening
- Regeneration through tissue culture, the step that limits which genotypes can be transformed at all
- Developmental regulators such as Baby Boom and Wuschel to make recalcitrant genotypes regenerable
- Southern blot and whole-genome sequencing for event characterisation
- Junction sequencing across the insertion site
- Event-specific detection assays for traceability and labelling compliance
- Gene stacking by conventional crossing of separately approved events

### Challenges

- Regulatory cost per event, running into tens of millions of euro, which excludes minor crops, public-sector breeders and every trait without a commodity-scale market behind it
- Evolution of Bt-resistant pest populations where refuge requirements are not enforced or not practical
- Herbicide-resistant weeds selected by the associated weed management system rather than by the transgene itself
- Recalcitrance to regeneration in elite cereal genotypes, so the varieties farmers actually want are often the hardest to transform
- Gene flow to wild relatives and to neighbouring non-GM fields, and the coexistence rules and buffer distances that follow
- Concentration of germplasm, traits and enabling patents in a handful of companies, which the regulatory cost structure actively reinforces
- Public acceptance in the European Union and several export markets, which conditions what can be planted far beyond the countries that reject it
- A first product generation offering no benefit a consumer could perceive, which made the technology easy to characterise as serving only its makers

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Transformation efficiency | `TE_plant` | per cent of explants yielding an independent event | 0.1 % in recalcitrant maize inbreds to 30 % in tobacco | REVIEWED |
| Transgene copy number | `CN` | inserted copies per haploid genome | 1 to 3; single copy strongly preferred | CONSENSUS |
| Trait protein expression level | `E_trait` | micrograms of protein per gram fresh weight | 1 - 100 ug/g, varying by tissue and growth stage | REVIEWED |
| Yield difference versus isogenic line | `dY` | per cent | 0 % under no pest pressure to 25 % or more under heavy pressure | REVIEWED |
| Insecticide applications avoided | `dA` | sprays per season | 2 - 8 fewer sprays in Bt cotton systems | REVIEWED |
| Structured refuge fraction | `R_ref` | per cent of the planted area sown to non-Bt plants | 5 - 20 % depending on crop and jurisdiction | CONSENSUS |
| Segregation ratio | `chi2` | observed against expected Mendelian ratio | 3:1 in a selfed hemizygous progeny | CONSENSUS |
| Adventitious presence threshold | `AP` | per cent of the ingredient by weight | 0.9 % labelling threshold in the European Union | CONSENSUS |

### History

- **1977** - Agrobacterium tumefaciens is shown to transfer its own DNA into plant genomes
- **1983** - First transgenic plants reported by three groups independently within months of each other
- **1987** - Bacillus thuringiensis toxin genes expressed in plants
- **1994** - Flavr Savr tomato becomes the first genetically modified food sold
- **1996** - Large-scale commercial planting of transgenic soybean and cotton begins
- **1998** - Virus-resistant papaya rescues the Hawaiian crop from ringspot virus
- **1999** - A monarch butterfly laboratory study is publicised before peer review and drives European opposition
- **2000** - Golden Rice prototype published
- **2013** - A Golden Rice field trial in the Philippines is destroyed by protesters
- **2016** - More than a hundred Nobel laureates sign an open letter supporting genetically modified crops
- **2021** - Golden Rice approved for commercial cultivation in the Philippines

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | FIELD |
| Regulatory status | VARIES |
| Domains | FOOD, ENVIRONMENT |
| SDGs | 2, 12, 15 |

### Regulations

- EU Directive 2001/18/EC on the deliberate release into the environment of genetically modified organisms, the process-based instrument that defines a GMO by the technique used to make it
- EU Directive (EU) 2015/412, which allows a Member State to prohibit cultivation of an EU-authorised event on its own territory for non-safety reasons
- EU Directive 2009/41/EC on contained use, which governs the laboratory and glasshouse stages
- EU Regulation (EC) No 1829/2003 on genetically modified food and feed
- EU Regulation (EC) No 1830/2003 on traceability and labelling, which imposes the 0.9 per cent adventitious presence threshold
- Cartagena Protocol on Biosafety to the Convention on Biological Diversity, and the advance informed agreement procedure it establishes
- Nagoya-Kuala Lumpur Supplementary Protocol on Liability and Redress
- National biosafety laws implementing the Cartagena Protocol, which is why most countries have a framework even where no event has ever been approved
- US coordinated framework, under which USDA APHIS, EPA and FDA each assess a different aspect of the same plant under pre-existing statutes
- Canadian Plants with Novel Traits regime, which regulates by product rather than by process and therefore captures some conventionally bred varieties that the EU regime does not
- Patent law over transgenic events and enabling techniques, which interacts with plant variety rights and is covered in `purple.biotechnology_patents`

### Standards

- Codex Alimentarius Guideline CAC/GL 45-2003 for the conduct of food safety assessment of foods derived from recombinant-DNA plants
- Codex Principles CAC/GL 44-2003 for the risk analysis of foods derived from modern biotechnology
- EFSA Guidance for risk assessment of food and feed from genetically modified plants
- OECD consensus documents on the biology and composition of individual crop species, which define what a conventional counterpart looks like and are therefore the baseline every comparative assessment rests on
- ISO 21569 horizontal methods for molecular biomarker analysis, qualitative nucleic acid based methods for GMO detection
- ISO 21570 quantitative nucleic acid based methods
- European Union Reference Laboratory validated event-specific detection methods, one per authorised event
- Insect Resistance Management plans imposed as conditions of authorisation, which convert the evolutionary calculation in `metrics.py` into an enforceable refuge requirement
- OECD seed schemes for varietal certification
- ISTA rules for seed testing and purity determination

### Related records

- `green.plant_tissue_culture`
- `green.agricultural_genome_editing`
- `green.molecular_plant_breeding`
- `green.biopesticides`
- `red.gene_therapy`
- `brown.drought_tolerance_engineering`
- `purple.biotechnology_patents`
- `purple.biosafety_law`

### Cross-references

- [green.plant_tissue_culture](plant_tissue_culture.md)
- [green.agricultural_genome_editing](agricultural_genome_editing.md)
- [green.molecular_plant_breeding](molecular_plant_breeding.md)
- [green.biopesticides](biopesticides.md)
- [red.gene_therapy](../red/gene_therapy.md)
- `brown.drought_tolerance_engineering` (branch not written yet)
- `purple.biotechnology_patents` (branch not written yet)
- `purple.biosafety_law` (branch not written yet)
