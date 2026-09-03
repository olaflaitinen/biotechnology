<!--
  GENERATED FILE. Do not edit.
  Produced from ROADMAP.md.
  Edit the source and run `make docs`.
-->

# Roadmap

What is planned, what is under consideration, and what has been ruled out.

Ruling things **out** in public is as useful as planning things in: it saves a
contributor from building something that will not be merged, and it forces the
maintainer to say why.

---

## Now - 0.1.x

Stabilisation of what exists. No new scope.

- [ ] Complete factual review pass over all eighty-five subtype records, facet
      by facet, against primary sources.
- [ ] Complete plain-language review pass by readers who are not scientists.
      This is the review most likely to change the text and the one hardest to
      obtain; see [`CONTRIBUTING.md`](contributing.md) §1.3.
- [ ] Formula test coverage to 100 % of branches, including every rejected
      input path.
- [ ] Documentation generator output reviewed page by page for dead links and
      mangled symbols.
- [ ] Continuous integration matrix green on Python 3.9 through 3.14, on
      Linux, macOS and Windows.

---

## Next - 0.2

### Coverage of jurisdictions beyond the European Union

The single most valuable improvement available. The `governance` facets
currently cite European instruments most completely, United States instruments
where they are the global reference, and others sparsely.

Target: at least three additional jurisdictions represented across every
subtype where the regulatory position materially differs - realistically the
United States, Japan and one of China, India or Brazil.

This does not require the maintainer. It requires contributors who can cite
their own regulator accurately, and a pull request adding two lines to one
`REGULATIONS` tuple is a complete contribution.

### Plain-language translation

The plain-language register is the one that benefits most from translation and
the one least well served by machine translation, because the analogies are
culturally specific. A fire drill and a sniffer dog do not travel equally well.

Under consideration: a `narrative_<lang>.py` facet, optional, with a fallback
to English and a marker in the API showing which registers are translated.
Finnish, Swedish, German, French, Spanish and Turkish are the plausible first
set. **Not started**, because a half-translated dataset that silently falls
back is worse than an honestly monolingual one, and solving that properly is a
design problem rather than a translation problem.

### Formula coverage

Extend the formula packages until every `Metric` in the taxonomy that *can* be
computed has a `formula` key that resolves. Currently a minority do.

### `bibliography` completeness

Every citation key resolved to a full reference with a DOI where one exists,
and a check in the integrity suite that no key resolves to a stub.

---

## Later - 0.3 and beyond

### Machine-readable exports for other ecosystems

- **JSON-LD** with a published vocabulary, so records can be referenced from
  linked-data systems.
- **SKOS** representation of the taxonomy, for library and archive systems that
  consume controlled vocabularies.
- **Frictionless Data** package descriptor for the tabular exports.

The `to_dict()` contract in [`DATA_MODEL.md`](../reference/data-model.md) §8 is already
stable enough to build these on.

### A citable versioned archive

Zenodo deposit with a DOI per release, so that a paper citing "version 0.4.2"
cites something immutable. `CITATION.cff` is already shaped for this.

### Teaching materials

Generated from the same source of truth rather than written separately:
one-page branch summaries, a printable colour-wheel poster, question banks
derived from `key_questions`, and a timeline rendering of `bt.timeline()` that
is genuinely a one-page history of applied biology.

### Uncertainty on metrics

Currently `EvidenceLevel` grades a claim but the range itself is opaque prose.
Under consideration: an optional structured interval alongside the string,
carrying its own conditions. Deliberately not done yet, for the reason in
[`FAQ.md`](faq.md) - a numeric pair invites exactly the misuse the string form
prevents. Any design must keep that property.

---

## Explicitly out of scope

These have been considered and rejected. Reopening one requires a new argument,
not a repeat of the old one.

### A third taxonomy level

Every proposed third level turned out to be a cross-reference in disguise. Two
levels are enforced by the grammar in `core/paths.py`, and the graph edges in
`linkage.py` carry what a third level would have.

### Company, product or market data

Not a database of who sells what. Products are named only where a specific
approval is the historical fact being reported. Market data ages in months,
would dominate maintenance, and is available commercially from people who do it
properly.

### Predictions

No "expected to reach market by", no technology-readiness forecasting, no
hype-cycle positioning. `Maturity` records where something **is**, evidenced.
Where something is going is an opinion, and this library does not hold
opinions.

### Advocacy

On genetically modified crops, gene editing in animals, cultivated meat,
gain-of-function oversight, patenting of living material: the project reports
what is established, reports what is disputed, and says who disputes it.
Records that argue a position are not merged, in either direction.

### Runtime dependencies

A hard constraint in `pyproject.toml` and in
[`GOVERNANCE.md`](governance.md) §3.3. A feature that cannot be built against
the standard library goes into an optional extra or a separate package.

### Generated source of truth

The facet files will not be generated from a compact specification. A domain
expert must be able to edit the file they are reading, and the comments - which
carry the editorial reasoning - cannot survive generation.

### Any relaxation of the dual-use policy

[`SECURITY.md`](security.md) §2 governs and is exempt from consensus. Not
subject to a roadmap item, a vote, or a persuasive argument about intent.

---

## How to influence this

Open an issue. Scope changes stay open at least fourteen days and receive
written reasons either way, per [`GOVERNANCE.md`](governance.md) §2.

The fastest way to move something up this list is to do part of it. A pull
request adding one jurisdiction's regulations to ten subtypes demonstrates more
than an issue arguing that jurisdictional coverage matters.
