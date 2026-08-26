---
type: paper
title: "Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting"
authors: [Kashif Rasul, Calvin Seward, Ingmar Schuster, Roland Vollgraf]
year: 2021
journal_conference: "ICML 2021 (International Conference on Machine Learning), Zalando Research"
doi_url: "https://arxiv.org/abs/2101.12072"
models_used: ["[[TimeGrad]]", "[[DDPM|Denoising Diffusion Probabilistic Model]]", "[[LSTM|2-layer LSTM RNN]]", "[[Dilated_Convolution|Conditional Dilated ConvNet (εθ)]]", "[[Score_Matching]]"]
datasets_used: ["[[Exchange_Dataset]]", "[[Solar_Energy|Solar]]", "[[Electricity_ECL|Electricity (UCI Load Diagrams)]]", "[[Traffic|PEM-SF Traffic]]", "[[NYC_Taxi]]", "[[Wikipedia_Pageviews]]"]
features_used: ["[[Multivariate_Time_Series]]", "[[Historical_Load]]", "[[Calendar_Features]]", "[[Lag_Features]]", "[[Mean_Scaling]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[CRPS]]", "[[CRPSsum]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting

## 🎯 Main Objective & Contribution
- Introduces **TimeGrad**: an autoregressive energy-based model that samples from the **full joint multivariate predictive distribution at each time step** via denoising diffusion ([[DDPM]]), avoiding restrictive parametric emission families (Gaussian / negative binomial / low-rank copulas / normalizing flows).
- Combines autoregressive extrapolation strength with EBM flexibility: diffusion head conditioned on an [[LSTM]] hidden state estimates the **score** of the data distribution; sampling proceeds by annealed Langevin-style reverse Markov chain from white noise.
- New state-of-the-art multivariate probabilistic forecasting on benchmarks with up to thousands of correlated dimensions (963 traffic sensors, 2,000 Wikipedia pages).

## 🧠 Methodology & Model Architecture
### 1. Diffusion Probabilistic Model (Ho et al., 2020)
Fixed forward process adding Gaussian noise along variance schedule $\beta_1,\dots,\beta_N$:
$$q(x_n|x_{n-1}) := \mathcal{N}(x_n;\sqrt{1-\beta_n}\,x_{n-1},\ \beta_n\mathbf{I})$$
Learned reverse process with Gaussian transitions starting at $p(x^N)=\mathcal{N}(0,\mathbf{I})$:
$$p_\theta(x_{n-1}|x_n) := \mathcal{N}(x_{n-1};\ \mu_\theta(x_n,n),\ \Sigma_\theta(x_n,n)\mathbf{I}) \tag{Reverse Transition}$$
Closed-form forward marginal with $\alpha_n:=1-\beta_n$, $\bar{\alpha}_n:=\prod_{i=1}^{n}\alpha_i$:
$$q(x_n|x_0) = \mathcal{N}\!\left(x_n;\sqrt{\bar{\alpha}_n}\,x_0,\ (1-\bar{\alpha}_n)\mathbf{I}\right) \tag{Forward Marginal}$$
Variational-bound objective reduced to KL divergences between Gaussians (Eq. 4–6), giving the simplified score-matching loss:
$$E_{x_0,\epsilon}\left[\frac{\beta_n^2}{2\Sigma_\theta\alpha_n(1-\bar{\alpha}_n)}\left\|\epsilon-\epsilon_\theta(\sqrt{\bar{\alpha}_n}x_0+\sqrt{1-\bar{\alpha}_n}\epsilon,\ n)\right\|^2\right] \tag{Diffusion Loss}$$
Sampling step (annealed Langevin dynamics):
$$x_{n-1} = \frac{1}{\sqrt{\alpha_n}}\left(x_n - \frac{\beta_n}{\sqrt{1-\bar{\alpha}_n}}\epsilon_\theta(x_n,n)\right) + \sqrt{\Sigma_\theta}\,z,\quad z\sim\mathcal{N}(0,\mathbf{I}) \tag{Reverse Sampling}$$

### 2. TimeGrad Conditional Formulation
Factorized conditional forecast with known covariates $c_{1:T}$:
$$q_X(x^0_{t_0:T}|x^0_{1:t_0-1}, c_{1:T}) = \prod_{t=t_0}^{T} q_X(x^0_t|x^0_{1:t-1}, c_{1:T}) \approx \prod_{t=t_0}^{T} p_\theta(x^0_t|h_{t-1}) \tag{Autoregressive Factorization}$$
RNN temporal encoder:
$$h_t = \text{RNN}_\theta(\text{concat}(x^0_t, c_t), h_{t-1}) \tag{RNN Update}$$
Training objective per step (with $\Sigma_\theta=\tilde\beta_n$, Algorithm 1):
$$E_{x^0_t,\epsilon,n}\left[\|\epsilon-\epsilon_\theta(\sqrt{\bar{\alpha}_n}x^0_t+\sqrt{1-\bar{\alpha}_n}\epsilon,\ h_{t-1},\ n)\|^2\right] \tag{Conditioned Training Loss}$$
- **εθ network**: 8 conditional residual blocks of bidirectional dilated 1-D convolutions (WaveNet/DiffWave-style), gated activation unit $\sigma(\cdot)\odot\tanh(\cdot)$, dilation $2^{i\bmod 2}$, residual channels = 8, circular padding, skip-connection sum output.
- Noise index $n\in\{1,\dots,N\}$ embedded with Transformer Fourier positional embeddings ($N_{\max}=500$) into $\mathbb{R}^{32}$.
- Training: Adam, LR $10^{-3}$, batch 64 random windows, context size = prediction length, early stopping on validation split; single Nvidia V100 16 GB.
- Inference: sample $S=100$ trajectories autoregressively for empirical quantiles (Algorithm 2).
- **Scaling trick**: each entity divided by its context-window mean before input, rescaled at output (from DeepAR); embeddings for categorical/time features + lag features per data frequency.

## 📊 Dataset & Input Features
Six real-world open datasets (Table 1), preprocessed exactly as Salinas et al. (GP-Copula):

| Dataset | Dim $D$ | Domain | Freq | Train steps | Pred steps |
| :-- | :--: | :--: | :--: | :--: | :--: |
| [[Exchange_Dataset]] | 8 | $\mathbb{R}^+$ | day | 6,071 | 30 |
| [[Solar_Energy|Solar]] | 137 PV plants | $\mathbb{R}^+$ | hour | 7,009 | 24 |
| [[Electricity_ECL|Electricity]] | 370 customers | $\mathbb{R}^+$ | hour | 5,833 | 24 |
| [[Traffic]] | 963 freeway sensors | (0,1) occupancy | hour | 4,001 | 24 |
| [[NYC_Taxi|Taxi]] | 1,214 locations | $\mathbb{N}$ counts | 30-min | 1,488 | 24 |
| [[Wikipedia_Pageviews|Wikipedia]] | 2,000 pages | $\mathbb{N}$ counts | day | 792 | 30 |

- Data URLs found in text:
  - Electricity: https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
  - Traffic: https://archive.ics.uci.edu/ml/datasets/PEMS-SF
  - Taxi: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
  - Wikipedia: https://github.com/mbohlkeschneider/gluon-ts/tree/mv_release/datasets
  - (Footnote) Kaggle Taxi Trajectory challenge: https://www.kaggle.com/c/pkdd-15-predict-taxi-service-trajectory-i
- Data availability statement: "The source code of the model will be made available after the review process" (paper: https://arxiv.org/abs/2101.12072).
- Features: historical multivariate target, time-dependent covariates (day-of-week, hour-of-day), categorical embeddings, frequency-specific lag features — all known over the forecast horizon; no normalization needed for Traffic.

## 📈 Performance & Results
Test-set [[CRPSsum]] (lower better; TimeGrad = mean ± SE over 10 retraining runs, Table 2):

| Method | Exchange | Solar | Electricity | Traffic | Taxi | Wikipedia |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| **TimeGrad** | 0.006±0.001 | **0.287±0.02** | **0.0206±0.001** | **0.044±0.006** | **0.114±0.02** | **0.0485±0.002** |
| Transformer-MAF | 0.005±0.003 | 0.301±0.014 | 0.0207±0.000 | 0.056±0.001 | 0.179±0.002 | 0.063±0.003 |
| GP-Copula | 0.007±0.000 | 0.337±0.024 | 0.0245±0.002 | 0.078±0.002 | 0.208±0.183 | 0.086±0.004 |
| GP-scaling | 0.009±0.000 | 0.368±0.012 | 0.022±0.000 | 0.079±0.000 | 0.183±0.395 | 1.483±1.034 |
| Vec-LSTM lowrank-Copula | 0.007±0.000 | 0.319±0.011 | 0.064±0.008 | 0.103±0.006 | 0.326±0.007 | 0.241±0.033 |
| VAR-Lasso | 0.012±0.0002 | 0.51±0.006 | 0.025±0.0002 | 0.15±0.002 | – | 3.1±0.004 |

- New SOTA on all datasets except the smallest (Exchange, where VAR/VES/Transformer-MAF tie at 0.005): ~21% lower CRPSsum than Transformer-MAF on Traffic, ~21% on Wikipedia, ~36% on Taxi vs GP methods.
- **Ablation on diffusion length $N$** (Electricity): performance already good at $N\approx10$, optimal at $N\approx100$; larger $N$ not beneficial. Linear schedule $\beta_1=10^{-4}\to\beta_N=0.1$, $N=100$ used throughout.
- Qualitative: calibrated median + 50%/90% intervals across first 6 of 963 Traffic dimensions despite order-of-magnitude scale differences between neighboring entities.

## 💡 Limitations & Identified Research Gaps
- **Inference latency**: sampling loops $N=100$ times over $\epsilon_\theta$ per autoregressive timestep × $S=100$ trajectory samples — costly for large-scale or near-real-time EV forecasting (mitigations noted: WaveGrad-style L1 loss/fewer steps; DDIM non-Markovian processes, Song et al. 2021).
- RNN conditioning limits very long sequences — authors propose Transformer encoders as replacement conditioning backbone.
- No explicit modeling of discrete distributions (flows need dequantization; EBMs do not — left as future work).
- No spatial inductive bias: suggests graph neural networks when inter-entity relationships are known (e.g., road networks between charging stations).
- Future work flagged by authors: anomaly/OOD detection exploiting EBM likelihood behavior.
- Gap for thesis: unconditional-per-step diffusion cost vs [[2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting]]'s joint temporal diffusion for EV charging applications.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{rasul2021timegrad,
  title={Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting},
  author={Rasul, Kashif and Seward, Calvin and Schuster, Ingmar and Vollgraf, Roland},
  booktitle={International Conference on Machine Learning (ICML)},
  year={2021}
}
```

## 🔗 Key References & Citation Graph
- Foundation: Ho et al., *Denoising Diffusion Probabilistic Models* (NeurIPS 2020); Sohl-Dickstein et al. 2015 (diffusion); Song & Ermon (score matching); WaveNet/DiffWave (εθ architecture).
- Baselines compared: Transformer-MAF (Rasul et al. 2021), GP-Copula/GP-scaling/Vec-LSTM ([[2020_Salinas_DeepAR_Probabilistic_Forecasting]] lineage), KVAE, VAR/GARCH/VES.
- Related vault papers: [[2017_Attention_Is_All_You_Need]] (Fourier positional embeddings), [[2021_Lim_TFT_Temporal_Fusion_Transformers]], [[2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting]], [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]]
- Shared benchmark: [[Electricity_ECL]] (370 customers, hourly) — direct relevance to aggregate EV/load forecasting.
