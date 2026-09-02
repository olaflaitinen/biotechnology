<!--
  .github/PULL_REQUEST_TEMPLATE.md

  Thank you for contributing.

  WHY THIS TEMPLATE IS LONG
  This repository is a curated dataset, and a reviewer checks your FACTS before
  your CODE. The checklists below are the ones a maintainer actually uses,
  taken from STYLE_GUIDE.md section 5, SECURITY.md, THREAT_MODEL.md and
  GOVERNANCE.md. Answering them here removes several rounds of review.

  HOW TO USE IT
  DELETE EVERY SECTION THAT DOES NOT APPLY. A one-line typo fix should leave
  behind sections 1, 2 and 14, and nothing else. Nobody will think less of you
  for deleting nine tenths of this file. Leaving irrelevant unticked boxes in
  place is worse than removing them, because a reviewer cannot tell "not
  applicable" from "not done".

  Where a question offers options, tick the one that applies and delete the
  rest, or leave them and tick one. Either is fine.

  SPDX-License-Identifier: EUPL-1.2
-->

# Pull request

## Section 1. Summary

**1.1 What does this change?**
<!-- One or two sentences. What is different after this is merged? -->

**1.2 Why?**
<!-- What problem does it solve? -->

**1.3 Linked issues**
<!--
  Closes #123
  Refs #456
  If there is no issue, say why not. Scope changes should normally have one.
-->

**1.4 Is this a follow-up to earlier work?**
<!-- Link the earlier pull request, or write "no". -->

---

## Section 2. Type of change

**2.1 Tick every type that applies**

- [ ] **Data correction**, a fact in the taxonomy was wrong or out of date
- [ ] **Editorial**, clarity, plain language, tone, balance
- [ ] **New content**, a subtype, formula, organism, technique, glossary term or reference
- [ ] **Jurisdictional**, regulations or standards for another country or region
- [ ] **Code**, machinery, CLI, exporters, formula implementations
- [ ] **Typing**, annotations or stub improvements
- [ ] **Tests**
- [ ] **Documentation**, root documents, docstrings or the generator
- [ ] **Accessibility**
- [ ] **Translation**
- [ ] **Performance**
- [ ] **Security**
- [ ] **Build, packaging or release**
- [ ] **Continuous integration or tooling**
- [ ] **Refactor**, no behaviour change
- [ ] **Chore**, dependency bumps, formatting, housekeeping
- [ ] **Revert**

**2.2 Scale of the change**

- [ ] One field in one record
- [ ] One whole record
- [ ] Several records in one branch
- [ ] A whole branch
- [ ] Every record in the taxonomy
- [ ] One registry entry
- [ ] The core machinery
- [ ] The facet contract, so all eighty-five subtype packages migrate
- [ ] Documentation or tooling only

**2.3 Roughly how many files does it touch?**

- [ ] One
- [ ] Two to five
- [ ] Six to twenty
- [ ] Twenty to a hundred
- [ ] More than a hundred

**2.4 Is this ready for review, or a draft for discussion?**

- [ ] Ready for review
- [ ] Draft, I want feedback on the approach first
- [ ] Draft, blocked on something named below

**2.5 Does it depend on another pull request being merged first?**
<!-- Link it, or write "no". -->

---

## Section 3. Sources

<!--
  REQUIRED for any factual change. Corrections in this project are settled by
  citation, not by seniority. See CODE_OF_CONDUCT.md, "Argue from sources, not
  from authority". Delete this section only if nothing factual changed.
-->

**3.1 Primary source**
<!-- DOI, official document identifier, case number, standard number, or a URL. -->

**3.2 Second independent source, if any**

**3.3 What kind of source is it?**

- [ ] Peer-reviewed primary research
- [ ] Peer-reviewed review or meta-analysis
- [ ] Consensus statement or clinical guideline
- [ ] Textbook or standard reference work
- [ ] Regulation, directive or statute
- [ ] Court judgment
- [ ] Regulatory agency guidance
- [ ] Technical standard or pharmacopoeial monograph
- [ ] Official statistics or government report
- [ ] Intergovernmental body report
- [ ] Product label or assessment report
- [ ] Preprint
- [ ] Patent
- [ ] Professional experience, no document

