import os
import re
import json
import shutil
import yaml
import html
from pathlib import Path

OBSIDIAN_DIR = Path(r"C:\Users\chaya\Documents\Obsidian\Thesis")
PROJECT_DIR = Path(r"C:\Users\chaya\Desktop\Thesis_html")
SITE_DIR = PROJECT_DIR / "site"

# Subdirectories in wiki
CATEGORIES = {
    "papers": "Papers & Literature",
    "models": "Models & Architectures",
    "datasets": "Datasets & Benchmarks",
    "features": "Features & Inputs",
    "metrics": "Evaluation Metrics",
    "hyperparameters": "Hyperparameters & Optimization",
    "horizons": "Forecasting Horizons",
    "github": "Code & Repositories",
    "references": "References & Citations",
    "guides": "Research Syntheses & Gaps"
}

CATEGORY_ICONS = {
    "papers": "📄",
    "models": "🧠",
    "datasets": "📊",
    "features": "⚙️",
    "metrics": "📐",
    "hyperparameters": "🎛️",
    "horizons": "🕐",
    "github": "💻",
    "references": "📚",
    "guides": "💡"
}


def ensure_dirs():
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    for cat in CATEGORIES.keys():
        (SITE_DIR / cat).mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "assets").mkdir(parents=True, exist_ok=True)

def parse_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return meta, body
            except Exception:
                pass
    return {}, content.strip()

def extract_title_and_meta(file_path, meta, body):
    file_stem = file_path.stem
    title = meta.get("title") or meta.get("name") or meta.get("dataset")
    if not title:
        # Check first header
        match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        if match:
            title = match.group(1).strip()
        else:
            title = file_stem.replace("_", " ")
    # Strip leading emojis or special icon characters (e.g. 📁, 🧠, 📊, etc.)
    title = re.sub(r"^[^\w\s\(\)\[\]\-\:\,\.\']+", "", title, flags=re.UNICODE).strip()
    # Resolve wiki-links so [[target|alias]] / [[target]] never leak into titles
    def _title_wiki(m):
        target = m.group(1)
        return target.split("|", 1)[1].strip() if "|" in target else target.strip()
    title = re.sub(r"\[\[([^\]]+)\]\]", _title_wiki, title).strip()
    return title

def clean_wiki_target(target):
    # e.g. [[2024_Li_DiffPLF|DiffPLF]] -> target: 2024_Li_DiffPLF, alias: DiffPLF
    if "|" in target:
        target_name, alias = target.split("|", 1)
    else:
        target_name, alias = target, target
    target_clean = target_name.strip().strip("[]")
    return target_clean, alias.strip().strip("[]")

def build_lookup_index():
    lookup = {} # clean_name -> rel_url
    all_pages = []

    # 1. Wiki files
    wiki_dir = OBSIDIAN_DIR / "wiki"
    for cat in CATEGORIES.keys():
        cat_dir = wiki_dir / cat
        if not cat_dir.exists():
            continue
        for f in cat_dir.glob("*.md"):
            rel_url = f"{cat}/{f.stem}.html"
            content = f.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(content)
            title = extract_title_and_meta(f, meta, body)
            
            item = {
                "stem": f.stem,
                "cat": cat,
                "cat_name": CATEGORIES[cat],
                "file_path": f,
                "rel_url": rel_url,
                "meta": meta,
                "body": body,
                "title": title,
                "year": meta.get("year", ""),
                "doi": meta.get("doi_url", "") or meta.get("doi", ""),
                "authors": meta.get("authors", []),
                "journal": meta.get("journal_conference", ""),
                "tags": meta.get("tags", []),
                "incoming_links": [],
                "outgoing_links": []
            }
            all_pages.append(item)
            lookup[f.stem.lower()] = rel_url
            lookup[title.lower()] = rel_url
            # Add short aliases
            if meta.get("name"):
                lookup[meta["name"].lower()] = rel_url

    # 2. Root guide markdown files
    root_files = [
        ("index.md", "Vault Master Index & Overview"),
        ("research_gaps.md", "Research Gaps & Identified Limitations"),
        ("progress_summary_and_research_gaps.md", "Progress Summary & Research Gaps"),
        ("proposed_architectures.md", "Proposed Novel Architectures"),
        ("transformer_research_ideas.md", "Transformer & Diffusion Research Ideas"),
        ("dataset_extraction_report.md", "Dataset Extraction Report"),
        ("schema.md", "Metadata Schema Reference"),
        ("log.md", "Research Activity Log")
    ]
    for filename, display_title in root_files:
        f = OBSIDIAN_DIR / filename
        if f.exists():
            rel_url = f"guides/{f.stem}.html"
            content = f.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(content)
            item = {
                "stem": f.stem,
                "cat": "guides",
                "cat_name": CATEGORIES["guides"],
                "file_path": f,
                "rel_url": rel_url,
                "meta": meta,
                "body": body,
                "title": display_title,
                "year": "",
                "tags": ["guide", "synthesis"],
                "incoming_links": [],
                "outgoing_links": []
            }
            all_pages.append(item)
            lookup[f.stem.lower()] = rel_url
            lookup[display_title.lower()] = rel_url

    return lookup, all_pages

