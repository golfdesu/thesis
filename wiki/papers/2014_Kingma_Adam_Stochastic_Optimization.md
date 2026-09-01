---
type: paper
title: "Adam: A Method for Stochastic Optimization"
authors: [Diederik P. Kingma, Jimmy Lei Ba]
year: 2014
journal_conference: "ICLR 2015 (arXiv:1412.6980)"
doi_url: "https://arxiv.org/abs/1412.6980"
models_used: ["[[Adam]]", "[[SGD]]", "[[AdaGrad]]", "[[RMSProp]]", "[[SFO_Optimizer]]"]
datasets_used: ["[[MNIST]]", "[[CIFAR-10]]", "[[IMDB_Movie_Reviews]]", "[[Synthetic_VAE_Objective]]"]
features_used: ["[[Adam]]", "[[Signal_to_Noise_Ratio]]", "[[Dropout_Noise]]", "[[Bag_of_Words_Features]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[NLL]]", "[[Regret_Bound]]", "[[Convergence_Iterations]]", "[[Wall_Clock_Time]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Adam: A Method for Stochastic Optimization

## 🎯 Main Objective & Contribution
- Introduces **Adam (Adaptive Moment Estimation)**, a first-order gradient-based stochastic optimization algorithm that computes **individual adaptive learning rates** from estimates of the first and second moments of the gradients.
- Combines the advantages of **[[AdaGrad]]** (works well with sparse gradients) and **[[RMSProp]]** (works well in online/non-stationary settings), adding a novel **initialization bias-correction** term.
- Key properties: parameter-update magnitudes **invariant to diagonal rescaling of gradients**; stepsizes approximately bounded by the stepsize hyperparameter α ("trust region"); no stationary objective required; handles noisy/sparse gradients; natural step-size annealing via the signal-to-noise ratio.
- Provides an $O(\sqrt{T})$ regret bound under the online convex optimization framework — comparable to the best known results — plus the **AdaMax** variant based on the infinity norm.

## 🧠 Methodology & Model Architecture
### Algorithm 1 — Adam update rules (Section 2)
- Objective: minimize $\mathbb{E}[f(\theta)]$ for stochastic differentiable $f$; gradient $\mathbf{g}_t = \nabla_\theta f_t(\theta_{t-1})$.
- **Biased First Moment Estimate (Exponential Moving Average of the Mean)**:
$$m_t = \beta_1 \cdot m_{t-1} + (1-\beta_1)\cdot g_t$$
- **Biased Second Raw Moment Estimate (EMA of Uncentered Variance)**:
$$v_t = \beta_2 \cdot v_{t-1} + (1-\beta_2)\cdot g_t^2 \qquad (g_t^2 = g_t \odot g_t)$$
- **Bias-Corrected First Moment Estimate**:
$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}$$
- **Bias-Corrected Second Raw Moment Estimate**:
$$\hat{v}_t = \frac{v_t}{1-\beta_2^t}$$
- **Parameter Update Step**:
$$\theta_t = \theta_{t-1} - \alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$
- **Default hyperparameters**: $\alpha=0.001$, $\beta_1=0.9$, $\beta_2=0.999$, $\epsilon=10^{-8}$; minibatch size 128 in all experiments.
### Step-size properties (Section 2.1)
- Effective step $\Delta_t = \alpha\cdot\hat{m}_t/\sqrt{\hat{v}_t}$ satisfies $|\Delta_t| \lesssim \alpha$ (trust-region interpretation); bounds $|\Delta_t|\le\alpha(1-\beta_1)/\sqrt{1-\beta_2}$ in extreme sparsity, else $|\Delta_t|\le\alpha$. The ratio $\hat{m}_t/\sqrt{\hat{v}_t}$ is the **signal-to-noise ratio (SNR)** → smaller SNR near optima gives automatic annealing. Gradient rescaling by $c$ cancels: $(c\,\hat m_t)/\sqrt{c^2 \hat v_t}=\hat m_t/\sqrt{\hat v_t}$.
### Initialization bias correction (Section 3)
- Expanding the EMA over all past gradients (**Second Moment as Weighted Sum**, Eqs. 1–4):
$$v_t = (1-\beta_2)\sum_{i=1}^{t}\beta_2^{\,t-i}\cdot g_i^2, \qquad \mathbb{E}[v_t] = \mathbb{E}[g_t^2]\cdot(1-\beta_2^{\,t}) + \zeta$$
with $\zeta=0$ for stationary second moments — motivating division by $(1-\beta_2^t)$; crucial precisely when small $(1-\beta_2)$ is needed for sparse gradients.
### Convergence analysis (Section 4)
- Regret definition (**Online Regret, Eq. 5**):
$$R(T) = \sum_{t=1}^{T}\left[f_t(\theta_t) - f_t(\theta_* )\right], \qquad \gamma \triangleq \frac{\beta_1^2}{\sqrt{\beta_2}}$$
- **Theorem 4.1 (Adam Regret Bound)** with bounded gradients $\|\nabla f_t(\theta)\|_2\le G$, $\|\nabla f_t(\theta)\|_\infty\le G_\infty$, bounded iterates $\|\theta_n-\theta_m\|_2\le D$, $\beta_1^2/\sqrt{\beta_2}<1$, decaying $\alpha_t=\alpha/\sqrt{t}$ and $\beta_{1,t}=\beta_1\lambda^{t-1}$:
$$R(T) \le \frac{D^2}{2\alpha(1-\beta_1)}\sum_{i=1}^{d}\sqrt{T\hat{v}_{T,i}} + \frac{\alpha(1+\beta_1)G_\infty}{(1-\beta_1)\sqrt{1-\beta_2}(1-\gamma)^2}\sum_{i=1}^{d}\|g_{1:T,i}\|_2 + \sum_{i=1}^{d}\frac{D_\infty^2 G_\infty}{2\alpha(1-\beta_1)(1-\lambda)^2\sqrt{1-\beta_2}}$$
- **Corollary 4.2 (Average Regret Convergence)**: $R(T)/T = O(1/\sqrt{T}) \to 0$. For sparse features Adam/AdaGrad achieve $O(\log d/\sqrt{T})$ vs. $O(\sqrt{dT})$ non-adaptive.
### Extensions (Section 7)
- **AdaMax ($L_\infty$ variant)**: with $v_t^{(p)} = \beta_2^p v_{t-1} + (1-\beta_2^p)|g_t|^p$ and $u_t = \lim_{p\to\infty}(v_t)^{1/p}$, one obtains the simple recursion:
$$u_t = \max(\beta_2\cdot u_{t-1}, |g_t|), \qquad \theta_t = \theta_{t-1} - \left(\frac{\alpha}{1-\beta_1^t}\right)\cdot\frac{m_t}{u_t}$$
(no bias correction needed for $u_t$; $|\Delta_t|\le\alpha$; defaults $\alpha=0.002$, $\beta_1=0.9$, $\beta_2=0.999$).
- **Temporal averaging**: Polyak–Ruppert averaging $\bar\theta_t = \frac{1}{t}\sum_k \theta_k$ or exponential moving average $\bar\theta_t = \beta_2\bar\theta_{t-1} + (1-\beta_2)\theta_t$ with bias correction $\tilde\theta_t = \bar\theta_t/(1-\beta_2^t)$.