**3.4 As of what date is the source current?**

**3.5 Is the source freely readable?**

- [ ] Open access
- [ ] Free with registration
- [ ] Paywalled, and I have quoted the relevant sentence
- [ ] Must be purchased
- [ ] Not publicly available

**3.6 Where in the source?**
<!-- Page, table, article, section. -->

**3.7 Do credible sources conflict on this point?**

- [ ] No
- [ ] Yes, and the record now says so and cites both
- [ ] Yes, and I have explained below why one supersedes the other

**3.8 Has the source been retracted, superseded or amended?**

- [ ] No
- [ ] Yes, and I am citing the current version

---

## Section 4. Editorial checklist

<!--
  Required if you touched any file under src/biotechnology/branches/.
  These are the fourteen normative rules in STYLE_GUIDE.md section 2.
  Delete this whole section if you touched no record.
-->

**4.1 Narrative rules**

- [ ] `PLAIN_LANGUAGE` contains no word that would need a glossary in a general newspaper *(rule 1)*
- [ ] Every technical idea in `PLAIN_LANGUAGE` is either explained in place or omitted *(rule 1)*
- [ ] `ANALOGY` is drawn from ordinary life, not from another technical field *(rule 2)*
- [ ] `ANALOGY` shows its own limits, and nothing depends on it not breaking down *(rule 2)*
- [ ] `WHY_IT_MATTERS` states a cost, a controversy or an access problem alongside the benefit *(rule 3)*
- [ ] Where benefits and harms are contested, all of it is stated *(rule 3)*
- [ ] `DESCRIPTION` reports what the field does, not what it hopes to do *(rule 4)*
- [ ] `DESCRIPTION` names the binding constraint that shapes the field *(rule 4)*
- [ ] `SUMMARY` stands alone with no surrounding context and is under 200 characters *(rule 4)*
- [ ] Every number appearing in prose also appears as a `Metric` with a unit and an evidence grade *(rule 5)*

**4.2 Practice rules**

- [ ] Every entry in `APPLICATIONS` names something a reader could go and look up *(rule 6)*
- [ ] No aspiration is listed as an application; aspirations are in `CHALLENGES` as obstacles *(rule 6)*
- [ ] At least four `CHALLENGES` *(rule 7)*
- [ ] At least one challenge is non-technical: cost, access, regulation, acceptance, capacity or geography *(rule 7)*
- [ ] Every `organisms` and `techniques` key resolves in its registry

**4.3 History rules**

- [ ] At least three `MILESTONES` *(rule 8)*
- [ ] A setback is included where the field has had one *(rule 8)*
- [ ] Simultaneous discoveries are not credited to a single group *(rule 8)*
- [ ] Each `event` is one clause, with elaboration in `note` *(rule 8)*
- [ ] Disputed or gradual dates use the conventional year and say so in the note *(rule 8)*

**4.4 Metric rules**

- [ ] Every `Metric` carries a unit *(rule 9)*
- [ ] Every `Metric` carries an evidence grade *(rule 9)*
- [ ] `Metric.typical` is a string, never a numeric pair *(rule 9)*
- [ ] Every symbol is ASCII, for example `mu` not the Greek letter *(rule 9, NOTATION.md)*
- [ ] Every unit is ASCII, using `u` for micro rather than the Greek letter *(NOTATION.md)*
- [ ] Scientific notation is written `1e14`, not `10^14`, in data fields *(NOTATION.md)*
- [ ] Any range that is conditional says so in the `note` *(rule 9)*

**4.5 Governance rules**

- [ ] Legal instruments are in `REGULATIONS`, technical consensus documents in `STANDARDS` *(rule 10)*
- [ ] Any jurisdictional narrowness is stated rather than implied *(rule 11)*
- [ ] Controlled-vocabulary values are justified in a comment where the choice is arguable
- [ ] `MATURITY` reflects where the field is, not where it is going

**4.6 Linkage rules**

