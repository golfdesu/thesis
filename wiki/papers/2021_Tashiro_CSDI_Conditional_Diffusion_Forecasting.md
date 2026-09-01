---
type: paper
title: "CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation"
authors: [Yusuke Tashiro, Jiaming Song, Yang Song, Stefano Ermon]
year: 2021
journal_conference: "NeurIPS 2021 (35th Conference on Neural Information Processing Systems)"
doi_url: "https://arxiv.org/abs/2107.03502"
models_used: ["[[CSDI]]", "[[DDPM|Conditional Score-based Diffusion Model]]", "[[Transformer]]", "[[TimeGrad]]"]
datasets_used: ["[[PhysioNet_2012_Healthcare]]", "[[Beijing_PM25_Air_Quality]]", "[[Solar_Alabama]]", "[[Electricity_ECL]]", "[[Traffic]]", "[[NYC_Taxi]]", "[[Wiki_Pageviews]]"]
features_used: ["[[Observation_Mask]]", "[[Conditional_Mask]]", "[[Timestamp]]", "[[Temporal_Embedding]]", "[[Feature_Embedding]]", "[[Diffusion_Step_Embedding]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[CRPS]]", "[[MAE]]", "[[RMSE]]", "[[MSE]]", "[[NLL]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation

## 🎯 Main Objective & Contribution
- **Core problem**: Probabilistic imputation of missing values in multivariate time series. Prior score-based approaches (Song et al. SDE; repainting-style methods) *approximate* the conditional reverse process by noising the observations, which destroys useful information in $x^{co}_0$ and does not correspond to the exact conditional distribution. Autoregressive/RNN imputation methods (BRITS, GLIMA) struggle with complex missing patterns.
- **Primary contribution**: **CSDI** — a conditional score-based [[DDPM]] trained *directly* on the conditional distribution $q(x^{ta}_0 \mid x^{co}_0)$ via a self-supervised masked-training scheme (inspired by masked language modeling / BERT), with a 2D (temporal + feature) Transformer denoiser based on [[DDPM]].
- Results: CRPS improved **40–65%** over existing probabilistic imputation baselines; deterministic MAE improved **5–20%** over SOTA deterministic methods; also competitive at interpolation and probabilistic forecasting.

## 🧠 Methodology & Model Architecture
- Time series expressed as $\{X, M, s\}$ with values $X = \{x_{1:K,1:L}\} \in \mathbb{R}^{K\times L}$ ($K$ features, length $L$), binary observation mask $M$, timestamps $s$ (irregular intervals allowed). Imputation generalizes to interpolation (all features at target time points) and forecasting (all features at future points).
- **Forward process** (Eq. 1): $q(x_{1:T}|x_0) := \prod_{t=1}^T q(x_t|x_{t-1})$, where $q(x_t|x_{t-1}) := N(\sqrt{1-\beta_t}\,x_{t-1},\ \beta_t I)$; closed form $x_t = \sqrt{\alpha_t}x_0 + (1-\alpha_t)\epsilon$, $\epsilon \sim N(0,I)$, with $\hat{\alpha}_t := 1-\beta_t$, $\alpha_t := \prod_{i=1}^t \hat{\alpha}_i$.
- **Reverse process** (Eq. 2): $p_\theta(x_{0:T}) := p(x_T)\prod_{t=1}^T p_\theta(x_{t-1}|x_t)$, $x_T \sim N(0,I)$, $p_\theta(x_{t-1}|x_t) := N(x_{t-1}; \mu_\theta(x_t,t), \sigma_\theta(x_t,t)I)$.
- **DDPM parameterization** (Eq. 3):
$$\mu_\theta(x_t,t) = \frac{1}{\sqrt{\hat{\alpha}_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\hat{\alpha}_t}}\,\epsilon_\theta(x_t,t)\right), \quad \sigma_\theta(x_t,t) = \tilde{\beta}_t^{1/2},\quad \tilde{\beta}_t = \begin{cases}\frac{1-\hat{\alpha}_{t-1}}{1-\hat{\alpha}_t}\beta_t & t>1\\ \beta_1 & t=1\end{cases}$$
- **Unconditional DDPM training loss** (Eq. 4 / unweighted ELBO Eq. 10): $\min_\theta L(\theta) := \min_\theta E_{x_0\sim q(x_0),\epsilon\sim N(0,I),t}\|\epsilon - \epsilon_\theta(\sqrt{\alpha_t}x_0+(1-\alpha_t)\epsilon, t)\|_2^2$.
- **Conditional reverse process** (Eq. 5): $p_\theta(x^{ta}_{0:T}|x^{co}_0) := p(x^{ta}_T)\prod_{t=1}^T p_\theta(x^{ta}_{t-1}|x^{ta}_t, x^{co}_0)$ — modeled exactly, unlike prior approximations.
- **CSDI parameterization** (Eq. 6): $\mu_\theta(x^{ta}_t, t|x^{co}_0) = \mu_{\text{DDPM}}(x^{ta}_t, t, \epsilon_\theta(x^{ta}_t, t|x^{co}_0))$, $\sigma_\theta = \sigma_{\text{DDPM}}$.
- **Training loss (conditional denoising objective)** (Eq. 7):
$$\min_\theta L(\theta) := \min_\theta E_{x_0\sim q(x_0),\epsilon\sim N(0,I),t}\left\|\left(\epsilon - \epsilon_\theta(x^{ta}_t, t \mid x^{co}_0)\right)\right\|_2^2$$
with noisy targets $x^{ta}_t = \sqrt{\alpha_t}x^{ta}_0 + (1-\alpha_t)\epsilon$. At sampling: targets = all missing values, conditionals = all observed; at training: targets = subset of observed values chosen by a target choice strategy, conditionals = remaining observed values (Table 1).
- **Self-supervised target choice strategies**: (1) **Random** (target ratio $r \sim U(0,100)\%$ of observed values); (2) **Historical** (targets = intersection of observed indices of one sample with missing indices of another sample → learns structured consecutive gaps); (3) **Mix** (draws random/historical 1:1 per sample); (4) **Test pattern** (fixed future mask — used for forecasting).
- **Denoiser architecture**: DiffWave-based residual network, adapted: diffusion steps $T=50$; DiffWave's dilated convolutions replaced by **2D attention** — temporal Transformer layer (input shape $(1,L,C)$, per-feature temporal dependency) + feature Transformer layer (shape $(K,1,C)$, per-timestep cross-feature dependency), each a 1-layer PyTorch TransformerEncoder (8 heads). Inputs zero-padded to fixed $K\times L$ space with conditional mask $m^{co}$; output masked by $(1-m^{co})$. Side info: 128-dim diffusion-step embedding (Eq. 13) and 128-dim timestamp embedding (Eq. 14, $\tau=10000$), plus 16-dim categorical feature embedding. For forecasting tasks only: efficient linear attention (global attention) due to many features/long sequences; feature subset sampling (size 64) during training.
- Masked training variant for data with real missing values (Eq. 12):
$$\min_\theta L(\theta) := \min_\theta E_{x_0\sim q(x_0),\epsilon\sim N(0,I),t}\|(\epsilon - \epsilon_\theta(\tilde{x}^{ta}_t, t | x^{co}_0, m^{co})) \odot m^{ta}\|_2^2$$
where $\tilde{x}^{ta}_t = \sqrt{\alpha_t}\tilde{x}^{ta}_0 + (1-\alpha_t)\tilde{\epsilon}^{ta}$ uses dummy zeros at missing indices and masked noise $\tilde{\epsilon}^{ta} = (1-m^{co})\odot\epsilon$.
- **Quadratic noise schedule** (Eq. 15): $\beta_t = \left(\sqrt{\frac{T-t}{T-1}}\sqrt{\beta_1} + \sqrt{\frac{t-1}{T-1}}\sqrt{\beta_T}\right)^2$ with $\beta_1=0.0001$, $\beta_T=0.5$.
- **CRPS computation** (Eqs. 16–17): $\text{CRPS}(F^{-1}, x) = \int_0^1 2\Lambda_\alpha(F^{-1}(\alpha), x)\,d\alpha$ approximated by quantile losses at 0.05 ticks over 100 generated samples; normalized average $\frac{\sum_{k,l}\text{CRPS}(F^{-1}_{k,l}, x_{k,l})}{\sum_{k,l}|x_{k,l}|}$ (Eq. 18); CRPS-sum for forecasting (Eq. 19).
- Hyperparameters: ~415k parameters, 4 residual layers, residual channels 64, batch size 16 (8 for forecasting), Adam lr 0.001 decayed to 0.0001/0.00001 at 75%/90% of epochs, 200 epochs (up to 300 for large-$K$ forecasting datasets).

