<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/yellow/food_fermentation/.
  Edit the source and run `make docs`.
-->

[Yellow Biotechnology](index.md) / **Food Fermentation**

## Food Fermentation

`yellow.food_fermentation`

Controlled microbial transformation of food and drink, the oldest biotechnology and still among the largest by volume.

### What it is

Food fermentation uses microbial metabolism to transform a raw material into something more stable, more digestible, safer or simply better. Those four functions are usually achieved together and it is worth separating them. Preservation comes from acid, alcohol and competition: organisms that drop the pH or produce ethanol exclude the ones that would spoil the food or poison the eater, which is why fermentation is a preservation technology that needs no refrigeration. Digestibility improves because microbial enzymes break down what human enzymes cannot, including lactose, phytate and some antinutritional factors. Safety improves because controlled acidification is a reliable barrier to pathogens. And flavour develops because the organisms generate hundreds of volatile compounds that no ingredient supplies directly. Two kinds of fermentation exist and the distinction runs through the whole field. Defined starter cultures are known organisms, propagated and added deliberately, which gives reproducibility and control. Spontaneous or backslopped fermentations rely on organisms already present in the raw material or carried over from the previous batch, and they are communities rather than cultures. Much of the world's fermented food is made the second way, and the resulting products frequently cannot be reproduced from a defined starter, because the succession of organisms over time is part of what makes them. The scientific contribution has been reproducibility rather than invention. Pure culture technique made starters possible, which allowed a dairy to produce the same yoghurt every day. Strain selection improved acidification rate, flavour and phage resistance. Process control replaced judgement with measurement. And molecular methods finally made it possible to see what is actually present in a community fermentation, which for most traditional foods had never been known. The constraints are unusual for this library. Bacteriophage infection is the dairy industry's chronic operational problem and can idle a plant. Starter culture supply is concentrated in a small number of companies. And there is a constraint that is cultural rather than technical: a traditional fermented food is frequently the property of a community and a place, and industrialising it raises questions about ownership, authenticity and benefit that no amount of process control answers.

### In plain language

Fermentation is letting helpful microbes change food on purpose. It is the oldest thing in this entire library: bread, cheese, yoghurt, beer, wine, soy sauce, kimchi and vinegar are all made this way, and people were doing it for thousands of years before anyone knew microbes existed. It does four useful things at once. It keeps food from spoiling, without a fridge. It makes food easier to digest. It makes food safer, because the acid the microbes produce keeps dangerous bacteria out. And it tastes good, which is not a small point: almost nothing in this list would have survived if it did not.

### An analogy

It is gardening rather than manufacturing. Nothing is built; conditions are set so that the organisms you want outcompete the ones you do not, and then you wait. The limit of the comparison is the useful part. A gardener can describe what is growing; the traditional fermenter often cannot, because a community of dozens of species arriving in succession is doing the work, and specifying it would change what grows.

### Why it matters

Fermented food is a very large fraction of what humans eat, and in much of the world it is the preservation technology that works without electricity or a cold chain. That is not a historical point: it remains how a great deal of food is kept edible today. Fermentation makes staple foods digestible that otherwise are not, breaking down lactose for people who cannot, and reducing the phytate that blocks iron and zinc absorption in cereals and legumes, which connects this record directly to the deficiencies `yellow.biofortification` addresses from the other end. It removes toxins, most strikingly in cassava processing, where fermentation reduces cyanogenic compounds that would otherwise make a staple crop dangerous. The costs are real and unevenly distributed. Bacteriophage infection can stop a dairy plant, and there is no vaccination for a starter culture. Starter supply is concentrated in a few companies, which leaves producers dependent. Industrialisation has narrowed the microbial diversity of foods that were once regionally distinct, and a defined starter is not always able to reproduce what a community fermentation produced. And traditional fermented foods belong to communities and places: taking one, characterising its organisms, and selling a defined culture back is legally permitted in most places and is not obviously fair, which is a question this record records rather than settles.

### Applications

- Lactic acid vegetable fermentation, including sauerkraut, kimchi and a great many regional pickles, which keeps a harvest edible through a season without any cold chain
- Fermented dairy products including yoghurt, kefir and cheese, where acidification and salt together make milk keep
- Fermented and cured meat products, where acidification, drying and nitrite chemistry combine, and where the safety margin is narrower than in any other group here
- Fermented fish and shrimp pastes and sauces, staples across Southeast Asia and among the oldest continuously made processed foods
- Bread and sourdough, where yeast leavens and lactic acid bacteria contribute acidity, flavour and keeping quality
- Soy fermentation into soy sauce, miso, tempeh and natto, which converts a difficult legume into several entirely different foods
- Cocoa and coffee fermentation, which is a required processing step rather than an optional one, since the flavour precursors of both are generated by microbes on the farm
- Vinegar production by acetic acid bacteria, and the fermented condiments built on it
- Cassava fermentation into gari, fufu and related products, which reduces cyanogenic compounds in a staple crop that is dangerous unprocessed, and which feeds hundreds of millions of people
- Cereal and legume fermentation reducing phytate, which improves the absorption of iron and zinc from foods that otherwise bind them
- Fermentation of grains into weaning foods such as ogi and uji, where acidification protects an infant food in the absence of refrigeration
- Brewing and winemaking, the largest fermentations in the world by volume and the ones whose organisms are best characterised
- Cheese ripening, where secondary cultures and moulds develop flavour over months by proteolysis and lipolysis
- Distilled spirits, where fermentation supplies the alcohol and the congeners that survive distillation
- Koji cultivation, in which a filamentous fungus supplies the enzymes that make sake, soy sauce and miso possible and which is a fermentation whose product is an enzyme preparation rather than a food

