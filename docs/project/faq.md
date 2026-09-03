<!--
  GENERATED FILE. Do not edit.
  Produced by tools/generate_docs.py from FAQ.md.
  Edit the source and run `make docs`.
-->

# Frequently asked questions

Honest answers, including to the awkward ones.

---

## About the colour scheme

### Is the colour scheme an official standard?

**No.** There is no ISO standard, no European directive and no learned society
that defines it. It grew out of European science-policy and
science-communication writing from the late 1990s onward and spread because it
was useful, not because anyone ratified it.

This library records the convention as it is actually taught and used. It does
not claim the convention is authoritative, and `Branch.origin_note` on each
branch says what is known about where that colour came from.

### Where did each colour come from?

Roughly, and with the caveat that attribution is uncertain:

| Colour | Origin |
|--------|--------|
| Red, green | The oldest pair. Entered wide use during the European debate over genetically modified food in the late 1990s, when the medical sector wanted its work considered separately from agriculture. Red for blood, green for plants. |
| White | Named by analogy with "white coat" industry; sometimes called grey in older literature, which is one reason the boundaries are confusing. |
| Blue | Marine, from the colour of the sea. |
| Yellow | Food and nutrition. Occasionally used for insect biotechnology in some sources - an outright conflict, noted in `FAQ` below. |
| Grey | Environmental. Also written "gray"; both resolve in this library. |
| Brown | Arid land and desert soils. |
| Gold | Bioinformatics, from the value of information. Sometimes extended to nanobiotechnology, which this library follows. |
| Dark | The harmful potential of the field. |
| Purple | Law, ethics and intellectual property. |

### Some sources say yellow is insect biotechnology. Which is right?

Both are in use, and that is a genuine conflict in the literature rather than
an error in one source.

This library follows the **food and nutrition** reading, because it is the
dominant usage in European teaching materials and because insect biotechnology
is covered adequately within `green.biopesticides` and
`yellow.alternative_proteins`. The choice is recorded here rather than hidden.

### Why exactly ten?

Because ten is the set that is actually taught. Sources exist with eight, with
twelve, and with a "violet" branch separate from purple. Ten is the most common
enumeration and the one this library documents.

### The boundaries overlap. Isn't that a flaw?

The overlaps are real and the library treats them as the interesting part
rather than as a defect.

An enzyme in a washing powder is white; the same enzyme in a cheese vat is
yellow; the algorithm that designed it is gold; the patent on it is purple. No
tree position is correct. That is why every record carries a `related` tuple of
cross-branch edges, and why `bt.related(path, depth=2)` exists.

---

## About the content

### Why is everything written twice?

Because the people who decide about biotechnology are mostly not
biotechnologists. Parliamentary committees, procurement officers, journalists,
teachers, patients and students shape what gets funded, approved, taught and
used - and they are routinely handed prose written for postdocs.

Writing the technical register only would exclude them. Writing the plain
register only would make the library useless to specialists. So every record
carries both, in full, and the validation suite rejects a record that leaves the
plain-language fields empty.

### Why must `why_it_matters` state a cost?

Because a record that lists only upside is advertising.

Editorial rule 3 in [`STYLE_GUIDE.md`](style-guide.md) requires the price, the
controversy, the access problem or the unresolved risk to appear alongside the
achievement. Gene therapy cures children *and* costs two million euro per
patient. Bt cotton cut insecticide use *and* concentrated seed supply into very
few companies. Both halves are true, and a reference work that omits the second
half is not neutral, it is promotional.

### Are the numbers reliable?

They carry an explicit evidence grade - `consensus`, `reviewed`, `reported` or
`indicative` - so you can see how much weight each one bears, and you can
filter to the settled material.

