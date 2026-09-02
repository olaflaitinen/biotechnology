# Style guide

The editorial rules every record in this library must satisfy.

This document is normative. `tests/test_editorial.py` enforces the parts that
can be checked mechanically; the rest is enforced in review. If you are writing
or correcting a record, read section 2 before you start.

---

## 1. The two registers

Every subtype is described **twice**, in full, in two registers that serve
different readers.

### 1.1 Technical register - `SUMMARY`, `DESCRIPTION`

Written for a reader who already has the vocabulary. Assume an undergraduate
life-science education. Dense, exact, no hedging, no marketing.

**`SUMMARY`** - one sentence, hard limit 200 characters. It appears in every
index, table, search result and CLI listing, so it must stand alone with no
surrounding context.

**`DESCRIPTION`** - three to eight sentences. The recommended structure, used
throughout the library:

1. a definition that fixes the **boundary** of the field;
2. the **strategies or sub-approaches** that exist inside that boundary;
3. how the thing is **actually done** in practice;
4. the **constraint** that shapes everything else.

Step 4 is the one that distinguishes a good record from an encyclopaedia entry.
Every field has one binding constraint - for gene therapy it is delivery, for
cell therapy it is manufacturing time, for biopesticides it is host range - and
naming it explains more than another paragraph of description would.

### 1.2 Public register - `PLAIN_LANGUAGE`, `ANALOGY`, `WHY_IT_MATTERS`

Written for a reader with **no scientific training at all**: a journalist, a
policy adviser, a patient, a school student, a procurement officer.

These fields are not decoration and they are not optional. The validation suite
rejects a subtype that leaves them empty, because a half-explained record is
worse than no record: it looks authoritative while excluding most of the people
who need it.

---

## 2. The rules

### Rule 1 - No unexplained jargon in `PLAIN_LANGUAGE`

Permitted without explanation: *DNA*, *gene*, *cell*, *virus*, *bacteria*,
*protein*, *immune system*, *vaccine*, *enzyme*.

Not permitted without explanation: *vector*, *episomal*, *transduction*,
*capsid*, *titre*, *allele*, *substrate*, *in vitro*, *phenotype*, *plasmid*,
*expression*, and everything like them.

The test: could this paragraph appear in a general newspaper without a glossary?

### Rule 2 - `ANALOGY` must be checkable, and must show its own limits

The reader should be able to see where the analogy breaks down, and the text
must not depend on it not breaking down.

> **Good.** "It slips a clean copy of that one page into the manual ... The hard
> part is not printing the page - it is getting it into every relevant manual in
> a building with several trillion rooms."
> The limit is stated in the analogy itself.

> **Bad.** "Gene therapy is like rebooting a computer."
> Wrong in kind, and gives the reader a false model they will reason from.

Draw from ordinary life: bread, hedges, sniffer dogs, fire drills, couriers,
police forces, photocopiers. Not from other technical fields.

### Rule 3 - `WHY_IT_MATTERS` must state the cost as well as the benefit

A record that lists only upside is advertising, and this library is not
advertising. Every `WHY_IT_MATTERS` must name the price, the controversy, the
access problem or the unresolved risk in the same breath as the achievement.

Where a field's benefits and harms are genuinely contested, say all of it:

> "Bt cotton cut insecticide applications ... Against that, the technology
> concentrated seed supply into very few companies, herbicide-tolerant systems
> selected for resistant weeds, and public trust in Europe never recovered from
> the way the first products were introduced. All four statements are true
> simultaneously."

### Rule 4 - `DESCRIPTION` reports what the field does, not what it hopes to do

Aspiration belongs in `practice.CHALLENGES`, phrased as the obstacle standing
in the way. "Will enable personalised treatment of all cancers" is not a
description; "poor efficacy so far in solid tumours" is.

### Rule 5 - No number in prose that is not also in `metrics.py`

If `DESCRIPTION` or `WHY_IT_MATTERS` states a figure, that figure must also
appear as a `Metric` with a unit and an evidence grade, or be an uncontested
matter of public record (a year, a body count from a cited source, a price
publicly listed).

### Rule 6 - `APPLICATIONS` must name things that exist

An entry must name something a reader could go and look up: an approved product
class, a completed trial, a deployed programme, a commercial process.

> "Could be used for neurodegeneration" is not an application. It is a hope,
> and hopes go in `CHALLENGES` as the obstacle.

Order applications roughly by how established they are, most established first,
or by historical sequence where that is clearer. Say which in a comment.

### Rule 7 - At least four `CHALLENGES`, at least one of them non-technical

Cost, access, regulation, public acceptance, capacity, workforce, geography.

A field described only by its technical obstacles is being described by its own
practitioners, and that is a biased sample. The non-technical challenges are
usually the ones that determine whether anybody actually benefits.

### Rule 8 - `MILESTONES` must include the failures

At least three milestones. Where the field has had a setback, at least one must
be a setback.

The 1999 death that halted gene therapy, the 2003 leukaemias, the 1985
Creutzfeldt-Jakob transmission through pituitary growth hormone, the 1957
transplant series in which every patient died - these are not blemishes on the
record. They are the reason the oversight looks the way it does, and a timeline
of unbroken triumph is a marketing document.

Other milestone rules:

- Prefer events datable to a year without argument. Where a date is disputed
  or gradual, choose the conventional year and say so in `note`.
- Do not credit a simultaneous discovery to one person. Several groups reached
  transgenic plants and CRISPR editing at nearly the same time; say so.
- Keep `event` to one clause; elaboration goes in `note`.
- Negative years mean BCE and are permitted for domestication events.