def convert_markdown_to_html(body, current_rel_url, lookup, all_pages_map):
    # Compute relative path prefix to root (e.g. "../" if in a category folder, "" if root)
    depth = len(current_rel_url.split("/")) - 1
    root_prefix = "../" * depth if depth > 0 else "./"

    # Replace Obsidian wiki links [[target]] or [[target|alias]]
    def wiki_repl(match):
        raw_target = match.group(1)
        target_name, alias = clean_wiki_target(raw_target)
        target_key = target_name.lower()
        if target_key in lookup:
            dest = root_prefix + lookup[target_key]
            return f'<a href="{dest}" class="wiki-link" title="Navigate to {html.escape(alias)}">{html.escape(alias)}</a>'
        else:
            return f'<span class="wiki-link-unresolved" title="Unresolved link">{html.escape(alias)}</span>'

    html_text = re.sub(r"\[\[(.*?)\]\]", wiki_repl, body)

    # Protect Math blocks before HTML escaping or line processing
    math_blocks = []
    def save_math_block(match):
        math_blocks.append(match.group(0))
        return f"___MATH_BLOCK_{len(math_blocks)-1}___"

    # Match $$...$$
    html_text = re.sub(r"\$\$(.*?)\$\$", save_math_block, html_text, flags=re.DOTALL)
    # Match \[...\]
    html_text = re.sub(r"\\\[(.*?)\\\]", save_math_block, html_text, flags=re.DOTALL)
    # Match inline $...$
    html_text = re.sub(r"\$([^\$\n]+)\$", save_math_block, html_text)
    # Match inline \(...\)
    html_text = re.sub(r"\\\((.*?)\\\)", save_math_block, html_text)

    # Handle Markdown Callouts / Alerts (> [!NOTE], > [!TIP], > [!IMPORTANT], > [!WARNING], > [!TARGET])
    def parse_callouts(text):
        lines = text.split("\n")
        out_lines = []
        in_callout = False
        callout_type = ""
        callout_title = ""
        callout_content = []

        for line in lines:
            callout_match = re.match(r"^>\s*\[\!(NOTE|TIP|IMPORTANT|WARNING|CAUTION|INFO|TARGET)\]\s*(.*)", line, re.IGNORECASE)
            if callout_match:
                if in_callout:
                    # Flush previous
                    c_body = "<br>".join(callout_content)
                    out_lines.append(f'<div class="callout callout-{callout_type.lower()}"><div class="callout-header"><span class="callout-icon">💡</span> <strong>{html.escape(callout_title or callout_type)}</strong></div><div class="callout-body">{c_body}</div></div>')
                    callout_content = []
                in_callout = True
                callout_type = callout_match.group(1).upper()
                callout_title = callout_match.group(2).strip()
            elif in_callout:
                if line.startswith(">"):
                    callout_content.append(line[1:].strip())
                else:
                    c_body = "<br>".join(callout_content)
                    out_lines.append(f'<div class="callout callout-{callout_type.lower()}"><div class="callout-header"><span class="callout-icon">💡</span> <strong>{html.escape(callout_title or callout_type)}</strong></div><div class="callout-body">{c_body}</div></div>')
                    in_callout = False
                    callout_content = []
                    out_lines.append(line)
            else:
                out_lines.append(line)

        if in_callout:
            c_body = "<br>".join(callout_content)
            out_lines.append(f'<div class="callout callout-{callout_type.lower()}"><div class="callout-header"><span class="callout-icon">💡</span> <strong>{html.escape(callout_title or callout_type)}</strong></div><div class="callout-body">{c_body}</div></div>')

        return "\n".join(out_lines)

    html_text = parse_callouts(html_text)

    def format_inline_markdown(text):
        # Match standard markdown links [text](url)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener" class="ext-link">\1</a>', text)
        # Match raw http/https URLs not already in href/tags
        text = re.sub(r'(?<!href=")(?<!src=")(?<!">)(https?://[^\s<>"\'\)]+)', r'<a href="\1" target="_blank" rel="noopener" class="ext-link">\1</a>', text)
        # Match bold **text**
        text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
        # Match italic *text*
        text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
        return text

    # Basic Markdown Converter for Headers, Code blocks, Lists, Tables
    lines = html_text.split("\n")
    processed_lines = []
    in_code_block = False
    code_lang = ""
    code_buf = []

    in_table = False
    table_buf = []

    for line in lines:
        if line.startswith("```"):
            if in_code_block:
                code_str = html.escape("\n".join(code_buf))
                processed_lines.append(f'<pre><code class="language-{code_lang}">{code_str}</code></pre>')
                in_code_block = False
                code_buf = []
            else:
                in_code_block = True
                code_lang = line[3:].strip()
            continue

        if in_code_block:
            code_buf.append(line)
            continue

        # Table detection
        if "|" in line and (line.strip().startswith("|") or line.strip().endswith("|")):
            in_table = True
            table_buf.append(line)
            continue
        elif in_table:
            # Process table
            in_table = False
            processed_lines.append(render_table(table_buf, format_inline_markdown))
            table_buf = []

        # Headers
        if line.startswith("# "):
            processed_lines.append(f'<h1>{format_inline_markdown(line[2:])}</h1>')
        elif line.startswith("## "):
            processed_lines.append(f'<h2>{format_inline_markdown(line[3:])}</h2>')
        elif line.startswith("### "):
            processed_lines.append(f'<h3>{format_inline_markdown(line[4:])}</h3>')
        elif line.startswith("#### "):
            processed_lines.append(f'<h4>{format_inline_markdown(line[5:])}</h4>')
        elif line.startswith("- ") or line.startswith("* "):
            # Unordered list item
            item_text = line[2:].strip()
            processed_lines.append(f'<ul><li>{format_inline_markdown(item_text)}</li></ul>')
        elif re.match(r"^\d+\.\s+", line):
            item_text = re.sub(r"^\d+\.\s+", "", line).strip()
            processed_lines.append(f'<ol><li>{format_inline_markdown(item_text)}</li></ol>')
        elif line.strip() == "":
            processed_lines.append("<br>")
        else:
            p_text = format_inline_markdown(line)
            processed_lines.append(f'<p>{p_text}</p>')

    if in_table and table_buf:
        processed_lines.append(render_table(table_buf, format_inline_markdown))

    final_html = "\n".join(processed_lines)
    # Merge consecutive <ul>/<ol> tags
    final_html = re.sub(r"</ul>\s*<ul>", "", final_html)
    final_html = re.sub(r"</ol>\s*<ol>", "", final_html)

    # Restore Math blocks
    for i, m_block in enumerate(math_blocks):
        # Escape HTML inside math block safely
        safe_m = html.escape(m_block)
        final_html = final_html.replace(f"___MATH_BLOCK_{i}___", safe_m)

    return final_html

