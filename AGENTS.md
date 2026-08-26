# Thesis Workspace Instructions

> **MANDATORY FIRST STEP**: Read `schema.md` before doing ANY work in this vault. It defines the wiki architecture, the paper-note template, and all ingestion/maintenance rules. This file (`AGENTS.md`) adds the ordered workflow and maintenance policies on top of it.

## Paper ingestion

- When ingesting a new paper, add its name to `raw_sources/paper_index.md` with the next sequential number and a link to the relevant PDF file.
- Before every ingestion, study existing notes and patterns in use so new entries stay consistent.
- After ingestion, update all related data across every designated folder — not just the source folder.

---

# Paper Ingestion Rules: Dataset & Long Link Extraction

When ingesting research papers in this workspace, ALWAYS adhere to the following rules:

1. **Mandatory Dataset & URL Extraction**:
   - Thoroughly scan the paper text, footnotes, page annotations, and Data Availability statements for:
     - Specific Dataset Names & Locations.
     - Exact URLs, Long Web Links, GitHub Code & Data Repositories, Zenodo DOIs, Kaggle links, or Government Open Data Portals.
     - Data Accessibility status (Public / Open-Source / Request Required / Proprietary).

2. **Documenting Datasets**:
   - List extracted dataset names and links under `datasets_used` in the frontmatter of the paper note.
   - Include direct clickable links and long URLs in the `## 📊 Dataset & Input Features` section of the paper summary note.
   - Create or update the corresponding dataset page in `wiki/datasets/`.

---

# Standard Ingestion Workflow (in order — complete every step)

Follow this order for every ingestion. Do not skip steps.

### Step 0 — Pre-flight
1. Read `schema.md` and 2–3 recent notes in `wiki/papers/` to lock the format.
2. Verify the PDF filename matches the actual content (year + key concept/author). If the name is wrong, flag or fix it **before** creating the note (e.g., the Cheng VMD-Prophet-LSTM case: filename said "Federated" but the content is not federated learning).

### Step 1 — Extract full text
3. Extract full PDF text with pymupdf (`fitz`) → save to `scratch/txt/<filename>.txt`. Read every page; never summarize from the abstract alone.

### Step 2 — Write the paper note
4. Create/rewrite `wiki/papers/YYYY_FirstAuthor_Keywords.md` using the template in `schema.md`:
   - Complete YAML frontmatter: title, authors, year, journal_conference, doi_url, models_used, datasets_used, features_used, forecasting_horizon, metrics, tags
   - Extract ALL key equations verbatim from the text → LaTeX ($$...$$), naming each equation.
   - Datasets: name, location, size (#sessions/#stations), resolution, **every URL/DOI/GitHub link found**.
   - Performance: real numbers vs baselines — **never invent values**; if a table is unreadable, state "not extractable".
   - Complete BibTeX + citation-graph wikilinks to foundation papers in the vault.
5. Verify metadata (year, DOI, author names) against the PDF text itself — past notes have had wrong years/DOIs.

### Step 3 — Propagate to concept pages (mandatory!)
6. `wiki/models/` — update "Literature Usage" of every model used by the paper (+ create a new page if it is a major architecture with no page yet).
7. `wiki/datasets/` — create the dataset page if missing / update Used-by list + URLs.
8. `wiki/features/`, `wiki/metrics/`, `wiki/horizons/`, `wiki/hyperparameters/` — add citing bullets referencing this paper.
9. `wiki/github/` + `wiki/references/github_repositories_index.md` — add newly discovered official repos (check for duplicates first).

### Step 4 — Update catalogs & reports
10. `index.md` — add the paper under `## 📄 Paper Summaries`.
11. `dataset_extraction_report.md` — append new datasets/URLs (append-only).
12. `log.md` — add an entry: `## [YYYY-MM-DD] ingest | <paper name>` summarizing what was done.
13. **Regenerate the one-file AI digest**: run `python gen_paper_digest.py` from the vault root so `paper_digest.md` includes the new paper (see section "One-File Paper Digest" below — never hand-edit it).

### Step 5 — Synthesis docs (for batch ingestions or when requested)
13. `research_gaps.md`, `progress_summary_and_research_gaps.md`, `proposed_architectures.md`, `transformer_research_ideas.md` — update paper counts, gap mappings, and novelty claims to match the current corpus.

---

# One-File Paper Digest (`paper_digest.md`)

- `paper_digest.md` at the vault root is a GENERATED, self-contained summary of ALL notes in `wiki/papers/`. Its purpose: an AI agent can read this ONE file and immediately know what every paper did (contribution, method core, key results, and the full limitations/gaps section) to make research-gap identification fast.
- **It is mandatory output of every ingestion** (Step 4, item 13): after adding any paper note, run `python gen_paper_digest.py` from the vault root. Also rerun it after any batch edit of notes in `wiki/papers/` or template changes.
- **Never hand-edit `paper_digest.md` entries.** The source of truth is always the per-paper note in `wiki/papers/` — fix the note, then regenerate.
- If the paper-note template in `schema.md` changes (frontmatter keys or section headers), update `gen_paper_digest.py` accordingly so extraction stays correct.
- Record regeneration in `log.md` (a one-line note inside the ingestion entry is enough; no separate entry needed).

---

# Maintenance Rules

- **Encoding**: ALWAYS write/append to vault files with Python (`open(..., encoding="utf-8")`) or an editor that guarantees UTF-8. NEVER use PowerShell `Add-Content`/`Set-Content` — they default to ANSI and corrupt non-ASCII text (this already happened once to `dataset_extraction_report.md`).
- `raw_sources/` is immutable — never modify existing PDF contents (renaming allowed only when a filename is wrong/misleading vs. the actual content).
- `scratch/txt/` stores extracted text for reuse — if a file already exists at >1KB, do not re-extract.
- When old notes conflict with the source PDF → **the PDF always wins**, and record the correction in `log.md`.
- Avoid duplicate concept names in frontmatter (e.g., ACN_Data vs ACN_Dataset vs Caltech_ACN_Dataset) — check existing pages in `wiki/datasets/` before introducing a new name.
