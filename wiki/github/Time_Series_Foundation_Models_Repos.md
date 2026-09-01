---
type: github
name: Time Series Foundation Models Repositories
category: Deep Learning Core & Foundation Architecture Codebases
tags:
  - github
  - foundation-models
  - transformers
  - mamba
  - state-space-models
---

# 🐙 Time Series Foundation Models Repositories

## Overview
This note indexes foundational open-source repositories for time-series Transformer variants, State Space Models (Mamba), and baseline linear models benchmarked across EV load forecasting literature.

## Repositories & Citation Graph

### 1. iTransformer (Inverted Transformers for Time Series)
- **Repository URL**: `https://github.com/thuml/iTransformer`
- **Description**: Official ICLR 2024 implementation applying self-attention over inverted variate dimensions.
- **Cited Paper**: [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]]

### 2. Mamba & Mamba-3 (State Space Models)
- **Repository URL**: `https://github.com/state-spaces/mamba`
- **Description**: Official selective state space model implementation with linear $O(N)$ sequence length scaling.
- **Cited Paper**: [[2026_Lahoti_Mamba_3_Sequence_Modeling]]

### 3. Autoformer (Decomposition Transformers with Auto-Correlation)
- **Repository URL**: `https://github.com/thuml/Autoformer`
- **Description**: NeurIPS 2021 implementation introducing series decomposition blocks and Auto-Correlation mechanisms.
- **Cited Paper**: [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]]

### 4. TimesNet (Temporal 2D-Variation Modeling)
- **Repository URL**: `https://github.com/thuml/TimesNet`
- **Description**: ICLR 2023 implementation transforming 1D time series into 2D spaces to model intraperiod and interperiod variations.
- **Cited Paper**: [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]]

### 5. Crossformer (Cross-Dimension Dependency Transformer)
- **Repository URL**: `https://github.com/Thinklab-SJTU/Crossformer`
- **Description**: ICLR 2023 implementation capturing cross-time and cross-dimension dependencies using Two-Stage Attention.
- **Cited Paper**: [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]]

### 6. FEDformer (Frequency Enhanced Decomposed Transformer)
- **Repository URL**: `https://github.com/MAZiqing/FEDformer`
- **Description**: ICML 2022 implementation performing attention operations in Fourier and Wavelet frequency domains.
- **Cited Paper**: [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]]

### 7. Informer (Beyond Efficient Transformer for Long Sequence)
- **Repository URL**: `https://github.com/zhouhaoyi/Informer2020`
- **Description**: AAAI 2021 Best Paper implementation introducing ProbSparse self-attention and distilling operation.
- **Cited Paper**: [[2021_Zhou_Informer_Beyond_Efficient_Transformer]]

### 8. LTSF-Linear / DLinear / NLinear (Linear Model Baselines)
- **Repository URL**: `https://github.com/cure-lab/LTSF-Linear`
- **Description**: AAAI 2023 implementation benchmarking lightweight linear decomposition models against Transformers.
- **Cited Paper**: [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]]

---

## 🆕 Newly Catalogued ([2026-08-23] Thorough Re-Ingestion Pass)

### 9. TFT (Temporal Fusion Transformer, official Google Research implementation)
- **Repository URL**: `https://github.com/google-research/google-research/tree/master/tft`
- **Cited Paper**: [[2021_Lim_TFT_Temporal_Fusion_Transformers]]
- **What you can reuse**:
  - *Code*: reference multi-horizon implementation (LSTM encoder-decoder + variable selection networks + static covariate encoders), full training/evaluation scripts.
  - *Data*: data-formatting pipelines for Favorita retail and Oxford-Man realized volatility benchmarks.
  - *Pretrained*: none official, but configs reproduce paper results on the included benchmarks; attention-weight interpretability utilities are directly reusable for EV station forecasting.

