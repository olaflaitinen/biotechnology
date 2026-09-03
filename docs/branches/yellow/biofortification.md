<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/yellow/biofortification/.
  Edit the source and run `make docs`.
-->

[Yellow Biotechnology](index.md) / **Biofortification**

## Biofortification

`yellow.biofortification`

Raising the micronutrient content of staple crops by breeding or engineering, so the nutrient travels with the seed rather than through a supply chain.

### What it is

Biofortification raises the micronutrient content of staple food crops through the crop itself. The problem it addresses is micronutrient deficiency, sometimes called hidden hunger, in which a diet supplies sufficient energy and insufficient iron, zinc, vitamin A or other micronutrients. It is a consequence of dietary monotony rather than of food shortage, it affects billions of people, and its effects on cognitive development, immune function, maternal mortality and vision are permanent where they occur in childhood. The distinguishing feature is the delivery mechanism rather than the nutrition. Supplementation and industrial fortification both work and both are cost-effective, and both require a person to reach a clinic or to buy centrally processed food. The populations with the highest deficiency rates are frequently subsistence farmers who consume what they grow, and for them a nutrient bred into the seed arrives with the harvest and requires no continuing programme, no purchase and no behaviour change. That is a delivery argument, and it is the whole argument. Two routes exist and their records differ sharply. Conventional breeding and marker-assisted selection exploit existing variation, and where the variation is sufficient this route has delivered varieties at scale: iron-biofortified beans and pearl millet, zinc-biofortified wheat and rice, and provitamin A orange-fleshed sweet potato, maize and cassava are in farmers' fields across many countries. Genetic engineering is required where the pathway does not exist in the crop at all, which is the case for provitamin A in rice endosperm, and that route has produced far more scientific attention and far less deployed food. The constraints are agronomic, nutritional and political in roughly equal measure. A biofortified variety must yield as well as the one it replaces, because a farmer will not accept less harvest for a nutrient they cannot see. The nutrient must survive processing and cooking, and must be absorbed, which for iron and zinc is limited by the phytate in the same cereals. Consumer acceptance matters where the trait is visible, as it is for orange maize in populations accustomed to white. And where the route is genetic engineering, the regulatory and political position has been decisive rather than incidental, as the history of provitamin A rice demonstrates.

### In plain language

Billions of people eat enough food and still do not get enough iron, zinc or vitamin A, because their diet is built around one staple crop that supplies energy and little else. The results are permanent: children go blind, do not develop properly, and are more likely to die of ordinary infections. Vitamin pills and added nutrients in flour both work, and both need the person to buy something or visit a clinic. Many of the people most affected grow their own food and do neither. Biofortification puts the nutrient in the seed instead, so it arrives with the harvest, every year, without anyone having to do anything differently.

### An analogy

It is adding fluoride to a water supply rather than handing out tablets. The tablets work, and they require somebody to collect them and remember to take them, every day, indefinitely. Treating the supply reaches everyone who drinks the water without asking anything of them. The comparison also carries the limitation honestly: it reaches only the people connected to that supply, and a household growing a different crop is a household on a different pipe.

### Why it matters

Micronutrient deficiency affects billions of people, and its consequences in childhood are irreversible. Vitamin A deficiency remains a leading cause of preventable childhood blindness and increases mortality from ordinary infections. Iron deficiency anaemia impairs cognitive development and contributes to maternal death. Zinc deficiency increases the severity of diarrhoeal disease, which kills large numbers of small children. Biofortified varieties are in farmers' fields in many countries, and orange-fleshed sweet potato in particular has been distributed at considerable scale with measured effects on vitamin A status. The costs and limitations deserve stating with equal precision. Biofortification reaches people who grow and eat the staple, which is a real population and not everyone. Yield parity is a hard requirement rather than a preference, since a farmer will not trade harvest for an invisible nutrient. Bioavailability limits what a content figure means, because the phytate in cereals binds the iron and zinc being added. Visible traits meet consumer resistance, and orange maize in a population accustomed to white maize is a marketing problem before it is a nutritional one. And where the nutrient requires genetic engineering, the twenty-year regulatory and political history of provitamin A rice is a caution about assuming that a demonstrated benefit produces deployment.

