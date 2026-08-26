---
type: model
name: PatchTST
category: Deep Learning / Patched Channel-Independent Transformer
tags:
  - model
  - deep-learning
  - transformer
  - long-term-forecasting
  - self-supervised
---

# 🩹 PatchTST

## Overview
PatchTST ("A Time Series is Worth 64 Words", Nie et al., ICLR 2023) answers the [[DLinear]] challenge by showing a vanilla-attention Transformer **can** win at long-term forecasting if designed properly. Two core designs:

1. **Patching**: subseries-level patches (length $P=16$, stride $S=8$) become input tokens instead of single points — retaining local semantic information and quadratically reducing attention compute ($N \approx L/S$ tokens):
$$N = \left\lfloor \frac{L-P}{S} \right\rfloor + 2, \qquad x_d^{(i)} = W_p x_p^{(i)} + W_{pos}$$
2. **Channel-independence (CI)**: each univariate channel is processed separately through shared embedding + Transformer weights.

Standard multi-head scaled dot-product attention per channel; encoder uses BatchNorm (superior to LayerNorm for TS Transformers); instance normalization ([[RevIN]]-style) normalizes each window before patching and adds statistics back. Variants: PatchTST/42 ($L=336$) and PatchTST/64 ($L=512$). Also demonstrates strong masked self-supervised pretraining (40% patches masked) and cross-dataset transfer learning.

MSE loss: $\mathcal{L} = \mathbb{E}_x \frac{1}{M}\sum_{i=1}^{M} \left\| \hat{x}_{L+1:L+T}^{(i)} - x_{L+1:L+T}^{(i)} \right\|_2^2$

## Typical Usage in EV Load Forecasting
- **Input**: long look-back windows (up to $L=512$) of multivariate load series, treated channel-wise.
- **Forecasting Horizon**: [[Long_Term]] ($T \in \{96,...,720\}$).
- **Strengths**: overall −21.0% MSE / −16.7% MAE vs best Transformer baselines; ×19–22 patching speedups at $L=336$; benefits monotonically from longer look-backs (unlike prior Transformers).
- **Weaknesses**: channel-independence ignores explicit cross-channel correlations (GNN extension suggested); point forecasts only (no uncertainty); memory-heavy for very long inputs (OOMs ≥ L=1440).

## Literature Usage
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — Original paper: patching + CI + RevIN-style normalization; Electricity T=96 MSE 0.129 vs DLinear 0.140; self-supervised fine-tuning further improves to 0.126.
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — The linear-model critique PatchTST directly answers and whose numbers it supplies/beats.
- [[2024_Das_TiDE_Long_Term_Forecasting]] — Strongest baseline: TiDE is >10× faster in training / 5× faster inference; PatchTST OOMs at L≥1440; PatchTST still wins Weather 96–336 and M5-without-covariates comparisons differ.
- [[2024_Ke_Divide_Conquer_Transformer_EV]] — DCT-EV home-charging Transformer inspired by PatchTST's sub-sequence "patch" partitioning idea.
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Prior SOTA baseline framed as "extreme patching"; iTransformer beats PatchTST on ECL (0.178 vs 0.205 avg MSE), Traffic, Solar; PatchTST fails on fluctuating PEMS.
- [[2025_Bao_ResMMoT_Informer_Time_Series]] — PatchTST baseline on NASDAQ100 beaten by ResMMoT-Informer (~30–40%); noted as weak at long-term dependencies.
- [[2025_Meyer_Benchmark_Foundation_Models]] — Best trained-from-scratch baseline for household STLF (MAE_h 0.494–0.535); ranks best at input size 24 but overtaken by foundation models at 96/168.
