---
type: metric
name: "msMAPE"
category: evaluation-metric
tags:
  - metric
---

# msMAPE (mean symmetric MAPE)

## Definition
$$\text{msMAPE} = \frac{1}{H}\sum_{i=1}^{H} \frac{2|y_{L+i} - \hat{y}_{L+i}|}{\max\{|y_{L+i}| + |\hat{y}_{L+i}| + \epsilon,\, 0.5 + \epsilon\}}, \quad \epsilon=0.1$$

Monash official metric (Eq. 7 in [[2024_TimesFM_Decoder_Only_Foundation_Model]]); avoids MAPE undefined-at-zero via symmetric denominator.

## Literature Usage
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Defines Eq. 7 and uses naive-scaled averaging (like MAE) across Monash datasets.
