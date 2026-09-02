# NOTICE

This file is the attribution notice required by Article 5 of the European Union
Public Licence v. 1.2, under which this work is distributed. It also records
the provenance of the third-party material referenced by the project, and the
disclaimers that govern how the content may be used.

---

## 1. Copyright and licence

```
Copyright (c) 2026
Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov
School of Information and Communication Technology
Metropolia University of Applied Sciences
Karaportti 2, 02610 Espoo, Finland

Licensed under the EUPL
```

This work is licensed under the **European Union Public Licence v. 1.2**
(EUPL-1.2). The full, authoritative text is reproduced verbatim in
[`LICENCE`](LICENCE) and is published by the European Commission at
<https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>.

SPDX short identifier: `EUPL-1.2`

Every source file in this repository carries the line

```
SPDX-License-Identifier: EUPL-1.2
```

which is the machine-readable form of the notice above.

---

## 2. What the EUPL permits and requires

This section is a plain-language summary for orientation only. It is **not** a
substitute for the licence text, and where the two differ the licence governs.

**You may**

- use the work for any purpose, including commercially;
- copy and redistribute it;
- modify it and distribute your modified version;
- sublicense it under the terms permitted by Article 2;
- use it as a component of a larger work.

**You must**

- keep all copyright, patent, trademark and attribution notices intact
  (Article 5, "Attribution right");
- provide the Source Code, or a means of obtaining it, to anyone you
  distribute the work to (Article 5, "Copyleft clause");
- state clearly what you changed, if anything (Article 5, "Provision of
  Source Code");
- distribute any Derivative Work under the EUPL or under one of the
  compatible licences listed in the Appendix to the licence, which include
  GPL v2 and v3, AGPL v3, LGPL v2.1 and v3, MPL v2, EPL v1.0, OSL v2.1 and
  v3.0, CeCILL v2.0 and v2.1, CC BY-SA 3.0 for non-software works, and
  LiLiQ-R and LiLiQ-R+.

**You should know**

- The EUPL has legal value in all twenty-three official languages of the
  European Union, and all language versions are equally authentic
  (Article 13).
- Unless the Licensor specifies otherwise, the governing law is that of the
  European Union Member State where the Licensor resides or has a registered
  office; where the Licensor is not established in the Union, Belgian law
  applies (Article 15).
- The work is provided **without warranty of any kind** (Article 7) and the
  Licensor's liability is excluded to the extent permitted by law
  (Article 8).

---

## 3. Third-party material

This project has **no runtime dependencies**. The distributed package contains
no third-party code.

### 3.1 The licence text itself

`LICENCE` reproduces the official EUPL v1.2 text.

> EUPL © the European Union 2007, 2016

It is reproduced verbatim and unmodified, as the licence requires.

### 3.2 Development-time tooling

The optional `dev`, `test`, `lint`, `docs` and `build` extras install
third-party tools - pytest, ruff, black, mypy, mkdocs, build, twine,
cffconvert, pre-commit - each under its own licence, none of which is
redistributed by this project and none of which is linked into the distributed
package.

### 3.3 Referenced standards, regulations and literature

The `governance` and `linkage` facets of every subtype cite legal instruments,
technical standards and scientific literature **by identifier only**. No text
from any of them is reproduced. Specifically:

- **European Union law** (regulations, directives, decisions) is cited by its
  official identifier. Consolidated official texts are available from
  EUR-Lex and are subject to the European Union's own reuse policy.
- **ISO, IEC, CEN and ASTM standards** are cited by number and title only.
  These documents are copyrighted by their respective bodies and must be
  purchased from them.
- **Pharmacopoeial monographs** (Ph. Eur., USP) are cited by chapter number
  only, for the same reason.
- **ICH, OECD, WHO, WOAH, FAO, EPPO and UPOV guidance** is cited by document
  identifier. Most of these are freely available from the issuing body.
- **Scientific literature** is cited by a citation key that resolves in
  [`BIBLIOGRAPHY.md`](BIBLIOGRAPHY.md) to author, year, title, venue and, where
  one exists, a DOI. No abstracts or figures are reproduced.

Citing a document by identifier is not a reproduction of it and does not
create a derivative work of it.

### 3.4 The Sustainable Development Goals

The `sdgs` field of every record refers to the seventeen goals adopted in
United Nations General Assembly Resolution A/RES/70/1, *Transforming our world:
the 2030 Agenda for Sustainable Development* (2015). Goal titles are used
descriptively. This project is not connected with, endorsed by, or affiliated
with the United Nations, and does not use the UN emblem or the official SDG
logo, colour wheel or icons.

---

## 4. Trademarks

Product names, company names, gene names, and the names of biological
materials, instruments and software mentioned anywhere in this repository are
used **nominatively**, to identify what is being described. They are the
property of their respective owners. Their use here does not imply endorsement
by, affiliation with, or any relationship to those owners.

Where a specific medicinal product is named - for example in a `history` facet
recording a first approval - it is named because that approval is a matter of
public record and is the fact being reported.

---

## 5. Institutional affiliation

The author is affiliated with Metropolia University of Applied Sciences. The
institution is named for identification and academic attribution. Nothing in
this repository constitutes an official statement, position or endorsement of
Metropolia University of Applied Sciences.

---

## 6. Scope and disclaimers

**This is a reference work, not professional advice.**

Nothing in this repository is medical advice, clinical guidance, legal advice,
regulatory advice, investment advice or biosafety guidance. In particular:

- **Metrics and typical ranges** are orientation figures carrying an explicit
  evidence grade. They are not specifications, and they must never be used to
  set a dose, a limit, a release criterion or a safety threshold.
- **Formula modules** implement published relationships for teaching and
  estimation. They are not validated software under any medical device,
  clinical laboratory or GxP framework, and must not be used as such.
- **Regulatory citations** were accurate to the best of the author's knowledge
  at the data freeze recorded in [`CHANGELOG.md`](CHANGELOG.md). Law changes.
  Verify every citation against the current official text before relying on it.
- **The `dark` branch** documents biosafety, biosecurity, oversight,
  detection, attribution and arms control. It contains no operational
  information about causing harm, and this framing is enforced by an automated
  test. See [`SECURITY.md`](SECURITY.md) for the full dual-use content policy.

---

## 7. How to attribute this work

When redistributing this work or a derivative of it, retain this file and the
`LICENCE` file, and include a notice of the following form:

```
This product includes software from the "biotechnology" project,
copyright (c) 2026 Gustav Olaf Yunus Laitinen-Fredriksson Lundstrom-Imanov,
licensed under the EUPL-1.2.
Source: https://github.com/olaflaitinen/biotechnology
```

If you modified the work, add a statement of what you changed, as Article 5 of
the licence requires.

For academic citation, see [`CITATION.cff`](CITATION.cff).
