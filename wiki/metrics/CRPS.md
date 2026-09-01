---
title: Continuous Ranked Probability Score (CRPS)
type: metric
metric: Continuous Ranked Probability Score (CRPS)
category: probabilistic-forecast-metric
formula: "CRPS(F, y) = ∫ (F(z) − 1{z ≥ y})² dz"
unit: Same as target variable (kW or kWh)
last_updated: 2026-08-23
tags: [metric, crps, probabilistic-forecast, distributional]
---

# 📐 Continuous Ranked Probability Score (CRPS)

## Definition

**CRPS** compares the full predictive CDF $\hat{F}$ against the observed outcome $y$ — it is the distributional generalization of [[MAE]]:

$$\text{CRPS}(\hat{F}, y) = \int_{-\infty}^{\infty} \left( \hat{F}(z) - \mathbb{1}\{z \geq y\} \right)^2 dz = E|\hat{X} - y| - \tfrac{1}{2}E|\hat{X} - \hat{X}'|$$

Lower is better; a perfect deterministic forecast gives CRPS = 0. For quantile-based forecasts it can be approximated as the integral of pinball losses across all quantile levels.

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Same as target variable |
| **Lower is better** | ✅ Yes |
| **Rewards sharpness + calibration jointly** | ✅ Yes — single number summarizing both |
| **Requires full predictive distribution** | ✅ Yes (samples or quantiles) |
| **Aggregated variant** | **CRPS-sum**: applied to the sum over all series/horizons to penalize joint miscalibration |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2021 — [[2021_TimeGrad_Diffusion_Forecasting]] | Diffusion-based TimeGrad achieved new SOTA CRPSsum on most datasets (~21% lower than Transformer-MAF on Traffic/Wikipedia). |
| 2021 — [[2021_CSDI_Conditional_Diffusion_Forecasting]] | CSDI improved CRPS 40–65% over probabilistic imputation baselines; best CRPS-sum on Electricity (0.017 vs TimeGrad 0.021). |
| 2023 — [[2023_DiffSTG_Probabilistic_ST_Graph_Diffusion]] | DiffSTG (masked DDPM on spatio-temporal graphs) cuts CRPS **−5.6% / −4.3% / −14.3%** vs most competitive baseline on AIR-BJ/AIR-GZ/PEMS08 (CRPS 0.34/0.22/0.06), beating TimeGrad (0.36/0.25/0.09) and CSDI (0.50/0.28/0.11); non-autoregressive sampling is ~40× faster than TimeGrad. |
| 2023 — [[2023_MetaProbformer_EV_Load]] | Reptile-meta Probformer beat DeepAR/FPSeq2Q/Probformer on CRPS for short-term probabilistic EV forecasting. |
| 2024 — [[2024_DiffPLF_Conditional_Diffusion_EV]] | DiffPLF improved CRPS by **49.87%** over conventional quantile regression on Palo Alto EV data. |
| 2025 — [[2025_QR_LSTM_Attention_EV_Load]] | QR-LSTM-Attention cut CRPS by **67.70%** vs persistence benchmark (Utrecht office parking lot); CRPS computed from empirical CDF via Eq. above. |
| 2026 — [[2026_MetaLearning_Informer_Probabilistic_EV]] | MAML-Informer cuts CRPS up to **~48%** vs baselines (CRPS 1.140/1.001/1.012 on ACN/Boulder/Palo Alto); Gaussian-head calibration verified with quantile metrics. |
| 2026 — [[2026_DualDirection_Transformer_EV_Charging]] | CRPS improvements reported qualitatively for USDT alongside near-uniform PIT histograms and ACE 0.0659 reliability diagrams. |

> [!TIP]
> When only a few quantiles are available, prefer reporting [[Pinball_Loss]] per level plus [[PICP]]; CRPS is the preferred headline metric when samples or a dense quantile grid are available.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated on GIFT-Eval and fev-bench.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Probabilistic evaluation metric on fm-impute-bench and fev-bench.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Continuous ranked probability score metric on GIFT-Eval (FlowState achieves Rank 1 CRPS 0.442).
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Primary probabilistic evaluation metric approximated via mean weighted quantile loss over 9 quantiles (GiftEval-ZS CRPS 0.411).
- [[2025_Chronos_2_Univariate_to_Universal]] — CRPS-adjacent probabilistic evaluation underlies SQL/WQL quantile losses (Eq.4, 21 quantiles 0.01-0.99); Chronos-2 21-quantile head improves tail coverage vs 9-level baselines.

## Related Pages

- [[MAE]]
- [[Pinball_Loss]]
- [[PICP]]
- [[Winkler_Score]]
- [[2026_Toto_2_Scaling_Era]] — Primary metric on BOOM/GIFT-Eval/TIME: Toto 2.5B CRPS 0.349 (BOOM), 0.476 (GIFT-Eval FM-only), 0.532 (TIME); CRPS ranks 3.88 (BOOM), 20.3 (GIFT), 3.43 (TIME); FnF ensemble 0.463. Quantile head (9 levels, pinball Eq.2-3) → CRPS via integration.

- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- [[2026_Moirai_2_When_Less_Is_More]] — GIFT-Eval normalized MASE/CRPS (geometric mean / seasonal naive, 97 tasks); WQL via 9 quantiles (0.1-0.9). Small: MASE 0.728 / CRPS 0.516 (Table 1); ranks 5th/6th among 37 FMs (Fig. 2); base/large underperform small on same corpus.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — Evaluated zero-shot out-of-distribution across 6 datasets (Electricity, Solar, Walmart, Weather, Istanbul Traffic, Turkey Power) and 9 Monash benchmarks using continuous/discrete quantile approximations.