### Rule 9 - Every `Metric` carries a unit and an evidence grade

`typical` is a **string**, never a pair of numbers. Almost every real range in
biology is conditional, and encoding it numerically invites a user to average
it, plot it or compare across conditions, all of which are wrong. The string
form forces the reader to read the `note`.

Symbols are **ASCII**: `mu`, not the Greek letter; `t_half`, not a subscript.
The same string must render in a terminal, a mis-encoded CSV, a LaTeX document
and an HTML page. Pretty rendering is generated from a lookup table in
`core/text.py`, never stored in the data.

### Rule 10 - Distinguish regulations from standards

A **regulation** is law: breaking it is an offence and a named authority
enforces it. A **standard** is a technical consensus document with no
independent legal force, though a regulation may incorporate it by reference.

Keep them in separate tuples, so that a reader in a third country can
substitute their own regulations while keeping the same standards.

### Rule 11 - State the jurisdictional bias, do not hide it

The `governance` facets lean European because that is what the maintainers can
cite accurately. That is written down in `NOTICE.md` and in `CONTRIBUTING.md`
rather than left for a reader to discover. Additions covering other
jurisdictions are the most welcome kind of contribution.

### Rule 12 - SDG claims must survive a sceptical auditor

Padding the `SDGS` tuple to make a field look socially useful is the most
common failure mode in impact reporting. Each number must survive the question:
*what would a hostile auditor say?*

Where a field **engages** a goal without **advancing** it - gene therapy and
SDG 10, reduced inequalities - include the goal and say so plainly in the
comment and in `WHY_IT_MATTERS`.

### Rule 13 - `RELATED` prefers edges that cross branches

Four to eight entries. An edge to a sibling in the same branch is worth
including only when the two are genuinely confused with each other - gene
therapy and cell therapy, plant genetic engineering and genome editing.

Reciprocity is **not** required. Gene therapy points at bioethics because a
reader of gene therapy needs the ethics; a reader of bioethics needs a much
broader set of examples. The validation suite reports asymmetries as
information, not as errors.

### Rule 14 - The `dark` branch is documented defensively, always

Biosafety, biosecurity governance, dual-use oversight, synthesis screening,
surveillance, countermeasures, forensics, arms control. No operational
information about causing harm, ever, in any facet, in any branch.

`tests/test_dark_branch_is_defensive.py` enforces this. If your contribution
fails that test, the test is not wrong.

---

## 3. Prose conventions

| Convention | Choice |
|------------|--------|
| Spelling | **British English** - *colour*, *organisation*, *analyse*, *litre*, *metre*, *haemoglobin*. `Branch.color` exists as a US-spelling alias in the API only. |
| Numbers in prose | Words up to ten, figures above: *four out of ten patients*, *twenty-three languages*, *2000 L*. |
| Large numbers | Words where the magnitude is the point: *two million euro*, *several trillion rooms*. |
| Scientific notation | ASCII `1e14`, never `10^14` in a data field. Rendered form is generated. |
| Units | SI, or the field convention where SI is not used in practice (`vg/kg`, `CFU/g`, `pg/cell/day`). Written out in `Metric.unit`, abbreviated in `Metric.symbol`. |
| Currency | Euro, written *euro* rather than the symbol. |
| Organism names | Full binomial on first use in a facet; genus abbreviated afterwards. Not italicised - the data is plain text. |
| Contractions | Avoided. *do not*, not *don't*. |
| Em dashes | Avoided in data fields; use a spaced hyphen. Some downstream consumers mangle non-ASCII punctuation. |
| Quotation marks | Straight ASCII quotes only, for the same reason. |

---

## 4. Comment conventions in source files

Content files carry **heavy comments**, deliberately. The comments are where
the editorial reasoning lives, and that reasoning is what makes the dataset
reviewable rather than merely readable.

Every facet file opens with a header stating:

1. which facet it is, and its position in the six;
2. where the full contract is documented (`red/gene_therapy/<facet>.py`);
3. **the subtype-specific note** - why this particular record is unusual, what
   a reviewer should pay attention to, what judgement call was made.

Inside the file, use banner comments to group entries:

```python
# =============================================================================
#  APPLICATIONS
#  Ordered by the historical sequence in which these product classes reached
#  patients, which is also roughly the order of increasing complexity.
# =============================================================================
APPLICATIONS = (
    # -- 1982 onwards: simple recombinant proteins ----------------------------
    "Recombinant human insulin and engineered insulin analogues",
    ...
)
```

Explain **judgement calls** at the point they were made. `MATURITY = COMMERCIAL`
with a four-line comment explaining why it is not `ESTABLISHED` is worth more
than any amount of separate documentation, because it is where the next person
to disagree will be looking.

---

## 5. Review checklist

Before opening a pull request that touches a record:

- [ ] `PLAIN_LANGUAGE` contains no unexplained jargon (Rule 1)
- [ ] `ANALOGY` shows its own limits (Rule 2)
- [ ] `WHY_IT_MATTERS` states a cost or a controversy (Rule 3)
- [ ] Every number in prose has a `Metric` behind it (Rule 5)
- [ ] Every `APPLICATION` names something that exists (Rule 6)
- [ ] At least four `CHALLENGES`, at least one non-technical (Rule 7)
- [ ] At least three `MILESTONES`, including a setback if there was one (Rule 8)
- [ ] Every `Metric` has a unit and an evidence grade (Rule 9)
- [ ] Regulations and standards are in the right tuples (Rule 10)
- [ ] Every SDG survives the sceptical auditor (Rule 12)
- [ ] Judgement calls are explained in comments (section 4)
- [ ] `make validate` passes
- [ ] `make test` passes
