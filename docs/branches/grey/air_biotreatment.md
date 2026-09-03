<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from src/biotechnology/branches/grey/air_biotreatment/.
  Edit the source and run `make docs`.
-->

[Grey Biotechnology](index.md) / **Air Biotreatment**

## Air Biotreatment

`grey.air_biotreatment`

Treating contaminated air by passing it through a wet biofilm, where the limit is what will dissolve rather than what the organisms will degrade.

### What it is

Biological air treatment removes contaminants from gas streams by passing them through a bed carrying a microbial biofilm. The organisms are not airborne. They live in a thin film of water on a packing material, and a contaminant becomes available to them only after it has partitioned out of the gas phase and dissolved into that film. The consequence governs the whole field: the binding constraint is solubility rather than biodegradability. Hydrogen sulphide, ammonia, alcohols, aldehydes and many organic acids partition readily and are treated efficiently. Poorly soluble compounds, including many chlorinated solvents and higher hydrocarbons, pass through a perfectly healthy bed largely untouched, because they never reach the phase in which the organisms are working. This is the same bioavailability argument made in `grey.bioremediation` about contaminant sorbed into soil, reaching this record through gas-liquid partitioning instead. Three configurations exist and they differ in how the water is handled. A biofilter uses an organic packing such as compost, bark or peat, kept damp, with the biofilm growing on the packing itself; it is the simplest and cheapest arrangement and it has no separate liquid phase to control. A biotrickling filter uses an inert packing with liquid recirculated over it, which allows pH and nutrients to be controlled and acidic degradation products to be washed out, and is therefore what hydrogen sulphide treatment generally uses. A bioscrubber separates the two steps entirely, absorbing the contaminant into liquid in one vessel and degrading it in a separate bioreactor, which gives the most control and costs the most. The comparison is with thermal or catalytic oxidation, which destroys essentially any organic compound and requires heating a gas stream that is almost entirely nitrogen. Biological treatment runs at ambient temperature and consumes little more than the fan power to move the air. The trade is therefore concentration and flow: for large volumes of weakly contaminated air, biology is far cheaper; at higher concentrations the biofilm cannot keep pace, the bed acidifies or dries, and combustion becomes the correct answer. Residence times are seconds, which is what makes treating very large air volumes practical at all. In deployment, most of this is odour control at wastewater works, composting and digestion facilities, rendering plants and intensive livestock housing. That matters for how success is judged. The driver is usually a neighbour's complaint rather than a measured exposure, the target is a detection threshold rather than a concentration limit, and compliance is assessed by trained human panels smelling diluted samples. A plant can therefore meet every chemical specification and still fail, because the compounds that offend a nose do so at concentrations far below anything an instrument was asked to find.

### In plain language

Smelly or polluted air from a factory or sewage works can be cleaned by blowing it slowly through a damp bed of bark, compost or plastic packing covered in bacteria. The bacteria are not in the air; they are in a thin layer of water on the packing, so the pollutant first has to dissolve into that water before anything can eat it. That is the catch: things that dissolve easily, like the rotten-egg smell of hydrogen sulphide, are removed very well, and things that do not dissolve pass straight through no matter how healthy the bacteria are. The alternative is burning the air clean, which works on anything and costs fuel to heat a great deal of air that was mostly harmless. So biology wins when there is a lot of air and not much pollution in it, which is most of the time. Whether it has worked is usually judged by people smelling samples, because the complaint that started it came from a neighbour.

### An analogy

It is brewing rather than filtering. A filter catches what is too big to pass; a brew extracts only what the water will take up, and whatever is insoluble stays in the leaf however long it steeps. These beds work the second way. The air is not strained, it is washed, and a compound that will not dissolve is not washed out of it. Steeping longer, which is to say building a bigger bed, does not change that.

### Why it matters

Odour is the commonest cause of complaint against waste and food processing facilities, and it determines whether such a facility can be sited near where people live. That is not a trivial matter: a wastewater works, a composting site or a digester has to be near the population it serves, and effective odour control is frequently the condition on which planning permission rests. This record is therefore what allows a great deal of `grey.wastewater_treatment` and `grey.biowaste_treatment` to exist in the places they need to be. The energy argument is real as well. Treating large volumes of weakly contaminated air thermally means heating mostly nitrogen, and doing it biologically means running a fan. For the flows involved that difference is substantial, and it is one of the few places where the biological option is cheaper on energy by an order of magnitude rather than by a margin. Hydrogen sulphide removal has a specific value beyond odour, since it is toxic and corrosive and destroys the gas engines that digester biogas is meant to run. The limits are firm. Poorly soluble compounds are outside the technique rather than treated slowly by it. Beds are large, because seconds of residence time at high flow still means a substantial volume, and land near a plant is not free. Compost and bark packing compacts and channels over a few years and has to be replaced, which is a recurring cost that proposals tend to omit. The community is slow to recover from drying out or from an interruption in the air supply, so a plant that stops for maintenance may smell for weeks afterwards. Acidic products from sulphur and chlorine compounds accumulate and kill the biofilm unless they are washed out. And there is an honest limitation on the objective itself: odour is measured against a human detection threshold, which varies between people and is not a health-based standard, so a plant can be compliant and still be a genuine nuisance to the person living nearest.

