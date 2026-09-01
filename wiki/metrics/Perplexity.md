---
type: metric
name: "Perplexity"
category: language-model-metric
formula: "PPL = exp(−(1/N) Σ log p(x_i | context))"
unit: Dimensionless (effective vocabulary branching factor)
last_updated: 2026-08-26
tags:
  - metric
  - perplexity
  - language-modeling
---

# Perplexity

## Definition

**Perplexity** is the exponentiated average negative log-likelihood per token — the standard intrinsic metric for language models:

$$\text{PPL} = \exp\left(-\frac{1}{N}\sum_{i=1}^{N} \log p(x_i \mid x_{<i})\right)$$

Equivalently, the inverse geometric mean probability assigned to each token. PPL equals $\exp(\mathrm{NLL}/N)$ when [[NLL]] is the total natural-log loss; lower is better. A model with perplexity $k$ is roughly as uncertain as choosing uniformly among $k$ options at each step.

| Property | Description |
|----------|-------------|
| **Lower is better** | ✅ Yes |
| **Depends on tokenizer/vocabulary** | ⚠️ Only comparable across models using identical tokenization and data |

## Referenced in this knowledge base

[[2017_Attention_Is_All_You_Need]], [[2018_Bai_Empirical_TCN_Sequence_Modeling]], [[2026_Lahoti_Mamba_3_Sequence_Modeling]]
