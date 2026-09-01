---
type: paper
title: "TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning"
authors: [Andreas Auer, Patrick Podest, Daniel Klotz, Sebastian Böck, Günter Klambauer, Sepp Hochreiter]
year: 2025
journal_conference: "39th Conference on Neural Information Processing Systems (NeurIPS 2025)"
doi_url: "https://arxiv.org/abs/2505.23719"
models_used: ["[[TiRex]]", "[[xLSTM]]", "[[LSTM]]", "[[Chronos]]", "[[Chronos-Bolt]]", "[[TimesFM]]", "[[Moirai]]", "[[PatchTST]]", "[[TFT]]", "[[DLinear]]", "[[DeepAR]]", "[[TabPFN-TS]]", "[[TTM]]"]
datasets_used: ["[[GIFT-Eval]]", "[[GIFT_Eval_Pretrain]]", "[[Chronos_Corpus]]", "[[KernelSynth]]", "[[Electricity_ECL]]", "[[Solar_Dataset]]", "[[Weather]]", "[[M4]]", "[[ETT]]"]
features_used: ["[[Historical_Load]]", "[[Patched_Embeddings]]", "[[Dynamic_Covariates]]"]
forecasting_horizon: ["[[Short_Term_Forecasting]]", "[[Long_Term_Forecasting]]"]
metrics: ["[[CRPS]]", "[[MASE]]", "[[WQL]]"]
tags:
  - paper
  - time-series-foundation-model
  - zero-shot-forecasting
  - in-context-learning
  - xlstm
  - slstm
  - contiguous-patch-masking
  - long-horizon-forecasting
  - probabilistic-forecasting
---

# Summary: TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning

## 🎯 Main Objective & Contribution
- **Core Problem**: Existing pre-trained zero-shot time series foundation models (TSFMs) predominantly rely on Transformer architectures (e.g., Chronos, TimesFM, Moirai, MOIRAI-2). While Transformers excel at short-term in-context learning, they lack true recurrent state-tracking, leading to degradation on long-horizon forecasting where recurrent models like LSTMs traditionally hold an edge. Conversely, classical LSTMs have strong state-tracking but weak in-context learning capabilities.
- **Primary Novel Contribution**:
  1. **TiRex Architecture**: Introduces TiRex, a 35M-parameter decoder-only foundation model built on **xLSTM** (specifically scalar LSTM / **sLSTM** blocks with exponential gating and normalizer states). TiRex bridges the gap between Transformer in-context learning and LSTM recurrent state-tracking, retaining state-tracking across long sequences.
  2. **Contiguous Patch Masking (CPM)**: Proposes a novel training-time masking technique that randomly masks full contiguous sequences of future patches (representing multi-patch inference conditions as missing values). This allows the sLSTM internal memory state to propagate predictive context and uncertainty seamlessly without autoregressive point-prediction reinitialization.
  3. **Data Diversity Protocol**: Curates a 47.5M time-series pretraining corpus combining 30M extended Chronos real series (with z-score TsMixup), 15M continuous-periodicity synthetic Gaussian Process series (expanded KernelSynth), and 2.5M GiftEval pretraining series.
  4. **State-of-the-Art Zero-Shot Performance**: Sets a new SOTA on both **GiftEval-ZS** (CRPS 0.411, rank 1) and **Chronos-ZS** (WQL 0.592, rank 1), outperforming models with up to 14× more parameters (e.g., TimesFM-2.0 500M, Chronos-Bolt Base 200M, TabPFN-TS) while being 11× faster than TimesFM-2.0 and 2176× faster than TabPFN-TS.

---

## 🧠 Methodology & Model Architecture

### 1. Backbone Architecture (sLSTM xLSTM Blocks)
TiRex is structured as a decoder-only recurrent network that stacks 12 sLSTM blocks between lightweight residual patching input and quantile output projection heads. Unlike Matrix LSTM (mLSTM) which trades recurrent state-tracking for matrix memory parallelization, **sLSTM** preserves the scalar recurrent pathway and normalizer state $n_t$, yielding Turing-complete / counter-automaton expressivity higher than Transformers and State Space Models (SSMs).

