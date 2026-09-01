# -*- coding: utf-8 -*-
"""Hierarchical 2-Tier Research Query & Topic Scanner for Thesis Vault.

Enables instant 80-95% Token Optimization when analyzing the vault:
- Tier 1: Fast in-memory / keyword filtered scan across the structured digest (1-5k tokens).
- Tier 2: Deep targeting of only the top matching paper notes (10-20k tokens instead of 300k+).
"""

import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

VAULT_ROOT = Path("C:/Users/chaya/Documents/Obsidian/Thesis")
DIGEST_PATH = VAULT_ROOT / "paper_digest.md"
PAPERS_DIR = VAULT_ROOT / "wiki" / "papers"


class HierarchicalQueryEngine:
    """Two-tier scanner for efficient literature review and research gap discovery."""

    @classmethod
    def parse_digest_entries(cls) -> List[Dict[str, Any]]:
        """Parses individual paper summaries from paper_digest.md into structured dicts."""
        if not DIGEST_PATH.exists():
            return []

        content = DIGEST_PATH.read_text(encoding="utf-8")
        entries_section = content.split("## 📄 Entries")
        if len(entries_section) < 2:
            return []

        raw_entries = re.split(r"\n###\s+", entries_section[1])
        parsed = []

        for item in raw_entries:
            if not item.strip():
                continue
            lines = item.strip().splitlines()
            paper_id = lines[0].strip()

            body = "\n".join(lines[1:])
            title_match = re.search(r"\*\*(.*?)\*\*", body)
            title = title_match.group(1) if title_match else paper_id

            models = []
            m_match = re.search(r"\*\*Models\*\*:\s*(.*?)(?=\n\*\*|\n-|\Z)", body, re.S)
            if m_match:
                models = [x.strip() for x in m_match.group(1).split(",") if x.strip()]

            datasets = []
            d_match = re.search(r"\*\*Data\*\*:\s*(.*?)(?=\n\*\*|\n-|\Z)", body, re.S)
            if d_match:
                datasets = [x.strip() for x in d_match.group(1).split(";") if x.strip()]

            gaps = []
            g_match = re.search(r"- \*\*Gaps/Limitations:\*\*\s*\n(.*?)(?=\n###|\n---|\Z)", body, re.S)
            if g_match:
                gaps = [re.sub(r"^\s*-\s*", "", l).strip() for l in g_match.group(1).splitlines() if l.strip()]

            parsed.append({
                "id": paper_id,
                "title": title,
                "models": models,
                "datasets": datasets,
                "gaps": gaps,
                "full_digest_text": f"### {paper_id}\n" + body
            })

        return parsed

    @classmethod
    def search_candidates(
        cls,
        query: str,
        top_k: int = 5,
        target_field: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Tier 1: Filter digest down to the most relevant candidate papers."""
        entries = cls.parse_digest_entries()
        keywords = [k.lower().strip() for k in query.split() if len(k.strip()) >= 2]

        scored = []
        for e in entries:
            score = 0
            text_to_search = e["full_digest_text"].lower()

            if target_field == "gaps":
                text_to_search = " ".join(e["gaps"]).lower()
            elif target_field == "models":
                text_to_search = " ".join(e["models"]).lower()

            for kw in keywords:
                if kw in text_to_search:
                    score += text_to_search.count(kw) * 2
                if kw in e["id"].lower():
                    score += 5
                if kw in e["title"].lower():
                    score += 4

            if score > 0:
                scored.append((score, e))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored[:top_k]]

    @classmethod
    def get_focused_context(cls, query: str, top_k: int = 4) -> Tuple[str, List[str]]:
        """Generates a compressed, high-density context prompt for answering queries (Tier 2).

        Returns: (compact_context_markdown, matched_paper_ids)
        """
        candidates = cls.search_candidates(query, top_k=top_k)
        if not candidates:
            return "No matching papers found in digest.", []

        matched_ids = [c["id"] for c in candidates]
        context_parts = [
            f"# Focused Research Context ({len(candidates)} Papers for '{query}')\n",
            "> Extracted via Hierarchical 2-Tier Scanner (Token Optimization)\n"
        ]

        for c in candidates:
            note_file = PAPERS_DIR / f"{c['id']}.md"
            if note_file.exists():
                note_text = note_file.read_text(encoding="utf-8")
                # Prune BibTeX and citation graph for clean context
                note_text = re.split(r"## 📚 BibTeX", note_text)[0].strip()
                context_parts.append(f"## [[{c['id']}]]\n{note_text}\n---\n")
            else:
                context_parts.append(c["full_digest_text"] + "\n---\n")

        full_context = "\n".join(context_parts)
        return full_context, matched_ids


if __name__ == "__main__":
    test_query = "diffusion probabilistic forecasting"
    print(f"=== Hierarchical Query Test for: '{test_query}' ===")
    ctx, ids = HierarchicalQueryEngine.get_focused_context(test_query, top_k=3)
    print(f"Matched Papers: {ids}")
    print(f"Context Length: {len(ctx):,} chars (~{len(ctx)/4:,.0f} tokens)")
    print(f"Token Reduction vs Loading Full 130 Notes (300k tokens): ~{((300000 - len(ctx)/4) / 300000)*100:.1f}%")
