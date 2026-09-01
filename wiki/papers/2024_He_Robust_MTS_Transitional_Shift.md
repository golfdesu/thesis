---
type: paper
title: "Robust Multivariate Time Series Forecasting against Intra- and Inter-Series Transitional Shift"
authors: [Hui He, Qi Zhang, Kun Yi, Xiaojun Xue, Shoujin Wang, Liang Hu, Longbing Cao]
year: 2024
journal_conference: "arXiv preprint (IEEE journal template, Journal of LaTeX Class Files style); arXiv:2407.13194"
doi_url: "https://doi.org/10.48550/arXiv.2407.13194"
status: needs-review # efficiency-table numbers (Exchange row) internally inconsistent; rest verified
models_used: ["[[JointPGM]]"]
datasets_used: ["[[Exchange]]", "[[ETT]]", "[[Electricity_ECL]]", "[[Traffic]]", "[[ILI]]"]
features_used: ["[[Multivariate_Time_Series]]", "[[Temporal_Order_Features]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Robust Multivariate Time Series Forecasting against Intra- and Inter-Series Transitional Shift

## 🎯 Main Objective & Contribution
- Tackle **distribution shift** in non-stationary Multivariate Time Series (MTS) forecasting by decomposing the coarse-grained transitional shift into two finer-grained components:
  - **Intra-series transitional shift**: $P(x^{(i)}_{u:u+H}|x^{(i)}_{u-L:u}) \neq P(x^{(i)}_{v:v+H}|x^{(i)}_{v-L:v})$ for any two steps $u \neq v$ (Definition 1).
  - **Inter-series transitional shift**: transitional distribution of series $i$ conditioned on its complementary set changes across time (Definition 2).
- Argues normalization-based methods (RevIN, Dish-TS, SAN) assume a **time-invariant transition** between inputs and outputs and ignore inter-series dynamics; time-variant models (Koopa, meta-learning approaches) model transitions coarsely and remain black-box.
- Proposes **JointPGM** ("Joint Probabilistic Graphical Model"): a unified PGM that *jointly* captures intra-/inter-series correlations AND models the time-variant transitional distribution.
- Key contributions: (1) JointPGM framework built on a tailored PGM with theoretical guarantees; (2) dual learners — intra-series learner with temporal gates, inter-series learner with multi-hop propagation + Gumbel-softmax sampling; (3) SOTA on six highly non-stationary datasets with average improvement of **15.3% in MAE** and **37.9% in MSE** over all baselines.

## 🧠 Methodology & Model Architecture
Dual-encoder architecture with four components: **Time Factor Encoder (TFE)**, **Independence-based Series Encoder (ISE)** (intra-series learner + inter-series learner), **Dynamic Inference (DI)**, and **Decoder**.

### Problem Formulation
MTS forecasting task (**Eq. 1, Forecasting Map**):
$$X_{t-L:t} = F_\Theta(X_{t-L:t}) = F_\Theta(\{x^{(i)}_{t-L:t}\}_{i=1}^N)$$
with mapping $F_\Theta : \mathbb{R}^{N\times L} \to \mathbb{R}^{N\times H}$, lookback length $L$, horizon length $H$.

### 1) Time Factor Encoder (TFE)
Uses temporal orders spanning lookback + horizon windows ($[0,1]$-normalized order set $t$) instead of timestamps, concatenated multiple Fourier basis functions (**Eq. 2, Fourier Basis Features**):
$$M_t^{(0)} = \sin(2\pi B_1 t) | \cos(2\pi B_1 t) | ... | \sin(2\pi B_s t)| \cos(2\pi B_s t)$$
(**Eq. 3, Feed-Forward Projection**):
$$M_t^{(1)} = \mathrm{FeedForward}(M_t^{(0)})$$
where elements of $B_s \in \mathbb{R}^{\frac{b}{2s}}$ sampled from $\mathcal{N}(0,\sigma_s^2)$, scale hyperparameters $\sigma_s \in \{0.01, 0.1, 1, 5, 10, 20, 50, 100\}$, $b$ = Fourier feature size; mitigates 'spectral bias'. Gaussian sampling of latent $Z_t$ via reparameterization trick (**Eqs. 4–6, Time Factor Gaussian Sampling**):
$$\mu_t = f^\mu_t(M_t^{(1)}), \quad \sigma^2_t = f^{\sigma^2}_t(M_t^{(1)}), \quad \mathcal{P}(Z_t|t) = \mathcal{N}(\mu_t, \sigma^2_t I)$$

### 2) Independence-based Series Encoder (ISE)
Series-independence mechanism: each individual series encoded separately.

**Intra-series learner** — per-series linear embedding (**Eq. 7**):
$$h^{(i)}_{t-L:t} = \mathrm{Linear}(x^{(i)}_{t-L:t})$$
Temporal gate adjusted by learned time factors (**Eqs. 8–9, Temporal Gate**):
$$G = \mathrm{Sigmoid}(\mathrm{Linear}(M_t^{(1)}))$$
$$\hat{h}^{(i)}_{t-L:t} = G^{(i)} \odot h^{(i)}_{t-L:t}$$
Gaussian sampling of intra-series latent variable (**Eqs. 10–12**):
$$\mu_{\hat{z}} = f^\mu_{\hat{z}}(\hat{h}^{(i)}_{t-L:t}), \quad \sigma^2_{\hat{z}} = f^{\sigma^2}_{\hat{z}}(\hat{h}^{(i)}_{t-L:t}), \quad \mathcal{P}(\hat{z}^{(i)}_{t-L:t}|x^{(i)}_{t-L:t}, t) = \mathcal{N}(\mu_{\hat{z}}, \sigma^2_{\hat{z}}I)$$

**Inter-series learner** — input-conditioned adjacency via self-attention (**Eqs. 13–15, Attention Adjacency Matrix**):
$$Q_t = \hat{Z}_{t-L:t}W^Q_t, \quad K_t = \hat{Z}_{t-L:t}W^K_t, \quad W_t = \mathrm{Softmax}\left(\frac{Q_t K_t^T}{\sqrt{d}}\right)$$
Discrete graph structure learning via Gumbel reparameterization trick (**Eq. 16, Gumbel-softmax Edge Sampling**):
$$a_{ij,t} = \mathrm{Sigmoid}\left((\log(w_{ij,t}/(1-w_{ij,t}))) + (g^1_{ij,t} - g^2_{ij,t})/\tau\right), \text{ s.t. } g^1_{ij,t}, g^2_{ij,t} \sim \mathrm{Gumbel}(0,1)$$
with temperature parameter $\tau \in (0,\infty)$ (set to 0.5 in experiments). Multi-hop propagation, a simplified mix-hop propagation (**Eqs. 17–18, Multi-hop Propagation**):
$$\tilde{H}^{(k)}_{t-L:t} = A_t \tilde{H}^{k-1}_{t-L:t}, \quad \tilde{H}_{t-L:t} = \sum_{k=1}^{K}\mathrm{Linear}^{(k)}(\tilde{H}^{(k)}_{t-L:t})$$
Inter-series latent variable sampling (**Eqs. 19–21**):
$$\mu_{\tilde{Z}} = f^\mu_{\tilde{Z}}(\tilde{H}_{t-L:t}), \quad \sigma^2_{\tilde{Z}} = f^{\sigma^2}_{\tilde{Z}}(\tilde{H}_{t-L:t}), \quad \mathcal{P}(\tilde{Z}_{t-L:t}|X_{t-L:t}, t) = \mathcal{N}(\mu_{\tilde{Z}}, \sigma^2_{\tilde{Z}}I)$$

### 3) Fusion & Dynamic Inference (DI)
Latent fusion regulated by trade-off parameter α (**Eq. 22, Latent Variable Fusion**):
$$Z_{t-L:t} = \alpha\hat{Z}_{t-L:t} + (1-\alpha)\tilde{Z}_{t-L:t}$$
DI reversely infers time factors from series latents (**Eqs. 23–25, Dynamic Inference**):
$$\hat{Z}_t = \mathrm{Linear}(Z_{t-L:t}), \quad \mu_{\hat{t}} = f^\mu_{\hat{t}}(\hat{Z}_t), \quad \sigma^2_{\hat{t}} = f^{\sigma^2}_{\hat{t}}(\hat{Z}_t)$$

### 4) Decoder
One-forward-step reconstruction + prediction (avoids error accumulation), two linear layers with LeakyReLU (**Eqs. 26–27, Decoder**):
$$\hat{X}_{t-L:t} = \mathrm{FeedForward}_{rec}(Z_{t-L:t}), \quad \hat{X}_{t:t+H} = \mathrm{FeedForward}_{pre}(Z_{t-L:t})$$

### Objective Decomposition
KL-divergence objective between transitional distributions (**Eq. 28**):
$$\mathcal{L} = \mathrm{KL}[\mathcal{P}_\psi(X_H, Z_L, Z_t|X_L)\,||\,\mathcal{P}_\phi(X_H, Z_L, Z_t|X_L, t)]$$
Decomposed via Proposition 1 into three terms (**Eq. 29**):
$$\mathcal{L} = \underbrace{\mathrm{KL}[\mathcal{P}_\psi(Z_L|X_L)||\mathcal{P}_\phi(Z_L|X_L,t)]}_{(a)} + \underbrace{\mathbb{E}_{Z_L \sim \mathcal{P}_\psi(Z_L|X_L)}\mathrm{KL}[\mathcal{P}_\theta(Z_t|Z_L)||\mathcal{P}_\phi(Z_t|t)]}_{(b)} + \underbrace{\mathbb{E}_{(Z_L,Z_t)\sim\mathcal{P}_\psi(Z_L,Z_t|X_L)}\mathrm{KL}[\mathcal{P}_\psi(X_H|Z_L)||\mathcal{P}_\phi(X_H|X_L,t)]}_{(c)}$$
Term (a) constrained by ELBO (**Eq. 30, Reconstruction Loss $L_a$**):
$$L_a = -\mathrm{ELBO} = -\mathbb{E}_{Z_L}[\log \mathcal{P}(X_L|Z_L)] + \mathrm{KL}[\mathcal{P}_\psi(Z_L|X_L)||\mathcal{P}(Z_L)] = l(\hat{X}_L - X_L) + (-\log\sigma_Z + \frac{1}{2}\sigma^2_Z + \frac{1}{2}\mu_Z^2 - \frac{1}{2})$$
Term (b) aligns inferred vs. encoded time-factor distributions (**Eq. 31, Dynamic Inference Loss $L_b$, Gaussian KL**):
$$L_b = -\log\frac{\sigma_{\hat{t}}}{\sigma_t} + \frac{1}{2}\frac{\sigma^2_{\hat{t}}}{\sigma^2_t} + \frac{1}{2}\frac{(\mu_{\hat{t}}-\mu_t)^2}{\sigma^2_t} - \frac{1}{2}$$
Term (c) is prediction consistency (**Eq. 32**): $L_c = l(\hat{X}_H - X_H)$ (MSE).
Total loss (**Eq. 33, Overall Loss**):
$$\mathcal{L} = L_a + L_b + L_c$$

Implementation: PyTorch, NVIDIA RTX 4090 24GB; latent dim $d = 128$, propagation depth $K=2$, $\tau = 0.5$, Adam optimizer lr 1e-3, batch size 128; z-score normalization; train/val/test split 7:1:2; each experiment run 3 times with different seeds.

## 📊 Dataset & Input Features
Six highly non-stationary benchmarks (non-stationarity quantified by Augmented Dickey-Fuller (ADF) test statistic — larger = more severe distribution shift):

| Dataset | Variables | Interval | Time Steps | ADF Statistic |
|---|---|---|---|---|
| Exchange | 8 | 1 day | 7588 | -1.902 |
| ETTm2 | 7 | 15 minutes | 69680 | -5.664 |
| ETTh1 | 7 | 1 hour | 17420 | -5.909 |
| Electricity | 321 | 1 hour (collected every 15 min since 01/01/2011, 321 clients) | 26304 | -8.445 |
| METR-LA | 207 | 5 minutes (LA County highway loop detectors, 01/03/2012–30/06/2012) | 34272 | -15.021 |
| ILI | 7 | 1 week (CDC influenza-like illness ratio, 2002–2021) | 966 | -5.334 |

Dataset URLs:
- Exchange: https://github.com/laiguokun/multivariate-time-series-data
- ETT (ETTh1, ETTm2): https://github.com/zhouhaoyi/ETDataset
- Electricity: https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- METR-LA: https://github.com/liyaguang/DCRNN (source data: http://pems.dot.ca.gov)
- ILI: https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
- Weather (excluded, too stationary): https://www.bgc-jena.mpg.de/wetter/

Baseline code repositories: Koopa https://github.com/thuml/Koopa ; Nonstationary Transformers https://github.com/thuml/Nonstationary_Transformers ; DLinear https://github.com/honeywell21/DLinear ; PatchTST https://github.com/PatchTST ; FEDformer https://github.com/MAZiqing/FEDformer ; Autoformer https://github.com/thuml/Autoformer ; iTransformer https://github.com/thuml/iTransformer ; Crossformer https://github.com/Thinklab-SJTU/Crossformer ; WaveForM https://github.com/alanyoungCN/WaveForM ; SAN https://github.com/icantnamemyself/SAN ; Dish-TS https://github.com/weifantt/Dish-TS ; RevIN https://github.com/ts-kim/RevIN .

Input features: raw multivariate series values within lookback window $X_{t-L:t}$ plus temporal-order features $t=\{0,...,\frac{i+L}{L+H-1},...,1\}$ spanning both lookback and horizon windows (order features preferred over timestamp embeddings due to spectral bias).

## 📈 Performance & Results
Metrics: MAE and MSE (lower better). Lookback 96 (ILI: 24).

**vs. nine baselines (Table II)** — JointPGM best in ~80% of settings; selected results (MAE/MSE):
- Exchange H=96: JointPGM 0.199/0.076 vs. best baseline iTransformer 0.206/0.086 → **13.2% MSE reduction (0.086→0.076)**.
- ILI H=24: JointPGM 1.354/3.818 vs. Koopa 1.285/3.697 (Koopa wins here); ILI H=48: 4.8% MSE reduction over SOTA (4.000→3.818).
- METR-LA H=96: 0.622/1.041 vs. next-best WaveForM 0.684/1.114.
- Electricity H=96: 0.256/0.161 (best MSE; PatchTST MSE 0.168).
- Average reduction vs. Koopa: **2.7% MAE and 9.3% MSE**.

**vs. normalization methods (Table III, L/H=96/96, ILI 24/48)**: JointPGM best in ~92% of comparisons. Exchange: 0.199/0.076 vs. FEDformer+SAN 0.206/0.080 → **5.3% MSE reduction**; ILI: 1.340/3.640 vs. FEDformer+SAN 1.354/3.880 → **6.6% MSE reduction**. JointPGM's MAE can be slightly worse than baselines because its loss uses two MSE terms (prediction + reconstruction), prioritizing MSE.

**Ablation (Table IV, H=192; ILI H=48, MAE/MSE)**: w/o DI 0.293→0.299/0.155→0.162 (Exchange); w/o OF (timestamp instead of order features) worse; w/o ISE(A) Exchange 0.426/0.331, w/o ISE(F) 0.492/0.458 (large degradation); w/o IL and w/o TG each degrade slightly. Full JointPGM Exchange 0.293/0.155, ETTh1 0.484/0.491, Electricity 0.279/0.187, ILI 1.340/3.640.

**Efficiency**: On Exchange (8 vars) vs. Koopa: **77.6% training-time reduction**, memory footprint 94.9% of Koopa (JointPGM 2.5GB/39.4s vs. Koopa 5.9GB/21.6s). On ETTm2 vs. Koopa: 58.9% training-time reduction, 97.8% memory footprint (JointPGM 2.3GB/14.2s vs. Koopa 2.3GB/34.5s). On Electricity (321 vars): speed comparable to PatchTST with lower memory (JointPGM 3.9GB/39.4s vs. PatchTST 16.2GB/41.5s, Crossformer 16.7GB/101.2s).
> ⚠️ Numeric caveat: on Exchange the quoted wall-clock seconds (JointPGM 39.4 s vs. Koopa 21.6 s) contradict the claimed 77.6% training-*time* reduction — likely the 39.4 s figure belongs to another row/model (the same 39.4 s appears under Electricity). Verify against the paper's efficiency table before quoting.

Hyperparameter sensitivity: moderate α optimal (<0.6 fluctuates wildly); propagation depth K≈2 optimal (over-smoothing beyond); longer lookback (up to 720) consistently improves JointPGM unlike Transformer baselines.

## 💡 Limitations & Identified Research Gaps
- Authors' stated future work: exploring time-variant dynamics on **higher-dimensional MTS data** and further improving **efficiency**.
- Slightly inferior MAE vs. MSE-only-trained baselines due to dual reconstruction+prediction MSE losses (bias of objective function).
- Sensitive to trade-off parameter α (violent fluctuation when α < 0.6); requires tuning.
- Multi-hop propagation suffers over-smoothing for larger depth K.
- Evaluated only on generic non-stationary benchmarks (Exchange, ETT, Electricity, METR-LA, ILI) — no direct evaluation on EV charging station load, though electricity consumption planning is listed among motivating applications.
- Research gap for thesis: probabilistic/fine-grained transitional-shift decomposition could be applied to non-stationary EV charging loads where intra-station dynamics and inter-station spatial correlation both shift.

## 📚 BibTeX & Citation Reference
```bibtex
@article{he2024jointpgm,
  title   = {Robust Multivariate Time Series Forecasting against Intra- and Inter-Series Transitional Shift},
  author  = {He, Hui and Zhang, Qi and Yi, Kun and Xue, Xiaojun and Wang, Shoujin and Hu, Liang and Cao, Longbing},
  journal = {arXiv preprint arXiv:2407.13194},
  year    = {2024},
  url     = {https://arxiv.org/abs/2407.13194},
  doi     = {10.48550/arXiv.2407.13194}
}
```

## 🔗 Key References & Citation Graph
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]] — RevIN [27], the reversible instance normalization this work explicitly critiques for assuming a time-invariant transitional distribution; JointPGM outperforms RevIN-augmented backbones in Table III/VI.
- Dish-TS [21] (Fan et al., AAAI 2023) and SAN [28] (Liu et al., NeurIPS 2023) — other adaptive-normalization baselines directly compared.
- Koopa [35] (Liu et al., NeurIPS 2023) and KNF [53] (Wang et al., ICLR 2023) — Koopman-operator time-variant predictors; closest conceptual competitor.
- Non-stationary Transformer / Stationary [22] (Liu et al., NeurIPS 2022) — de-stationary attention baseline.
- iTransformer [50] (ICLR 2024), Crossformer [49] (ICLR 2023), PatchTST [14] (ICLR 2023), Autoformer [13] (NeurIPS 2021), FEDformer [15] (ICML 2022), DLinear [44] (AAAI 2023), WaveForM [19] (AAAI 2023) — general forecasting baselines.
- Graph WaveNet [16]/MTGNN [18] (Wu et al.) — source of mix-hop propagation idea simplified into multi-hop propagation.
- Fourier feature literature [54] Tancik et al. (NeurIPS 2020), [55] Woo et al. (ICML 2023) — basis for the TFE design.
- Related vault lines: [[2019_Zhu_EV_Load_Forecasting]], [[2020_Huang_Ensemble_EV_Load]], [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] — application-domain counterparts whose EV load series exhibit exactly the kind of non-stationarity/transitional shift this method targets.