### Applications

- Orange-fleshed sweet potato, conventionally bred, distributed at scale across sub-Saharan Africa with measured improvements in vitamin A status, which is the field's clearest delivered success
- Provitamin A maize, conventionally bred, released in several countries and facing consumer preference for white maize in populations accustomed to it
- Provitamin A cassava, bred for a crop that is a staple for hundreds of millions and is otherwise almost purely starch
- Provitamin A rice, which requires genetic engineering because the pathway is absent from the endosperm entirely, and whose deployment history is recorded in `history.py` as a caution rather than a success
- Iron-biofortified beans, released widely in east and central Africa and in Latin America, where beans are a staple and the baseline iron content is already relatively high
- Iron-biofortified pearl millet, released in India, in a crop grown in areas with high deficiency prevalence and poor access to fortified foods
- Iron-biofortified wheat and rice varieties, where the gain is constrained by the low baseline and by phytate in the same grain
- Zinc-biofortified wheat, released in south Asia where wheat is the staple and zinc deficiency is widespread
- Zinc-biofortified rice and maize varieties
- Zinc-biofortified beans and lentils, which combine a reasonable baseline with a crop people already eat daily
- Low-phytate varieties, which raise the availability of the iron and zinc already present rather than adding more, and which trade against seed viability because phytate is the seed's phosphorus store
- Varieties bred for promoter compounds that enhance absorption, which is the less explored complement to reducing inhibitors
- Folate-biofortified rice and other staples, addressing neural tube defects
- Provitamin A and folate banana varieties for regions where banana is a staple rather than a fruit
- Amino acid composition improvement in maize and cassava, addressing protein quality rather than micronutrients

### Technologies

- Germplasm screening across genebank collections for existing variation in micronutrient content, which is where every conventional programme starts and which depends entirely on collections assembled decades earlier
- Marker-assisted selection for micronutrient traits, which allows selection on a seedling rather than on a harvested and analysed grain
- Genomic selection for traits controlled by many small-effect loci, drawing directly on `green.molecular_plant_breeding`
- Crossing biofortified traits into locally adapted and preferred varieties, which is the unglamorous majority of the work and the part that determines whether farmers plant it
- Transgenic introduction of a complete biosynthetic pathway, required where the crop cannot make the nutrient at all, as for provitamin A in rice endosperm
- Metabolic engineering of nutrient uptake, translocation and storage in the edible tissue rather than in the leaves
- Genome editing of transporters and of phytate biosynthesis, which in some jurisdictions avoids the regulatory position that has constrained the transgenic route
- High-throughput micronutrient analysis, including X-ray fluorescence screening that measures grain without destroying or dissolving it, which is what made screening thousands of lines practical
- Bioavailability assessment by in vitro digestion, cell models and stable isotope studies in people, since content and absorbed dose are different quantities
- Retention testing through the actual local processing and cooking, because a carotenoid that does not survive the pot has not been delivered
- Participatory variety selection, in which farmers choose among candidates, which is how yield parity and preference are established rather than assumed
- Seed system development, including community multiplication and vine distribution for vegetatively propagated crops such as sweet potato
- Demand creation and nutrition education, which for a visible trait such as orange maize is the difference between adoption and rejection
- Efficacy and effectiveness trials measuring nutritional status in the target population, which is the only evidence that the delivery argument actually holds

### Challenges

