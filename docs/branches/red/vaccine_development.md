<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/red/vaccine_development/.
  Edit the source and run `make docs`.
-->

[Red Biotechnology](index.md) / **Vaccine Development**

## Vaccine Development

`red.vaccine_development`

Design, manufacture and evaluation of prophylactic and therapeutic vaccines across live, subunit and nucleic-acid platforms.

### What it is

A vaccine presents the adaptive immune system with an antigen under conditions that generate immunological memory without causing disease. Platforms differ in how the antigen is supplied. Live attenuated vaccines use a weakened replicating organism and give the broadest and longest-lasting response, but cannot be given to everyone. Inactivated whole-organism vaccines are safer and weaker. Subunit, recombinant protein and virus-like particle vaccines present only the relevant antigen and depend on an adjuvant for potency. Conjugate vaccines couple a bacterial polysaccharide to a carrier protein to recruit T-cell help, which is what makes them work in infants. Viral vector vaccines use a replication-defective virus to deliver the antigen gene. Nucleic-acid vaccines deliver messenger RNA in a lipid nanoparticle, so that the recipient's own cells transiently make the antigen. Modern antigen design is increasingly structure-guided: stabilising a viral fusion protein in its prefusion conformation can raise neutralising titres by an order of magnitude relative to the wild-type sequence, which is a design gain rather than a manufacturing one. The binding constraint is not immunogenicity but deployment. A vaccine that works is only useful once it has been made in the hundreds of millions of doses, kept cold across a continent, and accepted by the people it is offered to.

### In plain language

Your immune system learns by experience. Once it has met a germ it remembers the encounter and responds much faster the next time. A vaccine arranges that first meeting safely. It shows the body a piece of the germ, or instructions for making one harmless piece of it, so the immune system builds its memory without you ever being ill. Some vaccines use a weakened version of the germ itself. Newer ones send a short message that your cells read once and then break down, leaving nothing behind except the memory.

### An analogy

It is a fire drill. Nobody sets the building alight; everyone simply walks the escape route once, in calm conditions, so that when smoke does appear the response is automatic instead of improvised. The comparison breaks down in one useful way: a drill only teaches people what to do, whereas a vaccine physically changes what the body is able to do.

### Why it matters

Smallpox killed an estimated three hundred million people in the twentieth century alone and no longer exists outside two freezers. Routine childhood immunisation is credited with preventing several million deaths a year. During the COVID-19 pandemic the interval between publishing a viral sequence and dosing the first trial participant fell to sixty-three days, which permanently changed what counts as a realistic response time to a new pathogen. Against that: doses reached high-income countries roughly a year before they reached low-income ones, cold chain requirements still exclude the places with the weakest health systems, and organised misinformation has pushed measles coverage below the level that stops transmission in several countries that had eliminated it.

### Applications

- Live attenuated measles, mumps and rubella vaccination
- Inactivated and oral poliovirus vaccination
- Recombinant hepatitis B surface antigen vaccine
- Human papillomavirus virus-like particle vaccines
- Conjugate vaccines against pneumococcus, meningococcus and Haemophilus
- Seasonal and pandemic influenza strain updates
- Viral-vector vaccines against Ebola virus disease
- Messenger RNA vaccines against respiratory viruses
- Malaria vaccination in children in endemic regions
- Respiratory syncytial virus vaccination in older adults
- Therapeutic cancer vaccines and individualised neoantigen platforms
- Maternal immunisation to protect newborns before they can be vaccinated

### Technologies

- In vitro transcription of messenger RNA with modified nucleosides
- Ionisable lipid nanoparticle formulation
- Self-amplifying RNA constructs at lower dose
- Recombinant protein expression in yeast, insect and mammalian cells
- Virus-like particle self-assembly
- Nanoparticle scaffolds displaying multiple antigen copies
- Egg-based, cell-culture and recombinant influenza production
- Attenuation by serial passage or by rational gene deletion
- Polysaccharide-protein conjugation chemistry
- Replication-defective adenoviral and vesicular stomatitis virus vectors
- Structure-based prefusion antigen stabilisation
- Adjuvant systems based on squalene emulsion or TLR agonists
- Reverse vaccinology from pathogen genome sequences
- Lyophilisation and thermostable formulation for warm climates
- Microneedle patches and needle-free delivery

### Challenges

