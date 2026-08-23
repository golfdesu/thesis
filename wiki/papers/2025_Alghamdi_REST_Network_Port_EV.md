---
type: paper
title: "REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains"
authors: [Elham Abdullah Alghamdi, Monagi Hassan Alkinani, Abdulwahab Ali Almazroi, Mohammed Alqarni, Eman Ali Aldhahri, Nasir Ayub]
year: 2025
journal_conference: "IEEE Access"
doi_url: "https://doi.org/10.1109/ACCESS.2025.3589292"
models_used: ["[[RESTNet]]", "[[ResNet]]", "[[SENet]]", "[[Transformer]]", "[[DeepSigRNet]]", "[[CNN]]", "[[VGGNet]]", "[[SVR]]", "[[Random_Forest]]"]
datasets_used: ["[[EV_Intelligent_Port_Logistics_Dataset]]", "[[Kaggle_Dallas_Port]]"]
features_used: ["[[Historical_Charging_Load]]", "[[Charging_Duration]]", "[[Battery_Capacity]]", "[[Grid_Demand]]", "[[Fleet_Size]]", "[[Charger_Power_Rating]]", "[[Electricity_Price]]", "[[Weather]]", "[[Calendar_Features]]", "[[Hourly_Demand_Variation]]", "[[Cyclic_Temporal_Indicator]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[MAPE]]", "[[RMSE]]", "[[MAE]]", "[[R2]]", "[[EEE]]", "[[LVD]]", "[[CPE]]", "[[TAA]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains

## 🎯 Main Objective & Contribution
- Forecast EV charging load for logistics fleets at **artificial (smart) ports**, where charging patterns are highly variable, nonlinear, and imbalanced (over-representation of peak-hour usage) — settings where linear regression/ARIMA/smoothing baselines fail.
- Contributions:
  1. **[[RESTNet]]** ensemble: [[ResNet]] (deep spatial pattern extraction via skip connections) + [[SENet]] (channel-wise squeeze-and-excitation attention) + [[Transformer]] (multi-head self-attention for long-range temporal dependencies), combined by weighted averaging.
  2. **Proportional Synthetic Sampling ([[PSS]])** with Contextual Feature Synthesis (CFS) to balance under-represented load classes.
  3. **Dual-Stage Relevance Selector ([[DSRS]])**: filter stage (Statistical Dependency Coefficient, SDC) + wrapper stage (Model-Driven Feature Importance, MDFI) + Interaction Influence Index (III).
  4. Custom operational metrics: Energy Efficiency Error (EEE), Load Variability Deviation (LVD), Cost of Prediction Error (CPE), Time-Aware Accuracy (TAA).

## 🧠 Methodology & Model Architecture
- Pipeline (Algorithm 1): preprocessing → DSRS feature selection + PSS balancing → train ResNet/SENet/Transformer submodules → weighted-average ensemble → validation/tuning on MAPE/RMSE/EEE. Hyperparameters: lr=0.001, batch=64, epochs=100; i7 CPU/32 GB RAM/4 GB GPU workstation.
- Preprocessing equations:
  - "Weighted interpolation" for missing values:
    $$ K_q = \frac{E_{q-1} \cdot K_{q-1} + E_{q+1} \cdot K_{q+1}}{E_{q-1} + E_{q+1}} $$
    (rolling window ±2 steps, inverse-distance weights; outliers |z| > 3 removed/imputed).
  - "Log normalization": $W' = \log(W+1)$; target scaling ("target log scaling"): $L_{scaled} = \log(L+1)$.
  - "Binary target encoding": $C_{encoded} = \frac{1}{m}\sum_{j=1}^{m} L_j \ \text{if } C = c$.
  - "Interaction feature": $I = B \times D$ (fleet size × battery capacity).
- PSS balancing — class ratio ("class proportion"):
  $$ R_j = \frac{M_j}{M_{total}}, \quad j = 1,\ldots,m $$
  synthetic-sample count ("synthetic sample count"):
  $$ T_j = \left(\frac{Q \times M_{total}}{M_j}\right) - M_j \quad \text{for } R_j < Q $$
  CFS synthesis ("contextual feature synthesis"):
  $$ Y_{new} = Y_k + \delta_k \cdot mean(N_k), \quad k=1,\ldots,T_j $$
  ($\delta_k$ small normal-distribution perturbation over nearest neighbors $N_k$).
- DSRS — filter metric ("statistical dependency coefficient"):
  $$ SDC(F_i, L) = \frac{Cov(F_i, L)}{\sigma_{F_i}\cdot\sigma_L}, \qquad \text{drop if } SDC(F_i,L) < \alpha $$
  wrapper importance ("model-driven feature importance"):
  $$ I(F_j) = E(M_{\neg F_j}) - E(M), \qquad \text{drop if } I(F_j) < \beta $$
  interaction preservation ("interaction influence index"):
  $$ III(F_p, F_q) = \frac{Cov(F_p \cdot F_q, L)}{\sigma_{F_p \cdot F_q}\cdot\sigma_L} $$
- Feature engineering: Hourly Demand Variation ("HDV") $HDV_t = L_t - \frac{1}{n}\sum_i L_i$; Battery Efficiency Ratio ("BER") $BER_t = \frac{\text{Avg\_Battery\_Capacity}_{kWh}}{L_t}$; Distance-to-Station Factor ("DSF") $DSF_j = \frac{1}{1+Distance_j}$; Load Consistency Index ("LCI") $LCI_t = 1 - \frac{\sigma(L_{t-w},\ldots,L_t)}{L_t}$; Seasonal Demand Index ("SDI") $SDI_t = \frac{L_t - \mu_{season}}{\sigma_{season}}$; Aggregate Charging Duration ("ACD") $ACD_t = \sum_{i=t-w}^{t} Charging\_Duration_i$.
- Attribute modification: Adaptive Scaling Technique ("AST") $AST_\alpha = \frac{Y_\alpha - \nu}{\tau + \delta}$; Temporal Rate Calculation ("TRC") $TRC_\beta = Z_\beta - Z_{\beta-1}$; Combined Interaction Metric ("CIM") $CIM_{pq} = \frac{Y_p \cdot Y_q}{\sum_r(Y_r^2+\delta)}$; Cyclic Temporal Indicator ("CTI") $CTI_\gamma = (\sin\frac{2\pi\gamma}{T_{day}}, \cos\frac{2\pi\gamma}{T_{day}})$, $T_{day}=24$.
- Regression head and training:
  - "REST network output":
    $$ \hat{y}_t = f_{REST}(X_t) = W_{out}\cdot z_t + b_{out} $$
  - "Gradient update (Aquila optimizer)":
    $$ \theta_{t+1} = \theta_t - \eta\cdot\nabla_\theta L(\theta_t) $$
  - "MSE loss":
    $$ L_{MSE} = \frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y}_i)^2 $$
