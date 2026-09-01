---
type: model
name: "FEDformer"
category: Stub (auto-generated)
status: needs-review
tags:
  - model
  - fedformer
---

## Overview
Frequency Enhanced Decomposed Transformer; combines seasonal-trend decomposition with attention in the frequency domain via Fourier transforms.

## Role in EV / Load Forecasting
Long-term forecasting benchmark model compared alongside [[Informer]], [[Autoformer]], and [[PatchTST]].

## Literature Usage

- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
