---
type: paper
title: "Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network"
authors: [Mohammad Wazed Ali, Asif bin Mustafa, Md. Aukerul Moin Shuvo, Bernhard Sick]
year: 2024
journal_conference: "arXiv preprint arXiv:2409.11862 (Sep 2024)"
doi_url: "https://doi.org/10.48550/arXiv.2409.11862"
models_used: ["[[MQ_TCN]]", "[[TCN]]", "[[Inductive_Transfer_Learning]]", "[[Quantile_Regression]]", "[[XGBoost]]", "[[DeepAR]]"]
datasets_used: ["[[ACN_Data]]", "[[NREL_Workplace_Charging]]"]
features_used: ["[[Historical_Load]]", "[[Calendar_Features]]", "[[Sine_Cosine_Time_Encoding]]", "[[StationID_Embedding]]", "[[DTW_Similarity]]"]
forecasting_horizon: "[[Day_Ahead]]"
metrics: ["[[PICP]]", "[[Pinball_Loss]]", "[[Winkler_Score]]", "[[Normalized_Deviation]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network

## 🎯 Main Objective & Contribution
- Prior EV charging-site load models are use-case/location specific, need large data + compute, give point forecasts without uncertainty, and ignore high-cardinality categorical features.
- Proposes **[[MQ_TCN]]** (Multi-Quantile [[TCN]]) with **[[Inductive_Transfer_Learning]]** to transfer day-ahead forecasting knowledge among geographically separated charging sites under extreme data scarcity and low compute.
- Key results: PICP 93.62% at JPL (**+28.93% over XGBoost**, day-ahead); with TL from JPL, **PICP 96.88% at NREL using only 2 weeks of data** (+18.23% vs XGBoost trained on 6 months); Office-1 91.04% (4 h-ahead) / 87.30% (day-ahead) with only 1 month of data; up to **72% reduction in learnable parameters** at negligible accuracy cost (~3.4% PICP).
- First (per authors) combination of multi-step quantile regression DL + inductive TL across separated EV sites; site selection for transfer guided by **Dynamic Time Warping (DTW)** similarity.

## 🧠 Methodology & Model Architecture
- **Problem**: multivariate series $X=\{x_t\}_{t=1}^T \in \mathbb{R}^{T\times d}$ (d non-predictive covariates), target $Y\in\mathbb{R}^{T\times1}$; forecast $\{\hat{y}_t\}_{t=T+1}^{T+\delta} = F(\{x_t\},\{y_t\})$ δ steps ahead; TL learns target function $f_{td}(.)$ from source domain $\mathcal{D}_{sd}$ to resource-constrained target site $\mathcal{D}_{td}$ ($\mathcal{D}_{sd}\neq\mathcal{D}_{td}$, $P_{sd}\neq P_{td}$); both homogeneous and heterogeneous TL settings investigated.
- **Dilated causal convolution** (**Eq. 1 – Dilated convolution**):
$$G(s) = (x *_{d_l} f_{\text{filter}})(s) = \sum_{i=0}^{k-1} f_{\text{filter}}(i)\cdot x_{s-d_l\cdot i}$$
with filter size $k$ and dilation factor $d_l$; 1D fully convolutional structure with zero-padding, causal masking prevents leakage.
- **Residual block** (**Eq. 2 – Residual output**): $o = \text{Activation}(x + G(x))$, with WeightNorm + ReLU + dropout and optional 1×1 conv (after Bai et al. TCN).
- **Multi-quantile heads**: TCN encoder feeds fully-connected layers each predicting a distinct quantile of the forecast distribution (quantile levels q ∈ {0.05, 0.50, 0.90}); outputs $\hat{y}^{q_n}_{T+1},\dots,\hat{y}^{q_n}_{T+\delta}$ per quantile n.
- **Pinball Loss training objective** (**Eq. 3 – Pinball loss**):
$$L_{PB}(q, y_{T+i}, \hat{y}^q_{T+i}) = \begin{cases} (1-q)\cdot(y_{T+i}-\hat{y}^q_{T+i}), & \hat{y}^q_{T+i} \geq y_{T+i} \\ q\cdot(y_{T+i}-\hat{y}^q_{T+i}), & \hat{y}^q_{T+i} < y_{T+i} \end{cases}$$
- **Inductive TL ("head replacement")**: pre-train MQ-TCN on data-rich source (JPL); remove last layer, add fresh TCN blocks on top as feature extractor plus FC quantile heads for the target task; enables heterogeneous label spaces $T_{td}\in\mathbb{R}^{1,4,24}$ (horizons 1 h, 4 h, 24 h).
- **Site matching**: DTW distance between site load profiles selects transfer pairs — low DTW for JPL↔Office-1 and JPL↔NREL (chosen sources/targets), high DTW for Caltech↔Office-1/NREL.
- **Evaluation metrics** (**Eq. 4–7 – PICP, Winkler Score, ND**):
$$\text{PICP} = \frac{1}{N}\sum_{i=1}^N \varepsilon_i,\quad \varepsilon_i = \begin{cases}1 & y_{T+i}\in[L_{T+i,q}, U_{T+i,q}]\\ 0 & \text{else}\end{cases}$$
$$WS = \begin{cases}\gamma, & L\le y \le U\\ \gamma + 2(L-y)/\alpha, & y<L\\ \gamma + 2(y-U)/\alpha, & y>U\end{cases} \quad (\alpha=0.15), \qquad ND = \frac{\sum_i|y_{T+i}-\hat{y}_{T+i}|}{\sum_i|y_{T+i}|}$$
- Protocol: last 10% test set; blocked time-series cross-validation on remaining 90% (80/20 train/val folds); hyperparameters via Tree-structured Parzen Estimator (Bayesian optimization); retrain best config on 90%.

## 📊 Dataset & Input Features
- **[[ACN_Data]]** (Lee, Li & Low, ACM e-Energy '19 — open EV charging dataset): Caltech — 54 stations, 31,424 sessions, ~40 months, 13 features; JPL — 50 stations, 33,638 sessions, ~35 months, 13 features; Office-1 (small office workplace) — 8 stations, 1,683 sessions, ~30 months, 13 features.
- **[[NREL_Workplace_Charging]]** (Neuman, Meintz & Jun, 2021 — workplace charging behavior collection): 141 stations, 40,979 sessions, ~59 months, 16 features.
- Hourly aggregation; anomalies removed with Facebook Prophet + domain knowledge; missing values handled; Min-Max scaling of numerical features; sine-cosine transforms of cyclic temporal features; StationID high-cardinality category compressed from 186→30 values by encoder-based dimensionality reduction; one-hot for 2–5 categories, embedding layers for 5–10; COVID period excluded (data curated until March 2020).
- Data availability URLs: no explicit repository URL stated in the paper; datasets identified via refs [21] (NREL workplace charging data) and [22] (ACN-Data, e-Energy '19).

## 📈 Performance & Results
Source domains (lookback/horizon in hours; quantiles 0.05/0.50/0.90):
- **JPL (168→24)**: MQ-TCN PICP **93.62%**, Pinball 2.28, WS 21.55, ND 0.2226 vs XGBoost PICP 64.69%, ND 0.1770, DeepAR ND 0.1770 → +28.93% coverage improvement over XGBoost.
- **JPL (168→48)**: MQ-TCN PICP 75.50% vs XGBoost — none (XGBoost row 78.96 belongs to Caltech); DeepAR ND 0.2955 vs MQ-TCN 0.2266.
- **Caltech (168→48)**: MQ-TCN PICP 84.93% vs XGBoost 78.96% (+5.97%); Caltech (336→24): 82.79%; (336→48): 80.90%; DeepAR achieves best ND at Caltech (0.1770).
Target domains (inductive TL from JPL):
- **NREL, 2 weeks data**: PICP **96.88%** (24 h lookback, 1 h ahead), Pinball 1.86, WS 9.78; 95.08% day-ahead with 72 h lookback/1 month — vs full-data XGBoost max 80.21% and DeepAR ND ≈ 1.06.
- **Office-1, 1 month data**: PICP **91.04%** (72→4), 87.30% (72→24), 86.76% single-step; mean MQ-TCN PICP 83.36 / ND 0.4813 vs XGBoost mean PICP 47.94 and DeepAR mean ND 1.067.
- Parameter efficiency: TL models use far fewer learnable params (e.g., 3,896–35,528) than source models (223k–261k) while achieving comparable/higher PICP; 72% parameter cut costs only ~3.4% PICP.
- No monotonic relationship found between lookback length or horizon and accuracy (e.g., increasing lookback 72→168 h degraded Office-1 day-ahead accuracy).

## 💡 Limitations & Identified Research Gaps
- Authors: model "failed in some novel situations" under transfer — future work on continual representation learning and adding meta-information.
- No conclusive guidance on lookback/horizon choice; sensitivity is site-specific.
- High NREL Winkler Scores despite high PICP indicate wide intervals (over-coverage without sharpness guarantees).
- Single-step DeepAR comparisons limited (DeepAR could not support some single-step settings); point-forecast baseline (ND) favors XGBoost/DeepAR even when interval quality is poor.
- Only quantile regression (no full predictive density); US workplace/public sites only.

## 📚 BibTeX & Citation Reference
```bibtex
@article{ali2024mqtcn,
  title   = {Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network},
  author  = {Ali, Mohammad Wazed and Mustafa, Asif bin and Shuvo, Md. Aukerul Moin and Sick, Bernhard},
  journal = {arXiv preprint arXiv:2409.11862},
  year    = {2024}
}
```

## 🔗 Key References & Citation Graph
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — TCN architecture (dilated causal conv + residual blocks) that MQ-TCN extends
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — probabilistic autoregressive baseline
- [[2021_VanKriekinge_Day_Ahead_EV_Demand]] — cited day-ahead DNN EV charging demand forecasting (LSTM, calendar/weather)
- [[2023_Koohfar_Transformer_EV_Demand]] — cited transformer-based e-mobility demand forecasting
- [[2023_Huang_MetaProbformer_EV_Load]] — related probabilistic/meta-learning EV charging forecasts (MBQFN context)
- [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] — quantile-regression probabilistic load forecasting lineage
