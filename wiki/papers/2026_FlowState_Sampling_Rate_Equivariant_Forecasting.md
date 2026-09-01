---
type: paper
title: "FlowState: Sampling-Rate-Equivariant Time-Series Forecasting"
authors: [Lars Graf, Thomas Ortner, Stanisław Woźniak, Angeliki Pantazi]
year: 2026
journal_conference: "Proceedings of the 43rd International Conference on Machine Learning (ICML 2026), PMLR 306"
doi_url: "https://arxiv.org/abs/2508.05287"
models_used: ["[[FlowState]]", "[[Mamba_SSM]]", "[[S5]]", "[[HiPPO]]", "[[TimesFM]]", "[[Chronos]]", "[[Chronos-Bolt]]", "[[Moirai]]", "[[TiRex]]", "[[TTM]]", "[[PatchTST]]", "[[DLinear]]"]
datasets_used: ["[[GIFT-Eval]]", "[[Chronos_Corpus]]", "[[KernelSynth]]", "[[Electricity_ECL]]", "[[Solar_Dataset]]", "[[Weather]]", "[[ETT]]"]
features_used: ["[[Historical_Load]]", "[[Continuous_Time_Basis]]", "[[Legendre_Polynomials]]", "[[Dynamic_Covariates]]"]
forecasting_horizon: ["[[Short_Term_Forecasting]]", "[[Long_Term_Forecasting]]", "[[Continuous_Horizon]]"]
metrics: ["[[MASE]]", "[[CRPS]]", "[[WQL]]"]
tags:
  - paper
  - time-series-foundation-model
  - state-space-model
  - ssm
  - functional-basis-decoder
  - sampling-rate-equivariant
  - continuous-time
  - zero-shot-forecasting
  - icml-2026
---

# Summary: FlowState: Sampling-Rate-Equivariant Time-Series Forecasting

## 🎯 Main Objective & Contribution
- **Core Problem**: Existing time series foundation models (TSFMs) based on Transformers, patch tokenizers, or discrete RNNs are inherently fixed to discrete grids. They lack adaptability to different or unseen sampling rates (e.g., predicting 15-min data from 1-hour context), struggle with varying context and target lengths, and incur high computational and memory costs.
- **Primary Novel Contribution**:
  1. **FlowState Architecture**: Introduces FlowState, a continuous-time foundation model pairing a State Space Model (**S5-based SSM encoder**) with a novel **Functional Basis Decoder (FBD)** using orthogonal Legendre polynomials (and Fourier bases).
  2. **Sampling-Rate Equivariance**: By adjusting continuous discretization scaling factors ($s_{\Delta_E}, s_{\Delta_F}$), FlowState processes inputs and generates forecasts at arbitrary, continuous temporal resolutions and horizons without retraining.
  3. **Parallel Horizon Pretraining**: Implements a training strategy where 4,076 causal forecasts of varying context lengths ($L_{\text{min}}=20$ to $L=4096$) are trained simultaneously per sequence in parallel without autoregressive rollout.
  4. **State-of-the-Art Efficiency**: Despite having only **18.6M parameters** (FlowState-18.6M) and a tiny 3M variant (FlowState-3M), it sets a new SOTA on the comprehensive **GIFT-Eval benchmark** (MASE 0.706, CRPS 0.442), outperforming TimesFM-2.5 (500M) and Chronos-Bolt (200M) while running up to orders of magnitude faster.

---

## 🧠 Methodology & Model Architecture

### 1. Model Structure & Discrete State Space Formulation
FlowState comprises $N=12$ S5 layers with gating and MLPs, followed by the Functional Basis Decoder (FBD). It operates directly on raw unpatched points without quantization or tokenization.

### 2. Key Equations (G3 — verbatim, hard fail if skipped)