### 2. Key Equations (G3 — verbatim, hard fail if skipped)

**Eq. 1 — Normalized Input Patch Mapping & Missing Mask**:
Given an input window of length $m_{\text{in}} = 32$, reversible instance normalization (RevIN) normalizes $\tilde{y}_{0:T} = (y_{0:T} - \bar{y}_{0:T}) / \sigma_{y_{0:T}}$, and a binary presence/absence mask $M \in \{0, 1\}^{m_{\text{in}}}$ is concatenated before the 2-layer residual projection:
$$x_t = \text{ResBlock}([ \tilde{y}_{t-m_{\text{in}}:t}, M_{t-m_{\text{in}}:t} ]) \in \mathbb{R}^d \tag{1}$$

**Eq. 2 — Quantile Multi-Patch Training Loss**:
TiRex directly outputs $|Q| = 9$ equidistant quantiles $Q = \{0.1, 0.2, \dots, 0.9\}$ for each time step in output patch window $m_{\text{out}} = 32$. The model optimizes the pinball quantile loss across all valid output tokens without differentiating between context and forecast during training:
$$\mathcal{L} = \frac{1}{|Q| m_{\text{out}}} \sum_{t=1}^{m_{\text{out}}} \sum_{q \in Q} \begin{cases} q (y_t - \hat{y}_t^q), & \text{if } \hat{y}_t^q \le y_t \\ (1 - q) (\hat{y}_t^q - y_t), & \text{otherwise} \end{cases} \tag{2}$$

**Eq. 3 — sLSTM Cell State Update**:
$$c_t = f_t \odot c_{t-1} + i_t \odot z_t \tag{3}$$

**Eq. 4 — sLSTM Normalizer State Update**:
$$n_t = f_t \odot n_{t-1} + i_t \tag{4}$$

**Eq. 5 — sLSTM Hidden State & Stabilized Normalization**:
$$h_t = o_t \odot \tilde{h}_t, \quad \tilde{h}_t = c_t \odot n_t^{-1} \tag{5}$$

**Eq. 6 — sLSTM Cell Input**:
$$z_t = \tanh(\tilde{z}_t), \quad \tilde{z}_t = W_z x_t + R_z h_{t-1} + b_z \tag{6}$$

**Eq. 7 — sLSTM Exponential Input Gate**:
$$i_t = \exp(\tilde{i}_t), \quad \tilde{i}_t = W_i x_t + R_i h_{t-1} + b_i \tag{7}$$

**Eq. 8 — sLSTM Exponential Forget Gate**:
$$f_t = \exp(\tilde{f}_t), \quad \tilde{f}_t = W_f x_t + R_f h_{t-1} + b_f \tag{8}$$

**Eq. 9 — sLSTM Output Gate**:
$$o_t = \sigma(\tilde{o}_t), \quad \tilde{o}_t = W_o x_t + R_o h_{t-1} + b_o \tag{9}$$
where $W_z, W_i, W_f, W_o \in \mathbb{R}^{d \times d_{\text{in}}}$, $R_z, R_i, R_f, R_o \in \mathbb{R}^{d \times d}$ are block-diagonal weight matrices across $N_h = 4$ heads (reducing parameter count to $d^2 / N_h$), and $b \in \mathbb{R}^d$ are learnable biases.

**Eq. 10 — TsMixup Data Augmentation**:
Convex combination of $k \sim \mathcal{U}(1, K_{\text{max}})$ z-score normalized time-series segments with length $l \sim \mathcal{U}(L_{\text{min}}, L_{\text{max}})$ using Dirichlet mixing weights $\lambda \sim \text{Dir}(\alpha)$:
$$x_{1:l}^{\text{mix}} = \sum_{i=1}^k \lambda_i \cdot \tilde{x}_{1:l}^{(i)}, \quad \text{where } K_{\text{max}} = 4, L_{\text{min}} = 128, L_{\text{max}} = 4096, \alpha = 1.5 \tag{10}$$

