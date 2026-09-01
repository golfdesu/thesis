---
type: paper
title: "Divide-Conquer Transformer Learning for Predicting Electric Vehicle Charging Events Using Smart Meter Data"
authors: [Fucai Ke, Hao Wang]
year: 2024
journal_conference: "arXiv preprint (arXiv:2403.13246)"
doi_url: "https://arxiv.org/abs/2403.13246"
models_used: ["[[DCT-EV]]", "[[Transformer]]", "[[Random_Forest]]", "[[XGBoost]]", "[[ANN]]", "[[LSTM]]"]
datasets_used: ["[[Pecan_Street]]"]
features_used: ["[[Smart_Meter_Load]]", "[[Electricity_Usage]]", "[[EV_Charging_Label]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[F1_Score]]", "[[AUC]]", "[[Average_Precision]]", "[[Accuracy]]", "[[MSE]]", "[[Precision]]", "[[Recall]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Divide-Conquer Transformer Learning for Predicting Electric Vehicle Charging Events Using Smart Meter Data

## 🎯 Main Objective & Contribution
- **Problem**: Predict **home** EV charging events using only historical [[Smart_Meter_Load]] data — at-home charging is behind-the-meter and invisible to grid operators, so historical charging profiles are unavailable (unlike public-station forecasting).
- Inspired by [[NILM]] but goes beyond detection of past charging: provides *predictive* information about future charging occurrences.
- **Contributions**:
  1. New practical task formulation: home-charging event prediction from residential meter data alone.
  2. **[[DCT-EV]]** (Divide-Conquer Transformer EV): non-intrusive, minute-interval model that divides long meter sequences into overlapping sub-sequences processed in parallel through a self-attention [[Transformer]] backbone ([[2017_Attention_Is_All_You_Need|self-attention Transformer encoder]], cf. [[2017_Attention_Is_All_You_Need]]).
  3. State-of-the-art on 10-min and 60-min ahead event prediction vs Random Forest, XGBoost, DNN, LSTM; insights on input length, prediction-span trade-offs, and probability threshold selection.

## 🧠 Methodology & Model Architecture
Three modules: **Load Embedding → EV Representation Learning → Charging Event Prediction**.

1. **Load Embedding Module** ("divide" step): input sequence $\boldsymbol{x} = x_1,...,x_t,...,x_T \in \mathbb{R}^{1\times T}$ is split into $N = \frac{T-L}{stride}+1$ overlapping sub-sequences ($\bar{\boldsymbol{x}} = \{\boldsymbol{x}_1,...,\boldsymbol{x}_N\} \in \mathbb{R}^{N\times L}$, sub-sequence length $L$, stride). Each sub-sequence is projected to a $D$-dim latent space via a convolutional layer (**Eq. 1 — Convolutional embedding**):
$$\boldsymbol{\chi}^n = \boldsymbol{x}^n \kappa$$
where $\kappa \in \mathbb{R}^{L\times D}$ is the conv kernel. Token count drops from $T$ to $N$, so attention cost scales as $T^2 \gg N^2$.

2. **EV Representation Learning Module**: fixed sinusoidal **positional encoding** (**Eq. 2 — Positional encoding**):
$$\boldsymbol{\chi}_{pos} := \boldsymbol{\chi} + \boldsymbol{b}^{pos}$$
Per-head Q/K/V projections (**Eq. 3**):
$$Q_h = \chi_{pos}W_{h,Q},\quad K_h = \chi_{pos}W_{h,K},\quad V_h = \chi_{pos}W_{h,V}$$
with $W^Q, W^K, W^V \in \mathbb{R}^{D\times D_m}$; scaled dot-product attention (**Eq. 4 — Multi-head attention scores**):
$$\alpha_h = \text{Softmax}\left(\frac{Q_h K'_h}{\sqrt{d_{K'_h}}}\right);\quad \psi_h = \alpha_h \times V_h$$
where $d_{K'_h} = D_m$. Feed-forward network (**Eq. 5 — FFN**):
$$\boldsymbol{Z} := \text{ReLu}(\psi\Phi_1 + b_1)\Phi_2 + b_2$$
with $\Phi_1 \in \mathbb{R}^{D\times D'_m}, \Phi_2 \in \mathbb{R}^{D'_m\times D}$, two-layer MLP with ReLU.

3. **Charging Event Prediction Module**: flatten $\boldsymbol{Z} \in \mathbb{R}^{(N*D)\times 1}$; per future minute $m$ (**Eq. 6 — Prediction probability**):
$$\hat{y}_m = \sigma(W'_m \boldsymbol{Z})$$
where $W'_m \in \mathbb{R}^{(N*D)\times 1}$, $\sigma(\cdot)$ sigmoid.

4. **Training objective** (**Eq. 7 — Binary cross-entropy loss**):
$$\mathcal{L} = -\sum_i \sum_m \left(y_{i,m}\log(\hat{y}_{i,m}) + (1-y_{i,m})\log(1-\hat{y}_{i,m})\right)$$

## 📊 Dataset & Input Features
- **[[Pecan_Street]]** (Pecan Street, Austin, TX, USA), 2018 minute-interval residential smart meter data aligned with EV charging profiles.
  - URL/data availability: https://www.pecanstreet.org/dataport/ (accessed Sep. 2019).
  - Size: **22 households** with EVs, **8,063,175 electricity usage records**, of which **402,296 EV charging records**; label = "charging" when EV load > 3 kW.
- **Input features**: household electricity usage only (EV charging records used solely to construct labels/validation). 80:20 train/test chronological split per home. Class-imbalanced (charging occurs only a few hours/week).

## 📈 Performance & Results
- **1–10 minutes ahead** span: [[DCT-EV]] F1@.5 = **87.35%**, AUC = **97.90%**, AP = **88.55%**, ACC@.5 = **98.80%**, MSE = **0.0102**, beating LSTM (83.91%/97.73%/86.89%/98.74%/0.0103), DNN, XGBoost (83.43% F1), Random Forest (22.14% F1).
- **1–60 minutes ahead**: DCT-EV F1@.5 = **63.78%**, AUC = 90.07%, AP = 61.59%, ACC = 96.81%, MSE = 0.0251 vs LSTM 55.94% F1 / 96.68% ACC / 0.0260 MSE and DNN 49.74% F1. ML baselines dropped out due to poor performance.
- Per-minute degradation (Table II): 1-min ahead AUC 99.63%, F1 90.88% → 10-min ahead AUC 94.78%, F1 81.59%.
- Input history length: F1 grows then plateaus beyond **180 minutes** input → chosen as trade-off.
- Optimal probability threshold for DCT-EV lies between 0.6–0.8 (more robust than DNN/LSTM whose optimum is 0.2–0.4).

## 💡 Limitations & Identified Research Gaps
- Performance degrades substantially with longer predictive spans (1–60 min much weaker than 1–10 min); far-future minute-level event prediction remains hard.
- Supervised labels derived from a fixed >3 kW heuristic; requires EV-charging-aligned ground truth during training even though inference needs only meter data.
- Single-dataset (Austin, TX) evaluation; no cross-region generalization or transfer learning tests.
- Class imbalance inherent to sparse home-charging events not explicitly addressed (no re-weighting/resampling reported).

## 📚 BibTeX & Citation Reference
```bibtex
@article{ke2024dctev,
  title   = {Divide-Conquer Transformer Learning for Predicting Electric Vehicle Charging Events Using Smart Meter Data},
  author  = {Ke, Fucai and Wang, Hao},
  journal = {arXiv preprint arXiv:2403.13246},
  year    = {2024}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — Transformer/self-attention backbone ([26]).
- [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — inspiration for sub-sequence ("patch") partitioning ([25]).
- [[1997_Long_Short_Term_Memory]] — LSTM baseline ([32]).
- Related vault concepts: [[NILM]], [[Smart_Meter_Load]], [[Pecan_Street]], [[DCT-EV]]
