---
type: paper
title: "Machine learning approaches to short-term electric vehicle charging demand prediction: Applicability and geographical transferability"
authors: [Shengyou Wang, Yilan Bu, Binru Wei, Enyuan Cao, Ruichen Ma, Chengxiang Zhuge]
year: 2026
journal_conference: "Journal of Energy Storage"
doi_url: "https://doi.org/10.1016/j.est.2026.122141"
models_used: ["[[SGD]]", "[[Random_Forest]]", "[[Lasso]]", "[[LSTM]]", "[[MLP]]", "[[GRU]]"]
datasets_used: ["[[Perth_EV]]", "[[Dundee_EV]]", "[[Hong_Kong_EV_Charging_Dataset]]", "[[Palo_Alto_EV]]", "[[Boulder_Colorado]]"]
features_used: ["[[Historical_Load]]", "[[Sliding_Window_Lags]]", "[[EV_Charging_Demand]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Machine learning approaches to short-term electric vehicle charging demand prediction: Applicability and geographical transferability

## 🎯 Main Objective & Contribution
- **Objective:** Benchmark six popular ML methods (three traditional ML + three deep learning) for **station-level, 1-hour-ahead** [[EV_Charging_Demand]] prediction across **12 real-world cities** in China, the UK and the USA, and examine their **geographical transferability** (can a model trained on city A predict city B with little/no local data?).
- **Contributions:**
	1. First systematic station-level comparison of ML/DL methods for short-term (hourly) EV charging demand at small temporal resolution across many scenarios (stations range 1–27 per city; 5.5–29.4 charging events/day/station).
	2. Explicit evaluation of geographical transferability via a pre-train → parameter-copy → fine-tune/test protocol (zero-shot T=0 or few-shot T≤11 h adaptation).
	3. Three key insights: (a) **simplicity over complexity** — traditional ML (esp. SGD linear regression) matched or beat DL models; (b) **data-efficiency threshold** — performance plateaus after only ~72 h (3 days) of training data; (c) **transfer without fine-tuning** — models from data-rich cities deploy well zero-/few-shot in data-scarce cities.
- Deliberately *not* a new architecture: a practical applicability/transferability benchmark.

## 🧠 Methodology & Model Architecture
### Problem formulation (Eq. 1)
$$[X_{t-p+1}, \dots, X_{t}] \xrightarrow{F(\cdot)} [X_{t+1}, \dots, X_{t+q}] \tag{1}$$
where $p$ = length of historical input series ($p=12$ h here) and $q$ = prediction length ($q=1$ h). Demand $X=(X_1,\dots,X_N)\in\mathbb{R}^{N\times n}$ counts charging events per station per hour; each station is an independent time-series regression. Sliding-window supervised format: past 12 hourly demand values → next-hour demand.

### Model selection
Systematic Web-of-Science popularity search (top highly-cited papers, elbow method on 5/10-year publication counts) → traditional ML: **[[Random_Forest|RF]]**, **[[Lasso|LASSO]]**, **[[SGD]]** (chosen instead of plain [[Linear_Regression]]); deep learning: **[[MLP]]**, **[[LSTM]]**, **[[GRU]]** (Bi-GRU variant).

### Key equations
- **Random Forest aggregation (Eq. 2):**
$$y = \sum_{i=0}^{n} \frac{1}{p} \sum_{j=1}^{p} W_j(x_i, x')\, y_i \tag{2}$$
where $W_i(x_i,x')$ is the non-negative weight of the i-th training instance relative to new point $x'$ within a tree, $p$ = number of trees.
- **LASSO optimization (Eq. 3):**
$$\min_\theta \left\{ \frac{1}{N}\|y-\theta x\|_2 \right\} \tag{3}$$
with $N$ = number of instances (L1 regularization for feature selection/shrinkage).
- **SGD weight update (Eq. 4):**
$$\theta := \theta - \eta \nabla L(\theta) \tag{4}$$
$\eta$ = learning rate; SGD trains a linear regressor (loss='squared_error', l2 penalty).
- **MLP output (Eq. 5):**
$$y = \sigma(W \cdot x + b) \tag{5}$$
σ = sigmoid activation, W = weight matrices, b = bias.
- **LSTM gating unit (Eq. 6):**
$$f_{LSTM} = \sigma(W \cdot [h, x] + b) \tag{6}$$
$h$ = previous hidden state (input/output/forget gates share this form).
- **GRU gating unit (Eq. 7):**
$$f_{GRU} = \sigma(W \cdot [h, x] + b) \tag{7}$$
GRU uses reset + update gates; fewer parameters than LSTM.
- **Metrics — MAPE (Eq. 8) & MAE (Eq. 9):**
$$MAPE(y,\hat y) = \frac{1}{N}\sum_{i}^{N} \left|\frac{y_i - \hat y_i}{y_i}\right| \times 100\% \tag{8}$$
$$MAE(y,\hat y) = \frac{1}{N}\sum_{i}^{N} |y_i - \hat y_i| \tag{9}$$

### Transferability protocol (Algorithm 1)
Input: source dataset $D_s=\{(x_i^{(s)},y_i^{(s)})\}_{i=1}^{N_s}$, target dataset $D_t$, architecture $f_\theta$, adaptation length $T\in\{0,1,2,\dots,11\}$ hours.
1. Pre-train on source city: $\theta \leftarrow \arg\min_\theta \mathcal{L}(f_\theta(X^{(s)}, y^{(s)}))$
2. Initialize target model: $\theta \leftarrow \theta_s$
3. If $T>0$ (few-shot): fine-tune $\theta^* \leftarrow \arg\min_\theta \mathcal{L}(f_\theta(X^{(t)}_{adapt}, y^{(t)}_{adapt}))$ on first T hours of target data
4. Else (zero-shot, T=0): $\theta^* \leftarrow \theta$
5. Evaluate: $\hat y^{(t)}_{test} \leftarrow f_{\theta^*}(X^{(t)}_{test})$

Cities grouped into Group-High/Medium/Low by mean daily events/station via k-means clustering.

### Experimental setup
- Split: chronological 75% train / 15% validation / 15% test; grid search on validation ([[MAE]] criterion); fixed random_state=0.
- Hyperparameters: RF (n_estimators=200, max_depth=15, min_samples_split=10, min_samples_leaf=5); LASSO (α=0.01, max_iter=10000); SGD (squared_error loss, l2 penalty, α=0.001, constant lr, max_iter=10000); MLP (3 hidden layers 128→64→32, ReLU, dropout 0.2, batch 64); LSTM (2×64 units, dropout 0.3, recurrent_dropout 0.2, batch 32); GRU (2×64 units, dropout 0.3, batch 32). DL trained with Keras/TensorFlow v2.12, [[Adam]] lr=0.001, early stopping (patience 15 epochs, min delta 1e-4, max 100 epochs); ML via scikit-learn v1.5.0. Hardware: i9-13900K, 64 GB RAM, RTX 4090, Python 3.10.

## 📊 Dataset & Input Features
- **12 public charging-session datasets (>30 days each), aggregated to hourly charging-event counts; 720 records per station over 30 days:**
	1. Perth, UK — 6 stations, 2019/7/1–30, 29.4 events/day/station ([[Perth_EV]])
	2. Hong Kong, China — 10 stations, 2022/5/17–6/15, 27.6 ([[Hong_Kong_EV_Charging_Dataset]])
	3. Dundee, UK — 27 stations, 2018/7/1–30, 25.5 ([[Dundee_EV]])
	4. Palo Alto, USA — 7 stations, 2020/11/1–30, 17.9 ([[Palo_Alto_EV]])
	5. Crieff, UK — 2 stations, 13.3; 6. Aberfeldy — 2, 13.2; 7. Pitlochry — 3, 10.8; 8. Kinross — 8, 8.4; 9. Auchterarder — 1, 6.5; 10. Blairgowrie — 1, 6.5; 11. Dunkeld — 1, 5.8 (all 2019/7/1–30)
	12. Boulder, USA — 19 stations, 2021/8/1–30, 5.5 ([[Boulder_Colorado]])
- Session fields: charger ID, start time, end time → transformed into hourly demand count series.
- **Input features:** only the past 12 h of hourly charging demand ([[Historical_Load]]) via sliding window — no exogenous weather/spatial/calendar covariates.
- **Data availability statement:** "Data will be made available on request." No direct download URLs given in the paper.

## 📈 Performance & Results
*(Results are reported in figures; exact numeric MAE/MAPE tables are not extractable from the text.)*
- **Applicability (same-city train/test):** By [[MAE]], [[LSTM]], [[GRU]], [[Random_Forest|RF]] and [[SGD]] beat [[MLP]] and [[Lasso|LASSO]]; by [[MAPE]] the three traditional ML methods (especially SGD and RF) were better. **SGD was best overall on both metrics** across the 12 cities. Group-High demand cities → lower MAPE but higher MAE; LSTM/GRU/RF/SGD best in Group-High.
- **Training-length analysis:** performance improves with training length up to **3 days (~72 h)**, then plateaus for all six models and all cities → only 3 days of session data needed for near-optimal accuracy.
- **Transferability:** DL methods ([[LSTM]], [[MLP]], [[GRU]]) tended to outperform RF/LASSO/SGD on transferred MAE (their transfer MAE even better than their applicability MAE); SGD still best overall (much smaller MAPE). Applicability generally beats transferability on MAPE, but with ≥3 days fine-tuning data transfer matches applicability on MAE. SGD's transfer performance even exceeded its applicability performance for the first 14 training lengths.
- **Statistical/qualitative conclusions:** DL does *not* necessarily beat traditional ML; simple stochastic-regularized linear models mine robust, transferable temporal patterns; zero-/few-shot deployment viable for emerging-EV markets.

## 💡 Limitations & Identified Research Gaps
- Only univariate historical-demand inputs — no spatial/urban features (distances to nearby stations, station density, land use, POIs), weather, or calendar indicators.
- Single-hour horizon only; multi-hour-ahead (1–3 h) extension needed for operational planning.
- Underlying drivers of cross-city transferability (urban structure, socioeconomic profiles, user behavior similarity) unexplained — planned investigation via city-level metadata.
- Future work: extend benchmark to emerging architectures (**Transformers**, [[TCN]]s), expand datasets, add weekday/weekend/holiday/time-of-day context features.
- Only 30 days of data per city; short windows may not capture seasonality.

## 📚 BibTeX & Citation Reference
```bibtex
@article{Wang2026MLGeographicalTransferability,
  author  = {Wang, Shengyou and Bu, Yilan and Wei, Binru and Cao, Enyuan and Ma, Ruichen and Zhuge, Chengxiang},
  title   = {Machine learning approaches to short-term electric vehicle charging demand prediction: Applicability and geographical transferability},
  journal = {Journal of Energy Storage},
  volume  = {163},
  pages   = {122141},
  year    = {2026},
  doi     = {10.1016/j.est.2026.122141}
}
```
Affiliations: People's Public Security University of China (Beijing); PolyU Shenzhen Technology & Innovation Research Institute (Futian); UCL Bartlett CAS; Zhejiang University IBS; The Hong Kong Polytechnic University. Funding: NSFC 72501286 & 52002345, Shenzhen S&T Commission JCYJ20230807140401003, HKSAR Public Policy Research 2023.A6.232.23B, RISUD 1-BBWR, Smart Cities RI Q-CDB9. Received 17 May 2025; revised 18 Mar 2026; accepted 4 Apr 2026.

## 🔗 Key References & Citation Graph
- [[2019_Zhu_EV_Load_Forecasting]] — cited ([44]) as key comparative DL study of EV charging load forecasting ([[LSTM]], [[GRU]], etc.)
- [[1997_Hochreiter_Long_Short_Term_Memory]] — cited ([86]) as the original [[LSTM]] reference
- [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] — related vault work on transfer learning for EV load forecasting (cross-site knowledge transfer)
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] — related vault work on meta-learning/few-shot adaptation for EV load
- [[2023_Huang_MetaProbformer_EV_Load]] — related vault work on adapting forecasting models to unseen environments
- [[2025_Meyer_Benchmark_Foundation_Models]] — related vault benchmarking study of forecasting models on EV/home charging demand
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — TCN baseline family the authors plan to add in future benchmarks
- External key citations (not yet in vault): Amara-Ouali et al. 2022 day-ahead EV load/occupancy benchmark (ACM e-Energy, doi:10.1145/3538637.3538850); Ma & Faye 2022 Dundee hybrid LSTM occupancy (Energy 244:123217); Wang et al. 2023 HST-GCN short-term prediction (Appl. Energy 340:121032); Breiman 2001 Random Forests; Tibshirani 1996 LASSO; Cho et al. 2014 GRU (arXiv:1409.1259)
