---
type: hyperparameter
name: Metaheuristic Optimization
category: Nature-Inspired Heuristic Optimization Algorithms
tags:
  - hyperparameter
  - metaheuristic
  - bwo
  - swarm-intelligence
---

# ⚙️ Metaheuristic Optimization Algorithms

## Overview
Metaheuristic optimization methods simulate biological or swarm behaviors (e.g., Beluga Whale Optimization - BWO, Particle Swarm Optimization - PSO, Genetic Algorithms - GA) to globalize hyperparameter search and avoid falling into local minima in non-convex loss landscapes.

## Key Features
- **Exploration & Exploitation**: Alternates between global exploration phase and localized exploitation phase.
- **Decomposition Coupling**: Often coupled with signal decomposition algorithms (e.g., ICEEMDAN, VMD) to optimize feature extraction parameters simultaneously with neural network weights.

## Papers Utilizing Metaheuristic Optimization
- [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] - Utilizes Beluga Whale Optimization (BWO) to joint-tune ICEEMDAN signal decomposition parameters and iTransformer architecture hyperparameters.
