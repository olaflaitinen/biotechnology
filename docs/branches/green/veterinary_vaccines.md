<!--
  GENERATED FILE. Do not edit.
  Produced from src/biotechnology/branches/green/veterinary_vaccines/.
  Edit the source and run `make docs`.
-->

[Green Biotechnology](index.md) / **Veterinary Vaccines and Animal Health**

## Veterinary Vaccines and Animal Health

`green.veterinary_vaccines`

Vaccines, diagnostics and therapeutics for farm and companion animals, central to controlling zoonoses and reducing antibiotic use.

### What it is

Veterinary vaccinology shares its platform technologies with human vaccinology and operates under entirely different constraints. Cost per dose is measured in cents rather than euro. Administration must work on thousands of animals an hour, which favours drinking water, spray, in-ovo and needle-free routes over individual injection. And the endpoint is usually transmission control across a herd or flock rather than protection of an individual, so a vaccine that reduces shedding without preventing infection can still be exactly what is wanted. One requirement has no human equivalent and shapes the whole field. A country with disease-free trading status loses it if its animals test positive, and a conventional vaccine makes vaccinated animals indistinguishable from infected ones. DIVA vaccines, meaning differentiating infected from vaccinated animals, solve this by deleting a non-essential antigen from the vaccine strain and testing for antibodies against it. Vaccinated animals lack that response; infected ones have it. This is a technical solution to a trade problem, and without it many countries would rather cull than vaccinate. Beyond vaccines the field covers herd-level molecular diagnostics, autogenous vaccines made from an isolate taken on the affected farm, parasite control, and the alternatives to antibiotic growth promoters that have displaced routine medication across Europe. The binding constraint is economic rather than immunological. A product must be developed, licensed and manufactured for a market that will pay a few cents a dose, and the diseases with the greatest global burden are concentrated in the countries least able to pay. Technical feasibility is rarely what decides whether a veterinary vaccine exists.

### In plain language

Farm animals are vaccinated for the same reason children are: it is cheaper and kinder to prevent an illness than to treat it. There are two extra reasons on a farm. First, a sick herd is a food supply problem, not only an animal problem. Second, most new human diseases start in animals, so stopping an infection in a poultry shed can stop it ever reaching people. Vaccinating animals also means fewer antibiotics are used, and that matters to everyone, because the more antibiotics are used anywhere the faster bacteria learn to survive them.

### An analogy

It is fitting smoke detectors in every flat of a building rather than only in your own. The fire that never starts next door is the one that never spreads to you. The comparison carries the awkward part too: most of the benefit goes to neighbours who paid nothing, which is precisely why somebody has to organise it collectively and why individual farmers cannot be expected to fund it alone.

### Why it matters

Rinderpest, a cattle disease that caused famines across Africa and Asia for centuries, was eradicated in 2011 by vaccination. It is the second disease of any species ever eradicated, and the first was smallpox. Avian influenza control in poultry is the front line against a virus with pandemic potential in humans. And veterinary antimicrobial use, which in some countries once exceeded human use by weight, has more than halved across the European Union since 2011, largely because vaccination and better husbandry replaced routine medication. The costs are structural. Trade rules in several disease categories penalise vaccination by removing disease-free status, so countries cull healthy animals rather than vaccinate them, which is expensive, wasteful and hard to defend on welfare grounds. Cold chains fail first in the places with the highest disease burden. Wildlife reservoirs cannot be reached by any vaccination programme aimed at livestock. And because the benefit is largely a public good captured by people who did not pay for it, the field is systematically underfunded relative to what it prevents.

### Applications

