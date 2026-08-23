# 🔬 Master Synthesis: Literature Taxonomy & Research Gaps for Thesis

This document synthesizes the core findings, mathematical methods, and open research gaps identified across all **70 PDF research papers** ingested into your Obsidian Second Brain.

> [!NOTE]
> Last updated: 2026-08-09 | Covers all 70 papers | **Transformer-focused deep analysis added**

---

## 🏛️ Comprehensive Literature Taxonomy

```mermaid
graph TD
    A[EV Load & Energy Demand Forecasting] --> B[1. Single-Station & Local Forecasting]
    A --> C[2. City-Level & Multi-Station Spatial-Temporal]
    A --> D[3. Probabilistic & Uncertainty Quantification]
    A --> E[4. Data Scarcity, Transfer & Federated Learning]
    A --> F[5. Downstream V2G Control & Market Participation]
    A --> G[6. Next-Generation Architectures]
    A --> H[7. Signal Decomposition & Hybrid Methods]

    B --> B1["LSTM / BiLSTM / GRU Baselines (Zhu 2019×2, Hippert 2001)"]
    B --> B2["CNN-LSTM-Attention & CAT-Former (Romia 2026, Hussain 2025)"]
    B --> B3["MLP & XGBoost Competitive Baselines (Bampos 2024)"]
    B --> B4["LSTM-Transformer Hybrid (Feng 2024, Hussain 2025)"]
    B --> B5["Autoformer Decomposition (Helmy 2024)"]

    C --> C1["Physics-Informed Attention Graph PAG (Qu 2024)"]
    C --> C2["GCN-TRN Spatial Transformer (Zhang 2022)"]
    C --> C3["Multi-Scale Spatial-Temporal GAT MSSTGAN (Tian 2025)"]
    C --> C4["EV-STLLM Large Language Model (Fan 2025)"]
    C --> C5["REST Network ResNet+SENet+Transformer (Alghamdi 2025)"]
    C --> C6["Multi-Scale Fusion Transformer MFT (Liu 2026)"]

    D --> D1["PICNN Convex Quantile Learning (Zheng 2025)"]
    D --> D2["Feature-Enhanced FEDM (Cao 2024)"]
    D --> D3["Multi-Quantile TCN & Pinball Loss (Ali 2024, Matrone 2025)"]
    D --> D4["DiffPLF Conditional Diffusion DDPM (Li 2024)"]
    D --> D5["Deep Gaussian Process DGP (Cao 2022)"]
    D --> D6["Conformal Prediction DER (Zhou 2024)"]
    D --> D7["DeepAR Autoregressive RNN (Salinas 2020)"]

    E --> E1["MetaProbformer Reptile Meta-Learning (Huang 2023)"]
    E --> E2["Inductive Transfer Learning MQ-TCN (Ali 2024)"]
    E --> E3["VMD + Prophet-LSTM Hybrid (Cheng 2023)"]
    E --> E4["Vertical Federated EGAT-LSTM (Han 2025)"]
    E --> E5["Personalized Federated pFed (Zhu 2025)"]
    E --> E6["Divide & Conquer Transformer Smart Meter (Ke 2024)"]

    F --> F1["Lyapunov Virtual Queue Dispatch (Huang 2021)"]
    F --> F2["V2G-SVE Value Metric (Zhong 2024)"]
    F --> F3["ADMM EVSFD Schedulable Capacity (Xu 2024)"]
    F --> F4["Multiscenario Stochastic MS-MPC (Yang 2025)"]
    F --> F5["Multiplicative Trend DAM Bidding (Bampos 2024)"]
    F --> F6["QoQ Queuing Model (Zhang 2021, Alizadeh 2014)"]

    G --> G1["Mamba-3 Selective SSM O(N) (Lahoti 2026)"]
    G --> G2["HyKANet Mamba + KAN (Hao 2026)"]
    G --> G3["PC-M3 Physics-Constrained Mamba MIMO (Chen 2026)"]
    G --> G4["Time Series Foundation Models Benchmark (Meyer 2025)"]
    G --> G5["EV-STLLM LoRA Fine-Tuned LLM (Fan 2025)"]

    H --> H1["BWO-ICEEMDAN-iTransformer Signal Decomp (Zheng 2025)"]
    H --> H2["VMD + Prophet + LSTM Hybrid (Cheng 2023)"]
    H --> H3["ResMMoT-Informer DWT + MoE (Bao 2025)"]
    H --> H4["Wavelet-CNN Ensemble (Zhang 2021)"]
```

---

## 🔑 Key Mathematical & Methodological Discoveries

### From Original 33 Papers

1. **Quantile Crossing Elimination via Convex Learning**:
   - Standard quantile regression frequently produces quantile inversion ($q_{0.2} > q_{0.8}$).
   - **PICNN Solution ([[2025_Zheng_Coherent_Hierarchical_EV_Load]])**: Learns a partially convex function $f(\alpha, h)$, taking its gradient $q(\alpha | h) = \nabla_\alpha f(\alpha, h)$ to strictly guarantee monotonic quantiles without crossing.

