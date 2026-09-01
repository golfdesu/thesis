---
type: model
name: "TimesFM"
category: Deep Learning / Decoder-Only Patched Foundation Model (Google)
tags:
  - model
  - deep-learning
  - foundation-model
  - decoder-only
  - zero-shot
  - long-term-forecasting
---

# ⏱️ TimesFM (Time-Series Foundation Model)

## Overview
TimesFM (Das et al., Google Research, arXiv:2310.10688v4, April 2024) is the first practical **decoder-only** patched Transformer foundation model for time-series forecasting — the time-series analogue of LLMs. A single pretrained model does **zero-shot** forecasting on unseen datasets across domains, horizons (tens to 512 steps) and granularities (10-min to yearly) with accuracy close to per-dataset supervised SOTA, despite being 1-2 orders of magnitude smaller than LLMs (17M / 70M / 200M params; ~100B pretraining time-points).

Core architecture (Fig. 1):

- **Input patching** — contiguous patches of length \(p=32\) are tokens (cf. [[PatchTST]]); MLP Residual Block \(t_j = \mathrm{InputResidualBlock}(\tilde{y}_j \odot (1-\tilde{m}_j)) + PE_j\) (Eq. 2).
- **Stacked causal Transformer** — \(n_l\) layers, \(o_j = \mathrm{StackedTransformer}((t_1,\dot{m}_1),\dots,(t_j,\dot{m}_j))\) with causal multi-head SA + FFN (Eq. 3); hidden dim = model_dim (1280 for 200M, 16 heads, 20 layers).
- **Longer output patches** — \(\hat{y}_{pj+1:pj+h} = \mathrm{OutputResidualBlock}(o_j)\) with \(h=128 > p\) (Eq. 4) — middle ground between 1-token AR (slow) and one-shot full-horizon (inflexible); 256→256 needs only 2 AR steps.
- **Patch masking** — random fractional masking \(r \sim U[0,p-1]\) of first patch per batch covers all context lengths \(1\dots\max\!\_len\) (512; 256 weekly, 64 monthly).
- **Loss** — \(\mathrm{TrainLoss} = \frac{1}{N}\sum_j \mathrm{MSE}(\hat{y}_{pj+1:pj+h}, y_{pj+1:pj+h})\) (Eq. 5); probabilistic extension via quantile heads / NLL noted but not evaluated.

Pretraining corpus (~100B points, Table 1): **Google Trends** (~0.5B, 22k queries, hourly/daily/weekly/monthly), **Wiki Pageviews** (~360B raw → mixed), **3M synthetic series** (6.1B, ARMA + seasonal + trend + step, length 2048), plus M4 / Electricity / Traffic / Weather / Favorita / LibCity; mixture 80% real / 20% synthetic with equal granularity-group weights; RevIN-standard normalization (mean/std of first patch); cosine-decay LR (peak 5e-4), 1.5M steps, batch 4096 on 16× TPUv5e (~2 days for 200M).

## Typical Usage in EV Load Forecasting
- **Input**: univariate past window \(y_{1:L}\) only — no covariates at pretraining (date features discussed as Eq. 8 future work).
- **Forecasting Horizon**: [[Long_Term_Forecasting]] and zero-shot [[Short_Term_Forecasting]] / [[Day_Ahead_Forecasting]] alike (horizons 32–512 demonstrated).
- **Strengths**: single model, no per-dataset training; monotonic scaling with FLOPs (17M→70M→200M); longer output patches reduce AR error accumulation; synthetic data crucial for rare granularities (yearly/quarterly/10-min).
- **Weaknesses**: univariate-only (no arrival/departure, SoC, tariff, weather fusion); point forecasts only (no CRPS/PICP); public-data contamination not audited; less interpretable than statistical baselines; monthly/weekly contexts shortened.

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Origin paper. Monash (18 datasets) GM scaled MAE **0.6846** (best; >25% better than LLMTime/GPT-3, within significance of N-BEATS); Darts (8 series) competitive with tuned ARIMA; ETT (8 tasks, last-window) avg MAE **0.36** vs PatchTST 0.37, LLMTime 0.45, FEDFormer/Autoformer 0.53, Informer 0.99; finetuning on 10% ETT (only I/O residual blocks) beats GPT4TS by 12–18% and matches full-data supervised baselines; ablations confirm scaling law, h=128 optimum, p=32 optimum, synthetic data necessity.
- [[2025_Meyer_Benchmark_Foundation_Models]] — Independent benchmark includes TimesFM / TimesFM 2.0 among 6 zero-shot TSFMs vs 4 TFS Transformers on 4 household STLF datasets: TimesFM competitive on IDEAL / Lower Saxony / REFIT / S. Germany (MAE_h 0.478–0.530), Chronos-Bolt slightly ahead, foundation models overtake PatchTST at input sizes 96/168.
- [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] — Cited as foundation-model baseline excluded from the controlled 6-ISO grid benchmark (focus on trained-from-scratch comparison); discussed in limitations as globally-pretrained alternative.

## Related Models
- Patched predecessor: [[PatchTST]] (encoder-decoder patching); compared directly — TimesFM decoder-only is more FLOPS-efficient for variable (context, horizon) zero-shot.
- LLM forecasters: [[LLMTime]] (GPT-3 prompting, Gruver et al. 2023) and [[TimeGPT-1]] (Garza et al. 2023) — both beaten significantly.
- Same first author dense alternative: [[TiDE]] ([[2024_Das_TiDE_Long_Term_Forecasting]]).
- Successors benchmarked in vault: [[Chronos]], [[Chronos-Bolt]], [[Moirai]], [[LagLlama]], [[Time-MoE]], [[Sundial]].
- [[2026_Khwaja_Toto_2_Scaling_Era]] — TimesFM 2.5/2.0 beaten on every benchmark by Toto 2.0 (BOOM 10.7/11.3, GIFT 25.8, TIME behind top-3); Fig. 1 Pareto comparison.
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — **TimesFM-2.5** baseline beaten: fev-bench W 75.9/S 42.3 vs 90.7/47.3 SQL; GIFT-Eval WQL 77.5/51.0 vs 81.9/51.4; capability matrix Table 1: no multivariate/covariate support.
