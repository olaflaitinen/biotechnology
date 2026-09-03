<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/blue/marine_enzymes/.
  Edit the source and run `make docs`.
-->

[Blue Biotechnology](index.md) / **Marine Enzymes**

## Marine Enzymes

`blue.marine_enzymes`

Enzymes from marine organisms whose adaptations to cold, pressure and salt give them properties terrestrial enzymes do not have.

### What it is

Marine enzymes are catalysts from marine organisms, and they constitute a distinct subject only where the marine environment imposed a constraint that terrestrial life did not face. Provenance alone is uninteresting: a protease from a fish gut and a protease from a pig behave similarly and belong to the same industrial category. What separates this record is a set of adaptations with no terrestrial equivalent at industrial scale, chiefly to permanent cold, to hydrostatic pressure and to high salt. Cold adaptation is the most consequential. Most of the ocean by volume sits between about minus one and four degrees Celsius, and enzymes that work there are not warm enzymes running slowly. They are structurally distinct: more flexible, with fewer stabilising interactions, higher catalytic rates at low temperature and much lower thermal stability. That combination is usually described as a trade in which stability is sacrificed for activity. Industrially the description is backwards. The instability IS the product. An enzyme that works at four degrees and is destroyed at forty can be added to a reaction, allowed to act, and then switched off by gentle warming, with no inhibitor, no separation step and no damage to a heat-sensitive product. Very few terrestrial enzymes offer that. Other marine adaptations matter more narrowly. Piezophilic enzymes from the deep sea retain function under hundreds of atmospheres, which is of scientific interest and limited industrial use because few processes run at pressure. Halophilic enzymes from hypersaline environments tolerate salt concentrations that precipitate ordinary proteins, and some function in organic solvent as a consequence. And hyperthermophiles from hydrothermal vents supplied one of the most widely used reagents in molecular biology, a high-fidelity polymerase, which is the field's clearest commercial success and sits at the opposite end of the temperature range from everything else here. The limits are those of the branch. The producing organisms mostly cannot be cultured, so discovery has moved to sequence-based mining, which finds candidates faster than they can be expressed and characterised. Heterologous expression of a protein from a cold, high-pressure organism in a mesophilic host frequently yields insoluble aggregate. And the supply argument that governs `blue.marine_natural_products` does not apply here at all, because an enzyme is a gene: once the sequence is known it can be manufactured by fermentation like any other protein, which is why this record has products and that one has a supply problem.

### In plain language

Enzymes are the tools living things use to build and break down molecules, and they are usually tuned to the temperature of whatever made them. Most of the ocean is close to freezing, so the creatures living there needed tools that still work in the cold. Those tools are useful to us for a reason that sounds like a flaw: they fall apart when warmed gently. That means you can add one to food or to a laboratory reaction, let it do its job in the cold, then warm it slightly to stop it completely, without adding chemicals and without cooking what you were working on. Being easy to destroy is the whole point.

### An analogy

It is a chisel made of ice. That sounds like a poor chisel, and for most work it is: anything requiring heat or force will destroy it immediately. But if the job is delicate and cold, and if what you most need is for the tool to disappear completely the moment you have finished without leaving anything behind, then a chisel that melts in your hand is exactly the right one.

### Why it matters

One marine enzyme is in almost every molecular biology laboratory in the world. A high-fidelity polymerase from a deep-sea hyperthermophile made accurate amplification of long sequences practical, and the sequencing that underpins `blue.marine_genomics` depends on reagents of this kind. Cold-adapted enzymes allow food processing at refrigeration temperature, which preserves flavour and texture that heating destroys, and allow detergents to clean in cold water, which saves the electricity that `white.industrial_enzymes` records as its largest environmental claim. In molecular biology, a cold-active phosphatase or nuclease can be inactivated by warming rather than by adding an inhibitor that must then be removed, which removes a step from thousands of protocols. The limits are real. Cold-adapted enzymes are unstable by design, so they have short operational lifetimes and cannot be used in any warm process. Deep-sea and polar sampling is expensive, and the organisms mostly refuse to grow. Expressing a protein evolved for cold and pressure in a mesophilic host often produces insoluble aggregate rather than working enzyme. And the access rules that govern the rest of this branch apply here too: a sequence from another country's waters carries obligations, and a sequence from the high seas carried none at all until very recently.

### Applications