- [ ] Every SDG in `SDGS` survives the sceptical-auditor test *(rule 12)*
- [ ] Where a goal is engaged rather than advanced, the comment says so *(rule 12)*
- [ ] `RELATED` has four to eight entries *(rule 13)*
- [ ] `RELATED` prefers edges that cross a branch boundary *(rule 13)*
- [ ] Same-branch edges are included only where the two records are genuinely confused *(rule 13)*
- [ ] Every `glossary` and `references` key resolves

**4.7 Safety and style**

- [ ] Nothing added anywhere reads as operational instructions *(rule 14)*
- [ ] British spelling throughout *(section 3)*
- [ ] No em dash, en dash, curly quote or other non-ASCII punctuation anywhere in the diff
- [ ] Contractions avoided: "do not", not "don't" *(section 3)*
- [ ] Numbers as words up to ten, figures above *(section 3)*
- [ ] Organism names given in full on first use in a facet *(section 3)*
- [ ] Judgement calls are explained in a comment at the point they were made *(section 4)*
- [ ] Each facet header carries a subtype-specific note, not only the boilerplate

---

## Section 4A. Record-level self-review

<!-- Delete unless you touched a record under src/biotechnology/branches/. -->

**4A.1 Which records did you touch?**

**4A.2 Did you re-read the whole record after your change, or only the field?**

- [ ] The whole record
- [ ] The whole facet
- [ ] Only the field

**4A.3 Does the record still read coherently end to end?**

- [ ] Yes
- [ ] Yes, after adjusting a neighbouring sentence
- [ ] I only checked the field I changed

**4A.4 Does the technical register still agree with the plain-language one?**

- [ ] Yes
- [ ] Both were updated together
- [ ] Not applicable

**4A.5 Does the analogy still hold after the change?**

- [ ] Yes
- [ ] It was updated
- [ ] It was replaced
- [ ] Not applicable

**4A.6 Did the change alter the balance of the record?**

- [ ] No
- [ ] It added a downside that was missing
- [ ] It added a benefit that was missing
- [ ] It removed one, and a replacement was added

**4A.7 Are any numbers in the prose now inconsistent with `metrics.py`?**

- [ ] Checked, consistent
- [ ] Both were updated
- [ ] Not applicable

**4A.8 Does the change affect the branch-level profile?**

- [ ] No
- [ ] Yes, and it was updated
- [ ] I have not checked

**4A.9 Does the same problem exist in sibling records?**

- [ ] No
- [ ] Yes, and they are fixed here too
- [ ] Yes, and a follow-up issue is opened
- [ ] I have not checked

**4A.10 Did you add or remove a cross-reference?**

- [ ] No
- [ ] Added, and the target exists
- [ ] Removed, and nothing now orphans the target

**4A.11 Did you check that every registry key you used resolves?**

- [ ] Yes, `make validate` passes
- [ ] Not applicable

**4A.12 Is the evidence grade still appropriate after the change?**

- [ ] Yes
- [ ] It was raised, justified below
- [ ] It was lowered, justified below
- [ ] Not applicable

---

## Section 5. New subtype checklist

<!-- Only if you added a subtype package. Delete otherwise. -->

- [ ] All seven filenames kept: `__init__.py`, `narrative.py`, `practice.py`, `metrics.py`, `history.py`, `governance.py`, `linkage.py`
- [ ] Each facet exports exactly the names the contract requires, and nothing more
- [ ] `KEY` matches the directory name exactly
- [ ] `NAME` is title case
- [ ] `ALIASES` are lowercase and are names people would actually search for
- [ ] No field left inherited from the template it was copied from
- [ ] `__init__.py` contains no descriptive content beyond identity
- [ ] Registered in the parent branch `__init__.py` with an import line and a tuple entry
- [ ] Placed in the right position in the published narrative order
- [ ] At least two existing subtypes now cross-reference it
- [ ] The branch-level profile still reads correctly with the new record in it
- [ ] Every new registry key it uses already exists, or is added in this pull request
- [ ] `make validate` passes with the new record in place
- [ ] `docs/` regenerated

**5.1 Which existing records now point at it?**

**5.2 Was a cross-reference considered instead of a new record?**

