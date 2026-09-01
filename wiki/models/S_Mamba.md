---
type: model
name: S-Mamba
category: Deep Learning / Minimalist Selective State-Space Forecaster
tags:
  - model
  - mamba
  - ssm
  - multivariate-forecasting
  - benchmark
---

# 🐍 S-Mamba

## Overview
S-Mamba (Wang et al., arXiv:2403.11144, *"Is Mamba Effective for Time Series Forecasting?"*) is a **minimalist Mamba encoder–decoder for multivariate time-series forecasting** — deliberately stripped down to test whether raw selective state-space modeling ([[Mamba_SSM]]) suffices without decomposition or fancy tokenization:

- **Channel-independent embedding**: each variate's lookback window linearly projected to tokens.
- **Stacked bidirectional Mamba blocks**: each layer runs selective SSM scans forward and backward over time, so every token sees both past and future context within the window at $O(n)$ complexity.
- **Simple decoder**: flatten + linear projection directly to the prediction horizon.

No series decomposition (contrast [[PowerMamba]]), no patching (contrast [[PatchTST]]), no variate-token attention (contrast [[iTransformer]]).

## Typical Usage in EV Load Forecasting
- **Input**: raw multivariate series; lookback L=240 h in the US grid benchmark.
- **Forecasting Horizon**: [[Long_Term_Forecasting]] (W ∈ {24,...,168} h).
- **Strengths**: near-PatchTST accuracy at half the parameters; **best architecture once weather covariates are available** on volatile grids; wins chaotic non-load tasks (wind 35.4% / price 27.5% nMAE).
- **Weaknesses**: point forecasts only; channel-independent embedding gives limited cross-variate interaction compared with inverted attention.

## 📚 Literature Usage
- [[2026_SSM_Transformer_LSTM_Grid_Benchmark]] — Benchmark role: second-best load-only (avg 5.80% MAPE, 7/30 wins) but best-with-weather on 3/7 grids (SWPP 3.11%, ERCOT 1.96%, NYISO 3.11% MAPE at W=24); strongest on wind and price tasks.
- [[2024_PowerMamba_Power_Systems_SSM]] — Cited as the Mamba-for-TSF evidence base [33] motivating PowerMamba's design.

## Related Pages
- [[Mamba_SSM]]
- [[PowerMamba]]