### Technologies

- Defined starter culture selection and propagation, which is what makes the same product possible twice
- Adjunct and secondary cultures added for flavour, texture or ripening rather than for acidification
- Backslopping, carrying a portion of a finished batch into the next, which is how most traditional fermentation is actually maintained and which propagates a community rather than a strain
- Spontaneous fermentation relying on the organisms present on the raw material, in the vessel or in the building
- Phage-resistant strain selection and starter rotation, which is the dairy industry's standing answer to its chronic operational problem
- Culture preservation by freeze drying and deep freezing, and the direct-vat inoculation formats that removed the need for a producer to propagate cultures themselves
- Culture collection maintenance and strain authentication
- Temperature, pH and salt control, which is how the competition described in `narrative.ANALOGY` is actually steered
- Controlled atmosphere and brine management for vegetable and dairy fermentations
- Endpoint determination by acidity, texture or sensory assessment rather than by time alone
- Amplicon and shotgun sequencing of fermented food communities, which for many traditional products revealed for the first time what organisms are responsible
- Metabolomics and volatile analysis linking specific organisms to specific flavour compounds
- Culture-independent monitoring of succession over the course of a fermentation, which is how a community process becomes describable without becoming a defined one
- Genomic characterisation of starter strains, including their metabolic capabilities and their phage defence systems

### Challenges

- Bacteriophage infection of dairy starter cultures, which is chronic rather than exceptional, can idle a plant, and against which the only durable answers are strain rotation and resistance breeding
- Starter culture failure and slow acidification, which in a fermented meat or dairy product is a food safety event rather than a quality one, since the acid is the safety barrier
- Mycotoxin and biogenic amine formation by unwanted organisms, particularly in spontaneous fermentations and in products aged for long periods
- Pathogen survival where acidification is too slow or too weak, which is why fermented meat and raw milk cheese carry tighter controls than their apparent simplicity suggests
- Alcohol and histamine formation in products not intended to contain them
- Loss of microbial diversity as defined starters replace community fermentations, which narrows both the products and the reservoir of strains available to improve them
- Inability to reproduce a community fermentation from a defined starter, since the succession of organisms over time is part of what makes the food
- Concentration of starter culture supply in a small number of companies, leaving producers dependent on a market they cannot influence
- Ownership of traditional fermented foods, where characterising a community's product and selling a defined culture derived from it is generally lawful and not obviously fair
- Protected designation and authenticity requirements, which restrict what may be called by a traditional name and which cut both ways for the communities they are meant to protect
- Consumer expectation of consistency, which pushes producers towards defined starters and away from the variability that characterised the products in the first place

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Final pH | `pH_f` | dimensionless | 4.0 - 4.6 for most lactic fermentations; below 4.6 is the conventional threshold for controlling Clostridium botulinum | CONSENSUS |
| Acidification rate | `dpH/dt` | pH units per hour | varies by product; a stall is a food safety event rather than a delay | CONSENSUS |
| Water activity | `a_w` | dimensionless, 0 to 1 | below 0.91 inhibits most pathogenic bacteria; dried fermented sausage reaches 0.85 - 0.90 | CONSENSUS |
| Salt concentration | `c_NaCl` | per cent in the aqueous phase | 2 - 3 % for vegetable brines, higher in fish sauce and some cured products | CONSENSUS |
| Viable starter count | `N_v` | colony forming units per gram or millilitre | 10^6 - 10^9 CFU/g depending on product and stage | CONSENSUS |
| Phage titre in whey or brine | `T_phage` | plaque forming units per millilitre | monitored continuously in dairy plants; rises sharply during an outbreak | REVIEWED |
| Degree of proteolysis | `f_prot` | per cent of total nitrogen that is soluble | rises through cheese ripening over weeks to years | CONSENSUS |
| Phytate reduction | `dPhy` | per cent of phytate degraded | substantial in cereal and legume fermentations | REVIEWED |
| Cyanogenic compound reduction | `dCN` | per cent reduction in cyanogenic glycosides | large reductions achieved in traditional cassava processing | CONSENSUS |
| Volatile compound count | `n_volatile` | distinct compounds detected | hundreds in a ripened cheese, wine or soy sauce | REVIEWED |
| Fermentation time | `t_ferm` | hours to years | 4 - 12 h for yoghurt, days for vegetables, months to years for cheese, soy sauce and cured meat | CONSENSUS |
| Batch loss rate | `R_loss` | per cent of batches failing to meet specification | low in controlled dairy production and higher in spontaneous and long-aged products | REPORTED |

