"""Validate the generated site: broken links, search index coverage,
duplicates, and thin/empty pages.

Usage:
    python scripts/validate_site.py
"""

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

SITE_DIR = Path(__file__).resolve().parent.parent / "site"

issues = {
    "broken_internal_links": [],
    "missing_assets": [],
    "index_missing_pages": [],
    "index_stale_entries": [],
    "duplicate_titles": [],
    "duplicate_rel_urls": [],
    "thin_pages": [],
    "missing_meta_description": [],
}

HTML_RE = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)

EXTERNAL_RE = re.compile(
    r"^(https?:|mailto:|tel:|data:|javascript:|#)", re.IGNORECASE
)


def normcase(path_str: str) -> str:
    return os.path.normcase(os.path.normpath(path_str))


def all_html_files():
    return sorted(SITE_DIR.rglob("*.html"))


def check_links(pages, existing):
    seen = set()
    for page in pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        rel_page = page.relative_to(SITE_DIR)
        parent = str(page.parent)
        for match in HTML_RE.finditer(text):
            link = match.group(1).strip()
            if not link or EXTERNAL_RE.match(link):
                continue
            key = (str(rel_page), link)
            if key in seen:
                continue
            seen.add(key)
            target = unquote(urlparse(link).path)
            if not target:
                continue
            resolved = normcase(os.path.join(parent, target))
            if resolved not in existing:
                entry = f"{rel_page} -> {link}"
                if link.lower().endswith(".html") or "/" in link.replace("\\", "/"):
                    issues["broken_internal_links"].append(entry)
                else:
                    issues["missing_assets"].append(entry)


def check_search_index(pages):
    index_path = SITE_DIR / "assets" / "search-index.json"
    if not index_path.exists():
        print("ERROR: search-index.json not found")
        sys.exit(1)
    entries = json.loads(index_path.read_text(encoding="utf-8"))

    page_urls = {p.relative_to(SITE_DIR).as_posix() for p in pages}
    indexed_urls = [e.get("rel_url", "") for e in entries]

    issues["index_missing_pages"] = sorted(page_urls - set(indexed_urls))
    issues["index_stale_entries"] = sorted(u for u in indexed_urls if u not in page_urls)

    title_counts = Counter(e.get("title", "").strip().lower() for e in entries)
    issues["duplicate_titles"] = sorted(
        t for t, c in title_counts.items() if c > 1 and t
    )
    url_counts = Counter(indexed_urls)
    issues["duplicate_rel_urls"] = sorted(
        u for u, c in url_counts.items() if c > 1
    )
    return len(entries)


def check_pages(pages):
    for page in pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        rel = page.relative_to(SITE_DIR)
        if rel.as_posix() == "index.html":
            continue
        if 'name="description"' not in text:
            issues["missing_meta_description"].append(rel.as_posix())
        body_match = re.search(r"<main[^>]*>(.*)</main>", text, re.DOTALL | re.IGNORECASE)
        body_text = ""
        if body_match:
            body_text = re.sub(r"<[^>]+>", " ", body_match.group(1))
        else:
            m = re.search(r"<body[^>]*>(.*)</body>", text, re.DOTALL | re.IGNORECASE)
            if m:
                body_text = re.sub(r"<script.*?</script>", " ", m.group(1), flags=re.DOTALL)
                body_text = re.sub(r"<[^>]+>", " ", body_text)
        words = len(body_text.split())
        if words < 50:
            issues["thin_pages"].append(f"{rel} ({words} words)")


def report():
    total = 0
    for key, items in issues.items():
        items = sorted(set(items))
        issues[key] = items
        total += len(items)
        status = "OK" if not items else f"{len(items)} issue(s)"
        print(f"[{status:>12}] {key}")
        for item in items[:20]:
            print(f"    - {item}")
        if len(items) > 20:
            print(f"    ... and {len(items) - 20} more")
    print()
    print(f"Total issues: {total}")


def main():
    if not SITE_DIR.exists():
        print(f"ERROR: site directory not found at {SITE_DIR}")
        sys.exit(1)
    t0 = __import__("time").time()
    pages = all_html_files()

    # index all existing files once (normalized string paths, no per-link syscall)
    existing = {normcase(str(p)) for p in SITE_DIR.rglob("*") if p.is_file()}

    check_links(pages, existing)
    n_indexed = check_search_index(pages)
    check_pages(pages)
    report()
    print(f"Checked {len(pages)} HTML pages in {__import__('time').time() - t0:.1f}s. "
          f"Search index entries: {n_indexed}")
    sys.exit(0)


if __name__ == "__main__":
    main()