**Eq. 1 — S5 Block State Transition & Output**:
$$\begin{aligned} s_t^l &= \bar{A}_l s_{t-1}^l + \bar{B}_l x_t^{l-1} \\ c_t^l &= \bar{C}_l s_t^l \\ o_t^l &= c_t^l \odot \sigma(W_l c_t^l + b_l) + \bar{D}_l x_t^{l-1} \end{aligned} \tag{1}$$
where $s_t^l \in \mathbb{C}^P$ is the latent state, $\bar{A}_l \in \mathbb{C}^{P \times P}$, $\bar{B}_l \in \mathbb{C}^{P \times c}$, $\bar{C}_l \in \mathbb{R}^{H \times P}$, $\bar{D}_l \in \mathbb{R}^{H \times c}$, and $W_l, b_l$ parameterize the gating mechanism.

**Eq. 2 — Continuous-to-Discrete ZOH Discretization**:
$$\bar{A}_l = \exp(A_l \Delta_E^l), \quad \bar{B}_l = A_l^{-1} (\bar{A}_l - I) B_l, \quad \bar{C}_l = C_l, \quad \bar{D}_l = D_l \tag{2}$$
where $\Delta_E^l$ is the step size adjusted by scale factor $s_{\Delta_E}$ according to input sampling rate.

**Eq. 3 — Functional Basis Decoder (FBD) Output Mapping**:
The final SSM encoder state $o_t^N \in \mathbb{R}^H$ is projected to polynomial basis coefficients $c \in \mathbb{R}^{K \times |Q|}$:
$$c = W_{\text{FBD}} o_t^N + b_{\text{FBD}} \tag{3}$$

**Eq. 4 — Continuous Function Space Reconstruction**:
$$\tilde{y}(t) = \sum_{i=1}^K c_i p_i(t), \quad t \in [a, b] \tag{4}$$
where $\{p_i\}_{i=1}^K$ are shifted orthonormal **Legendre polynomials** over interval $[a, b]$.

**Eq. 5 — Equidistant Discretized Sampling**:
$$\hat{y} = \text{sample}(\tilde{y}, \Delta_F) = \text{FBD}_{\Delta_F}(o_t^N) \tag{5}$$

**Eq. 6 — Discretization Scaling for Unseen Sampling Rates**:
$$\bar{\Delta}_E = s_{\Delta_E} \cdot \Delta_E, \quad \bar{\Delta}_F = s_{\Delta_F} \cdot \Delta_F \tag{6}$$
where $s_{\Delta} = \frac{\text{Base Seasonality}}{\text{Dataset Seasonality}}$, allowing FlowState to handle cross-rate conversions ($\Delta_E \neq \Delta_F$).

