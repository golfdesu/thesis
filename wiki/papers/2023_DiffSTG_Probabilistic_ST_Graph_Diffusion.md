---
type: paper
title: "DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models"
authors: [Haomin Wen, Youfang Lin, Yutong Xia, Huaiyu Wan, Qingsong Wen, Roger Zimmermann, Yuxuan Liang]
year: 2023
journal_conference: "ACM conference proceedings (© 2023 ACM); arXiv:2301.13629 (v4, Mar 2024)"
doi_url: "https://doi.org/10.48550/arXiv.2301.13629"
models_used: ["[[DiffSTG]]", "[[UGnet]]"]
datasets_used: ["[[Traffic]]", "[[AIR-BJ]]", "[[AIR-GZ]]"]
features_used: ["[[Traffic]]", "[[PM2.5_Concentration]]", "[[Adjacency_Matrix]]", "[[Noise_Level_Embedding]]"]
forecasting_horizon: "[[Spatial_Temporal_Forecasting]]"
metrics: ["[[CRPS]]", "[[MAE]]", "[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models

## 🎯 Main Objective & Contribution
First work to generalize Denoising Diffusion Probabilistic Models (DDPM) to **spatio-temporal graphs (STGs)**, yielding **DiffSTG**, a non-autoregressive probabilistic forecasting framework, plus the first DDPM denoising network dedicated to STGs, **UGnet** (Unet-based temporal architecture + GNN spatial modeling). Deterministic STGNNs cannot quantify prediction uncertainty, crippling downstream decision-making; existing diffusion time-series models (TimeGrad, CSDI) model single-node temporal dynamics only, miss spatial correlations, and suffer sequential train/inference inefficiency. DiffSTG reduces CRPS by 4%–14% and RMSE by 2%–7% over existing methods on three real-world datasets. **Relevance to EV charging load forecasting:** provides the conditional-diffusion machinery for *probabilistic* spatio-temporal load forecasting — directly relevant to quantifying uncertainty bands around EV charging-station load predictions for grid operations.

## 🧠 Methodology & Model Architecture
**DDPM background.**
*Forward Markov process (Eqs. 1–2)* with variance schedule $\{\beta_1,\dots,\beta_N\}$, $\beta_n \in (0,1)$:
$$q(\boldsymbol{x}_{1:N}|\boldsymbol{x}_0)=\prod_{n=1}^{N}q(\boldsymbol{x}_n|\boldsymbol{x}_{n-1}), \qquad q(\boldsymbol{x}_n|\boldsymbol{x}_{n-1}) = \mathcal{N}\big(\boldsymbol{x}_n;\sqrt{1-\beta_n}\boldsymbol{x}_{n-1},\beta_n\mathbf{I}\big)$$
*Closed-form marginal via reparameterization (Eq. 3)* with $\hat\alpha_n=1-\beta_n$, $\alpha_n=\prod_{i=1}^{n}\hat\alpha_i$:
$$q(\boldsymbol{x}_n|\boldsymbol{x}_0)=\mathcal{N}(\boldsymbol{x}_n;\sqrt{\alpha_n}\boldsymbol{x}_0,(1-\alpha_n)\mathbf{I})$$
*Learnable reverse process (Eqs. 4–5):*
$$p_\theta(\boldsymbol{x}_{0:N})=p(\boldsymbol{x}_N)\prod_{n=N}^{1}p_\theta(\boldsymbol{x}_{n-1}|\boldsymbol{x}_n), \qquad p_\theta(\boldsymbol{x}_{n-1}|\boldsymbol{x}_n)=\mathcal{N}(\boldsymbol{x}_{n-1};\mu_\theta(\boldsymbol{x}_n,n),\sigma_\theta(\boldsymbol{x}_n,n))$$
*Parameterization (Eqs. 6–7)*:
$$\mu_\theta(\boldsymbol{x}_n,n)=\frac{1}{\sqrt{\alpha_n}}\Big(\boldsymbol{x}_n-\frac{\beta_n}{\sqrt{1-\alpha_n}}\boldsymbol{\epsilon}_\theta(\boldsymbol{x}_n,n)\Big), \qquad \sigma_\theta(\boldsymbol{x}_n,n)=\sqrt{\frac{1-\alpha_{n-1}}{1-\alpha_n}}\beta_n$$
*Simplified training objective (Eq. 8):*
$$\min_\theta L(\theta)=\min_\theta \mathbb{E}_{\boldsymbol{x}_0\sim q(\boldsymbol{x}_0),\,\boldsymbol{\epsilon}\sim\mathcal{N}(0,\mathbf{I}),\,n}\big\|\boldsymbol{\epsilon}-\boldsymbol{\epsilon}_\theta\big(\sqrt{\alpha_n}\boldsymbol{x}_0+\sqrt{1-\alpha_n}\boldsymbol{\epsilon},n\big)\big\|_2^2$$

**DiffSTG formulation.** Graph $G=\{V,E,A\}$, signals $\mathbf{x}^t\in R^{F\times V}$; forecast horizon $T_p$ (Eq. 9):
$$\mathcal{F}: (\boldsymbol{x}_h; G)\to [x^{T_h+1},\cdots,x^{T_h+T_p}] := \boldsymbol{x}_p$$
*Conditional reverse process (Eqs. 10–11)* — history $\boldsymbol{x}_h$ and graph $G$ condition the denoising transitions; conditional loss (Eq. 12):
$$p_\theta(\boldsymbol{x}_{0:N}^p|\boldsymbol{x}_h,G)=p(\boldsymbol{x}_N^p)\prod_{n=N}^{1}p_\theta(\boldsymbol{x}_{n-1}^p|\boldsymbol{x}_n^p,\boldsymbol{x}_h,G), \quad \min_\theta L(\theta)=\min_\theta\mathbb{E}_{\boldsymbol{x}_0^p,\boldsymbol{\epsilon}}\big\|\boldsymbol{\epsilon}-\epsilon_\theta(\boldsymbol{x}_n^p,n|\boldsymbol{x}_h,G)\big\|_2^2$$
*Generalized masked formulation (Eqs. 13–14)* — history and future unified as $\boldsymbol{x}^{all}=[\boldsymbol{x}_h,\boldsymbol{x}_p]\in R^{F\times V\times T}$ ($T=T_h+T_p$), with history represented by masking future steps $\boldsymbol{x}^{all}_{msk}$; this unifies STG prediction/generation/interpolation in one framework and fully utilizes historical data:
$$p_\theta(\boldsymbol{x}_{0:N}^{all}|\boldsymbol{x}_{msk}^{all},G)=p(\boldsymbol{x}_N^{all})\prod_{n=N}^{1}p_\theta(\boldsymbol{x}_{n-1}^{all}|\boldsymbol{x}_n^{all},\boldsymbol{x}_{msk}^{all},G)$$
$$\min_\theta L(\theta)=\min_\theta\mathbb{E}_{\boldsymbol{x}_0^{all},\boldsymbol{\epsilon}}\big\|\boldsymbol{\epsilon}-\epsilon_\theta(\boldsymbol{x}_n^{all},n|\boldsymbol{x}_{msk}^{all},G)\big\|_2^2$$
**Non-autoregressive inference:** one reverse diffusion process generates all $T_p$ steps at once (vs TimeGrad's $T_p$ runs). Training/sampling given as Algorithms 1–2.

**Denoising network UGnet** $\boldsymbol{\epsilon}_\theta(\mathbf{X}^{all}\times R|\mathbf{X}^{all}_{msk},G)\to\mathbf{X}^{all}$: concatenates $\boldsymbol{x}^{all}_n$ and $\boldsymbol{x}^{all}_{msk}$ temporally → linear projection to $H\in R^{C\times V\times 2T}$ → stacked **ST-Residual Blocks** (down/up-sampling Unet structure over the temporal dimension) each with:
*Temporal gated causal convolution (Eq. 15)*, kernel $\Gamma_T\in R^{K\times C_{in}^t\times C_{out}^t}$, Hadamard product $\odot$, sigmoid gate $\sigma(Q_i)$:
$$\Gamma_T(H_i)=P_i\odot\sigma(Q_i)\in R^{C_{out}^t\times V\times T_i}$$
*Graph convolution (Eq. 16)* with vanilla GCN aggregation $\Phi_{gcn}=A_{gcn}H_i$, $A_{gcn}=D^{-\frac12}(A+I)D^{-\frac12}$, degree matrix $D_{ii}=\sum_j(A+I)_{ij}$:
$$\Gamma_G(H_i)=\sigma\big(\Phi(A_{gcn},H_i)W_i\big)$$
*Noise level embedding (Eq. 17)* — transformer positional encoding of $n\in[1,N]$, $d\le D/2$ dims, constant $r=10000$:
$$e(n)=[\dots,\cos(n/r^{-2d/D}),\sin(n/r^{-2d/D}),\dots]^T$$
*Accelerated sampling (Eq. 18)* — DDIM-style subset sampling of $M$ steps $\{\tau_1,\dots,\tau_M\}$ from $N$:
$$\boldsymbol{x}_{\tau_{m-1}}=\sqrt{\alpha_{\tau_{m-1}}}\Big(\frac{\boldsymbol{x}_{\tau_m}-\sqrt{1-\alpha_{\tau_m}}\,\epsilon_\theta^{(\tau_m)}}{\sqrt{\alpha_{\tau_m}}}\Big)+\sqrt{1-\alpha_{\tau_{m-1}}-\sigma_{\tau_m}^2}\cdot\epsilon_\theta^{(\tau_m)}+\sigma_{\tau_m}\boldsymbol{\epsilon}_{\tau_m}$$
plus reusing last-$k$ reverse steps as samples, reducing required processes from $S$ to $S/k$. Total cost $\tilde S\times\tilde N$ steps with $\tilde S=S/k<S$, $\tilde N=M<N$.

## 📊 Dataset & Input Features
| Dataset | Location / Period | Nodes | Signal ($F$) | Resolution | #Samples |
|---|---|---|---|---|---|
| PEMS08 | San Francisco Bay Area highways (Caltrans PeMS), extracted by STSGCN | 170 | Traffic flow | 5 minutes | 17,856 |
| AIR-BJ | Beijing, China, 2019/01/01–2019/12/31 | 34 stations | PM2.5 | 1 hour | 8,760 |
| AIR-GZ | Guangzhou, China, 2017/01/01–2017/12/31 | 41 stations | PM2.5 | 1 hour | 8,760 |

Adjacency construction: PEMS08 — sensors connected if on same road (actual road network); AIR-BJ/AIR-GZ — distance between monitoring stations. Splits chronological 6:2:2; $T_h=T_p=12$; batch size 8; Adam lr 0.002 halved every 5 epochs; quadratic variance schedule $\beta_n=(\frac{N-n}{N-1}\sqrt{\beta_1}+\frac{n-1}{N-1}\sqrt{\beta_N})^2$ with $\beta_1=10^{-4}$, hidden size $C=32$, searched $N\in[50,100,200]$, $\beta_N\in[0.1,0.2,0.3,0.4]$.
- Code (official, verified in text): https://github.com/wenhaomin/DiffSTG
- No dataset download URLs appear in the PDF text.

## 📈 Performance & Results
**Probabilistic comparison (Table 2, MAE/RMSE/CRPS), DiffSTG best everywhere:**

| Method | AIR-BJ | AIR-GZ | PEMS08 |
|---|---|---|---|
| Latent ODE | 20.61 / 32.27 / 0.47 | 12.92 / 18.76 / 0.30 | 26.05 / 39.50 / 0.11 |
| DeepAR | 20.15 / 32.09 / 0.37 | 11.77 / 17.45 / 0.23 | 21.56 / 33.37 / 0.07 |
| CSDI | 26.52 / 40.33 / 0.50 | 13.75 / 19.40 / 0.28 | 32.11 / 47.40 / 0.11 |
| TimeGrad | 18.64 / 31.86 / 0.36 | 12.36 / 18.15 / 0.25 | 24.46 / 38.06 / 0.09 |
| MC Dropout | 20.80 / 40.54 / 0.45 | 11.12 / 17.07 / 0.25 | 19.01 / 29.35 / 0.07 |
| **DiffSTG** | **17.88 / 29.60 / 0.34** | **10.95 / 16.66 / 0.22** | **17.68 / 27.13 / 0.06** |
| Error reduction | −4.1% / −7.1% / −5.6% | −1.5% / −2.4% / −4.3% | −7.0% / −7.6% / −14.3% |

CRPS reduced by 5.6%, 4.3%, 14.3% vs most competitive baseline per dataset.

**Inference speed (Table 3, AIR-GZ, $N=100$):** TimeGrad 9.58 s (S=8) / 128.40 s (S=16) / 672.12 s (S=32); DiffSTG (M=100,k=1) 0.24 / 0.48 / 0.95 s → **40× speed-up vs TimeGrad**; accelerated strategy gives a further 3~4× (M=40,k=2: 0.07 / 0.12 / 0.21 s). Parameter count (Table 6): DiffSTG 149,305 vs TimeGrad 52,423, CSDI 48,289, MC Dropout 371,393.

**Deterministic gap (Table 5):** DiffSTG is inferior to SOTA deterministic STGNNs — e.g., PEMS08: GMSDR MAE 16.01 / RMSE 24.84 and STGNCDE 15.83 / 25.05 beat DiffSTG's 17.68 / 27.13 (DCRNN 18.56 / 28.73; STGCN 20.15 / 30.14).

**Ablations (AIR-GZ):** removing GNN (w/o Spatial), TCN (w/o Temporal), or the Unet structure each degrades performance substantially. Hyperparameters: kernel $K=3$ best in TCN (MAE 13.38 vs 13.85–14.86 for K∈{2,4,5}); $S>32$ samples give marginal gains; $k=2$ ≈ k=1 when $S>32$ with ~1.5× faster sampling.

## 💡 Limitations & Identified Research Gaps
- Explicitly acknowledged: DiffSTG still trails state-of-the-art **deterministic** STGNNs (e.g., GMSDR, STGNCDE) because its variational-inference objective yields an inaccurate posterior when data samples are insufficient — improving this is left as future work.
- Only vanilla GCN used in UGnet for simplicity; incorporating more powerful GNNs to better capture ST dependencies is open.
- Future direction: applying DiffSTG to other spatio-temporal tasks such as STG imputation.
- Diffusion sampling remains multi-step at inference even with acceleration; parameter count larger than TimeGrad/CSDI.

## 📚 BibTeX & Citation Reference
```bibtex
@article{wen2023diffstg,
  title   = {DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models},
  author  = {Wen, Haomin and Lin, Youfang and Xia, Yutong and Wan, Huaiyu and Wen, Qingsong and Zimmermann, Roger and Liang, Yuxuan},
  journal = {arXiv preprint arXiv:2301.13629},
  year    = {2023},
  doi     = {10.48550/arXiv.2301.13629}
}
```

## 🔗 Key References & Citation Graph
- Extends DDPM (Ho et al., NeurIPS 2020) to graphs; conditions like [[2021_CSDI_Conditional_Diffusion_Forecasting]] (CSDI, ref [36]) but adds spatial conditioning + non-autoregressive generation; compares against TimeGrad (Rasul et al., ICML 2021), DeepAR, Latent ODE, MC Dropout (Wu et al., KDD 2021).
- Contrasts WaveNet-based denoising networks with [[2019_Graph_WaveNet_Spatial_Temporal_Modeling]] (cited as ref [44]); deterministic baselines include DCRNN (Li et al., ICLR 2018) and STGCN (Yu et al., IJCAI 2018).
- Related vault context: probabilistic uncertainty quantification complements deterministic EV station models [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]], [[2024_Physics_Informed_GAT_EV_Load]]; diffusion-based load forecasting lineage continues toward [[2026_Mamba_KAN_HyKANet_EV]]-era architectures.
