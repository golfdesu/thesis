---
name: ingest-paper
description: >-
  Use this skill to ingest a new PDF research paper into the Thesis vault, extract its full text,
  create the paper note, and propagate it throughout the knowledge graph.
---

# Ingest Paper Skill (`/ingest-paper`)

This skill defines the end-to-end workflow for ingesting a research paper PDF into the EV Charging Demand Load Forecasting Research Wiki.
**It is the ONLY allowed ingest path — regardless of underlying model (gemini, spark, opus, sonnet, local LLM, etc.) every agent MUST follow this file verbatim. No shortcuts.**

---

## Prerequisites & Critical Rules

1. **UTF-8 Encoding Only:** ALWAYS read/write files using Python with `encoding="utf-8"`. NEVER use PowerShell `Add-Content` / `Set-Content` as they corrupt non-ASCII characters.
2. **Immutable Source:** Never modify the original PDF in `raw_sources/` (except renaming if the filename is highly misleading). Staging PDFs live in `raw_sources/New/` — copy to `raw_sources/YYYY_Keywords.pdf` after duplicate checks.
3. **Truth Source:** If old notes conflict with the PDF, the PDF always wins.
4. **Mandatory Script Execution:** The one-file AI digest (`paper_digest.md`) MUST be regenerated at the end of ingestion by running `python gen_paper_digest.py`.
5. **Model-Agnostic Quality Standard (NEW — binding on every model):** Depth and completeness are **not model-dependent**. A paper ingested by gemini MUST be indistinguishable from one ingested by muse-spark/opus. If you are tempted to summarize from the abstract, stop — read every page of `scratch/txt/*.txt`. If a table/equation is hard to parse, state `not extractable` — never invent, never truncate silently.

---

## Model-Agnostic Quality Gates (hard fails — any fail = ingest incomplete)

Before marking an ingest done, **every** gate must pass. A weaker model that skips a gate is not "faster" — it is **incorrect**.

| Gate | What is checked | How to verify |
|------|-----------------|---------------|
| G1 Headings verbatim | 6 headings are **exact copy-paste** from `schema.md` template (including emoji). See Step 2. | `grep "^## " wiki/papers/YYYY_*.md` must match the 6 strings exactly — no paraphrase (`Contribution` vs `Main Objective`) |
| G2 Full-text read | Every page of `scratch/txt/*.txt` was read, not just abstract/intro | Note must cite page/section numbers beyond abstract (e.g., TimeBench Table 4 p.6, Appendix A) |
| G3 Equations verbatim | ALL key equations extracted as `$$...$$` with `\tag{}` and original symbols — **written via Python raw string `r"""` only** (never plain `"""`) | Count `$$` blocks ≥ number of numbered equations in PDF; `grep -P "[\x00-\x08\x0B\x0C\x0E-\x1F]" wiki/papers/YYYY_*.md` must return 0; `grep -c "\\\\tag" == grep -c "ag{"` must not have broken `ag{` without `\` |
| G4 Numbers not invented | Every metric in `## 📈 Performance & Results` has a concrete value or `not extractable` | `grep` for invented-looking round numbers without source table/figure |
| G5 Frontmatter complete | 8 required keys + `tags`, arrays use `[[Wikilink]]` not plain strings | `type/paper` frontmatter parses as YAML; `models_used/datasets_used/metrics` contain `[[` |
| G6 No ghost stubs | No `[[YYYY_Author_Title]]` wikilink points to a non-existent `wiki/papers/*.md` | `grep -r "\[\[20[0-9][0-9]_"` then check each target exists in `wiki/papers/` or `raw_sources/` |
| G7 Propagation complete | Every concept in frontmatter has a `Literature Usage` bullet on its concept page | `scratch/audit_corrected.py` + `scratch/verify_final.py` (or manual alias-aware check) |
| G8 Catalogs + digest | `paper_index.md`, `index.md`, `thesis_references.bib`, `dataset_extraction_report.md` updated; `paper_digest.md` regenerated | `paper_digest.md` contains the new paper; `paper_index.md` count incremented |