2. **Statistical Prior Reweighting for External Features**:
   - Arbitrarily feeding weather and TOU prices into deep networks creates noise.
   - **Pearson Prior Solution ([[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]])**: Computes Pearson correlation $r_{X,Y}$ as prior weights to initialize Gated Residual Networks (GRN), improving qualified prediction rate to **99.22%**.
   - **Scale-Masked Cross-Attention ([[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]])**: Combines scale masks with sample-level cross-attention feature reweighting for 96-hour forecasts.

3. **Data Scarcity & Few-Shot Station Generalization**:
   - Newly built stations lack historical load data.
   - **Inductive Transfer Learning ([[2024_Ali_MQ_TCN_Transfer_Learning_EV]])**: Uses DTW to match target stations and fine-tunes pre-trained TCN quantile heads, achieving **96.88% PICP coverage with only 2 weeks of data**.
   - **MetaProbformer ([[2023_Huang_MetaProbformer_EV_Load]])**: Uses Reptile meta-learning to generalize across stations with $<3$ days of historical data.

4. **Value-Oriented vs Error-Oriented Evaluation for Downstream V2G**:
   - Traditional MSE/MAE errors do not correlate with downstream V2G economic cost savings.
   - **V2G-SVE Metric ([[2024_Zhong_V2G_SVE_Evaluation_Metric]])**: Evaluates forecast value by simulating aggregate EV fleet battery degradation and peak shaving capability ($r=0.9994$).

5. **Operational Day-Ahead Market (DAM) Bidding**:
   - **Multiplicative Trend-Residual Decomposition ([[2024_Bampos_EV_Load_Forecasting_DAM]])**: Separates annual trend using Holt Exponential Smoothing before training ML models (XGBoost, MLP), outperforming complex deep learning on 36-hour rolling market forecasts.

6. **Stochastic Real-Time Control & Scenario Reduction**:
   - **Two-Layer MS-MPC ([[2025_Yang_Stochastic_MPC_Microgrid_EV]])**: Combines Latin Hypercube Sampling (LHS) with Two-Stage Simultaneous Backward Scenario Reduction to optimize microgrid V2G dispatch in **<0.9 seconds per step**.

### New Discoveries from Papers 34–54

7. **State Space Models (Mamba) — Post-Transformer Era**:
   - Transformers have $O(N^2)$ attention complexity, scaling poorly to long EV sequences.
   - **Mamba-3 ([[2026_Lahoti_Mamba_3_Sequence_Modeling]])**: Complex-valued Selective State Space Models with **linear $O(N)$ scaling**. HIPPO matrix initialization for long-range dependency capture.
   - **HyKANet ([[2026_Hao_Mamba_KAN_HyKANet_EV]])**: Combines Mamba (selective SSM) with KAN (Kolmogorov-Arnold Networks) for EV demand — KAN's learnable activation functions replace fixed MLPs.
   - **PC-M3 ([[2026_Chen_PC_M3_Mamba_EV_Clusters]])**: Physics-Constrained Mamba MIMO aggregator for 10,000+ EV clusters in real-time energy management.

8. **Generative Probabilistic Forecasting via Diffusion Models**:
   - Point forecasts and traditional quantile regression cannot capture complex multimodal demand distributions.
   - **DiffPLF ([[2024_Li_DiffPLF_Conditional_Diffusion_EV]])**: Conditional DDPM generates multiple EV load trajectories via reverse diffusion, producing full predictive distributions without quantile specification.
   - Key equation: $p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t, \mathbf{c}) = \mathcal{N}(\mu_\theta(\mathbf{x}_t, t, \mathbf{c}), \Sigma_\theta)$

9. **Distribution-Free Uncertainty via Conformal Prediction**:
   - Deep learning prediction intervals require distributional assumptions.
   - **Hierarchical Conformal Prediction ([[2024_Zhou_Conformal_Prediction_DER]])**: Provides **statistically guaranteed coverage** without any distributional assumptions, reconciled hierarchically for multi-feeder EV networks. Valid for any black-box model.

10. **Foundation Models for Zero-Shot EV Load Forecasting**:
    - Training station-specific models requires historical data that new stations lack.
    - **Foundation Model Benchmark ([[2025_Meyer_Benchmark_Foundation_Models]])**: Systematically evaluates TimesFM, Chronos, Moirai on short-term EV load forecasting. Key finding: **foundation models competitive with supervised LSTM/Transformer when historical data < 4 weeks**, but underperform with sufficient data.

11. **Federated Learning — Privacy-Preserving Multi-Station Forecasting**:
    - Sharing raw EV charging data raises user privacy concerns; centralized training is infeasible.
    - **Open gap — FL + decomposition**: VMD-Prophet-LSTM ([[2023_Cheng_VMD_Prophet_LSTM]]) is a *centralized* single-station hybrid (despite legacy "Federated" filename); combining local VMD-style preprocessing with horizontal federated aggregation remains unexplored.
    - **Vertical FL + EGAT-LSTM ([[2025_Han_Vertical_Federated_EGAT_LSTM]])**: Couples transportation and power distribution grid data under VFL — different data owners share graph embeddings without raw data exposure.
    - **Personalized FL ([[2025_Zhu_Personalized_Federated_Learning]])**: Addresses statistical heterogeneity (non-IID) across households with imbalanced historical data via local adaptation layers.

