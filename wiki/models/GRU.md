---
type: model
name: Gated Recurrent Unit (GRU)
category: Deep Learning / Recurrent Neural Network
tags:
  - model
  - deep-learning
  - rnn
  - gru
---

# 🧠 Gated Recurrent Unit (GRU)

## Overview
GRU, introduced by Cho et al. (2014), is a computationally efficient variant of LSTM. It combines the input gate and forget gate into a single **update gate ($\Gamma_u$)** and replaces the output gate with a **reset gate ($\Gamma_r$)**.

## Key Mathematical Equations
- **Reset Gate**: $\Gamma_r = \sigma(W_r [S_{t-1}, x_t] + b_r)$
- **Update Gate**: $\Gamma_u = \sigma(W_u [S_{t-1}, x_t] + b_u)$
- **Candidate Hidden State**: $\tilde{S}_t = \tanh(W_s [\Gamma_r * S_{t-1}, x_t] + b_s)$
- **Hidden State Update**: $S_t = (1 - \Gamma_u) * S_{t-1} + \Gamma_u * \tilde{S}_t$

## Performance in EV Charging Load Forecasting
- **Faster Training & Fewer Parameters**: Requires less memory and fewer matrix multiplications than LSTM.
- **Hourly Forecasting Superiority**: Outperformed LSTM and DNN in 1-hour ahead station load forecasting (Test-NRMSE = 2.89% in [[2019_ApplSci_EV_Load_Forecasting]]).

## Literature References
- [[2019_ApplSci_EV_Load_Forecasting]] - Demonstrated 1-layer GRU achieved top performance for hourly EV station load forecasting.
- [[2019_EV_Load_Forecasting]] - Compared GRU vs LSTM across minute-level time steps.
- [[2018_Empirical_TCN_Sequence_Modeling]] - Empirical evaluation showing generic TCNs beat GRU on most sequence benchmarks (Seq. MNIST accuracy 99.0 vs 96.2; Copy Memory loss 3.5e-5 vs 0.0197).
- [[2022_GCN_TRN_EV_Availability]] - GCN-GRU hybrid improved availability-prediction accuracy over standalone GRU (+2.1%/+6.1%/+10.6% at 30/60/90-min horizons), though GCN-TRN was best overall.
- [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] - GRU benchmarked as recurrent baseline for Beijing fast-charging station load; multi-graph STMGCN reduced MAE ~2–20 kW below all baselines incl. GRU.
- [[2025_Transformer_BiLSTM_Price_Forecasting]] - GRU baseline in Transformer-BiLSTM day-ahead price forecasting on NYISO (MAE $3.53/MWh vs proposed $2.78).
- [[2026_MFT_Multi_Scale_Fusion_Transformer]] - GRU weakest recurrent baseline for multi-scale EV charging-station load prediction; MFT achieved 26.54% average improvement over GRU (largest among competitors).
- [[2026_CNN_LSTM_Attention_Fast_Charging]] - GRU was the strongest single baseline for 1-h fast-charging load forecasting; CNN-LSTM-Attention cut MAE 17.45% and inference latency to 0.742 ms vs GRU's 2.319 ms.
- 2026 — [[2026_TFT_Conformal_Environmental_EV_Load]] — GRU baseline weakest recurrent model at 1-h-ahead Palo Alto forecasting (RMSE 7.307 kWh vs TFT 1.2687, >78% cut).
- 2026 — [[2026_ML_Geographical_Transferability_EV]] — Bi-GRU variant (2×64 units) among six benchmark models across 12 cities; beats MLP/LASSO on MAE and transfers well, though SGD stays best overall.
- 2026 — [[2026_ML_Comparison_EV_Charging_Forecasting]] — GRU consistently wins mid-term (2–8 h) in Dundee/Perth at all horizons/levels (Perth city MAE 8.17→6.54) and long-term (GRU best Dundee city MAE 21.48@5d where Transformer collapses to ≈93), thanks to its stronger local-temporal-continuity inductive bias on sparse data.
- 2024 — [[2024_TOU_Price_Meteorology_EV_Charging_Load]] — Two-layer GRU as temporal backend of CNN-GRU beats standalone GRU/BP/LSTM at every 4–168 h horizon on mall-station load (168 h RMSE 71.50 vs GRU 77.09); GRU preferred over LSTM for its cheaper two-gate computation.