## 📊 Dataset & Input Features
- **[[PhysioNet_2012_Healthcare]]** (PhysioNet/CinC Challenge 2012): 4000 ICU clinical time series, 35 variables, 48h; processed to hourly, 48 time steps; ~80% missing; no ground truth → 10/50/90% of observed values artificially held out. Split: 5-fold random test, train:val = 7:1.
- **[[Beijing_PM25_Air_Quality]]** (ST-MVL dataset): hourly PM2.5 from 36 stations in Beijing, 2014/05/01–2015/04/30 (12 months); sequences of 36 consecutive steps; ~13% structured (non-random) missing; artificial ground truth based on next-month patterns. Test months: 3rd, 6th, 9th, 12th.
- **Forecasting datasets** (GluonTS preprocessed, Table 6: features K / total steps / history $L_1$ / predict $L_2$):
  - [[Solar_Alabama]]: hourly solar power, 137 stations, Alabama, 10392 steps, 168→24
  - [[Electricity_ECL]]: hourly consumption of 370 customers, 5833 steps, 168→24
  - [[Traffic]]: hourly occupancy of 963 SF freeway lanes, 7009 steps, 168→24
  - [[NYC_Taxi]]: half-hourly taxi traffic at 1214 NYC locations, Jan 2015 train / Jan 2016 test, 1488 steps, 48→24
  - [[Wiki_Pageviews]]: daily views of 2000 Wikipedia pages, 792 steps, 90→30