12. **LLM-Adapted Spatio-Temporal Forecasting**:
    - Large Language Models encode rich spatio-temporal priors from pre-training.
    - **EV-STLLM ([[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]])**: Adapts GPT-style LLM with LoRA for city-wide EV station load and occupancy forecasting. Tokenizes spatial-temporal graph embeddings as LLM input.

13. **Signal Decomposition Before Deep Learning**:
    - Raw EV load signals contain mixed frequency components that confuse sequential models.
    - **ICEEMDAN ([[2025_Zheng_BWO_ICEEMDAN_iTransformer]])**: Improved Complete Ensemble EMD with Adaptive Noise separates intrinsic mode functions; inverted Transformer processes each IMF independently. BWO (Black Widow Optimization) for hyperparameter tuning.
    - **VMD ([[2023_Cheng_VMD_Prophet_LSTM]])**: Variational Mode Decomposition as preprocessing before Prophet trend estimation + LSTM residual forecasting.

14. **Autoformer's Progressive Series Decomposition for EV Load**:
    - Standard Transformers struggle with non-stationarity in EV session data.
    - **Autoformer ([[2024_Helmy_Autoformer_EV_Charging]])**: Auto-Correlation mechanism replaces self-attention; progressive trend-seasonality decomposition blocks handle long-range dependencies. Evaluated for EV charging load specifically.

15. **Real-World DC Fast-Charging Profile Prediction**:
    - Most papers forecast total station energy; DC fast-charging requires per-session power profile curves.
    - **TFT for DC Profiles ([[2025_Li_DC_Charging_Profiles_TFT]])**: Temporal Fusion Transformer predicts complete charging power curve shape and session duration (not just aggregate load). Published in Nature Communications — highest-impact venue in this collection.

16. **Cybersecurity via Graph Contrastive Learning in EV Charging**:
    - EV charging networks are attack surfaces for adversarial load manipulation.
    - **MV-GCL ([[2025_Li_Multi_View_Graph_Intrusion_Detection_EV]])**: Multi-View Graph Contrastive Learning for anomaly/intrusion detection at EV stations — tangential to forecasting but relevant to data quality and adversarial robustness.

---

## 🆕 Updated Model Landscape Summary

### Architecture Evolution Timeline

| Era | Dominant Architecture | Representative Papers |
|-----|----------------------|----------------------|
| Pre-2019 | LSTM, GRU, ANN | [[1997_Hochreiter_Long_Short_Term_Memory]], [[2001_Hippert_Neural_Networks_STLF_Review]] |
| 2019–2021 | LSTM ensembles, RL, Queuing | [[2019_Zhu_EV_Load_Forecasting]], [[2021_Zhang_Probabilistic_Queuing_EV_Load]] |
| 2022–2023 | GNN, Transformer, Meta-learning | [[2022_Zhang_GCN_TRN_EV_Availability]], [[2023_Huang_MetaProbformer_EV_Load]] |
| 2024 | Hybrid Transformer, Probabilistic, Physics-Informed | [[2024_Qu_Physics_Informed_GAT_EV_Load]], [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] |
| 2025 | Federated, Foundation Models, LLMs, Signal Decomp | [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]], [[2025_Meyer_Benchmark_Foundation_Models]] |
| 2026 | Mamba SSM, KAN, Physics-Constrained | [[2026_Hao_Mamba_KAN_HyKANet_EV]], [[2026_Chen_PC_M3_Mamba_EV_Clusters]] |

---

## 🎯 Updated Research Gaps (6 Primary)

### Gap 1: Causal Price Elasticity in Spatial-Temporal Forecasting *(Original)*
- Existing GNN models assume price sensitivity is purely numerical, leading to spurious positive demand correlation during peak prices.
- **Proposed Focus**: Integrate Physics-Informed Neural Network (PIML) pseudo-sampling ([[2024_Qu_Physics_Informed_GAT_EV_Load]]) with Multi-Scale Graph Attention ([[2025_Tian_MSSTGAN_City_EV_Load]]).
- **Supporting evidence**: Price misinterpretation documented in [[2024_Qu_Physics_Informed_GAT_EV_Load]]; Federated graph approach via [[2025_Han_Vertical_Federated_EGAT_LSTM]] offers privacy-preserving spatial coupling.

### Gap 2: Unified Coherent Probabilistic Hierarchical Reconciliation *(Original)*
- Multi-station forecasts rarely satisfy total feeder summation ($y_t = \mathbf{S}\mathbf{z}_t$).
- **Proposed Focus**: Combine PICNN quantile monotonicity ([[2025_Zheng_Coherent_Hierarchical_EV_Load]]) with Differentiable Convex Optimization Layers (`Cvxpylayers`) for multi-feeder EV networks.
- **New angle**: [[2024_Zhou_Conformal_Prediction_DER]] provides distribution-free conformal reconciliation — could be combined with PICNN for double guarantee (monotonicity + coverage).

