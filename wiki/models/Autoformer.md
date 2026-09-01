---
type: model
name: Autoformer
category: Deep Learning / Decomposition Transformer with Auto-Correlation
tags:
  - model
  - deep-learning
  - transformer
  - decomposition
  - long-term-forecasting
---

# 🔄 Autoformer

## Overview
Autoformer (Wu et al., NeurIPS 2021) is a decomposition architecture for long-term forecasting that embeds a **series decomposition block as an inner operator** — progressively decomposing intermediate hidden variables during forecasting rather than as preprocessing — combined with an **Auto-Correlation mechanism** replacing point-wise self-attention. Result: 38% average relative MSE improvement over previous SOTA across six benchmarks.

Key equations:
- Series decomposition (moving average): $X_t = \text{AvgPool}(\text{Padding}(X)), \qquad X_s = X - X_t$, summarized as $X_s, X_t = \text{SeriesDecomp}(X)$.
- Period-based dependency (autocorrelation confidence): $R_{XX}(\tau) = \lim_{L\to\infty}\frac{1}{L}\sum_{t=1}^{L} X_t X_{t-\tau}$.
- Auto-Correlation attention — top-$k$ period selection + softmax-normalized time-delay aggregation via circular Roll:
$$\text{Auto-Correlation}(Q,K,V) = \sum_{i=1}^{k} \text{Roll}(V, \tau_i)\ \hat{R}_{Q,K}(\tau_i), \quad k = \lfloor c \times \log L\rfloor$$
- FFT computation (Wiener–Khinchin) gives all lags at once → overall $O(L\log L)$ complexity: $R_{XX}(\tau) = F^{-1}\big(F(X_t)F^*(X_t)\big)$.
- Encoder keeps only seasonal components after each sublayer; decoder accumulates trend: $T_{de}^l = T_{de}^{l-1} + W^{l,1}*T_{de}^{l,1} + W^{l,2}*T_{de}^{l,2} + W^{l,3}*T_{de}^{l,3}$; final prediction $W_S * X_{de}^M + T_{de}^M$.

## Typical Usage in EV Load Forecasting
- **Input**: past window (length $I=96$ standard) of strongly periodic station-level/aggregated charging series.
- **Forecasting Horizon**: [[Long_Term_Forecasting]] ($O \in \{96,192,336,720\}$; EV studies use 30/60/90-day horizons).
- **Strengths**: discovers interpretable periods (24h/168h cycles); flat error growth across horizons; learned lags recover human-interpretable seasonality.
- **Weaknesses**: hyper-parameter $c$ trades performance vs efficiency; degrades on weak-periodicity data; high MAPE persists in sparse-feature EV settings.

## Literature Usage
- [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] — Original paper: progressive decomposition + FFT Auto-Correlation; 38% avg MSE reduction; input-96-predict-336 gains up to 74% (ETT) and 61% (Exchange).
- [[2024_Autoformer_EV_Charging]] — Applied to long-term EV charging-load forecasting on Boulder data (51 stations): RMSE ≈ 0.21 kWh/h flat across 30/60/90-day horizons vs LSTM degradation (90-day: 0.210 vs 0.540, ~60% lower RMSE/MAE).
- [[2023_NHiTS_Neural_Hierarchical_Interpolation]] — Autoformer baseline beaten by N-HiTS (ECL@96 MSE 0.147 vs 0.201) while being 45× faster (92.6 h vs 1.5 h training).
- [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — Baseline; applying channel-independence improves Autoformer too, but not enough to beat PatchTST.
- [[2023_TimesNet_Temporal_2D_Variation_Modeling]] — Auto-Correlation inspires TimesNet's amplitude-weighted aggregation; Autoformer-style decomposition does *not* help TimesNet since periodicity is already captured.
- [[2023_DLinear_Are_Transformers_Effective_LTSF]] — Autoformer's moving-average decomposition scheme reused inside DLinear; timestamp embeddings matter most for Autoformer among Transformers.
- [[2023_Crossformer_Cross_Dimension_Dependency]] — Baseline; Autoformer wins small ILI (decomposition priors help with limited data) but loses elsewhere.
- [[2024_TiDE_Long_Term_Forecasting]] — Benchmark protocol and baseline provider; sub-quadratic attention family far behind MLP encoders.
- [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Source of ECL/Traffic/Weather/Exchange benchmarks; component-adaptation baseline.
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Long-horizon baseline on ETT (avg MAE 0.53); TimesFM 0.36 significantly better.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
