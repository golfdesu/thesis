import os

base = r'C:\Users\chaya\Documents\Obsidian\Thesis'
src_pdf = r'C:\Users\chaya\Downloads\s41598-025-29739-z.pdf'

pdf_filename = '2025_Electric_Vehicles_Charging_Stations_Load_Forecasting_Based_on_Hybrid_XGBoost_BiLSTM_Model.pdf'
md_filename = '2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load.md'

dst_pdf_path = os.path.join(base, 'raw_sources', pdf_filename)
dst_md_path = os.path.join(base, 'wiki', 'papers', md_filename)

# 1. Copy PDF to raw_sources
with open(src_pdf, 'rb') as f_in, open(dst_pdf_path, 'wb') as f_out:
    f_out.write(f_in.read())

# 2. Write Markdown note
md_content = """---
type: paper
title: "Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model"
authors: ["Hany S. E. Mansour", "Amira S. Mohamed", "M. Abdel-Aziz"]
year: 2025
journal_conference: "Nature Scientific Reports"
doi_url: "https://doi.org/10.1038/s41598-025-29739-z"
models_used: ["[[XGBoost]]", "[[BiLSTM]]", "[[Ensemble_Stacking]]", "[[LightGBM]]", "[[CNN]]", "[[SARIMAX]]"]
datasets_used: ["[[Caltech_ACN]]"]
features_used: ["[[Historical_Load]]", "[[Arrival_Departure_Time]]", "[[Charging_Duration]]", "[[kWhRequested]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[R2_Score]]"]
tags:
  - paper
  - ev-load-forecasting
  - xgboost
  - bilstm
  - stacking-ensemble
  - nature-scientific-reports
---

# 📄 Summary: Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model

## 🎯 Main Objective & Core Contribution
- **Core problem addressed**: Volatile EV charging station demand strains grid infrastructure. Precise short-term, hourly, station-level load forecasting is critical for optimizing energy management and grid stability.
- **Primary novel contribution**: Proposes a **Hybrid XGBoost-BiLSTM Stacking Ensemble** (Hybrid 3) with an XGBoost meta-learner, benchmarked against 24 baseline models across statistical, machine learning, deep learning, and ensemble methods.

## 🧠 Methodology & Model Architecture
- **Model Type**: 
  1. **Base Learners**: Combined Bidirectional LSTM (BiLSTM) for temporal sequential features and Extreme Gradient Boosting (XGBoost) / LightGBM for non-linear tabular features.
  2. **Stacking Layer (Meta-Learner)**: Fuses base learner prediction outputs via an XGBoost Meta-Learner regressor.
- **Feature Engineering & Ablation**:
  - Identified **log-transformed charging duration** as the most influential predictor (importance score = 0.376).
  - Removing feature engineering degrades MAE by +13.7%.
  - Removing base learners degrades MAE by +18.8%.
  - Removing meta-learner degrades MAE by +29.2%.

## 📊 Dataset & Input Features
- **Dataset**: [[Caltech_ACN]] (Adaptive Charging Network at Caltech campus; 1,329 days, April 25, 2018 – September 13, 2021; 31,424 raw sessions preprocessed to 14,496 clean sessions across 55 charging stations).
- **Features**: [[Arrival_Departure_Time]], [[Charging_Duration]] (log), [[kWhRequested]], [[Historical_Load]].

## 📈 Performance & Results
- **Key numerical results**:
  - On ACN Caltech cleaned dataset: **MAE = 2.6870 kWh**, **R2 = 0.6395** (a 3.4% improvement over standalone BiLSTM).
  - Five-fold walk-forward validation: mean MAE = 2.5351 kWh, SD = 1.2885.
- **Baseline Comparisons**: Benchmarked against 24 models including Persistence, SARIMAX, Random Forest, LightGBM, CNN, LSTM, and BiLSTM.

## 💡 Limitations & Identified Research Gaps
- Cross-site evaluation on synthetic dataset (~1.96M sessions) showed sensitive transferability (MAE = 4.16 kWh, R2 = 0.01), showing that site-specific temporal patterns limit cross-facility zero-shot generalization.
"""

with open(dst_md_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Created MD note: {md_filename}")
print(f"Copied PDF: {pdf_filename}")

# 3. Update index.md
index_path = os.path.join(base, 'index.md')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

entry_stem = md_filename.replace('.md', '')
index_line = f"- [[{entry_stem}]] - Mansour et al. (2025): Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model (Nature Sci Rep).\n"

if entry_stem not in index_content:
    target_str = "## 📄 Paper Summaries (`wiki/papers/`)\n"
    index_content = index_content.replace(target_str, target_str + index_line)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Updated index.md")

# 4. Update log.md
log_path = os.path.join(base, 'log.md')
with open(log_path, 'a', encoding='utf-8') as f:
    f.write(f"\n## [2026-08-07] ingest | {entry_stem}\n")
    f.write(f"- Ingested PDF paper: Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model.\n")
    f.write(f"- Added structured note `wiki/papers/{md_filename}` and copied PDF to `raw_sources/{pdf_filename}`.\n")
    print("Updated log.md")
