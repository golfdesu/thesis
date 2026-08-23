# 📝 Thesis Progress Summary: Model Benchmarks, Architectural Analysis & Research Gaps

> **Topic:** Improving Baseline Time-Series Transformer for EV Charging Station Load Forecasting  
> **Last Updated:** 2026-08-23 (refreshed after ingestion of papers 81–103; corpus now 103 papers)  
> **Status:** Initial Benchmark Evaluation & Gap Analysis Complete; corpus refreshed

---

## 📌 Executive Summary

This document summarizes the current thesis progress, evaluation results across 5 baseline/benchmark models, an architectural comparison between the codebase implementations and original research literature, and identified research gaps to guide the proposed thesis contribution.

The core objective of this thesis is to **redesign and improve the baseline Transformer architecture to consistently outperform existing time-series benchmarks** (Informer, Autoformer, TFT, PTFT) in EV charging demand forecasting.

---

## 1. 📊 Progress & Benchmark Evaluation Results

Five Transformer-based models were evaluated on the EV charging load dataset under **SEED 42**:
1. `01_tfm_tfm` — Baseline Encoder-Only Transformer (TFM)
2. `02_tfm_ifm` — Informer Attention Model (IFM)
3. `03_tfm_afm` — Autoformer Decomposition Model (AFM)
4. `04_tfm_tft` — Temporal Fusion Transformer Attention (TFT)
5. `05_tfm_ptft` — Patch Temporal Fusion Transformer (PTFT)

### Performance Metrics Comparison Across Horizon Steps

#### **Step 0: Ultra Short-Term Forecast (30 min ahead)**
| Model | MAE (kWh) ↓ | RMSE (kWh) ↓ | R² ↑ | WAPE ↓ | Peak Zone WAPE ↓ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `01_tfm_tfm` (Base TFM) | 3.6682 | 5.4340 | 0.3855 | 86.07% | 36.93% |
| `02_tfm_ifm` (Informer) | 3.1559 | 4.3234 | 0.6110 | 74.05% | 27.74% |
| 🏆 **`03_tfm_afm` (Autoformer)** | **2.9481** | **3.9974** | **0.6675** | **69.17%** | **26.61%** |
| `04_tfm_tft` (TFT) | 3.1687 | 4.4517 | 0.5876 | 74.35% | 28.92% |
| `05_tfm_ptft` (PTFT) | 3.4469 | 4.8467 | 0.5112 | 80.87% | 35.24% |

#### **Step 5: Short-Term Forecast (3 hours ahead)**
| Model | MAE (kWh) ↓ | RMSE (kWh) ↓ | R² ↑ | WAPE ↓ | Peak Zone WAPE ↓ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `01_tfm_tfm` (Base TFM) | 3.2642 | 4.6823 | 0.5438 | 76.62% | 32.82% |
| 🏆 **`02_tfm_ifm` (Informer)** | **2.7304** | **3.8943** | **0.6845** | **64.09%** | **26.84%** |
| `03_tfm_afm` (Autoformer) | 2.9601 | 4.2179 | 0.6298 | 69.48% | 27.34% |
| `04_tfm_tft` (TFT) | 2.9641 | 4.2959 | 0.6160 | 69.57% | 33.18% |
| `05_tfm_ptft` (PTFT) | 3.0539 | 4.4954 | 0.5795 | 71.68% | 34.10% |

#### **Step 11: Medium-Term Forecast (6 hours ahead)**
| Model | MAE (kWh) ↓ | RMSE (kWh) ↓ | R² ↑ | WAPE ↓ | Peak Zone WAPE ↓ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `01_tfm_tfm` (Base TFM) | 3.0719 | 4.6148 | 0.5568 | 72.10% | 34.58% |
| 🏆 **`02_tfm_ifm` (Informer)** | **2.7588** | **4.0412** | **0.6602** | **64.75%** | **24.69%** |
| `03_tfm_afm` (Autoformer) | 2.8897 | 4.0594 | 0.6571 | 67.82% | 26.44% |
| `04_tfm_tft` (TFT) | 3.1149 | 4.4425 | 0.5893 | 73.10% | 33.88% |
| `05_tfm_ptft` (PTFT) | 3.0432 | 4.5082 | 0.5771 | 71.42% | 34.70% |

