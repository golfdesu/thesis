---
title: Pinball Loss (Quantile Loss)
type: metric
metric: Pinball Loss (Quantile Loss)
category: probabilistic-forecast-metric
formula: "L_τ(y, ŷ) = τ·max(0, y−ŷ) + (1−τ)·max(0, ŷ−y)"
unit: Same as target variable (per quantile level τ)
last_updated: 2026-08-23
tags: [metric, pinball-loss, quantile-loss, probabilistic-forecast]
---

# 📐 Pinball Loss (Quantile Loss)

## Definition

The **pinball loss** scores a single quantile forecast $\hat{y}_\tau$ at level $\tau \in (0,1)$ against the observation $y$:

$$L_\tau(y, \hat{y}_\tau) = \begin{cases} \tau (y - \hat{y}_\tau), & y \geq \hat{y}_\tau \\ (1-\tau)(\hat{y}_\tau - y), & y < \hat{y}_\tau \end{cases}$$

It is asymmetric: under-prediction of a high quantile is penalized more heavily than over-prediction. Minimizing the summed pinball loss over a grid of τ trains direct multi-quantile models ([[Quantile_Regression]], MQ-RNN, MQ-TCN) and doubles as their evaluation metric. Integrating pinball loss over all τ recovers [[CRPS]].

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Same as target variable |
| **Lower is better** | ✅ Yes |
| **Per-level interpretability** | ✅ Reveals asymmetry (skewed demand makes high τ harder) |
| **Dual use** | ✅ Training objective *and* evaluation metric |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2017 — [[2017_QRA_Sister_Forecasts_Probabilistic_Load]] | QRA combination selected by pinball score (best config QRA(8), 183-day calibration) — dominated all sister benchmarks on pinball and [[Winkler_Score]]. |
| 2019 — [[2019_Deep_Probabilistic_Scheduling_Power_Markets]] | Non-parametric BLSTM trained by minimizing total pinball loss over quantile set $Q$; compared against parametric Gaussian likelihood training. |
| 2021 — [[2021_Probabilistic_Queuing_EV_Load]] | WT-CNN achieved lowest pinball loss among all methods at PINC 90/95/99% vs quantile regression benchmark. |
| 2022 — [[2022_Robust_Deep_Gaussian_Process_Load]] | Improved quantile/pinball objective used to train probabilistic DGP load forecasts. |
| 2024 — [[2024_MQ_TCN_Transfer_Learning_EV]] | Pinball loss is the MQ-TCN training objective (JPL Pinball 2.28, NREL 1.86); paired with [[PICP]]/[[Winkler_Score]] evaluation. |
| 2024 — [[2024_Feature_Enhanced_Probabilistic_EV_Load]] | Enhanced pinball loss (Eqs. 28–29) with feature-reweighted FEDM network. |
| 2025 — [[2025_QR_LSTM_Attention_EV_Load]] | Minimized separately per quantile q20/q50/q80: best model cut pinball by 81.39%/62.09%/68.04% vs persistence. |
| 2026 — [[2026_TFT_Conformal_Environmental_EV_Load]] | TFT quantile head {0.1, 0.5, 0.9} trained with summed pinball loss (Eqs. 3–4) over Palo Alto hourly/daily horizons; P50 as point forecast, [P10, P90] as band. |
| 2026 — [[2026_MetaLearning_Informer_Probabilistic_EV]] | Pinball-derived Q50/Q90 outputs used to verify Gaussian-head calibration; MAML-Informer cuts RMSE50 up to 51.21%. |
| 2024 — [[2024_Adaptive_Probabilistic_Netload]] | Quantile regressions adapted online by OGD directly on the pinball loss with step size auto-selected via Bernstein Online Aggregation; adaptive QR cuts US-city RPS >20% during COVID and beats the best single expert on GB net-load. |
| Quantile-loss variants (same family) | [[2019_LogSparse_Enhancing_Locality_Transformer]], [[2020_DeepAR_Probabilistic_Forecasting]], [[2021_TFT_Temporal_Fusion_Transformers]] (P50/P90), [[2023_MetaProbformer_EV_Load]], [[2025_DC_Charging_Profiles_TFT]], [[2025_Coherent_Hierarchical_EV_Load]] (MLP baseline trained on summed pinball over α ∈ {0.05,…,0.95}). |

## Literature Usage
- [[2025_Chronos_2_Univariate_to_Universal]] — **Pinball/quantile loss** Eq.4 sum_q q*max(z-zq,0)+(1-q)*max(zq-z,0) over 21 quantiles (extension of standard 9-level); trained multi-patch direct, 21 levels include 0.01/0.99 extremes.

## Related Pages

- [[CRPS]]
- [[Winkler_Score]]
- [[PICP]]
- [[2026_Toto_2_Scaling_Era]] — Training loss: rho_tau=(y-qhat)(tau-1[y<qhat]) (Eq.2), L_quantile=1/|T| sum rho_tau (Eq.3), T={0.1..0.9}; sign-valued gradient Eq.4 motivates NorMuon; quantiles sorted at inference.