## 📊 Dataset & Input Features
- **[[MNIST]]** — 784-dimensional image vectors; logistic regression + two-hidden-layer MLP (1000 ReLU units each), minibatch 128.
- **[[IMDB_Movie_Reviews]]** (Maas et al., 2011) — bag-of-words feature vectors over the 10,000 most frequent words (highly sparse), with 50% dropout on BoW features; logistic regression.
- **[[CIFAR-10]]** — CNN with three stages of 5×5 convolutions + 3×3 max-pooling (stride 2) + 1000-unit ReLU fully connected layer (c64-c64-c128-1000); whitened inputs; dropout on input/FC layers; 45 epochs.
- **VAE objective** (Kingma & Welling 2013) — single hidden layer, 500 units, softplus nonlinearities, 50-dim spherical Gaussian latent; used to study bias correction across hyper-parameter grids.
- Features consumed by the optimizer: raw gradients, their elementwise squares, moment EMAs; input-side features include sparse BoW vectors and dropout noise (stochastic regularization).
- Data availability: no proprietary data; all benchmarks public. Links found in text: `arXiv:1412.6980v9 [cs.LG]` (`https://arxiv.org/abs/1412.6980`); related preprints cited: `arXiv:1308.0850`, `arXiv:1207.0580`, `arXiv:1301.3584`, `arXiv:1212.5701`, `arXiv:1206.1106`. Compute partly on Dutch national e-infrastructure (SURF Foundation).

