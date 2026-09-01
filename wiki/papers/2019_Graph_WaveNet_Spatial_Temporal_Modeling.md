---
type: paper
title: "Graph WaveNet for Deep Spatial-Temporal Graph Modeling"
authors: [Zonghan Wu, Shirui Pan, Guodong Long, Jing Jiang, Chengqi Zhang]
year: 2019
journal_conference: "IJCAI 2019 (28th International Joint Conference on Artificial Intelligence), pp. 1907-1913"
doi_url: "https://doi.org/10.48550/arXiv.1906.00121"
models_used: ["[[Graph_WaveNet]]"]
datasets_used: ["[[Traffic]]", "[[Traffic]]"]
features_used: ["[[Traffic_Speed]]", "[[Sensor_Time_Series]]", "[[Adjacency_Matrix]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Graph WaveNet for Deep Spatial-Temporal Graph Modeling

## 🎯 Main Objective & Contribution
Propose **Graph WaveNet**, a CNN-based deep spatial-temporal graph architecture that combines (i) a novel **self-adaptive adjacency matrix** learned end-to-end through node embeddings (capturing *hidden* spatial dependencies without prior knowledge, fixing cases where explicit graphs miss true dependencies) and (ii) **stacked dilated causal convolutions** whose receptive field grows exponentially with depth, enabling efficient long-sequence modeling without RNN-style iterative propagation or gradient explosion. Contributions: self-adaptive adjacency preserving hidden spatial dependencies; an effective framework assembling graph convolution with dilated causal convolution so each GCN layer operates at different temporal granularities; state-of-the-art results on two public traffic datasets with low computation cost. **Relevance to EV charging load forecasting:** this is the foundational spatial-temporal backbone (adaptive adjacency + gated dilated TCN) reused by many EV-charging-station GNN load forecasters, especially where inter-station dependency structure must be learned rather than given.

## 🧠 Methodology & Model Architecture
**Problem definition (Eq. 1)** — given graph $\mathcal{G}=(V,E)$, adjacency $A \in \mathbb{R}^{N\times N}$, dynamic feature matrix $X^{(t)}\in\mathbb{R}^{N\times D}$, learn $f$ mapping $S$ historical steps to $T$ future steps:
$$[\boldsymbol{X}^{(t-S):t}, \mathcal{G}] \xrightarrow{f} \boldsymbol{X}^{(t+1):(t+T)}$$

**Graph convolution layer (GCN).**
*Baseline GCN (Eq. 2)* (Kipf & Welling first-order Chebyshev approximation, $\tilde{A}$ = normalized adjacency with self-loops):
$$Z = \tilde{A}XW$$
*Generalized diffusion convolution (Eq. 3)* ($P_k$ = power series of transition matrix):
$$Z = \sum_{k=0}^{K} P^k X W_k$$
*Bidirectional diffusion convolution (Eq. 4)* — forward transition $P_f = A/\text{rowsum}(A)$, backward $P_b = A^T/\text{rowsum}(A^T)$:
$$Z = \sum_{k=0}^{K} P_f^k X W_{k1} + P_b^k X W_{k2}$$
*Self-adaptive adjacency matrix (Eq. 5)* — from learnable node embeddings $E_1, E_2 \in \mathbb{R}^{N\times c}$ (source/target node embeddings); ReLU eliminates weak connections, SoftMax normalizes so $\tilde{A}_{adp}$ acts as transition matrix of a hidden diffusion process:
$$\tilde{A}_{adp} = \text{SoftMax}(\text{ReLU}(E_1 E_2^T))$$
*Combined graph convolution (Eq. 6)* — predefined + hidden dependencies:
$$Z = \sum_{k=0}^{K} P_f^k X W_{k1} + P_b^k X W_{k2} + \tilde{A}_{apt}^k X W_{k3}$$
*Adaptive-only mode when graph structure unavailable (Eq. 7)*:
$$Z = \sum_{k=0}^{K} \tilde{A}_{apt}^k X W_k$$

**Temporal convolution layer (TCN).**
*Dilated causal convolution (Eq. 8)* — dilation factor $d$ controls skip distance; causal padding preserves temporal order; stacking layers with increasing dilation gives exponential receptive-field growth:
$$x \star f(t) = \sum_{s=0}^{K-1} f(s)\, x(t - d \times s)$$
*Gated TCN (Eq. 9)* — output gate with element-wise product $\odot$, activation $g(\cdot)$ (set to tanh) and sigmoid gate $\sigma(\cdot)$:
$$h = g(\Theta_1 \star X + b) \odot \sigma(\Theta_2 \star X + c)$$

**Framework:** stacked spatial-temporal layers, each = Gated TCN (two parallel TCNs, tanh/sigmoid branches, residual connection) followed by GCN; residual + skip connections into an output layer (two Linears + ReLU). Trained with **MAE loss (Eq. 10)**:
$$L(\hat{\boldsymbol{X}}^{(t+1):(t+T)};\Theta) = \frac{1}{TND}\sum_{i=1}^{T}\sum_{j=1}^{N}\sum_{k=1}^{D}\big|\hat{X}^{(t+i)}_{jk} - X^{(t+i)}_{jk}\big|$$
Unlike DCRNN/STGCN, outputs all $T$ horizon steps **in one shot** (non-recursive), eliminating train/test inconsistency; receptive field is designed to equal input sequence length.

## 📊 Dataset & Input Features
| Dataset | Location | #Nodes | #Edges | #Time Steps | Resolution |
|---|---|---|---|---|---|
| METR-LA | Highways of Los Angeles County (4 months) | 207 | 1515 | 34,272 | 5-minute windows |
| PEMS-BAY | San Francisco Bay Area (6 months) | 325 | 2369 | 52,116 | 5-minute windows |

Both released by Li et al. [DCRNN, ICLR 2018]; preprocessing follows DCRNN: sensor readings aggregated to 5-min windows, adjacency built from road-network distance via thresholded Gaussian kernel, z-score normalization, chronological 70/10/20 train/val/test split. Input features: per-sensor traffic speed time series. No dataset download URLs appear in the PDF text.
- Code (official, verified in text): https://github.com/nnzhan/Graph-WaveNet

## 📈 Performance & Results
**Main comparison (Table 2)** — Graph WaveNet best on both datasets (MAE/RMSE/MAPE):

| Model | 15 min | 30 min | 60 min |
|---|---|---|---|
| ARIMA (METR-LA) | 3.99 / 8.21 / 9.60% | 5.15 / 10.45 / 12.70% | 6.90 / 13.23 / 17.40% |
| FC-LSTM (METR-LA) | 3.44 / 6.30 / 9.60% | 3.77 / 7.23 / 10.90% | 4.37 / 8.69 / 13.20% |
| WaveNet (METR-LA) | 2.99 / 5.89 / 8.04% | 3.59 / 7.28 / 10.25% | 4.45 / 8.93 / 13.62% |
| DCRNN (METR-LA) | 2.77 / 5.38 / 7.30% | 3.15 / 6.45 / 8.80% | 3.60 / 7.60 / 10.50% |
| GGRU (METR-LA) | 2.71 / 5.24 / 6.99% | 3.12 / 6.36 / 8.56% | 3.64 / 7.65 / 10.62% |
| STGCN (METR-LA) | 2.88 / 5.74 / 7.62% | 3.47 / 7.24 / 9.57% | 4.59 / 9.40 / 12.70% |
| **Graph WaveNet (METR-LA)** | **2.69 / 5.15 / 6.90%** | **3.07 / 6.22 / 8.37%** | **3.53 / 7.37 / 10.01%** |
| DCRNN (PEMS-BAY) | 1.38 / 2.95 / 2.90% | 1.74 / 3.97 / 3.90% | 2.07 / 4.74 / 4.90% |
| STGCN (PEMS-BAY) | 1.36 / 2.96 / 2.90% | 1.81 / 4.27 / 4.17% | 2.49 / 5.69 / 5.79% |
| **Graph WaveNet (PEMS-BAY)** | **1.30 / 2.74 / 2.73%** | **1.63 / 3.70 / 3.67%** | **1.95 / 4.52 / 4.63%** |

Gains over second-best GGRU grow with horizon (larger at 60 min than 15 min), attributed to separate GCN parameters per temporal stage vs shared recurrent GCN weights.

**Adjacency-matrix ablation (Table 3, means over 12 horizons):** METR-LA Identity 3.58/7.18/10.21%; Forward-only 3.13/6.26/8.65%; **Adaptive-only 3.10/6.21/8.68%** (≈ matches forward-only even without any given graph); Forward-backward 3.08/6.13/8.25%; **Forward-backward-adaptive 3.04/6.09/8.23% (best)**. Same ordering on PEMS-BAY (best 1.58/3.52/3.55%). Learned adaptive matrix heatmap shows hub nodes (e.g., node 9 near intersection of main roads vs node 47 on a single road).

**Computation cost on METR-LA (Table 4):** training 53.68 s/epoch (vs DCRNN 249.31, STGCN 19.10); inference 2.27 s total on validation set — fastest of all (DCRNN 18.73, STGCN 11.37), since 12 predictions are generated in one run.

**Setup:** 8 layers, dilation factors {1,2,1,2,1,2,1,2}; Eq. 4 GCN with $K=2$; node embedding size 10; Adam lr 0.001; dropout p=0.3 on GCN outputs; metrics MAE/RMSE/MAPE.

## 💡 Limitations & Identified Research Gaps
- Future work stated by authors: scalable methods for large-scale datasets, and learning **dynamic** (time-varying) spatial dependencies — the adaptive adjacency is static once trained.
- Evaluation limited to highway traffic speed; no probabilistic/uncertainty quantification (point forecasts only).
- Receptive field must be artificially engineered to equal input length for one-shot multi-step output.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{wu2019graphwavenet,
  title     = {Graph WaveNet for Deep Spatial-Temporal Graph Modeling},
  author    = {Wu, Zonghan and Pan, Shirui and Long, Guodong and Jiang, Jing and Zhang, Chengqi},
  booktitle = {Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI)},
  pages     = {1907--1913},
  year      = {2019},
  note      = {arXiv:1906.00121, doi:10.48550/arXiv.1906.00121}
}
```

## 🔗 Key References & Citation Graph
- Builds directly on: WaveNet (dilated causal convolutions, Oord et al. 2016), DCRNN diffusion convolution (Li et al., ICLR 2018), STGCN (Yu et al., IJCAI 2018), GCN (Kipf & Welling, ICLR 2017), dilated convolutions (Yu & Koltun, ICLR 2016).
- Spatial-temporal backbone adopted by EV-station GNN forecasters in the vault: [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]], [[2024_Physics_Informed_GAT_EV_Load]].
- Its WaveNet-style denoising network family is contrasted by [[2023_DiffSTG_Probabilistic_ST_Graph_Diffusion]] (cites this paper as ref [44] when designing UGnet).
