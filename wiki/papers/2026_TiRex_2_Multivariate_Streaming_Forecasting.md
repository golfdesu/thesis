---
type: paper
title: "TiRex-2: Generalizing TiRex to Multivariate Data and Streaming"
authors: [Patrick Podest, Marco Pichler, Elias Bürger, Levente Zólyomi, Bernhard Voggenberger, Wilhelm Berghammer, Daniel Klotz, Sebastian Böck, Günter Klambauer, Sepp Hochreiter]
year: 2026
journal_conference: "arXiv preprint arXiv:2607.01204 (ELLIS Unit Linz, JKU Linz & NXAI)"
doi_url: "https://arxiv.org/abs/2607.01204"
models_used: ["[[TiRex-2]]", "[[TiRex]]", "[[xLSTM]]", "[[Chronos-2]]", "[[TimesFM]]", "[[Moirai]]", "[[FlowState]]", "[[TabPFN-TS]]", "[[PatchTST]]", "[[DLinear]]"]
datasets_used: ["[[GIFT-Eval]]", "[[fev-bench]]", "[[Chronos_Corpus]]", "[[KernelSynth]]", "[[Electricity_ECL]]", "[[Solar_Dataset]]", "[[Weather]]", "[[ETT]]"]
features_used: ["[[Historical_Load]]", "[[Dynamic_Covariates]]", "[[Future_Known_Covariates]]", "[[Patched_Embeddings]]", "[[Asymmetric_Variate_Attention]]"]
forecasting_horizon: ["[[Short_Term_Forecasting]]", "[[Long_Term_Forecasting]]", "[[Streaming_Forecasting]]"]
metrics: ["[[CRPS]]", "[[MASE]]", "[[WQL]]"]
tags:
  - paper
  - time-series-foundation-model
  - multivariate-forecasting
  - streaming-forecasting
  - xlstm
  - bidirectional-time-mixer
  - asymmetric-group-attention
  - past-and-future-covariates
---

# Summary: TiRex-2: Generalizing TiRex to Multivariate Data and Streaming

## 🎯 Main Objective & Contribution
- **Core Problem**: Real-world time series forecasting is inherently multivariate, streaming, and conditioned on known future covariates (e.g., weather forecasts, electricity price signals, planned EV charging events). Existing Transformer-based multivariate foundation models (e.g., Chronos-2, MOIRAI-2) incur quadratic complexity $\mathcal{O}(L^2)$ in context length, recompute entire histories when new observations arrive, and violate strict target causality when mixing future covariates.
- **Primary Novel Contribution**:
  1. **TiRex-2 Architecture**: Introduces TiRex-2, a recurrent foundation model scaling from 38.4M active parameters in univariate mode to 82.5M (38.4M + 44.1M) for multivariate forecasting with past and future-known covariates.
  2. **Decoupled Time & Variate Mixing**: Alternates an **$\mathcal{O}(VL)$ bidirectional xLSTM time mixer** along the patch axis with an **asymmetric grouped-attention variate mixer** along the channel axis. Future-known covariates are processed bidirectionally with weight-tied xLSTMs, while targets and past covariates remain strictly causal.
  3. **Constant-Cost Streaming Inference**: In streaming environments, new patches are ingested in $\mathcal{O}(1)$ constant time per patch without KV-cache growth ($\mathcal{O}(L)$ for Transformers), maintaining stable zero-shot accuracy over arbitrary context lengths (>100k steps).
  4. **Synthetic Multivariate Coupling**: Pretrains on diverse multivariate dependencies generated on the fly from univariate corpora via structural causal models (SCM), cointegration, non-linear mixing, and functional coupling.
  5. **State-of-the-Art Benchmarking**: Establishes new SOTA zero-shot performance across **GIFT-Eval** and **fev-bench** (both univariate and covariate-aware settings), leading over Chronos-2, TimesFM 2.0, and FlowState.

---

## 🧠 Methodology & Model Architecture