They are **orientation figures, not specifications**. Never use a `typical`
range to set a dose, a limit, a release criterion or a safety threshold. See
[`NOTICE.md`](https://github.com/olaflaitinen/biotechnology/blob/main/NOTICE.md) §6.

### Why is `typical` a string rather than two numbers?

Because almost every real range in biology is conditional. "1e11 to 2e14 vg/kg"
is meaningful only once you know the route of administration; storing it as a
numeric pair invites averaging, plotting and cross-condition comparison, all of
which are wrong. The string form forces the reader to read the note.

### The regulations are mostly European. Why?

Because those are the ones the maintainer can cite accurately.

This is a stated bias, written down in [`NOTICE.md`](https://github.com/olaflaitinen/biotechnology/blob/main/NOTICE.md) and
[`CONTRIBUTING.md`](contributing.md), not a hidden one. Adding coverage of other
jurisdictions is the most welcome kind of contribution, and a pull request that
adds two lines to one `REGULATIONS` tuple is complete and mergeable.

### Why are British spellings used?

Consistency, and the European institutional context. `colour`, `organisation`,
`litre`, `haemoglobin`. `Branch.color` exists as a US-spelling alias in the API
so that American code reads naturally.

---

## About the dark branch

### Why does a branch about bioweapons exist at all?

Because the colour scheme this library documents has ten branches and `dark` is
one of them. A taxonomy that silently omitted it would be an inaccurate
description of how the field is taught.

More substantively: the actual subject matter of the branch is containment
standards, oversight of risky research, gene synthesis screening, surveillance,
medical countermeasures, forensic attribution and treaty compliance. That is
exactly the material policy staff, journalists and students need in order to
argue about biosecurity, and it is poorly served by accessible sources.

### Does it contain anything dangerous?

No. It is documented exclusively from the protective side, and
`tests/test_dark_branch_is_defensive.py` enforces that on every commit.

Out of scope in every facet of every record: synthesis or acquisition routes,
enhancement of transmissibility or virulence, evasion of detection or
countermeasures, weaponisation or dissemination, target selection. See
[`SECURITY.md`](security.md) §2 for the full policy.

### What if I disagree with that policy?

The maintainers will not negotiate about it, and a stated purpose - research,
education, fiction, testing - does not change the outcome, because the
published text is identical either way. This is the one area of the project
explicitly exempted from consensus in [`GOVERNANCE.md`](governance.md) §3.4.

---

## About using the library

### Why no dependencies?

So that it can be imported inside teaching environments, air-gapped analysis
pipelines and regulatory review tooling where installing a dependency tree is
slow or prohibited. It is a hard constraint recorded in `pyproject.toml` and in
governance, not a preference.

The dataset is small enough that a full scan for search costs well under a
millisecond, so nothing is lost.

### Can I use this commercially?

Yes. The EUPL-1.2 permits commercial use.

It is a **copyleft** licence, so if you distribute a modified version or a
derivative work you must distribute it under the EUPL or a compatible licence
from its Appendix, and you must make the source available. Using the library
inside a service you host is not distribution. See [`NOTICE.md`](https://github.com/olaflaitinen/biotechnology/blob/main/NOTICE.md) §2,
and take your own legal advice - that section is a summary, not counsel.

### Why the EUPL rather than MIT or GPL?

Because the work was produced at a European public institution, the EUPL is the
licence drafted and published by the European Commission for exactly that
situation, and it is the only major open licence with equal legal force in
twenty-three languages. Its Appendix makes it compatible with GPL, AGPL, LGPL,
MPL, EPL, CeCILL, OSL and CC BY-SA, so it does not strand anyone.

### Is this a database of biotechnology companies or products?

No. It is a taxonomy of the **field**. Products are named only where a specific
approval is the historical fact being reported - the first recombinant
medicine, the first CAR-T product - and never as a catalogue.

### Can I use the formulas for real work?

For teaching, estimation and orientation, yes. For anything a decision depends
on, verify against the primary source cited in the formula's `derivation.py`.

The modules are **not validated software** under any medical device, in vitro
diagnostic, clinical laboratory or GxP framework, and must not be used as if
they were.

### How current is the data?

Every release records a **data freeze date** in
[`CHANGELOG.md`](changelog.md) - the date the factual and regulatory claims
were last verified. Nothing in the project claims currency beyond that date.
Law changes; check the official text.

---

## About contributing

### I am not a programmer. Can I still help?

Yes, and you are the contributor this project most needs. Factual corrections
and plain-language review are the top two priorities in
[`CONTRIBUTING.md`](contributing.md), and neither requires you to write code.
Open an issue with the record, the field, what it says, what it should say, and
a source.

### I found a mistake. How much detail do you want?

The record path (`red.gene_therapy`), the facet file (`metrics.py`), the field,
the current text, the corrected text, and a source. That is a complete report.

### Will you add my favourite subtype?

Possibly. Open an issue with an argument for why it is a distinct subtype rather
than a facet of an existing one, and which branch it belongs in. Scope changes
sit open for at least fourteen days before a decision, and a declined proposal
gets written reasons.

---

## About the project

### Who maintains this?

One person, named in [`GOVERNANCE.md`](governance.md). The bus factor is one,
that is a real risk for a work meant to be cited, and §6 of that document says
what is being done about it - starting with a copyleft licence that guarantees
anyone can fork and continue.

### How do I cite it?

Machine-readable metadata is in [`CITATION.cff`](https://github.com/olaflaitinen/biotechnology/blob/main/CITATION.cff); GitHub renders
a formatted citation from it in the sidebar. A BibTeX block is in the README.

### What is explicitly out of scope?

- Company, product or market databases.
- Investment, clinical, legal or regulatory advice.
- Predictions about which technologies will succeed.
- Advocacy for or against any contested technology.
- A third taxonomy level. Every proposed one turned out to be a
  cross-reference in disguise.

See [`ROADMAP.md`](roadmap.md) for what is planned and what has been ruled out.