- Yield parity, which is a hard requirement rather than a preference, since a farmer will not accept a smaller harvest in exchange for a nutrient they cannot see and whose benefit is invisible and delayed
- Adaptation to local conditions, because a biofortified trait in an unadapted variety is worthless and crossing it into locally preferred varieties is most of the work
- Seed system access, since a variety that exists in a research station and not in a farmer's hands has delivered nothing
- Bioavailability, since phytate in cereals binds iron and zinc and limits how much of an increased content is actually absorbed, which is why low-phytate breeding is a complement rather than an alternative
- Retention through local processing and cooking, particularly for carotenoids, which degrade with heat, light and storage
- The trade between low phytate and seed viability, since phytate is the seed's phosphorus store and removing it can impair germination and seedling vigour
- Consumer acceptance of visible traits, where orange maize in a population accustomed to white maize is a preference problem before it is a nutritional one, and where the visibility that aids adoption messaging also invites rejection
- Sustained consumption, since the benefit depends on the biofortified variety remaining a substantial part of the diet year after year rather than being tried once
- Demonstrating an effect on nutritional status rather than on grain content, which requires efficacy trials in the target population and is far more expensive and slower than the breeding
- Regulatory and political treatment of the transgenic route, which has been decisive rather than incidental and which the provitamin A rice history documents over more than two decades
- Dependence on donor funding for crops and populations that no commercial seed market serves, which makes the field's continuation a policy decision rather than a market outcome
- Genebank dependence, since conventional breeding requires variation that was collected and conserved decades ago by institutions now underfunded

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Yield penalty relative to the check variety | `dY` | per cent difference in grain or root yield | parity is the requirement; any measurable penalty is a barrier to adoption | CONSENSUS |
| Adoption rate | `f_adopt` | per cent of target farmers planting the biofortified variety | varies enormously with seed system access and with whether the trait is visible | REPORTED |
| Micronutrient concentration | `c_nutrient` | micrograms per gram of dry weight | breeding targets are set as an increment above the baseline variety rather than as an absolute figure | CONSENSUS |
| Breeding target increment | `dC_target` | micrograms per gram above the baseline, set per crop and per population | derived by working backwards from a required change in nutritional status | REVIEWED |
| Retention through processing and cooking | `R_ret` | per cent of the nutrient remaining after local preparation | substantial losses for carotenoids; minerals are not destroyed but can be lost with discarded fractions | CONSENSUS |
| Bioavailability | `B_avail` | per cent of the ingested nutrient absorbed | low for iron and zinc from cereal diets, and higher for provitamin A from processed orange-fleshed roots | REVIEWED |
| Phytate to mineral molar ratio | `PA_Zn` | molar ratio, dimensionless | ratios above roughly 15 for phytate to zinc indicate poor absorption | CONSENSUS |
| Contribution to estimated average requirement | `f_EAR` | per cent of the daily requirement supplied by usual consumption | the figure biofortification programmes actually target | REVIEWED |
| Change in biomarker of nutritional status | `dStatus` | change in serum retinol, ferritin, zinc or haemoglobin | the endpoint of an efficacy trial, and the only evidence the chain held end to end | REVIEWED |
| Deficiency prevalence in the target population | `P_def` | per cent of the population below the deficiency threshold | the figure that justifies a programme and defines its target population | REVIEWED |
| Cost per disability-adjusted life year averted | `C_DALY` | euro per DALY averted | favourable for established biofortified crops, and compared against supplementation and industrial fortification rather than against nothing | REPORTED |
| Time from programme start to released variety | `t_release` | years | commonly a decade or more for conventional breeding, and considerably longer where a regulatory approval is required | REVIEWED |

### History

- **1990** - Micronutrient deficiency is recognised as a distinct global health problem separate from calorie deficiency
- **1993** - Vitamin A supplementation is shown to reduce child mortality substantially
- **1999** - Provitamin A biosynthesis is engineered into rice endosperm
- **2003** - A coordinated international biofortification programme is established
- **2005** - A second-generation construct raises provitamin A content by a large factor
- **2007** - Orange-fleshed sweet potato is released and distributed at scale in sub-Saharan Africa
- **2012** - Iron-biofortified beans and pearl millet are released in Africa and India
- **2014** - Efficacy trials show measurable improvement in nutritional status from biofortified crops
- **2016** - Zinc-biofortified wheat is released in south Asia
- **2018** - Provitamin A rice receives food safety approvals in several countries that do not grow it
- **2020** - Genome editing is applied to micronutrient traits, and falls under different regulatory treatment in several jurisdictions
- **2021** - The Philippines approves provitamin A rice for commercial propagation
- **2022** - Biofortified varieties are reported to have reached tens of millions of farming households
- **2024** - An appellate court in the Philippines revokes the biosafety permits for provitamin A rice

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | REGULATED |
| Scale | POPULATION |
| Regulatory status | VARIES |
| Domains | HEALTH, FOOD |
| SDGs | 1, 2, 3, 5 |