- Cold-active alkaline phosphatase for dephosphorylating DNA, inactivated by gentle warming rather than by an inhibitor that would then have to be removed, which deletes a step from thousands of cloning protocols
- Heat-labile nucleases and uracil DNA glycosylase used to prevent carryover contamination and then destroyed before amplification begins
- Cold-active proteases and lipases in food processing, allowing enzymatic treatment at refrigeration temperature and termination by mild heating without cooking the product
- Enzymatic tenderising and flavour development in fish and seafood processing at chill temperature
- Cold-active enzymes in laundry detergent, contributing to the low temperature washing that `white.industrial_enzymes` records as its largest environmental claim
- Cold-adapted amylases and cellulases in textile processing where heating the bath is the dominant energy cost
- Enzymatic treatment in refrigerated dairy processing, including lactose hydrolysis carried out during cold storage rather than as a separate heated step
- Bioremediation in polar and deep-sea conditions, where mesophilic organisms and their enzymes are inactive
- High-fidelity DNA polymerase from a deep-sea hyperthermophile, which made accurate amplification of long sequences practical and is among the most widely used reagents in biology
- Thermostable ligases and other vent-derived enzymes used in molecular biology where a reaction must survive repeated heating
- Halophilic enzymes for reactions in high ionic strength or in the presence of organic solvent, which precipitate ordinary proteins
- Processing of salted and fermented foods where the substrate itself is a brine
- Agarases, carrageenases and alginate lyases that degrade seaweed polysaccharides no terrestrial enzyme addresses, which is the enzymatic basis of `blue.seaweed_cultivation` processing
- Chitinases and chitin deacetylases converting shellfish processing waste into the materials in `blue.marine_biomaterials`
- Enzymes producing defined oligosaccharides from marine polysaccharides for food and cosmetic use
- Marine haloperoxidases, which incorporate bromine and chlorine and are the enzymatic reason marine natural products are so frequently halogenated
- Ice-binding and antifreeze proteins used to control ice crystal formation in frozen food and in cryopreservation

### Technologies

- Sequence-based mining of marine metagenomes for enzyme families, which supplies candidates from organisms nobody has grown
- Functional metagenomic screening of expression libraries built from environmental DNA, which finds activity without needing to recognise the sequence
- Culture of the minority of marine organisms that will grow, still the route to the best-characterised enzymes
- Targeted sampling of habitats that impose the wanted constraint, which is the oldest heuristic in enzymology and works: look for a cold enzyme where it is cold
- Heterologous expression in conventional hosts, which is what removes this record's supply problem and introduces its folding problem
- Low-temperature expression and cold-adapted expression hosts, used because a protein evolved at four degrees frequently aggregates when made at thirty-seven
- Chaperone co-expression and refolding from inclusion bodies
- Codon optimisation for the expression host, since the source organism's codon usage may be strongly biased
- Directed evolution and rational design to raise stability without losing the low-temperature activity that motivated the enzyme, which is the central engineering tension of this record
- Immobilisation, which extends operational lifetime and partially compensates for inherent instability
- Formulation and stabiliser selection for enzymes that are unstable by design
- Determination of activity and stability profiles across temperature, which is the measurement that decides whether an enzyme is genuinely cold-adapted or merely from a cold place
- Structural determination to identify the flexibility features that underlie cold adaptation
- High-pressure assay equipment for piezophilic enzymes, which few laboratories have and which is why that area remains small

### Challenges

- Improving stability without losing the low-temperature activity that made the enzyme worth having, since the two properties arise from the same structural flexibility and engineering one degrades the other
- Short operational lifetime, which raises the cost per unit of product exactly as `white.industrial_enzymes` records for total turnover number, and which is inherent rather than a defect to be fixed
- Insoluble expression, since a protein evolved at four degrees and high pressure frequently aggregates when produced in a mesophilic host at thirty-seven
- Uncultivability of most source organisms, which moves discovery to sequence and expression rather than to isolation from the native producer
- Candidate sequences accumulating faster than they can be expressed and characterised, so the bottleneck has moved from finding to testing
- Sampling cost for deep-sea and polar habitats, which limits discovery to the places a vessel can reach
- Absence of high-pressure assay equipment in most laboratories, which is why piezophilic enzymology remains a small field regardless of its scientific interest
- Competition from engineered terrestrial enzymes, since a well-understood mesophilic enzyme evolved in the laboratory towards cold activity may reach the market faster than a marine one taken from discovery
- Narrow application windows, because an enzyme that is destroyed above forty degrees is excluded from every process that involves heat
- Access and benefit sharing obligations attaching to the sequence, which matter more here than in most enzyme work because the product IS the sequence rather than a physical sample
- Uncertain status of sequences obtained from beyond national jurisdiction before 2023

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Relative activity at low temperature | `A_rel` | per cent of maximal activity retained at 5 degrees Celsius | 30 - 70 % for a genuinely cold-adapted enzyme, against a few per cent for a mesophilic counterpart | CONSENSUS |
| Apparent optimum temperature | `T_opt` | degrees Celsius | 15 - 30 degrees C for cold-adapted enzymes, and above 90 for vent-derived thermostable ones | CONSENSUS |
| Inactivation temperature | `T_inact` | degrees Celsius for complete and irreversible loss of activity | 45 - 65 degrees C for a heat-labile marine enzyme | CONSENSUS |
| Melting temperature | `T_m` | degrees Celsius | 40 - 55 degrees C for psychrophilic enzymes, above 100 for hyperthermophilic ones | CONSENSUS |
| Operational half-life | `t_half` | hours of retained activity under process conditions | short relative to mesophilic industrial enzymes | REVIEWED |
| Activation energy | `E_a` | kilojoules per mole | lower for cold-adapted enzymes than for mesophilic counterparts | CONSENSUS |
| Turnover number | `k_cat` | per second | comparable to or exceeding mesophilic counterparts at low temperature | CONSENSUS |
| Specificity constant | `k_cat/K_M` | per molar per second | the correct basis for comparing two enzymes at a stated temperature | CONSENSUS |
| Salt tolerance | `c_salt` | molar sodium chloride at which activity is retained | up to 3 - 4 M for halophilic enzymes, where ordinary proteins precipitate well below | REVIEWED |
| Pressure tolerance | `p_tol` | megapascals at which activity is retained | up to roughly 100 MPa for piezophilic enzymes, corresponding to the deepest ocean | REVIEWED |
| Soluble expression fraction | `f_sol` | per cent of expressed protein recovered soluble and active | frequently low for psychrophilic and piezophilic proteins in mesophilic hosts | REPORTED |

