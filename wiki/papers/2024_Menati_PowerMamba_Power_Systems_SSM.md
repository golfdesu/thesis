---
type: paper
title: "PowerMamba: A Deep State Space Model and Comprehensive Benchmark for Time Series Prediction in Electric Power Systems"
authors: [Ali Menati, Fatemeh Doudi, Dileep Kalathil, Le Xie]
year: 2024
journal_conference: "IEEE Transactions on Power Systems (2025), doi:10.1109/TPWRS.2025.3647539; preprint arXiv:2412.06112"
doi_url: "https://arxiv.org/abs/2412.06112"
models_used: ["[[PowerMamba]]", "[[Mamba_SSM]]", "[[RevIN]]", "[[iTransformer]]", "[[PatchTST]]", "[[DLinear]]", "[[Autoformer]]", "[[TimesNet]]"]
datasets_used: ["[[ERCOT_GridSet]]"]
features_used: ["[[Historical_Load]]", "zonal electricity price", "ancillary service price", "renewable generation (wind/solar)", "ERCOT external forecasts (day-ahead load + renewables)"]
forecasting_horizon: ["[[Short_Term_Forecasting]]", "[[Long_Term_Forecasting]]"]
metrics: ["MSE", "[[MAE]]"]
tags: [paper, power-systems, mamba, ssm, time-series-forecasting]
---

# Summary: PowerMamba: A Deep State Space Model and Comprehensive Benchmark for Time Series Prediction in Electric Power Systems

## 🎯 Main Objective & Contribution
- Grid volatility from electrification (incl. EVs), renewables, storage, and flexible loads motivates **multivariate** forecasting of load, price, ancillary-service (AS) price, and renewable generation *jointly* — prior art forecasted each variable separately, losing cross-variable correlations and inflating compute/training cost.
- Three contributions: (1) **PowerMamba**, a selective-SSM ([[Mamba_SSM]]) multivariate forecaster with dual-path standard/inverse Mamba blocks and trend–seasonal decomposition tailored to power time series; (2) a **time-series processing block** that injects high-resolution external forecasts (ERCOT day-ahead load/renewables) into seq2seq predictors with negligible size increase; (3) an open-access benchmarking toolbox plus the five-year ERCOT dataset **GridSet** (22 core channels, 262 extended).
- Headline: improves state-of-the-art prediction error by ~7% on average while cutting parameters 43% vs best Mamba baseline and 78% vs leading Transformer.

## 🧠 Methodology & Model Architecture
- **SSM foundation**: continuous latent dynamics (Eq. 1, reconstructed from PDF-extracted text):
$$ \frac{dh(t)}{dt} = Ah(t) + Bx(t), \qquad y(t) = Ch(t) \tag{1} $$
zero-order-hold discretisation $\bar{A} = \exp(\Delta A)$, $\bar{B} = A^{-1}(\exp(\Delta A) - I)B$ gives (Eq. 3, reconstructed):
$$ h_t = \bar{A}h_{t-1} + \bar{B}x_t, \qquad y_t = Ch_t \tag{3} $$
unrolled into a convolution kernel $K = (CB, CAB, \ldots, CA^{L-1}B)$, i.e. $y = K * x$ → parallel training, linear $O(LD)$ complexity vs quadratic attention.
- **Selective SSM (Mamba)**: $B, C \leftarrow \text{Linear}_N(x)$ input-dependent; discretisation step (Eq. 7): $\Delta = \text{softplus}(\text{parameter} + \text{Linear}_D(\text{Linear}_1(x)))$ → content-dependent focus on volatile segments.
- **Pipeline**: [[RevIN]] normalisation (beats Z-score) → moving-average decomposition into trend $T(x)$ and seasonal $S(x) = x - T(x)$ (window size grid-searched) → concatenation $x_{ts} = [T(x); S(x)]$ ($2L \times D$) → **fixed-size** linear projection to $E \times D$ embedding (model size independent of context/prediction length).
- **Dual path** (Eq. 9, reconstructed): temporal tokens + variate tokens via transposed input:
$$ x_m = \text{Mamba}(\text{DO}_1(x_e)), \qquad x_{im} = \text{iMamba}(\text{DO}_2(x_e^\top)) \tag{9} $$
intra-series (temporal) and inter-series (cross-channel) dependencies captured simultaneously; dropout before each block.
- **Output head** (Eq. 10): element-wise sum of block outputs improves gradient flow/stability; residual keeps $x_e$:
$$ x_c = [x_e;\ x_m;\ x_{im};\ x_m \oplus x_{im}], \qquad y = \text{Linear}_W(x_c) \tag{10} $$
- **External-forecast token module** (Sec. IV-E): instead of naively appending $W$ future columns (25× width inflation at $W{=}24$), predictions for $t{+}1..t{+}W$ are appended to the context end ($L \to L{+}W$), shifted back into context as extra channel features ($L{+}W) \times 2D$, then compressed back to fixed $L \times 2D$ — token size stays independent of horizon $W$.