#### **Step 47: Long-Term Horizon (24 hours ahead)**
| Model | MAE (kWh) ↓ | RMSE (kWh) ↓ | R² ↑ | WAPE ↓ | Peak Zone WAPE ↓ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `01_tfm_tfm` (Base TFM) | 3.3922 | 4.8216 | 0.5082 | 80.16% | 29.39% |
| 🏆 **`02_tfm_ifm` (Informer)** | **2.9275** | **4.2503** | **0.6179** | **69.18%** | **26.70%** |
| `03_tfm_afm` (Autoformer) | 3.2089 | 4.4194 | 0.5868 | 75.83% | 31.70% |
| `04_tfm_tft` (TFT) | 3.2305 | 4.4061 | 0.5893 | 76.34% | 27.31% |
| `05_tfm_ptft` (PTFT) | 3.2726 | 4.7066 | 0.5314 | 77.33% | 35.71% |

---

## 2. 🏛️ Architectural Analysis: Codebase Implementation vs. Literature

### Current Codebase Setup: Unified Encoder-Only Direct Multi-Step (DMS)
In the current project notebooks, all 5 models are standardized using an **Encoder-Only architecture** with a **Direct MLP Projection Head**:
- **Why Encoder-Only?** Encoder-Only models avoid autoregressive step-by-step decoding ($t+1, t+2 \dots$), eliminating **Error Accumulation**. They process the full historical window (96 steps / 48h) bidirectionally and output all 48 future time steps ($t+1 \dots t+48$) in a single forward pass.
- **Controlled Backbone Comparison:** This setup isolates and compares the **attention mechanism** of each variant (Standard Multi-Head Attention, ProbSparse, Auto-Correlation, Gated Attention) under a unified framework.

### Comparison with Original Literature
| Model | Original Literature Architecture | Codebase Implementation | Key Trade-off / Note |
| :--- | :--- | :--- | :--- |
| **Informer** *(Zhou 2021)* | **Encoder-Decoder** (ProbSparse + Distillation + Generative Decoder) | **Encoder-Only** (ProbSparse + Distillation + Direct MLP Output) | Simpler, faster training; avoids complex decoder masking. |
| **Autoformer** *(Wu 2021)* | **Encoder-Decoder** (Auto-Correlation + Progressive Decomposition) | **Encoder-Only** (Auto-Correlation + Series Decomposition + Direct Head) | Preserves core decomposition logic while reducing parameter count. |
| **TFT** *(Lim 2021)* | **Encoder-Decoder Hybrid** (Variable Selection + GRN + Known Future Inputs Decoder) | **Encoder-Only Hybrid** (Variable Selection + GRN + Direct Head) | Ideal when future covariates (e.g. 24h weather forecasts) are unavailable. |
| **PatchTST** *(Nie 2023)* | **Encoder-Only** (Time-series Patching + Channel Independence) | **Encoder-Only** (Patching + Temporal Attention) | Aligns closely with modern time-series foundation benchmarks. |
| **iTransformer** *(Liu 2024)* | **Encoder-Only** (Inverted Variate-level Attention + Temporal MLP) | *Candidate for baseline improvement* | High potential for multi-variate EV load datasets. |

---

## 3. 🔬 Key Research Gaps of Standard Transformers in Time-Series

Based on literature review across all **103 EV load forecasting papers** now ingested in `wiki/papers/`, 6 primary research gaps have been identified in standard Transformer architectures:

1. **Non-Stationarity & Distribution Shift:**
   - Standard Transformers assume stable temporal distributions. EV load profiles exhibit heavy non-stationarity due to weather, day-of-week, and seasonal shifts.
   - *Gap:* Lack of instance-level normalization (e.g. **RevIN**) and series decomposition to stabilize inputs.

2. **Feature Noise & Lack of Feature Selection:**
   - Raw multi-dimensional features (weather, calendar, lag features) introduce noise when passed directly into self-attention.
   - *Gap:* Standard Transformers lack **Variable Selection Networks (VSN)** or **Pearson Prior Reweighting** to filter irrelevant features prior to attention.