### History

- **1969** - A thermophilic bacterium from a terrestrial hot spring is described, establishing that enzymes can be sought where the conditions are
- **1976** - A thermostable polymerase is purified from that hot spring organism
- **1977** - Hydrothermal vents are discovered, revealing organisms living above one hundred degrees Celsius under pressure
- **1984** - Psychrophilic enzymes are systematically characterised and their activity and stability trade is described
- **1991** - A high-fidelity proofreading polymerase from a deep-sea hyperthermophilic archaeon enters routine use
- **1997** - Disputes over commercial benefit from enzymes collected in protected areas force the question of who owns an extremophile
- **2000** - Functional metagenomic screening recovers enzymes from organisms that have never been cultured
- **2005** - Cold-active enzymes reach commercial molecular biology products
- **2012** - Sequence mining produces candidate enzymes faster than they can be expressed and characterised
- **2018** - Directed evolution of mesophilic enzymes towards cold activity becomes a practical alternative to marine discovery
- **2023** - The agreement on marine biological diversity beyond national jurisdiction brings high seas sequences within a framework

### Governance

| Field | Value |
|---|---|
| Maturity | COMMERCIAL |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | AUTHORISED |
| Domains | MATERIALS, FOOD, INFORMATION |
| SDGs | 9, 12, 13 |

### Regulations

- The Convention on Biological Diversity and the Nagoya Protocol, whose obligations attach to the sequence and not only to a physical sample, which is decisive here because nothing physical need ever cross a border
- Regulation (EU) No 511/2014, imposing due diligence and record-keeping on users of genetic resources within the Union
- The 2023 Agreement on marine biological diversity of areas beyond national jurisdiction, including its provisions on digital sequence information
- The United Nations Convention on the Law of the Sea, under which marine scientific research in another state's waters requires consent
- National marine collection permits and protected area conditions
- Directive 2009/41/EC on the contained use of genetically modified microorganisms, which governs the expression host rather than the enzyme
- Directive 2000/54/EC on biological agents at work
- Regulation (EC) No 1332/2008 on food enzymes and the Union list authorisation procedure
- Regulation (EC) No 1831/2003 on feed additives
- Regulation (EC) No 1907/2006 REACH and Regulation (EC) No 1272/2008 CLP
- Regulation (EC) No 648/2004 on detergents, for the cold-wash applications
- Occupational exposure requirements for enzyme dust as a respiratory sensitiser, which apply to marine enzymes exactly as to any other

### Standards

- Reporting conventions requiring activity to be stated at a defined temperature against a mesophilic comparator, without which a claim of cold adaptation cannot be distinguished from a claim of cold provenance
- Declaration of assay duration alongside an optimum temperature, since for an unstable enzyme a shorter assay moves the apparent optimum upwards
- Declaration of the criteria used for inactivation, since partial or reversible loss of activity does not deliver the property the product is sold for
- International Union of Biochemistry and Molecular Biology enzyme nomenclature and EC numbering
- Supplier-declared assay conditions for the activity unit, on the same terms `white.industrial_enzymes` records
- Joint FAO/WHO Expert Committee on Food Additives specifications for enzyme preparations, and Food Chemicals Codex monographs for food grades
- Good Manufacturing Practice and HACCP or FSSC 22000 certification for the production site
- Association of Manufacturers and Formulators of Enzyme Products guidance on safe handling and encapsulation
- Sequence deposition in the international nucleotide databases, which in this field is simultaneously good scientific practice and the act that makes a genetic resource globally available, a tension the benefit sharing instruments have not fully resolved
- Strain and clone deposit in a recognised culture collection under the Budapest Treaty where patent protection is sought
- Research partnership norms under which scientists from the sampled region are co-investigators, which for a sequence-based product is the only benefit sharing that occurs before commercialisation

### Related records

- `white.industrial_enzymes`
- `blue.marine_genomics`
- `blue.marine_natural_products`
- `white.biocatalysis`
- `blue.seaweed_cultivation`
- `purple.access_benefit_sharing`

### Cross-references

- [white.industrial_enzymes](../white/industrial_enzymes.md)
- [blue.marine_genomics](marine_genomics.md)
- [blue.marine_natural_products](marine_natural_products.md)
- [white.biocatalysis](../white/biocatalysis.md)
- [blue.seaweed_cultivation](seaweed_cultivation.md)
- `purple.access_benefit_sharing` (branch not written yet)