## 📈 Performance & Results
- **Logistic regression (MNIST)**: Adam converges similarly to SGD with Nesterov momentum, both faster than AdaGrad. On sparse IMDB BoW features, Adam converges **as fast as AdaGrad** and far faster than SGDNesterov (consistent with the $O(\log d/\sqrt T)$ sparse-feature theory).
- **Multi-layer NNs (MNIST)**: vs. quasi-Newton SFO, Adam makes faster progress per iteration AND wall-clock time; SFO is **5–10× slower per iteration** (curvature updates) with memory linear in #minibatches; SFO fails to converge entirely with dropout noise, while Adam shows best convergence among AdaGrad/RMSProp/SGDNesterov/AdaDelta.
- **CNNs (CIFAR-10)**: rapid early progress; Adam and SGD eventually converge considerably faster than AdaGrad; second-moment estimate $\hat v_t$ vanishes toward zero after a few epochs (dominated by ε) so CNN speedup comes mainly from first-moment minibatch-variance reduction; Adam adapts per-layer learning-rate scale automatically vs. hand-tuned SGD; marginal improvement over SGDNesterov overall.
- **Bias-correction ablation (VAE)**: without bias correction (= momentum-RMSProp), β₂ close to 1 causes instabilities especially in early epochs and late training when gradients grow sparse; with bias correction, small $(1-\beta_2)$ values perform best; Adam ≥ RMSProp across ALL tested hyper-parameter settings.
- Theory confirmed empirically: convex-case convergence matches predictions; robustness to hyperparameters (little tuning needed).

## 💡 Limitations & Identified Research Gaps
- Theoretical regret guarantee applies only to **convex** objectives; deep-learning experiments are non-convex and purely empirical.
- In CNNs the second-moment estimate becomes a poor approximation of cost-function geometry (collapses to ε-dominated values) — adaptive geometry less effective for weight-shared architectures.
- Adam requires learning-rate decay schedules ($\alpha/\sqrt t$) and exponentially decayed β₁ₜ for the strongest theoretical guarantees — practical training usually omits these; decaying β₁ₜ toward zero is noted as important (matches Sutskever et al. momentum-reduction findings).
- Memory overhead: stores two moment vectors per parameter (vs. one for plain SGD) — relevant for memory-constrained GPU settings (contrast SFO's linear-in-minibatches memory).
- Later research gaps (not in paper): generalization gap vs. SGD on image tasks, AdamW-style decoupled weight decay, and warm-up schedules — all post-hoc fixes beyond this paper's scope.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{kingma2014adam,
  title     = {Adam: A Method for Stochastic Optimization},
  author    = {Kingma, Diederik P. and Ba, Jimmy Lei},
  booktitle = {Proceedings of the 3rd International Conference on Learning Representations (ICLR)},
  year      = {2015},
  eprint    = {1412.6980},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1412.6980}
}
```

## 🔗 Key References & Citation Graph
- Duchi, Hazan & Singer (2011) — [[AdaGrad]], sparse-gradient precursor; Adam reduces to AdaGrad as $\beta_1\to0$, $(1-\beta_2)\to0$, annealed α
- Tieleman & Hinton (2012) Coursera Lecture 6.5 — [[RMSProp]]; Adam without bias correction ≈ momentum-RMSProp
- Zeiler (2012) AdaDelta; Schaul et al. (2012) vSGD; Sohl-Dickstein et al. (2014) SFO — curvature-from-first-order competitors
- Zinkevich (2003) — online convex programming framework used for the regret analysis
- Kingma & Welling (2013) Auto-Encoding Variational Bayes — VAE testbed for bias-correction experiments
- Graves (2013) sequence generation with RNNs — momentum-RMSProp usage precedent
- Vault context:
  - [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM architectures routinely trained with Adam in EV forecasting pipelines
  - [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] and [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — Transformer/LTSF models optimized with Adam
  - [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — efficient Transformers trained using Adam-family optimizers
  - [[2024_Das_TiDE_Long_Term_Forecasting]] — encoder-decoder MLP forecaster relying on Adam-style training

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2014_Kingma_Adam_Stochastic_Optimization_refs]]
