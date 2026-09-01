---
type: metric
name: "BLEU (Bilingual Evaluation Understudy)"
category: language-model-metric
formula: "BLEU = BP · exp(Σ_{n=1..N} w_n · log p_n)"
unit: Dimensionless, 0–1 (often ×100)
last_updated: 2026-08-26
tags:
  - metric
  - bleu
  - generation-quality
---

# BLEU

## Definition

**BLEU** scores generated text by the brevity-penalized geometric mean of modified n-gram precisions (typically n = 1…4, uniform weights $w_n = 1/4$):

$$\text{BLEU} = \underbrace{\min\!\left(1,\ e^{\,1 - r/c}\right)}_{\text{brevity penalty}} \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)$$

where $p_n$ is the modified (clipped) precision of n-grams against a reference corpus, $c$ the candidate length and $r$ the reference length. Higher is better; 1.0 = perfect n-gram overlap. Used in [[2017_Attention_Is_All_You_Need]] for machine translation quality.

| Property | Description |
|----------|-------------|
| **Higher is better** | ✅ Yes (0–1) |
| **Corpus-level metric** | Sentence-level BLEU is unreliable |
| **Caveats** | Ignores synonyms/paraphrase; correlated only moderately with human judgment |

## Referenced in this knowledge base

[[2017_Attention_Is_All_You_Need]]
