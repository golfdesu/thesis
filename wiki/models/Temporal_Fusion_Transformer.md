---
type: model
name: Temporal Fusion Transformer (TFT)
category: Deep Learning / Interpretable Multi-Horizon Attention Architecture
tags:
  - model
  - deep-learning
  - transformer
  - probabilistic-forecasting
  - interpretability
---

# 🎛️ Temporal Fusion Transformer (TFT)

## Overview
TFT (Lim et al., International Journal of Forecasting 2021) is an attention-based architecture for **multi-horizon forecasting** that natively handles heterogeneous inputs — [[Static_Covariates]], [[Past_Observed_Inputs]], and [[Known_Future_Inputs]]. Quantile forecast form:
$$\hat{y}_i(q,t,\tau) = f_q(\tau,\; y_{i,t-k:t},\; z_{i,t-k:t},\; x_{i,t-k:t+\tau},\; s_i)$$

Five architectural novelties: (1) gating for adaptive depth, (2) instance-wise variable selection, (3) static covariate encoders, (4) LSTM seq2seq local processing + interpretable multi-head self-attention decoder, (5) quantile outputs.

Key components:
- **Gated Residual Network (GRN)** with GLU suppression: $\text{GRN}_{\omega}(a,c) = \text{LayerNorm}(a + \text{GLU}_{\omega}(W_1 \text{ELU}(W_2a + W_3c + b_2) + b_1))$
- **Variable Selection Network**: $v_{\chi_t} = \text{Softmax}(\text{GRN}_{v_\chi}(\Xi_t, c_s))$, $\tilde{\xi}_t = \sum_j v_{\chi_t}^{(j)} \tilde{\xi}_t^{(j)}$
- **Interpretable multi-head attention** (shared values across heads): $\tilde{H} = \frac{1}{H}\sum_{h=1}^{m_H} \text{Attention}(QW_Q^{(h)}, KW_K^{(h)}, VW_V)$
- **Quantile outputs** trained with joint pinball loss over $Q=\{0.1,0.5,0.9\}$; normalized q-Risk metric.

Interpretability use cases demonstrated: global variable importance, persistent temporal patterns (attention reveals daily/weekly seasonality), regime/event detection (2008 financial crisis via Bhattacharyya-based attention distance $\text{dist}(t)$).

## Typical Usage in EV Load Forecasting
- **Input**: target + calendar features + entity IDs; static covariates condition selection/enrichment.
- **Forecasting Horizon**: [[Multi_Horizon]] (e.g., 24 h ahead with 168 h look-back).
- **Strengths**: beats all benchmarks on every dataset by 3–26% (avg 7% lower P50 / 9% lower P90); built-in interpretability of variable importance and attention patterns.
- **Weaknesses**: single attention layer, quadratic cost limits long look-backs; quantiles not calibrated probabilistically; fixed quantile set {0.1,0.5,0.9}; no joint multivariate sampling.

## Literature Usage
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — Original paper: GRN/VSN/static encoders/interpretable attention; Electricity P50/P90 0.055/0.027 vs DeepAR 0.075/0.040 (+36%/+48%); all ablations confirm each component contributes.
- [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] — FEDM borrows TFT's GRN/GLU building blocks for probabilistic EV demand; TFT benchmark qualified rate 94.79% (summer) vs FEDM 99.22%.
- [[2025_Li_DC_Charging_Profiles_TFT]] — TFT-style architecture (VSNs + GRNs + LSTM encoder-decoder + multi-head attention, ~9.8M params) predicts real-world DC fast-charging profiles/durations; beats RNN/GRU/LSTM/vanilla Transformer baselines.
- [[2025_Meyer_Benchmark_Foundation_Models]] — Trained-from-scratch baseline for household STLF (MAE_h 0.577–0.635), outperformed on several datasets by zero-shot foundation models.
- [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] — TFT cited as hyperparameter-range justification for fast-charging forecasting architectures.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : End-to-end TFT + quantile head + CQR conformal calibration with environmental covariates on Palo Alto hourly data — RMSE 1.2687 kWh (1–24 h) and post-conformal PICP 96.2% at 80% nominal; VSN attention reveals monthly billing cycles.
