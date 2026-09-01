---
type: paper
title: "Feature-enhanced deep learning method for electric vehicle charging demand probabilistic forecasting of charging station"
authors: [Tingwei Cao, Yinliang Xu, Guowei Liu, Shengyu Tao, Wenjun Tang, Hongbin Sun]
year: 2024
journal_conference: "Applied Energy 371 (2024) 123751"
doi_url: "https://doi.org/10.1016/j.apenergy.2024.123751"
models_used: ["[[FEDM]]", "[[GRN]]", "[[GLU]]", "[[LSTM]]", "[[Transformer]]", "[[NBEATS]]", "[[DeepAR]]", "[[TCN]]", "[[Temporal_Fusion_Transformer]]", "[[LGBM]]", "[[ARIMA]]", "[[ESM]]", "[[Persistence_Model]]"]
datasets_used: ["[[Shenzhen_ST_EVCDP]]"]
features_used: ["[[Pearson_Correlation_Coefficient]]", "[[Electricity_Tariff]]", "[[Temperature]]", "[[Calendar_Features]]", "[[Weather_Conditions]]", "[[EV_Charging_Demand|Charging demand series]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[Qualified_Rate]]", "[[Accuracy]]", "[[Winkler_Score]]", "[[AIW]]", "[[Pinball_Loss]]", "[[SMAPE]]", "[[RMSE]]", "[[R_squared]]", "[[NRMSE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Feature-Enhanced Deep Learning Method for Electric Vehicle Charging Demand Probabilistic Forecasting of Charging Station

## 🎯 Main Objective & Contribution
- Proposes **[[FEDM]]** (Feature-Enhanced Deep Learning Method) for **station-level day-ahead probabilistic EV charging demand forecasting** under **low historical data stock** (12–24 days of training data).
- Key novelty: a **two-stage feature selection model** injecting the [[Pearson_Correlation_Coefficient]] between charging demand and external features as *prior knowledge* to initialize feature-importance weights — instead of feeding all features equally.
- Contributions: (1) improves accuracy rate, qualified rate, sharpness and computational efficiency vs 8 benchmarks; (2) correlation-coefficient-as-prior reweighting mechanism; (3) excellent performance with low data volume; solves the trend-lagging defect of non-enhanced models via GRN + multi-head self-attention.

## 🧠 Methodology & Model Architecture
Pipeline: external features (static: date/weekday/holiday; dynamic: TOU price, temperature, weather) → two-stage feature selection → LSTM intermediate layer(s) → [[GRN]] with residual connections → multi-head self-attention → quantile outputs → PIs via Monte Carlo sampling.

**Preliminaries**: Quantile definition (**Eq. 1**): $q_t^{(a)} = \inf\{y | F_t(y) \geq a\}$; approximate CDF from m quantiles (**Eq. 2**); PI $\hat{I}_t^{(\beta)} = [L_t^{(\beta)}, U_t^{(\beta)}]$ with $L_t^{(\beta)} = \hat{q}_t^{(\underline{\alpha})}, U_t^{(\beta)} = \hat{q}_t^{(\bar{\alpha})}$, $\bar{\alpha} - \underline{\alpha} = 1-\beta$ (**Eq. 3**), coverage $\Pr(Y_t \in \hat{I}_t^{(\beta)}) = 100(1-\beta)\%$ (**Eq. 4**).

**Gated Residual Network** (**Eqs. 15–19**):
$$\text{GRN}_\omega(Y, X) = \text{Norm}(Y + \text{GLU}_\omega(d_1))$$
$$d_1 = W_\omega^{(1)} \cdot d_2 + b_\omega^{(1)}$$
$$d_2 = f_{elu}\left(W_\omega^{(2)} \cdot Y + W_\omega^{(3)} \cdot X + b_\omega^{(2)}\right), \quad f_{elu} = \begin{cases} x, & x > 0 \\ \alpha(e^x - 1), & x \leq 0 \end{cases}$$
$$\text{GLU}_\omega(d_1) = \sigma\left(W_\omega^{(4)} \cdot d_1 + b_\omega^{(4)}\right) \odot \left(W_\omega^{(5)} \cdot d_1 + b_\omega^{(5)}\right)$$
with ELU activation, layer Norm, Hadamard product ⊙, shared weights ω, state size 160.

**Two-stage feature selection**:
- Stage 1 — Pearson correlation (**Eq. 20 population / Eq. 21 sample**):
$$\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{\mathbb{E}[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}, \qquad r = \frac{\sum_{t=1}^T (X_t - \bar{X})(Y_t - \bar{Y})}{\sqrt{\sum_{t=1}^T (X_t - \bar{X})^2} \sqrt{\sum_{t=1}^T (Y_t - \bar{Y})^2}}$$
Features with $|r| < 0.1$ get initial weight compressed to 0. Softmax weighting (**Eqs. 22–23**):
$$\text{Softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^m e^{x_j}}, \qquad \mu_x = \text{Softmax}(\text{GRN}(\tilde{X}, r_x))$$
- Stage 2 — independent per-feature GRNs then weighted combination (**Eq. 24**):
$$\hat{x} = \sum_{i=1}^m \mu_{x_i} \hat{x}_i$$

**Multi-head self-attention** (**Eqs. 25–27**, cf. [[2017_Attention_Is_All_You_Need]], [[2019_Li_LogSparse_Enhancing_Locality_Transformer]]):
$$\alpha_{i,j} = \frac{q_i^T \cdot k_j}{\sqrt{d_{q,k}}}, \qquad \hat{\alpha}_{i,j} = \text{Softmax}(\alpha_{i,j}), \qquad b_i = \sum_{j=1}^T \hat{\alpha}_{i,j} \cdot v_j$$

**Training loss** — improved quantile/pinball loss (**Eqs. 28–29**):
$$\mathcal{L} = \frac{\sum_{y_\tau \in \Omega} \sum_{i=1}^M \sum_{t=1}^T l\left(y_\tau, \hat{y}(q^{(\alpha_i)}, \tau-t, t), q^{(\alpha_i)}\right)}{MT}, \quad l(y,\hat{y},q) = q \cdot \max(0, y - \hat{y}) + (1-q) \cdot \max(0, \hat{y} - y)$$
Normalized test risk (**Eq. 30**) reported at 50% and 90% levels. Hyperparameters: quantile loss, ReLU, Adam, hidden size 64, 1 LSTM layer, 4 attention heads, dense layers 160, batch 96, input/output length 36 steps, dropout 0.1 (Monte Carlo dropout), 200 epochs; grid-searched.

**Evaluation criteria** (**Eqs. 5–14**): MAPE; SMAPE; R²; NRMSE; AR = (1 − NRMSE)×100%; QR = fraction of points with $|\hat{y}_t - y_t|/S_{max} \leq \eta$ (η set to 0.1 vs actual station capability ~0.25); sharpness/AIW $W = \frac{1}{T}\sum_t \delta_t^\beta(x)$; Winkler score:
$$S_W^{(\beta)} = -\bar{W} + \frac{1}{T}\sum_{t=1}^T\left[-\frac{2}{\alpha}(\hat{q}_t^{(\bar{\alpha})} - y_t)\mathbb{I}(\hat{q}_t^{(\bar{\alpha})}-y_t \geq 0) + \frac{2}{1-\alpha}(y_t - \hat{q}_t^{(\underline{\alpha})})\mathbb{I}(y_t - \hat{q}_t^{(\underline{\alpha})} \geq 0)\right]$$

## 📊 Dataset & Input Features
- **[[Shenzhen_ST_EVCDP]]** — real EV charging demand from one of the earliest charging stations in the core area of a city in southern China ([[Shenzhen_ST_EVCDP]] region; city has ≈**930,000 EVs and 260,000 charging points** in 2023). Time range: **2022-01-01 to 2022-12-31**, resolution **15-min (96 points/day)**, no missing values/outliers. Station count: individual station case study + 2 additional same-city stations for generalization tests.
- **Data availability**: GitHub dataset link ([[FEDQR_Dataset]]) given in ref [37]: https://github.com/Kenny4everlucky/FEDQR_dataset ; statement: *"Data will be made available on request."* Weather from historical local weather records; prices from historical station charging pricing data. Funding: China Southern Power Grid Innovation Project SZKJXM20210138.
- **Input features**: demand series (96 pts/day); daily average temperature; TOU electricity price split into peak (10:00–12:00, 14:00–19:00), flat (08:00–10:00, 12:00–14:00, 19:00–24:00), valley (00:00–08:00); weekday one-hot (weekend=1); weather conditions (sunny/cloudy/overcast/rainy + intermediates). Train/test ratio 8:2; training sets of 12–24 days before forecast day; output window fixed at 1 day ahead.
- Pearson analysis: electricity price most influential (charging peaks align with valley prices); temperature/weekday/weather effects are seasonal.

## 📈 Performance & Results
- **Feature-enhancement ablation (20-day training)**: FEDM vs FEDM w/o two-stage selection: RMSE 175.1 vs ~228–390 across seasons; SMAPE 7.95–9.89% vs 16.8–20.6%; R² up to 0.9839; **AR +8.3%, QR +3.1%, WS reduced by 33.64%**; fixes inaccurate fitting and trend lagging.
- **Initial-weight ablation (Table IV)**: Case 1 (|r|≥0.1 prior, zeros below) best: QR 99.22%, WS −0.4323; all-r weights 98.44%/−0.4625; equal weights 96.88%; random weights worst (95.83%/−0.5413).
- **Benchmark comparison (90% level)**: FEDM average **QR = 99.22%** (100% in spring & summer; best benchmark spring NBEATS 96.88%, summer DeepTCN/TFT 94.79%), i.e., **+5.21% over NBEATS, +4.54% over DeepTCN**. FEDM average **WS = −0.4323** vs DeepTCN −0.6443, NBEATS −0.6606, TFT −0.6951, LGBM −0.6820, ESM −0.8764, ARIMA −1.1854, Persistence −1.6785 (worst, autumn/winter ≈ −1.88/−1.79).
- **Data dependence**: with only **15 days** of training data FEDM reaches avg QR = 93.23%, AR = 84.44%, WS = −0.7419 — better than 20-day-trained ARIMA and ESM, on par with LGBM/DeepAR; performance peaks around 20 days and saturates by 22–24 days; degrades fast below 15 days (12 days: QR 83.07%).
- **Generalization**: FEDM trained on Station 1 applied unchanged to Stations 2 & 3: AR > 85%, QR > 90% (Station 2: 95.05%, WS −0.5836; Station 3: 94.53%, WS −0.6142) → limited degradation, no overfitting.
- **Computational efficiency** (i7-12700H + RTX 3060): FEDM avg **597.4 s** (<10 min, shorter than the 15-min resolution), vs LGBM 622.3 s (−4%), ESM 850.1 s (−29.7%), NBEATS 964.0 s, DeepAR 1252.1 s, TFT 1680.8 s, DeepTCN 1926.4 s.

## 💡 Limitations & Identified Research Gaps
- Single-station focus — authors flag extension to **spatio-temporal multi-station forecasting** as future work.
- Assumes future values of exogenous features (price, weather, temperature) are reliably known.
- Linear (Pearson-only) prior may miss nonlinear feature-demand relations; threshold |r| ≥ 0.1 is heuristic.
- Point-interval construction relies on Monte Carlo dropout sampling rather than full distributional modeling.
- Future work: more external features, integration into EV demand scheduling and renewable-energy complementarity applications.
- Dataset access requires request (limited reproducibility despite GitHub link).

## 📚 BibTeX & Citation Reference
```bibtex
@article{cao2024fedm,
  title   = {Feature-enhanced deep learning method for electric vehicle charging demand probabilistic forecasting of charging station},
  author  = {Cao, Tingwei and Xu, Yinliang and Liu, Guowei and Tao, Shengyu and Tang, Wenjun and Sun, Hongbin},
  journal = {Applied Energy},
  volume  = {371},
  pages   = {123751},
  year    = {2024},
  doi     = {10.1016/j.apenergy.2024.123751}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — source of GRN/GLU building blocks and TFT benchmark ([32]).
- [[2017_Attention_Is_All_You_Need]] — multi-head self-attention ([35]).
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — attention for long-term relationships in time series ([34]).
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — DeepAR benchmark and risk metric convention ([36]).
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] — NBEATS basis/benchmark ([26]).
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — ensemble probabilistic EV load forecasting ([20]).
- Vault concepts: [[FEDM]], [[GRN]], [[GLU]], [[Pinball_Loss]], [[Winkler_Score]], [[Qualified_Rate]], [[Electricity_Tariff]]

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load_refs]]
