---
type: model
name: Informer
category: Deep Learning / Efficient Transformer for Long Sequence Time-Series Forecasting
tags:
  - model
  - deep-learning
  - transformer
  - long-term-forecasting
---

# ⚡ Informer

## Overview
Informer (Zhou et al., AAAI 2021 **Best Paper**) is an efficient Transformer for Long Sequence Time-Series Forecasting ([[Long_Term_Forecasting]]) that removes the three bottlenecks of the vanilla [[Transformer]]: quadratic $O(L^2)$ self-attention, $O(J \cdot L^2)$ memory when stacking $J$ layers, and slow step-by-step dynamic decoding. Its three distinctive components are:

- **ProbSparse self-attention** ($O(L \log L)$ time and memory): attention scores follow a long-tail distribution, so only Top-$u$ "dominant" queries are kept, measured by KL divergence from uniformity:
$$M(q_i, K) = \ln\sum_{j=1}^{L_K} e^{\frac{q_i k_j^\top}{\sqrt{d}}} - \frac{1}{L_K}\sum_{j=1}^{L_K} \frac{q_i k_j^\top}{\sqrt{d}}$$
approximated with a max–mean measurement over only $U = L_K \ln L_Q$ sampled dot-product pairs:
$$A(Q, K, V) = \text{Softmax}\left(\frac{\bar{Q}K^\top}{\sqrt{d}}\right)V, \qquad u = c \cdot \ln L_Q$$
- **Self-attention distilling**: Conv1d(ELU) + max-pooling halves the cascading layer input, giving total space complexity $O((2-\epsilon)L\log L)$:
$$X_{j+1}^t = \text{MaxPool}\Big(\text{ELU}\big(\text{Conv1d}([X_j^t]_{AB})\big)\Big)$$
- **Generative style decoder**: predicts the whole long horizon in ONE forward pass from a start token + zero placeholder ($X_{de}^t = \text{Concat}(X_{token}^t, X_0^t)$) with masked ProbSparse attention — avoiding cumulative error spreading of autoregressive decoding.

## Typical Usage in EV Load Forecasting
- **Input**: long historical load windows (encoder length 96 typical) + global/local timestamp embeddings.
- **Forecasting Horizon**: [[Long_Term_Forecasting]] (up to 720+ steps; predict-1440 demonstrated).
- **Strengths**: linear-ish scaling in sequence length; one-shot multi-step decoding; robust to temporal offsets; strong long-horizon accuracy (−26.6% to −60% MSE vs LSTMa at horizons 168–720).
- **Weaknesses**: multivariate advantage shrinks vs univariate; ProbSparse relies on long-tail sparsity assumptions; later shown by [[DLinear]] that its gains partly come from direct-multi-step decoding rather than attention itself.

## Literature Usage
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — Original paper: ProbSparse $O(L\log L)$ attention, distilling, generative decoder; wins 33/48 multivariate cases on ETT/ECL/Weather; reaches encoder input 1440 where LogTrans OOMs.
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — Direct successor using the ETT benchmark; Informer as key sparse-attention baseline beaten by Auto-Correlation (e.g., ETTh1 predict-336: 1.128→0.505 MSE).
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]] — Adding RevIN to Informer cuts ETTh2@960 MSE 2.972→0.600 and DTW 38.35→15.24 against distribution shift.
- [[2023_Huang_MetaProbformer_EV_Load]] — Informer adapted into the Gaussian-output [[MetaProbformer]]; plain Informer best non-meta baseline (ordering MetaProbformer < MetaTransformer < Informer < LSTM < Transformer < ARIMA).
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — Channel-independence applied to Informer improves it, yet PatchTST still dominates (ProbSparse baseline).
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — Gradually simplifying Informer (attention→linear→pure linear) *improves* MSE monotonically (Exchange T=96: 0.847→0.084); efficiency claims challenged (49.3 ms vs DLinear 0.4 ms).
- [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]] — Informer baseline far behind TimesNet on Electricity (avg MSE 0.311 vs 0.192).
- [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]] — Informer among eight baselines; dataset provider via Informer2020 repo.
- [[2024_Das_TiDE_Long_Term_Forecasting]] — Informer Traffic-96 MSE 0.733 vs TiDE 0.336; sub-quadratic attention approximations grouped as underperformers.
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Inverting duties promotes Informer by 28.5% average MSE reduction.
- [[2025_Bao_ResMMoT_Informer_Time_Series]] — ResMMoT-Informer couples a residual multiscale TCN sparse-expert network with an Informer module (ProbSparse) for global dependencies; beats plain Informer ~30–40% on NASDAQ100.
- [[2025_Tian_MSSTGAN_City_EV_Load]] — Informer baseline for city EV load; MSSTGAN outperforms it on 7-1/30-7 tasks across four datasets.
- [[2026_Chen_PC_M3_Mamba_EV_Clusters]] — Informer as flexibility-envelope baseline (Hausdorff 11.8/14.6 vs PC-M3 3.4/4.1); 18× slower inference than PC-M3 at 10k EVs.
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] — Informer weakest deep benchmark on ACN data (MAE 4.667 vs STL-Hybrid 0.614); also slowest relevant runtime (1.372 s inference).
- 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] — Causally-masked ProbSparse Informer + Gaussian head + per-station MAML adaptation: up to −51.21% RMSE50 and ~48% CRPS cut across ACN/Boulder/Palo Alto; few-shot ablation cuts RMSE50 36–48% vs vanilla Informer.
- 2026 — [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] — USDT extends the Informer backbone with SMAN multi-scale linear attention + DDI dual-direction interaction: EVnetNL RMSE 9.866→8.781 (−10.99%) with −36.5% peak VRAM; Informer cross-domain transfer degrades +102% vs USDT +27%.
- 2025 — [[2025_Zhou_MixerInformer_Transfer_Learning_New_EV_Stations]] — Informer (ProbSparse attention encoder–decoder) as the long-range temporal backbone inside MIK-TST (Mixer→Informer→KAN) with two-stage transfer for data-scarce new Boulder stations; full model MAE 0.4450/MSE 0.6322 (−4%/−8% vs PatchTST), beating Autoformer/DLinear/Crossformer/FreTS baselines.
