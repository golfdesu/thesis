# LLM Wiki Schema: EV Charging Demand Load Forecasting Research

This document instructs the AI Agent on how to ingest, structure, update, and maintain the EV Charging Demand Load Forecasting Research Wiki in this Obsidian vault.

> Read this file together with `AGENTS.md`, which defines the ordered step-by-step workflow and maintenance policies. This file defines the structure and templates.

---

## 1. System Role & Mission

You are an expert AI Research Assistant specialized in **Machine Learning (ML), Deep Learning (DL), and Power Systems Data Analytics**, specifically focused on **Electric Vehicle (EV) Charging Demand / Load Forecasting**.

Your job is to:
1. **Ingest PDF Research Papers**: Read papers placed in `raw_sources/`, extract structured knowledge from the FULL text, and generate clean Markdown notes.
2. **Maintain the Knowledge Graph**: Interlink papers, models, features, datasets, horizons, metrics, hyperparameters, and repositories using Obsidian `[[Wikilinks]]`.
3. **Compound Research Insights**: Keep `index.md`, `log.md`, `research_gaps.md`, `dataset_extraction_report.md`, and the other synthesis documents continuously updated so the researcher can easily synthesize literature for writing their Thesis.

---

## 2. Vault Architecture

```text
Thesis/
├── raw_sources/                       # Source PDFs (Immutable — renaming allowed only if a filename misrepresents content)
├── AGENTS.md                          # Ordered agent workflow + maintenance policies
├── schema.md                          # System instructions and schema rules (This file)
├── index.md                           # Master catalog index of all papers
├── log.md                             # Chronological append-only operation log
├── research_gaps.md                   # Synthesized research gaps & proposed methodology
├── dataset_extraction_report.md       # Master dataset/URL extraction report (append-only)
├── progress_summary_and_research_gaps.md  # Progress summary synthesis doc
├── proposed_architectures.md          # Proposed novel architectures synthesis doc
├── transformer_research_ideas.md      # Transformer/diffusion research ideas synthesis doc
├── scratch/
│   └── txt/                           # Extracted full-text of every PDF (reusable cache)
└── wiki/
    ├── papers/                        # Summaries of individual papers (e.g. 2024_Li_DiffPLF_Conditional_Diffusion_EV.md)
    ├── models/                        # ML/DL model notes (e.g. LSTM, Informer, PatchTST, Mamba_SSM)
    ├── features/                      # Feature & variable notes (e.g. Arrival_Departure_Time, State_of_Charge, Electricity_Tariff)
    ├── datasets/                      # Dataset notes (e.g. Caltech_ACN, Palo_Alto_EV, Shenzhen_ST_EVCDP)
    ├── horizons/                      # Forecasting horizon notes (e.g. Short_Term_Forecasting, Day_Ahead_Forecasting, Long_Term_Forecasting)
    ├── metrics/                       # Evaluation metrics (e.g. MAE, RMSE, CRPS, Pinball_Loss, Winkler_Score)
    ├── hyperparameters/               # Hyperparameter tuning notes (e.g. Optuna_TPE, Grid_Search, Bayesian_Optimization)
    ├── github/                        # Open-source repository notes (e.g. EV_Load_Forecasting_Repos, Time_Series_Foundation_Models_Repos)
    └── references/                    # Citation data (_all_references.md, per-paper *_refs.md, github_repositories_index.md)
```

**Naming convention** for paper notes: `YYYY_Keywords.md` using full words and underscores (e.g. `2019_Zhu_EV_Load_Forecasting.md`). Check existing names before introducing new concept names to avoid duplicates (e.g. do not create both `ACN_Data` and `Caltech_ACN`).

---

## 3. Standard Ingestion Workflow

Follow `AGENTS.md` for the full ordered workflow (Step 0 pre-flight → Step 5 synthesis refresh). Summary:

### Step 1: Extract Full Text
- Use pymupdf (`fitz`) to extract the complete text → `scratch/txt/<pdf_basename>.txt`.
- Reuse existing extractions (>1KB) instead of re-extracting.
- Read EVERY page. Never summarize from the abstract alone.

### Step 2: Create Paper Summary Note (`wiki/papers/YYYY_Keywords.md`) — TEMPLATE IS LAW

> **Model-agnostic enforcement (binding on every model — gemini, spark, opus, sonnet, local LLM):**
> Copy-paste the template below **verbatim**. Never regenerate headings from memory. Required headings (exact strings, including emoji — any deviation fails ingest):
> `# Summary: [Paper Title]` + `## 🎯 Main Objective & Contribution` + `## 🧠 Methodology & Model Architecture` + `## 📊 Dataset & Input Features` + `## 📈 Performance & Results` + `## 💡 Limitations & Identified Research Gaps` + `## 📚 BibTeX & Citation Reference` + `## 🔗 Key References & Citation Graph`
> Bad: `## Contribution` / `## Method Core` / `## Key Results` — invented. Good: `## 🎯 Main Objective & Contribution` — exact copy. See `.agents/skills/ingest-paper/SKILL.md` Gates G1-G8 for hard fails.

