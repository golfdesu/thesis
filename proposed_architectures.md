# 🚀 Proposed Architectural Innovations for EV Charging Load Forecasting

This document outlines three high-impact architectural proposals to overcome the limitations of current Transformer-based models for EV charging load forecasting. These proposals are synthesized from the gap analysis of all 103 ingested research papers (see [[research_gaps]] and [[index]]).

---

## 🔥 Proposal 1: The Hybrid Mamba-Transformer (Focus: Efficiency & Long-term Dependency)
**Objective:** Break the $O(N^2)$ complexity barrier of standard Transformers (Gap T-1) and advance into the post-Transformer era (Gap T-7).

* **The Problem in Literature:** Standard Transformers consume excessive memory and computational time when processing long historical sequences (e.g., 2 weeks of 15-minute resolution data).
* **The Proposed Novelty:**
  - **Hybrid Architecture:** Utilize **Mamba (State Space Model)**, which scales linearly $O(N)$, for efficient historical time-series feature extraction.
  - **Targeted Cross-Attention:** Deploy a lightweight Transformer (Cross-Attention) layer solely at the final stage to fuse the Mamba-extracted temporal features with exogenous variables (e.g., weather, Time-of-Use pricing, traffic data).
* **Key Selling Point:** This model will be significantly faster and lighter than conventional Transformers while possessing a superior ability to capture both ultra-long temporal dependencies and multivariate external influences.
* **➡️ Keywords for further study:** `Mamba`, `State Space Models (SSM)`, `Cross-Attention` *(See Prerequisites below)*

---

## 🔥 Proposal 2: Physics-Informed Probabilistic Transformer (Focus: Risk Management & Economic Laws)
**Objective:** Solve the black-box nature of Transformers and shift from point forecasting to reliable uncertainty quantification (Gaps T-3, T-4, P-1 to P-5).

* **The Problem in Literature:** Deep learning models often learn spurious correlations (e.g., falsely associating high peak TOU prices with higher demand). Furthermore, deterministic point forecasts provide no confidence intervals for downstream grid risk management, while standard quantile models suffer from quantile crossing (P-1), marginal path independence (P-2), and adaptation lag under non-stationarity (P-3).
* **The Proposed Novelty:**
  - **Probabilistic Head:** Replace standard Dense output layers with a **PICNN (Partially Input Convex Neural Network)** head or integrate **Adaptive Conformal Prediction**. This generates guaranteed non-crossing Prediction Intervals (PIs) for quantile forecasting while addressing extreme peak tail sharpness.
  - **Physics-Informed Loss (PINN):** Constrain the attention weights during training using economic elasticity rules (e.g., enforcing an inverse relationship between price spikes and load demand) and **Peak-Weighted Asymmetric Pinball Loss**.
* **Key Selling Point:** The resulting model will be highly reliable, interpretable, and immune to behavioral elasticity errors, providing actionable uncertainty bounds for grid operators.
* **➡️ Keywords for further study:** `Probabilistic Forecasting`, `Quantile Regression`, `Pinball Loss`, `PICNN`, `Conformal Prediction` *(See Prerequisites below)*

---

## 🔥 Proposal 3: Dynamic PatchTST for EV Networks (Focus: Time-series Inductive Bias)
**Objective:** Rectify the inappropriate application of NLP-based tokenization to continuous time-series data (Gaps T-2, T-5).

* **The Problem in Literature:** Feeding time-series data point-by-point destroys local semantic meaning, often causing Transformers to underperform LSTMs in short-term forecasting. Additionally, multi-station forecasts typically rely on static distance graphs.
* **The Proposed Novelty:**
  - **Patching Mechanism:** Adopt a **Patching** strategy (similar to PatchTST) to segment the time-series into sub-sequences (e.g., 4-hour blocks) before tokenization, preserving local temporal structures.
  - **Dynamic Spatial Attention:** Instead of fixed geographic graphs, implement a dynamic Graph Attention Network (GAT) layer where the adjacency matrix is recomputed at every time step, capturing real-time EV migration and congestion cascading between stations.
* **Key Selling Point:** A custom-tailored inductive bias designed specifically for EV charging behavior that dominates traditional baselines in short-term accuracy, while dynamically mapping city-wide charging mobility.
* ⚠️ *Refresh caveat (2026-08-23):* EVformer ([[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]]) already implements physical+semantic Top-K dynamic spatial attention for citywide EV load — this proposal must be positioned as adding **probabilistic output and per-timestep adjacency learning** on top, not as the first dynamic-graph EV Transformer.
* **➡️ Keywords for further study:** `PatchTST`, `Time-Series Patching`, `Dynamic Graph Attention Networks (GAT)` *(See Prerequisites below)*

