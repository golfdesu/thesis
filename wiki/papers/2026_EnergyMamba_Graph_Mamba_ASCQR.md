---
type: paper
title: "EnergyMamba: An Uncertainty-Aware Graph-Enhanced Selective State Space Model for Energy Consumption Prediction"
authors: [Dahai Yu, Rongchao Xu, Lin Jiang, Guang Wang]
year: 2026
journal_conference: "ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26)"
doi_url: "https://doi.org/10.1145/3770855.3818841"
models_used: ["[[EnergyMamba]]", "[[AS_CQR]]", "[[Mamba_SSM]]", "[[GCN]]", "[[PatchTST]]", "[[Transformer]]", "[[LSTM]]"]
datasets_used: ["[[Florida_CBG_Smart_Meter]]", "[[NYISO]]", "[[CAISO]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MPIW]]", "[[Interval_Score]]", "[[PICP]]"]
tags: [paper, ev-load-forecasting, mamba, ssm, conformal-prediction, probabilistic-forecasting]
---

# Summary: EnergyMamba: An Uncertainty-Aware Graph-Enhanced Selective State Space Model for Energy Consumption Prediction

> [!cite] Yu, Xu, Jiang & Wang (FSU), KDD '26, doi:10.1145/3770855.3818841 — arXiv 2606.00506

## 🎯 Main Objective & Contribution
- Reformulates energy-consumption prediction as an **uncertainty-aware spatiotemporal** task (not a purely temporal one): spatial dependencies among Census Block Groups (CBGs)/grid zones are explicitly modeled via grid-topology graphs.
- Proposes **GE-Mamba**: GCN-extracted spatial context injected into the selective-scan dynamics of a **bidirectional Mamba** ([[Mamba_SSM]]) organized in a U-Net encoder–decoder for multi-scale temporal modeling.
- Proposes **AS-CQR** ([[AS_CQR]]): Adaptive Sequential Conformalized Quantile Regression with locally adaptive nonconformity normalization + online feedback calibration of the target quantile level for non-stationary/extreme-event conditions.
- Empirically beats 15 SOTA baselines on four real-world datasets (~5% accuracy, ~6% UQ improvement over the best baseline).

