---
type: paper
title: "Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events"
authors: [Di Cao, Junbo Zhao, Weihao Hu, Yingchen Zhang, Qishu Liao, Zhe Chen, Frede Blaabjerg]
year: 2022
journal_conference: "IEEE Transactions on Industrial Informatics, 18(2), 1142-1153"
doi_url: "https://doi.org/10.1109/TII.2021.3081531"
models_used: ["[[Deep_Gaussian_Process]]", "[[Sparse_GP]]", "[[VAE_DGP]]", "[[SVR]]", "[[BPNN]]"]
datasets_used: ["[[COVID19_US_City_Load]]", "[[Weather]]", "Google/Apple Mobility Data"]
features_used: ["[[Historical_Load|Past 24h load (Italy case)]]", "[[Temperature]]", "[[Humidity]]", "[[Cloud_Cover]]", "[[Precipitation]]", "[[Air_Pressure]]", "Timing features (month/day/hour index, weekday/holiday)", "[[Google_Mobility_Index|Google mobility: parks, workplaces, residential, retail & recreation, grocery & pharmacy]]", "[[Apple_Mobility_Index|Apple mobility: walking, driving, transit]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[MAPE]]", "[[Pinball_Loss]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events

## 🎯 Main Objective & Contribution
- Casts load forecasting at the **onset of anomalous events** (COVID-19 lockdowns) as a **regression problem with limited training samples**, solved by an enhanced **double stochastic variational inference [[Deep_Gaussian_Process]] (DGP)**.
- Motivation: during COVID-19 the Northern Italy day-ahead MAPE of the system operator rose 61% (max MAPE +40%); mean absolute error grew from 329.5 to 428.2 MW (+30%) vs. 2019; French operator's adaptive-model MAPE was 5× normal during lockdown.
- Contributions: (1) DGP with "self-tuning" covariance via hierarchical input-space warping — no manual kernel design, works with only days of data; (2) full uncertainty quantification enabling uncertainty-aware operations; (3) benchmarks on city-level and country-level datasets vs SVR/BPNN/SGP/VAE-DGP.

## 🧠 Methodology & Model Architecture
**Equations (1)–(3) — GP prior with homoscedastic Gaussian noise:**
$$f(X) \sim \mathcal{GP}(m(X), K(X,X')), \qquad Y = f(X) + \epsilon,\; \epsilon \sim \mathcal{N}(0,\sigma_n^2 I), \qquad Y \sim \mathcal{GP}(m(X), K(X,X')+\sigma_n^2 I)$$

**Equation (5) — joint distribution of training outputs $Y$ and test latent $f_*$:**
$$\begin{bmatrix} Y \\ f_* \end{bmatrix} \sim \mathcal{N}\left(0, \begin{bmatrix} K(X,X)+\sigma_n^2 I_n & K(X,x_*) \\ K(x_*,X) & K(x_*,x_*) \end{bmatrix}\right)$$

**Equations (7)–(8) — GP posterior predictive mean and covariance:**
$$\bar{f}_* = k(x_*,x)^T(K+\sigma^2 I)^{-1}y$$
$$\text{cov}(f_*) = k(x_*,x_*) - k(x_*,x)^T(K+\sigma^2 I)^{-1}k(x_*,x_*)$$

**Equation (9) — RBF kernel:** $k(x,x') = \sigma_f^2 \exp\left(-\tfrac{1}{2}(x-x')^T M^{-1}(x-x')\right)$ with $M=\text{diag}(l^2)$; hyperparameters $\theta=\{M,\sigma_f^2,\sigma^2\}$ optimized by maximizing marginal likelihood (Eq. 10): $\hat{\theta} = \arg\max_\theta p(D|\theta)$.

**Equations (11)–(13) — Sparse GP with $M$ inducing points $Z$, $U$** reducing complexity from $O(N^3)$ to $O(NM^2)$:
$$p(f,u|X,Z)=\mathcal{N}([f,u]|[0,0],K([X,Z],[X,Z])), \quad p(u|Z)=\mathcal{N}(u|0,K(Z,Z)), \quad p(f|u;X,Z)=\mathcal{N}(f|K_{nm}K_{mm}^{-1}u,\; K_{nn}-K_{nm}K_{mm}^{-1}K_{mn})$$

**Equation (14)/(16) — variational lower bound:** $\ell = \mathbb{E}_{q(f,U)}\left[\log \frac{p(y,f,U)}{q(f,U)}\right]$, simplified to $\log p(y) \ge \sum_{i=1}^{N}\mathbb{E}_{q(f_i)}[\log p(y_i|f_i)] - KL(q(u)\|p(u))$.

**DGP (depth $L$, stacked SGPs):**
- Eq. 17 — joint density $p(Y,\{F^l,U^l\}_{l=1}^L)=\prod_i p(y_i|f_i^L)\prod_{l=1}^L p(F^l|U^l;F^{l-1},Z^{l-1})p(U^l;Z^{l-1})$, $F^0=X$.
- Eq. 20 — layer marginal $q(F^l;F^{l-1},Z^{l-1})=\mathcal{N}(F^l|K_{nm}^l K_{mm}^{l-1}U^l,\; K_{nn}^l+K_{nm}^l K_{mm}^{l-1}(\Sigma^l-K_{mm}^l)K_{mm}^{l-1}K_{mn}^l)$.
- Eq. 23 — ELBO: $\ell_{\text{DGP}} = \sum_{i=1}^{N}\mathbb{E}_{q(f_i^L)}[\log p(y_n|f_n^L)] - \sum_{l=1}^{L}KL(q(U^l)\|p(U^l))$.
- Eq. 25 — reparameterized layer sampling: $\hat{f}_i^l = m_{\mu^l,Z^{l-1}}(\hat{f}_i^{l-1}) + \xi_i^l \odot \sqrt{S_{\Sigma^l,Z^{l-1}}(\hat{f}_i^{l-1},\hat{f}_i^{l-1})},\; \xi_i^l\sim\mathcal{N}(0,I)$ ("double stochasticity": posterior samples + data subsampling).
- Eq. 27 — test distribution $q(f_*^L)=\frac{1}{S}\sum_{s=1}^S q(f_*^L; f_{*(s)}^{L-1}, Z^{L-1})$.
- Eq. 28 — confidence interval: $c^- = \bar{s}-t(\alpha/2,n-1)\cdot\frac{\sigma}{\sqrt{n}},\; \bar{c} = \bar{s}+t(\alpha/2,n-1)\cdot\frac{\sigma}{\sqrt{n}}$.

**Metrics:**
- Eq. 29 — $\text{MAPE} = \frac{100\%}{n}\sum_{i=1}^n\left|\frac{\hat{y}_{i,p=50}-y_i}{y_i}\right|$.
- Eq. 30 — Pinball loss: $\text{Pinball}(\hat{y}_{i,q},y_i,q) = \begin{cases}(y_i-\hat{y}_{i,q})q, & \hat{y}_{i,q}<y_i \\ (\hat{y}_{i,q}-y_i)(1-q), & \hat{y}_{i,q}>y_i\end{cases}$ summed over $q=0.01,\dots,0.99$.

Implemented in Python/TensorFlow + GPyFlow on Intel Xeon E5-2630.

## 📊 Dataset & Input Features
- **US metropolitan hourly load** (Boston, Seattle, Chicago, Philadelphia), Feb 15 – May 15, 2020, hourly resolution; **46-dimensional features**: timing indices (month/day/hour, weekday/holiday), weather (temperature, humidity, cloud cover, precipitation, air pressure), and 6 Google + 3 Apple mobility metrics.
- **Country-level hourly load** (Germany, France), same period; concatenated multi-city weather/mobility → **60 features per instance**.
- **Northern Italy** hourly electrical load (strong COVID demand drops after Mar 9, 2020 total lockdown); input = historical load of past 24 h.
- Data availability / source links found in text:
  - Main city/country dataset [29]: https://github.com/chennnnnyize/Load-Forecasting-During-COVID-19 (publicly available)
  - Northern Italy load [3]: ENTSO-E Transparency Platform https://transparency.entsoe.eu
  - IEA COVID-19 impact on electricity [2]: https://www.iea.org/reports/covid-19-impact-on-electricity
  - IEEE PES COVID-19 whitepaper [1]: https://resourcecenter.ieee-pes.org/publications/whitepapers/PES_TP_COVID19_050120.html
  - France lockdown adaptive forecasting [4]: https://arxiv.org/pdf/2009.06527
- Splits: small-scale test — train May 7–9, val May 10–12, test May 13–15, 2020 (3 days training); middle-scale — train Feb 15–Apr 29, val May 2–8, test May 9–15, 2020 (~75 days). Italy: train Apr 20–22 / Jan 11–Mar 25 variants.

## 📈 Performance & Results
- **Small-scale (3 days training)**: proposed DGP best in most cases; beats one-layer [[Sparse_GP]] in 5/6 regions and both [[SVR]] and [[VAE_DGP]]; parametric [[BPNN]] overfits severely (large validation/test gaps). Max MAPE reduction vs other methods: **70.9%**.
- **Middle-scale (~75 days)**: outperforms SVR/BPNN/VAE-DGP in all cases and SGP in 5 cases; max MAPE reduction **50.7%**.
- **Probabilistic**: Pinball loss up to **46.6%** (small-scale) and **39.7%** (middle-scale) lower than SGP/VAE-DGP; at least 23.0% lower than SGP/VAE-DGP with more data. The proposed 95% CI covers almost all actual loads where SGP/VAE-DGP miss large stretches (Seattle t=50–70 etc.); peak/valley values well predicted; density curves appropriately less steep (conservative under high uncertainty).
- **Northern Italy**: lowest error in both small- and middle-scale tests; max MAPE reductions **70.1%** and **80.7%** respectively.
- Note: Tables I–VI are figures in the extracted text; per-region numbers above are those reported in prose/conclusion.

## 💡 Limitations & Identified Research Gaps
- Gaussian posterior assumption per layer partially relaxed only by sampling; still GP-based (kernel stationarity assumptions).
- Demonstrated on aggregate zonal/city load, not EV charging stations; authors state future work targets other low-data power-system applications.
- Mobility features are pandemic-specific proxies — analog for EV would be e.g. traffic/events data for new or disrupted charging stations.
- Gap for thesis: nonparametric few-shot probabilistic forecasting is directly transferable to newly commissioned [[EV_Charging_Station]] load prediction (compare with [[2023_MetaProbformer_EV_Load]]).

## 📚 BibTeX & Citation Reference
```bibtex
@article{cao2022robustdgp,
  title   = {Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events},
  author  = {Cao, Di and Zhao, Junbo and Hu, Weihao and Zhang, Yingchen and Liao, Qishu and Chen, Zhe and Blaabjerg, Frede},
  journal = {IEEE Transactions on Industrial Informatics},
  volume  = {18},
  number  = {2},
  pages   = {1142--1153},
  year    = {2022},
  doi     = {10.1109/TII.2021.3081531}
}
```

## 🔗 Key References & Citation Graph
- [[2013_Gaussian_Processes_Time_Series]]
- [[2017_QRA_Sister_Forecasts_Probabilistic_Load]]
- [[1997_Long_Short_Term_Memory]] ([[LSTM]] baseline family)
- [[2001_Neural_Networks_STLF_Review]]
- [[2019_Deep_Probabilistic_Scheduling_Power_Markets]]
- [[2020_DeepAR_Probabilistic_Forecasting]]
- [[2023_MetaProbformer_EV_Load]] (alternative few-shot probabilistic approach)

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2022_Robust_Deep_Gaussian_Process_Load_refs]]
