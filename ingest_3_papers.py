import os
import fitz

base = r'C:\Users\chaya\Documents\Obsidian\Thesis'

# Define paper metadata
papers_meta = [
    {
        'pdf_name': '2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load.pdf',
        'src_pdf': r'C:\Users\chaya\Downloads\Decomposition_and_Stacked_Meta-Learning_for_Short-Term_Electric_Vehicle_Load_Forecasting.pdf',
        'md_name': '2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load.md',
        'title': 'Decomposition and Stacked Meta-Learning for Short-Term Electric Vehicle Load Forecasting',
        'authors': ['Syed Sajid Ullah', 'Gang Li', 'Muhammad Zunair Zamir', 'Abdul Malik', 'Saeed Mian Qaisar', 'Mudassar Riaz'],
        'year': 2026,
        'journal': 'IEEE Transactions on Smart Grid',
        'doi': '10.1109/TSG.2026.xxxxxx',
        'models': ['[[STL_Decomposition]]', '[[Gradient_Boosting]]', '[[Ensemble_Stacking]]', '[[LSTM]]'],
        'datasets': ['[[Caltech_ACN]]', '[[ElaadNL]]', '[[Boulder_Colorado]]'],
        'features': ['[[Historical_Load]]', '[[Seasonal_Components]]', '[[Residual_Components]]'],
        'horizon': '[[Short_Term_Forecasting]]',
        'metrics': ['[[MAE]]', '[[RMSE]]', '[[MAPE]]'],
        'tags': ['paper', 'ev-load-forecasting', 'stl-decomposition', 'meta-learning', 'ensemble'],
        'summary': """- **Core problem addressed**: Traditional forecasting models struggle to jointly capture multi-scale temporal structures, non-linear interactions, and cross-dataset heterogeneity in EV charging demand.
- **Primary novel contribution**: Proposes a decomposition-driven hybrid forecasting framework combining Seasonal-Trend decomposition using Loess (STL) with component-specific base learners and a Gradient Boosting Regressor meta-learner for stacked ensemble fusion.""",
        'methodology': """- **Model Architecture**: 
  1. **STL Signal Decomposition**: Decomposes raw EV load signal $Y_t$ into Trend ($T_t$), Seasonal ($S_t$), and Residual ($R_t$) components:
     $$Y_t = T_t + S_t + R_t$$
  2. **Component-Specific Base Learners**: Fits specialized learning algorithms aligned with the statistical variance of each component.
  3. **Stacked Ensemble Meta-Fusion**: Combines component-level forecasts using a Gradient Boosting Regressor (GBR) meta-learner:
     $$\hat{Y}_t = f_{\text{GBR}}(\hat{T}_t, \hat{S}_t, \hat{R}_t)$$""",
        'results': """- **Key numerical results**: Outperforms single deep learning models (LSTM, GRU, XGBoost) across four real-world datasets with significant reductions in MAE and RMSE.
- **Baseline comparisons**: Achieves consistent superiority in multi-scale short-term horizons (1h to 24h)."""
    },
    {
        'pdf_name': '2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load.pdf',
        'src_pdf': r'C:\Users\chaya\Downloads\Load_Forecasting_of_Electric_Vehicle_Charging_Stations_Attention_Based_Spatiotemporal_MultiGraph_Convolutional_Networks.pdf',
        'md_name': '2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load.md',
        'title': 'Load Forecasting of Electric Vehicle Charging Stations: Attention Based Spatiotemporal MultiGraph Convolutional Networks',
        'authors': ['Jinkai Shi', 'Weige Zhang', 'Yan Bao', 'David Wenzhong Gao', 'Zhihao Wang'],
        'year': 2024,
        'journal': 'IEEE Transactions on Smart Grid, Vol. 15, No. 3, pp. 3016-3029',
        'doi': '10.1109/TSG.2023.3328543',
        'models': ['[[STMGCN|Spatiotemporal Multi-Graph Convolutional Network]]', '[[GCN]]', '[[Attention]]', '[[Dilated_Causal_CNN]]'],
        'datasets': ['[[EV_Charging_Station_Network_Dataset]]'],
        'features': ['[[Historical_Load]]', '[[Spatial_Topology]]', '[[Weather_Traffic]]'],
        'horizon': '[[Spatial_Temporal_Forecasting]]',
        'metrics': ['[[MAE]]', '[[RMSE]]', '[[MAPE]]'],
        'tags': ['paper', 'ev-load-forecasting', 'spatiotemporal', 'multi-graph', 'gcn', 'attention'],
        'summary': """- **Core problem addressed**: Charging stations couple power systems with transportation systems; their loads are influenced simultaneously by driver behavior, traffic conditions, and spatial interactions among neighboring stations.
- **Primary novel contribution**: Introduces Spatiotemporal Multi-Graph Convolutional Networks (STMGCN) utilizing multi-graph representations (physical distance, functional similarity, traffic flow) with gated dilated causal convolutions and attention mechanisms.""",
        'methodology': """- **Model Architecture**:
  1. **Multi-Graph Spatial Feature Extraction**: Constructs multiple adjacency matrices $\mathbf{A}_1, \mathbf{A}_2, \mathbf{A}_3$ representing spatial distance, charging demand correlation, and traffic connectivity.
  2. **Gated Dilated Causal Convolution**: Captures long-range temporal dependencies efficiently.
  3. **Spatial & Temporal Attention Modules**: Dynamically re-weights spatial node neighbors and temporal lookback steps:
     $$\mathbf{S}_{\text{attn}} = \text{Softmax}\left(\frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}}\right) \mathbf{V}$$""",
        'results': """- **Key numerical results**: Superior spatial-temporal load prediction accuracy across charging station networks compared to ST-GCN, GCN-LSTM, and ARIMA baselines.
- **Robustness**: Maintains high forecasting stability across severe weather events and traffic surges."""
    },
    {
        'pdf_name': '2025_Wu_Meta_Learning_Physics_Informed_GACN_Power_System.pdf',
        'src_pdf': r'C:\Users\chaya\Downloads\Meta-Learning_Enhanced_Physics-Informed_Graph_Attention_Convolutional_Network_for_Distribution_Power_System_State_Estimation.pdf',
        'md_name': '2025_Wu_Meta_Learning_Physics_Informed_GACN_Power_System.md',
        'title': 'Meta-Learning Enhanced Physics-Informed Graph Attention Convolutional Network for Distribution Power System State Estimation',
        'authors': ['Huayi Wu', 'Zhao Xu', 'Minghao Wang', 'Xue Lyu'],
        'year': 2025,
        'journal': 'IEEE Transactions on Network Science and Engineering, Vol. 12, No. 2, pp. 1186-1198',
        'doi': '10.1109/TNSE.2024.3498123',
        'models': ['[[Meta_PIGACN|Meta Physics-Informed Graph Attention Network]]', '[[GCN]]', '[[Graph_Attention]]', '[[Meta_Learning]]'],
        'datasets': ['[[IEEE_Distribution_Test_Feeders]]'],
        'features': ['[[Node_Voltage]]', '[[Power_Injection]]', '[[Grid_Topology]]'],
        'horizon': '[[Real_Time_State_Estimation]]',
        'metrics': ['[[MAE]]', '[[RMSE]]'],
        'tags': ['paper', 'physics-informed', 'meta-learning', 'graph-attention', 'power-system'],
        'summary': """- **Core problem addressed**: Distribution power system state estimation (DSSE) faces severe challenges from frequent grid topology variations and volatile renewable/EV power injections.
- **Primary novel contribution**: Proposes Meta-PIGACN, integrating physical grid constraints into graph attention convolutions combined with MAML meta-learning to rapidly adapt to dynamic topology changes.""",
        'methodology': """- **Model Architecture**:
  1. **Physics-Informed Edge Weighting**: Embeds admittance matrix $Y_{\text{bus}}$ and physical Ohm/Kirchhoff laws directly into GCN graph aggregation.
  2. **Graph Attention Mechanism**: Dynamically learns node influence across varying grid topographies.
  3. **MAML Meta-Learning Outer Loop**: Pre-trains network parameters across multiple grid topology tasks for rapid few-shot adaptation to line outages or switching events.""",
        'results': """- **Key numerical results**: Outperforms conventional Extended Kalman Filter (EKF) and standard GCN by reducing voltage state estimation error under dynamic topology switching."""
    }
]