### 10. TiDE (Time-series Dense Encoder, official Google Research implementation)
- **Repository URL**: `https://github.com/google-research/google-research/tree/master/tide`
- **Cited Paper**: [[2024_Das_TiDE_Long_Term_Forecasting]]
- **What you can reuse**:
  - *Code*: compact MLP encoder-decoder with covariance feature projections — a fast, Transformer-free long-horizon baseline.
  - *Pretrained*: none; training configs for Weather/ETT/Traffic/Electricity benchmarks included.

### 11. PatchTST (Patch Time Series Transformer)
- **Repository URL**: `https://github.com/yuqinie98/PatchTST` *(official code; not surfaced as a link in the re-ingestion pass but cited in-corpus)*
- **Cited Paper**: [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]]
- **What you can reuse**:
  - *Code*: patching + channel-independence backbone, supervised & self-supervised (masked pretraining) variants.
  - *Pretrained*: self-supervised checkpoints on Electricity/ETT usable for transfer to EV load series.

### 12. Tensor2Tensor (Original Transformer framework)
- **Repository URL**: `https://github.com/tensorflow/tensor2tensor`
- **Cited Paper**: [[2017_Attention_Is_All_You_Need]]
- **What you can reuse**:
  - *Code*: canonical multi-head attention / positional encoding implementations (TF1) useful for ablation references when reimplementing in PyTorch.
  - *Data*: sequence-to-sequence problem registry (WMT 2014 En-De/En-Fr).

### 13. MAML & MAML-RL (Model-Agnostic Meta-Learning)
- **Repository URL**: `https://github.com/cbfinn/maml` ; RL variant: `https://github.com/cbfinn/maml_rl`
- **Cited Paper**: [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]]
- **What you can reuse**:
  - *Code*: first-order inner/outer gradient loop — the template behind few-shot adaptation schemes (cf. Reptile-based [[2023_Huang_MetaProbformer_EV_Load]]).
  - *Pretrained*: none; lightweight enough to wrap any PyTorch forecaster for per-station few-shot fine-tuning.

### 14. TCN (Temporal Convolutional Network, official empirical evaluation)
- **Repository URL**: `https://github.com/locuslab/TCN`
- **Cited Paper**: [[2018_Bai_Empirical_TCN_Sequence_Modeling]]
- **What you can reuse**:
  - *Code*: minimal `Chomp1d` + dilated causal conv blocks (`TemporalBlock`, `TemporalConvNet`) — drop-in encoders for hybrid LSTM/Transformer EV models (e.g., MQ-TCN transfer learning).
  - *Data*: scripts for sequence modeling (add/jazz), word-level PTB, and anomaly-thresholded TS benchmarks.

### 15. SCINet (Sample Convolution and Interaction Network)
- **Repository URL**: `https://github.com/cure-lab/SCINet` *(cited as related code in the RevIN paper)*
- **Cited Paper**: [[2022_Kim_RevIN_Reversible_Instance_Normalization]]
- **What you can reuse**:
  - *Code*: downsample–interact–reconstruct long-term forecasting architecture; pairs naturally with RevIN normalization modules from the same lineage.
  - *Pretrained*: none; experiment configs cover ETT/Electricity/Traffic benchmarks shared with Informer/Autoformer comparisons.

### 16. Neuralforecast / NHiTS (Nixtla unified library)
- **Repository URL**: `https://github.com/Nixtla/neuralforecast`
- **Cited Paper**: [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]]
- **What you can reuse**:
  - *Code*: production-grade unified API for NHiTS, N-BEATS, TFT, LSTM, and dozens more forecasters with cross-validation utilities.
  - *Data*: built-in loaders (LongHorizon, M4, etc.) plus automatic hyperparameter optimization hooks (`auto` models via Optuna) — fastest route to strong EV-load baselines.

### 17. TimeMachine (Quadruple-Mamba Long-Term Forecasting) — *added in [2026-08-23] re-ingestion*
- **Repository URL**: `https://github.com/Atik-Ahamed/TimeMachine`
- **Cited Paper**: [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]]
- **What you can reuse**:
  - *Code*: two-stage MLP embedding + quadruple-Mamba blocks with channel-mixing/channel-independence switching by tensor transposition; RevIN integration and LTSF training configs.
  - *Data*: Weather/ETT/Electricity/Traffic loaders mirroring the iTransformer protocol (L=96, T ∈ {96,192,336,720}).

