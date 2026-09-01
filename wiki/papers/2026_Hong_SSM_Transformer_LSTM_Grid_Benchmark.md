---
type: paper
title: "Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting"
authors: [Sunki Hong, Jisoo Lee]
year: 2026
journal_conference: "arXiv preprint (arXiv:2602.21415)"
doi_url: "https://arxiv.org/abs/2602.21415"
models_used: ["[[S_Mamba]]", "[[PowerMamba]]", "[[PatchTST]]", "[[iTransformer]]", "[[LSTM]]"]
datasets_used: ["EIA-930 hourly system load: CAISO, ISO-NE, MISO, PJM, ERCOT, NYISO (+ SWPP for weather experiments only)"] # no EIA-930 concept page yet
features_used: ["[[Historical_Load]]", "temporal embeddings (hour-of-day, day-of-week)", "[[Weather_Traffic]]", "weather covariates: temperature, humidity, wind speed, GHI, cloud cover"]
forecasting_horizon: "[[Long_Term_Forecasting]]" # W ∈ {24, 48, 72, 96, 168} h; weather study at W = 24
metrics: ["[[NRMSE]] (reported as normalized 'MSE %')", "[[MAPE]]", "[[MAE]] (nMAE for non-load tasks)", "signed-error tails P0.5/P99.5"]
tags: [paper, ev-load-forecasting, benchmark, mamba, ssm, transformer]
---

# Summary: Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting

## 🎯 Main Objective & Contribution

First benchmark of SSM vs Transformer vs RNN architectures **across multiple US ISOs under identical protocols**. Five models — [[PowerMamba]], [[S_Mamba]], [[iTransformer]], [[PatchTST]], 2-layer bidirectional [[LSTM]] (~2.6M params) — on hourly EIA-930 demand from six ISOs (seven for weather), forecast windows W = 24–168 h.

Three contributions:
1. **US Grid Benchmark** — consistent hyperparameters/preprocessing across grids; PatchTST leads load-only (15/30 MAPE wins), SSMs second (14/30 combined).
2. **Weather Integration Benchmark** — architecture-matched thermal-lag-aligned fusion layers; ranking reverses with weather: iTransformer's cross-variate attention gains **3×** more than PatchTST (−1.62 vs −0.52 pp avg ΔMAPE). Parameter-controlled tiers prove the gap is *architectural, not capacity-driven*.
3. **Multitype Generalization** — solar/wind/price/ancillary tasks show rankings are task-dependent: PatchTST wins rhythmic signals (solar), SSMs win chaotic ones (wind, price).

Key message: **no single best model — input availability determines the optimal architecture.**

## 🧠 Methodology & Model Architecture

**Task**: system-level (balancing-authority aggregate) load forecasting. Given lookback L = 240 h (10 days):

$$\hat{y}_{t+1:t+W} = f_\theta\!\left(x_{t-L+1:t},\; z_{t-L+1:t}\right) \tag{1}$$

where $x$ = historical load, $z$ = exogenous features (calendar embeddings; optionally weather).

**Five architectures**:
- **[[S_Mamba]]**: minimalist encoder→stacked Mamba blocks; tests whether raw selective SSM suffices; O(n).
- **[[PowerMamba]]**: series decomposition (trend + seasonal BiMamba branches) + bidirectional processing.
- **[[PatchTST]]**: channel-independent patching, shared Transformer weights per channel.
- **[[iTransformer]]**: variate-as-token inversion; attention over variables — degenerates to near-identity with a single load variate.
- **[[LSTM]]**: 2-layer bidirectional, d=256.

**Shared domain adaptations** (preserve each core mechanism): learnable hour-of-day/day-of-week embeddings; bidirectional encoding strictly within the fixed lookback window; attention-weighted pooling $c=\sum_t a_t h_t$; modular encode-then-fuse weather layer toggleable without retraining (~0.3M params for SSMs/LSTM, ~0.7M PatchTST).

**Architecture-matched weather fusion**: S-Mamba early summation into d_model before BiMamba stack; PowerMamba pre-decomposition fusion (routes weather variance to both trend/seasonal streams); PatchTST interleaved cross-attention (load patches query independently-patched weather patches); iTransformer weather as additional variate tokens; LSTM early per-timestep concatenation. Weather aligned to building thermal lags (2–6 h HVAC response).

**Capacity-controlled comparison**: Tier 1 d=512 (iTransformer 6.44M vs scaled PatchTST-L 9.84M), Tier 2 d=256 (shrunk iTransformer-S 2.44M vs PatchTST 1.77–2.0M) — confirms weather-benefit reversal survives parameter matching.

**Metrics**:

$$\text{MSE (\%)} = \frac{100}{\bar{y}}\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2} \tag{2}$$

$$\text{MAPE (\%)} = \frac{100}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right| \tag{3}$$

(Eq. 2 is effectively mean-normalized [[RMSE]] despite the "MSE" label; nMAE used where actuals ≈ 0; signed-error tails P0.5/P99.5 report under-/over-prediction extremes.) Training: AdamW lr 1e-3, OneCycleLR, ≤200 epochs, early stop patience 30 on validation MAPE, seed 42, 70/15/15 chronological split; walk-forward backtest Nov 2023–Nov 2025 for weather runs (105 + 84 capacity experiments).

## 📊 Dataset & Input Features

