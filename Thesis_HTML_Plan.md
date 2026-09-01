# HTML Research Knowledge Base Plan for Thesis

## Goal

Build a readable HTML research knowledge base from the Thesis folder. It should support expandable folders, fast search, future data growth, and later use as a dataset, API, dashboard, or commercial product.

## Current Data Structure

- `wiki/papers/` — research paper summaries
- `wiki/models/` — models and architectures
- `wiki/datasets/` — datasets and testbeds
- `wiki/features/` — input variables and features
- `wiki/metrics/` — evaluation metrics
- `wiki/references/` — references and citation data
- `raw_sources/` — original PDF files
- `data/*.json` — future metadata and relationship files

Markdown and JSON should remain the source of truth. HTML should be generated from them and should not be edited manually.

## Main Website Features

- Expandable folder tree in the sidebar
- Expand All / Collapse All buttons
- Search by paper, model, dataset, metric, and keyword
- Filters by year, model type, dataset, and forecast horizon
- A detail page for every item
- Links between papers, models, datasets, and metrics
- Links to original PDFs, DOI pages, code, and datasets
- Source, verification, and license status
- Offline-friendly static website
- Ability to add new categories without changing the core template

## Dark Mode and Light Mode

Every page must support a consistent theme switcher.

Requirements:

- Add a clearly visible Dark Mode / Light Mode button in the header
- Use CSS variables such as `--bg`, `--surface`, `--text`, `--muted`, `--border`, and `--accent`
- Detect the initial theme from `prefers-color-scheme`
- Save the user's choice in `localStorage`
- Restore the selected theme on the next visit
- Check contrast for body text, tables, links, code blocks, and forms
- Add `aria-label` and keyboard support to the theme button
- Avoid hard-coded colors inside components; use CSS variables instead
- Prevent visible layout jumps when changing themes

Theme flow:

~~~text
Open website
    ↓
Read localStorage
    ↓ if no saved value
Use prefers-color-scheme
    ↓
Set data-theme on <html>
    ↓
User toggles theme
    ↓
Update theme and save the new value
~~~

## Responsive Design for All Screen Ratios

Use a mobile-first layout that works on phones, tablets, laptops, desktop monitors, and ultrawide displays.

Requirements:

- Use CSS Grid and Flexbox instead of fixed positioning
- Use flexible units such as `%`, `fr`, `minmax()`, and `clamp()`
- Use a container such as `width: min(100% - 2rem, 1440px)`
- Keep the sidebar visible on desktop
- Convert the sidebar into a drawer or collapsible menu on small screens
- Reflow content naturally on portrait and landscape screens
- Wrap long URLs or provide horizontal scrolling for them
- Put large tables and diagrams inside responsive scroll containers
- Use responsive typography with `clamp()`
- Avoid fixed widths that create unnecessary horizontal overflow
- Support keyboard navigation, touch targets, and 200% browser zoom

Recommended test widths:

- 320px
- 375px
- 768px
- 1024px
- 1440px
- 2560px

Suggested layouts:

~~~text
Desktop: Header
         Sidebar Tree | Main Content | Optional Info Panel

Tablet:  Header
         Sidebar Drawer | Main Content

Mobile:  Header + Menu Button
         Main Content
         Wide tables and diagrams scroll horizontally
~~~

## Standard Metadata Schema

~~~yaml
id: 2024_Li_DiffPLF
title: DiffPLF Conditional Diffusion
year: 2024
category: probabilistic-forecasting
models:
  - Transformer
  - Diffusion
datasets:
  - ACN-Data
forecast_horizon:
  - short-term
metrics:
  - MAE
  - RMSE
  - CRPS
doi: ""
source_pdf: "../raw_sources/..."
dataset_url: ""
code_url: ""
status: verified
license: unknown
commercial_use: restricted
~~~

Include `license`, `commercial_use`, `source_type`, and `verification_status` from the beginning.

## Recommended Project Structure

~~~text
Thesis/
├── content/
│   ├── papers/
│   ├── models/
│   ├── datasets/
│   ├── features/
│   └── metrics/
├── data/
│   ├── papers.json
│   ├── datasets.json
│   ├── relationships.json
│   └── taxonomy.json
├── raw_sources/
├── site/
│   ├── index.html
│   ├── assets/
│   └── search-index.json
├── scripts/
│   ├── build_site.py
│   ├── validate_data.py
│   └── generate_index.py
└── README.md
~~~

## Recommended Technologies

- Python for reading Markdown/JSON and building the site
- `markdown-it-py` or another Markdown parser
- Static HTML, CSS, and JavaScript
- HTML `<details>` and `<summary>` for expandable folders
- Fuse.js or Lunr.js for offline search
- Mermaid for architecture and relationship diagrams
- JSON search indexes for fast filtering

## Build Pipeline

~~~text
Markdown + JSON + PDF metadata
            ↓
       Validate schema
            ↓
      Generate search index
            ↓
       Render HTML pages
            ↓
       Copy CSS/JS/assets
            ↓
      Test responsive layout and themes
            ↓
           site/
~~~

Provide one build command, for example:

~~~bash
python scripts/build_site.py
~~~

## Implementation Phases

1. Define the metadata schema and stable IDs
2. Detect duplicate filenames and missing metadata
3. Build the Markdown-to-HTML parser
4. Build the Dashboard and expandable Tree View
5. Add Expand All / Collapse All
6. Add search and filters
7. Connect papers, models, datasets, and metrics
8. Add Dark Mode / Light Mode and saved preferences
9. Implement mobile-first responsive layout
10. Test multiple screen sizes and aspect ratios
11. Add validation and missing-data reports
12. Automate the build process
13. Prepare JSON, CSV, API, or dashboard exports

## Future Commercial Use

If “selling the data” means future commercial use, focus on original value-added products such as:

- Structured metadata and research indexes
- Model comparison tables
- Benchmark results
- Taxonomies and knowledge graphs
- Original annotations and analysis
- Search APIs or research dashboards

Do not redistribute or sell copyrighted PDFs or copied paper text directly. Check the permissions for publishers, DOI content, datasets, and code repositories before publication.

Separate the data into:

~~~text
public/       Data that can be openly shared
private/      Personal or unverified data
commercial/   Data with clearly defined usage rights
~~~

## Definition of Done

- Folders can be expanded and collapsed
- Search and filters work
- Dark Mode and Light Mode work on every page
- The selected theme is remembered
- The layout works from mobile screens to ultrawide displays
- No unnecessary horizontal overflow
- Cross-links work correctly
- Metadata and license status are visible
- Adding a new paper does not require changing the main template
- Data can be exported for another AI system, API, or dashboard