def render_table(lines, format_fn=None):
    if len(lines) < 2:
        return ""
    headers = [c.strip() for c in lines[0].split("|") if c.strip() != ""]
    # Check delimiter line
    start_idx = 2 if len(lines) > 1 and "---" in lines[1] else 1

    rows = []
    for line in lines[start_idx:]:
        cells = [c.strip() for c in line.split("|") if c.strip() != ""]
        if cells:
            rows.append(cells)

    def fmt(val):
        if format_fn:
            return format_fn(val)
        return html.escape(val)

    th_html = "".join([f"<th>{fmt(h)}</th>" for h in headers])
    tr_html = ""
    for r in rows:
        td_html = "".join([f"<td>{fmt(c)}</td>" for c in r])
        tr_html += f"<tr>{td_html}</tr>"

    return f'<div class="table-wrapper"><table class="data-table"><thead><tr>{th_html}</tr></thead><tbody>{tr_html}</tbody></table></div>'

def generate_css():
    css_path = PROJECT_DIR / "assets_src" / "style.css"
    if not css_path.exists():
        raise FileNotFoundError(f"Missing stylesheet source: {css_path}")
    css_content = css_path.read_text(encoding="utf-8")

    # Append table trend chart styles (theme-agnostic, uses existing tokens)
    chart_css_path = PROJECT_DIR / "assets_src" / "chart.css"
    if chart_css_path.exists():
        css_content += "\n\n" + chart_css_path.read_text(encoding="utf-8")

    (SITE_DIR / "assets" / "style.css").write_text(css_content, encoding="utf-8")


def copy_charts_js():
    src = PROJECT_DIR / "assets_src" / "charts.js"
    dst = SITE_DIR / "assets" / "charts.js"
    if src.exists():
        shutil.copy2(src, dst)

def generate_js():
    js_path = PROJECT_DIR / "assets_src" / "app.js"
    if not js_path.exists():
        raise FileNotFoundError(f"Missing script source: {js_path}")
    js_content = js_path.read_text(encoding="utf-8")
    (SITE_DIR / "assets" / "app.js").write_text(js_content, encoding="utf-8")

