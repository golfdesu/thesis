---
type: paper
title: "MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations"
authors: [Xingshuai Huang, Di Wu, Benoit Boulet]
year: 2023
journal_conference: "IEEE Transactions on Intelligent Transportation Systems, 24(10), 10445-10455"
doi_url: "https://doi.org/10.1109/TITS.2023.3276947"
models_used: ["[[MetaProbformer]]", "[[MetaProbformer]]", "[[Reptile]]", "[[Informer]]", "[[Transformer]]", "[[LSTM]]", "[[DeepAR]]", "[[Prophet]]", "[[ARIMA]]", "[[FPSeq2Q]]"]
datasets_used: ["[[Palo_Alto_EV|D_Palo (City of Palo Alto EV charging usage)]]", "[[Boulder_Colorado|D_Boulder]]", "[[ElaadNL|D_NL]]", "[[Perth_EV|D_Perth (Perth & Kinross)]]"]
features_used: ["[[Historical_Load|Univariate hourly average charging load (kW)]]", "[[Calendar_Features|Time-dependent covariates (month of year, etc.)]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[MSE]]", "[[RMSE]]", "[[CRPS]]", "[[Pinball_Loss|Normalized ρ-quantile loss Qρ]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations

## 🎯 Main Objective & Contribution
- First Transformer-based method for **probabilistic charging load forecasting of EV charging stations**, and first to address **newly built stations with scarce historical data** via meta-learning.
- Proposes **[[MetaProbformer]]** — an adaptation of [[Informer]] that outputs a **Gaussian predictive distribution** instead of point forecasts — and **[[MetaProbformer]]**, combining it with the [[Reptile]] meta-learning algorithm to learn a well-generalized initialization adaptable to unseen stations in few gradient steps.
- Contributions: (I) Probformer architecture (Informer → probabilistic); (II) Reptile-based meta-learning framework for scarce-data charging stations; (III) experiments covering point + probabilistic forecasting, short-term (1 h) + long-term (24/48/168 h), and homogeneous vs heterogeneous tasks.

## 🧠 Methodology & Model Architecture
**Equation 1 — Forecasting as conditional likelihood factorization:** $p(y_{i,t_0+1:t_0+\tau}\mid y_{i,1:t_0}, X_{1:t_0+\tau};\theta)=\prod_{t=t_0+1}^{t_0+\tau} p(y_{i,t}\mid y_{i,1:t-1}, X_{1:t};\theta)$

**Equation 2 — Scaled dot-product attention:** $O_h = \text{softmax}\left(\frac{Q_h K_h^T}{\sqrt{d_k}}\right)V_h$

**Equation 4 — ProbSparse query sparsity measurement** (max-mean KL divergence vs uniform attention):
$$\bar{S}(q_l,K) = \max_m\left\{\frac{q_l k_m^\top}{\sqrt{d}}\right\} - \frac{1}{d_k}\sum_{m=1}^{d_k}\frac{q_l k_m^\top}{\sqrt{d}}$$
Only top-$u$ "active" queries are computed after sampling $d_k \ln d_k$ pairs → complexity reduced from $O(L^2)$ to $O(L\ln L)$.

**Equation 5 — Self-attention distilling:** $Z_{u+1} = \text{MaxPool}\left(\text{ELU}(\text{Conv1d}([Z_u]_{PS}))\right)$

**Equations 6–7 — Probabilistic output:** forecasts modeled as Gaussians, $p(y_{i,t}|y_{i,1:t-1},X_{1:t})=\mathcal{N}(\mu_{i,t},\sigma_{i,t}^2)$, with $\mu=\text{Linear}(z)$ and $\sigma=\text{Softplus}(\text{Linear}(z))$ ensuring σ>0; Gaussian likelihood $p(y|\mu,\sigma)=(2\pi\sigma^2)^{-1/2}\exp(-(y-\mu)^2/2\sigma^2)$.

**Equation 8 — Negative log-likelihood training loss:** $\mathcal{L}(f_\theta)=\sum_{i=1}^{N}\sum_{t=t_0+1}^{t_0+\tau}-\log p(y_{i,t}|y_{i,1:t-1},X_{1:t};\theta)$ (point-forecast variant uses MSE loss).

**Equation 9 — Reptile inner-loop adaptation on task $\mathcal{T}_j$:** $\theta_j' \leftarrow \theta_j' - \alpha\nabla_{\theta_j'}\mathcal{L}_{\mathcal{T}_j}(f_{\theta_j'})$

**Equations 10–11 — Reptile meta-update:** $\theta \leftarrow \theta+\beta(\theta_j'-\theta)$, batch form $\theta \leftarrow \theta+\beta\frac{1}{J}\sum_{j=1}^{J}(\theta_j'-\theta)$ (no second-order derivatives unlike MAML, whose objective is Eq. 3).

