<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/blue/marine_genomics/.
  Edit the source and run `make docs`.
-->

[Blue Biotechnology](index.md) / **Marine Genomics**

## Marine Genomics

`blue.marine_genomics`

Sequencing and analysing the genomes of marine organisms and communities, including the great majority that cannot be cultured.

### What it is

Marine genomics reads the genetic material of marine organisms and, more consequentially, of whole marine communities without isolating their members first. The distinction matters because only a small minority of marine microorganisms will grow in laboratory culture, so for most of the history of microbiology the marine microbial world was described from the unrepresentative fraction that happened to be cultivable. Sequencing DNA extracted directly from seawater removed that requirement and did not refine the existing picture so much as replace it: abundant lineages that no survey had recorded turned out to dominate whole water columns. Practice spans four scales. Single-organism genomics assembles reference genomes for species of scientific or commercial interest. Metagenomics sequences everything in a water or sediment sample together and reconstructs the genomes present computationally. Metatranscriptomics and single-cell genomics ask what is being expressed and what belongs to which cell, since a metagenome alone cannot always say which gene sits in which organism. Environmental DNA surveys detect the species present in a body of water from the traces they shed, which turns a genetic method into a monitoring tool for animals nobody has seen. Three features make marine sequencing a distinct problem rather than an application of the general method. Reference databases are poor, because marine lineages are under-represented, so a large fraction of marine sequence matches nothing known and is reported as dark matter. Symbiosis is pervasive, so a sponge genome arrives mixed with the genomes of the microbial community inside it, and separating them is a computational problem rather than a laboratory one. And sampling is expensive and sparse, since ship time and submersibles cost more than any sequencing, which inverts the usual economics of genomics. The binding constraints are therefore sampling cost, reference database poverty, and the legal position of samples taken outside national waters, which was unresolved until very recently and remains unsettled in practice. None of the three is a sequencing problem, and none is solved by sequencing more.

### In plain language

Almost everything we knew about life in the sea used to come from what we could catch and keep alive. That turns out to be a very small and very misleading sample: fewer than one in a hundred ocean microbes will grow in a laboratory. Reading DNA directly from a bucket of seawater removed that limit, and what appeared was not a few extra species but whole groups of organisms nobody knew existed, some of them among the most abundant living things on Earth. The same trick now identifies which fish are in a river from the traces they leave in the water, without catching or even seeing them.

### An analogy

It is the old story of looking for keys under the streetlight, with one difference that matters. The man in the story knows the light is only covering a small patch. Microbiology did not: the culturable organisms were assumed to be the ocean's inhabitants rather than the few that tolerated a plate of jelly. Sequencing did not brighten the lamp, it showed how dark the rest of the street had always been.

### Why it matters

This method rewrote the census of life. The most abundant photosynthetic organism on the planet was not described until 1988, and an entire abundant group of marine archaea was invisible until sequencing found them. Ocean-scale sampling expeditions have multiplied the number of known genes several times over, and the resulting catalogues are the raw material for the enzyme and natural product records elsewhere in this branch: you cannot search for a cold-adapted enzyme in organisms nobody knows exist. Environmental DNA has become a practical monitoring tool, detecting invasive species and rare animals from water samples rather than from nets. The costs are structural rather than technical. Ship time and deep-sea access are expensive enough that sampling, not sequencing, sets what gets studied, which concentrates knowledge in the waters of wealthy countries and near convenient ports. Reference databases are correspondingly skewed, so an unfamiliar sequence is often unidentifiable rather than novel. And a very large fraction of the ocean lies beyond any national jurisdiction, where the question of who may take a sample, publish its sequence and patent what it encodes had no clear answer at all until 2023, and where practice is still settling.

### Applications

- Ocean-scale metagenomic surveys that catalogue the genes present in seawater across depths and latitudes, which multiplied the number of known protein families several times over
- Reconstruction of genomes from metagenomes for organisms that have never been cultured and may never be
- Single-cell genomics of individual sorted cells, which resolves which gene belongs to which organism where a metagenome cannot
- Ribosomal gene surveys for community composition, still the cheapest way to ask what is present before deciding what to sequence deeply
- Reference genome assembly for marine species of scientific, commercial or conservation interest
- Metatranscriptomics and metaproteomics, which distinguish the genes a community carries from the genes it is actually using
- Resolution of host and symbiont genomes in sponges, corals and chemosynthetic animals, where the biology of interest belongs to the partnership rather than to either partner
- Comparative genomics of adaptation to pressure, cold, darkness and hypersalinity, which is where the enzymes in `blue.marine_enzymes` are first identified
- Genomic study of coral bleaching and of the algal symbionts whose loss causes it
- Biosynthetic gene cluster mining for natural products, which finds the chemistry a sequence encodes without needing to isolate the compound
- Identification of the microbial symbiont that actually produces a compound attributed to its animal host, which is frequently the route out of the supply problem described in the branch header
- Sequence-based discovery of enzymes with unusual stability, which is what makes a laboratory reagent out of a deep-sea organism
- Environmental DNA surveys that detect species present in a water body from shed traces, without catching, seeing or disturbing them
- Invasive species detection in ballast water and in ports, where early detection is worth more than accurate abundance
- Fisheries stock structure and traceability, including identification of the species actually present in a sold product
- Genetic monitoring of populations under exploitation or climate stress