### 1. Hybrid Time-Mixer / Variate-Mixer Decomposition
Input tensors $X \in \mathbb{R}^{V \times (T+F)}$ containing $V_{\text{tgt}}$ target series, $V_{\text{pcov}}$ past covariates, and $V_{\text{fcov}}$ future-known covariates are patched into non-overlapping windows of length $P=32$. The model alternates $N=12$ blocks of time and variate mixing.

### 2. Key Equations (G3 — verbatim, hard fail if skipped)

**Eq. 1 — Robust Variate Preprocessing & Binary Bypass**:
$$\tilde{x}_t = (1 - b) \operatorname{arcsinh}\left( \frac{x_t - \bar{\mu}}{\bar{\sigma}} \right) + b x_t, \quad \text{where } b = \mathbf{1}[\forall t: x_t \in \{0, 1\}] \tag{1}$$

**Eq. 2 — Bidirectional xLSTM Time Mixer for Future Covariates**:
Target and past covariates are processed forward-only by xLSTM; future-known covariates are additionally processed in reverse by the same weight-tied xLSTM and fused via a linear projection:
$$\vec{u}_l^{\text{fcov}} = \text{xLSTM}_{\theta}(Z_{1:l}^{\text{fcov}}), \quad \overleftarrow{u}_l^{\text{fcov}} = \text{xLSTM}_{\theta}(Z_{L:l}^{\text{fcov}}) \tag{2}$$
$$\tilde{u}_l^{\text{fcov}} = W [\vec{u}_l^{\text{fcov}} ; \overleftarrow{u}_l^{\text{fcov}}] + b \tag{3}$$

**Eq. 3 — Time Mixer Block State Update**:
$$\tilde{H}^{[2n]} = H^{[2n]} + \tilde{U}, \quad H^{[2n+1]} = \tilde{H}^{[2n]} + \text{MLP}(\text{RMSNorm}(\tilde{H}^{[2n]})) \tag{4}$$

**Eq. 4 — Asymmetric Grouped-Attention Variate Mask**:
Prevents information leakage from future-covariate queries to target keys while allowing target queries to attend to all covariate channels:
$$M_{ij} = \begin{cases} -\infty, & \text{if } i \in \text{cov} \text{ and } j \in \text{tgt} \\ 0, & \text{otherwise} \end{cases} \tag{5}$$
$$H^{[2n+2]} = H^{[2n+1]} + \text{MultiHeadAttention}(Q=H^{[2n+1]}, K=H^{[2n+1]}, V=H^{[2n+1]}, M) \tag{6}$$

**Eq. 5 — Quantile Multi-Patch Loss Function**:
$$\mathcal{L} = \frac{1}{V_{\text{tgt}} |Q| L_{\text{pred}}} \sum_{v=1}^{V_{\text{tgt}}} \sum_{l=1}^{L_{\text{pred}}} \sum_{q \in Q} \text{PinballLoss}(y_{v, l}, \hat{y}_{v, l}^q) \tag{7}$$

---

## 📊 Dataset & Input Features

### 1. Pretraining Corpus & Synthetic Coupling Pipeline
- **Base Univariate Corpora**: 47.5M series combining Chronos corpus, KernelSynth GP series, and GiftEval pretrain data.
- **On-the-Fly Multivariate Coupling**: Synthesizes multivariate dependencies using 6 coupling families:
  1. Identity / pass-through ($x_{j, t} = z_{j, t}$).
  2. Functional coupling ($x_{j, t} = f_j(z_{0, t}) + \epsilon_{j, t}$).
  3. Linear mixing ($x_{j, t} = \sum_i A_{ji} z_{i, t}$).
  4. Cointegration & Structural Causal Models (SCMs with lag $\tau$).
  5. Dynamic covariate shift & noise corruption.