- Newcastle disease vaccination by drinking water and coarse spray, which is how tens of billions of birds are vaccinated each year
- Marek's disease vaccination in ovo at day eighteen of incubation, before the chick has hatched
- Clostridial and respiratory vaccination in cattle and sheep
- Fish vaccines delivered by immersion or by automated injection in salmon aquaculture, which largely eliminated antibiotic use in that industry
- Autogenous vaccines produced from an isolate taken on the affected farm, for pathogens too variable for a commercial product
- Foot-and-mouth disease vaccination and strategic antigen banks held against an incursion
- Classical swine fever and porcine reproductive and respiratory syndrome control programmes
- Bluetongue vaccination campaigns following vector range expansion
- Avian influenza vaccination in poultry, the front line against a virus with pandemic potential in humans
- Oral rabies vaccination of wild foxes and raccoon dogs by aerial bait distribution, which eliminated fox rabies from western Europe
- Brucellosis and anthrax vaccination in livestock, both of which are principally human disease control measures
- Rift Valley fever and Japanese encephalitis vaccination in animal reservoirs
- Vaccination programmes deployed explicitly to replace routine antibiotic medication in intensive pig and poultry production
- Core companion animal vaccination against rabies, parvovirus and distemper

### Technologies

- DIVA vaccine design by deletion of a non-essential antigen, paired with a companion serological test for antibodies against it
- Marker vaccines based on subunit antigens that provoke a narrower response than infection does
- Live attenuated vaccines, attenuated by passage or by rational gene deletion
- Inactivated whole-organism vaccines in oil-adjuvanted emulsions, which are cheap and give long duration at the cost of injection-site reaction
- Herpesvirus of turkeys vectored constructs, which express antigens from other pathogens and can be given in ovo
- Recombinant subunit and virus-like particle vaccines
- Reverse vaccinology from pathogen genomes
- In-ovo injection at day eighteen, automated at tens of thousands of eggs per hour
- Drinking water and coarse spray mass administration
- Immersion vaccination for fish, and automated injection lines
- Oral bait formulation for wildlife, dropped from aircraft over defined grids
- Needle-free transdermal injectors, which also remove broken-needle risk in the food chain
- Thermostable and freeze-dried formulation for distribution without a cold chain
- Multivalent combination products, since each additional handling of an animal costs more than the vaccine
- Herd-level pooled PCR and serological surveillance
- Sequence-based strain matching to select the vaccine antigen against circulating field strains

### Challenges

- Antigenic variability in foot-and-mouth disease and avian influenza, which requires strain matching and antigen banks rather than a single product
- Wildlife reservoirs that no livestock vaccination programme can reach, so control succeeds in the farmed population and the pathogen persists
- Trade rules that remove disease-free status from a vaccinating country, so healthy animals are culled rather than vaccinated. DIVA vaccines exist to solve exactly this, and adoption still lags the technology
- Extreme price sensitivity, with a development and licensing cost that must be recovered at a few cents per dose
- A benefit that is largely a public good captured by people who did not pay for it, which leaves the field structurally underfunded relative to what it prevents
- Cold chain and delivery to extensive and smallholder systems, which fail first in exactly the regions with the highest disease burden
- Fragmented national approval, so a product licensed in one country must be re-registered in the next, at a cost the market frequently cannot repay
- Weak surveillance in many of the places where zoonotic spillover is most likely, so an outbreak is often detected in people before it is detected in animals

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Reproduction number under vaccination | `R_v` | secondary cases per case, dimensionless | target below 1 | CONSENSUS |
| Reduction in pathogen shedding | `dShed` | log10 reduction in organisms excreted | 1 - 4 log10 reduction | REVIEWED |
| Vaccine efficacy in the herd | `VE` | per cent reduction in risk relative to unvaccinated controls | 60 - 95 % against clinical disease | REVIEWED |
| Vaccination coverage | `V_cov` | per cent of the herd, flock or target population vaccinated | above 80 % for transmission control | CONSENSUS |
| Haemagglutination inhibition titre | `log2 HI` | log2 reciprocal titre | protective threshold around 4 to 5 log2 | CONSENSUS |
| DIVA test specificity | `Sp_DIVA` | per cent of vaccinated animals correctly identified as uninfected | above 99 % required for trade purposes | REVIEWED |
| Defined daily dose for animals | `DDDvet` | milligrams of active substance per population correction unit | the standard European benchmark; sales more than halved since 2011 | REVIEWED |
| Cost per dose | `C_dose` | euro cents per dose | 1 - 50 cents for poultry, higher for cattle and fish | REVIEWED |
| Duration of immunity | `DOI` | months of demonstrated protection | 6 months to lifetime, depending on platform and species | REVIEWED |

