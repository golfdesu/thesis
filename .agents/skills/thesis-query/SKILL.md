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

### Step 1: Knowledge Retrieval

When asked a research question:

1. **Consult the Digest:** Read `paper_digest.md` (the one-file summary of all ingested papers) to quickly identify relevant papers.
2. **Consult Synthesis Docs:** Check `research_gaps.md` or `transformer_research_ideas.md` if the query is about novelty or gaps.
3. **Deep Dive:** Read specific paper notes (`wiki/papers/`) or concept nodes (`wiki/models/`, `wiki/datasets/`) if granular details (like exact equations or metrics) are needed.

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