- Features: observation mask, conditional mask, timestamps, categorical feature embeddings, diffusion-step embedding.
- **Links / data availability**:
  - Code: https://github.com/ermongroup/CSDI
  - arXiv: https://arxiv.org/abs/2107.03502
  - GluonTS datasets: https://github.com/awslabs/gluon-ts
  - Electricity: https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
  - Traffic: https://archive.ics.uci.edu/ml/datasets/PEMS-SF
  - Taxi: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data
  - Linear attention transformer package: https://github.com/lucidrains/linear-attention-transformer

## 📈 Performance & Results
- **Probabilistic imputation (CRPS, lower better)**: healthcare CSDI 0.238 / 0.330 / 0.522 (10/50/90% missing) vs GP-VAE 0.574 / 0.774 / 0.998, Multitask GP 0.489 / 0.581 / 0.942, V-RIN 0.808 / 0.831 / 0.922; air quality CSDI **0.108** vs GP-VAE 0.397 → 40–65% CRPS reduction; unconditional diffusion clearly worse (e.g., 0.360 vs 0.238) proving explicit conditional modeling matters.
- **Deterministic imputation (MAE, median of 100 samples)**: healthcare 10% missing CSDI **0.217** vs BRITS 0.284, GLIMA* 0.265, V-RIN 0.271, RDIS 0.319; air quality CSDI **9.60** vs GLIMA* 10.54, BRITS 11.56–14.11 → 5–20% improvement. RMSE similarly best (healthcare 10%: CSDI 0.498 vs SSGAN* 0.598, BRITS 0.619; air quality 19.30 vs unconditional 22.58).
- **Interpolation (irregularly sampled healthcare)**: CRPS CSDI 0.380 / 0.418 / 0.556 vs mTANs 0.526 / 0.567 / 0.689 and Latent ODE 0.700+; MAE/RMSE consistent.
- **Probabilistic forecasting (CRPS-sum, Table 5)**: CSDI best on electricity (**0.017** vs TimeGrad 0.021, TransMAF 0.021) and traffic (**0.020** vs TimeGrad 0.044); competitive elsewhere (solar 0.298 vs TLAE 0.124 best; taxi 0.123 vs TimeGrad 0.114; wiki 0.047 vs TimeGrad 0.049). On plain CRPS/MSE (Tables 11–12) CSDI best across all five datasets.
- **Ablation (Table 7)**: 2D attention beats Bi-RNN, dilated conv, flatten, and single-axis variants (healthcare 10% MAE 0.217 vs Bi-RNN 0.272, dilated conv 0.279, flatten 0.383, no-temporal 0.439) → both temporal and feature dependencies essential.
- Target choice ablation (Table 13, air quality): random 0.108 ≈ mix 0.108 > historical 0.113 CRPS (historical slightly hurt by train/test missing-pattern mismatch).
- 5–10 generated samples already outperform baselines; gains saturate beyond ~50 samples.
- ELBO/NLL highly sensitive to noise schedule yet nearly uncorrelated with CRPS/sample quality (Table 8) → evaluation relies on CRPS/MAE.

## 💡 Limitations & Identified Research Gaps
- Sampling speed: iterative reverse diffusion (50 steps × network evals) slower than other generative models — authors suggest ODE solvers (DDIM etc.) for acceleration; relevant gap for real-time EV load forecasting deployment.
- Forecasting advantage smaller than imputation advantage since benchmark forecasting datasets have few missing values and suit RNN encoders.
- Historical strategy can underperform when train/test missing patterns differ.
- ELBO unsuitable as evaluation metric for noisy time series.
- Future work: joint training of imputation with downstream tasks (classification); extension to other modalities.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{tashiro2021csdi,
  title={CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation},
  author={Tashiro, Yusuke and Song, Jiaming and Song, Yang and Ermon, Stefano},
  booktitle={Advances in Neural Information Processing Systems},
  volume={34},
  pages={24904--24917},
  year={2021}
}
```

## 🔗 Key References & Citation Graph
- Vault papers: [[2021_Rasul_TimeGrad_Diffusion_Forecasting]] (direct predecessor; RNN+diffusion forecaster), [[2020_Salinas_DeepAR_Probabilistic_Forecasting]], [[2017_Attention_Is_All_You_Need]] (Transformer encoder layers), [[2014_Kingma_Adam_Stochastic_Optimization]], [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] (diffusion applied to EV charging load), [[2021_Lim_TFT_Temporal_Fusion_Transformers]]
- Cited-in-text foundations: DDPM (Ho et al. 2020), score SDE (Song et al. 2021), DDIM (Song et al. 2021), DiffWave (Kong et al. 2021), GP-VAE (Fortuin et al. 2020), BRITS (Cao et al. 2018), GLIMA (Suo et al. 2020), mTANs (Shukla & Marlin 2021), Latent ODE (Rubanova et al. 2019), BERT masked modeling (Devlin et al. 2019), GP-copula (Salinas et al. 2019), Transformer MAF (Rasul et al. 2021), TLAE (Nguyen & Quanz 2021), PhysioNet Challenge 2012 (Silva et al. 2012), ST-MVL (Yi et al. 2016)
