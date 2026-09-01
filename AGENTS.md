# Thesis Workspace Instructions

> **MANDATORY FIRST STEP**: Read `schema.md` before doing ANY work in this vault. It defines the wiki architecture, the paper-note template, and all ingestion/maintenance rules. This file (`AGENTS.md`) adds the ordered workflow and maintenance policies on top of it.

---

## Agent Skills Architecture (`.agents/skills/`)

**Source of truth**: `.agents/skills/` — the canonical skill runbooks. `.claude/skills` is a **Junction** (`New-Item -ItemType Junction`) pointing to `.agents/skills` so both Claude Code (`.claude/`) and Antigravity (`.agents/`) discover the same files. Never edit skills via `.claude/skills` directly — edit under `.agents/skills/`.

| Skill Name | Location | Description & Primary Use Case |
|---|---|---|
| `ingest-paper` | `.agents/skills/ingest-paper/SKILL.md` | Master end-to-end workflow: PDF text extraction, paper note, knowledge-graph propagation. |
| `extract-datasets` | `.agents/skills/extract-datasets/SKILL.md` | Aggressive hunting protocol for buried URLs, GitHub repos, and DOIs inside PDFs. |
| `thesis-query` | `.agents/skills/thesis-query/SKILL.md` | Synthesizing answers using `paper_digest.md` with strict Wikilink formatting. |
| `refresh-synthesis` | `.agents/skills/refresh-synthesis/SKILL.md` | Runs `gen_paper_digest.py` / `scan_datasets.py` and refreshes gap/progress docs. |

---

## Staging Inbox & Canonical Storage

- **Inbox**: `raw_sources/New/` — drop newly downloaded PDFs here (keeps `raw_sources/` clean and makes duplicate checks explicit).
- **Canonical**: `raw_sources/YYYY_FirstAuthor_Keywords.pdf` — after passing duplicate checks, **copy** (not move) the PDF from `New/` to `raw_sources/` under its canonical name (`YYYY` = publication year, verified against PDF text). This is the immutable record.
- **Cleanup**: After `wiki/papers/*.md` + `scratch/txt/*.txt` + catalogs are verified, delete the original in `raw_sources/New/` (the canonical copy is now the source of truth).

```
raw_sources/New/2310.10688v4.pdf  --copy+rename-->  raw_sources/2024_Das_TimesFM_Decoder_Only_Foundation_Model.pdf
raw_sources/New/2605.20119v2.pdf  --copy+rename-->  raw_sources/2026_Khwaja_Toto_2_Scaling_Era.pdf
```

---

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
2. **Duplicate check — 3 places (mandatory, before any extraction)**:
   - **(a) `raw_sources/*.pdf` — basename / arXiv ID**: Does a canonical PDF with the same arXiv ID or normalized basename already exist? (`ls raw_sources/*<keyword>*`, compare `arXiv:YYMM.NNNNN`).
   - **(b) `wiki/papers/*.md` — paper note**: Does `wiki/papers/YYYY_FirstAuthor_*.md` for this paper already exist (even under a different PDF filename)?
   - **(c) Content uniqueness — PDF text**: Do title / DOI / arXiv ID inside the PDF match a paper already ingested under a different filename? (Open the PDF or check `scratch/txt/*.txt`; use title/DOI hash if needed.)
   - If **any** of (a)(b)(c) hits → **skip ingestion**, record `duplicate — already ingested as [[Existing_Paper]]` in `log.md`, and delete the staging file in `raw_sources/New/` if it is an exact duplicate.
   - *Example: `2604.19841v1.pdf` had no basename hit in (a) but matched `2026_Bouaachra_INLA...` in (c) → skipped.*
3. Verify the PDF filename matches the actual content (year + key concept/author). If the name is wrong, flag or fix it **before** creating the note (e.g., the Cheng VMD-Prophet-LSTM case: filename said "Federated" but the content is not federated learning). For staging files, this determines the canonical name in `raw_sources/`.
4. Copy the staging PDF from `raw_sources/New/` to `raw_sources/YYYY_FirstAuthor_Keywords.pdf` under its canonical name (year verified against PDF text). Keep the staging original until the full ingestion is verified.

### Step 1 — Extract full text

5. Extract full PDF text with pymupdf (`fitz`) → save to `scratch/txt/<filename>.txt`. Read every page; never summarize from the abstract alone.
6. **Reuse & canonical copy**: If `scratch/txt/<pdf_basename>.txt` already exists at **>1KB**, skip extraction and reuse it. After extraction (or reuse), **copy** the txt to its canonical name as well so both names resolve: `scratch/txt/<staging_basename>.txt` ↔ `scratch/txt/YYYY_FirstAuthor_Keywords.txt` (same content, two filenames). This prevents re-extraction when the PDF was renamed.

### Step 2 — Write the paper note

