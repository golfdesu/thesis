---
type: paper
title: "On First-Order Meta-Learning Algorithms"
authors: [Alex Nichol, Joshua Achiam, John Schulman]
year: 2018
journal_conference: "arXiv preprint (OpenAI), arXiv:1803.02999"
doi_url: "https://arxiv.org/abs/1803.02999"
models_used: ["[[Reptile]]", "[[MAML]]", "[[Reptile|FOMAML]]"]
datasets_used: ["[[Omniglot]]", "[[MiniImageNet]]", "[[Sine_Wave_Regression]]"]
features_used: ["[[Task_Sampling]]", "[[K-Shot_N-Way_Classification]]", "[[Transduction|Transductive_Batch_Normalization]]", "[[Weight_Interpolation]]"]
forecasting_horizon: "[[MAML]]"
metrics: ["[[Accuracy]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: On First-Order Meta-Learning Algorithms

## 🎯 Main Objective & Contribution
- **Problem**: [[MAML]] requires second-order derivatives (Hessian-vector products via differentiating through the inner-loop SGD) for its outer-loop update — computationally expensive and memory-heavy, and unsuited to problems needing many inner gradient steps.
- **Contributions**:
  1. Shows **first-order MAML (FOMAML)** is far simpler to implement than widely recognized (treat inner-loop gradients as constants → outer gradient is just $g_{\text{FOMAML}} = L'_{\tau,B}(\tilde{\phi})$).
  2. Introduces **[[Reptile]]**, a new first-order algorithm closely related to FOMAML and to joint training / fast-weights-slow-weights: repeatedly sample a task, train on it for $k$ steps, move the initialization toward the task-trained weights. Unlike FOMAML it needs no train/test split per task.
  3. Provides theoretical analysis (Taylor expansion + solution-manifold argument) showing FOMAML and Reptile both optimize **within-task generalization**.
  4. Empirically matches MAML on [[Omniglot]] and [[MiniImageNet]] few-shot classification benchmarks.

## 🧠 Methodology & Model Architecture
- **Meta-learning an initialization** ([[MAML]] objective): find initial parameters $\phi$ minimizing expected loss after $k$ inner updates:
$$\min_{\phi}\ \mathbb{E}_{\tau}\left[\mathcal{L}_{\tau}\left(U^k_{\tau}(\phi)\right)\right] \tag{MAML objective}$$
- **MAML with train/test split** within each task (training samples $A$, test samples $B$, akin to cross-validation):
$$\min_{\phi}\ \mathbb{E}_{\tau}\left[\mathcal{L}_{\tau,B}\left(U_{\tau,A}(\phi)\right)\right] \tag{2}$$
with meta-gradient $g_{\text{MAML}} = \frac{\partial}{\partial \phi}\mathcal{L}_{\tau,B}(U_{\tau,A}(\phi)) = U'_{\tau,A}(\phi)\,\mathcal{L}'_{\tau,B}(\tilde{\phi})$, where $\tilde{\phi} = U_{\tau,A}(\phi)$ (Eqs. 3–4). FOMAML drops the Jacobian: $g_{\text{FOMAML}} = \mathcal{L}'_{\tau,B}(\tilde{\phi})$.
- **Reptile update rule** (serial version): sample task $\tau$; compute $\tilde{\phi} = U^k_{\tau}(\phi)$ ($k$ steps of [[Adam]] or SGD); then interpolate:
$$\phi \leftarrow \phi + \epsilon(\tilde{\phi} - \phi) \tag{Reptile update}$$
Optionally treat $(\phi - \tilde{\phi})/\alpha$ as a Reptile gradient and feed it to an adaptive optimizer.
- **Batched Reptile** over $n$ tasks per iteration:
$$\phi \leftarrow \phi + \epsilon\,\frac{1}{n}\sum_{i=1}^{n}(\tilde{\phi}_i - \phi) \tag{5}$$
identical to [[SimuParallelSGD]] except for stepsize/task sampling.
- **Connection to joint training**: for $k=1$ the Reptile gradient reduces to the expected-loss gradient,
$$g_{\text{Reptile},k=1} = \mathbb{E}_{\tau}[\phi - U_{\tau}(\phi)]/\alpha = \mathbb{E}_{\tau}[\nabla_{\phi}\mathcal{L}_{\tau}(\phi)] \tag{6–7}$$
but for $k>1$ second-and-higher derivative terms appear that differ from joint training.
- **Why it works (Taylor analysis)**: with definitions $g_i = \mathcal{L}'_i(\phi_i)$, $\phi_{i+1} = \phi_i - \alpha g_i$, Hessian $H_i = \mathcal{L}''_i(\phi_1)$, gradients expand to
$$g_i = g_i - \alpha H_i \sum_{j=1}^{i-1} g_j + O(\alpha^2) \tag{13–16}$$
and the MAML meta-gradient becomes
$$g_{\text{MAML}} = \left(\prod_{j=1}^{k-1}(I - \alpha L''_j(\phi_j))\right) g_k,\qquad g_{\text{MAML}} = g_k - \alpha \sum_{j=1}^{k-1} H_j g_k - \alpha H_k \sum_{j=1}^{k-1} g_j + O(\alpha^2) \tag{17–24}$$
For $k=2$: $g_{\text{MAML}} = g_2 - \alpha H_2 g_1 - \alpha H_1 g_2$, $g_{\text{FOMAML}} = g_2 - \alpha H_2 g_1$, $g_{\text{Reptile}} = g_1 + g_2 - \alpha H_2 g_1$ (all $+O(\alpha^2)$) (Eqs. 25–27). Taking expectations over minibatches leaves two terms:
$$\text{AvgGrad} = \mathbb{E}_{\tau,1}[g_1] \tag{28}$$
$$\text{AvgGradInner} = \mathbb{E}_{\tau,1,2}[H_2 g_1] = \frac{1}{2}\,\mathbb{E}_{\tau,1,2}\left[\frac{\partial}{\partial \phi_1}(g_1 \cdot g_2)\right] \tag{29–32}$$
so $-\text{AvgGradInner}$ maximizes the inner product between gradients of different minibatches of the same task (within-task generalization):
$$\mathbb{E}[g_{\text{MAML}}] = (1)\text{AvgGrad} - (2\alpha)\text{AvgGradInner},\quad \mathbb{E}[g_{\text{FOMAML}}] = (1)\text{AvgGrad} - (\alpha)\text{AvgGradInner},\quad \mathbb{E}[g_{\text{Reptile}}] = (2)\text{AvgGrad} - (\alpha)\text{AvgGradInner} \tag{33–35}$$
General $k \ge 2$: $\mathbb{E}[g_{\text{MAML}}] = (1)\text{AvgGrad} - (2(k{-}1)\alpha)\text{AvgGradInner}$, $\mathbb{E}[g_{\text{FOMAML}}] = (1)\text{AvgGrad} - ((k{-}1)\alpha)\text{AvgGradInner}$, $\mathbb{E}[g_{\text{Reptile}}] = (k)\text{AvgGrad} - (\frac{1}{2}k(k{-}1)\alpha)\text{AvgGradInner}$ (Eqs. 36–41). Ratio MAML > FOMAML > Reptile; all scale linearly with $\alpha k$.
- **Second interpretation**: Reptile performs SGD on expected squared distance to each task's optimal solution manifold:
$$\min_{\phi}\ \mathbb{E}_{\tau}\left[\frac{1}{2}D(\phi, W_{\tau})^2\right],\qquad \nabla_{\phi}\ \mathbb{E}_{\tau}\left[\tfrac{1}{2}D(\phi,W_{\tau})^2\right] = \mathbb{E}_{\tau}\left[\phi - P_{W_{\tau}}(\phi)\right] \tag{42–44}$$
yielding update $\phi \leftarrow (1-\epsilon)\phi + \epsilon P_{W_{\tau}}(\phi)$ (Eqs. 45–47), with $P_{W_{\tau}}$ approximated by $k$ gradient steps.
- **Case study (sine regression)**: tasks $\tau=(a,b)$ with $f_\tau(x)=a\sin(x+b)$, $a\sim U([0.1,5.0])$, $b\sim U([0,2\pi])$; loss is $\ell_2$ over $[-5,5]$:
$$\mathcal{L}_{\tau}(f) = \int_{-5}^{5} dx\, \|f(x) - f_{\tau}(x)\|^2 \tag{8}$$
MLP $1\to64\to64\to1$, 10 sampled points, 32 gradient steps; joint training collapses to $f(x)=0$ while Reptile/MAML learn representations adaptable in 32 steps.
- **Implementation details**: same CNN architectures/preprocessing as Finn et al.; Adam ($\beta_1=0$ — momentum hurts, since it lets one minibatch influence subsequent steps) inner loop, vanilla SGD outer loop; Adam moment statistics backed up/reset at evaluation.

## 📊 Dataset & Input Features
- **[[Omniglot]]** [Lake et al., CogSci 2011]: 1623 handwritten characters from 50 alphabets; used for K-shot N-way classification at 5-way/20-way × 1-shot/5-shot. Tasks sample $N$ classes and $K+1$ examples each (test set = 1 example/class).
- **[[MiniImageNet]]** [Vinyals et al., Matching Networks, NeurIPS 2016]: standard few-shot benchmark, 5-way 1-shot/5-shot. No URLs/data statements in text; both are public benchmarks.
- **Features/setup**: [[K-Shot_N-Way_Classification]] episode construction, transductive vs non-transductive batch normalization (transduction shares info across test samples via BN statistics).
- Hyperparameters (App. A): Omniglot 5-way/20-way — Adam LR 0.001/0.0005, inner batch 10/20, 5/10 inner iters, outer step 1.0, 100K/200K outer iterations, meta-batch 5; Mini-ImageNet — Adam LR 0.001, inner batch 10, 8 inner iters, 15 training shots, outer step 1.0, 100K iterations, meta-batch 5.

## 📈 Performance & Results
- **Mini-ImageNet (Table 1)**:

| Algorithm | 1-shot 5-way | 5-shot 5-way |
| :--- | :---: | :---: |
| MAML + Transduction | 48.70 ± 1.84% | 63.11 ± 0.92% |
| 1st-order MAML + Transduction | 48.07 ± 1.75% | 63.15 ± 0.91% |
| Reptile | 47.07 ± 0.26% | 62.74 ± 0.37% |
| **Reptile + Transduction** | **49.97 ± 0.32%** | **65.99 ± 0.58%** |

- **Omniglot (Table 2)**: MAML+Transd. 98.7/99.9/95.8/98.9% (1-shot 5-way / 5-shot 5-way / 1-shot 20-way / 5-shot 20-way); FOMAML+Transd. 98.3/99.2/89.4/97.9%; Reptile 95.39/98.90/88.14/96.65%; Reptile+Transd. 97.68/99.48/89.43/97.12%. Reptile slightly worse than MAML on Omniglot, slightly better on Mini-ImageNet; transduction helps everywhere.
- **Gradient-combination ablation (Sec. 6.2, 5-shot 5-way Omniglot)**: using only first gradient $g_1$ (= joint training) is ineffective; two-step Reptile ($g_1+g_2$) slightly worse than two-step FOMAML ($g_2$); performance improves monotonically as more inner minibatch gradients are summed — Reptile benefits from many inner-loop steps.
- **Mini-batch overlap ablation (Sec. 6.3)**: shared-tail FOMAML degrades sharply once the final minibatch overlaps earlier ones (≥5 cycling iterations or batch size >25); separate-tail FOMAML and Reptile are insensitive to inner-loop hyperparameters.
- **Efficiency**: no second derivatives anywhere; Reptile ≈ joint training cost.

## 💡 Limitations & Identified Research Gaps
- Taylor approximation valid only for small $\alpha k$; theory informal in parts (solution-manifold argument explicitly "should be taken much less seriously").
- Negative results applying Reptile to RL so far (joint training is a strong baseline there).
- Large gap between training and testing error in few-shot classification; regularization unexplored.
- Open questions posed by authors: whether SGD's automatic generalization effect can be amplified outside meta-learning; deeper classifier architectures; few-shot density modeling.
- Thesis relevance: first-order adaptation (no Hessians) is attractive for quickly adapting EV charging forecasters to new stations/sites with scarce history — but this paper validates only on vision benchmarks, not time series.

## 📚 BibTeX & Citation Reference
```bibtex
@article{nichol2018reptile,
  title={On First-Order Meta-Learning Algorithms},
  author={Nichol, Alex and Achiam, Joshua and Schulman, John},
  journal={arXiv preprint arXiv:1803.02999},
  year={2018}
}
```

## 🔗 Key References & Citation Graph
- Extends/directly compares against [[2017_MAML_Model_Agnostic_Meta_Learning]] (MAML/FOMAML, sine-wave regression setup, Mini-ImageNet/Omniglot protocols)
- Uses [[2014_Adam_Stochastic_Optimization|Adam]] (Kingma & Ba, ICLR 2015) in the inner loop
- Builds on Matching Networks (Vinyals et al., NeurIPS 2016 — MiniImageNet) and Omniglot (Lake et al., CogSci 2011)
- Related: Learning to learn by gradient descent by gradient descent (Andrychowicz et al., NeurIPS 2016); fast weights/slow weights (Hinton & Plaut, 1987); SimuParallelSGD (Zinkevich et al., NIPS 2010); Batch Normalization (Ioffe & Szegedy, 2015)
- Vault context for EV forecasting: [[2017_Attention_Is_All_You_Need]]