### 18. Bi-Mamba+ (Bidirectional Forget-Gated Mamba Forecasting) — *added in [2026-08-23] re-ingestion*
- **Repository URL**: `https://github.com/Leopold2333/Bi-Mamba+`
- **Cited Paper**: [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]]
- **What you can reuse**:
  - *Code*: custom CUDA backward pass for the forget-gated Mamba+ block, bidirectional encoder, and the Series-Relation-Aware (Spearman-based) channel-strategy decider — directly transferable to multi-station EV series.
  - *Pretrained*: none; scripts reproduce Electricity/Traffic/Solar/ETT benchmarks.

### 19. pykan (Kolmogorov-Arnold Networks, official implementation)
- **Repository URL**: `https://github.com/KindXiaoming/pykan` *(install: `pip install pykan`)*
- **Cited Paper**: [[2024_Liu_KAN_Kolmogorov_Arnold_Networks]]
- **What you can reuse**:
  - *Code*: KAN layers with learnable B-spline edge activations, grid-extension refinement, sparsification/pruning/symbolification pipeline for interpretable small models (e.g., KAN decoders as in [[2026_Hao_Mamba_KAN_HyKANet_EV]]).
  - *Pretrained*: none; toy/Feynman/knot-theory experiment notebooks included.

### 20. PowerMamba (Dual-Path SSM for Power Systems) + ERCOT GridSet toolbox — *added in [2026-08-23] ingestion pass*
- **Repository URL**: `https://github.com/alimenati/PowerMamba`
- **Cited Paper**: [[2024_Menati_PowerMamba_Power_Systems_SSM]]
- **What you can reuse**:
  - *Code*: dual-path standard/inverse Mamba blocks + series decomposition + external-forecast token module; full benchmarking toolbox (baselines via thuml Time-Series-Library) reproducing the GridSet experiments.
  - *Data*: **[[ERCOT_GridSet]]** — 5-year hourly ERCOT 2019–2023 (43,824 h), 22 core channels / extended 262-channel version with external day-ahead load & renewable forecasts.

### 21. grid-forecast-benchmark (SSM vs Transformer vs RNN on US EIA-930 grids) — *added in [2026-08-23] ingestion pass*
- **Repository URL**: `https://github.com/gramm-ai/grid-forecast-benchmark`
- **Cited Paper**: [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]]
- **What you can reuse**:
  - *Code*: architecture-matched implementations of S-Mamba/[[PowerMamba]]/PatchTST/iTransformer/LSTM with shared preprocessing, weather-fusion layers, and capacity-controlled tiers; checkpoints included.
  - *Data*: EIA-930 hourly demand pipelines for six/seven US ISOs plus Open-Meteo weather-covariate alignment.

### 22. Sundial (Highly Capable Time Series Foundation Models — TimeFlow + Decoder-Only Patched Transformer)
- **Repository URL**: `https://github.com/thuml/Sundial`
- **Weights (Hugging Face, 3 sizes)**: `https://huggingface.co/thuml/sundial-base-128m` (also Small 32M / Large 444M)
- **Cited Paper**: [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- **What you can reuse**:
  - *Code*: decoder-only patched Transformer (6/12/24 layers, RoPE, Pre-LN, FlashAttention, KV Cache) + FM-Net flow-matching head (Eq. 6-8); training/inference scripts with S3 univariate format and multi-patch prediction (F > P).
  - *Data*: **[[TimeBench]]** curation scripts (1,032B points, 12 sources, ERA5 406B dominant) and GIFT-Eval/FEV zero-shot evaluation pipelines.
  - *Pretrained*: 3 checkpoints (Small 32M / Base 128M / Large 444M) — zero-shot SOTA on TSLib long-term, GIFT-Eval (MASE 0.673 #1) and FEV (35x speedup over Chronos).