### Technologies

- Research vessel sampling with depth-resolved water bottles and filtration onto membranes, which is where most of the cost of this field sits
- Remotely operated and autonomous vehicles for deep and hazardous sampling
- Autonomous samplers and floats that collect and preserve without a ship present
- In situ preservation and cold chain from sample to laboratory, since nucleic acid degrades before it is analysed
- Nucleic acid extraction from low-biomass seawater, where the target is dilute and the volume is large
- Extraction from sediment and from calcifying tissue, where inhibitors co-purify with the nucleic acid and defeat the enzymes used downstream
- Whole genome amplification for single cells and for samples below the input requirement of a sequencer
- Short-read sequencing for depth and accuracy, and long-read sequencing for assembly across repeats
- Portable nanopore sequencing aboard ship, which removes the delay between sampling and result
- Amplicon sequencing of marker genes for community composition and for environmental DNA
- Metagenome assembly and binning into metagenome-assembled genomes
- Taxonomic assignment against reference databases, and the honest reporting of the large fraction that matches nothing
- Biosynthetic gene cluster prediction from sequence
- Phylogenomic placement of lineages with no cultured representative
- Reference barcode library construction, without which environmental DNA detects an organism it cannot name
- Open data deposition, which in this field is unusually consequential because re-analysis of existing expedition data is cheaper than any new sampling

### Challenges

- Sampling cost, since ship time, submersibles and deep-sea access cost far more than the sequencing, which inverts the usual economics of genomics and means access to a vessel rather than to a sequencer decides what is studied
- Geographic bias in what has been sampled, concentrated near wealthy countries, convenient ports and existing research stations, so the ocean is described unevenly rather than representatively
- Reference database poverty, so a large fraction of marine sequence matches nothing known and is reported as unidentified rather than as novel
- Absence of barcode reference libraries for many taxa, which lets environmental DNA detect an organism it cannot name
- The unculturable majority, which can now be sequenced but still cannot be grown, tested, mutated or asked a question experimentally
- Pervasive symbiosis, so a host genome arrives mixed with its microbial community and separating them is a computational rather than a laboratory problem
- Inhibitors co-purifying from sediment, mucus and calcifying tissue, which defeat the enzymes used in the next step
- Low biomass in open ocean water, so large volumes must be filtered to recover enough nucleic acid
- Degradation between sampling and analysis, which the cold chain addresses and does not eliminate
- The legal position of samples taken beyond national jurisdiction, unaddressed until 2023 and still settling in practice, which leaves historical collections in an uncertain position
- Access and benefit sharing obligations for samples from within national waters, which attach to the sequence and not only to the physical sample
- Damage to the habitat being surveyed, particularly where deep-sea sampling is destructive of slow-growing communities that will not recover within a human lifetime

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Unassigned sequence fraction | `f_dark` | per cent of reads with no match in reference databases | commonly a third to two thirds in open ocean metagenomes, and higher in deep sea and sediment samples | REVIEWED |
| Culturable fraction | `f_cult` | per cent of cells observed that will grow in laboratory culture | commonly quoted as around 1 %, and varying by habitat | CONSENSUS |
| Genome completeness | `C_gen` | per cent of expected single-copy marker genes present | above 90 % for a high-quality metagenome-assembled genome | CONSENSUS |
| Contamination of an assembled genome | `X_gen` | per cent of markers present in more than one copy | below 5 % for a high-quality bin | CONSENSUS |
| Assembly contiguity | `N50` | base pairs | kilobases for a short-read metagenome, megabases for a long-read single genome | CONSENSUS |
| Sequencing depth | `D_seq` | gigabases per sample | 1 - 100 Gb depending on community complexity | CONSENSUS |
| Coverage of the rare biosphere | `f_rare` | per cent of estimated diversity recovered at a given depth | rarely above 60 - 80 % for a complex marine community | REVIEWED |
| Environmental DNA detection probability | `p_det` | probability of detecting a species present, per sample | high for abundant species close by, poor for rare or distant ones | REVIEWED |
| Environmental DNA persistence | `t_eDNA` | hours to days before degradation below detection | hours to a few days in warm surface water, longer in cold and dark conditions | REVIEWED |
| Cost per sample including collection | `C_sample` | euro per sample, collection included | dominated by ship time rather than by sequencing, and orders of magnitude higher for deep-sea access | REPORTED |
| Biosynthetic gene clusters per genome | `n_BGC` | predicted clusters per assembled genome | varying widely; enriched in sponge and sediment symbionts | REVIEWED |