### 3. Contiguous Patch Masking (CPM) & Multi-Patch Horizon Forecast
- **Mechanism**: Rather than autoregressively feeding point estimates (mean/median) back as inputs for future steps (which collapses uncertainty and accumulates error), TiRex feeds missing-value tokens for all future steps $h > m_{\text{out}}$.
- **Training Strategy**: CPM randomly masks contiguous sequences of $c_{\text{mask}} \sim \mathcal{U}(1, c_{\text{mask}}^{\text{max}})$ patches with probability $p_{\text{mask}} \sim \mathcal{U}(0, p_{\text{mask}}^{\text{max}})$. This aligns training dynamics directly with multi-patch inference, forcing the internal sLSTM hidden state to track temporal dynamics and uncertainty across long unobserved horizons.

---

## 📊 Dataset & Input Features

### 1. Pretraining Corpus (47.5 Million Time Series)
- **Chronos Corpus (30M series)**: 30 million diverse real-world time-series augmented via TsMixup ($K_{\text{max}}=4, \alpha=1.5$) from HuggingFace `autogluon/chronos_datasets`.
- **Synthetic Gaussian Process Corpus (15M series)**: 15 million synthetic time series generated via random combinations of GP kernels (RBF, Periodic, Linear, Rational Quadratic, Piecewise Polynomial) with continuous periodicity sampling $\pi \sim \mathcal{U}(10, \min(512, T))$.
- **GiftEval Pretraining Subset (2.5M series)**: 2.5 million series from `Salesforce/GiftEvalpre-train` (sampled with 8% frequency).

### 2. Benchmark Datasets & Accessibility Links
- **Official Code & Pretrained Weights**: `https://github.com/NX-AI/tirex`
- **HuggingFace Chronos Pretraining Data**: `https://huggingface.co/datasets/autogluon/chronos_datasets`
- **HuggingFace GiftEval Pretraining Data**: `https://huggingface.co/datasets/Salesforce/GiftEvalpre-train`
- **GiftEval Benchmark (97 tasks across 7 domains)**: Includes [[Electricity_ECL]], [[Solar_Dataset]], [[Weather]], [[ETT]], Traffic, Web Traffic, Economics.
- **Chronos Zero-Shot Benchmark (27 datasets)**: Standard 27-dataset evaluation corpus from Ansari et al. (2024a).

---

## 📈 Performance & Results

### 1. Zero-Shot Benchmark Comparison
- **GiftEval-ZS (Zero-Shot setting excluding 16 overlapping tasks)** (Table 1 & Figure 4 p.7):
  - **TiRex (35M)**: **CRPS 0.411 ± 0.002**, **MASE 0.647 ± 0.004** (Rank 1 Overall, Rank 1 Short-Term CRPS 0.455, Rank 1 Long-Term CRPS 0.325).
  - **TimesFM 2.0 (500M)**: CRPS 0.460, MASE 0.680.
  - **TabPFN-TS**: CRPS 0.480, MASE 0.750.
  - **Chronos-Bolt Base (200M)**: CRPS 0.490, MASE 0.720.
  - **Chronos-Bolt Small (46M)**: CRPS 0.490, MASE 0.740.
  - **PatchTST (Task-specific)**: CRPS 0.500, MASE 0.760.
  - **Moirai-1.1 Large (311M)**: CRPS 0.510, MASE 0.790.
  - **TFT (Task-specific)**: CRPS 0.510, MASE 0.820.

- **Chronos-ZS Benchmark (27 datasets)** (Table 1 & Figure 5 p.8):
  - **TiRex (35M)**: **WQL 0.592 ± 0.007**, **MASE 0.776 ± 0.003** (Rank 1 WQL).
  - **TabPFN-TS**: WQL 0.610, MASE 0.760.
  - **Moirai-1.1 Large**: WQL 0.605, MASE 0.785 (note: 82% overlap with training data).
  - **Chronos-Bolt Base**: WQL 0.620, MASE 0.790.
  - **TimesFM 2.0**: WQL 0.650, MASE 0.830.

