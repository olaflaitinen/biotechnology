<!--
  GENERATED FILE. Do not edit.
  Produced from the taxonomy.
  Edit the source and run `make docs`.
-->

# API reference

Everything below is importable from the top-level package.

## Records

| Name | What it is |
|---|---|
| `Branch` | One colour branch, a container of records |
| `Subtype` | One record |
| `Metric` | A named, united, evidence-graded measurement |
| `Milestone` | A dated event with a note |
| `Node` | `Branch` or `Subtype`, for functions accepting either |

## Lookup and filtering

| Call | Returns |
|---|---|
| `get(path)` | a branch or a record |
| `get_branch(key)` | a branch, by key or alias |
| `get_subtype(path)` | a record |
| `branches()` | every written branch |
| `subtypes()` | every record |
| `by_sdg(n)` | records citing a goal |
| `by_domain(d)`, `by_maturity(m)`, `by_risk_tier(t)`, `by_scale(s)` | filtered records |
| `related_to(path, depth=1)` | records reachable by cross-reference |
| `timeline(path=None, since=None)` | `(year, event, source)` triples |
| `counts()` | headline figures |

## Search, export and validation

| Call | Returns |
|---|---|
| `search(query, limit=None)` | records, best first |
| `to_dict()`, `to_json()`, `to_csv()`, `to_markdown()`, `to_dot()`, `tree()` | text |
| `validate(strict=False)` | findings; raises `ValidationError` on error |

## Coverage

| Name | Meaning |
|---|---|
| `WRITTEN_COLOURS` | branches whose package exists |
| `PENDING_COLOURS` | branches not written yet |
| `BROWN`, `GOLD`, `DARK`, `PURPLE` | `None` while pending |

## Errors

Every error inherits from `BiotechnologyError`, so one `except` clause covers the library while ordinary Python errors still propagate.
