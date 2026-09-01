---
name: thesis-query
description: >-
  Use this skill when answering user queries about EV charging load forecasting literature,
  identifying research gaps, comparing models, or summarizing findings across the Thesis vault.
---

# Thesis Query Skill (`/query`)

This skill defines the process for synthesizing answers from the EV Charging Demand Load Forecasting Research Wiki.

---

## Workflow Steps

### Step 1: Knowledge Retrieval (Hierarchical 2-Tier Strategy)

When asked a research question:

1. **Tier 1 (Digest / Topic Scan):** Consult `paper_digest.md` or execute `python scripts/hierarchical_query_engine.py` to filter candidates and reduce context footprint by 85–95%.
2. **Consult Synthesis Docs:** Check `research_gaps.md` or `transformer_research_ideas.md` if the query is about novelty or gaps.
3. **Tier 2 (Deep Dive):** Read specific paper notes (`wiki/papers/`) or concept nodes (`wiki/models/`, `wiki/datasets/`) only for the top candidate papers to inspect granular equations or baseline tables.

### Step 2: Answer Synthesis

- Base your answers strictly on the ingested literature. Never hallucinate findings.
- **Cite every numeric claim** — each number, table value, or ranking must be followed by `[[Paper_Name]]` + location (e.g., `Table 3`, `p.7`, `Fig. 2`). If the location is not in the digest, open the paper note or PDF text to verify before citing. Never copy a number without its source.
- Compare methodologies objectively (e.g., "Paper A used a spatial-temporal graph, whereas Paper B used a pure transformer").
- Highlight the datasets used by different papers to provide context on generalizability.

### Step 3: Formatting the Response

- **Wikilinks:** Always link to vault nodes using Obsidian `[[wikilinks]]` syntax (e.g., `[[2023_Smith_EV_Forecasting]]`, `[[Informer]]`, `[[Caltech_ACN]]`).
- **Equations:** If citing a mathematical formula, render it in LaTeX (`$$...$$`).
- **Clarity:** Keep explanations academic, concise, and structured.

### Step 4: Proactive Action

- If the query reveals a missing synthesis angle (e.g., a new comparison of spatial-temporal models), offer to append a new section to `progress_summary_and_research_gaps.md` or `proposed_architectures.md`.
