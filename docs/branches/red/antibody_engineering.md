<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/antibody_engineering/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Antibody Engineering**

## Antibody Engineering

`red.antibody_engineering`

Designing and optimising antibody-derived molecules for affinity, specificity, half-life and effector function.

### What it is

A natural immunoglobulin G is a Y-shaped protein whose two arms bind an antigen and whose stem recruits immune effectors. Antibody engineering treats that architecture as modular: the binding arms and the effector stem are encoded separately, fold independently, and can be recombined with each other or with entirely non-antibody components. Discovery generates candidate binders from immunised animals, from human donor B cells, or from synthetic libraries displayed on phage, yeast or ribosomes. Selection enriches binders through iterative panning against the target, a directed evolution loop that can search a library of ten billion variants in a fortnight. Optimisation then addresses each property separately, which is what modularity buys. Affinity maturation improves binding, usually into the low nanomolar or picomolar range. Humanisation replaces rodent framework residues to reduce immunogenicity. Fc engineering tunes circulating half-life through the neonatal Fc receptor and tunes effector recruitment up or down independently of binding. Developability screening removes candidates that aggregate, oxidise or express poorly before they consume years of development. The binding constraint is delivery to the target, not affinity for it. A molecule of one hundred and fifty kilodaltons crosses a capillary wall slowly, penetrates a solid tumour poorly and crosses the blood-brain barrier hardly at all, which is why most format innovation in the last two decades has been about size and shape rather than about tighter binding.

### In plain language

Your immune system makes proteins called antibodies. Each one is shaped to lock onto a single specific target and nothing else, rather like a key cut for one lock. An antibody has two working parts: the end that grips the target, and the tail that calls the rest of the immune system over to deal with whatever has been gripped. Because those two parts are separate, scientists can change one without disturbing the other. They can find an antibody for almost any chosen target, make its grip tighter, make it last longer in the blood, attach a drug so the drug is delivered only where the antibody sticks, or join two different grips so that one molecule has to grab two things at once before anything happens.

### An analogy

A courier with an exact address. The parcel does not go to the whole city; it goes to one door. Antibody engineering is address-writing plus vehicle design: you can make the address more precise, put a different parcel in the van, or build a van that must visit two addresses on the same trip. Where the comparison fails is the interesting part. A real courier can reach any door in the city. These vans are large, the streets inside a tumour are badly built, and the road into the brain is closed, which is why so much of the field is about building a smaller van rather than writing a better address.

### Why it matters

Monoclonal antibodies are the largest class of biologic medicine by revenue and have changed the outlook in cancer, rheumatoid arthritis, asthma, migraine, high cholesterol and transplant rejection. They are also the fastest route to a therapy against a new pathogen: a neutralising antibody can be isolated from a convalescent donor within weeks, long before any vaccine campaign can protect a population. The costs are real and specific. Doses are measured in hundreds of milligrams rather than milligrams, so manufacturing is expensive and annual treatment costs run into tens of thousands of euro. The molecules must be injected rather than swallowed. And because the technology works best against targets that are easy to reach in the bloodstream, it has advanced fastest for the diseases of wealthy populations and slowest for those it could most cheaply have helped.

### Applications

- Checkpoint inhibitor antibodies that release a suppressed immune response against a tumour
- Anti-TNF and anti-interleukin antibodies in autoimmune disease
- PCSK9 inhibitors that lower circulating cholesterol
- CGRP-pathway antibodies for migraine prevention
- Long-acting neutralising antibodies for respiratory syncytial virus prophylaxis in infants
- Antivenoms and antitoxins produced as defined recombinant molecules
- Antibody-drug conjugates delivering a cytotoxic payload to a tumour cell
- Radioimmunoconjugates for imaging and for targeted radiotherapy
- Bispecific T-cell engagers that force a synapse between a tumour cell and a T cell
- Bispecific antibodies that replace the function of a missing clotting factor
- Antibody fragments small enough for intravitreal injection into the eye
- Nanobody-based imaging agents and intracellular binders
- Diagnostic and research antibodies underpinning most immunoassays

### Technologies

- Phage display of synthetic and immune libraries
- Yeast surface display with fluorescence-activated sorting
- Ribosome and mRNA display for libraries beyond cellular transformation limits
- Single B-cell cloning from convalescent or immunised donors
- Transgenic mice carrying human immunoglobulin loci
- Camelid immunisation for single-domain heavy-chain antibodies
- Iterative panning with increasing stringency
- Affinity maturation by error-prone PCR or targeted library design
- Deep mutational scanning of the binding interface
- Complementarity-determining region grafting onto human frameworks
- Germlining to revert non-essential residues to the closest human sequence
- Fc engineering for neonatal Fc receptor binding and extended half-life
- Afucosylation to increase antibody-dependent cellular cytotoxicity
- Effector-silent Fc variants where recruitment would be harmful
- Site-specific conjugation chemistry with defined attachment points
- Cleavable and non-cleavable linker design
- In silico developability and immunogenicity prediction
- High-concentration viscosity and aggregation screening
- Forced degradation studies for oxidation, deamidation and isomerisation

### Challenges

