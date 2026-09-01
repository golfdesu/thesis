---
type: model
name: KAN (Kolmogorov-Arnold Network)
category: Deep Learning / Learnable Spline-Edge Function Approximator
tags:
  - model
  - deep-learning
  - kan
  - interpretable-ml
  - function-approximation
---

# 🧩 KAN — Kolmogorov-Arnold Networks

## Overview
KANs (Liu et al., 2024; ICLR 2025) are alternatives to [[MLP]]: while MLPs have **fixed activations on nodes** ("neurons") and learnable weights on edges, KANs have **learnable activation functions on edges** ("weights") — every linear weight is replaced by a univariate function parametrized as a B-spline. Grounded in the Kolmogorov-Arnold representation theorem, generalized to arbitrary widths/depths and trainable with backpropagation.

- **Kolmogorov-Arnold theorem (Eq. 2.1)** — for smooth $f:[0,1]^n\to\mathbb{R}$:
$$f(\mathbf{x}) = \sum_{q=1}^{2n+1} \Phi_q \left( \sum_{p=1}^{n} \phi_{q,p}(x_p) \right)$$
("the only true multivariate function is addition").
- **KAN layer / network (Eqs. 2.5–2.7)**:
$$x_{l+1,j} = \sum_{i=1}^{n_l} \phi_{l,j,i}(x_{l,i}), \qquad \mathrm{KAN}(\mathbf{x}) = (\Phi_{L-1} \circ \cdots \circ \Phi_0)\,\mathbf{x}$$
- **Learnable edge activation (Eq. 2.10)** — residual form of basis + spline:
$$\phi(x) = w_b\,\mathrm{silu}(x) + w_s \sum_i c_i B_i(x),$$
with trainable B-spline coefficients $c_i$ and grids refreshed on the fly to input activation ranges.
- **Approximation theory (Theorem 2.1)** — residue rate $\le C\,G^{-k-1+m}$ **independent of dimension** → beats the curse of dimensionality ($\alpha = k+1 = 4$ for cubic splines vs MLPs' $\alpha=(k+1)/d$); empirically test RMSE $\propto N^{-4}$ on all five toy tasks.
- **Grid extension (Eq. 2.16)** — refine coarse spline grids to finer ones via least-squares coefficient refitting (staircase-like training-loss drops), improving accuracy without retraining from scratch.
- **Interpretability pipeline**: sparsification (L1 + entropy regularization), pruning (node importance thresholds), symbolification (`fix_symbolic` fits $y \approx c\,f(ax+b)+d$) — e.g., recovers $f(x,y)=e^{\sin(\pi x)+y^2}$ to machine precision.

## Typical Usage in EV Load Forecasting
- **Input**: exogenous drivers (temperature, price, calendar effects) mapped onto load via spline edges.
- **Forecasting Horizon**: [[Short_Term_Forecasting]] as decoder stage inside hybrid sequence models.
- **Strengths**: Pareto-dominates MLPs on smooth special functions (ellipj RMSE $1.33\times10^{-4}$ vs $6.48\times10^{-4}$); 100× more accurate Poisson solving with 100× fewer parameters than MLP-PINN; interpretable symbolic extraction; locality of B-splines avoids catastrophic forgetting.
- **Weaknesses**: ~10× slower training than equal-parameter MLPs (no batch computation across distinct activations); demonstrated only on small-scale AI+Science tasks; deep-KAN theory incomplete — motivates hybrid architectures pairing KAN decoders with efficient sequence backbones rather than pure-KAN stacks.

## Literature Usage
- [[2024_KAN_Kolmogorov_Arnold_Networks]] — Foundation paper: KA-theorem generalization, dimension-independent scaling laws, grid extension, knot-signature classification at 81.6% accuracy with ≈200 params vs DeepMind MLP's 78.0% with ~$3\times10^5$ params.
- [[2026_Mamba_KAN_HyKANet_EV]] — HyKANet adopts a Kolmogorov-Arnold **decoder** for station-level EV charging demand atop Mamba branches: the learnable spline edges are precisely the mechanism for accurate, interpretable nonlinear mapping of exogenous drivers onto charging load; best avg RMSE 4.67 (×10²) vs PAG 5.48 (−14.8%).
- 2025 — [[2025_MixerInformer_Transfer_Learning_New_EV_Stations]] — KAN as the final nonlinear-refinement module in MIK-TST (Mixer→Informer→KAN): learnable B-spline edge activations $f_{ij}(x_i)=\sum c_k b_k(x_i)$ capture station-specific traits during fine-tuning; removing KAN costs +1.3% MAE (0.4450→0.4508) on Boulder 26-station transfer, while layer-freezing (tuning only KAN) is the recommended scarce-data strategy.
