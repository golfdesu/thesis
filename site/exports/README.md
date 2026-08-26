# Data Exports

Machine-readable exports generated from the Obsidian research vault by
`scripts/export_data.py` (plan phase 13). Do not edit by hand; regenerate with:

~~~bash
python -X utf8 scripts/export_data.py
~~~

Source of truth: `C:\Users\chaya\Documents\Obsidian\Thesis\wiki` (read-only; nothing in the vault is modified).
All `rel_url` values are relative to the site root (`site/`), pointing at the
generated HTML page for the record.

Generated: 2026-08-26 10:00 UTC

## papers.json

JSON array of paper records:

| Field | Type | Notes |
|---|---|---|
| `id` | string | Note file stem (stable identifier) |
| `title` | string | Paper title |
| `authors` | string[] | Normalized from list or delimited string |
| `year` | integer | Publication year |
| `venue` | string | Journal/conference (`journal_conference` frontmatter); empty if unknown |
| `doi` | string | Bare DOI when derivable from `doi_url`; empty if unknown |
| `models_used` | string[] | Model/architecture labels cited by the paper note |
| `datasets_used` | string[] | Dataset labels cited by the paper note |
| `metrics` | string[] | Evaluation metric labels cited by the paper note |
| `rel_url` | string | Site-root-relative HTML page, e.g. `papers/<id>.html` |

## models.json / datasets.json / metrics.json / features.json

Each is a JSON array of entity records:

| Field | Type | Notes |
|---|---|---|
| `id` | string | Note file stem |
| `name` | string | Display name from frontmatter (`name`/`title`/`metric`) |
| `category` | string | Frontmatter `category`; empty if absent |
| `tags` | string[] | Frontmatter tags |
| `inbound_link_count` | integer | Distinct vault notes containing a `[[wiki link]]` to this note |
| `rel_url` | string | Site-root-relative HTML page, e.g. `datasets/<id>.html` |

## relationships_edges.csv

UTF-8 CSV with header `source_id,relation,target_id`. One row per resolved
paper-to-entity relationship, derived from paper frontmatter fields
`models_used`, `datasets_used`, `metrics`, `features_used`:

| Column | Values |
|---|---|
| `source_id` | Paper note stem (`papers.json[].id`) |
| `relation` | `model` \| `dataset` \| `metric` \| `feature` |
| `target_id` | Entity note stem (matches an `id` in the corresponding entity JSON) |

Only wiki-style references resolvable to an existing exported note become
edges; free-text labels are reported as warnings by the exporter instead.

## Record counts

- `papers`: 118 records
- `datasets`: 162 records
- `features`: 148 records
- `metrics`: 66 records
- `models`: 446 records
- `relationships_edges.csv`: 1805 edges
