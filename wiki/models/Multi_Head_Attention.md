---
type: model
name: "Multi-Head Attention"
category: Stub (auto-generated)
status: needs-review
tags:
  - model
  - multi-head-attention
---

## Overview
Core mechanism of the Transformer: several scaled dot-product attention heads run in parallel, each attending to different representation subspaces.

$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

## Key References
- [[2017_Attention_Is_All_You_Need]]