## 📊 Dataset & Input Features
- **[[ERCOT_GridSet]]** (released with toolbox): five years of hourly ERCOT data, **43,824 hours (1,826 days), 2019–2023**; train = first 4 years, test = final year. Captures Texas renewable/storage/flexible-load growth.
- **22 core channels**: zonal loads (8 weather zones), zonal day-ahead settlement-point electricity prices (8), AS prices (4: Reg-Up, Reg-Down, RRS, Non-Spin), renewable generation (wind + solar, 2). Stats: loads mean 5,797.93 MW (σ 1,446.52); prices mean \$67.06/MWh (σ 422.15); AS prices mean \$52.41 (σ 662.53); renewables mean 6,363.30 MW (σ 4,438.36).
- **Extended version**: + ERCOT external forecasts (8 zonal-load + 2 renewable columns × 24-hour window, updated hourly, up to one week ahead) → **22 + 10×24 = 262 channels**; no external price forecasts exist.
- Appendix: six-year PJM ISO companion dataset (2019–2024; loads, prices, renewables) confirms cross-ISO generalisation.
- Code/toolbox: https://github.com/alimenati/PowerMamba (baselines implemented via https://github.com/thuml/Time-Series-Library/, PyTorch).

## 📈 Performance & Results
- **Accuracy vs baselines** ([[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting|TimeMachine]] [37], [[iTransformer]], [[PatchTST]], [[DLinear]], [[TimesNet]], Autoformer; L=240, W∈{24,48,72,96,168}, MSE/MAE on standardised series): PowerMamba best on nearly every task; e.g. GridSet W=24: **0.129/0.166** vs TimeMachine 0.135/0.166, iTransformer 0.147/0.181, PatchTST 0.142/0.183, Autoformer 0.301/0.311. Strongest on volatile load & renewables; best or second-best on prices even at W=168.
- **+7% avg accuracy over TimeMachine with −43% parameters**; −78% parameters vs leading Transformer (iTransformer). Only DLinear is smaller (but far less accurate at long horizons).
- **External forecasts cut overall error 43%** (GridSet W=24 MSE 0.129→0.074); renewable error **−76%** (0.590→0.142); price error −7% *despite no external price forecasts* — evidence of cross-channel information transfer. Gains hold when the module is grafted onto every baseline.
- **Speed**: 19% faster training / 14% faster inference vs TimeMachine (11.56 min / 0.113 ms-per-instance vs 14.22 / 0.131); >60%/57% faster than iTransformer (28.65 min / 0.260 ms); TimesNET slowest (1,773 min).
- **Robustness**: Gaussian noise injected into external inputs → only +2.6% MSE at 10% noise level, ≤+25.9% even at 30%.
- **Ablations**: decomposition helps most on volatile top-5% samples (renewables −6.01%, prices −4.97% MSE, total −5.07%, loads ~0); performance plateaus/slightly degrades beyond ~1M params (overfitting); MSE keeps improving with longer context up to 240 h — Mamba exploits long-range dependencies better than TimeMachine.

## 💡 Limitations & Identified Research Gaps
- **Point forecasts only** — trained with L2 loss, evaluated with MSE/MAE; no probabilistic/quantile output (contrast with [[Pinball_Loss]]-style methods relevant to EV charging).
- **Zonal granularity, not station/nodal level** — authors position DSO-level adaptation as future work; nothing about EV charging stations or EV-specific load evaluation (EVs appear only as motivation for load volatility).
- External forecasts unavailable for price/AS series; robustness tested only against synthetic iid Gaussian forecast noise.
- Future work (authors): extend dataset with energy-storage and data-center series; use deep SSMs for transient/dynamic disturbance prediction.
- Gap hooks for thesis: no uncertainty quantification, no station-level/EV case study, and no comparison against probabilistic baselines → direct openings for T-7-style comparator work.

## 📚 BibTeX
```bibtex
@misc{2024_Menati_PowerMamba,
  author        = {Menati, Ali and Doudi, Fatemeh and Kalathil, Dileep and Xie, Le},
  title         = {{PowerMamba}: A Deep State Space Model and Comprehensive Benchmark for Time Series Prediction in Electric Power Systems},
  year          = {2024},
  eprint        = {2412.06112},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2412.06112},
  note          = {v2, updated 20 Dec 2025}
}
```

## 🔗 Key References & Citation Graph
- [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]] — closest Mamba-based competitor; strongest baseline throughout (cited as [37])
- [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]] — Bi-Mamba+/Bi-Mamba4ts bidirectional processing for intra-/inter-series correlations [36]
- [[Mamba_SSM]] lineage: Mamba (Gu & Dao, arXiv:2312.00752) [14]; S4 structured state spaces (Gu et al., ICLR 2022) [13]
- Transformers: [[iTransformer]] [27], [[PatchTST]] [25], Autoformer [26], original attention [24]
- Linear/lightweight: [[DLinear]] & NLinear [32], TiDE [31]
- [[RevIN]] reversible instance normalisation [45]; ADAM optimiser [47]
- Related datasets contrasted: ERCOT/MISO multi-scale set (Zheng et al.) [38], Buildings-900k [39], Lago et al. day-ahead price benchmark [8]

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2024_Menati_PowerMamba_Power_Systems_SSM_refs]]