### Gap 3: Ultra-Low Data Adaptation for Fast-Charging Stations *(Original — Expanded)*
- DC fast-charging stations exhibit high volatility and lack long historical records.
- **Extended finding**: [[2025_Meyer_Benchmark_Foundation_Models]] shows foundation models (Chronos, TimesFM) are competitive with $<4$ weeks of data — **zero-shot transfer learning is now a viable alternative** to inductive transfer.
- **Proposed Focus**: Benchmark foundation models vs. MQ-TCN transfer learning ([[2024_Ali_MQ_TCN_Transfer_Learning_EV]]) specifically for DC fast-charging using [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] as the task setup.

### Gap 4: Value-Oriented Downstream V2G Bidding Optimization *(Original)*
- Model training should optimize downstream market bidding revenue rather than standard MSE loss.
- **Proposed Focus**: Adopt V2G-SVE evaluation ([[2024_Zhong_V2G_SVE_Evaluation_Metric]]) and Forecast-Enhanced Lyapunov Optimization ([[2021_Huang_Lyapunov_EV_Scheduling]]) or MS-MPC ([[2025_Yang_Stochastic_MPC_Microgrid_EV]]).
- **New angle**: PC-M3 ([[2026_Chen_PC_M3_Mamba_EV_Clusters]]) demonstrates real-time feasibility for 10,000+ EV clusters — combining value-oriented training with Mamba-based real-time control is unexplored.

### Gap 5: Privacy-Preserving Spatial-Temporal Probabilistic Forecasting *(NEW)*
- Federated learning papers (Han 2025, Zhu 2025) separately address privacy and spatial-temporal structure — but **no paper combines federated learning with hierarchical probabilistic coherence**.
- **Open question**: Can vertical FL ([[2025_Han_Vertical_Federated_EGAT_LSTM]]) + conformal prediction ([[2024_Zhou_Conformal_Prediction_DER]]) produce statistically valid prediction intervals without centralizing data?
- **Research gap**: Federated coherent probabilistic forecasting for multi-operator EV charging networks.

### Gap 6: Post-Transformer Sequence Models for Long-Range EV Demand *(NEW)*
- Mamba (2026) and KAN (2026) represent fundamentally new architectural paradigms with $O(N)$ complexity.
- **Current state**: HyKANet ([[2026_Hao_Mamba_KAN_HyKANet_EV]]) and PC-M3 ([[2026_Chen_PC_M3_Mamba_EV_Clusters]]) are early applications — not yet benchmarked against full probabilistic forecasting suites.
- **Open question**: Can Mamba-3 ([[2026_Lahoti_Mamba_3_Sequence_Modeling]]) with complex-valued SSM outperform iTransformer ([[2025_Zheng_BWO_ICEEMDAN_iTransformer]]) for multi-week EV demand forecasting with uncertainty quantification?
- **Research gap**: Mamba + probabilistic output head (quantile or diffusion) for long-horizon EV charging demand.

---

## 📊 Metric Coverage Matrix

| Paper Category | MAE | RMSE | MAPE | CRPS | PICP | Winkler | V2G-SVE |
|---------------|-----|------|------|------|------|---------|---------|
| Point forecast (LSTM/GRU/MLP) | ✅ | ✅ | ✅ | — | — | — | — |
| Probabilistic (Quantile/Diffusion) | ✅ | ✅ | — | ✅ | ✅ | ✅ | — |
| V2G / Control | ✅ | ✅ | — | — | — | — | ✅ |
| Spatial-Temporal | ✅ | ✅ | ✅ | — | — | — | — |
| Foundation Models | ✅ | ✅ | ✅ | ✅ | — | — | — |

> [!TIP]
> For a thesis covering probabilistic forecasting + V2G: report MAE, RMSE, CRPS, PICP (90%), Winkler Score, **and** V2G-SVE for complete coverage of both forecast quality and downstream value.

---

## 🔗 Cross-Reference: Datasets × Methods

| Dataset | Best Method Found | Paper |
|---------|------------------|-------|
| [[Caltech_ACN]] | MQ-TCN Transfer Learning | [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] |
| [[ElaadNL]] | PICNN Coherent Hierarchical | [[2025_Zheng_Coherent_Hierarchical_EV_Load]] |
| [[Boulder_Colorado]] | XGBoost + Multiplicative Decomp | [[2024_Bampos_EV_Load_Forecasting_DAM]] |
| [[Pecan_Street]] | Personalized Federated Learning | [[2025_Zhu_Personalized_Federated_Learning]] |
| Custom DC Fast-Charging | CNN-LSTM-Attention (Optuna tuned) | [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] |

---

*Last updated: 2026-08-08 | Papers ingested: 59 | Gaps identified: 6 primary + 7 Transformer-specific*

---

## 🤖 Transformer Deep-Dive: Specific Gaps & Limitations

> [!IMPORTANT]
> Section added 2026-08-08 — focused gap analysis for Transformer-based EV charging load forecasting, synthesized directly from 20 Transformer-related papers.

### Background: Transformer Variant Landscape in This Corpus