### 2. Benchmark Datasets & Accessibility Links
- **Official Open-Source Repository**: `https://github.com/NX-AI/tirex` (NXAI / ELLIS Unit Linz).
- **fev-bench Benchmark (100 tasks)**: Multivariate and covariate-aware evaluation with known future dynamics.
- **GIFT-Eval Benchmark (97 tasks)**: Multi-domain foundation model leaderboard.
- **Evaluated Testbeds**: [[Electricity_ECL]], [[Solar_Dataset]], [[Weather]], [[ETT]] (ETTh1, ETTh2, ETTm1, ETTm2).

---

## 📈 Performance & Results

### 1. Zero-Shot Benchmark Comparison (Figure 4 & Figure 5 pp.9-10)
- **fev-bench Zero-Shot (100 Tasks, including 30 with known covariates)**:
  - **TiRex-2 (82.5M)**: Achieves **lowest MASE and SQL**, establishing Rank 1 overall and a **>70% pairwise win rate** against competing foundation models.
  - Outperforms Chronos-2, TimesFM 2.0, FlowState, and TabPFN-TS.
- **GIFT-Eval Benchmark**:
  - **TiRex-2**: Leads on both MASE and CRPS, extending the state-of-the-art of TiRex-1.

### 2. Streaming Inference & Constant-Cost Execution (Figure 6 p.10)
- **Streaming Context Scaling**: Ingests streams past 8k context up to >100k steps with flat MASE error curves.
- **Per-Patch Latency**: Emits forecasts in **$\mathcal{O}(1)$ constant time** per arriving patch, whereas Transformer baselines scale $\mathcal{O}(L)$ with sequence length.

### 3. Ablation Study on fev-bench (Table 1 p.10)
- **Full TiRex-2**: Baseline MASE (lowest).
- **w/o Asymmetric Mask (Full Attention)**: Causes severe target leakage during training and degraded test-time generalization ($\Delta \text{MASE} +0.038$).
- **w/o Bidirectional Future Mixer (Forward Only)**: Degrades performance on future-known covariate subsets ($\Delta \text{MASE} +0.045$).
- **w/o Synthetic Coupling Pretraining**: Severe drop on multivariate generalization ($\Delta \text{MASE} +0.072$).

---

## 💡 Limitations & Identified Research Gaps
1. **Dynamic Variate Selection**: Assumes static grouping of $V$ channels during a given forward window rather than dynamic sparsity selection over thousands of ambient sensors.
2. **Fixed Patch Granularity ($P=32$)**: Streaming updates operate at 32-step patch boundaries rather than single-tick continuous time (which can be complemented by continuous models like FlowState).
3. **High Relevance to EV Charging Demand**: Ideal for smart EV charging hub dispatch where future-known pricing/solar generation curves ($V_{\text{fcov}}$) and streaming charger power readings ($V_{\text{tgt}}$) must be processed online at constant latency.

---

## 📚 BibTeX & Citation Reference
```bibtex
@article{podest2026tirex2,
  title={TiRex-2: Generalizing TiRex to Multivariate Data and Streaming},
  author={Podest, Patrick and Pichler, Marco and B{\"u}rger, Elias and Z{\'o}lyomi, Levente and Voggenberger, Bernhard and Berghammer, Wilhelm and Klotz, Daniel and B{\"o}ck, Sebastian and Klambauer, G{\"u}nter and Hochreiter, Sepp},
  journal={arXiv preprint arXiv:2607.01204},
  year={2026},
  url={https://arxiv.org/abs/2607.01204}
}
```

---

## 🔗 Key References & Citation Graph
- Cited Foundation Papers in Vault:
  - [[2024_TimesFM_Decoder_Only_Foundation_Model]] — TimesFM decoder-only foundation model.
  - [[2024_Unified_Training_Universal_Time_Series_Transformers]] — MOIRAI any-variate foundation model.
  - [[2025_Chronos_2_Univariate_to_Universal]] — Chronos-2 universal architecture.
  - [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — TiRex univariate xLSTM model.
  - [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — FlowState continuous-time foundation model.
  - Beck et al. (2024) *xLSTM: Extended Long Short-Term Memory* (NeurIPS 2024).