---

## Workflow Steps

### Step 0: Pre-flight Checks

- Verify the PDF exists (staging: `raw_sources/New/*.pdf` or canonical: `raw_sources/*.pdf`).
- Ensure the filename convention is `YYYY_Keywords.pdf` (year verified against PDF text). For staging files this determines the canonical name.
- **Read `schema.md` to refresh the exact note template — COPY-PASTE the 6 headings, do not rephrase.**
- **Read 2–3 recent notes in `wiki/papers/`** (prefer `2026_Khwaja_Toto_2_Scaling_Era.md`, `2024_Das_TimesFM_Decoder_Only_Foundation_Model.md`, `2025_Ansari_Chronos_2_Univariate_to_Universal.md`) to lock tone, table style, and equation formatting.

### Step 0b: Duplicate Check — 3 Places (mandatory, before any extraction)

Run **all three** checks; if any hits, skip ingestion and log the duplicate:

1. **(a) `raw_sources/*.pdf` — basename / arXiv ID** — Does a canonical PDF with the same arXiv ID or normalized basename already exist?
   ```bash
   ls raw_sources/*<keyword>*.pdf
   # compare arXiv:YYMM.NNNNN or normalized title
   ```
2. **(b) `wiki/papers/*.md` — paper note** — Does `wiki/papers/YYYY_*.md` for this paper already exist (even under a different PDF filename)?
   ```bash
   ls wiki/papers/*<FirstAuthor>* wiki/papers/*<Keyword>*
   ```
3. **(c) Content uniqueness — PDF text** — Do title / DOI / arXiv ID inside the PDF match a paper already ingested under a different filename? Open the PDF or check `scratch/txt/*.txt`; use title/DOI hash if needed.
   - *Example: `2604.19841v1.pdf` had no hit in (a) but matched `2026_Bouaachra_INLA...` in (c) → skipped.*

- If **any** of (a)(b)(c) hits → **skip ingestion**, append `duplicate — already ingested as [[Existing_Paper]]` to `log.md`, and delete the staging file in `raw_sources/New/` if it is an exact duplicate.
- If all clear → copy staging PDF to `raw_sources/YYYY_Keywords.pdf` (canonical name, year verified against PDF text). Keep the staging original until the full ingestion is verified (Definition of Done).

### Step 1: Extract Full Text

- Use Python's `fitz` (PyMuPDF) to extract the complete text of the PDF.
- Save the output to `scratch/txt/<pdf_basename>.txt`.
- *Note: If a text file >1KB already exists for this PDF, skip extraction and reuse it.*
- **Canonical txt copy:** After extraction (or reuse), copy the txt to its canonical name as well so both names resolve: `scratch/txt/<staging_basename>.txt` ↔ `scratch/txt/YYYY_Keywords.txt` (same content, two filenames). This prevents re-extraction when the PDF was renamed.
- **Read every page of the extracted text.** Do not summarize from the abstract alone. For long papers (>10 pages), explicitly note the page count you read in `log.md`.

### Step 2: Write the Paper Note — TEMPLATE IS LAW

Create `wiki/papers/YYYY_Keywords.md` strictly following the `schema.md` template. **Copy-paste the template — never regenerate headings from memory.**

**Required headings (exact strings, including emoji — any deviation fails G1):**

```
# Summary: [Paper Title]

## 🎯 Main Objective & Contribution
## 🧠 Methodology & Model Architecture
## 📊 Dataset & Input Features
## 📈 Performance & Results
## 💡 Limitations & Identified Research Gaps
## 📚 BibTeX & Citation Reference
## 🔗 Key References & Citation Graph
```

Bad (fails G1) vs Good:
- Bad: `## Contribution` / `## Method Core` / `## Key Results` — invented, not in schema
- Good: `## 🎯 Main Objective & Contribution` — exact copy

Checklist inside Step 2 (all must be satisfied):

