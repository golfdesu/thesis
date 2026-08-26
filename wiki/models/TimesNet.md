---
type: model
name: TimesNet
category: Deep Learning / Temporal 2D-Variation Modeling (General Time Series Backbone)
tags:
  - model
  - deep-learning
  - cnn
  - fft
  - general-time-series
---

# 🕸️ TimesNet

## Overview
TimesNet (Wu et al., ICLR 2023) is a **task-general backbone** for five mainstream time-series tasks — short- and long-term forecasting, imputation, classification, anomaly detection — achieving consistent SOTA across all of them. Core idea: real-world series exhibit **multi-periodicity**; each period induces coupled **intraperiod** (within-period, columns) and **interperiod** (across-periods, rows) variations, so the 1D series is transformed into a set of **2D tensors** processable by mature vision backbones ([[Inception_2D_CNN]]).

Key equations:
- FFT period discovery with top-$k$ frequencies and periods $p_i = \lceil T/f_i \rceil$:
$$A = \text{Avg}\left(\text{Amp}\left(\text{FFT}(X_{1D})\right)\right), \quad \{f_1,\dots,f_k\} = \arg\text{Top}_k\left(A\right)$$
- 1D→2D reshaping: $X^i_{2D} = \text{Reshape}_{p_i,f_i}\left(\text{Padding}(X_{1D})\right)$, then $\tilde{X}^{l,i}_{2D} = \text{Inception}\left(X^{l,i}_{2D}\right)$ on deep features.
- Adaptive amplitude-weighted aggregation (inspired by Auto-Correlation):
$$X^l_{1D} = \sum_{i=1}^{k} \text{Softmax}\left(A^{l-1}_{f_i}\right) \times \tilde{X}^{l,i}_{1D}, \qquad X^l_{1D} = \text{TimesBlock}\left(X^{l-1}_{1D}\right) + X^{l-1}_{1D}$$

Shared weights across the $k$ tensors keep model size invariant to $k$; Inception is replaceable by ResNet/ConvNeXt/Swin. Smallest params among top models (0.067 MB constant across lengths 384–3072).

## Typical Usage in EV Load Forecasting
- **Input**: multivariate series with multi-periodicity (e.g., daily + weekly electricity cycles).
- **Forecasting Horizon**: both short-term (M4) and [[Long_Term_Forecasting]] ($T \in \{96,...,720\}$).
- **Strengths**: SOTA in >80% of forecasting cases (Electricity avg MSE 0.192); best imputation (ETTm1 avg MSE 0.027); anomaly F1 86.34%; unified pre-training potential demonstrated.
- **Weaknesses**: point forecasts only; sensitive to top-k frequency count in low-level tasks; no explicit cross-variate dependency mechanism.

## Literature Usage
- [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]] — Original paper: FFT periodicity → 2D variation modeling; beats DLinear/FEDformer/Informer across forecasting/imputation/classification/anomaly benchmarks.
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — Follow-up showing linear models fail classification/imputation while TimesNet still beats them at forecasting.
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Benchmark protocol and baseline provider; iTransformer surpasses TimesNet on ECL/Traffic/Solar via variate-token attention.