- Antigenic drift and shift, which force annual reformulation for influenza and leave every candidate chasing a moving target
- Correlates of protection are unknown for several major pathogens, so a candidate cannot be evaluated without a full efficacy trial
- Cold chain and last-mile delivery, which fail first in exactly the places with the highest disease burden
- Manufacturing capacity concentrated in a handful of countries, so a surge in demand is met in order of wealth rather than in order of need
- A commercial model that rewards chronic therapy over a product given once or twice in a lifetime at a few euro per dose
- Vaccine hesitancy and coordinated misinformation, which have pushed measles coverage below the elimination threshold in countries that had previously eliminated it
- Reactogenicity that is medically trivial but reduces uptake of second and subsequent doses
- Equitable global allocation during a surge, which no existing mechanism has yet delivered

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Vaccine efficacy | `VE` | per cent reduction in risk relative to control | 50 - 97 % against symptomatic disease | CONSENSUS |
| Basic reproduction number | `R0` | secondary cases per case, dimensionless | 1.5 for seasonal influenza to 15 or more for measles | CONSENSUS |
| Herd immunity threshold | `H_c` | fraction of the population immune | 1 - 1/R0, so about 0.93 for measles | CONSENSUS |
| Geometric mean titre | `GMT` | reciprocal serum dilution | platform-specific and assay-specific | CONSENSUS |
| Seroconversion rate | `SCR` | per cent of subjects reaching a defined titre rise | > 70 % for a licensable candidate in adults | REVIEWED |
| Number needed to vaccinate | `NNV` | people vaccinated per case prevented | 10 to several thousand, depending on incidence | CONSENSUS |
| Storage temperature requirement | `T_store` | degrees Celsius | -70 degC to +8 degC depending on platform | CONSENSUS |

### History

- **1721** - Variolation against smallpox is publicised in Britain by Lady Mary Wortley Montagu
- **1796** - Jenner demonstrates that cowpox inoculation protects against smallpox
- **1879** - Pasteur produces the first attenuated bacterial vaccine, for fowl cholera
- **1885** - Pasteur administers the first rabies post-exposure vaccine to a child
- **1923** - Formalin inactivation makes diphtheria and tetanus toxoid vaccines possible
- **1955** - Salk inactivated polio vaccine licensed, and the Cutter incident follows within weeks
- **1963** - Measles vaccine licensed, later combined into MMR
- **1980** - The World Health Assembly declares smallpox eradicated
- **1986** - First recombinant vaccine approved, for hepatitis B
- **1987** - First conjugate vaccine licensed, against Haemophilus influenzae type b
- **2006** - Human papillomavirus vaccines introduced
- **2020** - First messenger RNA vaccines authorised for human use
- **2021** - First malaria vaccine recommended by the World Health Organization
- **2023** - First respiratory syncytial virus vaccines approved, decades after a 1960s trial in which a candidate worsened disease

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | POPULATION |
| Regulatory status | AUTHORISED |
| Domains | HEALTH, SECURITY |
| SDGs | 3, 10, 17 |

### Regulations

- EU Directive 2001/83/EC on medicinal products for human use
- EU Regulation (EC) No 726/2004 centralised authorisation procedure
- EU Regulation (EU) 2022/2371 on serious cross-border threats to health
- EU Official Control Authority Batch Release, required for every batch of every vaccine before it may be placed on the market
- EU Regulation (EU) No 536/2014 on clinical trials
- ICH E11(R1) clinical investigation of medicinal products in paediatric populations
- US Public Health Service Act section 351 biologics licence
- US National Childhood Vaccine Injury Act 1986, which created a no-fault compensation scheme in order to keep manufacturers in the market
- International Health Regulations (2005)
- National immunisation acts and school-entry requirements, which vary widely and are the point at which vaccination becomes a civil liberties question rather than a medical one

### Standards

- WHO prequalification, which has no legal force and nonetheless determines what United Nations agencies may purchase
- WHO Technical Report Series guidelines on vaccine quality, safety and efficacy
- WHO Vaccine Vial Monitor specification, a heat-sensitive label that tells a health worker whether a dose is still viable
- Ph. Eur. general monograph 0153 on vaccines for human use
- USP general chapters on biological products
- EU GMP Annex 1 manufacture of sterile medicinal products
- EU GMP Annex 2 biological medicinal products
- ISO 13408 aseptic processing of health care products
- WHO Performance, Quality and Safety prequalification for cold chain equipment
- ISO 21973 general requirements for transportation of biological material

### Related records

- `red.molecular_diagnostics`
- `red.antibody_engineering`
- `red.pharmaceutical_biotechnology`
- `green.veterinary_vaccines`
- `dark.biodefence_countermeasures`
- `dark.biosurveillance`
- `purple.clinical_trial_ethics`

### Cross-references

- [red.molecular_diagnostics](molecular_diagnostics.md)
- [red.antibody_engineering](antibody_engineering.md)
- [red.pharmaceutical_biotechnology](pharmaceutical_biotechnology.md)
- [green.veterinary_vaccines](../green/veterinary_vaccines.md)
- `dark.biodefence_countermeasures` (branch not written yet)
- `dark.biosurveillance` (branch not written yet)
- `purple.clinical_trial_ethics` (branch not written yet)
