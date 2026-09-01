# -*- coding: utf-8 -*-
"""Generate `paper_digest.md`: single-file digest of ALL notes in wiki/papers/.

Run from anywhere:  python gen_paper_digest.py
Reads every wiki/papers/*.md note and rewrites paper_digest.md at the vault root.
Do not hand-edit paper_digest.md — fix the source note, then rerun this script.
"""
import re
from collections import Counter
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parent
PAPERS = VAULT / "wiki" / "papers"
OUT = VAULT / "paper_digest.md"
TODAY = date.today().isoformat()
Q = '"'


def clean_wikis(t):
    t = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)
    return t


def trunc(s, n):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " …"


def unquote(s):
    return s.strip().strip('"').strip("'").strip()


def smart_scalar(raw):
    """Extract a YAML scalar: prefer the first quoted segment; otherwise drop inline ' #' comments."""
    raw = raw.strip()
    if raw.startswith('"'):
        end = raw.find('"', 1)
        if end != -1:
            return raw[1:end]
        return raw.strip('"')
    return re.split(r"\s+#", raw)[0].strip()


def parse_fm(txt):
    data, cur, buf = {}, None, ""
    for line in txt.splitlines():
        if re.match(r"^[A-Za-z_]+:", line):
            if cur:
                data[cur] = buf.strip()
            cur, buf = line.split(":", 1)[0], line.split(":", 1)[1]
        elif cur is not None:
            buf += " " + line.strip()
    if cur:
        data[cur] = buf.strip()
    return data


def fm_list(data, key):
    raw = smart_scalar(data.get(key, ""))
    if not raw:
        return []
    if not raw.startswith("["):
        return [clean_wikis(raw)]
    if raw.startswith("[[") and "]]," not in raw:
        return [clean_wikis(unquote(raw))]
    inner = raw[1:raw.rfind("]")]
    # split on top-level commas only (respecting "quotes" and [[wikilinks]])
    parts, buf, inq, depth, i = [], "", False, 0, 0
    while i < len(inner):
        ch = inner[i]
        if ch == Q:
            inq = not inq
            buf += ch
        elif ch == "[" and inner[i:i + 2] == "[[":
            depth += 1
            buf += "[["
            i += 1
        elif ch == "]" and inner[i:i + 2] == "]]":
            depth -= 1
            buf += "]]"
            i += 1
        elif ch == "," and not inq and depth <= 0:
            parts.append(buf)
            buf = ""
        else:
            buf += ch
        i += 1
    parts.append(buf)
    items = []
    for part in parts:
        s = unquote(part)
        if "[[" not in s:
            s = s.strip("[] \t")
        if s and s not in items:
            items.append(clean_wikis(s))
    return items