- [ ] Yes, and a record is genuinely warranted because...
- [ ] No

---

## Section 6. New formula checklist

<!-- Only if you added a formula package. Delete otherwise. -->

- [ ] Four files: `__init__.py`, `notation.py`, `derivation.py`, `implementation.py`
- [ ] Every symbol declared in `notation.py` with its unit and permitted range
- [ ] Derivation given in ASCII
- [ ] Derivation also given in LaTeX
- [ ] The assumptions are stated, because a formula without them is a way of being wrong with more confidence
- [ ] Domain enforced, raising `DomainError` naming the parameter, the value and the accepted range
- [ ] No bare `ValueError` from `math` can escape into a caller pipeline
- [ ] Units are documented and checked, never silently coerced
- [ ] Full type annotations, passes `mypy --strict`
- [ ] Doctests are worked examples a reader can verify by hand or against the cited source
- [ ] At least two worked examples with different inputs
- [ ] Citation added to `src/biotechnology/refs/` and linked from `derivation.py`
- [ ] Test module in `tests/formulas/` covering the normal case
- [ ] Test covers both boundaries of the domain
- [ ] Test covers at least one rejected input
- [ ] At least one subtype's `metrics.FORMULAS` now references it

**6.1 Where does the relationship come from?**

- [ ] A named original paper
- [ ] A standard textbook derivation
- [ ] A regulatory or standards document
- [ ] A definition rather than a derivation
- [ ] An empirical fit

---

## Section 7. Code checklist

<!-- Only if you changed anything under src/ that is not a data record. -->

- [ ] Public API additions are exported in `__all__`
- [ ] New public functions have numpy-style docstrings with Parameters, Returns and Raises
- [ ] Errors raised inherit from `BiotechnologyError`
- [ ] Every "unknown X" message names the token, offers a suggestion and lists valid values
- [ ] No new module-level import that would create a cycle
- [ ] Any deferred import is commented at the point of deferral
- [ ] No mutable default arguments
- [ ] Frozen dataclasses stay frozen
- [ ] No new global mutable state
- [ ] Output is deterministic across runs, locales and dict ordering
- [ ] Behaviour is covered by a test that fails without the change
- [ ] Performance-sensitive paths were measured, not guessed
- [ ] Public identifiers follow the existing naming conventions
- [ ] Nothing relies on a Python feature newer than 3.9

**7.1 If you changed an error message, does the old wording appear in any test or document?**

- [ ] Checked, and updated everywhere
- [ ] Not applicable

---

## Section 8. Security checklist

<!--
  Required for EVERY pull request. It is short and it is the section a
  maintainer will not skip. See SECURITY.md and THREAT_MODEL.md.
-->

- [ ] No new runtime dependency *(hard constraint, GOVERNANCE.md 3.3)*
- [ ] No new development dependency, or one is added and justified below
- [ ] No `subprocess`, `os.system`, `os.popen`, `eval`, `exec`, `pickle`, `marshal`, `shelve` or `ctypes` added to `src/`
- [ ] No network capability added to `src/`: no socket, urllib, http, requests, ftplib or smtplib
- [ ] No file is written except to a path the caller passed explicitly
- [ ] No parsing of untrusted input at import time
- [ ] No regular expression that could backtrack catastrophically on user input
- [ ] No secret, token, key or credential appears anywhere in the diff, including in a test fixture
- [ ] No new GitHub Action reference, or one is added to `.github/action-pins.yml` with publisher, permissions, justification and review date
- [ ] Any new workflow declares a top-level `permissions: {}` and per-job least privilege
- [ ] Any new checkout sets `persist-credentials: false`
- [ ] No workflow uses `pull_request_target`
- [ ] No third-party origin added to the documentation site
- [ ] Nothing added to any facet of any record reads as operational instructions *(SECURITY.md 2.2)*
- [ ] If this touches the `dark` branch, I have read SECURITY.md section 2 in full

**8.1 Does this change the attack surface as described in SECURITY.md 1.2?**

- [ ] No
- [ ] Yes, and THREAT_MODEL.md has been updated to say how