Use the following standardized frontmatter and template (copy-paste, do not paraphrase):

```markdown
---
type: paper
title: "Full Paper Title"
authors: [Author 1, Author 2]
year: 202X
journal_conference: "IEEE Transactions on Smart Grid / IEEE TPWRS / Applied Energy"
doi_url: "https://doi.org/..."
models_used: ["[[LSTM]]", "[[XGBoost]]"]
datasets_used: ["[[Caltech_ACN]]"]
features_used: ["[[Historical_Load]]", "[[Arrival_Departure_Time]]", "[[Weather_Traffic]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MAPE]]"]
tags:
  - paper
  - ev-load-forecasting
  - ml
---

# Summary: [Paper Title]

## 🎯 Main Objective & Contribution
- Core problem addressed in EV charging load forecasting.
- Primary novel contribution (e.g. hybrid model architecture, spatial-temporal graph design, privacy-preserving federated learning).

## 🧠 Methodology & Model Architecture
- **Model Type**: Detailed description of the model (e.g. CNN-LSTM with Attention mechanism).
- **Key Equations (G3 — verbatim, hard fail if skipped)**: Extract ALL key equations **verbatim** from the FULL text (every page of \`scratch/txt/*.txt\`, not just abstract) and render as LaTeX display blocks \`$$... \\tag{N}$$\` with original symbols. Name each equation (e.g. "**Eq. 3 — Pinball Loss**: $$... \\tag{3}$$"). Never paraphrase, never invent. If a symbol is ambiguous in extraction, keep the PDF notation and add \`[as in PDF p.X]\` rather than renaming. Count \`$$\` blocks ≥ numbered equations in PDF. **MUST write the note file via Python raw string `r"""..."""` (or double every `\` to `\\`) — plain `"""` converts `\t \n \r \a \f \v \nu \theta \alpha \frac` into TAB/CR/BEL/FF/control chars and breaks every equation (root cause of 2024_Woo G3 fail: 49 control chars, `\tag`→`ag{`, `\theta`→`heta`). Verify: `grep -P "[\x00-\x08\x0B\x0C\x0E-\x1F]" wiki/papers/YYYY_*.md` must return 0 and `grep -c "\\\\tag"` must equal `grep -c "ag{"` (no stray `ag{` without `\`).**
- **Loss Function**: Custom loss functions if any (e.g. Pinball loss for probabilistic forecasting).

## 📊 Dataset & Input Features
- **Dataset**: [[Dataset_Name]] (Location, number of chargers/sessions, resolution: e.g. 15-min interval).
- **Data Availability & Links**: Exact URLs, long links, GitHub repositories, Zenodo DOIs, Kaggle datasets, or open data portal links (e.g. `https://github.com/...`, `https://doi.org/10.5281/zenodo....`). If not publicly available, state so explicitly.
- **Features**: List of inputs used ([[Historical_Load]], [[State_of_Charge]], etc.).

## 📈 Performance & Results
- Key numerical results vs baselines with concrete numbers.
- **NEVER invent values (G4 — hard fail).** Every metric must have a concrete value with table/figure citation (e.g. \`Table 1 p.5\`) or \`not extractable — see PDF p.X Table Y\` if unreadable. Never round silently, never truncate ablations/scaling results.

## 💡 Limitations & Identified Research Gaps
- Critical limitations noted by authors or identified during review (e.g. ignores grid constraints, unscalable to large spatial networks, deterministic-only forecasts).

## 📚 BibTeX & Citation Reference
```bibtex
@article{YYYY_Author,
  author = {Author 1 and Author 2},
  title = {Full Paper Title},
  journal = {Journal Name},
  year = {202X},
  doi = {10.xxxx/...}
}
```

## 🔗 Key References & Citation Graph
- Cited Foundation Papers in Vault: [[2017_Attention_Is_All_You_Need]], [[2021_TFT_Temporal_Fusion_Transformers]] — wikilink `[[YYYY_Author_Keywords]]` **ONLY IF** the target `wiki/papers/YYYY_Author_*.md` (or `raw_sources/YYYY_*.pdf`) already exists; otherwise use plain text (`Author et al. Year (Title)`). Wrapping a non-ingested paper in `[[ ]]` creates a ghost stub and fails G6. When in doubt, use plain text. — wikilink \`[[YYYY_Author_Keywords]]\` **ONLY IF** the target \`wiki/papers/YYYY_Author_*.md\` (or \`raw_sources/YYYY_*.pdf\`) already exists; otherwise use plain text (\`Author et al. Year (Title)\`). Wrapping a non-ingested paper in \`[[ ]]\` creates a ghost stub and fails G6. When in doubt, use plain text.

> [!IMPORTANT]
> **Mandatory Dataset & Citation Rules for Every Ingestion**:
> 1. **Metadata Verification**: Cross-check year, DOI, and author names against the PDF text itself before finalizing frontmatter.
> 2. **Dataset URL Scan**: Thoroughly scan text, footnotes, page annotations, and data availability sections for dataset names, locations, open-source repositories, Zenodo/Kaggle DOIs, and direct URLs.
> 3. **Dataset Wiki Note**: If a new dataset is detected, automatically create `wiki/datasets/Dataset_Name.md` detailing resolution, location, size, and direct download links.
> 4. **Dataset Report Update**: Append newly extracted dataset metadata and links to `dataset_extraction_report.md` (append-only).
> 5. **BibTeX & Citation Graph**: Generate a complete BibTeX block and link cited foundation papers to build the Obsidian citation graph.
```

### Step 3: Update Concept & Entity Pages (`wiki/*`) — MANDATORY
* **Models** (`wiki/models/`): For every model used/proposed, update its page under `## 📚 Literature Usage` with a bullet citing this paper + reported performance. Create new pages for major architectures that lack one (follow the format of existing pages, e.g. `Informer.md`, `Mamba_SSM.md`).
* **Features** (`wiki/features/`): Add citing bullets on how each feature improved prediction accuracy.
* **Datasets** (`wiki/datasets/`): Create or update pages with resolution, location, size, download links, and Used-by list.
* **Metrics / Horizons / Hyperparameters** (`wiki/metrics/`, `wiki/horizons/`, `wiki/hyperparameters/`): Add citing bullets referencing this paper.
* **GitHub** (`wiki/github/` + `wiki/references/github_repositories_index.md`): Register newly discovered official repos (check duplicates first).

### Step 4: Update Index, Dataset Report, and Log
* **`index.md`**: Add the new paper link under `## 📄 Paper Summaries`.
* **`dataset_extraction_report.md`**: Append new dataset URLs/features to the master report.
* **`log.md`**: Append an entry: `## [YYYY-MM-DD] ingest | YYYY_Keywords`.

### Step 5: Synthesis Refresh (batch ingestions or when requested)
* Update `research_gaps.md`, `progress_summary_and_research_gaps.md`, `proposed_architectures.md`, and `transformer_research_ideas.md`: correct paper counts, gap mappings, and novelty claims to match the current corpus.

---

## 3b. Model-Agnostic Quality Gates (G1-G8) — hard fails, any fail = ingest incomplete

Before marking any ingest done, every gate in `.agents/skills/ingest-paper/SKILL.md` must pass. A weaker model that skips a gate is not faster — it is incorrect.
| Gate | Checks |
|------|--------|
| G1 Headings verbatim | 6 headings exact copy-paste from template (including emoji) |
| G2 Full-text read | Every page of `scratch/txt/*.txt` read, citations beyond abstract |
| G3 Equations verbatim | ALL equations as `$$...\tag{}$$` with original symbols |
| G4 Numbers not invented | Concrete values or `not extractable` with source |
| G5 Frontmatter complete | 8 required keys + `tags`, concepts as `[[Wikilink]]` |
| G6 No ghost stubs | No `[[YYYY_...]]` to non-existent `wiki/papers/*.md` |
| G7 Propagation complete | Every frontmatter concept has a Literature Usage bullet |
| G8 Catalogs + digest | `paper_index.md`/`index.md`/`thesis_references.bib`/`dataset_extraction_report.md` + `python gen_paper_digest.py` |

## 4. Query & Synthesis Rules

When asked synthesis questions (e.g. *"What are the most common deep learning architectures used for day-ahead EV load forecasting?"*):
1. Scan `index.md` and relevant pages in `wiki/models/`, `wiki/horizons/`, and `wiki/metrics/`.
2. Synthesize an answer with comparative markdown tables.
3. Offer to file high-value synthesis back into `research_gaps.md` or a new note in `wiki/`.

---

## 5. Maintenance / Lint Rules

Periodically run a health check:
- Check for orphan notes without inbound links.
- Check for unresolved wikilinks (targets that don't exist as files).
- Check for duplicate concept names (same entity under different spellings) and consolidate.
- Highlight conflicting performance claims between papers.
- Verify paper-note metadata (years, DOIs) against source PDFs — corrections always go through `log.md`.

**Conflict policy**: When an old note contradicts the source PDF, the PDF wins. Record the correction in `log.md`. Never fabricate numbers, equations, or citations — mark unverifiable items explicitly.