**Eq. 7 — Equivariance Error Bound**:
$$e_{\text{equi}} := \| F_{\Delta'}(x) - \text{FBD}_{\Delta'}(\text{SSM}_{\Delta}(x)) \| = \| \text{FBD}_{\Delta'}(\text{SSM}_{\Delta'}(x)) - \text{FBD}_{\Delta'}(\text{SSM}_{\Delta}(x)) \| \tag{7}$$

**Eq. 8 — Causal Running Normalization & Variance**:
$$\mu_{r, t} = \frac{1}{t} \sum_{i=1}^t x_i^{(0)}, \quad \sigma_{r, t}^2 = \frac{1}{t} \sum_{i=1}^t (x_i^{(0)} - \mu_{r, i})^2 \tag{8}$$
$$\tilde{x}_{1:t}^{(0)} = \frac{x_{1:t}^{(0)} - \mu_{r, 1:t}}{\sigma_{r, 1:t}} \tag{9}$$

---

## 📊 Dataset & Input Features

### 1. Pretraining Corpus
- **Chronos Pretraining Corpus**: 30M series from `autogluon/chronos_datasets` augmented via TsMixup.
- **Synthetic KernelSynth Gaussian Process Data**: 15M series.
- **GiftEval Pre-training Data**: 2.5M series from `Salesforce/GiftEvalpre-train`.

### 2. Benchmark Datasets & Accessibility Links
- **Official HuggingFace Space & Code**: `https://huggingface.co/ibm-research/flowstate`
- **GIFT-Eval Benchmark Leaderboard**: `https://huggingface.co/spaces/Salesforce/GIFT-Eval` (97 evaluation settings across 7 domains).
- **Evaluated Testbeds**: [[Electricity_ECL]], [[Solar_Dataset]], [[Weather]], [[ETT]] (ETTh1, ETTh2, ETTm1, ETTm2).

---

## 📈 Performance & Results

### 1. GIFT-Eval Benchmark Leaderboard (Full Evaluation) (Table 1 p.7)
- **FlowState-18.6M (Context 4k)**: **MASE 0.706**, **CRPS 0.442** (Rank 1 Overall).
- **FlowState-3M (Context 4k)**: **MASE 0.718**, **CRPS 0.446** (Rank 2 Overall).
- **TimesFM-2.5 (500M)**: MASE 0.724, CRPS 0.468.
- **Chronos-Bolt Base (200M)**: MASE 0.735, CRPS 0.490.
- **Moirai-1.1 Large (311M)**: MASE 0.760, CRPS 0.510.
- **TiRex (35M)**: MASE 0.650 (on zero-shot subset), evaluated as stateful baseline.
- **PatchTST (Task-specific)**: MASE 0.770, CRPS 0.500.

### 2. Adaptability to Unseen Sampling Rates (Zero-Shot Cross-Resolution) (Figure 2 & Table 2)
- Tested cross-frequency prediction (e.g., ETT1h context at $\Delta=1.0\text{h}$ forecasting 15-min targets at $\Delta_F=0.25\text{h}$):
  - FlowState achieves seamless continuous curves aligning with ground-truth 15-min dynamics without retraining.
  - Baseline Transformers (TimesFM, Chronos) fail completely or require heuristic interpolation.

### 3. Ablation Study on Basis Functions & Architecture (Table 2 p.8)
- **Default Legendre Basis (FlowState-3M)**: MASE **0.725**, CRPS **0.449**.
- **Fourier Basis Decoder**: MASE 0.738, CRPS 0.458.
- **Full-Legendre Basis**: MASE 0.732, CRPS 0.454.
- **Linear Resolution-Agnostic Decoder (No FBD)**: MASE degraded to **0.754** (confirming FBD is essential).
- **Real SSM vs Complex S5**: Replacing complex diagonal SSM with real diagonal decreases MASE to 0.735.

---

## 💡 Limitations & Identified Research Gaps
1. **Polynomial Truncation Error**: Truncating Legendre polynomials to $K$ basis terms limits extremely high-frequency oscillation representation beyond degree $K$.
2. **Channel-Independent Univariate Processing**: Multivariate series are handled by mapping each variate independently, omitting spatial cross-channel correlations.
3. **Application to EV Charging Stations**: Highly suited for multi-resolution EV charging operations (e.g., converting 1-hour grid feeder telemetry into 5-minute ultra-fast charger control signals dynamically without model re-training).

---

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{graf2026flowstate,
  title={FlowState: Sampling-Rate-Equivariant Time-Series Forecasting},
  author={Graf, Lars and Ortner, Thomas and Wo{\'z}niak, Stanis{\l}aw and Pantazi, Angeliki},
  booktitle={Proceedings of the 43rd International Conference on Machine Learning (ICML 2026)},
  series={Proceedings of Machine Learning Research},
  volume={306},
  year={2026},
  url={https://arxiv.org/abs/2508.05287}
}
```

---

## 🔗 Key References & Citation Graph
- Cited Foundation Papers in Vault:
  - [[2021_TFT_Temporal_Fusion_Transformers]] — Temporal Fusion Transformers combining LSTM and attention.
  - [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — PatchTST patch-based forecasting.
  - [[2024_TimesFM_Decoder_Only_Foundation_Model]] — TimesFM decoder-only model.
  - [[2024_Unified_Training_Universal_Time_Series_Transformers]] — MOIRAI any-variate masked model.
  - [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — TiRex xLSTM stateful foundation model.
  - Gu et al. (2021) *Efficiently Modeling Long Sequences with Structured State Spaces (S4)* (NeurIPS 2021).
  - Smith et al. (2023) *Simplified State Space Layers for Sequence Modeling (S5)* (ICLR 2023).
