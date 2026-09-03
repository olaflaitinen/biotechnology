<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/green/plant_tissue_culture/.
  Edit the source and run `make docs`.
-->

[Green Biotechnology](index.md) / **Plant Tissue Culture and Micropropagation**

## Plant Tissue Culture and Micropropagation

`green.plant_tissue_culture`

Regenerating whole plants from cells, tissues or organs on sterile media to mass-produce uniform, disease-free planting material.

### What it is

Plant tissue culture exploits totipotency: most living plant cells retain the full genetic programme needed to rebuild an entire organism, which is a property animal cells lost long ago. An explant, meaning a shoot tip, a leaf disc, an anther or an immature embryo, is surface-sterilised and placed on a defined medium containing mineral salts, sucrose, vitamins and, critically, a balance of two hormone classes. The ratio does the work: a high cytokinin to auxin ratio favours shoot formation, the reverse favours roots, and an intermediate ratio produces undifferentiated callus. Skoog and Miller established that relationship in 1957, and it remains the single most useful fact in the field. Regeneration proceeds either by organogenesis, in which shoots and roots form successively from callus or directly from tissue, or by somatic embryogenesis, in which bipolar embryos form and can be encapsulated as synthetic seed. Meristem culture exploits a separate accident of plant biology: the apical dome is usually virus-free, because viral movement through the plant lags behind cell division at the growing tip, so excising a fragment under a millimetre across yields clean stock from an infected mother plant. The binding constraint is genotype-dependent recalcitrance. Regeneration protocols are developed species by species and often variety by variety, and elite commercial lines are frequently the hardest of all. That single fact limits `green.plant_genetic_engineering` and `green.agricultural_genome_editing` more than any property of the DNA delivery methods they use.

### In plain language

A cutting from a houseplant will grow roots in a glass of water. Plant tissue culture is that idea taken to its limit. With the right nutrients and the right balance of two plant hormones, a piece of tissue smaller than a grain of rice can be persuaded to grow into a complete plant, and each of those plants can be divided again. Because everything is done in sealed sterile jars, the resulting plants carry none of the diseases the parent may have had, and every one of them is genetically identical to that parent. Almost every banana eaten in the world was produced this way.

### An analogy

It is photocopying rather than reprinting. A seed is a new edition with fresh typesetting, and every one comes out slightly different. Tissue culture makes exact copies of a page you already like, and it makes them clean, without the coffee stains the original picked up. The comparison holds all the way to the failure mode: photocopy a photocopy of a photocopy for long enough and errors creep in, which is why commercial protocols cap how many times a line may be subcultured before it is started again from stock.

### Why it matters

Almost every banana eaten in the world is a clone produced this way, and the technique keeps the virus-free potato, sugarcane, strawberry, cassava and orchid industries running. For a smallholder, certified disease-free planting material can be the difference between a normal harvest and a loss of a third of the crop, and cassava and sweet potato programmes across Africa and Asia depend on it entirely. It is also the quiet prerequisite for genetic engineering and genome editing, neither of which can deliver a plant without it. The costs are specific and are usually left out. Labour dominates the economics, because a skilled operator dividing plantlets by hand is the whole production line, and that keeps micropropagation viable only for high-value or high-volume crops. Clonality means an entire industry can share one susceptibility: the Cavendish banana is genetically uniform across the planet and is losing ground to a soil fungus that no fungicide reaches. And the technique that conserves rare genotypes in a genebank is the same one that, applied commercially, replaces thousands of local varieties with one.

### Applications