### Applications

- Odour control at wastewater treatment works, covering inlet works, sludge handling and storage, which is the single commonest installation and is frequently a planning condition rather than an environmental one
- Odour control at composting and anaerobic digestion facilities, which is what allows `grey.biowaste_treatment` plants to be sited near the populations whose waste they take
- Rendering, fish processing and food factory exhaust treatment, where the offending compounds are amines, sulphides and aldehydes at very low concentration
- Intensive livestock housing ventilation treatment, which handles ammonia and odour together and is driven by both neighbour complaint and nitrogen deposition rules
- Landfill working face and waste transfer station air treatment
- Hydrogen sulphide removal from digester biogas, which is done because the gas is toxic and corrosive and destroys the engines the biogas is meant to run, so the driver is asset protection rather than emission
- Hydrogen sulphide treatment in sewer ventilation, which also addresses the concrete corrosion that the same chemistry causes in the pipe itself
- Ammonia removal from livestock and composting exhaust, which is regulated as an air quality and nitrogen deposition matter and not only as an odour
- Biological desulphurisation of biogas by controlled micro-aeration, which achieves the same result inside the digester headspace without a separate vessel
- Treatment of alcohol, ketone and ester vapours from printing, coating and painting operations, which are soluble enough for the technique to work well
- Styrene and toluene removal from composites and plastics manufacturing, which sits at the boundary of what partitions adequately
- Volatile organic compound treatment at pharmaceutical and chemical plants where the compound is soluble and the concentration is low
- Soil vapour extraction off-gas treatment, which pairs this record directly with `grey.bioremediation` by treating what the remediation strips out of the ground
- Methane oxidation in landfill biocovers, where methanotrophs in an engineered soil layer oxidise gas escaping the cap, which works at low flux and cannot handle a concentrated stream
- Dilute methane treatment from livestock and mine ventilation air, which is recorded as a research area rather than an established application, since methane is poorly soluble and very dilute in exactly these streams, which is the worst combination for this technique
- Chlorinated solvent vapour treatment, which is included with the same qualification: the compounds partition poorly and the degradation produces acid that damages the bed

### Technologies

- Biofilters on organic packing such as compost, bark, peat or wood chip, where the biofilm grows on the packing itself and there is no separate liquid phase to manage, which is the simplest and cheapest arrangement
- Biotrickling filters on inert packing with recirculated liquid, which permits pH and nutrient control and washes out acidic products, and is therefore what sulphide treatment generally uses
- Bioscrubbers, which absorb the contaminant into liquid in one vessel and degrade it in a separate bioreactor, giving the most control at the highest cost
- Membrane and two-phase partitioning bioreactors, which introduce an additional phase to improve the transfer of poorly soluble compounds and are the main line of attack on this record's central limitation
- Packing material selection for surface area, void fraction and water retention, which sets both the transfer area and the pressure drop the fan must overcome
- Structured and engineered media, which resist the compaction and channelling that eventually ruins an organic bed
- Gas distribution design, since a bed with a preferential path treats only the fraction of air that goes the long way
- Humidification of the incoming air, which is not optional: an unhumidified stream dries the bed out from the inlet end and the biofilm dies there first
- Irrigation and moisture control, which is the commonest cause of both success and failure and is what most operator attention goes to
- pH control and neutralisation, required wherever sulphur or chlorine compounds are degraded, since the products are acids that will kill the biofilm that made them
- Nutrient dosing of nitrogen and phosphorus in the recirculating liquid, which the air stream itself does not supply
- Backwashing and biomass control, since excess growth blocks the void space and raises the pressure drop until the fan cannot deliver the flow
- Media replacement scheduling for organic packings, which compact and degrade over a few years and are a recurring capital cost that proposals commonly omit
- Startup and reacclimation practice after a shutdown, since a bed recovers over weeks rather than hours and a maintenance outage has an odour consequence afterwards
- Dynamic olfactometry with trained human panels, which is the reference method for odour and is the acceptance criterion that actually matters
- Electronic nose and continuous sulphide instrumentation, which give a signal between panel assessments
- Inlet and outlet speciation by gas chromatography and mass spectrometry, which distinguishes what was removed from what was merely diluted