**8.2 If a development dependency was added, why could it not be avoided?**

---

## Section 8A. Supply chain and provenance

<!-- Delete unless you touched .github/, tools/, pyproject.toml or the release path. -->

**8A.1 Did you add or change a GitHub Action reference?**

- [ ] No
- [ ] Yes, and it is recorded in `.github/action-pins.yml`

**8A.2 If so, who publishes that action, and is the publisher verified?**

**8A.3 What permissions does it need, and why?**

**8A.4 Was a less privileged alternative considered?**

- [ ] Yes, and it was not sufficient because...
- [ ] Yes, and a script replaced the action
- [ ] Not applicable

**8A.5 Did you change any workflow permission?**

- [ ] No
- [ ] Yes, narrowed
- [ ] Yes, widened, justified below

**8A.6 Did you change the release, signing or attestation path?**

- [ ] No
- [ ] Yes, described below

**8A.7 Does the change affect the software bill of materials?**

- [ ] No
- [ ] Yes, and the SBOM step still runs

**8A.8 Does `THREAT_MODEL.md` need updating?**

- [ ] No, no threat or control changed
- [ ] Yes, and it is updated in this pull request
- [ ] Yes, and a follow-up issue is opened

---

## Section 9. Testing

**9.1 What testing did you do?**

- [ ] `make test` passes
- [ ] `make test-fast` passes
- [ ] New tests added
- [ ] Existing tests updated
- [ ] Doctests added or updated
- [ ] Tested manually, described below
- [ ] No testing was possible, explained below

**9.2 Which commands did you run?**

```
make lint
make typecheck
make policy
make validate
make test
make security
make docs
```

- [ ] `make all` passes locally
- [ ] `pre-commit run --all-files` passes

**9.3 Platforms tested on**

- [ ] Linux
- [ ] macOS
- [ ] Windows
- [ ] Windows Subsystem for Linux
- [ ] A container
- [ ] Only CI

**9.4 Python versions tested on**

- [ ] 3.9
- [ ] 3.10
- [ ] 3.11
- [ ] 3.12
- [ ] 3.13
- [ ] 3.14
- [ ] Only whatever CI runs

**9.5 Did coverage change?**

- [ ] It went up
- [ ] It stayed the same
- [ ] It went down, explained below
- [ ] Not measured

**9.6 Is there any part you could not test?**

---

## Section 9A. Performance and resources

<!-- Delete unless you changed anything that runs at import or in a hot path. -->

**9A.1 Does this change import time?**

- [ ] No
- [ ] It reduces it
- [ ] It increases it, measured below
- [ ] Not measured

**9A.2 Does it change memory use?**

- [ ] No
- [ ] It reduces it
- [ ] It increases it, measured below
- [ ] Not measured

**9A.3 Does it add work to a hot path such as `search()` or `get()`?**

- [ ] No
- [ ] Yes, and it was measured

**9A.4 What did you measure, and how?**

**9A.5 Does behaviour degrade gracefully on very large input?**

- [ ] Yes
- [ ] Input size is bounded by the taxonomy, which is small
- [ ] Not applicable

**9A.6 Could any new regular expression backtrack catastrophically?**

- [ ] No new regular expression
- [ ] Checked, it is anchored and bounded
- [ ] Not applicable

---

## Section 10. Breaking changes and compatibility

<!--
  Subtype keys, branch keys, formula keys, glossary keys and citation keys are
  PUBLIC API. External work cites these strings. A rename needs a major version
  bump and an alias retained for at least one minor cycle.
  See GOVERNANCE.md section 3.6.
-->

- [ ] This change renames no public identifier
- [ ] This change removes no public identifier
- [ ] This change does not alter the `to_dict()` contract
- [ ] This change does not alter the JSON export shape
- [ ] This change does not alter a CLI exit code
- [ ] This change does not alter CLI output that a script might parse
- [ ] This change does not alter an exception type or its inheritance
- [ ] This change does not narrow an accepted input
- [ ] This change does not change the minimum Python version
- [ ] Or: it does one of these, and the migration is described below

**10.1 Migration notes, if any**

**10.2 If an identifier is renamed, is an alias retained?**