- **Source**: [EIA-930 Hourly Electric Grid Monitor](https://www.eia.gov/electricity/gridmonitor/) — hourly system-level demand, ~4 years (2022–2025) per grid, z-score normalized per grid on train stats only.
- **Six core ISOs**: CAISO (47.1 GW peak, duck curve), ISO-NE (25.6 GW, winter-peaking), MISO (127.1 GW, wind-rich), PJM (150.4 GW, largest), ERCOT (85.5 GW, isolated/extreme weather), NYISO (32.1 GW, dense urban summer peaks); **SWPP** (54.4 GW) added for weather experiments only.
- **Weather covariates** ([[Weather_Traffic]] via Open-Meteo hourly products): temperature, humidity, wind speed, GHI, cloud cover — lag-aligned using empirical thermal-lag parameters. Note: reanalysis (observed) weather, not NWP forecasts.
- **Temporal features**: hour-of-day, day-of-week as learnable embeddings.
- **Code/checkpoints**: https://github.com/gramm-ai/grid-forecast-benchmark

## 📈 Performance & Results

**Load-only (30 grid×window rows)** — Table IV macro averages:

| Model | Params | MAPE % | MSE % | MAPE wins |
|---|---|---|---|---|
| PatchTST | 2.0M | **5.59** | **7.53** | **15/30** |
| PowerMamba | 4.0M | 5.72 | 7.62 | 7/30 |
| S-Mamba | 2.0M | 5.80 | 7.58 | 7/30 |
| iTransformer | 6.5M | 6.14 | 7.95 | 1/30 |
| LSTM | 2.6M | 6.83 | 9.13 | 0/30 |

Grid split: PatchTST leads CAISO/MISO/ERCOT (regular diurnal shapes fit patch boundaries); SSMs lead ISO-NE/PJM/NYISO (irregular modulation rewards selective gating). Best W=24 examples: ERCOT PatchTST 2.85%, MISO S-Mamba 2.33%, PJM S-Mamba 2.97%. Published operational day-ahead references: PJM ~1.9%, ISO-NE ~2.1%, ERCOT ~2.7% — benchmark approaches but doesn't match (no NWP inputs, ensembles, or analyst correction by design).

**With weather (7 grids, W=24)** — rankings reverse: **SSMs best on 5/7 grids** (S-Mamba: SWPP 3.11%, ERCOT 1.96%, NYISO 3.11%; PowerMamba: ISO-NE 3.62%, MISO 2.11%); iTransformer wins CAISO 3.19% and ties PJM. Avg ΔMAPE (Table VI): iTransformer **−1.62**, PowerMamba −0.74, S-Mamba −0.71, PatchTST −0.52, LSTM −0.36 pp. Temporal-token control shows iTransformer gains from *any* extra tokens; capacity tiers confirm the 3× gap is architectural. Weather value is largest where high climate variability meets high baseline error (ERCOT, ISO-NE, SWPP) and near zero in mild/large-smoothed grids (CAISO, MISO ceiling effect).

**Beyond load (nMAE, W=24)**: solar → PatchTST 23.1%; wind → S-Mamba 35.4%; price → S-Mamba 27.5%; ancillary → PatchTST 79.3%. Overall nMAE wins: PatchTST 11/18, S-Mamba 5/18.

**Tail errors (P0.5/P99.5)**: widen monotonically with horizon (e.g., CAISO W=168 S-Mamba −22.4/+51.2 pp); weather narrows the error range on sensitive grids.

## 💡 Limitations & Identified Research Gaps

- **System/balancing-authority level only** — explicitly not nodal/zonal, and nowhere near EV charging-station granularity; station-level loads are far sparser and event-driven.
- **Point forecasts only** — deterministic MSE/MAPE; no prediction intervals, quantiles, or probabilistic heads.
- **Hourly resolution** — no sub-hourly dynamics relevant to fast-charging ramps.
- Weather benchmark only at W=24; single seed (42), no significance testing; L=240 not ablated; efficiency measured by parameter count, not wall-clock latency; ancillary-service results preliminary (ERCOT only); excludes foundation models (Chronos, TimesFM), TimeMixer, and hybrid Mamba-Transformer designs.
- Reanalysis weather instead of operational NWP forecasts inflates weather benefit at longer horizons.

**Thesis relevance**: provides exactly the three-way (SSM/Transformer/RNN) architectural comparison Gap T-7 asks for — but at grid aggregate scale, leaving open whether the channel-independence vs cross-variate vs selective-SSM trade-off transfers to sparse, stochastic, price/weather-sensitive station-level EV loads.

## 📚 BibTeX & Citation Reference

```bibtex
@misc{2026_Hong_USGridBenchmark,
  title         = {Benchmarking State Space Models, Transformers, and Recurrent Networks for {US} Grid Forecasting},
  author        = {Hong, Sunki and Lee, Jisoo},
  year          = {2026},
  eprint        = {2602.21415},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  doi           = {10.48550/arXiv.2602.21415},
  url           = {https://arxiv.org/abs/2602.21415}
}
```

## 🔗 Key References & Citation Graph

- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — source of the variate-tokenized iTransformer benchmarked here.
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — PatchTST foundation note; its channel independence explains weak weather utilization.
- [[2024_Menati_PowerMamba_Power_Systems_SSM]] — PowerMamba origin (decomposition + bidirectional SSM for power data); page needs creating.
- [[Mamba_SSM]] — base selective state space mechanism underlying both SSMs.
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM baseline lineage.
- Context: [[2025_Meyer_Benchmark_Foundation_Models]] — this paper deliberately excludes zero-shot foundation models, complementing that line.