- Clonal propagation of banana, which supplies almost the entire global export trade
- Micropropagation of orchids, which created the modern cut-flower and potted orchid industry
- Sugarcane and date palm multiplication from elite selections
- Somatic embryogenesis in oil palm and in conifer forestry, where seed propagation loses the selected genotype
- Virus elimination from potato seed systems by meristem culture, often combined with thermotherapy
- Cassava and sweet potato clean-seed programmes, which underpin food security across large parts of Africa and Asia
- Certified virus-free strawberry and citrus foundation stock
- Embryo rescue in wide crosses, where the hybrid embryo forms but the endosperm fails and the seed would abort
- Ovule and anther culture where fertilisation succeeds but development does not
- Anther and microspore culture for doubled-haploid production, reaching complete homozygosity in one step
- In vitro germplasm banks under slow-growth conditions
- Cryopreservation of shoot tips for crops whose seed cannot be dried and frozen, including banana, potato and cassava
- Regeneration of transformed and edited cells into whole plants, without which no transgenic or genome-edited crop could exist
- Protoplast culture and regeneration, the route used for DNA-free editing
- Cell suspension culture for secondary metabolite production, including paclitaxel and shikonin

### Technologies

- Murashige and Skoog basal medium and its derivatives, still the default formulation more than sixty years after publication
- Auxin to cytokinin ratio control, the lever that decides shoot, root or callus
- Gelling agents and liquid systems, which change oxygen availability and therefore morphology
- Activated charcoal and antioxidants to absorb phenolics released by wounded tissue
- Surface sterilisation with hypochlorite or mercuric chloride, followed by rinsing
- Laminar flow sterile technique and contamination indexing
- Meristem excision under a stereomicroscope, taking domes under one millimetre
- Thermotherapy and chemotherapy before excision to push the virus front further back
- Indexing by ELISA and PCR to confirm the material really is virus-free
- Direct and indirect organogenesis
- Somatic embryogenesis and synthetic seed encapsulation in calcium alginate
- Developmental regulators such as Baby Boom and Wuschel to make recalcitrant genotypes regenerable
- Temporary immersion bioreactors, which cut labour and improve gas exchange
- Photoautotrophic culture, growing plantlets on carbon dioxide rather than sucrose so they are less prone to contamination and acclimatise better
- Slow-growth storage under reduced temperature and osmotic stress
- Cryopreservation by vitrification, droplet freezing and encapsulation dehydration
- Acclimatisation and hardening protocols before transfer to soil

### Challenges

- Genotype-dependent recalcitrance, where protocols must be developed variety by variety and elite commercial lines are often the hardest, which limits genetic engineering and genome editing more than any DNA delivery problem does
- Somaclonal variation accumulating during extended callus phases, including epigenetic changes such as the mantled-fruit abnormality that cost the oil palm industry years of production
- Endophytic bacterial contamination that is invisible for months and then appears simultaneously across a whole production batch
- Hyperhydricity, where plantlets become glassy and water-soaked in high humidity and fail to survive transfer
- Acclimatisation, where plantlets grown in saturated humidity with no functional cuticle meet real air, and losses of a fifth or more are ordinary
- Labour cost, which dominates the economics because dividing plantlets by hand is the production line, and which confines the technique to high-value or high-volume crops
- Cryopreservation protocols that must be developed species by species, so the crops most dependent on clonal conservation are often those with the least reliable way to store it

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Multiplication rate | `M` | shoots per explant per subculture cycle | 3 - 10 per cycle of four to six weeks | CONSENSUS |
| Maximum subculture number | `n_sub` | successive subcultures before restarting from stock | 8 - 12 in commercial protocols | REVIEWED |
| Regeneration frequency | `RF` | per cent of explants producing a shoot or embryo | 10 - 90 %, and below 1 % from protoplasts in most crops | REVIEWED |
| Auxin to cytokinin ratio | `A:C` | dimensionless ratio of molar concentrations | high for roots, low for shoots, intermediate for callus | CONSENSUS |
| Contamination rate | `C_rate` | per cent of cultures lost | below 5 % in a well-run laboratory | CONSENSUS |
| Acclimatisation survival | `S_acc` | per cent surviving transfer from jar to soil | 70 - 98 % | REVIEWED |
| Virus elimination efficiency | `VE_mer` | per cent of regenerants testing virus-free | 40 - 95 %, depending on virus and on excised dome size | REVIEWED |
| Genetic fidelity | `F_gen` | per cent of regenerants matching the mother plant by marker | above 95 % expected in a validated protocol | REVIEWED |
| Cryopreservation recovery | `R_cryo` | per cent of shoot tips regrowing after liquid nitrogen | 40 - 80 % where a protocol exists at all | REVIEWED |