1. **Frontmatter (G5):** Populate all required fields (`title`, `authors`, `year`, `journal_conference`, `doi_url`, `models_used`, `datasets_used`, `features_used`, `forecasting_horizon`, `metrics`, `tags`). Every concept that has a `wiki/*/*.md` page MUST be a `[[Wikilink]]` in the array — plain strings are not allowed for known concepts. Verify `year`/`doi_url` against the PDF text itself (not the PDF filename).
2. **Equations (G3):** Extract ALL key equations **verbatim** from the text using LaTeX `$$...$$` display blocks with `\tag{}` and original symbols. Name each equation (e.g., `**Eq. 1 — Conditional OT Flow-Matching**: $$... \tag{1}$$`). Never paraphrase or invent equations. If a symbol is ambiguous in extraction, keep the PDF's notation and add `[as in PDF p.X]` rather than renaming.
3. **Datasets & Links (G4):** Extract exact dataset names, sizes (#sessions/#stations/#points), resolution, and **every** URL/GitHub/Zenodo DOI/Kaggle link / government portal found — place in both frontmatter `datasets_used` and the `## 📊 Dataset & Input Features` section. For large corpora (e.g., TimeBench 1,032B) include the composition table. Create/update `wiki/datasets/*.md` per dataset (alias-aware — see below).
4. **Performance (G4):** Extract concrete numerical results vs baselines with table/figure citations (e.g., `Table 1 p.5`, `Fig. 4`). **Never invent values.** If a results table is unreadable in the txt extraction, write `not extractable — see PDF p.X Table Y` and keep the structure. Include scaling/ablation results when present.
5. **BibTeX & Citation Graph (G6):** Include the full BibTeX citation. Wikilink cited papers as `[[YYYY_Author_Keywords]]` **ONLY IF** the target `wiki/papers/YYYY_Author_*.md` (or `raw_sources/YYYY_*.pdf`) already exists in the vault. Otherwise use plain text (`Author et al. Year (Title)`) — wrapping a non-ingested paper in `[[ ]]` creates a ghost stub and fails G6. When in doubt, use plain text.

After writing the note, self-verify before proceeding:

```bash
# Headings must be exact
grep "^## " wiki/papers/YYYY_Keywords.md
# Frontmatter must contain [[
head -20 wiki/papers/YYYY_Keywords.md | grep -c "\[\["
# No ghost links to non-existent papers (manual: check any [[20??_ that is not in wiki/papers/)
grep -o "\[\[20[0-9][0-9]_[^]]*\]\]" wiki/papers/YYYY_Keywords.md
ls wiki/papers/ | grep -i "<check each>"
```

### Step 3: Propagate Concepts — MANDATORY, ALIAS-AWARE

Search for existing concepts before creating new ones to avoid duplicates.

- **Alias lookup first** — before creating `wiki/datasets/<name>.md`, check the canonical alias map in `AGENTS.md` (e.g., `[[Electricity]]` → `Electricity_ECL.md`, `[[Solar]]` → `Solar_Dataset.md`, `[[Weatherbench]]` → `Weather.md`, `[[ETTh1]]` → `ETT.md`). Reuse the canonical file; do not create `Electricity.md` alongside `Electricity_ECL.md`. If a genuinely new alias is encountered, add it to the map in `AGENTS.md` and create a redirect stub (alias file with `alias_for: "[[Canonical]]"` and a Literature Usage bullet).
- **Ghost-stub guard (G6):** If a concept page `wiki/models/*.md` / `wiki/datasets/*.md` does not exist and the concept is **not** a major architecture/dataset central to the paper's contribution, consider whether it needs a full page or just a plain-text mention. Do not create thin alias stubs for papers that are not ingested — mention them as plain text in `## 🔗 Key References`.

Update the "Literature Usage" or "Used-by" lists in the following directories:

- `wiki/models/` — for every entry in `models_used` (+ create a new page if it is a major architecture with no page yet; follow `Sundial.md` / `Chronos-2.md` as format examples)
- `wiki/datasets/` — create the dataset page if missing / update Used-by list + URLs. For variant datasets (ETTh1/ETTh2/ETTm1/ETTm2/ECL) create alias stubs pointing to the canonical `ETT.md` / `Electricity_ECL.md`.
- `wiki/features/` — add citing bullets referencing this paper
- `wiki/metrics/` — add citing bullets referencing this paper
- `wiki/horizons/` — add citing bullets referencing this paper
- `wiki/hyperparameters/` — **optional**: if the paper has no explicit HPO (no Optuna/GridSearch/TPE, only a training schedule like `2048→8192` ctx), skip this folder rather than forcing an entry.
- `wiki/github/` (and `wiki/references/github_repositories_index.md`) — add newly discovered official repos (check for duplicates first). Each entry must have `Repository URL`, `Cited Paper [[...]]`, and `What you can reuse` (code/data/pretrained).

### Step 4: Update Catalogs & Generate Digest

1. **Master Index:** Add the new paper note under `## 📄 Paper Summaries` in `index.md`.
2. **Dataset Report:** Append discovered datasets and URLs to `dataset_extraction_report.md` as a new numbered section `### N. YYYY_*.pdf` with `Identified Datasets` + `Dataset & Code Links (Direct/Long URLs)` + `Key Dataset Text Snippets / Context` (verbatim quotes with page refs).
3. **References dump:** Create `wiki/references/YYYY_Keywords_refs.md` verbatim from `scratch/txt/*.txt` References section (pp. XX-XX).
4. **Thesis bib:** Append/verify entry in `thesis_references.bib` (with `url`, `eprint`, `archivePrefix`, `primaryClass` when arXiv).
5. **Paper index:** Append to `raw_sources/paper_index.md` with next sequential number.
6. **Generate Digest:** Run `python gen_paper_digest.py` from the vault root to rebuild `paper_digest.md`. Verify `paper_digest.md` contains the new paper: `grep "YYYY_FirstAuthor" paper_digest.md`.
7. **Action Log:** Append an entry to `log.md`:
   ```markdown
   ## [YYYY-MM-DD] ingest | YYYY_Keywords
   - Duplicate check: (a)/(b)/(c) results
   - Extracted text to scratch/txt/*.txt (N lines / X KB, fitz)
   - Created/rewrote wiki/papers/YYYY_*.md to schema template (frontmatter X models, Y datasets, Z eqs)
   - Refs dump: wiki/references/YYYY_*_refs.md (pp. XX-XX)
   - Propagated to (list concepts with paths)
   - Catalogs: paper_index #N, index.md, thesis_references.bib, dataset_extraction_report.md #N
   - Regenerated paper_digest.md (N papers, X KB) via python gen_paper_digest.py
   - Ghost-stub guard: ONLY IF ingested; aliases created: (list)
   ```
8. **Final verify (Definition of Done):** Before deleting `raw_sources/New/<original>.pdf`, run:
   ```bash
   py -3 scratch/audit_corrected.py
   py -3 scratch/verify_final.py
   # expect: models/datasets/features/metrics/horizons all OK, catalogs 11/11 OK
   python gen_paper_digest.py && grep "YYYY_FirstAuthor" paper_digest.md
   ```
   Or invoke the `vault-audit` skill when available. All 8 checklist items in `AGENTS.md` → Definition of Done must pass. If any gate G1-G8 fails, fix it before committing.

### Step 5: Refresh Synthesis Docs (Optional/Batch)

If requested or if batch ingestions changed the corpus materially, update `research_gaps.md`, `progress_summary_and_research_gaps.md`, `proposed_architectures.md`, and `transformer_research_ideas.md` to reflect the new findings (paper counts, gap mappings, novelty claims).

### Step 6: Cleanup Staging

After Definition of Done passes, delete the original staging file `raw_sources/New/<original>.pdf` (the canonical copy in `raw_sources/` is now the source of truth). Record the deletion in the `log.md` entry. Use `git rm` or `Remove-Item` — never leave a staging file that has already been ingested as canonical.
