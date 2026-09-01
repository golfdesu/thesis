---
name: extract-datasets
description: >-
  Use this skill to aggressively hunt for hidden datasets, GitHub repos, DOIs, and long URLs
  inside a research paper, ensuring no data source goes undocumented.
---

# Dataset & Link Extraction Skill (`/extract-datasets`)

This skill defines the rigorous protocol for finding and documenting datasets and open-source code links within research papers. EV Charging load forecasting heavily relies on identifying obscure real-world datasets.

---

## Key Principles & Rules

1. **Rule of Deep Scanning:** Do not just rely on the Abstract or "Data Availability" section. URLs are often buried in footnotes, table captions, appendix sections, or embedded as hyperlinks in text.
2. **Rule of Exactness:** Extract exact URLs (e.g., `https://github.com/author/repo`, `https://doi.org/10.5281/zenodo.1234567`). If a link is dead, note it but still extract it.
3. **No Paraphrasing:** Dataset names must be extracted exactly as the authors refer to them — then map to the canonical vault file via the alias table in `AGENTS.md`.
4. **Rule of Long URL Capture:** Use the regex `https?://[^\s\)"\]]+` (and scan rendered PDF link annotations) to capture long URLs that simple keyword search misses. This catches Hugging Face, Figshare, IEEE DataPort, and unwrapped URLs split across lines.
5. **Rule of Variant Disambiguation:** Common names like `Solar`, `Electricity`, `Weather` have multiple variants — always record which variant the paper actually used (see Step 2).

---

## Workflow Steps

### Step 1: Text & Footnote Scanning

- Open the extracted text of the paper (`scratch/txt/<filename>.txt`).
- **Regex sweep first:** run `https?://[^\s\)"\]]+` over the full text to capture every URL, then classify each hit (GitHub / Zenodo / Kaggle / Hugging Face / Figshare / IEEE DataPort / publisher DOI / open-data portal).
- **Keyword sweep second:** grep for `http`, `https`, `github`, `gitlab`, `zenodo`, `kaggle`, `doi`, `huggingface.co/datasets`, `figshare`, `ieee-dataport`, `IEEE DataPort`, `Mendeley Data`, `dataset`, `data available`, `available at`, `open source`, `repository`, `supplementary material`.
- Scan all footnotes, table captions, appendix sections, and the References/Bibliography section for links (footnotes often hold the only copy of a URL).
- For scanned PDFs with no text layer, check PDF link annotations directly via `fitz` (`page.get_links()`).

### Step 2: Document the Dataset

For every dataset found:

1. **Name:** Extract the formal name exactly as authors write it (e.g., `Caltech ACN`, `Palo Alto EV`, `Shenzhen ST-EVCDP`). Then resolve to the canonical vault file via `AGENTS.md` alias map (e.g., `Solar` → `Solar_Dataset.md`, `Electricity` → `Electricity_ECL.md`).
2. **Variant disambiguation (mandatory for ambiguous names):**

   | Short name | Variants — record which one the paper used |
   |---|---|
   | `Solar` | LSTNet Alabama 137 PV plants (2006, 5-min) vs. Open Power System Data vs. other — note #plants, resolution, region, and citation |
   | `Electricity` / `ECL` | UCI ElectricityLoadDiagrams20112014 (321 clients, hourly, 2012-2014) vs. other — note #clients and years |
   | `Weather` / `Weatherbench` | Max Planck Jena (21 vars, 10-min) vs. Weatherbench2 (ERA5) — note source and vars |
   | `Traffic` / `Wiki_Pageviews` | Note city/region and time span |

   If the paper does not state the variant clearly, write "variant not specified in paper — likely <best guess> (needs confirmation)" and flag it.

3. **Location/URL:** Record the direct URL (use the regex hit, not a paraphrase).
4. **Metadata:** Extract size (e.g., number of charging sessions, number of stations, time span) and resolution (e.g., 15-minute, 1-hour).
5. **Accessibility:** Determine if it is Public, Open-Source, Request Required, or Proprietary/Confidential (check Data Availability statement + license).

### Step 3: Vault Integration

1. **Paper Note:** Add the dataset name to the `datasets_used` YAML frontmatter (as a `[[wikilink]]` — use the frontmatter alias, e.g., `[[Solar]]` is fine even though the file is `Solar_Dataset.md`). Detail the dataset fully in the `## 📊 Dataset & Input Features` section of the paper note (include variant, size, resolution, and every URL/DOI).
2. **Dataset Hub:** Create or update the standalone dataset page in `wiki/datasets/` under its **canonical** filename (alias-aware). Update Used-by list + URLs + variant note.
3. **Extraction Report:** Append the findings to `dataset_extraction_report.md` at the vault root using Python/UTF-8 (append-only, never overwrite).

### Step 4: Code Repository Extraction

If a GitHub or code repository is found:

1. Add it to the dataset/features section of the paper note.
2. Add it to `wiki/github/` (check `github_repositories_index.md` for duplicates first — search by URL, not just repo name).
3. Add it to `wiki/references/github_repositories_index.md`.
