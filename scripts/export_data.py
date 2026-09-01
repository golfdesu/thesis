"""Export machine-readable data from the Obsidian thesis vault.

Generates structured exports into site/exports/:
  - papers.json                 paper metadata + relationships
  - models.json / datasets.json / metrics.json / features.json
  - relationships_edges.csv     paper -> entity edges
  - README.md                   schema documentation

Read-only with respect to the vault and existing site pages.
Run: python -X utf8 scripts/export_data.py
"""

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VAULT_ROOT = Path(r"C:\Users\chaya\Documents\Obsidian\Thesis\wiki")
OUT_DIR = PROJECT_ROOT / "site" / "exports"

PAPER_DIR = "papers"
ENTITY_DIRS = {
    "models": "model",
    "datasets": "dataset",
    "metrics": "metric",
    "features": "feature",
}
# paper frontmatter field -> relation label in edges CSV
EDGE_FIELDS = {
    "models_used": "model",
    "datasets_used": "dataset",
    "metrics": "metric",
    "features_used": "feature",
}

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^#{1,6}\s+", re.M)


def parse_frontmatter(text):
    """Return (frontmatter dict or None, warning or None)."""
    m = FM_RE.match(text)
    if m:
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as exc:
            return None, f"unparseable YAML ({str(exc).splitlines()[0]})"
        if not isinstance(fm, dict):
            return None, "frontmatter is not a mapping"
        return fm, None
    # Recovery: opening '---' with no closing delimiter. Parse greedily,
    # keeping the last prefix that yields a non-empty mapping, stopping at the
    # first markdown heading or repeated parse failures.
    if not re.match(r"\A---\s*\n", text):
        return None, "no YAML frontmatter"
    lines = text.lstrip("\ufeff").splitlines()[1:]
    best = None
    buf = []
    failures = 0
    for line in lines:
        if HEADING_RE.match(line):
            break
        buf.append(line)
        try:
            fm = yaml.safe_load("\n".join(buf))
        except yaml.YAMLError:
            failures += 1
            if failures >= 3:
                break
            continue
        if isinstance(fm, dict) and fm:
            best = fm
            failures = 0
    if not best:
        return None, "unparseable unterminated frontmatter"
    return best, "recovered frontmatter - missing closing '---' delimiter"