### History

- **-7000** - Fermented beverages are produced in China, evidenced by residues on pottery
- **-3000** - Bread leavening, brewing and dairy fermentation are established across the ancient world
- **-300** - Soy fermentation into sauces and pastes is established in China
- **1000** - Cassava fermentation processes make a toxic staple safe across west Africa
- **1857** - Pasteur establishes that fermentation is caused by living microorganisms
- **1881** - Pure culture technique makes defined starter cultures possible
- **1890** - Commercial dairy starter cultures are introduced
- **1935** - Bacteriophage is identified as the cause of failed dairy fermentations
- **1960** - Direct-vat inoculation cultures remove the need for producers to propagate their own starters
- **1988** - Fermentation-produced chymosin is approved for cheesemaking
- **1990** - Industrial starter cultures displace regional fermentation communities
- **2010** - Sequencing reveals the microbial communities of traditional fermented foods
- **2015** - Fermented foods are investigated systematically for effects on the gut microbiome
- **2020** - Protected designation schemes and starter culture standardisation come into tension

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | UNREGULATED |
| Domains | FOOD, HEALTH |
| SDGs | 2, 3, 11, 12 |

### Regulations

- Regulation (EC) No 178/2002 general food law, establishing traceability and the obligation to withdraw unsafe food
- Regulation (EC) No 852/2004 on the hygiene of foodstuffs, which requires hazard analysis and critical control points, and under which the acidification curve in `metrics.py` is typically the critical control point itself
- Regulation (EC) No 853/2004 laying down specific hygiene rules for food of animal origin, under which dairy and meat establishments require approval and an identification mark
- Regulation (EC) No 2073/2005 on microbiological criteria, which sets the pathogen and indicator limits a fermented product must meet
- Regulation (EC) No 1333/2008 on food additives, relevant to nitrite in cured fermented meats, where the additive is part of the safety barrier rather than a cosmetic ingredient
- Regulation (EC) No 1881/2006 on contaminants, covering the mycotoxins and biogenic amines that a poorly controlled fermentation can generate
- Regulation (EU) No 1169/2011 on food information, whose allergen provisions cover milk, soy, cereals and fish across this record
- Regulation (EU) 2015/2283 on novel foods, which does not apply to foods with a significant history of consumption in the Union and does apply to a traditional product from elsewhere, which is a distinction about familiarity rather than about safety
- Regulation (EC) No 1829/2003, where a genetically modified organism is used in production, as with fermentation-produced chymosin
- Regulation (EU) No 1151/2012 on quality schemes, establishing protected designation of origin and protected geographical indication, which restrict traditional names and increasingly collide with standardised commercial cultures
- Excise, labelling and compositional rules for beer, wine and spirits, which are extensive, national and largely outside the scope of food law proper

### Standards

- Codex Alimentarius general principles of food hygiene and the HACCP system, which is the framework the hygiene regulation implements
- Codex standards for fermented milks, cheese and named fermented products, which define composition and permitted processes
- FSSC 22000, BRCGS and IFS certification schemes, which are what a retailer requires regardless of what the law requires
- Qualified presumption of safety assessment for microorganisms used in food production, which is how a starter organism is judged acceptable without a product authorisation
- Culture collection deposit and strain identification to species level, since a starter is sold as a defined organism and must be one
- Inventories of microbial species with a documented history of safe use in food, which function as the practical reference for what may be used
- Standard methods for pH, water activity and titratable acidity, which are the measurements the critical control points are expressed in
- Challenge testing and predictive microbiology protocols, which is how a producer demonstrates that a hurdle combination actually controls a pathogen rather than assuming it
- Reporting conventions for microbial community composition in fermented foods, which are still developing and which matter because most traditional products were characterised only recently
- Authenticity and traditional speciality conventions, which attempt to say what makes a named food that food, and which have no settled position on whether the organisms are part of the answer

### Related records

- `yellow.precision_fermentation`
- `white.microbial_fermentation`
- `white.industrial_enzymes`
- `yellow.food_biopreservation`
- `yellow.probiotics_and_prebiotics`
- `yellow.biofortification`

### Cross-references

- [yellow.precision_fermentation](precision_fermentation.md)
- [white.microbial_fermentation](../white/microbial_fermentation.md)
- [white.industrial_enzymes](../white/industrial_enzymes.md)
- [yellow.food_biopreservation](food_biopreservation.md)
- [yellow.probiotics_and_prebiotics](probiotics_and_prebiotics.md)
- [yellow.biofortification](biofortification.md)
