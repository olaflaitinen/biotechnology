<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from the taxonomy.
  Edit the source and run `make docs`.
-->

# biotechnology

A machine-readable taxonomy of the ten colour-coded branches of biotechnology and their subtypes, with zero runtime dependencies.

> **Coverage.** 6 of 10 branches are written, holding 51 records. Still to come: brown, gold, dark, purple. Cross-references into those branches resolve to nothing until they land, and the validator reports them as forward references rather than as errors.


## The branches

| Colour | Branch | Records | Covers |
|---|---|---:|---|
| `red` | [Red Biotechnology](branches/red/index.md) | 8 | Medicine, health care and pharmaceutical applications. |
| `green` | [Green Biotechnology](branches/green/index.md) | 8 | Agriculture, livestock and crop production. |
| `white` | [White Biotechnology](branches/white/index.md) | 9 | Industrial processes, biofuels, biomaterials and biobased chemicals. |
| `blue` | [Blue Biotechnology](branches/blue/index.md) | 8 | Marine and aquatic organisms as sources of medicines, materials, enzymes and food. |
| `yellow` | [Yellow Biotechnology](branches/yellow/index.md) | 9 | Food production, fermentation, nutrition and the safety of what people eat. |
| `grey` | [Grey Biotechnology](branches/grey/index.md) | 9 | Environmental cleanup, waste treatment, monitoring and the biological maintenance of ecological balance. |
| `brown` | *not written yet* | 0 | |
| `gold` | *not written yet* | 0 | |
| `dark` | *not written yet* | 0 | |
| `purple` | *not written yet* | 0 | |

## At a glance

| | |
|---|---:|
| Branches written | 6 of 10 |
| Records | 51 |
| Applications listed | 765 |
| Cross-references | 336 |
| Runtime dependencies | 0 |

## Getting started

```python
import biotechnology as bt

bt.get("grey.biomining").summary
bt.search("fermentation", limit=5)
bt.by_sdg(6)
```

```
biotechnology list
biotechnology show grey.biomining --plain
biotechnology export --format csv -o taxonomy.csv
```

See the [guide](guide/getting-started.md).
