---
type: paper
title: "Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting"
authors: [Yunhao Zhang, Junchi Yan]
year: 2023
journal_conference: "ICLR 2023"
doi_url: "https://arxiv.org/abs/2301.03982"
models_used: ["[[Crossformer]]", "[[DSW_Embedding]]", "[[Two_Stage_Attention]]", "[[Hierarchical_Encoder_Decoder]]", "[[Router_Attention]]"]
datasets_used: ["[[ETTh1]]", "[[ETTm1]]", "[[Weather]]", "[[Electricity_ECL]]", "[[ILI]]", "[[Traffic_PEMS]]"]
features_used: ["[[Multivariate_Time_Series]]", "[[Cross_Time_Dependency]]", "[[Cross_Dimension_Dependency]]", "[[Segment_Embeddings]]", "[[Multi_Scale_Representations]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting

## 🎯 Main Objective & Contribution
- Identifies that existing Transformer-based MTS models embed all dimensions at one time step into a single vector and only model **cross-time dependency**, omitting **cross-dimension (cross-variate) dependency** — critical when series are associated (e.g., temperature ↔ wind speed; correlated EV charging stations).
- Proposes [[Crossformer]] — among the first Transformers to explicitly exploit cross-dimension dependency — via three components: **Dimension-Segment-Wise (DSW) embedding** into a 2D vector array (time × dimension), **Two-Stage Attention (TSA)** layer with a router mechanism, and a **Hierarchical Encoder-Decoder (HED)** using multi-scale information.
- Ranks top-1 in 36/58 settings and top-2 in 51/58 against 8 baselines across six real-world benchmarks.

## 🧠 Methodology & Model Architecture
Task: predict $x_{T+1:T+\tau} \in \mathbb{R}^{\tau \times D}$ from history $x_{1:T} \in \mathbb{R}^{T \times D}$ ($D$ = number of dimensions).
- **DSW embedding** — partition each dimension into segments of length $L_{seg}$, embed each segment via learnable linear projection + position embedding:
$$x_{1:T} = \left\{ x^{(s)}_{i,d} \,\middle|\, 1 \le i \le \tfrac{T}{L_{seg}},\, 1 \le d \le D \right\}, \quad x^{(s)}_{i,d} = \left\{ x_{t,d} \mid (i-1)L_{seg} < t \le i L_{seg} \right\}$$
$$h_{i,d} = E x^{(s)}_{i,d} + E^{(pos)}_{i,d}, \quad E \in \mathbb{R}^{d_{model}\times L_{seg}},\ E^{(pos)}_{i,d} \in \mathbb{R}^{d_{model}}$$
Motivation: attention maps of vanilla Transformers naturally segment (Fig. 1a); a single scalar carries little semantics unlike words.
- **Two-Stage Attention (TSA) layer**, input $Z \in \mathbb{R}^{L\times D\times d_{model}}$:
  - *Cross-Time Stage* (MSA along segments within each dimension; complexity $O(DL^2)$):
$$\hat{Z}^{time}_{:,d} = \text{LayerNorm}\left(Z_{:,d} + \text{MSA}_{time}(Z_{:,d}, Z_{:,d}, Z_{:,d})\right), \qquad Z^{time} = \text{LayerNorm}\left(\hat{Z}^{time} + \text{MLP}(\hat{Z}^{time})\right)$$
  - *Cross-Dimension Stage* with **router mechanism**: $c \ll D$ learnable routers per time step first aggregate from all dimensions (routers as query), then distribute back — reduces $O(D^2L)$ to $O(DL)$:
$$B_{i,:} = \text{MSA}^{dim}_1(R_{i,:}, Z^{time}_{i,:}, Z^{time}_{i,:}), \qquad Z^{dim}_{i,:} = \text{MSA}^{dim}_2(Z^{time}_{i,:}, B_{i,:}, B_{i,:})$$
$$\hat{Z}^{dim} = \text{LayerNorm}(Z^{time} + Z^{dim}), \qquad Z^{dim} = \text{LayerNorm}(\hat{Z}^{dim} + \text{MLP}(\hat{Z}^{dim}))$$
  - Combined: $Y = Z^{dim} = \text{TSA}(Z)$; overall TSA complexity $O(DL^2 + DL) = O(DL^2)$.
- **HED encoder** — segment merging every two adjacent time vectors per layer + TSA at coarser scales ($M \in \mathbb{R}^{d_{model}\times 2d_{model}}$ learnable merger):
$$l>1:\ \hat{Z}^{enc,l}_{i,d} = M[Z^{enc,l-1}_{2i-1,d} \cdot Z^{enc,l-1}_{2i,d}], \qquad Z^{enc,l} = \text{TSA}(\hat{Z}^{enc,l})$$
- **HED decoder** — $N+1$ layers; each consumes the corresponding encoder scale plus cross-attention to it, initialized by learnable decoder position embedding $E^{(dec)} \in \mathbb{R}^{\frac{\tau}{L_{seg}}\times D\times d_{model}}$:
$$\tilde{Z}^{dec,l} = \text{TSA}(Z^{dec,l-1})\ (\text{or } \text{TSA}(E^{(dec)}) \text{ if } l=0), \qquad Z'^{dec,l}_{:,d} = \text{MSA}(\tilde{Z}^{dec,l}_{:,d}, Z^{enc,l}_{:,d}, Z^{enc,l}_{:,d})$$
- **Multi-scale prediction sum** — per-layer linear projections $W_l \in \mathbb{R}^{L_{seg}\times d_{model}}$, summed over layers:
$$x^{pred,l}_{T+1:T+\tau} = \text{rearrange}\left(W_l Z^{dec,l}_{i,d}\right), \qquad x^{pred}_{T+1:T+\tau} = \sum_{l=0}^{N} x^{pred,l}_{T+1:T+\tau}$$
- Config: 3 encoder layers, $c=10$ routers, $d_{model}=256$ / 4 heads (ETTh1, ETTm1, WTH, ILI) or 64 / 2 heads (ECL, Traffic); $L_{seg}$ grid-searched from {6,12,24}; MSE loss, Adam (LR grid {5e-3…1e-5}), batch 32, 20 epochs w/ early stop (patience 3); PyTorch on Quadro RTX 8000 48GB. Padding scheme handles indivisible lengths (Eq. 9); covariate embedding extension proposed (Eq. 10) but found not to help.

## 📊 Dataset & Input Features
Six real-world benchmarks: ETTh1 (7 indicators, hourly, 12/4/4 months train/val/test); ETTm1 (same indicators, 15-min); WTH/Weather (12 US meteorological indicators, 4 years, 28/10/10 months); ECL/Electricity (hourly kWh consumption of 321 clients, 2 years, 15/3/4 months); ILI (7 weekly CDC patient indicators, 2002–2021, split 0.7:0.1:0.2); Traffic (hourly road occupancy of 862 SF Bay Area freeway sensors, 2 years, 0.7:0.1:0.2). Past window $T$ searched per horizon from {24,48,96,168,336,720} (ETTm1: {24,…,288,672}; ILI: {24,…,60}); rolling stride 1; zero-mean normalization by training stats; metrics MSE/MAE averaged over 5 runs. Crossformer uses past series only — baselines additionally use timestamp covariates (hour-of-day etc.).
Data URLs (appendix footnotes):
- Code: https://github.com/Thinklab-SJTU/Crossformer
- ETTh1/ETTm1/WTH/ECL: https://github.com/zhouhaoyi/Informer2020
- ILI/Traffic: https://github.com/thuml/Autoformer
- Baseline code: LSTNet https://github.com/laiguokun/LSTNet ; MTGNN https://github.com/nnzhan/MTGNN ; Autoformer https://github.com/thuml/Autoformer ; Pyraformer https://github.com/alipay/Pyraformer ; FEDformer https://github.com/MAZiqing/FEDformer
- Paper: https://arxiv.org/abs/2301.03982

## 📈 Performance & Results
- Main benchmark (Table 1): top-1 in 36/58, top-2 in 51/58 settings vs LSTMa, LSTnet, MTGNN, Transformer, Informer, Autoformer, Pyraformer, FEDformer. Highlights (MSE): ETTh1 τ=168 Crossformer **0.410** vs FEDformer 0.412, Autoformer 0.493; ETTh1 τ=720 **0.519** vs FEDformer 0.521; ETTm1 τ=96 **0.320** vs FEDformer 0.366; ETTm1 τ=288 **0.404** vs FEDformer 0.398; WTH τ=336 **0.495**; ECL τ=48 **0.156** (FEDformer 0.229, MTGNN 0.173); Traffic τ=24 **0.491** vs MTGNN 0.506, FEDformer 0.562. FEDformer/Autoformer win on small ILI (decomposition priors help with limited data).
- Extra comparison (Appendix Table 4): beats STformer (which flattens 2D→1D and OOMs on ECL/Traffic). DLinear wins on ETTm1 (τ≥288), ECL and Traffic (e.g., Traffic τ=24 DLinear 0.351 vs Crossformer 0.491); Crossformer wins on WTH and long-horizon ETTh1 (τ=168: 0.410 vs 0.416).
- Ablation (Table 2, ETTh1): Transformer→DSW alone improves (τ=24: 0.620→0.373 MSE) proving embedding/cross-dimension value; +TSA improves further (0.305 at τ=24 with HED); HED helps long-term but slightly hurts short-term; full model best everywhere.
- Router ablation (Table 5): TSA(w/o Router) ≈ TSA short-term, router slightly better long-term (τ=720: 0.519 vs 0.540) while enabling linear scaling in D (handles D=300; w/o-router OOMs beyond D≈200; no-TSA OOMs beyond D≈50 on an 11GB GPU).
- Hyperparameters: longer $L_{seg}$ helps long-term forecasting (daily-period data favors $L_{seg}=24$); performance stable for $c \ge 5$. Efficiency: lowest memory and fastest per-batch runtime among the five Transformers for tested input lengths ($T \le 10^4$).

## 💡 Limitations & Identified Research Gaps
- Router builds full all-to-all dimension connections → introduces noise on high-dimensional datasets; sparse graph-transformer structures suggested as future improvement.
- Permutation-invariance critique of DLinear acknowledged: Crossformer is outperformed by DLinear on several datasets (ETTm1 long horizons, ECL, Traffic); enhancing order preservation (relative position encodings) is flagged as promising.
- Straightforward covariate embedding does not improve accuracy — incorporating covariates remains an open problem.
- Time-series benchmark datasets are too small/simple relative to vision/text; larger, more diverse datasets needed for Transformers to reach their potential.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{zhang2023crossformer,
  title     = {Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting},
  author    = {Zhang, Yunhao and Yan, Junchi},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2023}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — MSA backbone used in both TSA stages
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — baseline; dataset provider (Informer2020 repo)
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — baseline; ILI/Traffic data provider
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — concurrent linear challenger that beats Crossformer on some datasets; motivates order-preservation research
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — LogTrans efficient-attention lineage