3. **Smooth Regressive Bias & Peak Load Underestimation:**
   - Standard MSE/MAE loss functions force the model towards mean regression, severely underestimating critical **Peak Loads (Top 20% > 17.35 kWh)**.
   - *Gap:* Peak Zone WAPE remains high (24%–37%). Lack of **Extreme-Value-Aware Attention** or **Asymmetric Peak Loss Functions**.

4. **Single-Scale Point-Wise Attention:**
   - Point-wise attention at 30-minute intervals is susceptible to high-frequency random noise.
   - *Gap:* Inability to capture multi-scale temporal patterns (e.g., 30-min micro-patterns vs 24-hr macro-patterns) without **Multi-Scale Temporal Patching**.

5. **Lack of Probabilistic Coherence & Uncertainty Quantification (Gaps P-1 to P-5):**
   - Point forecasts provide no confidence intervals for grid operators or V2G scheduling.
   - *Gap P-1 (Monotonicity vs Tail Sharpness):* Monotonic quantile nets (PICNN) oversmooth extreme tail peak quantiles ($\alpha \ge 0.95$).
   - *Gap P-2 (Autoregressive vs Joint Trajectory Coherence):* DMS heads project independent marginal quantiles without capturing joint 24h path distribution $p(y_{1:H}|x)$.
   - *Gap P-3 (Conformal Recalibration under Shift):* Conformal Prediction (ACI) suffers adaptation lag during non-stationary tariff/weather transitions.
   - *Gap P-4 (Multimodal Diffusion Latency):* Generative Diffusion (DiffPLF) models multimodality but is too slow for sub-second real-time control.
   - *Gap P-5 (Non-linear Hierarchical Reconciliation):* Quantiles are non-additive ($q_\alpha(A+B) \neq q_\alpha(A) + q_\alpha(B)$), breaking spatial grid reconciliation.

### Corpus Coverage Update (2026-08-23 refresh, 103 papers)

The refreshed corpus ([[research_gaps]]) partially addresses several of the gaps above — none are fully closed:

- **Gap 1/2 (normalization & decomposition):** Now well-supported by [[2022_Kim_RevIN_Reversible_Instance_Normalization]], [[2024_Helmy_Autoformer_EV_Charging]], and the signal-decomposition line ([[2025_Zheng_BWO_ICEEMDAN_iTransformer]], [[2023_Cheng_VMD_Prophet_LSTM]] — note: Cheng 2023 is a *centralized* VMD+Prophet+LSTM hybrid, **not** federated learning despite legacy filenames). *New:* He JointPGM (2024) beats the RevIN line under distribution shift — normalization alone is not sufficient.
- **Gap 3 (peak underestimation / probabilistic coherence):** Partially addressed by PICNN convex quantile learning ([[2025_Zheng_Coherent_Hierarchical_EV_Load]], P-1/P-5), hierarchical conformal prediction for DERs ([[2024_Zhou_Conformal_Prediction_DER]], P-3), and diffusion-based multimodality ([[2024_Li_DiffPLF_Conditional_Diffusion_EV]], P-4). The monotonicity-vs-tail-sharpness trade-off and covariate-aware conformal recalibration remain open. *New:* [[2024_DeVilmarest_Adaptive_Probabilistic_Netload]] does online BOA quantile recalibration (net load, non-EV) — adjacent to P-3 but no covariate conditioning; [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] brings *static* CQR conformal calibration to EV load via TFT — P-3's adaptive-recalibration core stays open.
- **Gap 4 (multi-scale attention):** MFT ([[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]]) and MSSTGAN ([[2025_Tian_MSSTGAN_City_EV_Load]]) bring multi-scale fusion, but no controlled tokenization benchmark exists for EV load. This is now reinforced by [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]]: in a reproducible 4-city benchmark, **Transformers win only short-term horizons while GRU/LSTM win mid/long-term** — exactly the horizon-dependent behavior a controlled tokenization/multi-scale study must explain.
- **Gap 5 (spatial-temporal):** *New line:* EVformer ([[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]]) introduces decoupled temporal/spatial modules with dynamic Top-K spatial attention, and TriCast ([[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]]) models causal price elasticity explicitly — both point-forecast only, leaving spatial-temporal + calibrated uncertainty open (P-5).
- **Gap 6 (computational limits):** The post-Transformer line is now ingested: Mamba-3 ([[2026_Lahoti_Mamba_3_Sequence_Modeling]]), HyKANet ([[2026_Hao_Mamba_KAN_HyKANet_EV]]), PC-M3 ([[2026_Chen_PC_M3_Mamba_EV_Clusters]]), plus foundational Mamba papers (TimeMachine [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]], Bi-Mamba+ [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]]) and the foundation-model benchmark ([[2025_Meyer_Benchmark_Foundation_Models]]) / EV-STLLM ([[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]]). No EV paper combines these backbones with probabilistic heads — see Gap T-7 in [[research_gaps]]. *Caveat updated below.*
- **Low-data/transfer (Gap 3 primary):** Now crowded for standard stations: MixerInformer two-stage transfer for new stations ([[2025_Zhou_MixerInformer_Transfer_Learning_New_EV_Stations]]), MAML-Informer probabilistic few-shot ([[2026_Singh_MetaLearning_Informer_Probabilistic_EV]]), and the 12-city transferability benchmark ([[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] — linear SGD ≥ DL, performance plateaus after ~3 days of data). DC fast-charging + calibrated probabilistic low-data adaptation remains unexplored.

> [!IMPORTANT] Flagship novelty re-validation (papers 81–103)
> The nearest new competitors are: **USDT** ([[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]]) = probabilistic Transformer with Gaussian heads but Informer/Probformer backbone, no Mamba, no cross-attention exogenous fusion, no coverage guarantees; **MoghadamDost TFT+CQR** = Transformer + post-hoc static conformal calibration but LSTM-attention backbone, non-monotonic plain quantile head; **MAML-Informer** = probabilistic few-shot Informer but no conformal layer or convexity constraint. **No 2025–2026 paper combines a Mamba/SSM backbone with cross-attention exogenous fusion AND a conformalized PICNN head.** The full combination remains unexplored; component-level claims ("first probabilistic EV Transformer", "first conformalized EV Transformer", "first dynamic-graph EV Transformer") are no longer claimable.

6. **Computational & Inductive Bias Limits:**
   - Standard temporal attention on long lag sequences has $O(N^2)$ complexity and struggles with tabular lag features compared to GBDTs (XGBoost).
   - *Gap:* Opportunity to leverage **Inverted Transformer (iTransformer)** or **Mamba Selective SSM** ($O(N)$ linear scaling).

---

## 💡 Proposed Thesis Strategy & Action Plan

To fulfill the thesis goal of **overhauling the baseline Transformer to outperform Informer, Autoformer, TFT, and PTFT**:

1. **Architecture Redesign (Enhanced Baseline Transformer):**
   - **Input Module:** Integrate **RevIN** (Reversible Instance Normalization) + **Pearson/GRN Feature Selection Gate**.
   - **Encoder Core:** Combine **Series Decomposition** (Trend + Seasonality) with **Multi-Scale Temporal Patching**.
   - **Output Module:** Implement an **Asymmetric Peak-Weighted Loss Function** to minimize Peak Zone WAPE below 20%.
   - **Flagship novelty direction (re-verified 2026-08-23 against [[research_gaps]] Gaps 6, T-4, T-7 and P-1..P-5, all 103 papers):** a **Mamba backbone** ($O(N)$ selective SSM) + **cross-attention exogenous fusion** + **conformalized PICNN quantile head** — no paper in the 103-paper corpus combines these three components. Nearest neighbors (USDT, MoghadamDost TFT+CQR, MAML-Informer) each lack at least two of the three. Details in [[proposed_architectures]].

2. **Academic Verification:**
   - Evaluate the Enhanced Baseline against both the unified codebase benchmarks and official benchmark libraries (`NeuralForecast` / `PyTorch Forecasting`) for complete academic rigor.