- [ ] Yes, for at least one minor cycle
- [ ] Not applicable

---

## Section 11. Documentation

- [ ] `CHANGELOG.md` updated under `## [Unreleased]`
- [ ] `docs/` regenerated with `make docs` and committed
- [ ] Docstrings added or updated
- [ ] Command line help updated
- [ ] `README.md` updated
- [ ] `DATA_MODEL.md` updated
- [ ] `NOTATION.md` updated
- [ ] `ARCHITECTURE.md` updated
- [ ] `STYLE_GUIDE.md` updated
- [ ] `GOVERNANCE.md` updated
- [ ] `SECURITY.md` or `THREAT_MODEL.md` updated
- [ ] `GLOSSARY.md` or `BIBLIOGRAPHY.md` updated
- [ ] `FAQ.md` updated
- [ ] No documentation change is needed, and I have said why below

**11.1 If no documentation changed, why not?**

---

## Section 11A. Release impact

**11A.1 Should this appear in the changelog?**

- [ ] Yes, under Added
- [ ] Yes, under Changed
- [ ] Yes, under Fixed
- [ ] Yes, under Deprecated or Removed
- [ ] Yes, under Security
- [ ] No, it is invisible to users

**11A.2 What kind of version bump does it imply?**

- [ ] None, it is documentation or tooling
- [ ] Patch
- [ ] Minor
- [ ] Major
- [ ] I have no view

**11A.3 Does it change the data freeze position?**

- [ ] No
- [ ] Yes, a factual claim was reverified today
- [ ] Yes, and the next release should record a new freeze date

**11A.4 Is a release needed soon because of this?**

- [ ] No, fold it into the next one
- [ ] Yes, it corrects something misleading
- [ ] Yes, it is a security fix

**11A.5 Does it affect anyone who has already cited the project?**

- [ ] No
- [ ] Yes, a cited value changes
- [ ] Yes, a cited identifier changes

**11A.6 Does `CITATION.cff` need updating?**

- [ ] No
- [ ] Yes, and it is updated here
- [ ] Only at release time

**11A.7 Does any known-limitations list need updating?**

- [ ] No
- [ ] Yes, a limitation is removed
- [ ] Yes, a limitation is added

---

## Section 12. Accessibility and language

<!-- Delete unless this touches rendered output, the site, or prose. -->

- [ ] No colour is used as the only carrier of meaning
- [ ] Any new table has proper headers
- [ ] Any new diagram has a text alternative
- [ ] Contrast is adequate in both the light and the dark palette
- [ ] Any new terminal output is readable without colour
- [ ] Any new abbreviation is expanded on first use
- [ ] New prose reads at the intended register for its field
- [ ] Not applicable

---

## Section 12A. Honest self-assessment

<!--
  The most useful section in this template, and the one most often skipped.
  Nothing here counts against you. A contribution that says plainly what is
  weak about it is reviewed faster and merged sooner than one that does not.
-->

**12A.1 What is the weakest part of this change?**

**12A.2 What did you not check that you probably should have?**

**12A.3 Is there anything you guessed at rather than verified?**

**12A.4 How confident are you in the factual content?**

- [ ] Certain, I have the primary sources
- [ ] Confident, this is my field
- [ ] Reasonably confident, a specialist should look
- [ ] Uncertain, I would like this checked carefully

**12A.5 How confident are you in the code?**

- [ ] Confident, it is covered by tests
- [ ] Reasonably confident
- [ ] Uncertain, please review closely
- [ ] Not applicable

**12A.6 Did you copy any pattern from elsewhere in the repository?**

- [ ] Yes, and I understood why it was written that way
- [ ] Yes, and I am not sure why it was written that way
- [ ] No

**12A.7 Is there a simpler version of this change?**

- [ ] No
- [ ] Yes, and I rejected it because...
- [ ] Possibly, I would welcome a suggestion

**12A.8 Did you leave anything deliberately unfinished?**

**12A.9 Would you be comfortable if this were cited in a policy document tomorrow?**

- [ ] Yes
- [ ] Yes, with the evidence grade it carries
- [ ] No, and I have said why above