### Challenges

- Poor solubility, which places compounds outside the method rather than making them slow within it, since a contaminant that will not partition into the water film is never presented to the organisms at all
- Very short gas residence times, measured in seconds, which leaves little opportunity for a slowly partitioning compound to transfer
- Low and variable inlet concentration, which can be insufficient to sustain the biomass that a subsequent peak load requires
- Drying of the bed, which kills the biofilm from the inlet end and is the commonest operational failure, and which is why incoming air must be humidified
- Acidification from sulphur and chlorine compound degradation, where the products destroy the community that produced them unless they are washed out
- Compaction and channelling in organic packings, which lets air bypass most of the bed while the instrumentation still reports flow
- Excess biomass growth blocking void space and raising pressure drop until the fan can no longer deliver the design flow
- Slow recovery after shutdown or shock loading, over weeks rather than hours, so a maintenance outage produces an odour problem after it ends
- Footprint, since seconds of residence at high flow is still a large volume, and land adjacent to a treatment works is rarely available
- Media replacement every few years for organic packings, which is a recurring cost routinely omitted from comparisons against thermal treatment
- Fan power against pressure drop, which is the whole of the running cost and rises as the bed ages
- Odour measurement resting on human detection thresholds, which vary between people, are not health-based, and mean a compliant plant can still be a genuine nuisance to the nearest resident
- Compounds offensive far below instrumental detection limits, so a plant can satisfy every chemical specification and fail a panel
- Distinguishing removal from dilution where treated and untreated streams combine before the stack
- Bioaerosol emission from the beds themselves, particularly from organic packings, which is a treatment introducing its own emission

### Metrics

| Metric | Symbol | Unit | Typical | Evidence |
|---|---|---|---|---|
| Henry's law constant | `H` | dimensionless gas to liquid partition ratio | low for hydrogen sulphide, ammonia and alcohols, which are treatable; high for methane and chlorinated solvents, which are not | CONSENSUS |
| Empty bed residence time | `EBRT` | seconds | seconds, which is what makes treating very large air volumes practical | CONSENSUS |
| Elimination capacity | `EC` | grams of contaminant destroyed per cubic metre of bed per hour | compound specific, and highest for readily soluble compounds such as hydrogen sulphide | CONSENSUS |
| Removal efficiency | `eta` | per cent of inlet load removed | high for soluble compounds; poor for compounds with an unfavourable partition ratio regardless of bed condition | CONSENSUS |
| Critical load | `L_crit` | grams per cubic metre of bed per hour at which removal begins to fall | the design ceiling, and the point at which thermal treatment becomes the correct choice | REVIEWED |
| Odour concentration | `c_od` | European odour units per cubic metre | expressed as the dilution at which half a trained panel can just detect the sample | CONSENSUS |
| Hedonic tone and odour annoyance | `H_tone` | qualitative scale from pleasant to unpleasant, assessed by panel | assessed alongside concentration where a complaint has been made | REPORTED |
| Bed moisture content | `w_bed` | per cent by mass | a narrow window, below which the biofilm dies and above which the bed becomes anaerobic and blocks | CONSENSUS |
| Pressure drop across the bed | `dP` | pascals | rises over the life of the packing as it compacts and biomass accumulates | CONSENSUS |
| Bed pH | `pH` | dimensionless | falls where sulphur or chlorine compounds are degraded, unless the products are washed out | CONSENSUS |
| Media service life | `t_media` | years | a few years for organic packings, considerably longer for structured inert media | REPORTED |
| Energy consumption per volume of air treated | `E_air` | kilowatt hours per thousand cubic metres | far below thermal oxidation for dilute streams, since only fan power is required | REPORTED |

### History

- **1923** - Soil beds are used to treat odorous air from sewage installations
- **1955** - Open soil biofilters are installed at wastewater and rendering sites
- **1970** - Engineered biofilters on compost and bark packing are developed in parallel in several countries
- **1980** - Humidification of the incoming air is established as a requirement rather than an option
- **1985** - Biotrickling filters with recirculated liquid enter use for hydrogen sulphide
- **1990** - Air emission legislation extends to odour and volatile organic compounds at waste facilities
- **1995** - Extension to chlorinated and poorly soluble solvents fails, and the cause is identified as partitioning rather than degradation
- **2000** - Two-phase partitioning bioreactors are developed to carry poorly soluble compounds into the aqueous phase
- **2003** - Dynamic olfactometry is standardised, giving odour a reproducible measurement
- **2008** - Landfill biocovers using methanotrophic soil layers are demonstrated at field scale
- **2012** - Biological desulphurisation is integrated into biogas plants by controlled micro-aeration
- **2018** - Bioaerosol emission from biofilter media is recognised as an exposure concern in its own right

