---
type: paper
title: "iTransformer: Inverted Transformers Are Effective for Time Series Forecasting"
authors: [Yong Liu, Tengge Hu, Haoran Zhang, Haixu Wu, Shiyu Wang, Lintao Ma, Mingsheng Long]
year: 2024
journal_conference: "ICLR 2024 (Spotlight)"
doi_url: "https://doi.org/10.48550/arXiv.2310.06625"
models_used: ["[[iTransformer]]", "[[Transformer]]", "[[Informer]]", "[[Reformer]]", "[[Flowformer]]", "[[FlashAttention]]", "[[PatchTST]]", "[[Crossformer]]", "[[DLinear]]", "[[TimesNet]]", "[[TiDE]]", "[[SCINet]]", "[[FEDformer]]", "[[Stationary_Transformer]]"]
datasets_used: ["[[Electricity_ECL]]", "[[ETT]]", "[[Exchange]]", "[[Traffic]]", "[[Weather]]", "[[Solar_Energy]]", "[[PEMS]]", "[[Market_Alipay]]"]
features_used: ["[[Variate_Tokens]]", "[[Series_Representations]]", "[[Multivariate_Correlation_Map]]", "[[Layer_Normalization]]", "[[Feed_Forward_Temporal_MLP]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MSE]]", "[[MAE]]", "[[CKA_Similarity]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: iTransformer: Inverted Transformers Are Effective for Time Series Forecasting

## 🎯 Main Objective & Contribution
- Diagnoses why [[Transformer]]-based forecasters underperform simple linear models in multivariate time series forecasting: embedding multiple variates of the *same timestamp* into one temporal token fuses distinct physical measurements (delayed events, inconsistent measurements), yields meaningless attention maps, and applies permutation-invariant attention to an order-sensitive dimension.
- Proposes **[[iTransformer]]**: simply **inverts** the duties of the native Transformer components without modifying them — each variate's whole lookback series is embedded as a **variate token**; **self-attention operates across variates** to capture multivariate correlations; the **feed-forward network operates along time** to learn series representations.
- Achieves comprehensive state-of-the-art on real-world benchmarks; shows the inversion framework consistently improves Transformer variants (38.9% avg promotion on vanilla Transformer, 36.1% Reformer, 28.5% Informer, 16.8% Flowformer, 32.2% Flashformer); enables generalization to unseen variates and better use of enlarged lookback windows.
- Code: https://github.com/thuml/iTransformer

## 🧠 Methodology & Model Architecture
Encoder-only Transformer with embedding → L inverted blocks → projection. Given lookback $X \in \mathbb{R}^{T\times N}$ (T steps, N variates), predict $\hat{Y} \in \mathbb{R}^{S\times N}$. The per-variate forecast is formulated as (**Eq. 1 – Overall formulation**):

$$h_n^0 = \text{Embedding}(X_{:,n}), \quad H^{l+1} = \text{TrmBlock}(H^l),\ l=0,\dots,L-1, \quad \hat{Y}_{:,n} = \text{Projection}(h_n^L)$$

where Embedding: $\mathbb{R}^T \mapsto \mathbb{R}^D$ and Projection: $\mathbb{R}^D \mapsto \mathbb{R}^S$ are MLPs; no positional embedding is needed since sequence order is implicitly stored in FFN neuron permutation.

- **Layer normalization** applied per-variate-token over its feature/series dimension (**Eq. 2 – Inverted LayerNorm**):

$$\text{LayerNorm}(H) = \left( \frac{h_n - \text{Mean}(h_n)}{\sqrt{\text{Var}(h_n)}} \;\middle|\; n = 1,\dots,N \right)$$

  Normalizing each variate token to a Gaussian diminishes discrepancies from inconsistent measurements (related to [[RevIN]] / stationarization).
- **Self-attention across variate tokens**: queries, keys, values $Q,K,V \in \mathbb{R}^{N\times d_k}$; pre-Softmax score entries form the multivariate correlation map $A \in \mathbb{R}^{N\times N}$ (**Eq. 3 – Variate attention scores**):

$$A_{i,j} = \left(\frac{QK^\top}{\sqrt{d_k}}\right)_{i,j} \propto q_i^\top k_j$$

  Highly correlated variates are weighted more for value interaction; score maps are interpretable (shallow layers resemble raw lookback correlations, deeper layers approach future correlations).
- **FFN along time**: shared feed-forward network applied identically to each variate token, encoding observed series and decoding future series via dense non-linear connections (universal approximation; combines benefits of linear forecasters + channel independence).
- **Efficient training strategy**: randomly sample part of variates per batch during training, forecast all variates at inference — comparable accuracy with greatly reduced memory footprint.
- Training: PyTorch, single NVIDIA P100 16GB, [[Adam]] optimizer, lr ∈ {10⁻³, 5×10⁻⁴, 10⁻⁴}, L2 loss, batch size 32, 10 epochs, L ∈ {2,3,4}, D ∈ {256, 512}, fixed lookback T=96.

## 📊 Dataset & Input Features
7 public benchmarks (+6 private Market subsets), TimesNet chronological train/val/test splits:

| Dataset | Dim | Freq | Size (train/val/test) |
|---|---|---|---|
| ETTh1/h2 | 7 | hourly | (8545, 2881, 2881) |
| ETTm1/m2 | 7 | 15 min | (34465, 11521, 11521) |
| Exchange | 8 | daily | (5120, 665, 1422) |
| Weather (Max Planck Biogeochemistry Inst., 2020) | 21 | 10 min | (36792, 5271, 10540) |
| [[Electricity_ECL]] (321 clients) | 321 | hourly | (18317, 2633, 5261) |
| Traffic (SF Bay Area freeways, 862 sensors, Jan 2015–Dec 2016) | 862 | hourly | (12185, 1757, 3509) |
| Solar-Energy (137 PV plants, 2006; LSTNet) | 137 | 10 min | (36601, 5161, 10417) |
| PEMS03/04/07/08 (California traffic networks) | 358/307/883/170 | 5 min | e.g. PEMS07 (16911, 5622, 5622) |
| Market-Merchant/Wealth/Finance/Terminal/Payment/Customer (Alipay server load, Jan 30–Apr 9 2023) | 285–759 | 10 min | (7045, 1429, 1429) |

- Prediction lengths S ∈ {96, 192, 336, 720} (PEMS {12,24,36,48}; Market {12,24,72,144}); lookback T=96 (Market 144).
- Features = raw variate series; no exogenous features. Data/code availability: https://github.com/thuml/iTransformer (baselines reproduced from the TimesNet benchmark repository).

## 📈 Performance & Results
Averaged MSE/MAE over all horizons vs baselines:
- **ECL**: 0.178/0.270 (best; PatchTST 0.205/0.290, TimesNet 0.192/0.295, Autoformer 0.227/0.338). Per-horizon ECL MSE: 0.148 (96), 0.162 (192), 0.178 (336), 0.225 (720).
- **Traffic**: 0.428/0.282 (best; PatchTST 0.481/0.304, RLinear 0.626/0.378).
- **Solar-Energy**: 0.233/0.262 (best; PatchTST 0.270/0.307).
- **Weather**: 0.258/0.278 (best; PatchTST 0.259/0.281).
- **PEMS avg**: 0.119/0.218, essentially tied with SCINet 0.121/0.222; PatchTST fails on fluctuating PEMS (0.217/0.305).
- **ETT avg**: 0.383/0.399 (comparable to RLinear 0.380/0.392); Exchange 0.360/0.403.
- Inversion promotions: Transformer→iTransformer 35.6% MSE reduction on ECL/Traffic, 60.2% on Weather, 86.1% on ETT; Informer −28.5%, Flowformer −16.8%, Reformer −36.1%, Flashformer −32.2% (avg).
- Generalization: trained on 20% of variates, iTransformers forecast all unseen variates with small degradation (e.g., ECL +0.034 MSE) vs large CI-Transformer degradation (e.g., Traffic +0.113).
- Efficiency (Traffic 96→96): iTransformer 1.66GB/91ms with flow attention or 20%-variate training vs PatchTST 8.58GB/635ms, Crossformer 9.74GB/702ms.
- Ablations confirm attention-on-variate + FFN-on-temporal is optimal; vanilla arrangement worst (e.g., Traffic 0.913 MSE).

## 💡 Limitations & Identified Research Gaps
- Quadratic complexity O(N²) in number of variates for high-dimensional datasets; mitigated by efficient attentions or variate sampling but not solved natively.
- Under univariate scenarios iTransformer degrades into a stackable linear forecaster; temporal dependency modeling could be further enhanced (structural TCN-like embeddings suggested).
- Distribution shift handling left to layer norm; explicit non-stationarity modules remain future work.
- Future directions stated by authors: large-scale pre-training / foundation models for diverse multivariate series, more time series analysis tasks, fine-grained variate tokenization and better embedding mechanisms.
- No probabilistic forecasts (point predictions only, L2 loss) — relevant gap for EV charging demand uncertainty quantification.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{liu2024itransformer,
  title     = {iTransformer: Inverted Transformers Are Effective for Time Series Forecasting},
  author    = {Liu, Yong and Hu, Tengge and Zhang, Haoran and Wu, Haixu and Wang, Shiyu and Ma, Lintao and Long, Mingsheng},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — vanilla Transformer whose components are repurposed on inverted dimensions
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — source of ECL/Traffic/Weather/Exchange benchmarks and component-adaptation baseline
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — efficient attention variant promoted by inversion; source of ETT datasets
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — patching/channel-independence prior SOTA; iTransformer framed as extreme patching
- [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]] — cross-dimension dependency alternative that underperforms iTransformer
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — linear forecaster motivating the reflection
- [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]] — benchmark protocol and baseline
- [[2024_Das_TiDE_Long_Term_Forecasting]] — MLP-based dense encoder baseline
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]] — instance normalization related to inverted LayerNorm
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]], [[2018_Bai_Empirical_TCN_Sequence_Modeling]], [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] — cited TCN/RNN/linear forecaster lineage