---

### 💡 Recommendation for Maximum Impact
To achieve publication in a Top-Tier Q1 Journal, the most promising approach is to **combine Proposal 1 with the output head of Proposal 2**.

**The Ultimate Architecture (The "Winning" Formula):**
> **Mamba Backbone** (for fast historical encoding $O(N)$) + **Cross-Attention Layer** (for weather/price fusion) + **PICNN / Conformalized Quantile Head** (for coherent probabilistic output solving Gaps P-1 to P-5)

> [!NOTE] **Global Novelty Verified (re-checked 2026-08-23 against all 103 local papers, incl. papers 81–103)**
> - The full re-ingestion (103 papers in `wiki/papers/`, all verified) still confirms **0 overlap** between the Mamba backbone and the PICNN/Conformalized Quantile frameworks: [[2026_Lahoti_Mamba_3_Sequence_Modeling]], [[2026_Hao_Mamba_KAN_HyKANet_EV]], [[2026_Chen_PC_M3_Mamba_EV_Clusters]], plus the foundational TimeMachine ([[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]]) and Bi-Mamba+ ([[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]]) lines are all **point-forecast** Mamba/SSM models with no probabilistic heads, while [[2025_Zheng_Coherent_Hierarchical_EV_Load]] (PICNN) and [[2024_Zhou_Conformal_Prediction_DER]] (hierarchical conformal) use no Mamba/SSM backbones.
> - **New nearest neighbors from papers 81–103 (each narrows the claim but misses ≥2 of the 3 components):**
>   - [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] — Transformer + quantile head + **post-hoc CQR conformal calibration** for EV load. Backbone is TFT (LSTM-attention), calibration is a *single static validation split* (no adaptivity under shift → Gap P-3 open), quantile head is a plain linear layer (**no PICNN monotonicity** → Gap P-1 open). No Mamba, no cross-attention exogenous fusion.
>   - [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] (USDT) — native probabilistic Transformer (per-step Gaussian + CRPS) on Informer/Probformer backbone. No Mamba, no coverage guarantees, covariates limited to calendar/station IDs.
>   - [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] (MAML-Informer) — probabilistic few-shot per-station forecasting with PICP/CRPS/Winkler. Plain quantile heads: no conformal layer, no convexity constraint, no Mamba.
> - Caveat refined: the corpus now contains **Mamba + attention hybrids** (HyKANet's dynamic adjacency module; MFT's scale-masked cross-attention in [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]]) — so *Mamba + cross-attention alone* is no longer claimable as novel. Likewise "first probabilistic/conformalized/dynamic-graph EV Transformer" claims are now refuted by USDT / MoghadamDost / EVformer ([[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]]) respectively.
> - **What remains unexplored (precisely):** the full combination — **Mamba backbone + cross-attention exogenous fusion + conformalized PICNN head** — i.e., an $O(N)$ SSM encoder fused with external drivers via attention, producing *monotonic* quantiles with *distribution-free* coverage that *adaptively recalibrates* under non-stationarity. No paper in the 103-paper corpus implements or ablates this combination; it remains the thesis's defensible novelty per Gaps 6 / T-7 / P-1..P-5 in [[research_gaps]].

---

## 📚 Required Prerequisites & Learning Path
To successfully implement the recommended **"Winning Formula"**, the following concepts and frameworks must be studied:

### 1. State Space Models (SSMs) & Mamba
- **Concept:** Understand continuous-time differential equations discretized for deep learning, specifically Structured State Space sequence models (S4) and the hardware-aware selective state space model (Mamba).
- **Practical Skill:** Learn the `mamba-ssm` PyTorch library (developed by Albert Gu and Tri Dao). Understand how to adapt its token-mixing block for continuous multi-variate time-series instead of NLP tokens.
- **Key Paper to Read:** *Mamba: Linear-Time Sequence Modeling with Selective State Spaces (Gu & Dao, 2023)* and *Mamba-3 (2026)*.

### 2. Cross-Attention Mechanisms
- **Concept:** Differentiate between Self-Attention (Query, Key, Value from the same source) and Cross-Attention (Query from the historical sequence, Key/Value from external features like weather or price embeddings).
- **Practical Skill:** Implement a custom multi-head cross-attention layer in PyTorch to fuse heterogeneous data sources effectively without losing temporal resolution.

