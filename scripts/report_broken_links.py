"""Generate a full broken wiki-link report for the Obsidian thesis vault.

Scans all .md notes under the wiki folder, extracts [[wiki-links]],
and reports every link target that does not resolve to an existing note.
For each broken target it suggests existing notes with similar names.

Usage:
    python scripts/report_broken_links.py
"""

import difflib
import re
from collections import Counter
from pathlib import Path

OBSIDIAN_DIR = Path(r"C:\Users\chaya\Documents\Obsidian\Thesis")
WIKI_DIR = OBSIDIAN_DIR / "wiki"
REPORT_PATH = Path(__file__).resolve().parent.parent / "broken_links_report.md"

WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def extract_target(link_body: str) -> str:
    # [[target|alias]] -> target ; [[target#heading]] -> target
    return link_body.split("|")[0].split("#")[0].strip()


def main():
    notes = sorted(WIKI_DIR.rglob("*.md"))
    names = {n.stem for n in notes}
    names_lower = {k.lower(): k for k in names}

    broken = {}          # target -> set of file names
    counts = Counter()   # target -> total occurrences
    total_links = 0

    for note in notes:
        text = note.read_text(encoding="utf-8", errors="replace")
        # strip code blocks so example links don't count
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for m in WIKI_LINK_RE.finditer(text):
            total_links += 1
            target = extract_target(m.group(1))
            if not target:
                continue
            if target.lower() not in names_lower:
                broken.setdefault(target, set()).add(note.name)
                counts[target] += 1

    lines = [
        "# Broken Wiki-Link Report",
        "",
        f"- Vault: `{OBSIDIAN_DIR}`",
        f"- Notes scanned: **{len(notes)}**",
        f"- Total wiki-links found: **{total_links}**",
        f"- Broken (unresolved) targets: **{len(broken)}**",
        f"- Total broken-link occurrences: **{sum(counts.values())}**",
        "",
        "Sorted by number of occurrences. 'Suggestion' is the closest",
        "existing note name (only shown when similarity >= 0.6).",
        "",
        "| Occurrences | Broken target | Suggestion | Files (up to 5) |",
        "|---:|---|---|---|",
    ]

    for target, cnt in counts.most_common():
        close = difflib.get_close_matches(target, names, n=1, cutoff=0.6)
        suggestion = close[0] if close else "-"
        sample_files = ", ".join(sorted(broken[target])[:5])
        more = f" (+{len(broken[target]) - 5} more)" if len(broken[target]) > 5 else ""
        lines.append(f"| {cnt} | `{target}` | `{suggestion}` | {sample_files}{more} |")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")
    print(f"Notes: {len(notes)}, links: {total_links}, "
          f"broken targets: {len(broken)}, occurrences: {sum(counts.values())}")


if __name__ == "__main__":
    main()
