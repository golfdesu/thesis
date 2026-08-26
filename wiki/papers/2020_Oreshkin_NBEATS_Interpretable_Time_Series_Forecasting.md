---
type: paper
title: "N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting"
authors: [Boris N. Oreshkin, Dmitri Carpov, Nicolas Chapados, Yoshua Bengio]
year: 2020
journal_conference: "ICLR 2020"
doi_url: "https://arxiv.org/abs/1905.10437"
models_used: ["[[NBEATS]]", "[[NBEATS-G]]", "[[NBEATS-I]]"]
datasets_used: ["[[M4]]", "[[M3]]", "[[Tourism]]", "[[Electricity_ECL]]", "[[Traffic]]"]
features_used: ["[[Lookback_Window]]", "[[Learned_Basis]]", "[[Polynomial_Trend_Basis]]", "[[Fourier_Seasonality_Basis]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[sMAPE]]", "[[MAPE]]", "[[MASE]]", "[[OWA]]", "[[ND]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting

## 🎯 Main Objective & Contribution
- Pure deep learning architecture for **univariate point forecasting**: deep stack of fully connected layers with **backward (backcast) and forward (forecast) residual links** — no time-series-specific components, no feature engineering, no input scaling.
- First empirical proof that pure DL outperforms well-established statistical approaches on [[M4]], [[M3]], and [[Tourism]]: on M4 by **11% over the statistical benchmark**, 7% over the best statistical entry, and **3% over the M4 competition winner** (Smyl's DL/TS hybrid).
- Second contribution: an **interpretable configuration** whose outputs decompose into human-readable trend and seasonality components (like STL / X-13ARIMA) with negligible accuracy loss.

## 🧠 Methodology & Model Architecture
### Basic block
The ℓ-th block takes input $x_\ell$ and outputs backcast $\hat{x}_\ell$ and partial forecast $\hat{y}_\ell$. First a 4-layer FC stack predicts basis expansion coefficients (**FC Stack Equations**):
$$h_{\ell,1} = \mathrm{FC}_{\ell,1}(x_\ell), \quad h_{\ell,2} = \mathrm{FC}_{\ell,2}(h_{\ell,1}), \quad h_{\ell,3} = \mathrm{FC}_{\ell,3}(h_{\ell,2}), \quad h_{\ell,4} = \mathrm{FC}_{\ell,4}(h_{\ell,3})$$
$$\theta^b_\ell = \mathrm{LINEAR}^b_\ell(h_{\ell,4}), \quad \theta^f_\ell = \mathrm{LINEAR}^f_\ell(h_{\ell,4}) \tag{1}$$
with $h_{\ell,1} = \mathrm{RELU}(W_{\ell,1}x_\ell + b_{\ell,1})$. Then basis layers project coefficients onto basis vectors (**Basis Expansion Equations**):
$$\hat{y}_\ell = \sum_{i=1}^{\dim(\theta^f_\ell)} \theta^f_{\ell,i}\, v^f_i, \qquad \hat{x}_\ell = \sum_{i=1}^{\dim(\theta^b_\ell)} \theta^b_{\ell,i}\, v^b_i$$

### Doubly residual stacking (DRESS)
Two residual branches — one over backcasts, one accumulating partial forecasts (**Doubly Residual Recursion**):
$$x_\ell = x_{\ell-1} - \hat{x}_{\ell-1}, \qquad \hat{y} = \sum_\ell \hat{y}_\ell$$
Each prior block removes from the signal what it can approximate well, easing downstream forecasting; hierarchical aggregation of partial forecasts enables interpretability.
Generic configuration basis layers are learnable linear projections:
$$\hat{y}_\ell = V^f_\ell \theta^f_\ell + b^f_\ell, \qquad \hat{x}_\ell = V^b_\ell \theta^b_\ell + b^b_\ell$$

### Interpretable configuration (trend + seasonality stacks)
**Trend model** — polynomial basis of small degree $p$ (slowly varying; Eq. 2), with time vector $t = [0,1,\dots,H-2,H-1]^\top/H$:
$$\hat{y}^{s,\ell}_t = \sum_{i=0}^{p} \theta^{s,\ell,f}_i t^i, \qquad \hat{y}^{tr}_{s,\ell} = T\theta^{s,\ell}_f, \;\; T = [1, t, \dots, t^p]$$
**Seasonality model** — Fourier basis of periodic functions (Eq. 3):
$$\hat{y}^{s,\ell}_t = \sum_{i=0}^{\lfloor H/2 - 1 \rfloor} \theta^{s,\ell,f}_i \cos(2\pi i t) + \theta^{s,\ell,f}_{i+\lfloor H/2 \rfloor} \sin(2\pi i t), \qquad \hat{y}^{seas}_{s,\ell} = S\theta^{s,\ell}_f$$
Architecture: trend stack followed by seasonality stack, 3 residual blocks each, basis functions shared per stack, all weights shared within stack (best validation performance). Trend is removed from the input before the seasonality stack sees it.
### Ensembling & training
Ensemble diversity via: 3 losses ([[sMAPE]], [[MASE]], [[MAPE]]; MAPE-only for TOURISM), 6 lookback window lengths ($2H,\dots,7H$), and bagging over random initializations — **180 models**, median aggregation. Ensembling proved a stronger regularizer than dropout or L2. Trained in TensorFlow with [[Adam]] (lr = 0.001), batch size 1024, early stopping; gradient flow stopped through sMAPE denominator for numerical stability. One model per horizon; architecture/hyperparameters fixed across horizons and datasets (generic: width 512, 30 stacks × 4 FC layers; interpretable: trend width 256/degree 2–3, seasonality width 2048).
### Meta-learning interpretation
Blocks act as iterations of an inner learning procedure modifying expansion coefficients $\theta^f$, while gradient descent on network parameters is the outer procedure — deeper stacks/ensembles improve generalization like more inner iterations.

## 📊 Dataset & Input Features
| Dataset | # Series | Frequencies | Horizons |
|---|---|---|---|
| M4 | 100,000 | yearly→hourly (23k Y / 24k Q / 48k M / 359 W / 4,227 D / 414 H) | 6/8/18/13/14/48 |
| M3 | 3,003 | yearly/quarterly/monthly/other (645/756/1428/174) | 6/8/18/8 |
| TOURISM | 1,311 | yearly/quarterly/monthly (518/427/366) | 4/8/24 |
| ELECTRICITY (UCI) | 370 client hourly series | hourly (aggregated by sum) | test splits at 2014-09-01, 2014-03-31, last 7 days |
| TRAFFIC (PEMS-SF, UCI) | 963 SF freeway sensors | hourly (aggregated by mean), Jan 2008–Mar 2009 | test splits at 2008-06-15, 2008-01-14, last 7 days |

- Input features: only the raw lookback window $x \in \mathbb{R}^t$ (length $2H$–$7H$); no covariates, scaling, or TS-specific engineering (unlike DeepAR/Deep State which use day-of-week/hour-of-day covariates).
- Data URLs found in footnotes: ELECTRICITY — https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014 ; TRAFFIC — https://archive.ics.uci.edu/ml/datasets/PEMS-SF ; MatFact aggregated data script — https://github.com/rofuyu/exp-trmf-nips16/blob/master/python/exp-scripts/datasets/download-data.sh ; M4 dataset — https://github.com/M4Competition/M4-methods/tree/master/Dataset ; UCI repository — http://archive.ics.uci.edu/ml ; X-13ARIMA manual — http://www.census.gov/ts/x13as/docX13AS.pdf ; code: https://github.com/ElementAI/N-BEATS

## 📈 Performance & Results
- **M4 (100k series)**: N-BEATS-I+G sMAPE **11.135**, OWA **0.795** vs M4 winner DL/TS hybrid 11.374/0.821, best ML/TS combination (FFORMA) 11.720/0.838, best statistical 11.986/0.861, best pure ML 12.894/0.915. N-BEATS-G alone: 11.168/0.797. Statistically significant improvement over Smyl in 18/31 frequency×type subsets (99% two-sided paired t-test).
- **M3**: average sMAPE **12.37** (I+G) vs EXP 12.71 (prior SOTA), DOTM 12.90, Theta 13.01, ARIMA 14.01.
- **TOURISM**: average MAPE **18.47** (G) vs LeeCBaker 19.35, Stratometrics 19.52, Theta/ETS 20.88 → gains of **4.2% over best-known** and 11.5% over auto-ARIMA.
- **ELECTRICITY / TRAFFIC (ND metric, point forecasts)**: N-BEATS-G ND **0.064** on ELECTRICITY (DeepAR 0.07, Deep State 0.083, MatFact 0.16) and **0.171** on TRAFFIC (DeepAR 0.17, Deep State 0.167, MatFact 0.20); also beats Deep Factors (0.065 vs 0.112 ELECTRICITY alt split; 0.114 vs 0.225 TRAFFIC). Achieved **without covariates**.
- **M4-Hourly ND**: N-BEATS-G 0.023 vs DeepState 0.044, DeepAR 0.09; TOURISM-Monthly 0.097 vs DeepAR 0.107; TOURISM-Quarterly 0.077 vs DeepState 0.098.
- Ablations: more stacks monotonically reduce validation sMAPE (11.154 @1 stack → 10.937 @30 stacks); interpretable trend+seasonality stacks synergize (10.986 @3+3 blocks vs 11.572 seasonality-only); DRESS beats PARALLEL/NO-RESIDUAL/LAST-FORWARD alternatives (e.g., OWA 0.803 vs 0.822 PARALLEL-G); state-of-the-art holds even with ensemble size 18 (<0.5% OWA loss).

## 💡 Limitations & Identified Research Gaps
- Univariate **point** forecasting only — no native probabilistic distributions/uncertainty quantification.
- Generic-model basis waveforms lack inherent structure (non-interpretable); interpretability requires hand-imposed inductive bias.
- No exogenous covariates supported in main experiments; meta-learning connection speculative ("should be the subject of future work").
- Ensemble of 180 models is computationally heavy for deployment, though results degrade <0.5% with 18 models.
- Reproducibility concerns raised about other works' split points (esp. TRAFFIC date reconstruction required heuristics).

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{oreshkin2020nbeats,
  title     = {N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting},
  author    = {Oreshkin, Boris N. and Carpov, Dmitri and Chapados, Nicolas and Bengio, Yoshua},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2020},
  url       = {https://arxiv.org/abs/1905.10437}
}
```

## 🔗 Key References & Citation Graph
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — DeepAR baseline compared against on ELECTRICITY/TRAFFIC/M4-Hourly
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — subsequent hybrid deep architecture for interpretable forecasting
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — linear models lineage following N-BEATS
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — later univariate forecasting benchmark building on N-BEATS
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] — direct successor architecture (hierarchical interpolation)
- [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] — electricity load probabilistic RNN context cited in related work
- Smyl (2020) M4 winner hybrid; He et al. (2016) ResNet; Huang et al. (2017) DenseNet; Yu et al. (2016) MatFact; Rangapuram et al. (2018) Deep State; Wang et al. (2019) Deep Factors