def as_list(value):
    """Normalize a scalar-or-list YAML value into a flat list of strings."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value.strip()] if value.strip() else []
    if isinstance(value, (int, float, bool)):
        return [str(value)]
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(as_list(item))
        return out
    return [str(value)]


def as_authors(value):
    """Authors may be a YAML list or a single delimited string."""
    if isinstance(value, str):
        parts = [p.strip() for p in re.split(r"[;,]", value)]
        return [p for p in parts if p]
    return as_list(value)


def clean_link(raw):
    """Turn 'Target|alias' / 'Target#heading' / plain text into a bare name."""
    return str(raw).split("|", 1)[0].split("#", 1)[0].strip()


def strip_markup(value):
    """Remove wiki-link brackets for display in JSON exports."""
    return WIKI_LINK_RE.sub(lambda m: m.group(1).split("|", 1)[1].strip()
                            if "|" in m.group(1)
                            else m.group(1).split("#", 1)[0].strip(),
                            str(value)).strip()


def extract_doi(value):
    """Prefer a bare DOI over a resolver URL."""
    if value is None:
        return ""
    v = str(value).strip()
    m = re.match(r"(?i)https?://(?:dx\.)?doi\.org/(.+)", v)
    if m:
        return m.group(1)
    return v


def collect_inbound_links(vault_root):
    """Map resolved wiki-target stem -> set of distinct source note stems."""
    inbound = {}
    for path in vault_root.rglob("*.md"):
        src = path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in WIKI_LINK_RE.findall(text):
            target = clean_link(raw).replace(" ", "_")
            if target:
                inbound.setdefault(target, set()).add(src)
    return inbound


def load_papers(warnings):
    papers = []
    folder = VAULT_ROOT / PAPER_DIR
    for path in sorted(folder.glob("*.md")):
        fm, warn = parse_frontmatter(
            path.read_text(encoding="utf-8", errors="replace"))
        if fm is None:
            warnings.append(f"{path.name}: skipped - {warn}")
            continue
        if warn:
            warnings.append(f"{path.name}: {warn}")
        missing = [k for k in ("title", "authors", "year") if fm.get(k) in (None, "")]
        if missing:
            warnings.append(
                f"{path.name}: skipped - missing required field(s): {', '.join(missing)}")
            continue
        year = fm["year"]
        try:
            year = int(str(year))
        except (TypeError, ValueError):
            warnings.append(f"{path.name}: non-numeric year {year!r}; kept as string")
        optional = []
        for key in EDGE_FIELDS:
            if key not in fm:
                optional.append(key)
        if optional:
            warnings.append(
                f"{path.name}: note - missing optional relationship field(s): "
                f"{', '.join(optional)}")
        papers.append({
            "id": path.stem,
            "title": strip_markup(fm["title"]),
            "authors": as_authors(fm["authors"]),
            "year": year,
            "venue": strip_markup(fm.get("journal_conference", "") or ""),
            "doi": extract_doi(fm.get("doi") or fm.get("doi_url")),
            "models_used": [strip_markup(x) for x in as_list(fm.get("models_used"))],
            "datasets_used": [strip_markup(x) for x in as_list(fm.get("datasets_used"))],
            "metrics": [strip_markup(x) for x in as_list(fm.get("metrics"))],
            "rel_url": f"{PAPER_DIR}/{path.stem}.html",
        })
    return papers


def load_entities(warnings, inbound):
    entities = {}   # dir -> list of dicts
    ids = {}        # resolved id -> (dir, index) for edge resolution
    for dirname in ENTITY_DIRS:
        records = []
        folder = VAULT_ROOT / dirname
        for path in sorted(folder.glob("*.md")):
            fm, warn = parse_frontmatter(
                path.read_text(encoding="utf-8", errors="replace"))
            name_src = None
            if fm is not None:
                name_src = (fm.get("name") or fm.get("title")
                            or fm.get("metric") or fm.get("concept"))
                if warn:
                    warnings.append(f"{dirname}/{path.name}: {warn}")
            if fm is None or not name_src:
                warnings.append(
                    f"{dirname}/{path.name}: skipped - {warn or 'no usable name field'}")
                continue
            if "category" not in fm:
                warnings.append(f"{dirname}/{path.name}: note - no category in frontmatter")
            rec_id = path.stem
            tags = as_list(fm.get("tags"))
            records.append({
                "id": rec_id,
                "name": strip_markup(name_src),
                "category": strip_markup(fm["category"]) if fm.get("category") else "",
                "tags": tags,
                "inbound_link_count": len(inbound.get(rec_id, ())),
                "rel_url": f"{dirname}/{rec_id}.html",
            })
            ids[rec_id] = (dirname, len(records) - 1)
            ids[rec_id.lower()] = (dirname, len(records) - 1)
        entities[dirname] = records
    return entities, ids


def resolve_target(name, ids):
    """Resolve a link/plain label to an exported entity id, or None."""
    s = str(name).strip()
    m = WIKI_LINK_RE.search(s)
    if m:
        s = m.group(1)
    target = clean_link(s).replace(" ", "_").rstrip("/")
    if target in ids:
        dirname, idx = ids[target]
        return dirname, idx
    lowered = target.lower()
    if lowered in ids:
        dirname, idx = ids[lowered]
        return dirname, idx
    return None


def load_paper_field_cache():
    """Map paper stem -> frontmatter dict, for edge extraction."""
    cache = {}
    for path in (VAULT_ROOT / PAPER_DIR).glob("*.md"):
        fm, _ = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        cache[path.stem] = fm if fm else {}
    return cache


def build_edges(papers, entities, ids, warnings):
    """Edges: (paper_id, relation, target_entity_id)."""
    edges = []
    unresolved = {}
    field_cache = load_paper_field_cache()
    for paper in papers:
        fm_links = field_cache.get(paper["id"], {})
        for field, relation in EDGE_FIELDS.items():
            for raw in fm_links.get(field, []):
                hit = resolve_target(raw, ids)
                if hit is None:
                    unresolved.setdefault(strip_markup(raw), []).append(paper["id"])
                    continue
                dirname, idx = hit
                edges.append((paper["id"], relation, entities[dirname][idx]["id"]))
    for label, sources in sorted(unresolved.items()):
        warnings.append(
            f"edge target '{label}' did not resolve to an exported note "
            f"(referenced by: {', '.join(sorted(set(sources))[:5])}"
            f"{' ...' if len(set(sources)) > 5 else ''})")
    edges.sort(key=lambda e: (e[0], e[1], e[2]))
    return edges


def write_json(path, records):
    path.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")


README_TEMPLATE = """# Data Exports

