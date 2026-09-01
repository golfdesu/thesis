---
type: paper
title: "Personalized federated learning for household electricity load prediction with imbalanced historical data"
authors: [Shibo Zhu, Xiaodan Shi, Huan Zhao, Yuntian Chen, Haoran Zhang, Xuan Song, Tianhao Wu, Jinyue Yan]
year: 2025
journal_conference: "Applied Energy"
doi_url: "https://doi.org/10.1016/j.apenergy.2025.125419"
models_used: ["[[PF-HoLo]]", "[[LSTM]]", "[[Encoder_Decoder]]", "[[FedAvg]]", "[[Federated_Mutual_Learning]]"]
datasets_used: ["[[REFIT]]"]
features_used: ["[[Appliance_Level_Load]]", "[[Historical_Load]]", "[[Last_Observed_Power_Anchor]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Personalized Federated Learning for Household Electricity Load Prediction with Imbalanced Historical Data

## 🎯 Main Objective & Contribution
- Household consumption accounts for 30–40% of global electricity; accurate [[Short_Term_Forecasting]] appliance-level prediction supports Smart Home Energy Management Systems (SHEMS), but faces four challenges:
  1. **Non-IID user behavior** — the IID assumption of classical FL breaks at household level.
  2. **Imbalanced residential data** — households differ in appliances and in data volume (different smart-meter installation dates).
  3. **Randomness/sparsity** of appliance usage — high proportion of zero values for short-duration appliances (kettles, microwaves).
  4. **Need for an effective local–global interaction strategy** in personalized FL.
- Contributions: (a) the [[PF-HoLo]] framework for appliance-level prediction under imbalanced data; (b) an end-to-end federated [[Encoder_Decoder]] model where only the Encoder is shared; (c) a personalized loss using encoder hidden states as soft targets for mutual learning; (d) extensive ablations on real-world household data.

## 🧠 Methodology & Model Architecture
- **[[PF-HoLo]]**: each household holds a *Meme model* (participates in federation via [[FedAvg]]) and a *Personal model* (local-only), trained mutually via knowledge distillation. Only the **Encoder of the Meme model is shared** during aggregation; Decoders stay local to adapt to household-specific distributions.
- **Model structure**: LSTM Encoder → fixed-length hidden/cell vectors; Decoder = LSTM + fully connected layers. Last observed per-appliance power values are concatenated with encoder states as decoder initial input.
  - Encoder update ("Encoder state equation"):
    $$ h^{Enc}_{Tobs}, c^{Enc}_{Tobs} = f_{Enc}(X, h_{Tobs-1}, c_{Tobs-1}) $$
  - Decoder initialization ("Decoder seed equation"):
    $$ \hat{Y}, h^{Dec}_{Tobs}, c^{Dec}_{Tobs} = f_{Dec}\big((p^1_{Tobs}, p^2_{Tobs}, \ldots, p^m_{Tobs}), h^{Enc}_{Tobs}, c^{Enc}_{Tobs}\big) $$
- **Classical FL baseline ([[FedAvg]]) global update** ("FedAvg aggregation"):
  $$ \omega_G = \frac{1}{H} \sum_{h}^{H} \omega_h $$
- **Personalized mutual-learning losses** (soft targets = encoder hidden states):
  - Mutual soft-target loss ("mutual learning loss"):
    $$ L^s_{mu} = Criterion(h^M_{Tpred}, h^P_{Tpred}) $$
  - MSE criterion ("mean squared error"):
    $$ MSE = \frac{1}{n} \sum_{i=1}^{n} (\hat{Y}_i - Y_i)^2 $$
  - MAE criterion ("mean absolute error"):
    $$ MAE = \frac{1}{n} \sum_{i=1}^{n} |\hat{Y}_i - Y_i| $$
  - True-label losses ("target losses"):
    $$ L_{target,m} = MSE(\hat{Y}^{Me}, Y), \qquad L_{target,p} = MSE(\hat{Y}^{Pe}, Y) $$
  - Final joint losses ("combined Meme/Personal losses"):
    $$ L_m = L^s_{mu} + L_{target,m}, \qquad L_p = L^s_{mu} + L_{target,p} $$
  - Ablation variant without encoder–decoder ("alternative soft-target loss"):
    $$ L^{s2}_{mu} = Criterion(h^M_{Tobs+Tpred}, h^P_{Tobs+Tpred}) $$
- Training: E=5 local epochs × R=10 federated rounds; lr=0.003; batch size 4096; hidden dim 128; PyTorch on RTX 3090. Observation window 120 min.

## 📊 Dataset & Input Features
- **Dataset**: [[REFIT]] (Murray et al., *Sci Data* 2017) — electrical power consumption of **20 UK households over two years**, originally sampled at 6–8 s intervals; cleaned (removed distributor>total power records), forward-filled at 1 s, resampled to **1-min resolution**, min–max normalized. Subset used: April 1, 2014 – April 30, 2015 (13 months).
- **Features**: per-appliance power time series for 8 frequent appliance types (fridge, washing machine, dishwasher, microwave, kettle, television site, computer site, dryer); missing appliances set to zero. Predictions aggregated back to household level.
- **Imbalance simulation**: households split into *Enough* (train ratio 0.6), *Cascade* (11 households, train ratios 0.05–0.55), *Very Little* (train ratios 0.00625/0.0125/0.025 ≈ as little as ~2.5 days of data).
- **Data availability**: "The authors do not have permission to share data." REFIT is publicly available (refit smart-meter dataset, Murray et al. 2017).

## 📈 Performance & Results
- vs [[FedAvg]] benchmark (avg across households):
  - Cascade households: PF-HoLo **11 298.66 W² / 18.00 W** vs FedAvg 13 198.92 / 20.38 → **14.40% MSE / 11.69% MAE improvement**; FedSGD −1.86%/−0.22%; Central −1.32%/+3.54% (worse).
  - Very-Little households: PF-HoLo **8028.87 / 12.28** vs FedAvg 9267.36 / 14.19 → **13.36% / 13.50% improvement**.
  - Enough households: PF-HoLo **6601.60 / 13.44** vs FedAvg 7349.58 / 14.83 → **10.18% / 9.37% improvement**.
- Overall: **13.41% MSE and 11.33% MAE improvement over FedAvg**; largest gains for data-scarce households.
- Ablations: soft-target mutual learning > hard target; encoder–decoder structure alone (EnDe FedAvg) already gives most of the gain (+12.65%/+10.64% Cascade); PF-HoLo best combined MSE+MAE. Highest $R^2$ for dishwashers/TVs; lowest for kettles/microwaves (sparse short use) and fridges (low variance).
- Qualitative: PF-HoLo correctly captures dishwasher startup peaks (~2200 W) and fridge periodic cycles where FedAvg mispredicts.

## 💡 Limitations & Identified Research Gaps
- Requires appliance-level sub-metering; future work integrates [[NILM]] disaggregation to enable sensor-free deployment.
- 1-min resampling too coarse for short-duration appliances (microwave/kettle) — limited accuracy gains there.
- Planned systematic comparison of household-level vs appliance-level prediction trade-offs.
- Framework validated only on household loads (not EV charging stations), but the imbalanced non-IID personalization recipe transfers directly to heterogeneous-charger federated EV forecasting.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zhu2025personalized,
  title   = {Personalized federated learning for household electricity load prediction with imbalanced historical data},
  author  = {Zhu, Shibo and Shi, Xiaodan and Zhao, Huan and Chen, Yuntian and Zhang, Haoran and Song, Xuan and Wu, Tianhao and Yan, Jinyue},
  journal = {Applied Energy},
  volume  = {384},
  pages   = {125419},
  year    = {2025},
  doi     = {10.1016/j.apenergy.2025.125419}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — encoder–decoder paradigm lineage ([43] Cho et al. RNN encoder–decoder)
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM backbone
- [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]] — personalization context
- Related vault papers: [[2023_Cheng_VMD_Prophet_LSTM]], [[2020_Salinas_DeepAR_Probabilistic_Forecasting]], [[2024_Ke_Divide_Conquer_Transformer_EV]] (smart-meter load settings)

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_Zhu_Personalized_Federated_Learning_refs]]