| Paper | Model / Architecture | Key Innovation | Limitation Identified |
|-------|---------------------|----------------|----------------------|
| [[2017_Vaswani_Attention_Is_All_You_Need]] | Original Transformer | Multi-head self-attention | O(N²) complexity; cannot handle very long sequences efficiently |
| [[2022_Zhang_GCN_TRN_EV_Availability]] | GCN-TRN | GCN + Transformer | Lacks local feature extraction; limited spatial scalability |
| [[2023_Huang_MetaProbformer_EV_Load]] | MetaProbformer (Informer variant) | Reptile meta-learning | Single-variate only; memory limits input sequence length |
| [[2023_Li_Transformer_EV_Charging_Demand]] | Vanilla Transformer | First use for EV demand | Day-level aggregation only; no hourly resolution |
| [[2024_Qu_Physics_Informed_GAT_EV_Load]] | PAG (Physics + Attention Graph) | Physics-informed meta-learning | Cannot handle completely unobserved pricing mechanisms |
| [[2024_Ke_Divide_Conquer_Transformer_Smart_Meter]] | DCT-EV | CNN embedding + self-attention | Home charging only; no multi-household aggregation |
| [[2024_Feng_LSTM_Transformer_Energy_Consumption]] | LSTM + Transformer | Long+short term fusion | Single-vehicle focus; geographic generalization not validated |
| [[2024_Li_Attention_MultiGraph_EV_Load]] | AST-MGCN (Multi-Graph + Attention) | Multi-graph spatial attention | Assumes location correlation exists (fails for distant stations) |
| [[2024_Helmy_Autoformer_EV_Charging]] | Autoformer | Series decomposition + auto-correlation | Data scarcity worsens performance; short-term underperformance |
| [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] | BWO-ICEEMDAN-iTransformer | Signal decomp + inverted Transformer | Evaluated on general load only; not EV-specific |
| [[2025_Ramzan_LSTM_Transformer_Charging_Stations]] | LSTM-Transformer Hybrid | Complementary fusion | High computational cost; not suitable for real-time/edge |
| [[2025_Hussain_CAT_Former_EV_STCS]] | CAT-Former | Context-aware temporal Transformer | Aggregated evaluation; ignores inter-station spatial correlation |
| [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] | MFT (Multi-scale Fusion Transformer) | Scale mask + cross-attention | Battery-related factors not yet incorporated |

---

### 🔴 Transformer Gap T-1: Quadratic Complexity vs. Long EV Sequences

**Core Problem**: Standard Transformer self-attention has $O(N^2)$ time and memory complexity, where $N$ = sequence length. EV charging datasets typically require input windows of 48–168 time steps (2–7 days at 30-min resolution) — at which point vanilla Transformer becomes computationally prohibitive for real-time deployment.

**Evidence from papers**:
- [[2023_Huang_MetaProbformer_EV_Load]]: *"The memory usage for piling encoder/decoder layers also restricts the length of the input sequence for vanilla Transformer."*
- [[2025_Ramzan_LSTM_Transformer_Charging_Stations]]: *"The complexity of the model makes it more demanding and the training time can be longer which can be restrictive in the usage of real-time applications in other environments that are resource-limited."*
- [[2026_Lahoti_Mamba_3_Sequence_Modeling]]: Mamba-3 directly addresses this with $O(N)$ selective SSM — confirming this is an active research frontier.

**Current Workarounds**: 
- Informer (ProbSparse attention) → used in MetaProbformer
- Autoformer (auto-correlation) → used in [[2024_Helmy_Autoformer_EV_Charging]]
- LSTM preprocessing to compress sequences → used in [[2025_Ramzan_LSTM_Transformer_Charging_Stations]]

**Open Gap**: None of the EV-specific papers have adopted Mamba/SSM as a drop-in replacement. The computational cost barrier remains unaddressed for EV charging scenarios with high-frequency (15-min or 1-min) data.

---

### 🔴 Transformer Gap T-2: Standard Transformer Applied Directly to Time-Series — Inappropriate Inductive Bias

**Core Problem**: Transformers were designed for token-sequence NLP tasks. Applying positional encoding and standard tokenization directly to continuous time-series violates inductive bias assumptions — leading to inferior short-term performance compared to LSTM.

**Evidence from papers**:
- [[2024_Feng_LSTM_Transformer_Energy_Consumption]]: *"However, applying the Transformer model to time series forecasting directly may not be appropriate."*
- [[2023_Li_Transformer_EV_Charging_Demand]]: *"Transformer provided the best long-term prediction performance… Even while the model's performance for short-term prediction is slightly behind that of LSTM."*
- [[2025_Hussain_CAT_Former_EV_STCS]]: *"They aggregated the demand data by day to predict for 7, 30, and 90 days ahead; the data aggregation reduced the training data size for the proposed Transformer model and also disabled its capacity to forecast for shorter time steps (e.g., 1h)."*

**Variants that attempt to fix this**:
- **iTransformer** ([[2025_Zheng_BWO_ICEEMDAN_iTransformer]]): Inverts token and feature dimensions — treats each variate as a token
- **CAT-Former** ([[2025_Hussain_CAT_Former_EV_STCS]]): Context-aware temporal encoding with session-level features
- **MFT** ([[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]]): Scale masks for multi-granularity temporal modeling

**Open Gap**: No paper has systematically benchmarked which tokenization strategy (patch-based, variate-based, temporal hierarchy) is optimal specifically for EV charging load with its distinct patterns (diurnal + weekly periodicity + stochastic EV arrival).

---

