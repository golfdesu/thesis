---
type: model
name: DeepAR
category: Deep Learning / Autoregressive Probabilistic RNN (Global Model)
tags:
  - model
  - deep-learning
  - rnn
  - probabilistic-forecasting
---

# 🎲 DeepAR

## Overview
DeepAR (Salinas et al., International Journal of Forecasting 2020) trains an **autoregressive multi-layer [[LSTM]]** as a **global model** across a large number of related time series, producing probabilistic forecasts via a chosen likelihood (Gaussian for real-valued data, **negative-binomial** for counts) instead of Gaussian-noise assumptions. ~15% accuracy improvement over SOTA probabilistic baselines.

Key equations:
- Autoregressive factorization with LSTM recurrence $h_{i,t} = h(h_{i,t-1}, z_{i,t-1}, x_{i,t}, \Theta)$:
$$Q_\Theta(z_{i,t_0:T} \mid \cdot) = \prod_{t=t_0}^{T} \ell\big(z_{i,t} \mid \theta(h_{i,t}, \Theta)\big)$$
- Gaussian likelihood with softplus positivity: $\mu(h_{i,t}) = w_\mu^\top h_{i,t} + b_\mu$, $\sigma(h_{i,t}) = \log(1 + \exp(w_\sigma^\top h_{i,t} + b_\sigma))$.
- Negative-binomial likelihood (mean $\mu$, shape $\alpha$, $\mathrm{Var}[z] = \mu + \mu^2\alpha$):
$$\ell_{NB}(z \mid \mu, \alpha) = \frac{\Gamma(z + \frac{1}{\alpha})}{\Gamma(z+1)\,\Gamma(\frac{1}{\alpha})}\left(\frac{1}{1+\alpha\mu}\right)^{\frac{1}{\alpha}} \left(\frac{\alpha\mu}{1+\alpha\mu}\right)^{z}$$
- Training by direct log-likelihood maximization $\mathcal{L} = \sum_i \sum_t \log \ell(z_{i,t}\mid\theta(h_{i,t}))$ with Adam; prediction by ancestral sampling (200 traces → consistent quantile estimates).

Special treatment of **power-law scale heterogeneity**: item-dependent rescaling ($\nu_i = 1 + \frac{1}{t_0}\sum z_{i,t}$) + velocity-weighted window sampling. Handles items with little/no history and missing observations naturally.

## Typical Usage in EV Load Forecasting
- **Input**: target history + covariates (age feature, time features, item embedding), all known over the horizon.
- **Forecasting Horizon**: [[Short_Term_Forecasting]] (encoder/decoder e.g. 168/24 hourly).
- **Strengths**: minimal feature engineering; calibrated marginal distributions; forecasts for cold-start series; Monte Carlo samples give all sub-range quantiles.
- **Weaknesses**: teacher-forcing exposure bias; heuristic scale factor; autoregressive decoding slow for long horizons; degrades on long-dependency synthetic tasks beyond ~96 steps.

## Literature Usage
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — Original paper: global autoregressive LSTM + flexible likelihoods; electricity ND 0.07 vs MatFact 0.16; count-data relative risk 0.77–0.94 vs ISSM/ETS baselines.
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — DeepAR as probabilistic baseline beaten by LogSparse Transformer (e.g., traffic-c 7d R0.5 0.179 vs 0.139); scale handling adopted.
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] — DeepAR baseline on ELECTRICITY/TRAFFIC/M4-Hourly (ND 0.07/0.17/0.09) beaten by covariate-free N-BEATS.
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — Key benchmark: TFT cuts P50 loss 36% on Electricity, 69% on Traffic, 62% on Retail vs DeepAR.
- [[2021_Rasul_TimeGrad_Diffusion_Forecasting]] — DeepAR's mean-scaling trick and lag-feature pipeline inherited by TimeGrad; GP-copula/Vec-LSTM baselines from the same lineage.
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — Univariate baseline on ETT/Exchange benchmarks.
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — Univariate baseline; DeepAR better only on ECL short horizons (≤336); Informer beats it by 49–65% MSE at longer horizons.
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] — Probabilistic baseline (ETTm2@720 MSE 0.332 vs N-HiTS 0.157).
- [[2023_Huang_MetaProbformer_EV_Load]] — Probabilistic baseline for EV charging-load forecasting beaten by MetaProbformer on RMSE/Q50/Q90/CRPS.
- [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] — Benchmark for low-data probabilistic EV demand (FEDM qualified rate 99.22% vs DeepTCN-family comparisons).
- [[2024_Das_TiDE_Long_Term_Forecasting]] — M5 comparison baseline (WRMSSE 0.789 ≈20% worse than TiDE with covariates).
- [[2025_Zheng_Coherent_Hierarchical_EV_Load]] — Hierarchical reconciliation benchmark: total MAE 2.15 (PICNN) vs DeepAR 9.67 on coherent EV load forecasting.
- 2026 — [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] — DeepAR weakest baseline in USDT study (EVnetNL RMSE 29.675 / MAE 25.822; Perth RMSE 24.170), far behind even vanilla Transformer and Informer.