def generate_header(current_rel_url, root_prefix):
    return f"""
<header class="app-header">
  <div class="header-left">
    <button class="menu-toggle-btn" id="menu-toggle" aria-label="Toggle Sidebar Menu">☰</button>
    <a href="{root_prefix}index.html" class="logo-text">
      <span class="logo-mark" aria-hidden="true"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.0001 2.00004L4.09189 13.4099C3.73854 13.8632 4.06293 14.5275 4.63742 14.5275H10.2712L9.04558 21.1558C8.92488 21.8149 9.75925 22.1911 10.1738 21.6664L19.9083 9.34965C20.2616 8.89636 19.9373 8.23203 19.3628 8.23203H13.729L14.9546 1.60372C15.0753 0.944626 14.2409 0.568394 13.8264 1.09312L13.0001 2.00004Z"/></svg></span>
      <span class="logo-word">EV&nbsp;<span class="gradient-text">Research Hub</span></span>
    </a>
  </div>
  
  <div class="header-search">
    <span class="search-icon">🔍</span>
    <input type="text" id="global-search-input" data-root-prefix="{root_prefix}" placeholder="Search papers, models, datasets..." aria-label="Global Search">
    <kbd class="search-kbd">⌘K</kbd>
    <div id="search-results" style="display:none; position:absolute; top:calc(100% + 6px); left:0; right:0; background:var(--surface-solid); border:1px solid var(--border); border-radius:0.75rem; z-index:100; box-shadow:var(--shadow-lg);"></div>
  </div>

  <div class="header-right">
    <button class="theme-toggle-btn" id="theme-toggle" aria-label="Toggle Theme">
      <span class="theme-icon">☀️</span>
      <span class="theme-text">Light</span>
    </button>
  </div>
</header>
"""

def generate_sidebar(all_pages, current_rel_url, root_prefix):
    # Group pages by category
    cats = {c: [] for c in CATEGORIES.keys()}
    for page in all_pages:
        c = page["cat"]
        if c in cats:
            cats[c].append(page)

    tree_nodes_html = ""
    for c_id, c_name in CATEGORIES.items():
        pages = cats[c_id]
        if not pages:
            continue
        pages_sorted = sorted(pages, key=lambda x: x["title"])
        items_html = ""
        for p in pages_sorted:
            active_class = "class='active'" if p["rel_url"] == current_rel_url else ""
            link_dest = root_prefix + p["rel_url"]
            items_html += f"<li><a href='{html.escape(link_dest)}' {active_class} title='{html.escape(p['title'])}'>{html.escape(p['title'])}</a></li>"

        is_current_cat = any(item["rel_url"] == current_rel_url for item in pages)
        is_index_default = (current_rel_url == "index.html" and c_id == "papers")
        open_attr = "open" if (is_current_cat or is_index_default) else ""
        icon = CATEGORY_ICONS.get(c_id, "📁")
        tree_nodes_html += f"""
<details class="tree-node" id="tree-node-{c_id}" {open_attr}>
  <summary>
    <span class="summary-title"><span class="chevron-icon">▸</span> <span>{icon} {c_name}</span></span>
    <span class="badge-count">{len(pages)}</span>
  </summary>
  <ul class="tree-list">
    {items_html}
  </ul>
</details>
"""

    return f"""
<aside class="app-sidebar" id="sidebar">
  <div class="sidebar-controls">
    <button class="btn-sm" id="expand-all-btn">Expand All</button>
    <button class="btn-sm" id="collapse-all-btn">Collapse All</button>
  </div>
  <nav class="sidebar-nav">
    {tree_nodes_html}
  </nav>
</aside>
"""

FOOTER_LOGO_SVG = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13.0001 2.00004L4.09189 13.4099C3.73854 13.8632 4.06293 14.5275 4.63742 14.5275H10.2712L9.04558 21.1558C8.92488 21.8149 9.75925 22.1911 10.1738 21.6664L19.9083 9.34965C20.2616 8.89636 19.9373 8.23203 19.3628 8.23203H13.729L14.9546 1.60372C15.0753 0.944626 14.2409 0.568394 13.8264 1.09312L13.0001 2.00004Z"/></svg>'

