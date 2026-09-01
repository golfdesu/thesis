---
type: paper
title: "Multi-view graph contrastive representative learning for intrusion detection in EV charging station"
authors: [Yi Li, Guo Chen, Zhaoyang Dong]
year: 2025
journal_conference: "Applied Energy"
doi_url: "https://doi.org/10.1016/j.apenergy.2025.125439"
models_used: ["[[MVGCRL]]", "[[Mask_Attention_Graph_Transformer]]", "[[GNN]]", "[[GCN]]", "[[GAT]]", "[[EdgeConv]]", "[[CNN]]", "[[LSTM]]", "[[DGI]]", "[[GRACE]]", "[[MVGRL]]"]
datasets_used: ["[[CICEVSE2024]]"]
features_used: ["[[Hardware_Performance_Counters]]", "[[Kernel_Events]]", "[[Microarchitecture_Events]]"]
forecasting_horizon: "[[Spatial_Temporal_Forecasting]]"
metrics: ["[[Precision]]", "[[Recall]]", "[[F1_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Multi-View Graph Contrastive Representative Learning for Intrusion Detection in EV Charging Station

## 🎯 Main Objective & Contribution
- EV charging infrastructure (EVSE ↔ CSMS via [[OCPP]], EVCC via ISO15118) is exposed to cyberattacks (DoS/DDoS, MitM, cryptojacking, scans, floods). Traditional IDS treat flow records independently (ignoring feature interrelations) and need large labeled datasets.
- Contributions:
  1. **[[MVGCRL]]**: supervised multi-view graph contrastive learning that represents [[Hardware_Performance_Counters]] (HPC) logs as two graph views — a *temporal graph* (log entries = nodes, full-connected weighted) and a *feature graph* (HPC metrics = nodes over the window transpose).
  2. Weighted graphs with edge weights learned during training via edge-weight perturbation + edge-masked attention propagation inside a novel **mask-attention Graph Transformer**, revealing hidden feature relationships and improving interpretability.
  3. A **self-supervised MVGCRL** variant with a novel **node shrink task** (minimizing distance between node embeddings and input features) for pre-training with limited labels, then fine-tuning.

## 🧠 Methodology & Model Architecture
- **Problem formulation** ("patching of HPC logs"): HPC logs split into patches $X_l = (\boldsymbol{x_t}, \ldots, \boldsymbol{x_{t+l-1}}) \in R^{l\times N}$, stride $s=l$, $P=\lfloor\frac{L-l}{s}\rfloor$; task ("intrusion target"):
  $$ f: X_l \rightarrow \{\hat{y}_t,\ldots,\hat{y}_{t+l-1}\} \quad\text{and}\quad f:\{X_l, G\} \rightarrow \{\hat{y}_t,\ldots,\hat{y}_{t+l-1}\} $$
- **Graph construction** ("weighted adjacency matrix"):
  $$ A = \begin{cases} A_{ij}, & e_{ij}\in E \\ 0, & \text{otherwise} \end{cases} $$
  initialized to the identity ($A=I$); weights learned dynamically.
- **GNN message passing** ("general GNN framework"):
  $$ a_u^k = AGGREGATE^k\{h_u^{k-1}: u\in N(u)\}, \qquad h_u^k = COMBINE^k\{h_u^{k-1}, a_u^k\} $$
- **Contrastive loss** ("InfoNCE-style contrastive loss"), temperature $\beta=0.5$, cosine similarity:
  $$ L_{cont}(\boldsymbol{h_i},\tilde{\boldsymbol{h_i}}) = -\frac{1}{P}\sum_{i=1}^{P}\log\frac{\exp(sim(\boldsymbol{h_i},\tilde{\boldsymbol{h_i}})/\beta)}{\sum_{j=1}^{N}\exp(sim(\boldsymbol{h_i},\boldsymbol{h_j})/\beta)}, \quad sim = \frac{\boldsymbol{h_i}\cdot\boldsymbol{h_j}}{\|\boldsymbol{h_i}\|\|\boldsymbol{h_j}\|} $$
- **Hybrid augmentation** — "node feature masking":
  $$ \tilde{x}_i = \begin{cases} x_i, & \text{prob } (1-p) \\ 0, & \text{prob } p \end{cases} $$
  "edge weight perturbation" (Gaussian $\Delta w_{ij}$):
  $$ \tilde{A}_{ij} = \begin{cases} A_{ij}+\Delta w_{ij}, & \text{prob } (1-p) \\ A_{ij}, & \text{prob } p \end{cases} $$
- **Mask-attention Graph Transformer encoder** (after a CNN extracts initial hidden reps $H_l$ from $X_l$): per head $c$, "QKV projections": $Q_i^c = W_q^c\boldsymbol{h_i}+b_q^c$, $K_j^c = W_k^c\boldsymbol{h_j}+b_k^c$, $V_j^c = W_v^c\boldsymbol{h_j}+b_v^c$; "attention coefficient":
  $$ \alpha^c_{i,j} = \frac{\langle Q_i^c, K_j^c\rangle}{\sum_{u\in N(i)}\langle Q_i^c,K_u^c\rangle}, \qquad \langle Q,K\rangle = softmax\!\left(\frac{Q^\top K}{\sqrt{d}}\right) $$
  "edge-mask message aggregation" with mask matrix $M\in R^{N\times N}$ derived from adjacency:
  $$ \boldsymbol{h_i^c} = W_1 h_i + \sum_{j\in N(i)} \alpha^c_{i,j}\odot M\,W_2 V_j^c $$
  "edge mask threshold": $M_{ij}=A_{ij}$ if $A_{ij}\ge\sigma$, else 0; adjacency update ("adjacency refinement"): $A_{ij}=A_{ij}*\alpha$, $\alpha=average(\alpha^c)$; final node embedding ("multi-head concat"): $\boldsymbol{h_i}=[\boldsymbol{h_1^c},\ldots,\boldsymbol{h_i^c}]$.
- **Graph embeddings** ("view projection"): $\mathcal{G}=W\times H_l$, $\tilde{\mathcal{G}}=W\times\tilde{H}_l$ (per view); fused graph embedding: $\mathcal{G}=W_g[\mathcal{G}_{temporal}\|\mathcal{G}_{feature}]$.
- **Multi-view contrastive losses** ("positive/negative view losses"):
  $$ Loss_{pos} = Loss_{cont}(G_t,\tilde{G}_t)+Loss_{cont}(G_f,\tilde{G}_f), \qquad Loss_{neg} = Loss_{cont}(G_t,G_f)+Loss_{cont}(\tilde{G}_t,\tilde{G}_f) $$
  $$ Loss_{view} = Loss_{pos} + \tfrac{1}{2}Loss_{neg} $$
  **Node shrink task** ("node shrink loss", applied on original temporal view only):
  $$ Loss_{shrink} = \frac{1}{c}\sum_{i=1}^{N}\sum_{j=1}^{c}\sqrt{\boldsymbol{h_{c,i}}-\boldsymbol{x_i}} $$
  Total graph contrastive loss: $Loss_{cl} = Loss_{view} + 0.2\cdot Loss_{shrink}$.
- **Decoder/classification**: vanilla Transformer decoder $\mathcal{H}=Transformer(\mathcal{G})$ → MLP $\hat{Y}_{i,l}=MLP(\mathcal{H})$; cross-entropy label loss $Loss_{label}=\sum(-Y_{i,l}\log(softmax(\hat{Y}_{i,l})))$; total ("total MVGCRL loss"): $Loss_{all}=\alpha Loss_{label}+(1-\alpha)Loss_{cl}$.
- SSL version: pre-train with $Loss_{cl}$/$Loss_{shrink}$ only, freeze graph-embedding params, fine-tune classifier.
- Implementation: batch 16, patch size 20, lr $10^{-4}$, dropout 0.5, $\sigma=0.3$, $\alpha=0.8$ optimal, perturbation rate p=0.4, 200 rounds, 60/20/20 split, GridSearch, Python 3.10 on Nvidia A100.

## 📊 Dataset & Input Features
- **Dataset**: [[CICEVSE2024]] [26] (Buedi et al., IFIP DBSec 2024) — real-world testbed with a Level 2 EVSE: EVSE-A talks OCPP to a remote CSMS; EVSE-B is a Raspberry Pi interfacing EVCC (ISO15118) and CSMS (OCPP). PERF2 collects ~900 kernel/HPC events every **5 s**.
- Size: **8465 log series**, each recording **907 low-level microarchitecture events** (instruction execution, memory access, …). Preprocessing: NaN-column removal → standard normalization → Pearson correlation filtering (threshold 0.3) → **47 selected features** (e.g., `ase_spec`, `block_bio_backmerge`, `branch-misses`).
- **18-class labels** (Table 1): Benign (54.36%), Cryptojacking (21.18%), Aggressive-Scan, Vuln-Scan, Syn-Stealth, Port-Scan, TCP/SYN/Udp/Icmp-Flood, Icmp-Fragmentation (old), Os-Scan/Fingerprinting, Service/Serial-Detection, Push-Ack-Flood, Synonymous-Ip-Flood.
- **Data availability**: "Data will be made available on request." Dataset reference: Buedi et al., *Enhancing EV charging station security using a multi-dimensional dataset: CICEVSE2024*, IFIP 2024, pp. 171–190.

## 📈 Performance & Results
- **Supervised (Table 3)**: MVGCRL (SL) weighted precision/recall/F1 = **97.55% / 97.13% / 97.20%**, vs LSTM 96.94/96.39/96.54, CNN 94.86/94.21/94.30, MLP 91.80/91.48/91.54, SVM 91.61/91.18/91.25, LogisticRegression 91.52/90.65/90.97, Random Forest 93.22/92.77/92.88, Decision Tree 90.36/90.30/90.24, KNN 90.19/88.89/89.16 (+8.2%/9.3%/9% vs worst baseline, p<0.05).
- **Self-supervised (Table 4)**: MVGCRL (SSL) **97.71% / 96.79% / 97.11%**, vs GRACE 95.68/82.46/88.17, MVGRL 91.71/89.12/90.22, DGI 90.18/86.06/87.85 (+8.3%/17.4%/10.5% vs worst, p<0.05).
- **Encoder ablation (Table 5)**: mask-attention Graph Transformer best in SSL (97.71/96.79/97.11); vanilla Graph Transformer slightly better in SL (97.76/97.04/97.30); GCN/GAT/EdgeConv clearly worse (e.g., EdgeConv SSL F1 92.84%). vs worst GNN baseline: +4%/5.3%/5.1% (SL), +3.7%/4.5%/4.6% (SSL).
- **Node shrink task (Table 6)**: +1.4%/3.1%/2.4% (SL), +0.3%/0.4%/0.4% (SSL), all p<0.05.
- **Augmentation ablation (Table 7)**: hybrid node+edge perturbation best; removing feature masking costs up to 0.8% recall (SL); removing edge perturbation costs up to 1.7% recall (SL) / 1.5% recall (SSL).
- Hyperparameters: peak at lr=$10^{-4}$, dropout 0.5, $\sigma=0.3$, p=0.4 (p>0.5 degrades: 96.21/95.21/95.5 at p=0.8).

## 💡 Limitations & Identified Research Gaps
- Performance highly sensitive to hyperparameter tuning (lr, augmentation rate); augmentations must be manually designed to align pretext tasks with downstream objectives.
- Future work: adaptive graph-augmentation methods tailored automatically to tasks; theoretical grounding of multi-view contrastive objectives.
- Broader applications proposed: anomaly detection/demand-response support in integrated power-transportation networks, soft-open-point scheduling with energy storage.
- Note for load-forecasting research: the multi-view graph construction + mask attention recipe is transferable to spatio-temporal EV charging demand graphs.

## 📚 BibTeX & Citation Reference
```bibtex
@article{li2025mvgcrl,
  title   = {Multi-view graph contrastive representative learning for intrusion detection in EV charging station},
  author  = {Li, Yi and Chen, Guo and Dong, Zhaoyang},
  journal = {Applied Energy},
  volume  = {385},
  pages   = {125439},
  year    = {2025},
  doi     = {10.1016/j.apenergy.2025.125439}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — Transformer/attention backbone [29]
- Related vault papers: [[2024_Physics_Informed_GAT_EV_Load]] (spatio-temporal GAT for EV charging demand prediction [2]), [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]], [[2023_Crossformer_Cross_Dimension_Dependency]] (cross-feature dependency modeling)

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_Multi_View_Graph_Intrusion_Detection_EV_refs]]
