---
type: model
name: LogSparse Transformer
category: Deep Learning / Convolutional Log-Sparse Attention Transformer
tags:
  - model
  - deep-learning
  - transformer
  - probabilistic-forecasting
---

# 🪵 LogSparse Transformer

## Overview
The LogSparse Transformer (Li et al., NeurIPS 2019) is the first systematic application of the [[Transformer]] to multivariate time-series forecasting, fixing two canonical weaknesses: **(1) locality-agnosticism** — point-wise dot-product attention ignores local context/shape; **(2) memory bottleneck** — $O(L^2)$ attention blocks fine-grained long-sequence modeling.

Two mechanisms:
- **Convolutional self-attention**: causal convolutions (kernel $k$, stride 1) generate queries/keys so query–key matching uses local shape context (up to 9% relative improvement on traffic-c; faster convergence, lower training NLL):
$$O_h = \text{softmax}\left(\frac{Q_h K_h^T}{\sqrt{d_k}} \cdot M\right)V_h$$
- **LogSparse self-attention** with only $O(L(\log L)^2)$ memory — each cell attends to cells at exponential step distances plus itself:
$$I_l^k = \{l - 2^{\lfloor \log_2 l \rfloor},\ l - 2^{\lfloor \log_2 l \rfloor - 1},\ \dots,\ l - 2^0,\ l\}$$
Theorem 1: stacking $\lfloor \log_2 L \rfloor + 1$ layers guarantees every cell receives information from all previous cells, with super-exponentially many information paths. Extensions: **Local Attention** (dense window of size $O(\log_2 L)$) and **Restart Attention** (LogSparse within subsequences).

Decoder-only autoregressive mode with Gaussian likelihood head + softplus positivity and DeepAR-style scale handling.

## Typical Usage in EV Load Forecasting
- **Input**: historical values + time-based covariates (year/month/day-of-week/hour/minute/age/series-ID).
- **Forecasting Horizon**: [[Short_Term_Forecasting]] to medium-term (1-day to 30-day evaluations).
- **Strengths**: fine-grained forecasting under GPU memory budgets; beats DeepAR/DeepState/TRMF on electricity/traffic quantile losses (traffic-c 7d R0.5 0.139 vs DeepAR 0.179).
- **Weaknesses**: with identical input lengths full attention still mostly wins (except strong-long-dependency traffic-f); training unstable with vanilla Adam on 15-min data (BERTAdam workaround).

## Literature Usage
- [[2019_LogSparse_Enhancing_Locality_Transformer]] — Original paper: convolutional self-attention + log-sparse sparsity $O(L(\log L)^2)$; synthetic tests show LSTM/DeepAR degrade beyond ~96-step dependencies while Transformer holds accuracy.
- [[2021_Informer_Beyond_Efficient_Transformer]] — Direct precursor benchmarked as LogTrans: test complexity still $O(L^2)$, OOMs at encoder input 1440 where Informer succeeds.
- [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] — Attention ablation baseline: Auto-Correlation beats LogSparse attention at all input/prediction lengths.
- [[2023_DLinear_Are_Transformers_Effective_LTSF]] — LogTrans among the efficient Transformers beaten by one-layer linear models on all nine benchmarks.
- [[2023_MetaProbformer_EV_Load]] — Cited within the EV meta-learning forecaster lineage of locality-aware attention for charging-load sequences.
