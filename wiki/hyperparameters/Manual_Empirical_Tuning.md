---
type: hyperparameter
name: Manual & Empirical Search
category: Heuristic Standard Default Configurations
tags:
  - hyperparameter
  - manual-tuning
  - standard-defaults
---

# ⚙️ Manual & Empirical Search Tuning

## Overview
Manual and empirical hyperparameter tuning relies on domain expertise, published standard baseline defaults (e.g., Adam default $\beta_1=0.9, \beta_2=0.999, \text{lr}=10^{-3}$), and trial-and-error validation iterations to select architecture settings.

## Common Empirical Default Settings
- **Adam Optimizer**: $\eta = 10^{-3}$, $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$.
- **Transformer Encoders**: $d_{\text{model}} \in \{128, 256, 512\}$, $N_{\text{heads}} \in \{4, 8\}$, dropout $= 0.1$.
- **Sequence Windows**: Look-back window $L \in \{96, 168, 336, 720\}$ steps.

## Papers Utilizing Manual & Empirical Tuning
- [[2017_Attention_Is_All_You_Need]] - Empirical selection of Transformer base/large configurations.
- [[2021_Informer_Beyond_Efficient_Transformer]] - Empirical selection of ProbSparse self-attention sampling factor $c=5$.
- [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] - Auto-Correlation factor $k=6$ and series decomposition moving average kernel size $=25$.
- [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] - Patch length $P=16$ and stride $S=8$.
- [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] - Inverted dimension tokenization empirical defaults.