def generate_footer(root_prefix):
    return f"""
<footer class="app-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <a href="{root_prefix}index.html" class="logo-text">
        <span class="logo-mark" aria-hidden="true">{FOOTER_LOGO_SVG}</span>
        <span class="logo-word">EV&nbsp;<span class="gradient-text">Research Hub</span></span>
      </a>
      <p>An open research knowledge base covering EV charging demand, probabilistic forecasting, deep learning architectures, real-world charging datasets, and benchmark metrics.</p>
    </div>
    <div class="footer-cols">
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="{root_prefix}index.html">Dashboard</a></li>
          <li><a href="{root_prefix}guides/index.html">Master Index</a></li>
          <li><a href="{root_prefix}guides/schema.html">Metadata Schema</a></li>
          <li><a href="{root_prefix}references/_all_references.html">Reference Index</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Research</h4>
        <ul>
          <li><a href="{root_prefix}guides/research_gaps.html">Research Gaps</a></li>
          <li><a href="{root_prefix}guides/proposed_architectures.html">Proposed Architectures</a></li>
          <li><a href="{root_prefix}guides/progress_summary_and_research_gaps.html">Progress Summary</a></li>
          <li><a href="{root_prefix}guides/log.html">Activity Log</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Code &amp; Data</h4>
        <ul>
          <li><a href="{root_prefix}github/EV_Load_Forecasting_Repos.html">EV Forecasting Repos</a></li>
          <li><a href="{root_prefix}github/Probabilistic_Time_Series_Repos.html">Probabilistic TS Repos</a></li>
          <li><a href="{root_prefix}github/Time_Series_Foundation_Models_Repos.html">Foundation Models</a></li>
          <li><a href="{root_prefix}references/github_repositories_index.html">GitHub Master Index</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-bottom-inner">
      <span>&copy; 2026 EV Research Hub. Built for research clarity.</span>
      <span>Data &middot; Models &middot; Benchmarks</span>
    </div>
  </div>
</footer>
<button class="back-to-top" id="back-to-top" aria-label="Back to top">&uarr;</button>
"""