**12A.10 Is there anything a reviewer would only find by reading the source rather than the diff?**

---

## Section 13. Reviewer guidance

**13.1 Please look hardest at**

**13.2 I am least sure about**

**13.3 Deliberately out of scope for this pull request**

**13.4 What would change your mind about the approach?**

**13.5 How long do you expect review to take?**

- [ ] Minutes, it is a typo
- [ ] Under an hour
- [ ] It needs a careful read
- [ ] It needs domain expertise, described below
- [ ] It needs a second opinion from a specialist

**13.6 Which kind of reviewer would be most useful?**

- [ ] Anyone
- [ ] Someone who works in this scientific field
- [ ] A clinician or veterinary professional
- [ ] A regulatory affairs professional
- [ ] A lawyer
- [ ] A non-specialist, to check the plain-language register
- [ ] A Python developer
- [ ] A security reviewer
- [ ] An accessibility reviewer
- [ ] A native or fluent speaker of a named language

---

## Section 13A. Process

**13A.1 How would you like review feedback delivered?**

- [ ] Line comments
- [ ] A summary comment
- [ ] Whichever is easier
- [ ] Be blunt, I would rather have it direct

**13A.2 Are you happy for a maintainer to push small fixes to your branch?**

- [ ] Yes, anything
- [ ] Yes, formatting and typos only
- [ ] Please ask first
- [ ] No

**13A.3 How should this be merged?**

- [ ] Squash, I have no view
- [ ] Squash, my commits are messy
- [ ] Rebase, my commits are meaningful
- [ ] Whichever the maintainer prefers

**13A.4 Are you available to iterate on this?**

- [ ] Yes, promptly
- [ ] Yes, but slowly
- [ ] Only for the next week or so
- [ ] No, please take it from here or close it

**13A.5 If this goes stale, what should happen?**

- [ ] Close it
- [ ] Someone else may take it over
- [ ] Ping me first
- [ ] Keep it open, I will come back

**13A.6 Is this your first contribution here?**

- [ ] Yes
- [ ] No
- [ ] Prefer not to say

**13A.7 Did anything about the contribution process confuse you?**

<!-- Genuinely useful. A confusing process is a defect in CONTRIBUTING.md. -->

**13A.8 Is there anything you needed that the documentation did not give you?**

---

## Section 14. Declarations

- [ ] I agree that my contribution is licensed under the **EUPL-1.2**
- [ ] I confirm I have the right to contribute this material
- [ ] This contribution contains no third-party text reproduced beyond fair quotation
- [ ] This contribution reproduces no copyrighted figure, table or dataset
- [ ] I have not used any material whose licence is incompatible with the EUPL-1.2
- [ ] I am happy to be listed in `AUTHORS.md`
- [ ] I have read and agree to follow the [Code of Conduct](../CODE_OF_CONDUCT.md)

**14.1 How would you like to be credited?**

- [ ] By my GitHub handle
- [ ] By my full name, given below
- [ ] By name and affiliation, given below
- [ ] Anonymously
- [ ] Not at all

**14.2 Do you have an interest to declare?**

<!--
  Authorship of a cited source, employment by a named organisation, a patent or
  commercial interest, related funding, membership of an advocacy organisation,
  a public position on the subject.

  Declaring one does not disqualify a contribution; corrections are settled by
  the source. It lets a reviewer weigh the framing.
-->

- [ ] None
- [ ] I am an author of a cited source
- [ ] I work for an organisation named in the record
- [ ] I work for a competitor of an organisation named in the record
- [ ] I hold a patent or commercial interest in the subject
- [ ] I receive funding related to the subject
- [ ] I am a member of an advocacy organisation on this subject
- [ ] I hold a stated public position on this subject
- [ ] Other, described below

**14.3 Detail of any declared interest**

**14.4 Would you be willing to maintain this area in future?**

- [ ] No, this is a one-off contribution
- [ ] Maybe, ask me again
- [ ] Yes, I would review it occasionally
- [ ] Yes, I would like to be a domain editor for this branch
- [ ] Yes, I would like to be the editor for a jurisdiction
