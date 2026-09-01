---
name: ingest-paper
description: >-
  Use this skill to ingest a new PDF research paper into the Thesis vault, extract its full text,
  create the paper note, and propagate it throughout the knowledge graph.
---

# Ingest Paper Skill (`/ingest-paper`)

This skill defines the end-to-end workflow for ingesting a research paper PDF into the EV Charging Demand Load Forecasting Research Wiki.

---

## Prerequisites & Critical Rules

1. **UTF-8 Encoding Only:** ALWAYS read/write files using Python with `encoding="utf-8"`. NEVER use PowerShell `Add-Content` / `Set-Content` as they corrupt non-ASCII characters.
2. **Immutable Source:** Never modify the original PDF in `raw_sources/` (except renaming if the filename is highly misleading). Staging PDFs live in `raw_sources/New/` — copy to `raw_sources/YYYY_FirstAuthor_Keywords.pdf` after duplicate checks.
3. **Truth Source:** If old notes conflict with the PDF, the PDF always wins.
4. **Mandatory Script Execution:** The one-file AI digest (`paper_digest.md`) MUST be regenerated at the end of ingestion by running `python gen_paper_digest.py`.

---

## Workflow Steps

### Step 0: Pre-flight Checks

- Verify the PDF exists (staging: `raw_sources/New/*.pdf` or canonical: `raw_sources/*.pdf`).
- Ensure the filename convention is `YYYY_FirstAuthor_Keywords.pdf` (year verified against PDF text). For staging files this determines the canonical name.
- Read `schema.md` to refresh the exact note template.

### Step 0b: Duplicate Check — 3 Places (mandatory, before any extraction)

Run **all three** checks; if any hits, skip ingestion and log the duplicate:

1. **(a) `raw_sources/*.pdf` — basename / arXiv ID** — Does a canonical PDF with the same arXiv ID or normalized basename already exist?
   ```bash
   ls raw_sources/*<keyword>*.pdf
   # compare arXiv:YYMM.NNNNN or normalized title
   ```
2. **(b) `wiki/papers/*.md` — paper note** — Does `wiki/papers/YYYY_FirstAuthor_*.md` for this paper already exist (even under a different PDF filename)?
   ```bash
   ls wiki/papers/*<FirstAuthor>* wiki/papers/*<Keyword>*
   ```
3. **(c) Content uniqueness — PDF text** — Do title / DOI / arXiv ID inside the PDF match a paper already ingested under a different filename? Open the PDF or check `scratch/txt/*.txt`; use title/DOI hash if needed.
   - *Example: `2604.19841v1.pdf` had no hit in (a) but matched `2026_Bouaachra_INLA...` in (c) → skipped.*

- If **any** of (a)(b)(c) hits → **skip ingestion**, append `duplicate — already ingested as [[Existing_Paper]]` to `log.md`, and delete the staging file in `raw_sources/New/` if it is an exact duplicate.
- If all clear → copy staging PDF to `raw_sources/YYYY_FirstAuthor_Keywords.pdf` (canonical name, year verified against PDF text). Keep the staging original until the full ingestion is verified (Definition of Done).

### Step 1: Extract Full Text

- Use Python's `fitz` (PyMuPDF) to extract the complete text of the PDF.
- Save the output to `scratch/txt/<pdf_basename>.txt`.
- *Note: If a text file >1KB already exists for this PDF, skip extraction and reuse it.*
- **Canonical txt copy:** After extraction (or reuse), copy the txt to its canonical name as well so both names resolve: `scratch/txt/<staging_basename>.txt` ↔ `scratch/txt/YYYY_FirstAuthor_Keywords.txt` (same content, two filenames). This prevents re-extraction when the PDF was renamed.
- **Read every page of the extracted text.** Do not summarize from the abstract alone.

### Step 2: Write the Paper Note

Create `wiki/papers/YYYY_FirstAuthor_Keywords.md` strictly following the `schema.md` template:

1. **Frontmatter:** Populate all required fields (`title`, `authors`, `year`, `journal_conference`, `doi_url`, `models_used`, `datasets_used`, `features_used`, `forecasting_horizon`, `metrics`, `tags`).
2. **Equations:** Extract ALL key equations verbatim from the text using LaTeX `$$...$$` blocks.
3. **Datasets & Links:** Extract exact dataset names, URLs, GitHub repos, and Zenodo DOIs (place in both frontmatter and the Dataset section).
4. **Performance:** Extract concrete numerical results vs baselines. Never invent values.
5. **BibTeX:** Include the full BibTeX citation and interlink to foundation papers.

### Step 3: Propagate Concepts

Search for existing concepts before creating new ones to avoid duplicates.

- **Alias lookup first** — before creating `wiki/datasets/<name>.md`, check the canonical alias map in `AGENTS.md` (e.g., `[[Electricity]]` → `Electricity_ECL.md`, `[[Solar]]` → `Solar_Dataset.md`, `[[Weatherbench]]` → `Weather.md`). Reuse the canonical file; do not create `Electricity.md` alongside `Electricity_ECL.md`. If a new alias is encountered, add it to the map in `AGENTS.md` and create a redirect stub.

Update the "Literature Usage" or "Used-by" lists in the following directories:

- `wiki/models/`
- `wiki/datasets/`
- `wiki/features/`
- `wiki/metrics/`
- `wiki/horizons/`
- `wiki/hyperparameters/` — **optional**: if the paper has no explicit HPO (no Optuna/GridSearch/TPE, only a training schedule like `2048→8192` ctx), skip this folder rather than forcing an entry.
- `wiki/github/` (and `wiki/references/github_repositories_index.md`)

### Step 4: Update Catalogs & Generate Digest

1. **Master Index:** Add the new paper note under `## 📄 Paper Summaries` in `index.md`.
2. **Dataset Report:** Append discovered datasets and URLs to `dataset_extraction_report.md`.
3. **Generate Digest:** Run `python gen_paper_digest.py` from the vault root to rebuild `paper_digest.md`.
4. **Action Log:** Append an entry to `log.md`:
   ```markdown
   ## [YYYY-MM-DD] ingest | <paper name>
   - Extracted text to scratch.
   - Created paper note.
   - Propagated to (list concepts).
   - Regenerated digest.
   ```
5. **Final verify (Definition of Done):** Before deleting `raw_sources/New/<original>.pdf`, run:
   ```bash
   py -3 scratch/audit_corrected.py
   py -3 scratch/verify_final.py
   # expect: models/datasets/features/metrics/horizons all OK, catalogs 11/11 OK
   ```
   Or invoke the `vault-audit` skill when available. All 8 checklist items in `AGENTS.md` → Definition of Done must pass.

### Step 5: Refresh Synthesis Docs (Optional/Batch)

If requested, update `research_gaps.md`, `progress_summary_and_research_gaps.md`, `proposed_architectures.md`, and `transformer_research_ideas.md` to reflect the new findings.

### Step 6: Cleanup Staging

After Definition of Done passes, delete the original staging file `raw_sources/New/<original>.pdf` (the canonical copy in `raw_sources/` is now the source of truth). Record the deletion in the `log.md` entry.
