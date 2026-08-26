---
type: model
name: Multi-scale Fusion Transformer (MFT)
category: Deep Learning / Multi-Scale Cross-Attention Transformer
tags:
  - model
  - mft
  - scale-masking
  - cross-attention
  - long-horizon-forecasting
---

# 🧠 Multi-scale Fusion Transformer (MFT)

## Overview
MFT combines a **Multi-scale Modeling Mechanism (3M)** (using scale masks $m_n^{a,b}$ to constrain attention heads), a **Feature-correlation Analysis Module (FAM)** (Pearson correlation prior weights), and a **Multi-variable Fusion Module (MFM)** (cross-attention sample-level dynamic reweighting) for long-horizon load prediction (up to 96h).

## Key Mathematical Equations
- **Scale Masked Attention**:
  $$m_n^{a,b} = \begin{cases} 0 & \frac{a-b}{n} \in \mathbb{Z} \\ -\infty & \text{otherwise} \end{cases}, \quad r_n = \text{softmax}\left(\frac{\alpha_n + m_n}{\sqrt{d_k^n}}\right) v_n$$
- **Dynamic Weight Cross-Attention**:
  $$\tilde{w}_i = w_i + \text{softmax}(l_Q x_{ki}^T), \quad E = \text{LeakyReLU}\left(\sum \tilde{w}_i x_{vi}\right)$$

## Literature References
- [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] - Proposed MFT achieving up to 25.59% performance boost over standard Transformers on 96-hour prediction tasks.
