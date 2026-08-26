---
type: paper
title: "Mixer-Informer-Based Two-Stage Transfer Learning for Long-Sequence Load Forecasting in Newly Constructed Electric Vehicle Charging Stations"
authors: [Zhenhua Zhou, Bozhen Jiang, Qin Wang]
year: 2025
journal_conference: "arXiv preprint (submitted to Elsevier), arXiv:2505.06657 [eess.SY]"
doi_url: "https://doi.org/10.48550/arXiv.2505.06657"
models_used: ["[[MIK-TST]]", "[[MLP-Mixer]]", "[[Informer]]", "[[KAN]]"]
datasets_used: ["[[Boulder_Colorado]]"]
features_used: ["[[Historical_Load]]", "[[Calendar_Features]]", "[[Charging_Session_Logs]]", "[[Calendar_Features]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Mixer-Informer-Based Two-Stage Transfer Learning for Long-Sequence Load Forecasting in Newly Constructed Electric Vehicle Charging Stations

## 🎯 Main Objective & Contribution
Address EV charging station load forecasting when (a) long-sequence temporal dependencies (daily/weekly/seasonal cycles spanning hundreds–thousands of steps) must be captured, and (b) historical data are scarce because the station is newly constructed. Contributions:
1. **MIK hybrid architecture**: integrates an MLP-**Mi**xer module (multi-source feature fusion across temporal and channel dimensions), an **I**nformer module (long-range dependency capture via ProbSparse attention), and a **K**AN module (nonlinear approximation with learnable edge activation functions, improving interpretability).
2. **Two-stage transfer learning strategy (MIK-TST)**: pre-train on large multi-station source data, then fine-tune on data-scarce target stations (layer freezing / partial-full fine-tuning / small-batch learning), reducing dependence on extensive target-domain data.
3. **Empirical gains**: on 26 charging stations in Boulder, USA, MIK-TST beats PatchTST/Autoformer/DLinear/Crossformer/FreTS baselines by ~4% MAE and ~8% MSE.
4. Practical significance for smart-grid management and urban energy planning.

## 🧠 Methodology & Model Architecture
Pipeline: **Mixer (feature fusion) → Informer (temporal modeling) → KAN (nonlinear refinement)**, wrapped in a two-stage transfer learning pipeline.

**Input standardization (Standardization Equation):**
$$X_{std} = \frac{x_i - u}{\theta}$$
where $u$ is the mean and $\theta$ the standard deviation scaling factor.

### Mixer Module
Temporal-mixing layer (linear projection + fully connected ops over time steps) followed by feature/channel-mixing layer (same ops across feature channels).
**Mixer output equation:**
$$X_{Mixer} = f_L(X)$$
**Linear projection:**
$$f_L(X) = WX + b, \quad x \in \mathbb{R}^n,\ y \in \mathbb{R}^m,\ W \in \mathbb{R}^{m\times n},\ b \in \mathbb{R}^m$$
**Spatio-temporal block (residual composition):**
$$ST\_blocks(X) = X + f_C(X + f_T(X))$$
**Temporal mixing function:**
$$f_T(X) = \mathcal{R}(f_L(\sigma_{ReLU}(f_L(X))))$$
**Channel mixing function:**
$$f_C(X) = \mathcal{R}(f_L(\sigma_{ReLU}(f_L(X))))$$
where $\sigma_{ReLU}$ is the ReLU activation [Glorot et al.] and $\mathcal{R}$ denotes a regularization technique (Dropout, per ref. [16] Hinton et al.) — operator glyph not extractable from the PDF text.

### Informer Module
ProbSparse self-attention selects top key queries probabilistically, cutting quadratic attention cost.
**ProbSparse attention equation:**
$$Attention(Q, K, V) = \sigma_{softmax}\!\left(QK^{T}/\sqrt{d_k}\right)V$$
with Q, K, V linear projections of the input sequence and $d_k$ the key dimension. Encoder–decoder design.
**Informer output equation:**
$$X_{Informer} = Decoder(Encoder(X))$$
(decoder structure analogous to encoder; exact glyphs partially not extractable.)
**Decoder layer equation:**
$$T(X) = f_{conv2}(f_{conv1}(A(X)))$$
where $f_{conv1}, f_{conv2}$ are convolutional networks and $A(\cdot)$ is ProbSparse self-attention.

### KAN Module
Kolmogorov-Arnold Network: learnable univariate activation functions (B-splines) placed on edges instead of fixed activations at nodes.
**KAN output equation:**
$$y = \sum f_{ij}(X_i)$$
where $f_{ij}$ is the learnable activation connecting input feature $x_i$ to output node $j$.
**Edge spline activation equation:**
$$f_{ij}(x_i) = \sum c_k \cdot b_k(x_i)$$
where $b_k$ are basis functions (e.g., B-spline bases) and $c_k$ learnable coefficients.

### Two-Stage Transfer Learning
- **Pre-training** on source stations, Adam/AdamW optimizer, LR 1e-3–1e-4, dropout 0.1–0.3, L2 weight decay ≈ 1e-4.
**Source-domain MSE loss:**
$$L_{source} = \frac{1}{N}\sum_{i=1}^{N}\left(y_i - y'(\theta)\right)^2$$
- **Fine-tuning** on target stations: layer freezing (freeze Mixer + Informer, tune only KAN for station-specific traits), optional full fine-tuning at reduced LR (~1/10 initial) with early stopping, small batches (8/16) under extreme scarcity.
**Target-domain MSE loss:**
$$L_{target} = \frac{1}{M}\sum_{i=1}^{M}\left(y_i - y'(\theta)\right)^2$$

Implementation: PyTorch, embedding size 256 (Normal/Xavier init), Adam LR 1e-4, weight decay 0, MLP structure [256, 2048, 256], max 10 iterations. Baselines run with original paper settings.

## 📊 Dataset & Input Features
- **[[Boulder_Colorado]]** — City of Boulder Open Data, Boulder, Colorado, USA: historical records from **26 EV charging stations** (charging times, power consumption, user behavior patterns, station-level indicators).
  - URL: https://open-data.bouldercolorado.gov/datasets/95992b3938be4622b07f0b05eba95d4c_0/explore
  - Transfer setting: stations indexed 0–20 (by chronological order of first recorded activity) = **source domain** (full history for pre-training); stations 21–25 = **target domain**, fine-tuned only on small early data (prior to 2023), evaluated on future loads — simulating newly deployed stations.
- **Input features**: historical charging power, timestamps/calendar indicators (e.g., day-of-week flags), charging session logs, other station-level indicators; z-score style standardization applied.
- No external weather/traffic features used (noted as limitation).

## 📈 Performance & Results
Metrics: MAE and MSE (normalized domain).
**Evaluation metrics:**
$$MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i - \hat{y}_i| \qquad MSE = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2$$

**Main comparison (Table 1):**

| Model | MAE | MSE |
|---|---|---|
| PatchTST | 0.4638 | 0.7409 |
| Autoformer | 0.4845 | 0.6869 |
| DLinear | 0.4751 | 0.7293 |
| Crossformer | 0.4726 | 0.7319 |
| FreTS | 0.4670 | 0.7282 |
| **MIK-TST (ours)** | **0.4450 (−4%)** | **0.6322 (−8%)** |

Best baseline PatchTST beaten by 4% MAE and 8% MSE.

**Ablation (Table 2):**

| Variant | MAE | MSE |
|---|---|---|
| w/o-Mcl (no Mixer) | 0.4582 (+3%) | 0.6540 (+3.5%) |
| w/o-Kcl (no KAN) | 0.4508 (+1.3%) | 0.6338 (+0.3%) |
| w/o-Dcl (no two-stage transfer learning) | 0.4772 (+7.2%) | 0.7457 (+18%) |
| MIK-TST | 0.4450 | 0.6322 |

Transfer learning removal is the most damaging → indispensable for data-scarce new stations; Mixer + transfer learning act synergistically.

**Hyperparameter sensitivity (RQ3):**
- Hidden dim $d \in \{64,128,256,512,1024\}$: best at $d=256$ (MAE 0.4450, MSE 0.6322); d=64 → MAE 0.4599/MSE 0.6692; d=512 → 0.4475/0.6350; d=1024 → 0.4540 (overfitting).
- Attention heads $N_{heads} \in \{1,2,4,6,8,10\}$: best at 8 (0.4450/0.6322); 1 head → 0.4611/0.6837; 10 heads → 0.4456/0.6368.
- Encoder/decoder depth $r \in \{1,2,4,6\}$: best at $r=2$ (0.4450/0.6322); $r=4$ → 0.4561/0.6531, $r=6$ → 0.4599/0.6704 (overfitting on sparse fine-tuning data).

## 💡 Limitations & Identified Research Gaps
- Relies mainly on station-specific historical data; external variables (weather, traffic patterns, socio-economic factors) not modeled.
- Robustness in highly heterogeneous or rapidly evolving environments (drastically different usage profiles) unverified.
- Computational efficiency still a challenge for real-time deployment on resource-constrained systems despite ProbSparse attention.
- Future work: adversarial/domain-regularization-based domain adaptation; exogenous real-time features; model pruning/quantization for real-time energy management; uncertainty quantification via Bayesian/ensemble methods.
- Research gaps relevant here: cold-start forecasting for new stations via transfer learning ↔ [[2024_Ali_MQ_TCN_Transfer_Learning_EV]], [[2023_Huang_MetaProbformer_EV_Load]]; Informer-line evolution ↔ [[2021_Zhou_Informer_Beyond_Efficient_Transformer]], [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]]; KAN foundations ↔ [[2024_Liu_KAN_Kolmogorov_Arnold_Networks]]; benchmarked long-sequence backbones ↔ [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]], [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]], [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]], [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]]; same Boulder data reused for benchmarking ↔ [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]].

