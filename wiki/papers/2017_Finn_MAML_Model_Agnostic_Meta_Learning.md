---
type: paper
title: "Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks"
authors: [Chelsea Finn, Pieter Abbeel, Sergey Levine]
year: 2017
journal_conference: "Proceedings of the 34th International Conference on Machine Learning (ICML 2017), Sydney, PMLR 70"
doi_url: "https://arxiv.org/abs/1703.03400"
models_used: ["[[MAML]]", "[[First_Order_MAML|FOMAML]]", "[[Fully_Connected_Network]]", "[[Convolutional_Network]]", "[[TRPO]]", "[[REINFORCE]]"]
datasets_used: ["[[Sinusoid_Regression]]", "[[Omniglot]]", "[[miniImageNet]]", "[[rllab_2D_Navigation]]", "[[MuJoCo_Half_Cheetah]]", "[[MuJoCo_Ant]]"]
features_used: ["[[Task_Distribution]]", "[[K_Shot_Support_Set]]", "[[Meta_Gradient]]", "[[Hessian_Vector_Products]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[Accuracy]]", "[[MSE]]", "[[Average_Return]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks

## 🎯 Main Objective & Contribution
- Proposes **MAML**, a model- and task-agnostic meta-learning algorithm that trains an initialization $\theta$ such that **one or a few gradient steps on a new task's data yields maximal generalization** — in effect "training the model to be easy to fine-tune."
- Unlike prior meta-learners (learned update rules, recurrent [[MANN]], Siamese/matching/metric networks), MAML adds **no extra learned parameters** and imposes **no architectural constraints**: works with fully connected, convolutional, or recurrent networks and any differentiable loss, including non-differentiable RL objectives.
- Interpretable two ways: (a) feature learning — building a representation broadly suitable for many tasks so light fine-tuning suffices; (b) dynamical systems — explicitly maximizing the sensitivity of new-task losses to the parameters.
- State-of-the-art on few-shot image classification benchmarks, strong few-shot regression, and accelerated policy-gradient RL adaptation; foundational for transfer/meta-learning approaches to EV charging station forecasting with scarce data.

## 🧠 Methodology & Model Architecture
**Meta-learning problem setup.** A task is
$$\mathcal{T} = \{\mathcal{L}(x_1,a_1,\dots,x_H,a_H),\ q(x_1),\ q(x_{t+1}\mid x_t,a_t),\ H\}$$
with loss $\mathcal{L}$, initial-observation distribution $q(x_1)$, transition distribution $q(x_{t+1}|x_t,a_t)$, episode length $H$ ($H=1$ for i.i.d. supervised). Model $f_\theta$ adapts to tasks drawn from $p(\mathcal{T})$ using $K$ samples ($K$-shot).

**Inner loop — task-specific gradient step (adapted parameters):**
$$\theta'_i = \theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}_i}(f_\theta)$$
where step size $\alpha$ may be fixed or meta-learned; multiple updates are a straightforward extension.

**Meta-objective** — minimize post-update loss across the task distribution:
$$\min_\theta \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i}\big(f_{\theta'_i}\big) = \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i}\big(f_{\theta - \alpha\nabla_\theta \mathcal{L}_{\mathcal{T}_i}(f_\theta)}\big)$$

**Outer loop — SGD meta-update (Equation 1):**
$$\theta \leftarrow \theta - \beta \nabla_\theta \sum_{\mathcal{T}_i \sim p(\mathcal{T})} \mathcal{L}_{\mathcal{T}_i}(f_{\theta'_i})$$
The meta-gradient requires a gradient through a gradient (Hessian-vector products via an extra backward pass, supported by TensorFlow); dropping this gives the first-order approximation ([[First_Order_MAML|FOMAML]]) that still evaluates gradients at post-update parameters $\theta'_i$, yielding ≈33% speed-up with nearly identical accuracy.

**Supervised losses.** MSE for K-shot regression (Equation 2):
$$\mathcal{L}_{\mathcal{T}_i}(f_\phi) = \sum_{x^{(j)}, y^{(j)} \sim \mathcal{T}_i} \| f_\phi(x^{(j)}) - y^{(j)} \|_2^2$$
Cross-entropy for classification (Equation 3):
$$\mathcal{L}_{\mathcal{T}_i}(f_\phi) = \sum_{x^{(j)}, y^{(j)} \sim \mathcal{T}_i} y^{(j)} \log f_\phi(x^{(j)}) + (1 - y^{(j)}) \log(1 - f_\phi(x^{(j)}))$$

**Reinforcement learning loss (Equation 4)** — negative expected reward under policy $f_\phi$:
$$\mathcal{L}_{\mathcal{T}_i}(f_\phi) = -\,\mathbb{E}_{x_t, a_t \sim f_\phi, q_{\mathcal{T}_i}}\left[\sum_{t=1}^{H} R_i(x_t, a_t)\right]$$
Policy gradients ([[REINFORCE]]) estimate both inner and outer gradients; [[TRPO]] serves as meta-optimizer with finite-difference Hessian-vector products to avoid third derivatives.

**Architectures used:** sinusoid regressor = 2 hidden layers × 40 ReLU units; classifier = 4 conv modules (3×3, 64 filters, BN, ReLU, 2×2 max-pool; 32 filters on miniImageNet; strided convs on Omniglot) plus a non-conv 4-hidden-layer net (256-128-64-64); RL policy = 2 hidden layers × 100 ReLU units.

## 📊 Dataset & Input Features
- **Sinusoid regression (synthetic)**: continuous $p(\mathcal{T})$ with amplitude ∈ [0.1, 5.0], phase ∈ [0, π]; inputs $x \sim U[-5, 5]$, 1-D input/output; $K=10$ shots, single update at $\alpha = 0.01$, [[Adam]] as meta-optimizer.
- **[[Omniglot]]**: 20 instances of 1,623 characters across 50 alphabets (each instance drawn by a different person); 1,200 training characters, rest for testing; augmented with 90° rotations; images downsampled to 28×28.
- **[[miniImageNet]]** (Ravi & Larochelle split): 64 training / 12 validation / 24 test classes; N-way K-shot protocol of Vinyals et al.; 15 examples per class for the post-update meta-gradient.
- **RL domains (rllab + MuJoCo)**: 2D point-agent navigation (goals uniform in unit square, horizon $H=100$, 20 trajectories per update); half-cheetah and ant goal-velocity (goal ∈ [0, 2.0] cheetah, [0, 3.0] ant) and forward/backward direction tasks, horizon $H = 200$, 20–40 rollouts per step.
- Training: 60,000 meta-iterations on a single NVIDIA Pascal Titan X; Omniglot 5-way trained with α=0.4, meta batch 32; MiniImageNet 5 steps α=0.01, evaluated with 10 steps, meta batch 4 (1-shot) / 2 (5-shot).
- **Code availability (stated in paper)**: supervised/regression experiments at github.com/cbfinn/maml; RL experiments at github.com/cbfinn/maml_rl; learned-policy videos at sites.google.com/view/maml. Preprint: https://arxiv.org/abs/1703.03400

## 📈 Performance & Results
- **Omniglot 5-way**: 98.7 ± 0.4% (1-shot), 99.9 ± 0.1% (5-shot); 20-way: 95.8 ± 0.3% / 98.9 ± 0.2% — beats matching nets (98.1/98.9; 93.8/98.5), memory module (98.4/99.6; 95.0/98.6), Siamese nets, and non-conv MAML beats non-conv MANN (89.7 vs 82.8% 1-shot).
- **miniImageNet 5-way**: 48.70 ± 1.84% (1-shot) and 63.11 ± 0.92% (5-shot) vs matching nets 43.56/55.31, meta-learner LSTM 43.44/60.60, nearest-neighbor 41.08/51.04, fine-tuning baseline 28.86/49.79. First-order approximation essentially ties full MAML (48.07 ± 1.75% / 63.15 ± 0.91%).
- **Sinusoid regression (5-shot MSE)**: MAML 0.67 after 1 gradient step → 0.35 after 10, vs pretrain-on-all-tasks 2.41→2.19, multi-task parameter averaging 2.91→2.71 (reg-to-mean variant), showing MAML learns more than the mean optimal parameter vector; MAML infers amplitude/phase from one half of the input range and keeps improving without overfitting.
- **RL**: half-cheetah forward/backward average return −50.69 → **293.19 after one gradient step** (315.65 after 3) vs adaptable context vector stuck at −44.08; good performance within 2–3 gradient steps where pretraining is sometimes worse than random init.
- FOMAML removes second derivatives for ~33% computational speed-up.

## 💡 Limitations & Identified Research Gaps
- Meta-gradient requires differentiating through the inner gradient update (second-order information); although the first-order surrogate works surprisingly well (ReLU networks are locally almost linear), the authors leave principled analysis open — later formalized by Reptile-style methods [[2018_Nichol_Reptile_First_Order_Meta_Learning]].
- On-policy RL adaptation requires fresh trajectory samples for every additional inner-loop gradient step.
- Performance depends on the choice of task distribution $p(\mathcal{T})$; no mechanism proposed for task-distribution shift.
- Not applied to time series/load forecasting: extension to probabilistic EV charging demand forecasting (e.g., [[2023_Huang_MetaProbformer_EV_Load]], [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]], [[2024_Ali_MQ_TCN_Transfer_Learning_EV]]) is left as future work by successor literature.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{finn2017maml,
  title={Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks},
  author={Finn, Chelsea and Abbeel, Pieter and Levine, Sergey},
  booktitle={Proceedings of the 34th International Conference on Machine Learning (ICML)},
  volume={70},
  year={2017},
  organization={PMLR},
  eprint={1703.03400},
  url={https://arxiv.org/abs/1703.03400}
}
```

## 🔗 Key References & Citation Graph
- Optimizer used for supervised meta-updates: [[2014_Kingma_Adam_Stochastic_Optimization]]
- First-order follow-up: [[2018_Nichol_Reptile_First_Order_Meta_Learning]]
- Meta-learning descendants in EV forecasting vault: [[2023_Huang_MetaProbformer_EV_Load]], [[2024_Ali_MQ_TCN_Transfer_Learning_EV]], [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]]
