---
type: paper
title: "Unified Training of Universal Time Series Forecasting Transformers"
authors: ["Gerald Woo", "Chenghao Liu", "Akshat Kumar", "Caiming Xiong", "Silvio Savarese", "Doyen Sahoo"]
year: 2024
journal_conference: "Proceedings of the 41st International Conference on Machine Learning (ICML 2024)"
doi_url: "https://arxiv.org/abs/2402.02592"
models_used: ["[[Moirai]]", "[[Transformer]]", "[[PatchTST]]", "[[TimesFM]]", "[[TiDE]]", "[[TFT]]", "[[DeepAR]]", "[[DLinear]]", "[[FEDformer]]", "[[Autoformer]]", "[[Informer]]", "[[TimesNet]]", "[[iTransformer]]", "[[Lag-Llama]]"]
datasets_used: ["[[LOTSA]]", "[[BuildingsBench]]", "[[ClimateLearn]]", "[[LargeST]]", "[[LibCity]]", "[[Monash_Archive]]", "[[ProEnFo]]", "[[SubseasonalClimateUSA]]", "[[Electricity_ECL]]", "[[Solar_Dataset]]", "[[Weather]]", "[[M4]]", "[[KDD_Cup_2022]]"]
features_used: ["[[Historical_Load]]", "[[Dynamic_Covariates]]", "[[Time_Encoding]]", "[[Variate_Identifier]]"]
forecasting_horizon: ["[[Short_Term_Forecasting]]", "[[Long_Term_Forecasting]]"]
metrics: ["[[CRPS]]", "[[MSIS]]", "[[MAE]]", "[[MSE]]", "[[WQL]]"]
tags:
  - paper
  - time-series-foundation-model
  - transformer
  - universal-forecasting
  - lotsa
  - icml-2024
  - salesforce
---

# Summary: Unified Training of Universal Time Series Forecasting Transformers

## 🎯 Main Objective & Contribution
- **Core Problem Addressed**: Deep learning for time series forecasting has traditionally operated in an isolated "one-model-per-dataset" paradigm, lacking universal foundation models capable of zero-shot transfer across diverse domains, frequencies, and dimensionalities. Existing architectures fail because of three fundamental bottlenecks:
  1. *Cross-Frequency Learning*: Time series span frequencies from yearly to sub-second; a single fixed patch size causes mismatch between high-frequency fine details and low-frequency macro trends.
  2. *Any-Variate Dimensionality*: Real-world multivariate series contain arbitrary numbers of target variates and dynamic exogenous covariates, whereas conventional transformers assume fixed dimension $d_y$ or process channels independently.
  3. *Distributional Heterogeneity*: Real datasets have strictly positive support (energy/sales), heavy tails, or high confidence spikes, making symmetric Gaussian/Student-$t$ heads inadequate.
- **Primary Novel Contributions**:
  - **MOIRAI Architecture** (*Masked EncOder-based UnIveRsAl TIme Series Forecasting Transformer*):
    - *Multi Patch Size Input/Output Projections*: Frequency-aware projection layers mapping multiple patch sizes (8, 16, 32, 64, 128) to shared hidden representation space $\mathbb{R}^{d_h}$.
    - *Any-Variate Attention*: Flattens multivariate time series into a unified sequence and introduces binary attention biases combined with Rotary Position Embeddings (RoPE) to achieve permutation equivariance w.r.t. variate ordering and invariance w.r.t. variate indices.
    - *Parametric Mixture Distribution Head*: Flexible output head combining Student's $t$, continuous negative binomial, log-normal, and low-variance normal distributions.
  - **LOTSA Archive (*Large-scale Open Time Series Archive*)**:
    - The largest open collection of time series data curated for pre-training foundation models, comprising **27,646,462,733 (27.6B)** univariate observations (or **231,082,956,489 (231B)** observations when accounting for target variates) across 9 distinct domains in unified Apache Arrow format.
  - **Zero-Shot Generalization**: Outperforms or matches full-shot supervised models on in-distribution benchmarks (Monash) and out-of-distribution probabilistic forecasting benchmarks (CRPS / MSIS on Electricity, Solar, Walmart, Weather, Istanbul Traffic, Turkey Power).

---

## 🧠 Methodology & Model Architecture