## 🧠 Methodology & Model Architecture
- Model Type: **GE-Mamba** = per-time-step GCN (learnable surrogate for power-flow/Kirchhoff propagation) whose output conditions the input-dependent B, C, Δ of a selective SSM; blocks stacked in a U-Net (S=2 stages, K=2 blocks/stage, D=64, state dim D_s=16, expansion 2); skip connections preserve spikes; three linear heads output median/lower/upper quantiles. **AS-CQR** wraps the quantile head: (i) signed nonconformity scores normalized by predicted interval width (scale-invariant across high/low-load regions — motivated by measured r=0.94 load-vs-residual-std heteroscedasticity), and (ii) ACI-style online update of the effective miscoverage rate from recent coverage.
- Key Equations (PDF→txt extraction garbled all math; each equation below is faithfully reconstructed from the extracted text):
  - Eq. (1) — Gaussian-kernel adjacency with sparsity thresholding (reconstructed from text):
    $$A_{ij}=\begin{cases}\exp\!\left(-d_{ij}^2/\sigma^2\right), & i\neq j \ \text{and}\ \exp(-d_{ij}^2/\sigma^2)\ge\epsilon\\ 0, & \text{otherwise}\end{cases}$$
  - Eq. (4) — target coverage guarantee (reconstructed from text):
    $$\mathbb{P}\bigl(Y\in\hat{C}(X)\bigr)\ge 1-\alpha$$
  - Eq. (5) — input embedding (reconstructed from text):
    $$h^{(0)}_{n,t}=W_{\text{emb}}x_{n,t}+e_{\text{pos},t}$$
  - Eq. (6) — spatial context extraction (reconstructed from text):
    $$Z_t=\mathrm{GCN}(H_t,A)=\mathrm{GELU}\!\left(\tilde{D}^{-\frac12}\tilde{A}\tilde{D}^{-\frac12}H_tW_{\text{gcn}}\right),\quad \tilde{A}=A+I_N$$
  - Eq. (7) — continuous SSM dynamics (reconstructed from text):
    $$s'(t)=A_{\text{ssm}}s(t)+Bx(t),\qquad y(t)=Cs(t)$$
  - Eq. (8) — ZOH discretization (reconstructed from text):
    $$\bar{A}=\exp(\Delta A_{\text{ssm}}),\qquad \bar{B}=(\Delta A_{\text{ssm}})^{-1}\bigl(\exp(\Delta A_{\text{ssm}})-I\bigr)\cdot\Delta B$$
  - Eq. (9) — discrete recurrence (reconstructed from text):
    $$s_t=\bar{A}s_{t-1}+\bar{B}h_t,\qquad \tilde{h}_t=Cs_t$$
  - Eqs. (10)–(12) — spatial-conditioned selectivity (reconstructed from text):
    $$B_t=W_B[h_t\,\|\,z_t]+b_B,\quad C_t=W_C[h_t\,\|\,z_t]+b_C,\quad \Delta_t=\mathrm{Softplus}\!\left(W_\Delta[h_t\,\|\,z_t]+b_\Delta\right)$$
  - Eq. (13) — Bidirectional Processing (reconstructed from text):
    $$\mathrm{BIP}(H,Z)=\mathrm{Mamba}_{\rightarrow}(H,Z)+\mathrm{Mamba}_{\leftarrow}(\mathrm{Flip}(H),\mathrm{Flip}(Z))$$
  - Eqs. (14)–(15) — block integration (reconstructed from text):
    $$Z^{(l)}=\mathrm{GCN}(\mathrm{RMSNorm}(H^{(l-1)}),A),\qquad H^{(l)}=H^{(l-1)}+\mathrm{Dropout}\bigl(\mathrm{BIP}(\mathrm{RMSNorm}(H^{(l-1)}),Z^{(l)})\bigr)$$
  - Eqs. (16)–(18) — three linear output heads $\hat{Y}= \mathrm{RMSNorm}(H_{\text{out}})W_{\text{mi}}+b_{\text{mi}}$, and analogously $\hat{q}_{\text{lo}},\hat{q}_{\text{up}}$ with $W_{\text{lo}}/W_{\text{up}}$ (reconstructed from text).
  - Eq. (19) — pinball loss (reconstructed from text):
    $$L_\tau(y,\hat{q}_\tau)=\begin{cases}\tau\cdot(y-\hat{q}_\tau), & y\ge\hat{q}_\tau\\ (1-\tau)\cdot(\hat{q}_\tau-y), & y<\hat{q}_\tau\end{cases}$$
  - Eq. (20) — total loss = mean over nodes/horizon of summed pinball losses at $\tau\in\{\alpha/2,\,0.5,\,1-\alpha/2\}$ (reconstructed from text).
  - Eq. (21) — AS-CQR locally adaptive nonconformity score (reconstructed from text):
    $$\epsilon_t=\frac{\max\bigl(\hat{q}_{\text{lo}}(X_t)-Y_t,\; Y_t-\hat{q}_{\text{up}}(X_t)\bigr)}{\hat{q}_{\text{up}}(X_t)-\hat{q}_{\text{lo}}(X_t)+\delta}$$
    (signed: ε_t<0 inside interval, >0 miscoverage; δ≈1e−6)
  - Eq. (22) — correction factor over sliding window of m=100 scores (reconstructed from text):
    $$Q_t=\mathrm{Quantile}_{1-\tilde{\alpha}_t}(E_t)$$
  - Eq. (23) — calibrated interval, multiplicatively scaled by raw width $w_t=\hat{q}_{\text{up}}-\hat{q}_{\text{lo}}$ (reconstructed from text):
    $$\hat{C}(X_t)=\bigl[\hat{q}_{\text{lo}}(X_t)-Q_t w_t,\;\hat{q}_{\text{up}}(X_t)+Q_t w_t\bigr]$$
  - Eq. (24) — online feedback update of effective miscoverage rate ($\tilde{\alpha}_0=\alpha$, γ=0.005) (reconstructed from text):
    $$\tilde{\alpha}_{t+1}=\tilde{\alpha}_t+\gamma\bigl(\alpha-\mathbb{I}\{Y_t\notin\hat{C}(X_t)\}\bigr)$$
  - Eq. (25) — long-run coverage guarantee inherited from adaptive conformal inference (reconstructed from text):
    $$\lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T}\mathbb{I}\{Y_t\in\hat{C}(X_t)\}=1-\alpha$$
  - Eq. (26) — preprocessing log-normalization $X'=\ln(X+1)$ (reconstructed from text).
- Loss Function: composite pinball (quantile regression) loss, Eq. (20); trained end-to-end with τ ∈ {0.05, 0.5, 0.95}; Adam, lr 1e−3 decayed every 15 epochs, batch 128, early stopping patience 50.

## 📊 Dataset & Input Features
- Datasets (all general electricity consumption — NOT EV charging):
  - **Florida 1**: Leon County, FL municipal utility, 60k+ smart meters aggregated to **201 CBGs**, year 2018 (incl. Hurricane Michael), 30-min resolution, 17,520 steps, kWh.
  - **Florida 2**: same source/aggregation, year 2019 (record heat waves), 30-min, 17,520 steps, kWh.
  - **NYISO**: New York ISO zonal SCADA load, 2024, **11 zones**, 1-hour, 8,760 steps, MWh.
  - **CAISO**: California ISO TAC-area load, 2024, **9 regions/zones**, 1-hour, 8,760 steps, MWh.
