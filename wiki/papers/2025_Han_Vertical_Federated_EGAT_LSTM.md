---
type: paper
title: "A Vertical Federated Learning Method for Electric Vehicle Charging Station Load Prediction in Coupled Transportation and Power Distribution Systems"
authors: [Qi Han, Xueping Li]
year: 2025
journal_conference: "Processes"
doi_url: "https://doi.org/10.3390/pr13020468"
models_used: ["[[V2AFedEGAT-LSTM]]", "[[EGAT]]", "[[LSTM]]", "[[GGNN]]", "[[GAT]]", "[[Time_Aware_Attention]]"]
datasets_used: ["[[CTPS_IEEE33_7Node_TN]]", "[[CTPS_IEEE69_12Node_TN]]", "[[NYISO]]"]
features_used: ["[[Node_Voltage]]", "[[Active_Power]]", "[[Reactive_Power]]", "[[Line_Active_Power]]", "[[Line_Reactive_Power]]", "[[Traffic]]", "[[Congestion_Rate]]", "[[Electricity_Tariff]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[R_squared]]", "[[MAE]]", "[[MAPE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Vertical Federated Learning Method for EV Charging Station Load Prediction in Coupled Transportation and Power Distribution Systems

## 🎯 Main Objective & Contribution
- Predict [[EV_Charging_Station_Load]] (EVCSL) using **both** Distribution Network (DN) and Transportation Network (TN) characteristics under a data-privacy barrier between the two operators in a coupled transportation–power distribution system (CTPS). DN-only prediction loses TN information (congestion, charging price) that strongly drives charging choice.
- Contributions:
  1. **[[V2AFedEGAT-LSTM]]**: vertical federated ([[VFL]]) prediction combining DN + TN features via an EGAT–LSTM spatio-temporal model inside a secure federated linear regression framework (ID = aligned time points).
  2. A **spatio-temporal hybrid attention** method — [[EGAT]] at local feature-extraction level (spatial skew) and a time-aware attention module at the cloud aggregation level (temporal skew) — to alleviate DN/TN characteristic distribution skew.
  3. Adjusted federated training strategy (info transmission, encryption/decryption) and model update strategy (freeze last FC layer; update via intermediate result u) balancing privacy vs training efficiency (+11% training speed).

## 🧠 Methodology & Model Architecture
- **Local model**: EGAT characteristic-extraction module (edge-aggregation graph attention; learns node AND edge features of DN/TN topologies; 4-head attention, output node-feature dim 6) → LSTM load-prediction module (Seq_len 5, 2 layers, 16 hidden units, dropout 0.05). Time-aware attention input dim 32; batch 16; lr 0.005; PyCharm/Xeon Platinum 8255C.
- **Federated framework**: partial homomorphic encryption (PHE); three phases — encrypted entity alignment (time-point IDs), encrypted training, encrypted prediction. Cloud hosts the time-aware attention module.
- Key equations ("last-layer gradient"):
  $$ \frac{\partial Loss_{global}}{\partial M_{W_{L+1}}} = \frac{\partial Loss_{global}}{\partial y_{L+1}} \cdot A'_{L+1}(M_{x_{L+1}}) \cdot M_{y_L} $$
  with MSE loss ("global loss"):
  $$ Loss_{global} = \frac{1}{2}(y_{L+1} - y_{Label})^2 $$
  Since $\frac{\partial Loss_{global}}{\partial y_{L+1}} = y_{L+1} - y_{Label}$ contains DN label information, the last FC layer is **frozen**. Layer-$L$ gradient ("layer-L parameter gradient"):
  $$ \frac{\partial Loss_{global}}{\partial M_{W_L}} = \frac{\partial Loss_{global}}{\partial M^L_{x_{DN}}} \cdot M^{DN}_{y_{L-1}} $$
  Layer-$L$ error propagation matrix ("error propagation recursion"):
  $$ \frac{\partial Loss_{global}}{\partial M_{x_L}} = \frac{\partial Loss_{global}}{\partial M_{x_{L+1}}} \cdot (M_{W_{L+1}})^T \cdot A'_L(M_{x_L}) $$
  The non-square weight matrices make inversion impossible, so the encrypted intermediate result ("secure intermediate result") is used:
  $$ u = \frac{\partial Loss_{global}}{\partial M_{x_{L+1}}} \cdot (M_{W_{L+1}})^T $$
  Layer-($L{-}1$) gradient ("layer L−1 gradient"): $\frac{\partial Loss_{global}}{\partial M_{W_{L-1}}} = \frac{\partial Loss_{global}}{\partial M^ {DN}_{x_{L-1}}} \cdot M^{DN}_{y_{L-2}}$ with error propagation via $(M_{W_L})^T A'_{L-1}(M_{x_{L-1}})$. Backprop proceeds to layer 1 without ever exposing loss or labels to the cloud.

## 📊 Dataset & Input Features
- **Simulated CTPS datasets** generated via a two-layer optimal dispatching model ([32] Geng et al., Distflow DN + mixed-integer TN, IPOPT solver):
  - Case 1: IEEE 33-bus DN + 7-node TN; Case 2: IEEE 69-bus DN + 12-node TN. Charging station 1's load = target.
  - **8760 hourly points/year**, 80/20 train/test split; ±15% fluctuation added to NYISO typical daily load curves and to 24 h OD travel demand benchmarks.
- **Features** (Table 1): DN nodes — voltage, active power, reactive power; DN edges — line active/reactive power; TN nodes — traffic flow; TN edges — congestion rate (volume-to-capacity ratio), electricity price.
- Generator limits 8 MW active / −5–8 MW reactive; cost coefficients $a_g$=0.3 USD/MW²h, $b_g$=150 USD/MWh, main-grid purchase φ=140 USD/MWh; queuing coefficient J=5, time value W=10 USD/h.
- **Data availability**: "Due to the current research project, there may be privacy issues with publicly available data" — no public code/data link.

## 📈 Performance & Results
- **IEEE 33-bus / 7-node** (Table 2): V2AFedEGAT-LSTM **R²=0.973, MAE=0.0382, MAPE=0.0421, MSE=0.0023** vs EGAT–LSTM (0.936/0.0523/0.0542/0.0050), VFedGGNN–LSTM (0.919/…/0.0058), GGNN–LSTM (0.911/0.0593/0.0625/0.0063).
- **IEEE 69-bus / 12-node** (Table 3): V2AFedEGAT-LSTM **R²=0.976, MAE=0.0385, MAPE=0.0425, MSE=0.0023** vs EGAT–LSTM (0.938/…/0.0049); baselines degrade more at scale while the proposed method stays stable.
- Convergence: R² converges by ~epoch 70 vs ~100 (EGAT–LSTM) and ~150 (GGNN variants).
- Overall ≈ **4% accuracy improvement** over alternatives; online prediction sub-second (0.313 s small / 0.330 s large scale); proposed update strategy cuts offline encrypted training ~11% (e.g., 523 s vs 590 s per epoch, small scale).

## 💡 Limitations & Identified Research Gaps
- Collaborative cloud assumed semi-honest ("not purely malicious"); malicious-cloud inference not covered — future work on data decomposition and multi-cloud collaborative training.
- Encrypted offline training still ~10× slower than local training (homomorphic overhead); online stage avoids encryption.
- Only simulated dispatch-generated data (no real charging-session records); single-station target per case.

## 📚 BibTeX & Citation Reference
```bibtex
@article{han2025vertical,
  title   = {A Vertical Federated Learning Method for Electric Vehicle Charging Station Load Prediction in Coupled Transportation and Power Distribution Systems},
  author  = {Han, Qi and Li, Xueping},
  journal = {Processes},
  volume  = {13},
  number  = {2},
  pages   = {468},
  year    = {2025},
  doi     = {10.3390/pr13020468}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — attention mechanism foundation [16]
- Related vault papers: [[2025_Hussain_CAT_Former_Short_Term_EV]], [[2023_Koohfar_Transformer_EV_Demand]] (DL comparison for EV demand [17]), [[2025_Zhu_Personalized_Federated_Learning]], [[2023_Cheng_VMD_Prophet_LSTM]], [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]], [[2019_Zhu_EV_Load_Forecasting]]

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_Han_Vertical_Federated_EGAT_LSTM_refs]]