# Write MD files for each paper
for p in papers_meta:
    # 1. Copy PDF to raw_sources
    raw_pdf_path = os.path.join(base, 'raw_sources', p['pdf_name'])
    with open(p['src_pdf'], 'rb') as f_in, open(raw_pdf_path, 'wb') as f_out:
        f_out.write(f_in.read())
    
    # 2. Write Markdown note in wiki/papers/
    md_path = os.path.join(base, 'wiki', 'papers', p['md_name'])
    models_str = str(p['models']).replace("'", '"')
    datasets_str = str(p['datasets']).replace("'", '"')
    features_str = str(p['features']).replace("'", '"')
    metrics_str = str(p['metrics']).replace("'", '"')
    authors_str = str(p['authors']).replace("'", '"')
    
    content = f"""---
type: paper
title: "{p['title']}"
authors: {authors_str}
year: {p['year']}
journal_conference: "{p['journal']}"
doi_url: "{p['doi']}"
models_used: {models_str}
datasets_used: {datasets_str}
features_used: {features_str}
forecasting_horizon: "{p['horizon']}"
metrics: {metrics_str}
tags:
"""
    for t in p['tags']:
        content += f"  - {t}\n"
    content += f"""---

# 📄 Summary: {p['title']}

## 🎯 Main Objective & Core Contribution
{p['summary']}

## 🧠 Methodology & Model Architecture
{p['methodology']}

## 📊 Dataset & Input Features
- **Datasets**: {', '.join(p['datasets'])}
- **Features**: {', '.join(p['features'])}

## 📈 Performance & Results
{p['results']}
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created wiki paper note: {p['md_name']}")

# 3. Update index.md
index_path = os.path.join(base, 'index.md')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

new_index_entries = ""
for p in papers_meta:
    note_stem = p['md_name'].replace('.md', '')
    first_author = p['authors'][0].split()[-1]
    entry = f"- [[{note_stem}]] - {first_author} et al. ({p['year']}): {p['title']}.\n"
    if note_stem not in index_content:
        new_index_entries += entry

if new_index_entries:
    # Append to Section 📄 Paper Summaries
    target_str = "## 📄 Paper Summaries (`wiki/papers/`)\n"
    if target_str in index_content:
        index_content = index_content.replace(target_str, target_str + new_index_entries)
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print("Updated index.md with new papers.")

# 4. Update log.md
log_path = os.path.join(base, 'log.md')
with open(log_path, 'a', encoding='utf-8') as f:
    f.write("\n")
    for p in papers_meta:
        note_stem = p['md_name'].replace('.md', '')
        f.write(f"## [2026-08-07] ingest | {note_stem}\n")
        f.write(f"- Ingested PDF paper: {p['title']}.\n")
        f.write(f"- Added structured note `wiki/papers/{p['md_name']}` and copied PDF to `raw_sources/{p['pdf_name']}`.\n\n")

print("Ingestion workflow complete!")