### 🔴 Transformer Gap T-3: Single-Variate Dominance — Multivariate Context Underutilization

**Core Problem**: Most Transformer papers for EV charging are trained and evaluated on **single-variate historical load** only. External factors (weather, traffic, time-of-use price, EV fleet growth) are either ignored or naively concatenated without principled attention-based fusion.

**Evidence from papers**:
- [[2023_Huang_MetaProbformer_EV_Load]]: *"Given that historical data for other variates is missing from the public-available datasets, our experiments are mainly focused on forecasting with single-variate. We believe that the proposed methods in this work can be naturally extended to multivariate forecasting."*
- [[2024_Helmy_Autoformer_EV_Charging]]: *"The scarcity of accessible data on EV charging and driving patterns hinders the development of accurate EV load forecasting models."*
- [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]]: *"Existing deep learning models still struggle to capture the multi-scale temporal dependency of charging load and fail to fully incorporate the dynamic influence of external factors such as weather and traffic conditions."*

**Attempted solutions**:
- PAG ([[2024_Qu_Physics_Informed_GAT_EV_Load]]): Physics laws as prior to incorporate price features
- MFT ([[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]]): Pearson correlation weighting + cross-attention fusion

**Open Gap**: No Transformer paper for EV charging has evaluated whether **learned cross-attention weighting** (which factors, at which time) is superior to fixed-weight multivariate fusion. SHAP/attention interpretability for feature importance is largely absent from the EV Transformer literature.

---

### 🟡 Transformer Gap T-4: Purely Point-Forecast Transformers — Probabilistic Output is Rare

**Core Problem**: Despite the strong need for uncertainty quantification in EV grid management, the majority of Transformer-based EV forecasting papers produce **point estimates only**. Probabilistic Transformer variants are underexplored for EV charging specifically.

**Evidence from papers**:
- [[2024_On_Autoformer_EV_Charging]]: Autoformer evaluated only with MAE/RMSE/MAPE — no uncertainty quantification.
- [[2023_Li_Transformer_EV_Charging_Demand]]: Compared against ARIMA/LSTM using RMSE alone.
- [[2023_Huang_MetaProbformer_EV_Load]]: **Exception** — adapts Informer to probabilistic forecasting using quantile heads.
- [[2025_Matrone_Probabilistic_LSTM_Attention]]: Uses LSTM+attention with quantile regression — suggests the gap exists even in attention-based work.

**Probabilistic Transformer options not yet applied to EV charging**:
- Temporal Fusion Transformer (TFT) with quantile head — used for DC charging profiles only in [[2025_Li_DC_Charging_Profiles_TFT]]
- Diffusion + Transformer conditioning (DiffPLF [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] uses cross-attention but the backbone is a diffusion model)
- Conformalized Transformer (Transformer + conformal prediction calibration)

**Open Gap**: A Transformer architecture with **native probabilistic output** (e.g., distribution-head or normalizing flow decoder) compared head-to-head with MetaProbformer and DiffPLF on the same EV dataset has not been done.

---

### 🟡 Transformer Gap T-5: Spatial Attention — Static Graph vs. Dynamic Graph Structure

**Core Problem**: Transformer-based spatial-temporal models for EV charging define the adjacency graph **statically** (based on geographic distance or road connectivity). This fails to capture **dynamic demand coupling** between charging stations that varies by time of day, day of week, or seasonal context.

**Evidence from papers**:
- [[2024_Li_Attention_MultiGraph_EV_Load]]: *"The model without graph over-reliance on time series features fails to provide an accurate forecast."* + *"The major limitation is that the proposed model is based on the supposition of the existence of location correlations in historical temporal load series, which cannot be captured completely when the charging stations are relatively far away."*
- [[2022_Zhang_GCN_TRN_EV_Availability]]: *"The transformer utilization method is able to comprehend periodicity in a global view, however, it has a limitation of aggregating local information."*
- [[2026_Hao_Mamba_KAN_HyKANet_EV]]: addresses this by introducing a **dynamic adjacency module** — but uses Mamba, not pure Transformer.

**Open Gap**: Dynamic graph Transformer (where adjacency is learned per time step, e.g., via attention over node embeddings) for EV charging has not been proposed. The HyKANet approach (2026) demonstrates demand exists; a pure Transformer version would fill this gap.

---

### 🟡 Transformer Gap T-6: Interpretability & Attention Weight Analysis

**Core Problem**: Transformer models used for EV charging are treated as black boxes — no paper performs systematic **attention weight visualization** or **feature attribution** to explain *which* historical time steps and *which* external features drive the prediction. This limits regulatory adoption and grid operator trust.

**Evidence from papers**:
- [[2025_Li_Enhanced_Transformer_BiLSTM_Energy_Price]]: *"Explainability techniques such as LIME (Local Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations) will be integrated to make the proposed model more transparent"* — listed as **future work only**.
- [[2024_Qu_Physics_Informed_GAT_EV_Load]]: Physics-informed pre-training provides some interpretability via economic laws, but attention weights are not analyzed.
- [[2025_Benchmarking_Foundation_Models_EV]]: *"Whether massive pre-training of Transformers on very large collections of generic time series can actually represent household load patterns in real-world scenarios is an empirical question."*

