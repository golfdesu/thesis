---
type: feature
name: "Time Encoding"
category: feature
tags: [feature, positional-encoding, time-feature]
---

# Time Encoding

## Overview
Temporal positional encodings that inject calendar and clock information (time-of-day, day-of-week, month, elapsed time) into sequence models so they can distinguish absolute and relative temporal positions.

## Literature Usage
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Continuous positional encoding $\gamma(\mathcal{T})$ used to align irregular timestamps.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — MOIRAI uses Rotary Position Embeddings (RoPE, $R_{i-j}$) for relative time encoding within Any-variate Attention alongside binary variate biases ($u^{(1)}, u^{(2)}$), plus frequency-conditioned patch projections; see Eq. 2–3.