def get_section(body, keyword):
    m = re.search(r"^## .*?" + re.escape(keyword) + r".*?$\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return m.group(1).strip() if m else ""


def bullets_of(sec, max_bullets=None, max_chars=420):
    out, cur = [], None
    for line in sec.splitlines():
        st = line.strip()
        if not st:
            continue
        if st.startswith("|") or st.startswith("```") or st.startswith("#"):
            continue
        if st.startswith("- ") or st.startswith("* "):
            if cur:
                out.append(cur)
            cur = clean_wikis(st[2:])
        elif st.startswith(">"):
            if cur:
                out.append(cur)
                cur = None
        elif cur is not None:
            cur += " " + clean_wikis(st)
        else:
            cur = clean_wikis(st)
    if cur:
        out.append(cur)
    out = [trunc(b, max_chars) for b in out if b.strip()]
    out = [b.replace("$$", " ") for b in out]
    seen, uniq = set(), []
    for b in out:
        k = b.lower()
        if k not in seen:
            seen.add(k)
            uniq.append(b)
    out = uniq
    if max_bullets:
        out = out[:max_bullets]
    return out


def method_core(sec):
    picks = []
    for line in sec.splitlines():
        st = line.strip()
        if "$$" in st or st.startswith("```") or st.startswith("|"):
            continue
        core = clean_wikis(st.lstrip("- ").strip())
        if not core:
            continue
        if re.match(r"^(\*?\*)?(Key\s+)?Eq(uations?)?", core, re.I):
            continue
        if "Model Type" in core or "Model type" in core or "architecture" in core.lower():
            picks.append(trunc(core, 380))
            if len(picks) >= 2:
                break
    picks = [p for p in picks if "$$" not in p]
    if not picks:
        for line in bullets_of(sec, max_bullets=3, max_chars=380):
            if "$$" not in line:
                picks.append(line)
                break
    return picks


def result_lines(sec, max_lines=3):
    keep = []
    for b in bullets_of(sec, max_chars=320):
        if re.search(r"\d", b) and re.search(r"%|=|×|[0-9]\.[0-9]|[0-9]{2,}", b):
            keep.append(b)
        if len(keep) >= max_lines:
            break
    return keep


notes = []
for p in sorted(PAPERS.glob("*.md")):
    raw = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", raw, re.S)
    data = parse_fm(m.group(1)) if m else {}
    body = raw[m.end():] if m else raw
    title = clean_wikis(smart_scalar(data.get("title", ""))) or p.stem
    year = re.sub(r"\D", "", data.get("year", "")[:4]) or "????"
    venue = clean_wikis(smart_scalar(data.get("journal_conference", "")))
    doi = smart_scalar(data.get("doi_url", ""))
    models = fm_list(data, "models_used")
    datasets = fm_list(data, "datasets_used")
    feats = fm_list(data, "features_used")
    metrics = fm_list(data, "metrics")
    hz = fm_list(data, "forecasting_horizon")
    horizon = " / ".join(hz) if hz else clean_wikis(smart_scalar(data.get("forecasting_horizon", "")))
    obj = bullets_of(get_section(body, "Main Objective"))
    meth = method_core(get_section(body, "Methodology"))
    res = result_lines(get_section(body, "Performance"))
    lim = bullets_of(get_section(body, "Limitations"))
    authors_raw = fm_list(data, "authors")
    first_author = authors_raw[0].split()[-1] if authors_raw else ""
    et_al = f"{first_author} et al." if len(authors_raw) > 1 else (first_author or "")
    notes.append(dict(name=p.stem, title=title, year=year, venue=venue, doi=doi,
                      models=models, datasets=datasets, feats=feats, metrics=metrics,
                      horizon=horizon, obj=obj, meth=meth, res=res, lim=lim,
                      author=et_al))

notes.sort(key=lambda n: (-int(n["year"]) if n["year"].isdigit() else 9999, n["name"]))

L = []
L.append("# 📋 One-File Paper Digest — All Papers (for AI Gap Analysis)")
L.append("")
L.append(f"> **Purpose**: single-file, self-contained digest of ALL {len(notes)} ingested papers "
         f"(source: `wiki/papers/*.md`, generated {TODAY}). Built so an AI agent can read ONE file and "
         f"immediately know what every paper did — enabling research-gap identification without opening individual notes.")
L.append(f"> **Entry format**: `### filename` → Title — venue, year → metadata line (Models / Horizon / Metrics / Data / Features) "
         f"→ **What they did** (objective & contribution) → **Method core** → **Key results** (numbers) → **Gaps/Limitations**.")
L.append("> **Ordering**: newest first. Wikilinks were flattened to plain text; equations omitted; "
         "full details/equations/BibTeX live in the linked per-paper note. "
         "GENERATED FILE — do not hand-edit; fix source notes and rerun `gen_paper_digest.py`.")
L.append("")

years = Counter(n["year"] for n in notes)
L.append("## 🗂️ Corpus Snapshot")
L.append(f"- Total papers: **{len(notes)}**")
L.append("- By year: " + " · ".join(f"{y} ({c})" for y, c in sorted(years.items())))
top_models = Counter(m for n in notes for m in n["models"]).most_common(12)
L.append("- Most-cited model concepts: " + ", ".join(f"{k} ({v})" for k, v in top_models))
L.append("")
L.append("## 🔎 Quick-Scan Table")
L.append("| Paper | Yr | Venue | Core Models | Horizon | Data (#) |")
L.append("|---|---|---|---|---|---|")
for n in notes:
    core = ", ".join(n["models"][:2]) + (" …" if len(n["models"]) > 2 else "")
    L.append(f"| {n['name']} | {n['year']} | {trunc(n['venue'], 38)} | {trunc(core, 46)} | {trunc(n['horizon'], 22)} | {len(n['datasets'])} |")

L.append("")
L.append("---")
L.append("## 📄 Entries")
for n in notes:
    L.append("")
    L.append(f"### {n['name']}")
    head = f"**{trunc(n['title'], 220)}**"
    meta = []
    if n["author"]:
        meta.append(n["author"])
    if n["venue"]:
        meta.append(trunc(n["venue"], 90))
    meta.append(n["year"])
    L.append(head + "  \n" + " · ".join(meta))
    if n["doi"]:
        L.append(f"<{n['doi']}>")
    info = []
    if n["models"]:
        info.append("**Models**: " + trunc(", ".join(n["models"]), 260))
    if n["horizon"]:
        info.append("**Horizon**: " + n["horizon"])
    if n["metrics"]:
        info.append("**Metrics**: " + trunc(", ".join(n["metrics"]), 160))
    if n["datasets"]:
        info.append("**Data**: " + trunc("; ".join(n["datasets"]), 300))
    if n["feats"]:
        info.append("**Features**: " + trunc(", ".join(n["feats"]), 240))
    L.append("  \n".join(info))
    if n["obj"]:
        L.append("")
        L.append("- **What they did:**")
        L.extend(f"  - {b}" for b in n["obj"])
    if n["meth"]:
        L.append("- **Method core:** " + " — ".join(n["meth"]))
    if n["res"]:
        L.append("- **Key results:**")
        L.extend(f"  - {b}" for b in n["res"])
    if n["lim"]:
        L.append("- **Gaps/Limitations:**")
        L.extend(f"  - {b}" for b in n["lim"])

OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"WROTE {OUT} | papers: {len(notes)} | size: {OUT.stat().st_size/1024:.0f} KB | lines: {len(L)}")