### Regulations

- National variety release and registration systems, requiring distinctness, uniformity and stability testing and value for cultivation and use trials, which is the only approval a conventionally bred biofortified variety needs
- Seed certification and quality control legislation, which governs whether the seed a farmer receives is what it claims to be and is frequently the practical bottleneck in the delivery systems this record depends on
- Plant variety protection under UPOV and national equivalents, and the farmers' rights provisions that determine whether saved seed may be replanted, which matters for crops distributed to subsistence growers
- The Cartagena Protocol on Biosafety and national biosafety frameworks implementing it, which govern the transboundary movement and release of living modified organisms
- National biosafety authorisation for cultivation, and separate food and feed approvals, which in the central case of this record were obtained in different countries years apart
- Regulation (EC) No 1829/2003 and Regulation (EC) No 1830/2003 on authorisation, traceability and labelling, applicable to import into the European Union
- National judicial review of biosafety permits, which in 2024 revoked a cultivation approval that had been granted in 2021
- Divergent national treatment of genome-edited crops, regulated as conventional breeding in several jurisdictions and as transgenesis in others, which is the same unresolved divergence `green.agricultural_genome_editing` records
- Regulation (EC) No 1924/2006 on nutrition and health claims, and national equivalents, which govern whether a biofortified crop may be marketed on its nutritional content
- Codex Alimentarius nutrient reference values, which define the requirements the breeding targets are calculated against
- The International Treaty on Plant Genetic Resources for Food and Agriculture, whose multilateral system governs access to the genebank collections that every conventional programme depends on
- The Convention on Biological Diversity and the Nagoya Protocol, for material outside the treaty's multilateral system

### Standards

- Breeding target-setting conventions derived from deficiency prevalence, consumption data, retention and bioavailability, which is the backwards calculation that distinguishes this field from raising a content figure for its own sake
- Standardised micronutrient analysis protocols, including calibrated X-ray fluorescence screening against reference wet chemistry, which is what made screening thousands of breeding lines practical
- Retention testing through documented local preparation methods rather than through a standard laboratory procedure
- Bioavailability assessment conventions, from in vitro digestion through to stable isotope studies in the target population
- Efficacy and effectiveness trial design standards for nutritional outcomes, and CONSORT reporting, since the last link in the chain is the only one that matters and is measured least often
- Biomarker measurement and interpretation conventions, including adjustment for inflammation, which otherwise distorts ferritin and retinol readings in exactly the populations being studied
- Participatory variety selection protocols, which is how yield parity and farmer preference are established rather than assumed
- Community seed and vine multiplication practice, which is what delivered orange-fleshed sweet potato and which no formal seed system replaced
- Quality declared seed standards, an intermediate between certified seed and no standard at all, designed for exactly the systems this record operates in
- Genebank management and characterisation standards, since conventional biofortification requires variation collected and conserved decades ago by institutions that are now underfunded

### Related records

- `yellow.food_fermentation`
- `green.molecular_plant_breeding`
- `green.agricultural_genome_editing`
- `green.plant_genetic_engineering`
- `yellow.nutrigenomics`
- `purple.access_benefit_sharing`

### Cross-references

- [yellow.food_fermentation](food_fermentation.md)
- [green.molecular_plant_breeding](../green/molecular_plant_breeding.md)
- [green.agricultural_genome_editing](../green/agricultural_genome_editing.md)
- [green.plant_genetic_engineering](../green/plant_genetic_engineering.md)
- [yellow.nutrigenomics](nutrigenomics.md)
- `purple.access_benefit_sharing` (branch not written yet)