Machine-readable exports generated from the Obsidian research vault by
`scripts/export_data.py` (plan phase 13). Do not edit by hand; regenerate with:

~~~bash
python -X utf8 scripts/export_data.py
~~~

Source of truth: `{vault}` (read-only; nothing in the vault is modified).
All `rel_url` values are relative to the site root (`site/`), pointing at the
generated HTML page for the record.

Generated: {generated}

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
| `rel_url` | string | Site-root-relative HTML page, e.g. `{example_dir}/<id>.html` |

## relationships_edges.csv

UTF-8 CSV with header `source_id,relation,target_id`. One row per resolved
paper-to-entity relationship, derived from paper frontmatter fields
`models_used`, `datasets_used`, `metrics`, `features_used`:

| Column | Values |
|---|---|
| `source_id` | Paper note stem (`papers.json[].id`) |
| `relation` | `model` \\| `dataset` \\| `metric` \\| `feature` |
| `target_id` | Entity note stem (matches an `id` in the corresponding entity JSON) |

Only wiki-style references resolvable to an existing exported note become
edges; free-text labels are reported as warnings by the exporter instead.

## Record counts

{counts}
"""


def main():
    if not VAULT_ROOT.is_dir():
        print(f"ERROR: vault not found: {VAULT_ROOT}", file=sys.stderr)
        return 1
    warnings = []
    inbound = collect_inbound_links(VAULT_ROOT)
    papers = load_papers(warnings)
    entities, ids = load_entities(warnings, inbound)
    edges = build_edges(papers, entities, ids, warnings)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "papers.json", papers)
    for dirname, records in entities.items():
        write_json(OUT_DIR / f"{dirname}.json", records)

    edges_path = OUT_DIR / "relationships_edges.csv"
    with edges_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["source_id", "relation", "target_id"])
        writer.writerows(edges)

    counts_lines = "\n".join(
        f"- `{name}`: {len(records)} records"
        for name, records in
        [("papers", papers)] + sorted(entities.items())
    ) + f"\n- `relationships_edges.csv`: {len(edges)} edges"
    readme = README_TEMPLATE.format(
        vault=VAULT_ROOT,
        generated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        example_dir=sorted(entities)[0],
        counts=counts_lines,
    )
    (OUT_DIR / "README.md").write_text(readme, encoding="utf-8")

    print(f"Vault: {VAULT_ROOT}")
    print(f"Papers exported:          {len(papers)}")
    for dirname in sorted(entities):
        print(f"{dirname.capitalize():<26}{len(entities[dirname])}")
    print(f"Relationship edges:       {len(edges)}")
    if warnings:
        print(f"\nWarnings/skips ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("\nNo warnings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
