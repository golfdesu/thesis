---
type: model
name: Q-Learning Reinforcement Learning
category: Machine Learning / Reinforcement Learning
tags:
  - model
  - reinforcement-learning
  - q-learning
  - model-free
---

# 🧠 Q-Learning Reinforcement Learning

## Overview
Q-Learning is a model-free, off-policy Reinforcement Learning algorithm that learns an optimal action-value function $Q(s, a)$ to select actions maximizing cumulative future rewards in a Markov Decision Process (MDP).

## Key Mathematical Equations
- **Q-Table Value Update**:
  $$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_t + \lambda \max_a Q(s_{t+1}, a) - Q(s_t, a_t) \right]$$
- **Exponential Error Reward Function** (for Load Forecasting):
  $$r_t = \frac{1}{\exp\left| P_{\text{actual}} - \lambda_i P_{\text{model}} \right|}$$

## Application in EV Charging Load Forecasting
- Serves as a dynamic meta-selector that switches hourly between candidate predictions (e.g. ANN vs RNN) based on real-time forecasting error.
- Reduced MSE by over 35% in smart charging scenarios with volatile load profiles ([[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]]).

## Literature References
- [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] - Applied Q-learning for ensemble selection in uncoordinated, coordinated, and smart EV charging.