### 1. Problem Formulation & Objective Function
Consider a dataset $\mathcal{D} = \{(Y^{(i)}, Z^{(i)})\}_{i=1}^N$, where $Y^{(i)} \in \mathbb{R}^{d_{y_i} \times T_i}$ is a target time series with $d_{y_i}$ variates and $T_i$ time steps, and $Z^{(i)} \in \mathbb{R}^{d_{z_i} \times T_i}$ represents covariates.
The model predicts the parameters $\hat{\phi}$ of predictive distribution $p(Y_{t:t+h} \mid \hat{\phi})$ from historical lookback $Y_{t-l:t}$ and known dynamic covariates $Z_{t-l:t+h}$:

**Eq. 1 — Pre-training Maximum Log-Likelihood Objective**:
$$\max_{\theta} \mathbb{E}_{(Y, Z) \sim p(\mathcal{D}), (t, l, h) \sim p(\mathcal{T} \mid \mathcal{D})} \left[ \log p(Y_{t:t+h} \mid \hat{\phi}) \right], \quad \text{s.t. } \hat{\phi} = f_{\theta}(Y_{t-l:t}, Z_{t-l:t+h}) \tag{1}$$

where $p(\mathcal{D})$ samples time series and $p(\mathcal{T} \mid \mathcal{D})$ samples dynamic lookback context $l \in [2, 512]$ and forecast horizon $h$ (proportion $15\% - 50\%$ of sequence window).

---

### 2. Multi-Patch Size Projection & Sequence Flattening
- **Sequence Flattening**: A multivariate time series with $d$ variates and time length $L$ is flattened into a single concatenated 1D sequence of patch tokens.
- **Frequency-to-Patch Mapping**: Linear projection layers learned per patch size $P \in \{8, 16, 32, 64, 128\}$:
  - *Yearly, Quarterly*: $P = 8$
  - *Monthly*: $P \in \{8, 16, 32\}$
  - *Weekly, Daily*: $P \in \{16, 32\}$
  - *Hourly*: $P \in \{32, 64\}$
  - *Minute-level*: $P \in \{32, 64, 128\}$
  - *Second-level*: $P \in \{64, 128\}$
- **Instance Normalization**: Non-learnable reversible normalization applied per-variate to handle non-stationarity.
- **Learnable `[mask]` Token**: Replaces tokens falling within the forecast horizon $Y_{t:t+h}$.

---

### 3. Any-Variate Attention Mechanism
To handle arbitrary numbers of variates while guaranteeing permutation equivariance w.r.t. variate ordering and invariance w.r.t. variate indices, Any-variate Attention modifies standard self-attention by injecting binary variate indicator biases alongside Rotary Position Embeddings:

**Eq. 2 — Attention Energy with Binary Variate Bias & RoPE**:
$$E_{ij,mn} = (W^Q x_{i,m})^T R_{i-j} (W^K x_{j,n}) + u^{(1)} \cdot \mathbf{1}_{\{m=n\}} + u^{(2)} \cdot \mathbf{1}_{\{m \neq n\}} \tag{2}$$

**Eq. 3 — Any-variate Attention Softmax Normalization**:
$$A_{ij,mn} = \frac{\exp\{E_{ij,mn}\}}{\sum_{k,o} \exp\{E_{ik,mo}\}} \tag{3}$$

- $i, j$: Temporal token indices; $m, n$: Variate indices.
- $W^Q x_{i,m}, W^K x_{j,n} \in \mathbb{R}^{d_h}$: Query and key vectors.
- $R_{i-j} \in \mathbb{R}^{d_h \times d_h}$: Rotary matrix encoding relative time difference $(i-j)$.
- $u^{(1)}, u^{(2)} \in \mathbb{R}$: Head-specific learnable scalar biases for intra-variate ($m=n$) and inter-variate ($m \neq n$) attention.

---

### 4. Flexible Parametric Mixture Distribution Head
The output projection produces mixture weights $w_i$ (constrained to probability simplex via softmax) and distribution parameters $\hat{\phi}_i$ for $c=4$ component distributions:

**Eq. 4 — Mixture Predictive Distribution**:
$$p(Y_{t:t+h} \mid \hat{\phi}) = \sum_{i=1}^c w_i \, p_i(Y_{t:t+h} \mid \hat{\phi}_i) \tag{4}$$

The 4 parametric component distributions (Appendix B.2):
1. **Student's $t$-Distribution** (heavy tails, general series):
   $$p(x; \nu, \mu, \tau) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right) \sqrt{\pi \nu} \tau} \left(1 + \frac{1}{\nu} \left(\frac{x - \mu}{\tau}\right)^2\right)^{-\frac{\nu+1}{2}} \tag{B.1}$$
   Parameters $\nu > 0$ (degrees of freedom, lower-bounded to 2), $\mu \in \mathbb{R}$ (location), $\tau > 0$ (scale via softplus).
