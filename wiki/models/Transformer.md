---
type: model
name: Transformer
category: Deep Learning / Self-Attention Mechanism
tags:
  - model
  - deep-learning
  - transformer
  - attention
---

# 🧠 Transformer Architecture

## Overview
The Transformer architecture, introduced by Vaswani et al. (2017) in [[2017_Attention_Is_All_You_Need]], replaces recurrent networks with self-attention mechanisms. It enables parallel sequence processing and effectively captures long-range temporal dependencies.

## Key Mathematical Equations
- **Scaled Dot-Product Attention**:
  $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- **Multi-Head Attention**:
  $$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$

## Usage in EV Charging Load Forecasting
- Used for long-term and multi-horizon time-series forecasting.
- Forms the backbone for hybrid models like Transformer-LSTM, Temporal Fusion Transformer (TFT), and Spatial-Temporal Transformers.

## Key Literature References
- [[2017_Attention_Is_All_You_Need]] - Original Transformer paper by Vaswani et al.

## 📚 Literature Usage
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on fm-impute-bench and fev-bench zero-shot benchmarks for forecasting and missing-value imputation.
- 2019 — [[2019_LogSparse_Enhancing_Locality_Transformer]] : LogSparse convolutional self-attention fixes the Transformer's memory bottleneck — electricity-c 1-day R0.5 quantile loss 0.059 vs DeepAR 0.075, best of all baselines.
- 2021 — [[2021_CSDI_Conditional_Diffusion_Forecasting]] : CSDI builds conditional diffusion forecasting on a Transformer with 2D temporal/feature attention — CRPS-sum electricity 0.017 vs TimeGrad 0.021, traffic 0.020 vs 0.044.
- 2022 — [[2022_GCN_TRN_EV_Availability]] : GCN-augmented Transformer (GCN-TRN) lifts 30-min station availability accuracy to 0.8312 vs vanilla Transformer 0.7236 (+14.3%) on Dundee data.
- 2023 — [[2023_MetaProbformer_EV_Load]] : baseline ordering MetaProbformer < MetaTransformer < Informer < LSTM < Transformer; 8.479% MAE gain over MetaTransformer on heterogeneous Palo Alto task.
- 2023 — [[2023_Transformer_EV_Demand]] : pure Transformer applied to Boulder EV charging demand — best at K=30/60/90 steps ahead (K=90 RMSE 0.085 vs LSTM 0.522, ARIMA 0.920).
- 2023 — [[2023_Multi_Branch_ResTrans_Solar]] : swapping LSTM for a Transformer encoder in ResTrans lowers RMSE 14.04% (multi-branch); final model reaches R² = 97% on NSRDB solar irradiance.
- 2024 — [[2024_Feature_Enhanced_Probabilistic_EV_Load]] : transformer-family TFT used as benchmark — FEDM attains QR 99.22%/WS −0.4323 vs TFT WS −0.6951 for Shenzhen day-ahead probabilistic forecasting.
- 2024 — [[2024_LSTM_Transformer_EV_Consumption]] : LSTM-Transformer framework predicts per-trip EV energy consumption at MAPE 4.63% (400 s windows) vs standalone LSTM 10.69%.
- 2024 — [[2024_Divide_Conquer_Transformer_EV]] : divide-and-conquer Transformer (DCT-EV) detects charging events 1–10 min ahead with F1@.5 87.35%, AUC 97.90%, beating LSTM/DNN/XGBoost.
- 2024 — [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] : inverting dimensions (attention over variates, FFN over time) cuts vanilla Transformer MSE by 35.6–86.1%; iTransformer avg ECL MSE 0.178/MAE 0.270.
- 2025 — [[2025_REST_Network_Port_EV]] : Transformer block embedded in the REST ensemble port-EV forecaster — overall MAPE 6.5%, RMSE 9.8 kW, 99% relative efficiency, 33 ms inference.
- 2025 — [[2025_CAT_Former_Short_Term_EV]] : context-aware Temporal Transformer (CAT-Former) reduces 1-h-ahead MSE up to 11.82% vs Hybrid Transformer (Park 1: 0.4610 vs 0.5155).
- 2025 — [[2025_Hybrid_LSTM_Transformer_Demand]] : hybrid LSTM-Transformer cuts 30-day-ahead Caltech MAE to 32.416 vs standalone Transformer 39.183 (−17.27%).
- 2025 — [[2025_Transformer_BiLSTM_Price_Forecasting]] : Transformer-BiLSTM hybrid gains −16.98% MAE vs standalone Transformer on NYISO day-ahead prices ($2.7818 vs $3.3511 per MWh).
- 2025 — [[2026_Hybrid_XGBoost_BiLSTM_EV_Load]] : standalone Transformer underperforms badly (test MAE 4.8141 kWh, R² −0.007 vs XGBoost 2.6697), motivating boosting-based hybrids.
- 2026 — [[2026_Mamba_3_Sequence_Modeling]] : Mamba-3 language-modeling benchmark — 1.5B MIMO downstream accuracy 57.6 vs Transformer 55.4; validation ppl 10.24 vs 10.51.
- 2026 — [[2026_MFT_Multi_Scale_Fusion_Transformer]] : Multi-scale Fusion Transformer averages a 10.79% metric gain over vanilla Transformer; at K=96 h MSE 1.89 vs 2.51 (−35.78%).
- 2026 — [[2026_CNN_LSTM_Attention_Fast_Charging]] : vanilla Transformer collapses at long horizons (48-h R² 0.39); CNN-LSTM-Attention cuts 1-h-ahead MAE 17.45% and RMSE 13.83% vs GRU.
- 2026 — [[2026_TFT_Conformal_Environmental_EV_Load]] : vanilla Transformer far behind TFT with weather covariates on Palo Alto daily load (normalized MSE 0.02008 vs 0.001764; MAPE 19.03% vs 1.20%).
- 2026 — [[2026_MetaLearning_Informer_Probabilistic_EV]] : Transformer point/probabilistic baseline beaten by MAML-Informer across ACN/Boulder/Palo Alto (e.g., Boulder RMSE 8.672 vs 7.095).
- 2026 — [[2026_DualDirection_Transformer_EV_Charging]] : vanilla Transformer baseline cut by USDT (EVnetNL RMSE 12.264 vs 8.781; Perth RMSE 23.967 vs 13.837).
- 2026 — [[2026_EVformer_Spatio_Temporal_Decoupled_Citywide]] : decoupled spatio-temporal Transformer (channel-first global-aggregation temporal attention + semantic Top-K spatial attention) best on ALL MAE/RMSE/MAPE at 15/30/45 min on Shenzhen ST-EVCDP (RMSE 3.06/4.98/6.45 ×10⁻² vs best baseline PAG).
- 2026 — [[2026_ML_Comparison_EV_Charging_Forecasting]] : Transformers dominate short-term regional/city forecasts across Palo Alto/Boulder/Dundee/Perth (MAE 10–15% below ARIMA/XGBoost) and long-term Boulder (city MAE 2.63@5d), but collapse on sparse daily Dundee data (city MAE ≈ 93 vs GRU ≈ 21–24).

## Literature Usage
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Vanilla Transformer baseline on Monash (GM 0.9384) and ETT; TimesFM significantly outperforms (0.6846 / 0.36 avg MAE).
- [[2026_Toto_2_Scaling_Era]] — Toto 2.0 is a decoder-only patched Transformer with alternating time/variate attention (Toto 1.0 backbone); CPM + quantile head + NorMuon + u-muP scaling recipe.
- [[2025_Chronos_2_Univariate_to_Universal]] — **Transformer** heritage: Chronos-2 is encoder-only T5 (Raffel et al. 2020) with RoPE (Su et al. 2024); alternates time attention (temporal) and group attention (cross-series at same patch).

- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