- Custom metrics ("EEE / LVD / CPE / TAA"):
  $$ EEE = \frac{1}{m}\sum_{k=1}^{m}\left(\frac{(o_k-\hat{o}_k)^2}{o_k\times\hat{o}_k}\right), \quad LVD = \frac{1}{n}\sum_{i=1}^{n}|\sigma_{y_i}-\sigma_{\hat{y}_i}| $$
  $$ CPE = \frac{1}{n}\sum_{i=1}^{n}(\lambda_u\times max(0,y_i-\hat{y}_i)+\lambda_o\times max(0,\hat{y}_i-y_i)), \quad TAA = \frac{1}{n}\sum_{i=1}^{n}(w_i\times|y_i-\hat{y}_i|) $$

## 📊 Dataset & Input Features
- **Dataset**: EV intelligent port logistics dataset, Dallas, Texas — **65,736 hourly data points** covering January 2017–June 2024 (abstract states Jan 2020–Jun 2024; Section III-A states Jan 2017). Target: hourly EV fleet charging load (kW); deliberately imbalanced to mirror real operations.
- **Features** (Table 2): calendar (timestamp, weekday, holiday, time-of-day); fleet (fleet size, vehicle types incl. light-duty/heavy-duty split, average battery capacity); infrastructure (number of charging stations, power rating, efficiency); operations (distance driven, average speed, loading/unloading times); environment (temperature, humidity, precipitation); historical loads/durations; grid/economic (electricity cost, grid demand, government incentives); behavior (day vs night preference, high/medium/low usage class).
- **SHAP analysis**: historical charging loads, charging duration, battery capacity, and local grid demand are the top features; then fleet size, charger power rating, electricity price.
- **Data availability**: dataset published on Kaggle [25] — https://doi.org/10.34740/KAGGLE/DSV/9490653

## 📈 Performance & Results
- Headline results: **MAPE = 6.5%, RMSE = 9.8 kW**, EEE = 3.2%, LVD = 4.1%, CPE = \$12.50, TAA = 92.3%.
- Benchmarks (Tables 3–4): outperforms [[SVR]], [[Random_Forest]], [[CNN]], [[VGGNet]], [[DeepSigRNet]] across MAPE/RMSE/MAE/R² and custom metrics (exact per-baseline numbers in table images not machine-readable in the text extraction).
- Statistical tests: ANOVA F=5.67 (p=0.004); Pearson correlation 0.89 (p=0.0001); Student's t=3.12 (p=0.002); Kendall's τ=0.82, Spearman's ρ=0.86; Wilcoxon signed-rank statistic 3.45 (p=0.004); chi-square-like grouped test 7.23 (p=0.009).
- Efficiency (Table 5): highest relative efficiency score (**99%**), training time **210 s**, inference **33 ms**, model size **20 MB** (vs 45–55 MB for VGGNet/CNN/DeepSigRNet) — suitable for edge deployment. Accuracy/loss curves rise from ~70%/0.70 to ~99%/0.29 over 20 epochs without overfitting.

## 💡 Limitations & Identified Research Gaps
- Future work: incorporate real-time sensor feedback streams, external energy-market signals, adaptive learning mechanisms; scale to smart-city ecosystems and decentralized energy systems.
- Dataset is a single-location Kaggle set for port logistics fleets (not public charging stations); key result tables only available as images, limiting reproducibility of baseline comparisons.

## 📚 BibTeX & Citation Reference
```bibtex
@article{alghamdi2025rest,
  title   = {REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains},
  author  = {Alghamdi, Elham Abdullah and Alkinani, Monagi Hassan and Almazroi, Abdulwahab Ali and Alqarni, Mohammed and Aldhahri, Eman Ali and Ayub, Nasir},
  journal = {IEEE Access},
  volume  = {13},
  pages   = {133128--133144},
  year    = {2025},
  doi     = {10.1109/ACCESS.2025.3589292}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — Transformer/self-attention backbone
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — convolutional sequence-modeling context
- Related vault papers: [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]], [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]], [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]], [[2020_Huang_Ensemble_EV_Load]], [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]]