- Data Availability & Links: official code repo https://github.com/UFOdestiny/EnergyMamba ; NYISO data https://www.nyiso.com/load-data ; CAISO data https://www.caiso.com/TodaysOutlook/Pages/default.aspx ; Florida data is utility-partner data under NDA (not public).
- Features used: univariate historical consumption per node ([[Historical_Load]]) plus learnable temporal position embedding; graph structure built from geographic centroid distances (Eq. 1). No weather/tariff/calendar exogenous covariates.

## 📈 Performance & Results
- Overall (Table 1): best on nearly all metrics on all four datasets; ≈5% lower MAE and ≈6% better IS vs the best baseline averaged over datasets; achieves ≥90% target coverage (COV ✓) everywhere.
- Florida 1: MAE 36.57 / RMSE 61.06 / MPIW 122.51 / IS 231.86 (best baseline ST-LLM: 38.49 / 64.27 / 134.28 / 246.66).
- Florida 2: 32.42 / 52.66 / 107.83 / 198.23 (ST-LLM: 34.12 / 55.42 / 114.71 / 210.64).
- New York: 43.13 / 64.79 / 201.87 / 295.42 (best baseline MAE UrbanGPT 46.42; G-Mamba 45.40).
- California: 199.18 / 401.88 / 692.05 / 1279.17 (UrbanGPT 210.55 MAE; U-Mamba 428.54 RMSE, 735.47 MPIW).
- Ablation (Florida 1): w/o GCN 47.82 MAE; w/o BIP 42.91; w/o U-Net 39.24; **w/o AS-CQR 44.12 MAE and misses target coverage** (standard static CQR insufficient); decoupled GCN+Linear 58.79. Full model 36.57.
- Efficiency (Table 3): train 7,945 s, inference 2.78 s, 4.03 GB GPU memory, 312.8K params — far lighter than LLM baselines (ST-LLM 67M+, UrbanGPT 72M params).
- Calibration plots: closest to diagonal in empirical-vs-target coverage; informative selective-regression risk–coverage curve. Per-figure numeric values beyond tables: not extractable.

## 💡 Limitations & Identified Research Gaps
- **Domain granularity**: regional/building-aggregate energy consumption (CBGs, ISO zones) — NOT EV-charging-station-level forecasting; no plug-in/session dynamics, no SOC or user behavior. Direct transfer to EV station loads is untested.
- Authors' own limitation (Sec. 8): graph edges are geographic-proximity proxies; physical grid topology is not modeled (future work: true topology + adaptive graph learning).
- No monotonicity/exogeneity guarantees à la [[PICNN]]: intervals come from quantile heads + post-hoc conformal wrapper, so there is no structural constraint linking covariates to interval width; also no cross-attention exogenous fusion at all (univariate inputs).
- Static vs adaptive calibration: standard CQR (exchangeability-assuming, static Q) fails coverage under distribution shift (their ablation); AS-CQR fixes this online but only via scalar feedback γ(α − miss indicator) — window m and γ are fixed hyperparameters; no per-region/per-horizon adaptive learning rates.
- Coverage guarantee is marginal long-run average (Eq. 25), not finite-sample per-step conditional coverage.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{2026_Yu_EnergyMamba,
  title     = {EnergyMamba: An Uncertainty-Aware Graph-Enhanced Selective State Space Model for Energy Consumption Prediction},
  author    = {Yu, Dahai and Xu, Rongchao and Jiang, Lin and Wang, Guang},
  booktitle = {Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26)},
  year      = {2026},
  address   = {Jeju Island, Republic of Korea},
  publisher = {ACM},
  pages     = {1--12},
  doi       = {10.1145/3770855.3818841}
}
```

## 🔗 Key References & Citation Graph
- Builds directly on **Mamba** (Gu & Dao, COLM 2024) [ref 10] — the selective SSM backbone; see vault page [[Mamba_SSM]]. Related Mamba-family baselines it cites: G-Mamba (Graph-Mamba, arXiv 2402.00789) and U-Mamba (arXiv 2401.04722); closest prior bidirectional-Mamba forecasting work in the vault: [[2024_BiMamba_Bidirectional_Mamba_Forecasting]] (not cited by this paper).
- Uncertainty lineage: **Conformalized Quantile Regression** (Romano, Patterson & Candès, NeurIPS 2019) [ref 36] → static CQR baseline; **Adaptive Conformal Inference** (Gibbs & Candès, NeurIPS 2021) [ref 9] → the α̃_t update rule in Eq. (24). Vault anchor for TS conformal: [[2021_Conformal_Time_Series_Forecasting]]; DER-side adaptive recalibration: [[2024_Conformal_Prediction_DER]].
- Cites **PatchTST** (Zeng et al., ICLR 2023) as a Transformer baseline → [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]]; RMSNorm from Zhang & Sennrich 2019 [ref 57].
- Same-group predecessor systems cited: TrustEnergy (AAAI '26, meta-learning + conformal) and UQGNN (SIGSPATIAL '25) — the direct accuracy/calibration competitors it outperforms.
- Does **not** cite Attention Is All You Need or the Mamba-3 line — no wikilink drawn to them from this note.
