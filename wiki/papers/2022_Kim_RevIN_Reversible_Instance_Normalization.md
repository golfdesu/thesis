---
type: paper
title: "Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift"
authors: [Taesung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jang-Ho Choi, Jaegul Choo]
year: 2022
journal_conference: "ICLR 2022"
doi_url: "https://openreview.net/forum?id=cGDAkQo1C0p"
models_used: ["[[RevIN]]", "[[Informer]]", "[[N-BEATS]]", "[[SCINet]]"]
datasets_used: ["[[ETT_Dataset]]", "[[ECL_Dataset]]", "[[UCI_Air_Quality]]", "[[Nasdaq_CNNpred]]", "[[M4_Competition]]"]
features_used: ["[[Historical_Load|Multivariate historical series (power load, oil temperature)]]", "Instance mean μ and standard deviation σ per input window", "Learnable affine parameters γ, β"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MSE]]", "[[MAE]]", "DTW", "TDI"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift

## 🎯 Main Objective & Contribution
- Addresses the **distribution shift problem** in time-series forecasting: statistical properties (mean/variance) of training vs. test data diverge because train/test splits are made at a point in time, degrading model accuracy — especially for long horizons.
- Proposes **[[RevIN]]**: a simple, generally-applicable, end-to-end trainable **normalization-and-denormalization** layer with learnable affine transformation, symmetrically structured to *remove* non-stationary statistics (instance mean μ, variance σ²) at the input layer and *restore* them at the output layer.
- Contributions: (1) model-agnostic plug-in layer applicable to any DNN with negligible cost; (2) state-of-the-art on seven large-scale real-world datasets by adding RevIN to Informer/N-BEATS/SCINet; (3) quantitative + qualitative analyses showing reduced train-test distribution discrepancy.

## 🧠 Methodology & Model Architecture
RevIN consists of two symmetric layers placed at virtually symmetric positions of an encoder-decoder structure (input and output layers; can also be added to intermediate layers).

**Equation 1 — Instance statistics (per variable k, instance i):**
$$\mathbb{E}_t[x_{kt}^{(i)}] = \frac{1}{T_x}\sum_{j=1}^{T_x} x_{kj}^{(i)}, \qquad \text{Var}[x_{kt}^{(i)}] = \frac{1}{T_x}\sum_{j=1}^{T_x}\left(x_{kj}^{(i)} - \mathbb{E}_t[x_{kt}^{(i)}]\right)^2$$

**Equation 2 — Instance normalization with learnable affine transform:**
$$\hat{x}_{kt}^{(i)} = \gamma_k \left( \frac{x_{kt}^{(i)} - \mathbb{E}_t[x_{kt}^{(i)}]}{\sqrt{\text{Var}[x_{kt}^{(i)}] + \epsilon}} \right) + \beta_k$$
where $\gamma, \beta \in \mathbb{R}^K$ are learnable affine parameter vectors.

**Equation 3 — Denormalization (output layer), using the SAME input statistics:**
$$\hat{y}_{kt}^{(i)} = \sqrt{\text{Var}[x_{kt}^{(i)}] + \epsilon} \cdot \left( \frac{\tilde{y}_{kt}^{(i)} - \beta_k}{\gamma_k} \right) + \mathbb{E}_t[x_{kt}^{(i)}]$$

Input length $T_x$ and prediction length $T_y$ may differ since normalization is over the temporal dimension.

**Theoretical justification (A.9):**
- Eq. 4/5 — distribution shift redefined as $\mathbb{E}[x^{tra}] \neq \mathbb{E}[x^{tst}]$ or $\text{Var}[x^{tra}] \neq \text{Var}[x^{tst}]$.
- Eq. 6/7 — after normalization, $\mathbb{E}[\hat{x}^{(i)}] = \beta$ and $\text{Var}[\hat{x}^{(i)}] = \gamma^2$ for all instances → train/test distributions become identical by definition.
- Eq. 8/9 — denormalized output satisfies $\mathbb{E}[\hat{y}^{(i)}] = \Delta + \mathbb{E}[x^{(i)}]$ and $\text{Var}[\hat{y}^{(i)}] = \lambda \cdot \text{Var}[x^{(i)}]$; the model only needs to learn the offset $(\Delta, \lambda)$ from the input distribution to the future distribution.

**Feature divergence analysis (A.10)** via symmetric KL divergence between train/test features:
$$D(f_k^{train} \| f_k^{test}) = KL(f_k^{train}\|f_k^{test}) + KL(f_k^{test}\|f_k^{train}), \quad KL(f_k^A\|f_k^B) = \log\frac{\sigma_k^B}{\sigma_k^A} + \frac{\sigma_A^2 + (\mu_k^A-\mu_k^B)^2}{2(\sigma_k^B)^2} - \frac{1}{2}$$