### Governance

| Field | Value |
|---|---|
| Maturity | ESTABLISHED |
| Risk tier | CONTROLLED |
| Scale | INDUSTRIAL |
| Regulatory status | NOTIFIED |
| Domains | ENVIRONMENT, HEALTH |
| SDGs | 3, 11, 12 |

### Regulations

- Planning permission conditions requiring odour abatement, which are typically the reason a plant is installed and which are imposed before construction by an authority weighing neighbours against infrastructure
- Odour management plan requirements attached to permits at waste, composting and wastewater facilities, which specify complaint procedures as well as abatement
- Statutory nuisance provisions, under which persistent odour is actionable independently of whether an emission limit was met
- Separation distance and buffer zone requirements between odour-generating facilities and residential areas
- The Industrial Emissions Directive 2010/75/EU and equivalent regimes, which set permit conditions and require best available techniques for the installations this record serves
- Best available techniques reference documents for waste treatment, which name biological air treatment as an accepted technique and describe the performance expected of it
- National air quality legislation setting limits for ammonia, hydrogen sulphide and volatile organic compounds
- Solvent emissions requirements for coating, printing and cleaning operations, which are what drive the solvent vapour applications
- Ammonia emission ceilings and nitrogen deposition rules under the National Emission Ceilings Directive 2016/2284 and habitats protection, which apply to livestock housing and composting
- Occupational exposure limits for hydrogen sulphide, ammonia and solvent vapours, which govern the workplace inside the fenceline rather than the emission beyond it
- Gas quality requirements for biogas use, which are why sulphide removal is performed to protect engines as well as to satisfy an emission limit
- Bioaerosol assessment requirements at composting and waste facilities, which apply to the abatement media themselves and make the treatment plant a regulated source in its own right
- Waste classification and disposal requirements for spent biofilter media, which is a waste stream generated every few years by an installation whose purpose is emission control
- General duty of care and environmental permitting compliance obligations, including monitoring, record keeping and reporting against the conditions above

### Standards

- EN 13725 dynamic olfactometry, which defines the odour unit through a standardised procedure with trained panels and is what allowed odour to be written into permits as a number at all
- Panel selection, screening and calibration practice against reference gases, which is what makes a human measurement reproducible between laboratories
- Odour sampling conventions for stacks and area sources, including bag material selection, since several relevant compounds are lost to the sample container itself
- Hedonic tone and annoyance assessment methods, which capture the fact that equal odour concentrations from different sources produce very different complaint rates
- Dispersion modelling conventions for odour impact assessment, which is how a stack concentration is translated into an expected exposure at a dwelling
- Empty bed residence time and elimination capacity reporting conventions, which are what make performance figures comparable between installations
- Packing material specification for surface area, void fraction, water retention and structural durability
- Air humidification and pretreatment design guidance, which addresses the commonest cause of bed failure
- Pressure drop measurement and fan sizing practice, since fan power is the whole of the running cost
- Moisture, pH and nutrient monitoring practice for operating beds
- Startup, acclimation and post-shutdown recovery procedures, which matter because a bed recovers over weeks and an outage has an odour consequence after it ends
- Media replacement and disposal scheduling for organic packings, which is a recurring cost commonly omitted from comparisons with thermal treatment
- Speciated inlet and outlet analysis by gas chromatography and mass spectrometry, which distinguishes genuine removal from dilution where streams combine before the stack
- Continuous instrumentation calibration practice for sulphide and volatile organic compound monitors
- Bioaerosol sampling and enumeration methods, which apply to the treatment media as a source

### Related records

- `grey.wastewater_treatment`
- `grey.biowaste_treatment`
- `grey.bioremediation`
- `white.bioprocess_engineering`
- `grey.bioaugmentation`
- `grey.environmental_biomonitoring`

### Cross-references

- [grey.wastewater_treatment](wastewater_treatment.md)
- [grey.biowaste_treatment](biowaste_treatment.md)
- [grey.bioremediation](bioremediation.md)
- [white.bioprocess_engineering](../white/bioprocess_engineering.md)
- [grey.bioaugmentation](bioaugmentation.md)
- [grey.environmental_biomonitoring](environmental_biomonitoring.md)