**Open Gap**: A dedicated Transformer interpretability study for EV charging load — mapping attention heads to temporal patterns (diurnal, weekly) and spatial patterns (neighboring stations) — is completely absent from this corpus.

---

### 🟢 Transformer Gap T-7: Hybrid Transformer + Emerging Architectures (Mamba, KAN, LLM)

**Core Problem**: The field is transitioning from pure Transformer to hybrid architectures. Papers from 2026 show Mamba and KAN outperforming Transformers, but systematic **ablation studies comparing Transformer vs. Mamba vs. hybrid** within a single EV charging benchmark are absent.

**Evidence from papers**:
- [[2026_Hao_Mamba_KAN_HyKANet_EV]]: Mamba+KAN (HyKANet) achieves 17.3% better RMSE than PAG (attention-based). Shows Mamba replacing self-attention.
- [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]]: Optimized Transformer still outperforms vanilla GRU/LSTM/BiLSTM, but not compared to Mamba.
- [[2025_Benchmarking_Foundation_Models_EV]]: *"Foundation models perform comparably to TFS Transformer models… while certain conditions favor TFS Transformer."*
- [[2026_Lahoti_Mamba_3_Sequence_Modeling]]: Mamba-3 surpasses Transformers on sequence tasks with O(N) complexity.

**Emerging research directions**:
1. **Transformer + Mamba hybrid**: Use Transformer for global periodicity + Mamba for local dynamics
2. **KAN decoder for Transformer**: Replace MLP decoder layers with KAN for better nonlinear representation
3. **Frozen LLM + fine-tuned Transformer attention**: EV-STLLM pattern applied with LoRA on SOTA time-series Transformer

**Open Gap**: No EV charging paper has benchmarked pure Transformer vs. Mamba vs. Transformer+Mamba hybrid on identical datasets and evaluation protocols. This three-way comparison is the most immediately actionable research gap.

---

## 🎯 Summary: Transformer Gap Priority Matrix

| Gap ID | Description | Novelty | Feasibility | Impact | Priority |
|--------|-------------|---------|-------------|--------|----------|
| **T-1** | O(N²) complexity — long EV sequences | High | Medium | High | 🔴 Critical |
| **T-2** | Inappropriate direct time-series application | Medium | High | High | 🔴 Critical |
| **T-3** | Single-variate dominance — multivariate underuse | High | High | High | 🔴 Critical |
| **T-4** | Point-only output — probabilistic Transformer rare | High | High | Very High | 🔴 Critical |
| **T-5** | Static vs. dynamic spatial graph structure | High | Medium | High | 🟡 Important |
| **T-6** | Interpretability — no attention weight analysis | Medium | High | Medium | 🟡 Important |
| **T-7** | Transformer vs. Mamba vs. hybrid — no benchmark | Very High | High | Very High | 🟢 Emerging |

> [!TIP]
> **Recommended thesis focus**: Combine **T-4** (probabilistic Transformer) + **T-7** (Transformer vs. Mamba comparison) into a single contribution: a **probabilistic hybrid Transformer-Mamba model** evaluated on EV charging demand with CRPS + PICP metrics.

---

## 📚 New Papers Added (Papers 55–59)

The following papers were added after the previous version (2026-08-02):

| File | Key Contribution | Relevance |
|------|-----------------|-----------|
| [[2025_Benchmarking_Foundation_Models_EV]] | Zero-shot foundation models vs. TFS Transformer | Gap T-7, Gap 3 |
| [[2026_Mamba_3_Sequence_Modeling]] | O(N) complex-valued SSM | Gap T-1, Gap 6 |
| [[2026_Hao_Mamba_KAN_HyKANet_EV]] | Mamba + KAN for EV demand | Gap T-7, Gap 6 |
| [[2026_Chen_PC_M3_Mamba_EV_Clusters]] | Physics-constrained Mamba MIMO | Gap T-1, Gap 4 |
| [[2025_REST_Ensemble_Deep_Learning_Port_EV]] | ResNet+SENet+Transformer ensemble | Gap T-7 |

---

*Last updated: 2026-08-10 | Papers ingested: 70 | Gaps identified: 6 primary + 7 Transformer-specific + 5 Probabilistic-specific*

---

## 🎲 Probabilistic Deep-Dive: Theoretical Gaps & Uncertainty Quantification (Gaps P-1 to P-5)

> [!IMPORTANT]
> Section added 2026-08-10 — focused gap analysis for Probabilistic Time-Series & EV Charging Load Forecasting, synthesized across statistical learning theory and power system literature.

### 🔴 Probabilistic Gap P-1: Monotonicity vs. Tail Expressiveness Paradox (Quantile Crossing in Convex Nets)
- **Core Problem**: Multi-quantile models suffer from quantile crossing ($\hat{q}_{\alpha_1} > \hat{q}_{\alpha_2}$). While Partially Input Convex Neural Networks (PICNN) enforce monotonicity via non-negative weights ($W \ge 0$), this constraint restricts tail expressiveness, causing oversmoothing and underestimation at extreme tail quantiles ($\alpha \ge 0.95$).
- **Impact on EV**: Severe under-prediction of extreme high-power charging spikes during peak demand hours.
- **Open Research Gap**: Designing strictly monotonic quantile architectures that preserve sharpness and expressiveness at extreme high-volatility tail spikes.

