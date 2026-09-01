---
type: metric
name: "MSIS"
category: metric
tags: [metric, probabilistic, interval-score]
---

# MSIS (Mean Scaled Interval Score)

## Overview
Metric evaluating uncertainty and sharpness of prediction intervals, popularized in the M4 Competition (Makridakis et al., 2020). For a $(1-\alpha)$ prediction interval $[L_t, U_t]$ and ground truth $Y_t$:

$$\text{MSIS} = \frac{\frac{1}{h} \sum_{t=1}^h \left( (U_t - L_t) + \frac{2}{\alpha}(L_t - Y_t)\mathbf{1}_{\{Y_t < L_t\}} + \frac{2}{\alpha}(Y_t - U_t)\mathbf{1}_{\{Y_t > U_t\}} \right)}{\frac{1}{n-m} \sum_{t=m+1}^n |Y_t - Y_{t-m}|}$$

## Literature Usage
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — Evaluated zero-shot out-of-distribution across 6 benchmark datasets (Electricity, Solar, Walmart, Weather, Istanbul Traffic, Turkey Power) at $\alpha=0.05$ (Table 5).
