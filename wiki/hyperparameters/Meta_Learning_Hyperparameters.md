---
type: hyperparameter
name: Meta-Learning & Few-Shot Hyperparameter Adaptation
category: Meta-Learning / Fast Adaptation Framework
tags:
  - hyperparameter
  - meta-learning
  - maml
  - reptile
  - few-shot
---

# ⚙️ Meta-Learning & Few-Shot Hyperparameter Adaptation

## Overview
Meta-learning ("learning to learn") optimizes initial model parameter initialization $\theta$ across a distribution of tasks (e.g., multiple EV charging stations or regions), enabling rapid adaptation to a new target station with minimal gradient update steps ($k$-shot learning) and hyperparameter tuning.

## Meta-Optimization Strategies
- **MAML (Model-Agnostic Meta-Learning)**: Optimizes initial parameters using inner-loop gradient steps and outer-loop meta-updates.
- **Reptile**: First-order meta-learning algorithm computing task updates without second-order derivatives.
- **Stacked Meta-Learning**: Ensembles hierarchical base models and metalearners.

## Papers Utilizing Meta-Learning Hyperparameter Adaptation
- [[2023_Huang_MetaProbformer_EV_Load]] - Combines Reptile meta-learning with Informer Transformer for few-shot probabilistic load forecasting at newly deployed charging stations.
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] - Employs stacked meta-learning for fast parameter adaptation across short-term EV load series.
- [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]] - Foundational MAML meta-learning algorithm.
- [[2018_Nichol_Reptile_First_Order_Meta_Learning]] - Foundational Reptile first-order meta-learning algorithm.
