---
type: model
name: Multi-Quantile Temporal Convolutional Network (MQ-TCN)
category: Deep Learning / Quantile Regression TCN
tags:
  - model
  - mq-tcn
  - tcn
  - quantile-regression
  - transfer-learning
---

# 🧠 Multi-Quantile Temporal Convolutional Network (MQ-TCN)

## Overview
MQ-TCN combines dilated causal convolutions from **Temporal Convolutional Networks (TCN)** with multiple fully connected quantile regression heads trained via **Pinball Loss**.

## Key Mathematical Equations
- **Dilated Causal Convolution**:
  $$G(s) = \sum_{i=0}^{k-1} f_{\text{filter}}(i) \cdot x_{s - d_l \cdot i}$$
- **Pinball Loss Function for Quantile $q$**:
  $$L_{\text{PB}}(q, y, \hat{y}^q) = \begin{cases} q(y - \hat{y}^q) & \hat{y}^q \le y \\ (1-q)(\hat{y}^q - y) & \hat{y}^q > y \end{cases}$$

## Literature References
- [[2024_MQ_TCN_Transfer_Learning_EV]] - Proposed MQ-TCN with inductive transfer learning for data-scarce EV charging sites.