### History

- **1879** - Pasteur produces the first deliberately attenuated vaccine, against fowl cholera
- **1881** - Pasteur demonstrates anthrax vaccination publicly at Pouilly-le-Fort
- **1950** - Live attenuated Newcastle disease vaccines are developed for mass administration
- **1960** - A thermostable rinderpest vaccine is developed
- **1970** - In-ovo vaccination against Marek's disease is introduced
- **1978** - Oral rabies vaccination of wild foxes begins in Switzerland
- **1992** - DIVA marker vaccine concepts are introduced for pseudorabies
- **2001** - The United Kingdom foot-and-mouth disease epidemic is controlled by culling rather than vaccination
- **2003** - Avian influenza H7N7 in the Netherlands infects 89 people and kills a veterinarian during a poultry cull
- **2006** - The European Union bans antibiotic growth promoters
- **2011** - Rinderpest is declared globally eradicated
- **2022** - EU veterinary antimicrobial sales are reported to have more than halved since 2011

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | REGULATED |
| Scale | POPULATION |
| Regulatory status | AUTHORISED |
| Domains | FOOD, HEALTH, ENVIRONMENT |
| SDGs | 1, 2, 3, 17 |

### Regulations

- Regulation (EU) 2019/6 on veterinary medicinal products, the legal basis for authorisation, manufacture, distribution and pharmacovigilance, deliberately separate from the human medicines code
- Regulation (EU) 2019/4 on medicated feed, which governs the route by which routine antibiotic medication was historically delivered
- United States Virus-Serum-Toxin Act, under which veterinary biologics are licensed by the Department of Agriculture rather than by the Food and Drug Administration
- Regulation (EC) No 470/2009 and the maximum residue limits established under it, which set the withdrawal period before a treated animal may enter the food chain
- Regulation (EU) 2016/429, the Animal Health Law, which sets out categorised diseases and the powers to require vaccination, movement restriction or culling
- Directive 2010/63/EU on the protection of animals used for scientific purposes, which governs the challenge studies on which efficacy claims rest
- Council Regulation (EC) No 1099/2009 on the protection of animals at the time of killing, which applies to the culling that vaccination is intended to avoid
- National high-containment requirements for work with foot-and-mouth disease and other high-consequence animal pathogens, including seed virus handling

### Standards

- World Organisation for Animal Health Terrestrial Animal Health Code, which defines disease-free status, the conditions under which vaccination is compatible with it, and the surveillance required to demonstrate freedom
- World Organisation for Animal Health Manual of Diagnostic Tests and Vaccines for Terrestrial Animals, which prescribes the reference methods and potency tests
- European Pharmacopoeia monographs for veterinary vaccines, including batch potency and safety requirements
- Veterinary International Conference on Harmonisation guidelines, the veterinary counterpart of ICH
- Good Manufacturing Practice as applied to veterinary immunologicals
- World Organisation for Animal Health WAHIS notification requirements for listed diseases
- European Surveillance of Veterinary Antimicrobial Consumption reporting, which produced the halving figure recorded in `history.py`
- ISO/IEC 17025 accreditation for the diagnostic laboratories that perform DIVA and surveillance testing
- The tripartite One Health framework of the World Health Organization, the World Organisation for Animal Health and the Food and Agriculture Organization, under which animal vaccination is treated as a human health measure

### Related records

- `red.vaccine_development`
- `red.molecular_diagnostics`
- `green.animal_biotechnology`
- `red.pharmaceutical_biotechnology`
- `dark.biosecurity`
- `purple.bioethics`

### Cross-references

- [red.vaccine_development](../red/vaccine_development.md)
- [red.molecular_diagnostics](../red/molecular_diagnostics.md)
- [green.animal_biotechnology](animal_biotechnology.md)
- [red.pharmaceutical_biotechnology](../red/pharmaceutical_biotechnology.md)
- `dark.biosecurity` (branch not written yet)
- `purple.bioethics` (branch not written yet)