2. **Log-Normal Distribution** (strictly positive, right-skewed energy/economic data):
   $$p(x; \mu, \sigma) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\left( - \frac{(\ln x - \mu)^2}{2\sigma^2} \right) \tag{B.2}$$
3. **Continuous Negative Binomial Distribution** (count data):
   $$p(x; r, p) \propto \frac{\Gamma(x + r)}{\Gamma(x + 1) \Gamma(r)} (1 - p)^r p^x \tag{B.3}$$
   Parameters $r > 0$ (softplus), $p \in [0, 1]$ (sigmoid).
4. **Low-Variance Normal Distribution** (high-confidence / deterministic peaks):
   $$p(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( - \frac{(x - \mu)^2}{2\sigma^2} \right), \quad \text{with fixed } \sigma = 10^{-3} \tag{B.4}$$

---

### 5. Evaluation Metrics Formulations (Appendix C.1)
- **Continuous Ranked Probability Score (CRPS)** via Normalized Sum Quantile Loss ($wQL$):
  $$wQL[\alpha] = 2 \frac{\sum_t \Lambda_{\alpha}(\hat{q}_t(\alpha), y_t)}{\sum_t |y_t|}, \quad \text{where } \Lambda_{\alpha}(q, y) = (\alpha - \mathbf{1}_{\{y < q\}})(y - q)$$
  $$\text{CRPS} \approx \frac{1}{K} \sum_{k=1}^K wQL[\alpha_k], \quad \text{for } K=9 \text{ quantiles } \alpha \in \{0.1, 0.2, \dots, 0.9\}$$
- **Mean Scaled Interval Score (MSIS)** ($95\%$ prediction interval $\alpha=0.05$):
  $$\text{MSIS} = \frac{\frac{1}{h} \sum_{t=1}^h \left( (U_t - L_t) + \frac{2}{\alpha}(L_t - Y_t)\mathbf{1}_{\{Y_t < L_t\}} + \frac{2}{\alpha}(Y_t - U_t)\mathbf{1}_{\{Y_t > U_t\}} \right)}{\frac{1}{n-m} \sum_{t=m+1}^n |Y_t - Y_{t-m}|}$$

---

## 📊 Dataset & Input Features

### 1. The LOTSA Pretraining Archive (Table 2 & 3, §3.2.1, Appendix A)
LOTSA contains **27,646,462,733 observations** across 9 domains and frequencies from sub-second to yearly:

| Domain | Datasets Included | Observations (# Obs) | % of Corpus | Key Sources / References |
|---|---|---|---|---|
| **Energy** | 30 | 16,358,600,896 | 59.17% | [[BuildingsBench]] (Buildings900K, BDG-2, Low Carbon London), [[ProEnFo]] (GEF12/14/17, PDB, Spanish, ELF), Monash (London Smart Meters, Wind Farms/Power, Solar Power), KDD Cup 2022 |
| **Transport** | 23 | 4,900,453,419 | 17.73% | [[LargeST]] (42,333 series, 4.45B obs), [[LibCity]] (PEMS03/04/07/08/Bay, Seattle, SZ-Taxi, SHMetro, Q-Traffic), GluonTS Taxi / Uber |
| **Climate** | 6 | 4,188,011,890 | 15.15% | [[ClimateLearn]] (ERA5, CMIP6 at $2.8125^\circ$ grid: 64x128), SubseasonalClimateUSA, Oikolab |
| **CloudOps** | 3 | 1,518,268,292 | 5.49% | Azure VM Traces 2017 (885M obs), Borg Cluster Data 2011 (537M obs), Alibaba Cluster Trace 2018 (95M obs) |
| **Web** | 3 | 428,082,373 | 1.55% | Kaggle Extended Web Traffic (370M obs), Wiki-Rolling (40M obs), Kaggle Weekly |
| **Sales** | 6 | 197,984,339 | 0.72% | Favorita Sales (139M obs), M5 (58M obs), Favorita Transactions, Restaurant, Car Parts |
| **Nature** | 5 | 28,547,647 | 0.09% | Temperature Rain (22M obs), China Air Quality (5.7M obs), Beijing Air Quality, Saugeen, Sunspot |
| **Econ/Fin** | 23 | 24,919,596 | 0.10% | M1, M3, M4 (Yearly, Quarterly, Monthly, Daily, Weekly), Tourism, CIF 2016, GoDaddy, FRED MD, Bitcoin |
| **Healthcare** | 6 | 1,594,281 | 0.01% | Project Tycho (1.37M obs), CDC Fluview ILINet / WHO NREVSS, Hospital, COVID Deaths, US Births |
| **Total** | **105** | **27,646,462,733** | **100%** | Unified Apache Arrow format |

### 2. Direct Repository & Data Links
- **Official Code & Model Checkpoints**: `https://github.com/SalesforceAIResearch/uni2ts`
- **Hugging Face Checkpoints**: `https://huggingface.co/Salesforce/moirai-1.0-R-small`, `moirai-1.0-R-base`, `moirai-1.0-R-large`
- **Dataset Sources & Portal URLs**:
  - BuildingsBench: `https://openreview.net/forum?id=c5rqd6PZn6`
  - LargeST: `https://github.com/liuxu77/LargeST`
  - Monash Time Series Forecasting Archive: `https://openreview.net/forum?id=wEc1mgAjU-`
  - Apache Arrow Storage Integration: `https://arrow.apache.org/docs/r/`
  - Istanbul Traffic Index: `https://www.kaggle.com/datasets/leonardo00/istanbul-traffic-index`
  - Turkey Electricity Power Demand: `https://www.kaggle.com/datasets/dharanikra/electrical-power-demand-in-turkey`
  - CDC Fluview Portal: `https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html`

### 3. Input Features & Sequence Configuration
- **Target Channels**: $Y \in \mathbb{R}^{d_y \times T}$ (univariate or arbitrary multivariate target signals).
- **Dynamic Covariates**: $Z \in \mathbb{R}^{d_z \times T}$ (known in forecast horizon, e.g. calendar/time-of-day features).
- **Variate & Time IDs**: Binary variate identifier for Any-variate Attention; RoPE for relative temporal distance.
- **Sequence Packing**: Packed training without padding tokens reduces padding overhead from $61.08\%$ to $0.38\%$ (calculated over 1,000 iterations, §4.4).

---

## 📈 Performance & Results

### 1. Model Scaling Configurations (Table 4 p.6)
- **$\text{MOIRAI}_{\text{Small}}$**: 6 layers, $d_{\text{model}}=384$, $d_{ff}=1536$, 6 heads, $d_{kv}=64$, **14M parameters**, 100K training steps.
- **$\text{MOIRAI}_{\text{Base}}$**: 12 layers, $d_{\text{model}}=768$, $d_{ff}=3072$, 12 heads, $d_{kv}=64$, **91M parameters**, 1M training steps.
- **$\text{MOIRAI}_{\text{Large}}$**: 24 layers, $d_{\text{model}}=1024$, $d_{ff}=4096$, 16 heads, $d_{kv}=64$, **311M parameters**, 1M training steps.

---

### 2. In-Distribution & Out-of-Distribution Probabilistic Forecasting (Table 5 p.7)
Evaluated across 6 out-of-distribution benchmarks under rolling-window evaluation (CRPS & MSIS; mean $\pm$ std for 5 seeds on baselines):

| Dataset | Metric | $\text{MOIRAI}_{\text{Small}}$ (Zero-shot) | $\text{MOIRAI}_{\text{Base}}$ (Zero-shot) | $\text{MOIRAI}_{\text{Large}}$ (Zero-shot) | PatchTST (Full-shot) | TiDE (Full-shot) | TFT (Full-shot) | DeepAR (Full-shot) | AutoARIMA | Seasonal Naive |
|---|---|---|---|---|---|---|---|---|---|---|
| **Electricity** | CRPS | 0.072 | 0.055 | **0.050** | 0.052 $\pm$ 0.00 | **0.048** $\pm$ 0.00 | 0.050 $\pm$ 0.00 | 0.065 $\pm$ 0.01 | 0.327 | 0.070 |
| | MSIS | 7.999 | 6.172 | 5.875 | 5.744 $\pm$ 0.12 | **5.672** $\pm$ 0.08 | 6.278 $\pm$ 0.24 | 6.893 $\pm$ 0.82 | 29.412 | 35.251 |
| **Solar** | CRPS | 0.471 | 0.419 | **0.406** | 0.518 $\pm$ 0.09 | 0.420 $\pm$ 0.00 | 0.446 $\pm$ 0.03 | 0.431 $\pm$ 0.01 | 1.055 | 0.512 |
| | MSIS | 8.425 | 7.011 | **6.250** | 8.447 $\pm$ 1.59 | 13.754 $\pm$ 0.32 | 8.057 $\pm$ 3.51 | 11.181 $\pm$ 0.67 | 25.849 | 48.130 |
| **Walmart** | CRPS | 0.103 | 0.093 | 0.098 | 0.082 $\pm$ 0.01 | **0.077** $\pm$ 0.00 | 0.087 $\pm$ 0.00 | 0.121 $\pm$ 0.00 | 0.124 | 0.151 |
| | MSIS | 9.371 | 8.421 | 8.520 | **6.005** $\pm$ 0.21 | 6.258 $\pm$ 0.12 | 8.718 $\pm$ 0.10 | 12.502 $\pm$ 0.03 | 9.888 | 49.458 |
| **Weather** | CRPS | 0.049 | **0.041** | 0.051 | 0.059 $\pm$ 0.01 | 0.054 $\pm$ 0.00 | 0.043 $\pm$ 0.00 | 0.132 $\pm$ 0.11 | 0.252 | 0.068 |
| | MSIS | 5.236 | 5.136 | **4.962** | 7.759 $\pm$ 0.49 | 8.095 $\pm$ 1.74 | 7.791 $\pm$ 0.44 | 21.651 $\pm$ 17.34 | 19.805 | 31.293 |
| **Istanbul Traffic** | CRPS | 0.173 | 0.116 | 0.112 | 0.112 $\pm$ 0.00 | 0.110 $\pm$ 0.01 | 0.110 $\pm$ 0.01 | **0.108** $\pm$ 0.00 | 0.589 | 0.257 |
| | MSIS | 5.937 | 4.461 | 4.277 | **3.813** $\pm$ 0.09 | 4.752 $\pm$ 0.17 | 4.057 $\pm$ 0.44 | 4.094 $\pm$ 0.31 | 16.317 | 45.473 |
| **Turkey Power** | CRPS | 0.048 | 0.040 | **0.036** | 0.054 $\pm$ 0.01 | 0.046 $\pm$ 0.01 | 0.039 $\pm$ 0.00 | 0.066 $\pm$ 0.02 | 0.116 | 0.085 |
| | MSIS | 7.127 | 6.766 | **6.341** | 8.978 $\pm$ 0.51 | 8.579 $\pm$ 0.52 | 7.943 $\pm$ 0.31 | 13.520 $\pm$ 1.17 | 14.863 | 36.256 |

---

### 3. Long Sequence Deterministic Forecasting Benchmark (Table 6 p.7)
Averaged across forecast horizons $H \in \{96, 192, 336, 720\}$:

| Dataset | Metric | $\text{MOIRAI}_{\text{Small}}$ | $\text{MOIRAI}_{\text{Base}}$ | $\text{MOIRAI}_{\text{Large}}$ | iTransformer | TimesNet | PatchTST | TiDE | DLinear | FEDformer |
|---|---|---|---|---|---|---|---|---|---|---|
| **ETTh1** | MSE / MAE | **0.400** / **0.424** | 0.434 / 0.438 | 0.510 / 0.469 | 0.454 / 0.448 | 0.458 / 0.450 | 0.469 / 0.455 | 0.541 / 0.507 | 0.456 / 0.452 | 0.444 / 0.464 |
| **ETTh2** | MSE / MAE | **0.341** / **0.379** | 0.345 / 0.382 | 0.354 / 0.376 | 0.383 / 0.407 | 0.414 / 0.497 | 0.387 / 0.407 | 0.611 / 0.550 | 0.559 / 0.515 | 0.437 / 0.449 |
| **ETTm1** | MSE / MAE | 0.448 / 0.409 | **0.381** / **0.388** | 0.390 / 0.389 | 0.407 / 0.410 | 0.400 / 0.406 | 0.387 / 0.400 | 0.419 / 0.419 | 0.403 / 0.407 | 0.448 / 0.452 |
| **ETTm2** | MSE / MAE | 0.300 / 0.341 | **0.272** / **0.321** | 0.276 / **0.320** | 0.288 / 0.332 | 0.291 / 0.333 | 0.281 / 0.326 | 0.358 / 0.404 | 0.350 / 0.401 | 0.305 / 0.349 |
| **Electricity** | MSE / MAE | 0.233 / 0.320 | **0.188** / 0.274 | **0.188** / 0.273 | **0.178** / **0.270** | 0.193 / 0.295 | 0.216 / 0.304 | 0.252 / 0.344 | 0.212 / 0.300 | 0.214 / 0.327 |
| **Weather** | MSE / MAE | 0.242 / 0.267 | **0.238** / **0.261** | 0.259 / 0.275 | 0.258 / 0.278 | 0.259 / 0.287 | 0.259 / 0.281 | 0.271 / 0.320 | 0.265 / 0.317 | 0.309 / 0.360 |

---

### 4. Systematic Ablation Study (Table 7 p.8)
On Monash Benchmark (Normalized MAE, lower is better):
- **Full $\text{MOIRAI}_{\text{Small}}$**: **0.655**
- **w/o patch size constraints**: 0.720 ($+9.9\%$ degradation)
- **w/o multi patch size (fixed patch 32)**: 1.156 ($+76.5\%$ severe degradation)
- **w/o Any-variate Attention (additive learned embeddings)**: 0.904 ($+38.0\%$ degradation)
- **w/o mixture distribution (Student's $t$ only)**: 0.740 ($+13.0\%$ degradation)
- **w/o LOTSA (trained only on Monash + GluonTS)**: 0.809 ($+23.5\%$ degradation)
- **w/o sequence packing**: 0.785 ($+19.8\%$ degradation due to padding token dilution)

---

## 💡 Limitations & Identified Research Gaps

1. **Heuristic Frequency-to-Patch Mapping**: The mapping from sampling frequency to allowed patch sizes is fixed heuristically ($8 \dots 128$) rather than dynamically learned or continuous.
2. **Computational Overhead with High-Dimensional Variates**: Flattening $d$ variates scales the sequence length by $d$, causing the full self-attention matrix in the masked encoder to scale quadratically $O((d \cdot L / P)^2)$, which limits scalability to hundreds of simultaneous channels.
3. **Absence of Strict Neural Scaling Laws**: Model performance does not monotonically scale from Base (91M) to Large (311M) on fixed training compute, suggesting the need for revised scaling laws (data vs compute ratios) tailored for time series foundation models.
4. **Masked Autoencoding Efficiency Bottleneck**: Masked encoder processing requires full attention over both visible and masked tokens during generation, which is slower than causal decoder-only autoregressive models (later addressed in Moirai 2.0).

---

## 📚 BibTeX & Citation Reference

```bibtex
@inproceedings{woo2024unified,
  title     = {Unified Training of Universal Time Series Forecasting Transformers},
  author    = {Woo, Gerald and Liu, Chenghao and Kumar, Akshat and Xiong, Caiming and Savarese, Silvio and Sahoo, Doyen},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML 2024)},
  volume    = {235},
  pages     = {53155--53181},
  year      = {2024},
  publisher = {PMLR},
  url       = {https://arxiv.org/abs/2402.02592}
}
```

---

## 🔗 Key References & Citation Graph

- **Predecessor & Baseline Time Series Architectures in Vault**:
  - [[2017_Attention_Is_All_You_Need]] — Core Transformer self-attention foundation (Vaswani et al., 2017).
  - [[2021_TFT_Temporal_Fusion_Transformers]] — Temporal Fusion Transformers for interpretable multi-horizon forecasting (Lim et al., 2021).
  - [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] — Autoformer series decomposition (Wu et al., 2021).
  - [[2021_Informer_Beyond_Efficient_Transformer]] — Informer ProbSparse self-attention (Zhou et al., 2021).
  - [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — PatchTST subseries patching and channel-independent modeling (Nie et al., 2023).
  - [[2023_TimesNet_Temporal_2D_Variation_Modeling]] — TimesNet 2D temporal variation modeling (Wu et al., 2023).
  - [[2023_DLinear_Are_Transformers_Effective_LTSF]] — DLinear / NLinear baseline challenge (Zeng et al., 2023).
  - [[2024_TiDE_Long_Term_Forecasting]] — TiDE dense encoder-decoder baseline (Das et al., 2023/2024).
  - [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] — iTransformer inverted variate tokens (Liu et al., 2024).
  - [[2024_TimesFM_Decoder_Only_Foundation_Model]] — TimesFM decoder-only foundation model comparison (Das et al., 2024).
  - [[2025_Chronos_2_Univariate_to_Universal]] — Chronos-2 probabilistic pretrained TSFM comparison (Ansari et al., 2025).
- **Direct Successor in Vault**:
  - [[2026_Moirai_2_When_Less_Is_More]] — Moirai 2.0: Salesforce AI Research transition from masked encoder to causal decoder-only quantile architecture on 36M/295B corpus (Liu et al., 2026).
- **Extracted Reference Dump**:
  - `wiki/references/2024_Unified_Training_Universal_Time_Series_Transformers_refs.md`