### 3. Probabilistic Forecasting & Quantile Regression
- **Concept:** Move beyond Mean Squared Error (MSE) and understand the **Pinball Loss (Quantile Loss)** to predict upper, median, and lower bounds (e.g., 10th, 50th, 90th percentiles).
- **Practical Skill:** Design a multi-output regression head in PyTorch and write a custom training loop that minimizes the Pinball Loss across multiple quantiles simultaneously.

### 4. Partially Input Convex Neural Networks (PICNN)
- **Concept:** Learn how to enforce mathematical convexity in neural networks to prevent **quantile crossing** (a common error where the predicted lower bound is mathematically higher than the upper bound).
- **Practical Skill:** Understand how to constrain neural network weights (e.g., using non-negative weights on specific paths) to guarantee monotonically increasing quantile outputs.
- **Key Paper to Read:** *Input Convex Neural Networks (Amos et al., 2017)* and *Coherent Hierarchical Probabilistic Forecasting of EV Charging Demand (Zheng, 2025)*.

---

## 🆕 New Proposals Informed by the 2026 Corpus Lines (added 2026-08-23)

The re-ingestion confirmed three active architectural frontiers in the corpus. These are scoped as *comparators and extensions* for the flagship formula above, not replacements.

### Proposal 8: KAN-Augmented Probabilistic Mamba (HyKANet extension)
- **Corpus basis:** [[2026_Hao_Mamba_KAN_HyKANet_EV]] shows Mamba + KAN learnable activations beating attention-based PAG by ~17% RMSE for EV demand.
- **Proposal:** Replace the MLP layers inside the PICNN quantile head with **KAN splines** to test whether learnable activation functions reduce the tail oversmoothing problem of Gap P-1 while preserving convexity constraints.
- **Relation to flagship:** This is an ablation of the winning formula's output head — same Mamba + cross-attention trunk.

### Proposal 9: Physics-Constrained Mamba Comparator (PC-M3 baseline)
- **Corpus basis:** [[2026_Chen_PC_M3_Mamba_EV_Clusters]] runs physics-constrained Mamba in MIMO mode over 10,000+ EV clusters in real time; [[2025_Meyer_Benchmark_Foundation_Models]] shows foundation models (Chronos, TimesFM) competitive only below ~4 weeks of history.
- **Proposal:** Benchmark the flagship model against (a) PC-M3-style physics-constrained Mamba and (b) zero-shot foundation models under the controlled EV benchmark of Proposal 5 — directly serving Gap T-7's missing Transformer-vs-Mamba-vs-hybrid comparison ([[research_gaps]]).

### Proposal 10: Horizon-Aware Benchmark with Classical Comparators (Kyriakopoulos extension)
- **Corpus basis:** [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] shows in a reproducible 4-city protocol that Transformers win only short-term horizons while GRU/LSTM win mid/long-term; [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] shows linear SGD matching DL at station level with performance plateauing after ~3 days of data; [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] provides a competitive non-DL hybrid (similar-day selection + NSGA-II).
- **Proposal:** Extend Proposal 5's controlled benchmark to include GRU/LSTM, linear (SGD/Lasso), and similar-day-selection baselines, reporting results per horizon band — any claimed Transformer/Mamba contribution must beat these cheap baselines or explain the horizon regime where it matters.
- **Relation to flagship:** This is a *defensive* evaluation gate for the winning formula; it also supplies the low-data axis (1/3/7/14 days) for the few-shot ablations informed by [[2025_Zhou_MixerInformer_Transfer_Learning_New_EV_Stations]] and [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]].

---

## Additional Proposals Based on the Current Benchmark

This section adds new proposals based on the current benchmark results. The original proposals above are retained unchanged.

### Proposal 4: Peak-aware Probabilistic Transformer

**Objective:** Reduce peak-load underestimation and provide reliable prediction intervals for multi-horizon forecasting.

**Motivation:**

- Peak Zone WAPE remains approximately 25–37% in the current benchmark.
- Autoformer performs best at the ultra-short-term horizon, while Informer performs best at 3–24 hours.
- All current benchmark models produce point forecasts only.

**Proposed design:**

- Use Informer or Autoformer as the backbone.
- Add quantile heads for P10, P50, and P90 forecasts.
- Combine Pinball Loss with a peak-weighted loss.
- Optionally use a PICNN head to prevent quantile crossing.
- Evaluate both point accuracy and uncertainty calibration.

**Evaluation metrics:** MAE, RMSE, WAPE, Peak Zone WAPE, CRPS, PICP, and Winkler Score.

**Research question:**