### History

- **1932** - The gap between cells counted under a microscope and colonies grown on a plate is documented
- **1977** - Ribosomal RNA sequence comparison establishes that microbial relationships can be read from molecules
- **1977** - Hydrothermal vent communities are discovered
- **1985** - Ribosomal gene sequences are recovered directly from seawater, revealing organisms absent from every culture collection
- **1988** - Prochlorococcus is described and proves to be among the most abundant photosynthetic organisms on Earth
- **1990** - An abundant lineage of marine archaea is found by sequence in ordinary seawater
- **1991** - A thermostable polymerase from a deep-sea hyperthermophile enters routine laboratory use
- **2004** - Shotgun sequencing of Sargasso Sea water produces a very large number of previously unknown genes from a single expedition
- **2010** - The accumulation of unassignable marine sequence outpaces the ability to identify it
- **2015** - A global ocean sampling expedition publishes depth-resolved and systematically collected metagenomes
- **2016** - Environmental DNA becomes an accepted survey method for aquatic animals
- **2023** - An international agreement addresses marine genetic resources beyond national jurisdiction

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | CONTROLLED |
| Scale | POPULATION |
| Regulatory status | NOTIFIED |
| Domains | INFORMATION, ENVIRONMENT, HEALTH |
| SDGs | 9, 14, 17 |

### Regulations

- The United Nations Convention on the Law of the Sea, which defines the zones and under whose Part XIII marine scientific research in another state's waters requires that state's consent
- The 2023 Agreement on marine biological diversity of areas beyond national jurisdiction, the first instrument to address marine genetic resources from the high seas, including digital sequence information
- International Seabed Authority rules for activities on the deep seabed, a regime designed for minerals and applied to a biological question
- The Convention on Biological Diversity and the Nagoya Protocol on access and benefit sharing, under which prior informed consent and mutually agreed terms are required and the obligation follows the sequence rather than only the sample
- Regulation (EU) No 511/2014, which implements the Nagoya Protocol for users within the Union and imposes due diligence and record-keeping
- National marine scientific research permit requirements and territorial sea access conditions
- Marine protected area legislation and site-specific sampling permits
- CITES and national protected species legislation, where the organism sampled is itself protected
- Ballast water management requirements, relevant where environmental DNA is used for compliance monitoring
- Biosecurity and phytosanitary import rules for transporting biological samples between jurisdictions
- Regulation (EU) 2016/679, applicable in the narrow but real case where human sequence is recovered incidentally from an environmental sample

### Standards

- Minimum Information about any Sequence and the related genomic standards, which fix what must be reported alongside a sequence for it to be reusable
- Standardised sampling and filtration protocols from the major ocean sampling programmes, without which depth, volume and filter pore size vary enough to change the answer
- Environmental DNA reporting guidelines covering replication, controls and the distinction between detection and abundance
- Reference barcode library conventions, since environmental DNA can detect only what a library can name
- Taxonomic nomenclature conventions for lineages known only from sequence, which are still contested since the codes were written for organisms that could be deposited as specimens
- International Nucleotide Sequence Database Collaboration deposition requirements, which are what makes re-analysis cheaper than resampling
- FAIR data principles, which in this field have unusual force because collection cost so far exceeds analysis cost
- Research collaboration norms against helicopter science, under which scientists from the sampled region are partners rather than a logistics arrangement, and which the 2023 agreement's capacity-building provisions are intended to reinforce
- Institutional codes on sampling impact, particularly for slow-growing deep-sea communities that will not recover within a human lifetime
- ISO/IEC 17025 accreditation where environmental DNA results are used for regulatory decisions rather than for research

### Related records

- `blue.marine_natural_products`
- `blue.marine_enzymes`
- `gold.genomics_data_analysis`
- `grey.environmental_biomonitoring`
- `grey.biodiversity_conservation`
- `purple.access_benefit_sharing`

### Cross-references

- [blue.marine_natural_products](marine_natural_products.md)
- [blue.marine_enzymes](marine_enzymes.md)
- `gold.genomics_data_analysis` (branch not written yet)
- [grey.environmental_biomonitoring](../grey/environmental_biomonitoring.md)
- [grey.biodiversity_conservation](../grey/biodiversity_conservation.md)
- `purple.access_benefit_sharing` (branch not written yet)