- Poor penetration into solid tumours, where a large molecule must cross a leaky vasculature and diffuse through dense stroma against raised interstitial pressure
- Almost no transfer across the blood-brain barrier, which excludes most neurological targets without an active transport strategy
- Injection only, since a protein of this size is digested if swallowed, which limits use in conditions where daily oral dosing is the standard
- Aggregation and viscosity at the high concentrations needed to deliver a large dose in a small subcutaneous volume
- Anti-drug antibodies that neutralise the therapeutic over months to years, which is difficult to predict from sequence alone
- Cytokine release with agonist and T-cell-engaging formats, requiring step-up dosing and inpatient monitoring
- Crowded intellectual property around popular targets, where dozens of molecules chase the same antigen while neglected targets attract none
- Cost of goods for chronic indications, which keeps annual treatment in the tens of thousands of euro and confines many products to wealthy health systems

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Equilibrium dissociation constant | `K_D` | molar | 1e-12 - 1e-8 M | CONSENSUS |
| Association rate constant | `k_on` | per molar per second | 1e4 - 1e7 1/(M*s) | CONSENSUS |
| Dissociation rate constant | `k_off` | per second | 1e-5 - 1e-2 1/s | CONSENSUS |
| Avidity enhancement | `beta` | fold, dimensionless | 10 - 1000 fold over monovalent affinity | REVIEWED |
| Half maximal effective concentration | `EC50` | nanomolar | 0.01 - 100 nM | CONSENSUS |
| Drug-to-antibody ratio | `DAR` | payload molecules per antibody | 2 - 8, most commonly 4 | REVIEWED |
| Serum half-life | `t_half` | days | 14 - 21 days for IgG1; hours for a fragment | CONSENSUS |
| High molecular weight aggregate | `HMW` | per cent by size-exclusion chromatography | < 2 - 5 % at release | CONSENSUS |

### History

- **1890** - Behring and Kitasato demonstrate serum therapy against diphtheria
- **1975** - Kohler and Milstein describe hybridoma monoclonal antibodies
- **1986** - Muromonab-CD3 approved: the first therapeutic monoclonal antibody
- **1988** - Complementarity-determining region grafting demonstrated
- **1990** - Phage display of antibody fragments demonstrated
- **1993** - Camelid heavy-chain-only antibodies described
- **1997** - Rituximab approved, establishing antibodies as a mainstream modality
- **1998** - Trastuzumab approved alongside a companion diagnostic
- **2006** - The TGN1412 first-in-human trial causes multi-organ failure in six healthy volunteers
- **2011** - Modern antibody-drug conjugates reach approval
- **2014** - Checkpoint inhibitor antibodies transform oncology practice
- **2017** - Emicizumab approved, a bispecific antibody that substitutes for a missing clotting factor
- **2021** - Deep-learning structure prediction enters routine antibody design

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | BENCH |
| Regulatory status | AUTHORISED |
| Domains | HEALTH |
| SDGs | 3, 9 |

### Regulations

- EU Directive 2001/83/EC on medicinal products for human use
- EU Regulation (EC) No 726/2004 centralised authorisation procedure, mandatory for all biotechnology-derived medicines
- US Public Health Service Act section 351 biologics licence
- US Biologics Price Competition and Innovation Act 2009, under which antibody biosimilars are authorised
- EU Regulation (EU) No 536/2014 on clinical trials
- EMA Guideline on strategies to identify and mitigate risks for first-in-human and early clinical trials, EMEA/CHMP/SWP/28367/07 Rev 1, written in direct response to the 2006 TGN1412 incident
- ICH S6(R1) preclinical safety evaluation of biotechnology-derived pharmaceuticals, which sets the species-relevance requirement
- EU Directive 2010/63/EU on the protection of animals used for scientific purposes, a first-order constraint here because immunisation is a routine production step
- EU Directive 2010/63/EU Article 4, the Three Rs, which is the formal basis for preferring display technologies over immunisation where either would work
- ICH Q6B specifications for biotechnological and biological products

### Standards

- WHO International Nonproprietary Name scheme for monoclonal antibodies, revised in 2021 to replace the single -mab stem with -tug, -bart, -mig and -ment, encoding format rather than species of origin
- IMGT unique numbering for immunoglobulin and T-cell receptor variable domains
- Kabat and Chothia numbering schemes, still in parallel use, which is a routine source of confusion when comparing two papers
- ICH Q5E comparability of products subject to changes in manufacturing
- EMA Guideline on similar biological medicinal products containing monoclonal antibodies
- WHO International Standards for biological reference preparations, without which titres from different laboratories are not comparable
- ISO 20395 requirements for evaluating the performance of quantification methods for nucleic acid target sequences
- EU GMP Annex 2 biological medicinal products
- ICH Q11 development and manufacture of drug substances

### Related records

- `red.pharmaceutical_biotechnology`
- `red.cell_therapy`
- `red.vaccine_development`
- `red.molecular_diagnostics`
- `yellow.food_safety_biotechnology`
- `gold.nanobiotechnology`
- `gold.structural_bioinformatics`
- `gold.machine_learning_in_biology`

### Cross-references

- [red.pharmaceutical_biotechnology](pharmaceutical_biotechnology.md)
- [red.cell_therapy](cell_therapy.md)
- [red.vaccine_development](vaccine_development.md)
- [red.molecular_diagnostics](molecular_diagnostics.md)
- [yellow.food_safety_biotechnology](../yellow/food_safety_biotechnology.md)
- `gold.nanobiotechnology` (branch not written yet)
- `gold.structural_bioinformatics` (branch not written yet)
- `gold.machine_learning_in_biology` (branch not written yet)
