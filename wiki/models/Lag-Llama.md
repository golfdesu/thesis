---
type: model
name: "Lag-Llama"
category: model
tags: [model, lag-llama]
---

# Lag-Llama

## Overview

Probabilistic time series foundation model with lag features (Rasul et al. 2023).

## Literature Usage

- [[2026_Moirai_2_When_Less_Is_More]] — Compared among 30 GIFT-Eval baselines (Fig. 2 normalized MASE/CRPS); trails Moirai 2.0 (cf. §5.1 GIFT-Eval list).
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
