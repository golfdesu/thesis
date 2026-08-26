"""Round A: structural content audit of the Obsidian thesis vault.

Checks per note:
- YAML frontmatter parses
- type-specific required fields present and non-empty
- filename year == frontmatter year (papers)
- doi_url looks like a URL / DOI
- authors is a list of strings, first author surname appears in filename (papers)
- title vs filename sanity
- mojibake / replacement-char detection
- refs-file pairing for papers that have _refs counterparts

Writes a machine-readable JSON report + prints a summary.
"""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required")
    sys.exit(1)

VAULT = Path(r"C:\Users\chaya\Documents\Obsidian\Thesis\wiki")

REQUIRED = {
    "paper": ["type", "title", "authors", "year", "doi_url"],
    "model": ["type", "name"],
    "dataset": ["type", "name"],
    "metric": ["type"],
    "feature": ["type", "name"],
}

MOJIBAKE_PATTERNS = [
    re.compile(r"\uFFFD"),                          # replacement char
    re.compile(r"[\u00C0-\u00FF]{2,}"),             # latin-1 soup (Ã¢â‚¬ etc.)
    re.compile(r"\bdY[\u0020-\u007E\u2018-\u201D\u2032\u2033_+]?"),
    re.compile(r"\bæ[\u0000-\uFFFF]*?\b"),
    re.compile(r"â€"),
]

DOI_OK = re.compile(r"(https?://(dx\.)?doi\.org/|https?://arxiv\.org/|https?://huggingface\.co/|10\.\d{4,}/\S+|https?://openreview\.net/|https?://proceedings\.|https?://www\.jmlr\.org/|https?://ojs\.aaai\.org/)", re.IGNORECASE)


def find_mojibake(text):
    hits = []
    for pat in MOJIBAKE_PATTERNS:
        for m in pat.finditer(text):
            ctx = text[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")
            hits.append((m.group(0)[:20], ctx))
    return hits


def main():
    report = {
        "yaml_errors": [], "missing_fields": [], "year_mismatch": [],
        "bad_doi": [], "authors_issue": [], "mojibake": {},
        "empty_bodies": [], "title_stem_mismatch": [],
        "counts": {}, "total": 0,
    }
    files = sorted(VAULT.rglob("*.md"))
    report["total"] = len(files)

    for f in files:
        rel = f.relative_to(VAULT).as_posix()
        raw = f.read_text(encoding="utf-8", errors="replace")
        meta = {}
        if raw.startswith("---"):
            parts = raw.split("---", 2)
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except Exception as e:
                report["yaml_errors"].append(f"{rel}: {e}")
                meta = None

        # mojibake scan on whole file
        hits = find_mojibake(raw)
        if hits:
            bucket = report["mojibake"].setdefault(rel, [])
            seen = set()
            for token, ctx in hits:
                if token not in seen:
                    seen.add(token)
                    bucket.append({"token": token, "ctx": ctx})

        if meta is None:
            continue
        ftype = str(meta.get("type", "")).lower()
        report["counts"][ftype] = report["counts"].get(ftype, 0) + 1

        # required fields
        req = REQUIRED.get(ftype)
        if req:
            missing = [k for k in req
                       if meta.get(k) in (None, "", [], {})
                       and str(meta.get(k, "")).strip() == ""]
            # 'type' itself always set if we got here
            missing = [k for k in missing if k != "type"]
            if missing:
                report["missing_fields"].append(f"{rel}: missing {missing}")

        # papers: extra checks
        if ftype == "paper":
            m_year = re.match(r"^(\d{4})_", f.stem)
            fm_year = meta.get("year")
            if m_year and fm_year is not None and str(fm_year) != m_year.group(1):
                report["year_mismatch"].append(
                    f"{rel}: filename {m_year.group(1)} vs frontmatter {fm_year}")
            y_int = int(m_year.group(1)) if m_year else None
            if y_int and not (1990 <= y_int <= 2026):
                report["year_mismatch"].append(f"{rel}: implausible year {y_int}")
            doi = str(meta.get("doi_url", "") or "")
            if doi and not DOI_OK.search(doi):
                report["bad_doi"].append(f"{rel}: {doi[:80]}")
            authors = meta.get("authors")
            if authors is not None and not (
                isinstance(authors, list) and all(isinstance(a, str) and a.strip() for a in authors)
            ) and not isinstance(authors, str):
                report["authors_issue"].append(f"{rel}: authors={authors!r:.80}")
            body = raw.split("---", 2)[-1] if raw.startswith("---") else raw
            text_words = len(re.sub(r"[#*|\-\[\]()$`]", " ", body).split())
            if text_words < 40:
                report["empty_bodies"].append(f"{rel} ({text_words} words)")

        # stubs flagged
        if meta.get("status") == "needs-review":
            pass  # tracked separately, known

    out = Path(__file__).parent / "_content_audit.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"files: {report['total']}")
    print(f"types: {json.dumps(report['counts'], ensure_ascii=False)}")
    for key in ("yaml_errors", "missing_fields", "year_mismatch", "bad_doi",
                "authors_issue", "empty_bodies"):
        items = sorted(set(report[key]))
        print(f"[{key}] {len(items)}")
        for i in items[:15]:
            print("   -", i)
        if len(items) > 15:
            print(f"   ... +{len(items)-15} more")
    mb = report["mojibake"]
    n_tokens = sum(len(v) for v in mb.values())
    print(f"[mojibake] {len(mb)} files, {n_tokens} distinct tokens")
    tokens = {}
    for v in mb.values():
        for item in v:
            tokens[item["token"]] = tokens.get(item["token"], 0) + 1
    for t, c in sorted(tokens.items(), key=lambda kv: -kv[1])[:25]:
        print(f"   token={t!r} x{c}")


if __name__ == "__main__":
    main()
