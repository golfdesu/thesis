---
type: paper
title: "Enhanced Transformer-BiLSTM Deep Learning Framework for Day-Ahead Energy Price Forecasting"
authors: [Abdullah Al Ahad Khan, Md Habib Ullah, Ruchira Tabassum, Md Faisal Kabir]
year: 2025
journal_conference: "IEEE Transactions on Industry Applications, vol. 62, no. 2, pp. 1933-1947 (Mar/Apr 2026 issue)"
doi_url: "https://doi.org/10.1109/TIA.2025.3599812"
models_used: ["[[Transformer_BiLSTM]]", "[[Transformer]]", "[[BiLSTM]]", "[[XGBoost]]", "[[GRU]]", "[[CNN]]", "[[CNN_LSTM]]", "[[LSTM]]"]
datasets_used: ["[[NYISO]]", "[[PJM_Energy_Market_Dataset]]", "[[MISO_Market_Dataset]]"]
features_used: ["[[Historical_Zonal_Price]]", "[[Lag_Features]]", "[[Positional_Encoding]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MAPE]]", "[[sMAPE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Enhanced Transformer-BiLSTM Deep Learning Framework for Day-Ahead Energy Price Forecasting

## 🎯 Main Objective & Contribution
- Hybrid deep learning framework for **day-ahead electricity price forecasting (DA EPF)** to support strategic bidding by market participants, generation companies, and network operators — relevant for EV aggregators in deregulated DA markets.
- Contributions:
  - **Transformer-BiLSTM hybrid**: Transformer multi-head self-attention captures long-range/parallel sequence patterns; BiLSTM adds bidirectional past+future temporal context.
  - Uses **only historical price data** (no load/weather/generation covariates), robust to raw datasets containing outliers — unlike prior work requiring extensive auxiliary features and preprocessing.
  - Outperforms XGBoost, LSTM, BiLSTM, GRU, CNN, CNN-LSTM, CNN-BiLSTM, Transformer on NYISO; generalizes to PJM and MISO markets.
  - Time-series decomposition analysis of prices into trend/seasonal/residual components to guide model selection.

## 🧠 Methodology & Model Architecture
- **Pipeline**: hourly LBMP data → missing-value imputation $x_t = \frac{x_{t-1}+x_{t+1}}{2}$ → [[Min_Max_Scaling]] $x' = \frac{x - X_{\min}}{X_{\max} - X_{\min}}$ → sliding-window feature/target pairs ($X_t = D(t-1:t-T_{lag})$, target next $T$ hours) → positional encoding → Transformer encoder (LayerNorm → Multi-Head Attention → Dropout(0.1) → LayerNorm → Dense ReLU → Dropout) → BiLSTM (64 units per direction, 128 concatenated features) → Dense 128 + ReLU → Dropout 0.1 → Dense with linear activation ($T$ outputs).
- **Hyperparameters**: $T_{lag} = 60$ h lookback, learning rate 0.001, batch size 32, 4 attention heads × 64-dim attention spaces, layer norm ϵ = 10⁻⁶, ~50 epochs (convergence ≈ 20 epochs). Direct multi-horizon models trained separately for T = 1, 6, 12, 24, 48 h.
- **Key Equations**:
  - **Eq. (1) — Query/Key/Value projections** from input matrix $X \in \mathbb{R}^{n \times d_{model}}$:
    $$ Q = XW_Q, \quad K = XW_K, \quad V = XW_V, \quad W_Q, W_K, W_V \in \mathbb{R}^{d_{model} \times d_k}. $$
  - **Eqs. (2)–(3) — Positional encoding** (position $p$, embedding dimension $i$):
    $$ PE_{(p,2i)} = \sin\!\left(\frac{p}{10000^{2i/d_{model}}}\right), \qquad PE_{(p,2i+1)} = \cos\!\left(\frac{p}{10000^{2i/d_{model}}}\right). $$
  - **Eq. (4) — Scaled dot-product attention**:
    $$ \text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V. $$
  - **Eq. (5) — Multi-head attention**:
    $$ \text{MultiHead}(Q,K,V) = \text{Concat}(head_1,\ldots,head_N)W^o. $$
  - **Eq. (6) — Per-head projection**:
    $$ head_i = \text{Attention}(QW_i^Q,\, KW_i^K,\, VW_i^V). $$
  - **Eq. (7) — Position-wise feedforward network**:
    $$ \text{FFN}(x) = \text{ReLU}(xW_1+b_1)W_2+b_2. $$
  - **Eq. (8) — Layer normalization**:
    $$ \text{LN}(x) = \gamma\left(\frac{x-\mu}{\sqrt{\alpha^2+\epsilon}}\right)+\beta. $$
  - **Eqs. (9)–(14) — LSTM cell gates**:
    $$ f_t = \sigma(W_f\cdot[h_{t-1},x_t]+b_f), \qquad i_t = \sigma(W_i\cdot[h_{t-1},x_t]+b_i), $$
    $$ \tilde{C}_t = \tanh(W_i\cdot[h_{t-1},x_t]+b_C), \qquad C_t = f_t\odot C_{t-1} + i_t\odot\tilde{C}_t, $$
    $$ o_t = \sigma(W_o\cdot[h_{t-1},x_t]+b_o), \qquad h_t = o_t\odot\tanh(C_t). $$
  - **Eqs. (15)–(17) — Bidirectional hidden states & concatenation**:
    $$ \overrightarrow{h}_t = \text{LSTM}(x_t,\overrightarrow{h}_{t-1},\overrightarrow{C}_{t-1}), \qquad \overleftarrow{h}_t = \text{LSTM}(x_t,\overleftarrow{h}_{t+1},\overleftarrow{C}_{t+1}), \qquad h_t = [\overrightarrow{h}_t;\overleftarrow{h}_t]. $$
  - **Eq. (18) — BiLSTM output**:
    $$ o_t = W_{\overrightarrow{h}_t}\overrightarrow{h}_t + W_{\overleftarrow{h}_t}\overleftarrow{h}_t + b_o. $$
  - **Metrics Eqs. (19)–(24)**:
    $$ \text{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i-\hat{y}_i|, \quad \text{RMSE} = \sqrt{\tfrac{1}{n}\sum(y_i-\hat{y}_i)^2}, \quad \text{MAPE} = \frac{100\%}{n}\sum\left|\frac{y_i-\hat{y}_i}{y_i}\right|, $$
    $$ \text{sMAPE} = \frac{100\%}{n}\sum\frac{|y_i-\hat{y}_i|}{(|y_i|+|\hat{y}_i|)/2}, \quad R^2 = 1-\frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}, \quad \bar{y}=\tfrac{1}{n}\sum y_i. $$
- **Environment**: Google Colab, Tesla T4 GPU, 12.7 GB RAM, Python 3.11, TensorFlow/Keras + scikit-learn; MATLAB visualizations.

## 📊 Dataset & Input Features
- **NYISO zonal LBMP** (primary): hourly day-ahead Locational Based Marginal Pricing, **CAPITL zone**, **2016–2023** (~8 years); train 2016–2022, test 2023. Single attribute "Price" at 1-hour sampling.
  - Data available: https://data.mendeley.com/datasets/s54n4tyyz4/2 ; source portal: https://www.nyiso.com/energy-market-operational-data
- **PJM market** hourly prices: https://www.pjm.com/markets-and-operations/energy
- **MISO market** hourly prices: https://www.misoenergy.org/markets-and-operations/real-time--market-data/market-reports/
- **Features**: only past $T_{lag}=60$ hours of price data (sliding window); positional encoding supplies sequence order. No exogenous variables (load, weather, renewables).
- Time-series decomposition revealed yearly recurring seasonal pattern with variable magnitude (2016 and 2023 exceptionally high early/late values).

## 📈 Performance & Results
- **NYISO CAPITL, 2023 test set (Table I)**:
  | Model | MAE ($/MWh) | RMSE ($/MWh) | sMAPE (%) | MAPE (%) | R² |
  |---|---|---|---|---|---|
  | **Transformer-BiLSTM (proposed)** | **2.7818** | **6.4937** | **6.6060** | **6.3741** | **0.9393** |
  | BiLSTM | 3.1027 | 6.7663 | 7.4780 | 8.3563 | 0.9381 |
  | XGBoost | 3.1634 | 7.7484 | 7.1422 | 7.7925 | 0.9119 |
  | Transformer | 3.3511 | 7.3436 | 8.2084 | 7.5236 | 0.9223 |
  | CNN-LSTM | 3.3455 | 7.1131 | 8.3043 | 8.0200 | 0.9247 |
  | GRU | 3.5310 | 7.4869 | 8.2806 | 7.1245 | 0.9194 |
  | CNN | 6.8251 | 13.2971 | 17.0186 | 18.8426 | 0.7455 |
  - Gains vs Transformer: −16.98% MAE, −11.6% RMSE, −19.5% sMAPE, −15.3% MAPE, +1.8% R²; vs BiLSTM: −10.3% MAE; vs XGBoost: −12.0% MAE, −16.2% RMSE.
- **Cross-market generalization (Table IV)**: PJM MAE 1.9291 / RMSE 3.57 / sMAPE 6.1209% / R² 0.9396; MISO MAE 1.5543 / RMSE 2.4607 / sMAPE 5.6742% / R² 0.9280 (lower volatility than NYISO).
- **Literature comparison (Table III)**: lowest MAE/RMSE vs outlier-adaptive non-crossing quantile regression [47], weighted kNN + Gaussian process [3], SSA-DELM [48].
- **Horizon study (Fig. 12f)**: best at T=1h (MAE 2.7818), stable up to 24h, degraded at 48h.
- **Error structure**: weekly MAE mostly < $5/MWh (max $18.122 in first week of February; min $1.029 in August); worst month February (MAE $6.65, RMSE $16.63), best August (MAE $1.32, RMSE $2.14); winter MAE $4.17/RMSE $10.98 vs fall $2.16/$3.58; high-price quantile (> $35.96/MWh) MAE $5.48/RMSE $10.88 vs low-quantile $1.16/$1.60; residuals right-skewed with systematic underestimation above $200/MWh.
- **Efficiency (Table II)**: highest training time among compared models but competitive inference speed (1.72 s).
- **Sensitivity (Figs. 14–15)**: performance improves with 80–140 transformer units and 4–8 attention heads; >100 LSTM units gives diminishing returns; optimal LR 0.001 / batch 32.

## 💡 Limitations & Identified Research Gaps
- Degrades on extreme price spikes/outliers (February/July spikes, prices > $200/MWh systematically underestimated) — no explicit spike-handling mechanism.
- Univariate design ignores load forecasts, weather, generation mix/renewables, and other market covariates that could improve accuracy in volatile periods.
- Highest training time of the compared models; computational cost needs optimization.
- Stated future work: LIME/SHAP explainability; decomposition preprocessing (FFT, wavelet, VMD, CEEMDAN); multivariate inputs; reduced training/inference time.

## 📚 BibTeX & Citation Reference
```bibtex
@article{khan2025transformer,
  title   = {Enhanced Transformer-BiLSTM Deep Learning Framework for Day-Ahead Energy Price Forecasting},
  author  = {Khan, Abdullah Al Ahad and Ullah, Md Habib and Tabassum, Ruchira and Kabir, Md Faisal},
  journal = {IEEE Transactions on Industry Applications},
  volume  = {62},
  number  = {2},
  pages   = {1933--1947},
  year    = {2025},
  doi     = {10.1109/TIA.2025.3599812}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — Vaswani et al., original Transformer architecture (ref. [32])
- Khan et al., IEEE Kansas Power & Energy Conf. 2024, doi:10.1109/KPEC61529.2024.10676111 — conference precursor of this framework (ref. [1])
- NYISO energy market & operational data — https://www.nyiso.com/energy-market-operational-data (ref. [45])
- PJM energy market — https://www.pjm.com/markets-and-operations/energy (ref. [49]); MISO market reports — https://www.misoenergy.org/markets-and-operations/real-time--market-data/market-reports/ (ref. [50])
- Mendeley replication dataset — https://data.mendeley.com/datasets/s54n4tyyz4/2

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_Khan_Transformer_BiLSTM_Price_Forecasting_refs]]
