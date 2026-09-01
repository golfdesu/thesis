---
type: paper
title: "A Physics-Informed and Attention-Based Graph Learning Approach for Regional Electric Vehicle Charging Demand Prediction"
authors: [Haohao Qu, Haoxuan Kuang, Qiuxuan Wang, Jun Li, Linlin You]
year: 2024
journal_conference: "IEEE Transactions on Intelligent Transportation Systems, vol. 25, no. 10, pp. 14284-14297"
doi_url: "https://doi.org/10.1109/TITS.2024.3401850"
models_used: ["[[PAG]]", "[[PIML]]", "[[GAT]]", "[[TPA-LSTM]]", "[[LSTM]]", "FourierGNN", "AST-GAT", "DCRNN", "STGCN", "HSTGCN", "GCN-LSTM", "[[GCN]]", "FCNN", "[[VAR]]", "Lasso", "KNN"]
datasets_used: ["[[Shenzhen_ST_EVCDP]]"]
features_used: ["[[Station_Occupancy]]", "[[Charging_Price]]", "[[Price_Elasticity_of_Demand]]", "[[Spatial_Spillover]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAPE]]", "RAE", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Physics-Informed and Attention-Based Graph Learning Approach for Regional EV Charging Demand Prediction

## 🎯 Main Objective & Contribution
- Solves **price misinterpretation** in data-driven [[EV_Charging_Demand]]: models trained on partially observed data learn "higher price → higher demand" because peak-price hours coincide with peak demand, which is fatal for pricing-policy decision support.
- Proposes **PAG**: (a) a **graph embedding module** ([[GAT]] + temporal CNN), (b) a **multivariate decoder module** ([[TPA-LSTM]]) with revised hop-wise/sequence-wise attention, and (c) a **model pre-training module** based on **Physics-Informed Meta-Learning (PIML)** that generates synthetic tuning samples from economic laws (price elasticity of demand) and pre-trains via [[MAML]].
- Contributions: model-free PIML pre-training step; attention-based spatiotemporal network avoiding conv/recurrent inflexibility; SOTA accuracy on 18,061 Shenzhen charging piles with correct price-elasticity interpretation; demonstration that 1-hop spatial spillover offsets >90% of local demand loss after a 30% price increase.

## 🧠 Methodology & Model Architecture
Problem setup: urban area as graph of $N$ zones (nodes = traffic zones, edges = centroid links); tensor $\mathcal{X}(i,j,t)$ = $j$-th feature of node $i$ at time $t$; sliding window $\{\mathbf{x}_{t-w},\dots,\mathbf{x}_{t-1}\}$; task: predict $\mathbf{y} = X(:,o,t+\Delta) = \mathbf{o}^{t+\Delta}$ for all zones at horizon $\Delta$.

### Graph Embedding Module (CNN + GAT)
2-D CNN extracts temporal features per node; masked multi-head GAT models spatial relations. Attention similarity score (**Eq. 1, GAT similarity**):
$$e_{ij} = a([\mathbf{W}\mathbf{x}_i \parallel \mathbf{x}_j]) = \text{LeakyReLU}(\vec{\mathbf{a}}^T[\mathbf{W}\mathbf{x}_i \parallel \mathbf{W}\mathbf{x}_j])$$
Attention coefficients (**Eq. 2, softmax normalization**):
$$\alpha_{ij} = \text{softmax}_j(e_{ij}) = \frac{\exp(e_{ij})}{\sum_{n\in\mathcal{N}_i}\exp(e_{in})}$$
$K$-head averaged output (**Eq. 3, multi-head GAT aggregation**):
$$\mathbf{x}'_i = \sigma\left(\frac{1}{K}\sum_{k=1}^{K}\sum_{j\in\mathcal{N}_i}\alpha^k_{ij}\mathbf{W}^k\mathbf{x}_j\right)$$
Momentum residual connection against over-smoothing across stacked layers (**Eq. 4, momentum residual**, $\beta$ residual coefficient, output has $MF$ features for $M$ hops):
$$\mathbf{x}''_i = \parallel_{m=1}^{M}\left[(1-\beta)\mathbf{x}^{\prime m}_i + \beta\,\mathbf{x}^{\prime m-1}_i\right], \quad \mathbf{x}^{\prime 0}_i = \mathbf{x}_i$$

### Multivariate Decoder Module (revised TPA-LSTM)
LSTM gates over input $\mathbf{x}_t \in \mathbb{R}^{MF}$ (**Eq. 5, LSTM gate equations**):
$$\begin{aligned}
\mathbf{u}_t &= \sigma(\mathbf{W}_{uu}\mathbf{x}_t + \mathbf{b}_{uu} + \mathbf{W}_{hu}\mathbf{h}_{t-1} + \mathbf{b}_{hu}), \quad
\mathbf{f}_t = \sigma(\mathbf{W}_{uf}\mathbf{x}_t + \mathbf{b}_{uf} + \mathbf{W}_{hf}\mathbf{h}_{t-1} + \mathbf{b}_{hf})\\
\mathbf{g}_t &= \tanh(\mathbf{W}_{ug}\mathbf{x}_t + \mathbf{b}_{ug} + \mathbf{W}_{hg}\mathbf{h}_{t-1} + \mathbf{b}_{hg}), \quad
\mathbf{q}_t = \sigma(\mathbf{W}_{uq}\mathbf{x}_t + \mathbf{b}_{uq} + \mathbf{W}_{hq}\mathbf{h}_{t-1} + \mathbf{b}_{hq})\\
\mathbf{c}_t &= \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{u}_t \odot \mathbf{g}_t\\
\mathbf{h}_t &= \mathbf{q}_t \odot \tanh(\mathbf{c}_t)
\end{aligned}$$
TPA attention revised to attend over both hop-wise ($M$ CNN filters $\mathbf{C}_m \in \mathbb{R}^{F\times w}$, stride $F$, applied to hidden states $\{\mathbf{h}_{t-w},\dots,\mathbf{h}_{t-1}\}$) and sequence-wise features (average pooling $\mathbf{P}_\alpha \in \mathbb{R}^{F\times 1}$ on $\mathbf{h}_t$); sigmoid used instead of softmax so multiple variables are attended (**Eq. 6, TPA attention scores**, giving $M\times M$ scores):
$$\vec{\boldsymbol{\alpha}}_m = \sigma(\mathbf{P}_\alpha^T\mathbf{h}_t \odot \parallel_{m=1}^{M}[\mathbf{C}_m^T\mathbf{H}_m]) = \sigma(\mathbf{h}^P_t \odot \parallel_{m=1}^{M}[h^{C}_{m,m}])$$
Final prediction via two linear layers $\mathbf{W}_p, \mathbf{W}_\alpha \in \mathbb{R}^M$ (**Eq. 7, prediction integration**):
$$\mathbf{y} = \mathbf{W}_p^T(\mathbf{W}_\alpha\mathbf{H}\boldsymbol{\alpha} + \mathbf{h}^P_t)$$

### Physics-Informed Meta-Learning Pre-Training (PIML)
Tuning samples generated from laws: normally distributed price impulses $\Delta p$ → demand responses via Beijing EV-charging price elasticity $(\Delta y/y)/(\Delta p/p) = -1.48$ (**Eq. 8, elasticity-based tuning sample**):
$$\Delta y_i = \mathcal{F}(\Delta p_i) = -1.48\left(\Delta p_i / p_i\right)y_i$$
Spillover to each of $N$ neighbors (**Eq. 9, neighbor spillover sample**):
$$\Delta y_j = -\frac{1}{N}\Delta y_i$$
[[MAML]] objective over $S$ tuning-sample buffers (**Eq. 10, FOMAML objective**):
$$\min L(\phi) = \sum_{s=1}^{S} l^s(\theta^s)$$
Gradient chain rule (**Eq. 11**) and first-order approximation dropping the second-derivative term (**Eqs. 12-13, FOMAML gradient approximation**):
$$\nabla_\phi L(\phi) = \sum_{s=1}^S \frac{\partial l^s}{\partial \theta^s}\frac{\partial \theta^s}{\partial \phi}, \qquad \frac{\partial \theta^s}{\partial \phi} = \frac{1 - \varepsilon\nabla_\phi l(\phi)\,\partial\phi/\partial\phi}{\partial\phi\,\partial\phi} \approx 1 \;\Rightarrow\; \nabla_\phi L(\phi) \approx \sum_{s=1}^{S}\frac{\partial l^s}{\partial\theta^s} = \sum_{s=1}^S \nabla_\theta l^s(\theta^s)$$
Epoch update with learning rate $\lambda$ (**Eq. 14, meta-update**):
$$\phi_{e+1} = \phi_e - \lambda\frac{\nabla_\phi L(\phi)}{S}$$
Buffers split into Support (Day 1-12) and Query (Day 13-24) sets; proportion of tuning samples gradually reduced by mixing in observed samples. Two buffers built from elasticities: $-1.48$ (Beijing EV public charging) and $-0.228$ (global household electricity average 1950-2014).

### Hyperparameters
Window $w = 12$ intervals (60 min retrospective); GAT heads/layers $K=4$, $M=2$; $\beta=0.5$; MSE loss; [[Adam]], batch 512, lr 0.001, weight decay $10^{-5}$; 200 pre-training epochs + 1000 fine-tuning epochs with early stopping (100 epochs patience).

## 📊 Dataset & Input Features
- **[[Shenzhen_ST_EVCDP]]**: real-time pile availability from a public mobile app; **18,061 public charging piles in Shenzhen, China**, period **19 June – 18 July 2022 (30 days)**; aggregated to pile occupancy (demand) and charging price per zone; updated every **5 minutes**; organized over **247 traffic zones** (6th Residential Travel Survey of Shenzhen) → graph with **247 nodes, 1006 edges**; **8640 timestamps** total, train/val/test = 6:2:2 chronological (Days 1-18 / 19-24 / 25-30). 57 zones use time-of-day pricing; the rest fixed pricing. No smoothing/denoising applied.
- Features: pile occupancy demand (target), charging price (time-based or fixed), price-impulse-derived physics knowledge.
- **Code & data (GitHub)**: https://github.com/IntelligentSystemsLab/ST-EVCDP (stated: "the datasets and code used in this paper are shared in Github").
- Hardware: NVIDIA Quadro RTX 4000 GPU, Intel i9-10900K, 64 GB RAM.

## 📈 Performance & Results
Averages over 247 zones across 15/30/45/60-min horizons:

| Model | RMSE | MAPE | RAE | MAE |
| :--- | :---: | :---: | :---: | :---: |
| **PAG** | **0.0548** | **16.87%** | **19.63%** | **0.0333** |
| FourierGNN | 0.0565 | 18.82% | 20.50% | 0.0350 |
| AST-GAT | 0.0573 | 18.33% | 20.28% | 0.0349 |
| DCRNN | 0.0593 | 18.00% | 21.13% | 0.0375 |
| GCN-LSTM | 0.0581 | 19.32% | 21.80% | ~worse |
| LSTM | 0.0670 | 17.25% | 21.16% | 0.0406 |
| VAR | 0.0944 | 62.64% | 56.19% | 0.0999 |

(Note: text reports MAE 0.0393 vs table value 0.0333; both appear in paper.)
- vs VAR: **61.3% average improvement**; vs LSTM: 18.21%/13.17%/11.37%/17.98% improvements in RMSE/MAPE/RAE/MAE; vs SOTA spatiotemporal baselines (DCRNN, AST-GAT, FourierGNN): 5.29% RMSE, 8.97% MAPE, 5.13% RAE, 7.51% MAE; overall ≈**6.73% average improvement** over SOTA.
- Robustness: randomly dropping 20% (49) of zones (10 runs) still beats baselines by ≈17.09% on average.
- **Ablation**: removing TPA degrades RMSE by 50.84%, removing GAT by 40.27%, removing PIML costs ≈4.18% — all modules necessary.
- **Interpretation tests** (57 dynamic-pricing zones, 30-min model): GCN-LSTM/AST-GAT respond *positively* to price impulses (misinterpretation); un-pre-trained PAG− reacts erratically up to ±1000%; PIML-pre-trained models give stable inelastic responses (PAG responses within [0, 0.6] absolute). Applying PIML to baselines (FourierGNN, AST-GAT, GCN-LSTM, HSTGCN) also fixes their price understanding.
- **Spillover**: 30% CBD price increase raises 1-hop neighbor demand offsetting >90% of local loss; 2-hop responses marginal.

## 💡 Limitations & Identified Research Gaps
- Focus limited to the demand–price relationship; many other misinterpretations exist in spatiotemporal deep models and remain unaddressed.
- Pre-training must be carefully monitored ("model curing" / overfitting to tuning samples); authors suggest an automated critique module trained by Reinforcement Learning as future work.
- Spillover effects are detected but not quantified; quantification would help regulators evaluate policy impacts.

## 📚 BibTeX & Citation Reference
```bibtex
@article{qu2024pag,
  author  = {Qu, Haohao and Kuang, Haoxuan and Wang, Qiuxuan and Li, Jun and You, Linlin},
  title   = {A Physics-Informed and Attention-Based Graph Learning Approach for Regional Electric Vehicle Charging Demand Prediction},
  journal = {IEEE Transactions on Intelligent Transportation Systems},
  year    = {2024},
  volume  = {25},
  number  = {10},
  pages   = {14284--14297},
  doi     = {10.1109/TITS.2024.3401850}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — attention mechanism foundation [9]
- [[2017_MAML_Model_Agnostic_Meta_Learning]] — MAML / FOMAML basis for PIML [13]
- [[1997_Long_Short_Term_Memory]] — LSTM decoder backbone [34]
- [[2014_Kingma_Adam_Optimization]] — optimizer [40]
- Temporal Pattern Attention (TPA), Shih et al. 2019 — decoder attention source [10]
- Velickovic et al., Graph Attention Networks (ICLR 2018) — GAT module [11]
- Raissi et al., Physics-Informed Neural Networks (JCP 2019) — PINN motivation [12]
- Bao et al., IEEE Trans. Smart Grid 2021 — Beijing EV price elasticity −1.48 [35]
- Zhu et al., J. Cleaner Prod. 2018 — household electricity elasticity −0.228 [39]
- Yi et al., NeurIPS 2023 — FourierGNN baseline [27]
- Li & Lasenby, IEEE TITS 2022 — AST-GAT baseline [25]
- Li et al. 2017, DCRNN (arXiv:1707.01926) — baseline [47]
- Yu et al., IJCAI 2018 — STGCN baseline [46]
- Wang et al., Transp. Res. C 2023 — HSTGCN baseline [24]
- Kipf & Welling, ICLR 2016 — [[GCN]] [45]
- He et al., CVPR 2016 — residual learning (momentum residual basis) [33]

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2024_Physics_Informed_GAT_EV_Load_refs]]