### 2. Architectural & CPM Ablation Study (Table 1 p.9)
- **Ablation of Backbone**:
  - **TiRex (12 sLSTM blocks)**: Gift-ZS Overall CRPS **0.411**, Long-Term CRPS **0.325**.
  - **xLSTM [1:11] (1 sLSTM + 11 mLSTM)**: Gift-ZS Overall CRPS 0.421, Long-Term CRPS 0.334.
  - **xLSTM [1:5] (1 sLSTM + 5 mLSTM)**: Gift-ZS Overall CRPS 0.428, Long-Term CRPS 0.339.
  - **mLSTM only (12 mLSTM blocks)**: Gift-ZS Overall CRPS 0.448, Long-Term CRPS 0.362 (severely degrades long-term).
  - **Transformer + RoPE**: Gift-ZS Overall CRPS 0.435, Long-Term CRPS 0.355.
  - **Chronos-Bolt Base Architecture (trained on same data)**: Gift-ZS Overall CRPS 0.442, Long-Term CRPS 0.360.
- **Ablation of CPM**:
  - **Naïve Multi-patch (Autoregressive)**: Gift-ZS Long-Term CRPS drops to **0.335** (MASE 0.460).
  - **Fixed Multi-patch**: Gift-ZS Long-Term CRPS drops to **0.342**.
  - **TiRex with CPM**: Gift-ZS Long-Term CRPS reaches **0.325**.

### 3. Inference Speed & GPU Memory Efficiency (p.8)
- Context length 2048, prediction length 32:
  - TiRex is **11× faster** than TimesFM 2.0.
  - TiRex is **4× faster** than Chronos-Bolt Base.
  - TiRex is **2176× faster** than TabPFN-TS.

---

## 💡 Limitations & Identified Research Gaps
1. **Univariate Formulation Only**: TiRex processes multivariate time series via channel-independence (independent univariate sequences), ignoring inter-variate cross-series correlations and spatio-temporal interactions.
2. **Deterministic Context Length (2048)**: While sLSTM allows long sequences, context windows remain bounded during standard pretraining.
3. **Absence of Dynamic Exogenous Covariates**: Cannot natively inject external future covariates (e.g., weather forecasts, EV arrival schedules, electricity price signals) without flattening them into univariate streams or mask channels.
4. **Relevance to EV Load Forecasting**: For EV charging stations, TiRex provides ultra-fast zero-shot probabilistic base forecasts (9 quantiles) across multiple horizons; however, capturing cross-station spatial coupling or traffic-EV interactions requires multivariate extensions (addressed subsequently in TiRex-2).

---

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{auer2025tirex,
  title={TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning},
  author={Auer, Andreas and Podest, Patrick and Klotz, Daniel and B{\"o}ck, Sebastian and Klambauer, G{\"u}nter and Hochreiter, Sepp},
  booktitle={Thirty-ninth Conference on Neural Information Processing Systems (NeurIPS 2025)},
  year={2025},
  url={https://arxiv.org/abs/2505.23719}
}
```

---

## 🔗 Key References & Citation Graph
- Cited Foundation Papers in Vault:
  - [[2021_TFT_Temporal_Fusion_Transformers]] — Temporal Fusion Transformers combining LSTM and multi-head attention.
  - [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — PatchTST patch-based channel-independent transformer.
  - Ansari et al. (2024) *Chronos: Learning the Language of Time Series* (Transactions on Machine Learning Research).
  - [[2024_TimesFM_Decoder_Only_Foundation_Model]] — TimesFM decoder-only foundation model.
  - [[2024_Unified_Training_Universal_Time_Series_Transformers]] — MOIRAI any-variate masked foundation model.
  - [[2025_Chronos_2_Univariate_to_Universal]] — Chronos-2 universal architecture.
  - Beck et al. (2024) *xLSTM: Extended Long Short-Term Memory* (NeurIPS 2024).
  - Hochreiter & Schmidhuber (1997) *Long Short-Term Memory* (Neural Computation).