## 📚 BibTeX & Citation Reference
```bibtex
@article{zhou2025miktst,
  title   = {Mixer-Informer-Based Two-Stage Transfer Learning for Long-Sequence Load Forecasting in Newly Constructed Electric Vehicle Charging Stations},
  author  = {Zhou, Zhenhua and Jiang, Bozhen and Wang, Qin},
  journal = {arXiv preprint arXiv:2505.06657},
  year    = {2025},
  url     = {https://arxiv.org/abs/2505.06657},
  note    = {Affiliation: Department of Electrical and Electronic Engineering, The Hong Kong Polytechnic University}
}
```

## 🔗 Key References & Citation Graph
- Zhou et al. (2021), "Informer: Beyond efficient transformer for long sequence time-series forecasting," AAAI 2021 → backbone module; vault: [[2021_Zhou_Informer_Beyond_Efficient_Transformer]].
- Tolstikhin et al. (2021), "MLP-Mixer: An all-MLP architecture for vision," NeurIPS → Mixer module origin.
- Liu et al. (2024), "KAN: Kolmogorov-Arnold Networks," arXiv:2404.19756 → KAN module; vault: [[2024_Liu_KAN_Kolmogorov_Arnold_Networks]].
- Nie et al. (2022), PatchTST (arXiv:2211.14730) — baseline; vault: [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]].
- Wu et al. (2021), Autoformer (NeurIPS) — baseline; vault: [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]].
- Chen et al. (2022), DLinear (arXiv:2205.13504) — baseline; vault: [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]].
- Zhang & Yan (2023), Crossformer (ICLR) — baseline; vault: [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]].
- Yi et al. (2023), FreTS, NeurIPS — frequency-domain MLP baseline.
- Zhu et al. (2019), EV charging load comparative deep-learning study, Energies 12(14):2692; vault: [[2019_Zhu_EV_Load_Forecasting]].
- Wang K. et al. (2023), DRL-based transfer learning for EV charging strategy, Applied Energy 343:121186.
- Wang W. et al. (2025), weather-aware EV charging load forecasting, Applied Energy 383:125337.
- Al-Ogaili et al. (2019), review of scheduling/clustering/forecasting for EV charging, IEEE Access 7:128353–128371.
- Forootani et al. (2023), transfer learning + generative model for cold-start residential EV charging, IEEE Trans. Intelligent Vehicles 9(1):190–198.
- IEA Global EV Outlook 2024: https://www.iea.org/reports/global-ev-outlook-2024
