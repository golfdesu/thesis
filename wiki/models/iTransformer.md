---
type: model
name: iTransformer
category: Deep Learning / Inverted Transformer (Variate-Token Attention)
tags:
  - model
  - deep-learning
  - transformer
  - multivariate-forecasting
  - long-term-forecasting
---

# 🔃 iTransformer

## Overview
iTransformer (Liu et al., ICLR 2024 Spotlight) diagnoses why Transformer forecasters lose to linear models: embedding multiple variates of the *same timestamp* into one temporal token fuses distinct physical measurements, yields meaningless attention maps, and applies permutation-invariant attention to an order-sensitive dimension. The fix simply **inverts** component duties without modifying them:

- Each variate's whole lookback series becomes one **variate token** ($h_n^0 = \text{Embedding}(X_{:,n})$).
- **Self-attention operates across variates** to capture multivariate correlations; pre-Softmax scores form an interpretable correlation map $A_{i,j} = (QK^\top/\sqrt{d_k})_{i,j} \propto q_i^\top k_j$.
- **FFN operates along time** to learn per-variate series representations; LayerNorm is applied per-variate-token over its series dimension (related to [[RevIN]]), diminishing inconsistent-measurement discrepancies.
- No positional embedding needed — order lives implicitly in FFN neuron permutation.

$$h_n^0 = \text{Embedding}(X_{:,n}), \quad H^{l+1} = \text{TrmBlock}(H^l),\ l=0,\dots,L-1, \quad \hat{Y}_{:,n} = \text{Projection}(h_n^L)$$

Inversion consistently improves Transformer variants: −38.9% avg MSE on vanilla Transformer, −36.1% Reformer, −28.5% Informer, −32.2% Flashformer. Efficient training via random variate sampling.

## Typical Usage in EV Load Forecasting
- **Input**: raw multivariate series only (no exogenous features); fixed lookback T=96.
- **Forecasting Horizon**: [[Long_Term_Forecasting]] ($S \in \{96,...,720\}$).
- **Strengths**: comprehensive SOTA (best ECL avg MSE 0.178, Traffic 0.428, Solar 0.233); generalizes to unseen variates (+0.034 MSE when trained on 20% of ECL variates) — useful for new/evolving EV stations; memory-efficient vs PatchTST/Crossformer.
- **Weaknesses**: $O(N^2)$ in number of variates for high-dimensional datasets; degrades into a stackable linear forecaster in univariate scenarios; point forecasts only (no uncertainty).

## Literature Usage
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Original paper: variate-token inversion; beats PatchTST/TimesNet/DLinear on most benchmarks; ablation shows attention-on-variate + FFN-on-temporal is optimal.
- [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] — EV/power load application: BWO–ICEEMDAN–iTransformer pipeline forecasts IMF subsequences + exogenous factors; R² 0.9873 / MAE 48.0 vs plain iTransformer R² 0.9577 / MAE 83.3 (+3.09% improvement).
- [[2025_Bao_ResMMoT_Informer_Time_Series]] — iTransformer baseline on NASDAQ100 beaten by ResMMoT-Informer; less stable under noise/volatility.
- [[2025_Li_Multi_View_Graph_Intrusion_Detection_EV]] — Related cross-feature dependency modeling line for EV charging-station security.
- [[2025_Meyer_Benchmark_Foundation_Models]] — Trained-from-scratch baseline for household STLF; outperformed by zero-shot foundation models on several datasets (MAE_h 0.588–0.648).
- 2026 — [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] — Degenerate load-only (near-identity with a single variate; 1/30 MAPE wins, 6.14% avg) yet the **largest weather gain** of all architectures: −1.62 pp avg ΔMAPE, ~3× more efficient than PatchTST at converting covariate tokens into accuracy; parameter-controlled tiers prove the gap is architectural.