> Can a peak-aware probabilistic Transformer improve peak-load accuracy while maintaining calibrated prediction intervals across multiple forecasting horizons?

### Proposal 5: Controlled Multi-scale Transformer Benchmark

**Objective:** Determine which temporal representation is most suitable for EV charging load, which contains 30-minute, daily, and weekly patterns.

**Proposed comparison:**

- Point-wise temporal tokens.
- Fixed-size patches with sizes 2, 4, 8, and 12 steps.
- Multi-scale patches such as 2 + 8 + 48 steps.
- Series decomposition into trend, seasonal, and residual components.
- Variate-level tokens inspired by iTransformer.

All models should use the same dataset split, input window, prediction head, optimizer, and training budget.

**Motivation:** PatchTFT does not win consistently in the current benchmark. Therefore, patch size and tokenization should be studied systematically instead of drawing conclusions from a single patch-based model.

**Research question:**

> Which temporal tokenization strategy provides the best accuracy–efficiency trade-off for EV charging load forecasting at different horizons?

**Additional measurements:** training time, inference latency, GPU memory, and parameter count.

### Proposal 6: Context-aware Cross-attention Transformer

**Objective:** Incorporate external variables more systematically than directly concatenating them with historical load.

**Possible context variables:** weather, time-of-use price, calendar, traffic, station occupancy, arrival/departure time, and state of charge.

**Proposed design:**

- Use a historical-load encoder to create temporal representations.
- Use separate context encoders for weather, price, and session/context variables.
- Use cross-attention to select the context relevant to each future time step.
- Add feature attribution using SHAP and attention analysis.

**Required comparisons:** direct concatenation, GRN/Variable Selection Network, and cross-attention.

**Research question:**

> Does cross-attention improve the use and interpretability of exogenous variables compared with direct feature concatenation?

**Important caution:** Attention weights should be treated as model-interpretation evidence, not direct evidence of causal relationships.

### Proposal 7: Peak-aware Multi-scale Context Transformer

**Objective:** Combine the strongest elements of Proposals 4–6 into an integrated candidate architecture.

**Candidate architecture:**

```text
Historical Load
      |
      |-- RevIN / Decomposition
      |-- Multi-scale Temporal Patching
      `-- Transformer Encoder
                  |
External Context --+-- Cross-attention Fusion
                              |
                 Peak-aware Quantile Head
                              |
                    P10 / P50 / P90 Forecast
```

**Recommended ablation sequence:**

1. Baseline point Transformer.
2. Add a quantile head.
3. Add peak-weighted loss.
4. Add multi-scale representation.
5. Add cross-attention context fusion.
6. Add calibration or a PICNN constraint.

This sequence separates the contribution of the output head, loss function, temporal representation, and external-feature fusion.

## Updated Recommendation Without Removing the Original Proposals

The original proposals remain valid as possible extensions. The new proposals help prioritize experiments based on the current benchmark:

| Track | Role in Thesis | Priority |
|---|---|---:|
| Original Proposal 1: Hybrid Mamba-Transformer | Efficiency extension or optional comparison | 3 |
| Original Proposal 2: Physics-Informed Probabilistic Transformer | Long-term research direction | 2 |
| Original Proposal 3: Dynamic PatchTST for EV Networks | Spatial-temporal extension | 4 |
| New Proposal 4: Peak-aware Probabilistic Transformer | Main candidate contribution | 1 |
| New Proposal 5: Controlled Multi-scale Benchmark | Main experimental study | 1 |
| New Proposal 6: Context-aware Cross-attention | Optional feature-fusion contribution | 2 |
| New Proposal 7: Peak-aware Multi-scale Context Transformer | Integrated final architecture | 1 |
| Proposal 8: KAN-Augmented Probabilistic Mamba | Output-head ablation of flagship formula | 3 |
| Proposal 9: Physics-Constrained Mamba / Foundation-model Comparator | Benchmark extension (Gap T-7) | 2 |
| Proposal 10: Horizon-Aware Benchmark with Classical Comparators | Defensive evaluation gate (T-2 / Kyriakopoulos) | 1 |

## Suggested Thesis Formulation

> This thesis proposes and evaluates a peak-aware, multi-scale probabilistic Transformer for multi-horizon EV charging load forecasting. The study systematically compares temporal tokenization strategies and investigates whether context-aware cross-attention improves peak prediction and uncertainty calibration under a controlled benchmark.

The original Mamba, physics-informed learning, and dynamic spatial-attention proposals can remain as extension or future-work tracks without changing the original research direction.