Baselines used with/without RevIN: [[Informer]], [[N-BEATS]], [[SCINet]]. Lightweight: only $2K$ extra parameters vs. ≥$3K^2$ for [[DAIN]]. Ablations show the affine transform helps consistently; RevIN in intermediate layers also works (e.g., MSE@960 ETTh2: LSTNet* 5.627, ES-RNN* 1.338, RevIN inter. 0.523, RevIN i/o 0.471).

## 📊 Dataset & Input Features
- **[[ETT_Dataset]]** (Electricity Transformer Temperature): 7 features (power load + oil temperature), two regions in China, 2 years; ETTh1/ETTh2 hourly, ETTm1 every 15 min. Split 12/4/4 months train/val/test. URL: https://github.com/zhouhaoyi/ETDataset
- **[[ECL_Dataset]]** (Electricity Consuming Load): kWh consumption of 321 clients, hourly, each client = one variable; split 15/3/4 months. URL: https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- **[[UCI_Air_Quality]]**: hourly averaged responses from 5 metal oxide chemical sensors in Italy; 13 variables, length 9537. URL: https://archive.ics.uci.edu/ml/datasets/Air+Quality
- **[[Nasdaq_CNNpred]]**: 82 variables (world indices, US company prices, treasury rates), daily, 1984 samples each. URL: https://archive.ics.uci.edu/ml/datasets/CNNpred%3A+CNN-based+stock+market+prediction+using+a+diverse+set+of+variables
- **[[M4_Competition]]**: ~100,000 series across hourly/daily/weekly/monthly/quarterly/yearly frequencies. URL: https://mofc.unic.ac.cy/m4/
- Inputs are the raw multivariate historical series only; no exogenous features. Prediction lengths: 1d–40d (hourly sets); 6h–14d (ETTm1). Metrics computed on z-score normalized data. Baseline code: https://github.com/zhouhaoyi/Informer2020 , https://github.com/cure-lab/SCINet . No explicit data availability statement beyond these public URLs.

## 📈 Performance & Results
Average MSE/MAE over 5 runs (Table 1 highlights):
- **ETTh1 @720**: SCINet 0.596/0.571 → **0.507/0.505**; N-BEATS 1.389/0.926 → 0.576/0.534; Informer 1.357/0.945 → 0.926/0.717.
- **ETTh2 @960**: N-BEATS MSE 6.408 → **0.471**; Informer 2.972 → 0.600; SCINet 1.862 → **0.438**.
- **ECL @960**: SCINet 0.235/0.330 → **0.200/0.292**; N-BEATS 0.399 → 0.325; Informer 0.930 → 0.894.
- Long-sequence robustness (input fixed at 48, Table 2, ETTh1): SCINet@960 MSE 0.900 → **0.557**.
- Vs other normalizations (Table 3, N-BEATS, MSE @168/@960 ETTh2): z-score 3.329/3.087, batch norm 6.206/7.755, RevBN 0.729/2.148, DAIN 1.982/2.802, **RevIN 0.419/0.465**.
- Similarity metrics (Table 8): DTW@960 ETTh2 reduced Informer 38.35→15.24, N-BEATS 53.15→12.77, SCINet 20.50→11.08.
- Cross-domain forecasting (A.2, SCINet trained on one ETT set, tested on another): e.g., ETTh1→ETTm1 @960 MSE 0.765 → **0.452**.
- Qualitative: baselines' predictions are shifted/scaled on ECL & Nasdaq; RevIN restores original distribution so predictions track level shifts.

## 💡 Limitations & Identified Research Gaps
- Purely point forecasts — no uncertainty quantification; no EV-specific evaluation despite direct relevance (EV charging load is strongly non-stationary across station lifecycle).
- Assumes future window statistics ≈ input-window statistics plus a small offset (Eq. 9 assumption) — may fail under abrupt regime changes longer than the input window.
- Evaluated mostly on generic benchmarks; no spatio-temporal modeling (each variable treated independently).
- Gap for thesis: apply [[RevIN]] to EV charging load models ([[MetaProbformer]], [[NHiTS]]) under distribution shift from new stations / anomalous events.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{kim2022revin,
  title     = {Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift},
  author    = {Kim, Taesung and Kim, Jinhee and Tae, Yunwon and Park, Cheonbok and Choi, Jang-Ho and Choo, Jaegul},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2022}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] (Transformer backbone underlying [[Informer]])
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]]
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]]
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]]
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] (successor long-horizon architecture)
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]]
