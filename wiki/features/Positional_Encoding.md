---
type: feature
name: "Positional Encoding"
category: Stub (auto-generated)
status: needs-review
tags:
  - feature
  - positional_encoding
---

## Overview
Injects order information into Transformer inputs via sinusoidal functions or learned embeddings, since self-attention is permutation-invariant.

$$PE_{(pos,2i)} = \sin(pos/10000^{2i/d})$$

## Usage in EV / Load Forecasting
Component of every Transformer-based forecaster ([[Informer]], [[PatchTST]], etc.); related to [[Cyclical_Encodings]] for timestamp features.