7. Create/rewrite `wiki/papers/YYYY_FirstAuthor_Keywords.md` using the template in `schema.md`:
   - Complete YAML frontmatter: title, authors, year, journal_conference, doi_url, models_used, datasets_used, features_used, forecasting_horizon, metrics, tags
   - Extract ALL key equations verbatim from the text → LaTeX ($$...$$), naming each equation.
   - Datasets: name, location, size (#sessions/#stations), resolution, **every URL/DOI/GitHub link found**.
   - Performance: real numbers vs baselines — **never invent values**; if a table is unreadable, state "not extractable".
   - Complete BibTeX + citation-graph wikilinks to foundation papers **ONLY IF** they are already ingested in the vault. Do not wrap external references in `[[ ]]` (e.g., `[[Bahdanau2016]]`) if the PDF is not in our `raw_sources/`, as it creates ghost stub files. Use plain text for external refs.
8. Verify metadata (year, DOI, author names) against the PDF text itself — past notes have had wrong years/DOIs.

### Step 3 — Propagate to concept pages (mandatory!)

9. `wiki/models/` — update "Literature Usage" of every model used by the paper (+ create a new page if it is a major architecture with no page yet).
10. `wiki/datasets/` — create the dataset page if missing / update Used-by list + URLs. **Alias lookup first** — check the canonical map below before creating a new file (to avoid `ACN_Data` vs `Caltech_ACN` or `Electricity` vs `Electricity_ECL` duplicates).
11. `wiki/features/`, `wiki/metrics/`, `wiki/horizons/`, `wiki/hyperparameters/` — add citing bullets referencing this paper. **Hyperparameters are optional** — if the paper has no explicit HPO (e.g., no Optuna/GridSearch/TPE, only a training schedule like `2048→8192` ctx), skip this folder rather than forcing an entry.
12. `wiki/github/` + `wiki/references/github_repositories_index.md` — add newly discovered official repos (check for duplicates first).

### Step 4 — Update catalogs & reports

13. `index.md` — add the paper under `## 📄 Paper Summaries`.
14. `dataset_extraction_report.md` — append new datasets/URLs (append-only).
15. `log.md` — add an entry: `## [YYYY-MM-DD] ingest | <paper name>` summarizing what was done (including which duplicate checks were run).
16. **Regenerate the one-file AI digest**: run `python gen_paper_digest.py` from the vault root so `paper_digest.md` includes the new paper (see section "One-File Paper Digest" below — never hand-edit it).

### Step 5 — Synthesis docs (for batch ingestions or when requested)

17. `research_gaps.md`, `progress_summary_and_research_gaps.md`, `proposed_architectures.md`, `transformer_research_ideas.md` — update paper counts, gap mappings, and novelty claims to match the current corpus.

---

# One-File Paper Digest (`paper_digest.md`)

- `paper_digest.md` at the vault root is a GENERATED, self-contained summary of ALL notes in `wiki/papers/`. Its purpose: an AI agent can read this ONE file and immediately know what every paper did (contribution, method core, key results, and the full limitations/gaps section) to make research-gap identification fast.
- **It is mandatory output of every ingestion** (Step 4, item 16): after adding any paper note, run `python gen_paper_digest.py` from the vault root. Also rerun it after any batch edit of notes in `wiki/papers/` or template changes.
- **Never hand-edit `paper_digest.md` entries.** The source of truth is always the per-paper note in `wiki/papers/` — fix the note, then regenerate.
- If the paper-note template in `schema.md` changes (frontmatter keys or section headers), update `gen_paper_digest.py` accordingly so extraction stays correct.
- Record regeneration in `log.md` (a one-line note inside the ingestion entry is enough; no separate entry needed).

---

# Definition of Done — Ingest Checklist

Before marking an ingest complete (and before deleting `raw_sources/New/<original>.pdf`), verify **all 8**:

| # | Artifact | Check |
|---|----------|-------|
| 1 | `wiki/papers/YYYY_*.md` | Paper note exists, frontmatter complete, equations/BibTeX present |
| 2 | `wiki/references/YYYY_*_refs.md` | Refs dump exists (if paper has references) |
| 3 | `wiki/models/` etc. | Every `models_used` / `datasets_used` / `features_used` / `metrics` / `forecasting_horizon` entry has a citing bullet (alias-aware) |
| 4 | `wiki/github/` + `github_repositories_index.md` | New repos added (or confirmed none) |
| 5 | `raw_sources/paper_index.md` + `index.md` + `thesis_references.bib` | Catalog counts incremented, paper linked |
| 6 | `dataset_extraction_report.md` | New datasets/URLs appended (append-only) |
| 7 | `paper_digest.md` | Regenerated via `python gen_paper_digest.py` and contains the new paper |
| 8 | `log.md` | Entry `## [YYYY-MM-DD] ingest | <paper>` appended |

Quick verify: `py -3 scratch/audit_corrected.py && py -3 scratch/verify_final.py` (or the `vault-audit` skill when available).

---

# Maintenance Rules

- **Encoding**: ALWAYS write/append to vault files with Python (`open(..., encoding="utf-8")`) or an editor that guarantees UTF-8. NEVER use PowerShell `Add-Content`/`Set-Content` — they default to ANSI and corrupt non-ASCII text (this already happened once to `dataset_extraction_report.md`).
- `raw_sources/` is immutable — never modify existing PDF contents (renaming allowed only when a filename is wrong/misleading vs. the actual content).
- `scratch/txt/` stores extracted text for reuse — if a file already exists at >1KB, do not re-extract. When a PDF is renamed to its canonical name, copy the txt to the canonical name as well.
- When old notes conflict with the source PDF → **the PDF always wins**, and record the correction in `log.md`.
- **Dataset alias canonical map** — check this before creating a new `wiki/datasets/*.md` to avoid duplicates. Frontmatter wikilink → actual file:

  | Frontmatter `[[...]]` | Canonical file |
  |---|---|
  | `[[Electricity]]` | `Electricity_ECL.md` |
  | `[[Solar]]` | `Solar_Dataset.md` |
  | `[[Weatherbench]]` | `Weather.md` |
  | `[[Wikipedia]]` / `[[Wiki_Pageviews]]` | `Wiki_Pageviews.md` (alias `Wikipedia.md` is a separate concept note) |
  | `[[GIFT_Eval_Pretrain]]` | `GIFT_Eval_Pretrain.md` |

  If a new alias is encountered, add it here and create a redirect stub (or rename) so the wikilink resolves.
- Avoid duplicate concept names in frontmatter (e.g., ACN_Data vs ACN_Dataset vs Caltech_ACN_Dataset) — check existing pages in `wiki/datasets/` before introducing a new name.