Architecture: two-layer encoder + single-layer decoder (Informer setup); encoder input length 96, decoder input 48; generative-style decoder with zero-padded target ($Y_0$); halving distilling replicas mitigate information loss. Base learners optimized with Adam (lr 1e-4); meta-learner with SGD (lr 0.1); hyperparameters tuned by random search; standard normalization; test split 0.6:0.2:0.2; Intel i9-10900F + RTX 3070. Benefits justified via PAC-Bayesian bounds [43]–[45].

## 📊 Dataset & Input Features
Four real-world public datasets transformed to hourly average charging load (kW) series; each record has charging event start/end time and energy (kWh). **Univariate setting**: only load series + time-dependent covariates (weather/traffic unavailable from public sources).
- **$D_{Palo}$** — City of Palo Alto, CA, USA: 4 months, 3113 hourly data points. URL: https://data.cityofpaloalto.org/dataviews/241685/ELECT-VEHIC-CHARG-STATI-USAGE/
- **$D_{Boulder}$** — Boulder, CO, USA: 31 months, 22632 points. URL: https://open-data.bouldercolorado.gov/datasets/
- **$D_{NL}$** — ElaadNL, Netherlands: 12 months, 8760 points. URL: https://platform.elaad.io/analyses/ElaadNL_opendata.php
- **$D_{Perth}$** — Perth & Kinross, UK: 24 months, 17520 points; split non-overlapping into $D_{Perth1}$ (20 months, meta-training) and $D_{Perth2}$ (4 months, homogeneous test). URL: https://data.pkc.gov.uk/dataset/ev-charging-data
- Tasks: **homogeneous** = test on $D_{Perth2}$ (similar pattern to training); **heterogeneous** = test on $D_{Palo}$ (unseen pattern).
- Code availability: implementation + datasets at https://github.com/XingshuaiHuang/MetaProbformer ; Prophet baseline code https://facebook.github.io/prophet/

## 📈 Performance & Results
Point forecasting (MAE/MSE/RMSE, mean ± std over 5 random seeds; Tables III–IV): MetaProbformer beats all baselines.
- **Homogeneous task ($D_{Perth2}$)**: improvements of **3.614% MAE, 1.553% MSE, 0.773% RMSE** over the best baseline (MetaTransformer); Informer best among non-meta methods.
- **Heterogeneous task ($D_{Palo}$)**: lowest errors with **8.479% MAE, 5.834% MSE, 2.950% RMSE** improvement over MetaTransformer; ordering MetaProbformer < MetaTransformer < Informer < LSTM < Transformer < ARIMA.
- **Short-term probabilistic** (RMSE, Q50, Q90, CRPS; Tables V–VI): outperforms Transformer-P, MetaTransformer-P, DeepAR, FPSeq2Q, Probformer on all metrics for both tasks; average gains up to **3.620%** (homogeneous) and **5.319%** (heterogeneous). MetaTransformer-P best baseline, then Probformer → validates both the Reptile framework and Gaussian Probformer design.
- **Long-term probabilistic** (horizons 24, 48, 168 h on $D_{Palo}$): significantly outperforms all methods across every horizon/metric; accuracy degrades with horizon vs 1-h-ahead.
- **Input-length study** (24–336 h inputs): metrics generally improve with longer input; 336-h input best for short-term forecasting, 96 h comparable with lower compute.
- Overall (conclusion): average improvement of **3.87%** (point) and **2.19%** (probabilistic) over the best baselines.

## 💡 Limitations & Identified Research Gaps
- **Univariate only** — weather/traffic covariates missing from public datasets; multivariate extension left open.
- Requires *some* historical data: fails on brand-new stations with zero history — authors propose **zero-shot** generalization across heterogeneous station record systems as future work.
- Gaussian output assumption may underfit heavy-tailed/multimodal EV load distributions (vs quantile or diffusion models).
- Theoretical analysis limited to citing PAC-Bayesian bounds; no station-network/spatial modeling (single-station series only).
- Gap for thesis: combine few-shot adaptation ([[Reptile]]) with spatial information from nearby stations or mobility features (cf. [[2022_Cao_Robust_Deep_Gaussian_Process_Load]]) for cold-start stations.

## 📚 BibTeX & Citation Reference
```bibtex
@article{huang2023metaprobformer,
  title   = {MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations},
  author  = {Huang, Xingshuai and Wu, Di and Boulet, Benoit},
  journal = {IEEE Transactions on Intelligent Transportation Systems},
  volume  = {24},
  number  = {10},
  pages   = {10445--10455},
  year    = {2023},
  doi     = {10.1109/TITS.2023.3276947}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]]
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]]
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]]
- [[2018_Nichol_Reptile_First_Order_Meta_Learning]]
- [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]]
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]]
- [[1997_Hochreiter_Long_Short_Term_Memory]]
- [[2020_Huang_Ensemble_EV_Load]]
- [[2021_An_Ensemble_Methodology_for_Hierarchical_Probabilistic_EV_Load_Forecasting_at_Regular_Charging_Stations]]
- [[2021_Rasul_TimeGrad_Diffusion_Forecasting]]
