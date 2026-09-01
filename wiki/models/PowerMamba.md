---
type: model
name: PowerMamba
category: Deep Learning / Dual-Path Selective State-Space Model for Power Systems
tags:
  - model
  - mamba
  - ssm
  - power-systems
  - multivariate-forecasting
---

# ⚡ PowerMamba

## Overview
PowerMamba (Menati, Doudi, Kalathil & Xie, arXiv:2412.06112) is a selective-SSM ([[Mamba_SSM]]) multivariate forecaster tailored to electric power systems — jointly forecasting zonal load, day-ahead price, ancillary-service price, and renewable generation instead of one series at a time. Pipeline:

1. **[[RevIN]]** normalization (empirically beats Z-score on non-stationary grid series) → moving-average decomposition into trend $T(x)$ and seasonal $S(x)=x-T(x)$ → concatenation $x_{ts}=[T(x);S(x)]$ → fixed-size linear projection to $E\times D$ (model size independent of context/horizon).
2. **Dual-path standard/inverse Mamba blocks** — temporal tokens and transposed variate tokens processed simultaneously for intra-series and inter-series dependencies:
$$x_m = \text{Mamba}(\text{DO}_1(x_e)), \qquad x_{im} = \text{iMamba}(\text{DO}_2(x_e^\top))$$
3. **Output head**: element-wise sum of block outputs + residual, then linear: $x_c=[x_e;\,x_m;\,x_{im};\,x_m \oplus x_{im}]$, $\;y=\text{Linear}_W(x_c)$.
4. **External-forecast token module**: ERCOT day-ahead load/renewable forecasts are appended to the context end ($L\to L+W$), then compressed back to fixed $L\times 2D$ — token size stays independent of horizon (vs naive appending's 25× width inflation at W=24).

## Typical Usage in EV Load Forecasting
- **Input**: 22–262 channel [[ERCOT_GridSet]] series ([[Historical_Load]], prices, AS prices, renewables ± external forecasts); L=240.
- **Forecasting Horizon**: [[Short_Term_Forecasting]] to [[Long_Term_Forecasting]] (W ∈ {24,48,72,96,168}).
- **Strengths**: ~7% avg error reduction vs best Mamba baseline (TimeMachine) with −43% params and −78% vs iTransformer; external forecasts cut overall MSE **43%** (renewables −76%) and even prices −7% despite no external price forecasts; fastest training/inference of the strong baselines.
- **Weaknesses**: point forecasts only (L2 loss); zonal granularity, not station/nodal or EV-station level.

## 📚 Literature Usage
- [[2024_Menati_PowerMamba_Power_Systems_SSM]] — Original paper + open benchmarking toolbox and [[ERCOT_GridSet]] dataset release.
- [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] — Benchmarked as a core SSM representative on EIA-930: 5.72% avg MAPE load-only; best-with-weather on ISO-NE/MISO after pre-decomposition weather fusion.
- [[2026_Tang_PC_M3_Mamba_EV_Clusters]] — Used as flexibility-envelope baseline (Hausdorff error 9.7 vs PC-M3's 3.4).

## Related Pages
- [[Mamba_SSM]]
- [[S_Mamba]]
- [[RevIN]]