### 🔴 Probabilistic Gap P-2: Autoregressive Accumulation vs. Joint Temporal Trajectory Coherence
- **Core Problem**: Autoregressive probabilistic models (DeepAR) experience exponential error accumulation over multi-step horizons ($t+1 \dots t+48$). Direct Multi-Step (DMS) models (TFT, MQ-TCN) avoid error accumulation but project independent marginal quantiles $\hat{q}_\alpha(t+h)$, failing to capture joint path distributions $p(y_{1:H} | x)$.
- **Impact on EV**: Inability to evaluate total cumulative 24-hour energy delivery ($\sum_{\tau=1}^H y_{t+\tau}$) for battery storage and V2G dispatch.
- **Open Research Gap**: Non-autoregressive multi-horizon decoders that model joint temporal trajectory covariance without compounding recursive variance.

### 🔴 Probabilistic Gap P-3: Adaptive Conformal Recalibration Under Severe Non-Stationarity
- **Core Problem**: Adaptive Conformal Inference (ACI) guarantees finite-sample coverage ($\mathbb{P}(y_t \in \hat{I}_t) \ge 1-\alpha$) assuming exchangeability. EV load profiles violate exchangeability due to dynamic Time-of-Use (TOU) tariffs, extreme weather, and non-stationary driver behavior, causing severe ACI adaptation lag (under-coverage followed by interval dilation).
- **Impact on EV**: Inaccurate prediction intervals during sharp weather transitions or sudden tariff updates.
- **Open Research Gap**: Covariate-aware, real-time conformal recalibration that adapts dynamically to distribution shifts without excessive interval dilation.

### 🟡 Probabilistic Gap P-4: Multimodal Generative Diffusion Latency vs. Operational Real-Time Control
- **Core Problem**: Conditional Diffusion Models (DiffPLF) capture complex multimodal demand distributions (DC fast-charging vs AC overnight vs V2G idle) where scalar quantile regression fails. However, reverse denoising requiring 50–100 sampling steps introduces high computational latency, preventing real-time control (<1 sec).
- **Impact on EV**: Incompatibility with real-time microgrid dynamic power allocation and dynamic pricing response.
- **Open Research Gap**: Lightweight, distilled generative diffusion decoders with formal distribution-free coverage guarantees for sub-second microgrid dispatch.

### 🟡 Probabilistic Gap P-5: Non-Linearity of Quantiles in Spatial-Temporal Hierarchical Reconciliation
- **Core Problem**: EV charging demand spans hierarchical levels (Charger $\to$ Station Hub $\to$ Feeder $\to$ Substation). Standard point forecast reconciliation ($\hat{\mathbf{y}}_t = \mathbf{S}\hat{\mathbf{b}}_t$) fails because quantiles are non-additive ($q_\alpha(A+B) \neq q_\alpha(A) + q_\alpha(B)$), leading to quantile inversion and negative physical load values across grid levels.
- **Impact on EV**: Operational conflicts between Distribution System Operators (DSOs) and Charge Point Operators (CPOs).
- **Open Research Gap**: Coherent spatial-temporal quantile reconciliation frameworks preserving physical non-negativity and marginal calibration across hierarchical power grids.

---

### 📊 Summary: Probabilistic Gap Priority Matrix

| Gap ID | Description | Novelty | Feasibility | Impact | Priority |
|--------|-------------|---------|-------------|--------|----------|
| **P-1** | Monotonicity vs. Tail Sharpness Paradox (PICNN oversmoothing) | High | High | High | 🔴 Critical |
| **P-2** | Autoregressive Accumulation vs. Joint Trajectory Coherence | High | Medium | High | 🔴 Critical |
| **P-3** | Conformal Recalibration under Severe Non-Stationarity | High | High | High | 🔴 Critical |
| **P-4** | Generative Diffusion Latency vs. Real-Time Microgrid Control | Medium | Medium | Medium | 🟡 Important |
| **P-5** | Non-Linear Quantiles in Hierarchical Grid Reconciliation | High | Medium | High | 🟡 Important |

## 🆕 New Foundational Baselines Added (2026-08-20)

- **TCN** ([[2018_Bai_Empirical_TCN_Sequence_Modeling]]) provides a causal dilated-convolution baseline with long effective memory and linear-time sequence processing.
- **N-BEATS** ([[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]]) provides an interpretable residual-MLP point-forecast baseline.
- **N-HiTS** ([[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]]) adds multi-rate sampling and hierarchical interpolation for efficient long-horizon forecasting.
- **TiDE** ([[2024_Das_TiDE_Long_Term_Forecasting]]) provides a fast covariate-aware dense encoder-decoder without self-attention.

These models strengthen the controlled benchmark required by Gap T-7 and the proposed peak-aware probabilistic study: compare recurrent, convolutional, dense residual, hierarchical multi-scale, Transformer and Mamba backbones under the same EV dataset and evaluation protocol. Their original studies are mostly point-forecast benchmarks, leaving probabilistic heads, peak calibration and downstream V2G value as open extensions.