def generate_page_html(page, all_pages, lookup, all_pages_map):
    current_rel_url = page["rel_url"]
    depth = len(current_rel_url.split("/")) - 1
    root_prefix = "../" * depth if depth > 0 else "./"

    header_html = generate_header(current_rel_url, root_prefix)
    sidebar_html = generate_sidebar(all_pages, current_rel_url, root_prefix)
    footer_html = generate_footer(root_prefix)

    # Render main markdown content
    body_html = convert_markdown_to_html(page["body"], current_rel_url, lookup, all_pages_map)

    # Render metadata chips
    meta = page["meta"]
    meta_chips = []
    if page.get("year"):
        meta_chips.append(f'<span class="chip">📅 Year: <strong>{page["year"]}</strong></span>')
    if page.get("authors"):
        authors_str = ", ".join(page["authors"]) if isinstance(page["authors"], list) else str(page["authors"])
        meta_chips.append(f'<span class="chip">👤 Authors: <strong>{html.escape(authors_str)}</strong></span>')
    if page.get("journal"):
        meta_chips.append(f'<span class="chip">🏛️ Venue: <strong>{html.escape(page["journal"])}</strong></span>')
    if page.get("doi"):
        doi_val = str(page["doi"])
        doi_url = doi_val if doi_val.startswith("http") else (f"https://{doi_val}" if doi_val.startswith("doi.org") else f"https://doi.org/{doi_val}")
        meta_chips.append(f'<span class="chip">🔗 DOI: <a href="{html.escape(doi_url)}" target="_blank" rel="noopener" class="ext-link"><strong>{html.escape(doi_val)}</strong></a></span>')
    if meta.get("code_url"):
        meta_chips.append(f'<span class="chip">💻 Code: <a href="{html.escape(meta["code_url"])}" target="_blank" rel="noopener" class="ext-link"><strong>{html.escape(meta["code_url"])}</strong></a></span>')
    if meta.get("dataset_url"):
        meta_chips.append(f'<span class="chip">📊 Dataset: <a href="{html.escape(meta["dataset_url"])}" target="_blank" rel="noopener" class="ext-link"><strong>{html.escape(meta["dataset_url"])}</strong></a></span>')

    chips_html = f'<div class="meta-badges">{"".join(meta_chips)}</div>' if meta_chips else ""

    # Back links / Related pages
    related_cards = []
    stem_lower = page["stem"].lower()
    for other in all_pages:
        if other["stem"] == page["stem"]:
            continue
        if stem_lower in other["body"].lower() or page["title"].lower() in other["body"].lower():
            link_dest = root_prefix + other["rel_url"]
            related_cards.append(f"""
<a href="{link_dest}" class="card">
  <div class="card-title">{html.escape(other["title"])}</div>
  <div class="card-desc">Category: {html.escape(other["cat_name"])}</div>
</a>
""")
            if len(related_cards) >= 6:
                break

    related_section = ""
    if related_cards:
        related_section = f"""
<div class="related-box" data-reveal>
  <h3>🔗 Cross-Referenced Literature &amp; Models</h3>
  <div class="grid-cards">
    {"".join(related_cards)}
  </div>
</div>
"""

    out_filepath = SITE_DIR / page["rel_url"]
    out_filepath.parent.mkdir(parents=True, exist_ok=True)

    cat_icon = CATEGORY_ICONS.get(page["cat"], "📄")

    full_page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(page["title"])} | EV Research Knowledge Base</title>
  <meta name="description" content="Research knowledge base entry for {html.escape(page["title"])}">
  <script>
    (function() {{
      document.documentElement.classList.add('js');
      const saved = localStorage.getItem('kb-theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = saved || (prefersDark ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    }})();
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root_prefix}assets/style.css">
  <!-- KaTeX for math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{ delimiters: [ {{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}, {{left: '\\\\(', right: '\\\\)', display: false}}, {{left: '\\\\[', right: '\\\\]', display: true}} ], throwOnError: false }});"></script>
</head>
<body>
  {header_html}
  <script>
    (function() {{
      var t = document.documentElement.getAttribute('data-theme');
      var i = document.querySelector('.theme-icon');
      var x = document.querySelector('.theme-text');
      if (i) i.textContent = t === 'dark' ? '\U0001F319' : '\u2600\uFE0F';
      if (x) x.textContent = t === 'dark' ? 'Dark' : 'Light';
    }})();
  </script>
  <div class="app-container">
    {sidebar_html}
    <main class="app-content">
      <div class="content-inner">
        <div class="page-breadcrumb">
          <a href="{root_prefix}index.html">Home</a>
          <span>/</span>
          <span>{cat_icon} {html.escape(page["cat_name"])}</span>
        </div>
        <h1 class="page-title">{html.escape(page["title"])}</h1>
        {chips_html}
        <article class="markdown-body">
          {body_html}
        </article>
        {related_section}
      </div>
    </main>
  </div>
  {footer_html}
  <script src="{root_prefix}assets/search-index.js"></script>
  <script src="{root_prefix}assets/charts.js"></script>
  <script src="{root_prefix}assets/app.js"></script>
</body>
</html>
"""
    out_filepath.write_text(full_page_html, encoding="utf-8")

def generate_dashboard_index(all_pages, lookup, all_pages_map):
    current_rel_url = "index.html"
    root_prefix = "./"

    header_html = generate_header(current_rel_url, root_prefix)
    sidebar_html = generate_sidebar(all_pages, current_rel_url, root_prefix)
    footer_html = generate_footer(root_prefix)

    # Count stats
    cat_counts = {c: 0 for c in CATEGORIES.keys()}
    for p in all_pages:
        if p["cat"] in cat_counts:
            cat_counts[p["cat"]] += 1

    # Timeline calculation for papers by publication era
    eras = {
        "Pre-2018": 0,
        "2018-2020": 0,
        "2021": 0,
        "2022": 0,
        "2023": 0,
        "2024": 0,
        "2025": 0,
        "2026": 0
    }
    for p in all_pages:
        if p["cat"] == "papers" and p.get("year"):
            try:
                y = int(p["year"])
                if y < 2018:
                    eras["Pre-2018"] += 1
                elif 2018 <= y <= 2020:
                    eras["2018-2020"] += 1
                elif str(y) in eras:
                    eras[str(y)] += 1
            except Exception:
                pass

    max_era_count = max(eras.values()) if eras.values() else 1

    timeline_bars_html = ""
    for era_label, count in eras.items():
        pct = max(12, int((count / max_era_count) * 100))
        timeline_bars_html += f"""
<div class="bar-group">
  <div class="bar-count">{count}</div>
  <div class="bar-fill" style="height: {pct}%;"></div>
  <div class="bar-label">{era_label}</div>
</div>
"""

    # Featured 2025-2026 papers
    recent_papers = [p for p in all_pages if p["cat"] == "papers" and p.get("year") in [2025, 2026, "2025", "2026"]][:6]
    recent_cards = ""
    for i, p in enumerate(recent_papers):
        delay = (i % 3) * 70
        recent_cards += f"""
<a href="{root_prefix + p['rel_url']}" class="card" data-reveal style="--reveal-delay: {delay}ms;">
  <div class="card-title">📄 {html.escape(p['title'])}</div>
  <div class="card-desc">📅 {p.get('year', '')} • {html.escape(p.get('journal', 'Literature'))}</div>
</a>
"""

    # Featured guides
    guides = [p for p in all_pages if p["cat"] == "guides"]
    guides_cards = ""
    for i, g in enumerate(guides):
        delay = (i % 3) * 70
        guides_cards += f"""
<a href="{root_prefix + g['rel_url']}" class="card" data-reveal style="--reveal-delay: {delay}ms;">
  <div class="card-title">💡 {html.escape(g['title'])}</div>
  <div class="card-desc">Comprehensive synthesis file analyzing EV research gaps and novelty ideas.</div>
</a>
"""

    dashboard_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EV Charging & Load Forecasting Knowledge Base Dashboard</title>
  <meta name="description" content="Interactive research knowledge base for Electric Vehicle charging demand, probabilistic forecasting, deep learning models, datasets, and benchmark metrics.">
  <script>
    (function() {{
      document.documentElement.classList.add('js');
      const saved = localStorage.getItem('kb-theme');
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = saved || (prefersDark ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    }})();
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
  <!-- KaTeX for math rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{ delimiters: [ {{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}, {{left: '\\\\(', right: '\\\\)', display: false}}, {{left: '\\\\[', right: '\\\\]', display: true}} ], throwOnError: false }});"></script>
</head>
<body>
  {header_html}
  <script>
    (function() {{
      var t = document.documentElement.getAttribute('data-theme');
      var i = document.querySelector('.theme-icon');
      var x = document.querySelector('.theme-text');
      if (i) i.textContent = t === 'dark' ? '\U0001F319' : '\u2600\uFE0F';
      if (x) x.textContent = t === 'dark' ? 'Dark' : 'Light';
    }})();
  </script>
  <div class="app-container">
    {sidebar_html}
    <main class="app-content">
      <div class="content-inner">
        
        <!-- Hero Banner -->
        <section class="hero-section" data-reveal>
          <div class="hero-bg" aria-hidden="true">
            <div class="orb orb-a"></div>
            <div class="orb orb-b"></div>
            <div class="orb orb-c"></div>
          </div>
          <div class="hero-grid-overlay" aria-hidden="true"></div>
          <div class="hero-inner">
            <span class="hero-eyebrow"><span class="pulse-dot"></span> Knowledge Base &middot; 2026 Edition</span>
            <h1 class="hero-title">EV Charging &amp; Load Forecasting<br><span class="gradient-text">Research Knowledge Hub</span></h1>
            <p class="hero-subtitle">
              A structured, cross-referenced repository covering {cat_counts.get('papers', 0)} annotated papers, deep learning &amp; diffusion models, real-world charging datasets, feature engineering taxonomies, and forecasting metrics.
            </p>
            <div class="hero-actions">
              <a href="#latest-research" class="btn btn-primary">Explore Research <span class="btn-arrow">&rarr;</span></a>
              <a href="./guides/index.html" class="btn btn-secondary">Research Syntheses</a>
            </div>
            <div class="hero-meta">
              <span class="meta-pill"><strong>{cat_counts.get('papers', 0)}</strong> Papers</span>
              <span class="meta-pill"><strong>{cat_counts.get('models', 0)}</strong> Models</span>
              <span class="meta-pill"><strong>{cat_counts.get('datasets', 0)}</strong> Datasets</span>
              <span class="meta-pill">Updated <strong>2026</strong></span>
            </div>
          </div>
        </section>

        <!-- Stats Grid -->
        <div class="dashboard-stats-grid">
          <div class="stat-card" data-reveal style="--reveal-delay: 0ms;">
            <div class="stat-card-accent" style="background:#6366f1;"></div>
            <div class="stat-number" style="color:#6366f1;" data-count="{cat_counts.get('papers', 0)}">0</div>
            <div class="stat-label">📄 Papers & Literature</div>
            <div class="stat-desc">Annotated summaries, mathematical formulations & benchmarks.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 60ms;">
            <div class="stat-card-accent" style="background:#10b981;"></div>
            <div class="stat-number" style="color:#10b981;" data-count="{cat_counts.get('models', 0)}">0</div>
            <div class="stat-label">🧠 Models & Architectures</div>
            <div class="stat-desc">Transformers, DiffPLF, Mamba, PINNs, GCNs, and Ensembles.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 120ms;">
            <div class="stat-card-accent" style="background:#f59e0b;"></div>
            <div class="stat-number" style="color:#f59e0b;" data-count="{cat_counts.get('datasets', 0)}">0</div>
            <div class="stat-label">📊 Datasets & Benchmarks</div>
            <div class="stat-desc">Palo Alto, Caltech ACN, ElaadNL, Dundee, Boulder & Pecan Street.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 180ms;">
            <div class="stat-card-accent" style="background:#ec4899;"></div>
            <div class="stat-number" style="color:#ec4899;" data-count="{cat_counts.get('hyperparameters', 0)}">0</div>
            <div class="stat-label">🎛️ Hyperparameters</div>
            <div class="stat-desc">Bayesian optimization, Optuna TPE, Grid search, and tuning heuristics.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 240ms;">
            <div class="stat-card-accent" style="background:#3b82f6;"></div>
            <div class="stat-number" style="color:#3b82f6;" data-count="{cat_counts.get('features', 0)}">0</div>
            <div class="stat-label">⚙️ Features & Inputs</div>
            <div class="stat-desc">Arrival/Departure times, weather, SoC, session durations & grid data.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 300ms;">
            <div class="stat-card-accent" style="background:#14b8a6;"></div>
            <div class="stat-number" style="color:#14b8a6;" data-count="{cat_counts.get('metrics', 0)}">0</div>
            <div class="stat-label">📐 Evaluation Metrics</div>
            <div class="stat-desc">MAE, RMSE, MAPE, CRPS, Pinball Loss, Picp, and Winkler Score.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 360ms;">
            <div class="stat-card-accent" style="background:#06b6d4;"></div>
            <div class="stat-number" style="color:#06b6d4;" data-count="{cat_counts.get('github', 0)}">0</div>
            <div class="stat-label">💻 Open Source Code</div>
            <div class="stat-desc">Curated GitHub repositories for EV forecasting, DiffPLF, and foundation models.</div>
          </div>
          <div class="stat-card" data-reveal style="--reveal-delay: 420ms;">
            <div class="stat-card-accent" style="background:#8b5cf6;"></div>
            <div class="stat-number" style="color:#8b5cf6;" data-count="{cat_counts.get('guides', 0)}">0</div>
            <div class="stat-label">💡 Research Syntheses</div>
            <div class="stat-desc">Identified research gaps, proposed novel architectures & gap reports.</div>
          </div>
        </div>

        <!-- Research Publication Timeline -->
        <section class="timeline-section" data-reveal>
          <div class="panel-head">
            <h3>📈 Literature Distribution by Publication Era</h3>
            <span class="panel-head-total">Total: {cat_counts['papers']} Papers</span>
          </div>
          <div class="timeline-bars">
            {timeline_bars_html}
          </div>
        </section>

        <!-- Featured Recent Publications -->
        <section class="home-section" id="latest-research">
          <div class="section-head" data-reveal>
            <span class="section-kicker">New in 2025&ndash;2026</span>
            <h2 class="section-title">🔥 Latest Research Contributions</h2>
            <p class="section-sub">The most recent peer-reviewed additions to the hub.</p>
          </div>
          <div class="grid-cards">
            {recent_cards}
          </div>
        </section>

        <!-- Key Research Syntheses & Gaps -->
        <section class="home-section" id="syntheses">
          <div class="section-head" data-reveal>
            <span class="section-kicker">Deep Dives</span>
            <h2 class="section-title">📌 Key Research Syntheses &amp; Gap Reports</h2>
            <p class="section-sub">Curated analyses of open problems and proposed novel architectures.</p>
          </div>
          <div class="grid-cards">
            {guides_cards}
          </div>
        </section>

      </div>
    </main>
  </div>
  {footer_html}
  <script src="assets/search-index.js"></script>
  <script src="assets/charts.js"></script>
  <script src="assets/app.js"></script>
</body>
</html>
"""
    (SITE_DIR / "index.html").write_text(dashboard_html, encoding="utf-8")

def main():
    print("Building HTML Knowledge Base...")
    ensure_dirs()
    generate_css()
    generate_js()
    copy_charts_js()

    lookup, all_pages = build_lookup_index()
    all_pages_map = {p["stem"].lower(): p for p in all_pages}

    # Generate search index JSON
    search_data = []
    for p in all_pages:
        search_data.append({
            "title": p["title"],
            "year": p["year"],
            "cat_name": p["cat_name"],
            "rel_url": p["rel_url"],
            "body": p["body"][:300]
        })
    (SITE_DIR / "assets" / "search-index.json").write_text(json.dumps(search_data, indent=2), encoding="utf-8")
    # Embedded variant for file:// (offline) usage — fetch() fails on file:// in Chrome
    js_payload = "window.SEARCH_INDEX = " + json.dumps(search_data, ensure_ascii=False) + ";"
    (SITE_DIR / "assets" / "search-index.js").write_text(js_payload, encoding="utf-8")

    # Build individual HTML pages
    for p in all_pages:
        generate_page_html(p, all_pages, lookup, all_pages_map)

    # Build Dashboard Index
    generate_dashboard_index(all_pages, lookup, all_pages_map)

    print(f"Build complete! Generated {len(all_pages)} pages in {SITE_DIR}")

if __name__ == "__main__":
    main()