### History

- **1902** - Haberlandt proposes that any living plant cell can regenerate a whole organism
- **1934** - Auxin identified as a plant growth substance
- **1939** - First indefinitely growing plant callus cultures established
- **1957** - Skoog and Miller describe hormonal control of organogenesis
- **1958** - Somatic embryogenesis demonstrated in carrot cell suspensions
- **1960** - Morel demonstrates meristem culture for virus elimination and clonal orchid propagation
- **1962** - Murashige and Skoog publish their medium formulation
- **1974** - Commercial orchid and ornamental micropropagation industry forms
- **1983** - Tissue culture regeneration becomes the enabling step for the first transgenic plants
- **1985** - Cryopreservation of plant meristems demonstrated
- **1986** - Oil palm clones planted at scale develop the mantled-fruit abnormality
- **2000** - Temporary immersion bioreactors reach commercial banana production
- **2016** - Developmental regulators are shown to make recalcitrant maize genotypes regenerable

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | ROUTINE |
| Scale | INDUSTRIAL |
| Regulatory status | NOTIFIED |
| Domains | FOOD, ENVIRONMENT |
| SDGs | 2, 15 |

### Regulations

- EU Regulation (EU) 2016/2031 on protective measures against pests of plants, under which plants for planting are the highest-risk category precisely because propagation multiplies any infection
- EU Regulation (EU) 2017/625 on official controls, governing inspection at the point of entry
- International Plant Protection Convention and the phytosanitary certificate regime, which is why material cannot simply be posted between countries
- National quarantine requirements for imported in vitro material, which in several countries mandate post-entry growing-on under observation
- Nagoya Protocol on Access and Benefit-sharing, engaged whenever a landrace or wild relative collected elsewhere is propagated
- EU Regulation (EU) No 511/2014 implementing Nagoya user compliance
- International Treaty on Plant Genetic Resources for Food and Agriculture, and its standard material transfer agreement, which is the route most crop germplasm actually moves by
- EU marketing directives for propagating material of fruit, vegetable and ornamental plants
- National seed and planting material certification schemes, which set the pathogen indexing a batch must pass
- EU Directive 2009/41/EC on contained use, which applies to the culture step only where the material being regenerated is genetically modified

### Standards

- EPPO certification schemes for pathogen-tested planting material, which define the indexing a nuclear stock plant must pass
- EPPO diagnostic protocols for regulated pests, PM 7 series
- National virus-tested stock schemes, such as those operated for potato, fruit and strawberry
- FAO Genebank Standards for Plant Genetic Resources for Food and Agriculture, including the in vitro and cryopreservation sections
- Bioversity International and CGIAR technical guidelines for in vitro conservation and cryopreservation
- Multi-Crop Passport Descriptors for germplasm accessions
- FAO and Bioversity crop descriptor lists
- ISO 9001 quality management, commonly held by commercial micropropagation laboratories
- Good practice guidance on aseptic technique and contamination indexing from national horticultural research bodies
- Molecular marker and methylation-based genetic fidelity testing protocols, adopted after the oil palm mantled-fruit episode showed that a sequence-identical clone can still be defective

### Related records

- `green.plant_genetic_engineering`
- `green.agricultural_genome_editing`
- `green.molecular_plant_breeding`
- `brown.arid_land_crops`
- `red.regenerative_medicine`
- `grey.biodiversity_conservation`
- `purple.access_benefit_sharing`

### Cross-references

- [green.plant_genetic_engineering](plant_genetic_engineering.md)
- [green.agricultural_genome_editing](agricultural_genome_editing.md)
- [green.molecular_plant_breeding](molecular_plant_breeding.md)
- `brown.arid_land_crops` (branch not written yet)
- [red.regenerative_medicine](../red/regenerative_medicine.md)
- [grey.biodiversity_conservation](../grey/biodiversity_conservation.md)
- `purple.access_benefit_sharing` (branch not written yet)
