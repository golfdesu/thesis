---
type: paper
title: "Gaussian processes for time-series modelling"
authors: [Stephen Roberts, Michael Osborne, Mark Ebden, Steven Reece, Niall Gibson, Suzanne Aigrain]
year: 2013
journal_conference: "Philosophical Transactions of the Royal Society A, 371, 20110550"
doi_url: "https://doi.org/10.1098/rsta.2011.0550"
models_used: ["[[Gaussian_Process]]", "[[Bayesian_Nonparametric_Regression]]", "[[Kalman_Filter]]", "[[Bayesian_Quadrature]]", "[[Markov_Chain_Monte_Carlo]]"]
datasets_used: ["[[Bramblemet_Sensor_Network]]", "[[Nile_River_Water_Levels]]", "[[Dow_Jones_1972_1975]]", "[[HD_189733_Photometry]]"]
features_used: ["[[Covariance_Function]]", "[[Squared_Exponential_Kernel]]", "[[Rational_Quadratic_Kernel]]", "[[Matern_Kernel]]", "[[Periodic_Kernel]]", "[[Changepoint_Kernel]]", "[[Mean_Function]]", "[[Hyperparameters]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[RMSE]]", "[[Normalized_Mean_Square_Error]]", "[[Log_Marginal_Likelihood]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Gaussian processes for time-series modelling

## 🎯 Main Objective & Contribution
- Tutorial/review presenting **Bayesian non-parametric [[Gaussian_Process]] (GP) modelling** as a principled framework for time-series analysis, forecasting under uncertainty, interpolation AND extrapolation in continuous time.
- Shows how **domain knowledge enters through covariance/mean function design**: kernels for periodicity, delays, noise, long-term drift, quasi-periodicity, changepoints, sensor faults; sums/products of valid kernels are valid kernels.
- Demonstrates **multi-output GPs** with cross-series correlations (spherical decomposition over series labels), **active data selection** (uncertainty-driven sampling), sequential/changepoint prediction, and **Bayesian quadrature** for hyperparameter marginalization.
- Foundation reference for probabilistic load forecasting lines later used in EV charging demand ([[Gaussian_Process]] → deep GP / robust GP forecasting).

## 🧠 Methodology & Model Architecture
### GP regression core (Section 3)
- Regression setting: $y(x) = f(x) + \eta$ with additive noise; inference targets $p(y^*|x^*)$. A set of function values at locations $\mathbf{x}$ is a multivariate Gaussian (**GP prior**):
$$p(y(\mathbf{x})) = \mathcal{N}(\boldsymbol{\mu}(\mathbf{x}), K(\mathbf{x},\mathbf{x})) \quad \text{(Eq. 3.2)}$$
with covariance matrix built element-wise from a kernel $k(x_i,x_j)$ (**Covariance Matrix**, Eq. 3.1); noisy observations fold into the diagonal (**Noisy Covariance**, Eq. 3.3):
$$V(\mathbf{x},\mathbf{x}) = K(\mathbf{x},\mathbf{x}) + \sigma^2 I$$
- Joint of data and test point (Eq. 3.4), giving the **GP Posterior Mean & Variance** (Eqs. 3.5–3.6):
$$m_* = \mu(x_*) + K(x_*,\mathbf{x})K(\mathbf{x},\mathbf{x})^{-1}\left(y-\mu(\mathbf{x})\right), \qquad \sigma_*^2 = k(x_*,x_*) - K(x_*,\mathbf{x})K(\mathbf{x},\mathbf{x})^{-1}K(\mathbf{x},x_*)$$
and vector form $p(\mathbf{y}_*)=\mathcal{N}(m_*, C_*)$ with $C_* = K_{**}-K_{*x}K_{xx}^{-1}K_{*x}^\top$ (Eqs. 3.7–3.10).
- **Kernel zoo**:
  - White noise (Eq. 3.12): $k_{WN}(x_i,x_j)=\sigma^2\delta(i,j)$
  - Squared exponential (Eqs. 3.11/3.13): $k_{SE}=h^2\exp\!\big(-\frac{(x_i-x_j)^2}{\lambda^2}\big)$ — output scale $h$, time scale $\lambda$, infinitely differentiable draws
  - Rational quadratic (Eq. 3.14): $k_{RQ}(x_i,x_j)=h^2\big(1+\tfrac{(x_i-x_j)^2}{\alpha\lambda^2}\big)^{-\alpha}$ — scale mixture of SEs; $\alpha\to\infty$ recovers SE
  - Matérn class (Eq. 3.15): $k_M = h^2\frac{1}{\Gamma(\nu)2^{\nu-1}}\big(\tfrac{2\sqrt{\nu}|x_i-x_j|}{\lambda}\big)^{\nu} B_\nu\big(\tfrac{2\sqrt{\nu}|x_i-x_j|}{\lambda}\big)$ — functions $(\nu+\tfrac{1}{2})$-times differentiable; $\nu=\tfrac12$ gives the exponential/Ornstein–Uhlenbeck (= AR(1)) kernel (Eq. 3.16); AR(p) ≈ Matérn $\nu=p-\tfrac12$
  - Periodic via warping $u(x)=(\cos\frac{2\pi x}{T},\sin\frac{2\pi x}{T})$ (Eq. 3.19), periodic-SE kernel (Eq. 3.20): $k_{per\text{-}SE}=h^2\exp\!\big(-\tfrac{1}{2w^2}\sin^2\!\big|\tfrac{\pi(x_i-x_j)}{T}\big|\big)$
  - Quasi-periodic (periodic × SE, Eq. 3.21): $k_{QP,SE}=h^2\exp\big(-\tfrac{\sin^2[\pi(x_i-x_j)/T]}{2w^2}-\tfrac{(x_i-x_j)^2}{\lambda^2}\big)$
  - Multi-input: product correlation rule (Eq. 3.17) or **Mahalanobis distance metric** (Eq. 3.18): $d^{(M)}(x_i,x_j;\Sigma)=\sqrt{(x_i-x_j)^\top\Sigma^{-1}(x_i-x_j)}$
  - Multi-output: inputs $[l,x]$ (label + time), $k([l_m,x_i],[l_n,x_j]) = k_x(x_i,x_j)\,k_l(l_m,l_n)$ with spherical decomposition of the label covariance
- **Changepoint covariances**: drastic change ($k_1$ before $x_c$, $k_2$ after, $x_c$ a hyperparameter), continuous conditionally independent variant, sudden changes in input scale λ or output scale h, and fault-model likelihood changes (biased/stuck/drifted sensors).
- **Mean functions** dominate far-from-data forecasts (e.g., exponential decay mean $m(x_*)=A e^{-a x_*}$, exoplanet transit shape).
- **Sequential modelling & active selection**: posterior variance shrinks on observation; adaptive sample retention because GP cost scales as $O(n^3)$ in retained samples.
### Hyperparameter marginalization (Section 4)
- Predictive distribution integrates over hyperparameters θ (Bayesian Model Averaging, Eq. 4.1):
$$p(y^*|y) = \frac{\int p(y^*|y,\theta)\,p(y|\theta)\,p(\theta)\,d\theta}{\int p(y|\theta)\,p(\theta)\,d\theta}$$
- Approximations compared: maximum likelihood (Dirac delta approximation), Laplace, variational Bayes, Monte Carlo/MCMC sampling of the hyperparameter posterior (Eq. 4.3), and **Bayesian quadrature** (GP fitted to the log-integrand) — the latter used exclusively in the examples.

## 📊 Dataset & Input Features
- **[[Bramblemet_Sensor_Network]]** — four real-time weather/sea-state sensors (Bramblemet, Sotonmet, Cambermet, Chimet) on the south coast of the UK; variables: wind speed/direction, air temperature, sea temperature, tide height; sporadic real-time stream + finer-grained retrospective data for assessment; 5-day tide-height evaluation set. Details in Osborne et al. [7].
- **[[Nile_River_Water_Levels]]** — canonical changepoint dataset, minimum water levels of the Nile, AD 622–1284 [20] (annual resolution).
- **[[Dow_Jones_1972_1975]]** — daily returns of the Dow–Jones industrial average, 3 July 1972 – 30 June 1975 [22] (`http://arxiv.org/abs/0710.3742` context).
- **[[HD_189733_Photometry]]** — photometric observations of planet-hosting star HD 189733 from Henry & Winn [24] (0.8 m Automated Patrol Telescope, Strömgren b/y filters).
- Features: time indices, sensor labels, external state variables (detector temperature, orbital phase, CCD position for the transit model); kernel inputs are continuous-time locations not fixed grids.
- Data availability / code links found in text:
  - Paper DOI: `http://dx.doi.org/10.1098/rsta.2011.0550`; journal site `http://rsta.royalsocietypublishing.org/`
  - Introductory GP code: `ftp://ftp.robots.ox.ac.uk/pub/outgoing/mebden/misc/GPtut.zip`
  - General GPML code: `http://www.gaussianprocess.org/gpml`

## 📈 Performance & Results
- **Bramblemet tide-height (5-day test, Table 1)**: naive persistence RMSE $7.5\times10^{-1}$ m (−2.1 dB NMSE); Kalman filter (best history length 16) $1.7\times10^{-1}$ m (−15.2 dB); independent per-sensor GPs $8.7\times10^{-2}$ m (−20.3 dB); **multi-output GP $3.8\times10^{-2}$ m (−27.6 dB)** — ~4.5× better than Kalman filter.
- Learned structure: tide period $T\approx$ half a day; disturbance Matérn ($\nu=5/2$) time scale ≈ 2.5 h; all four sensors inferred near-perfectly correlated (spherical decomposition ≈ 1); inter-sensor tidal delays ≈ 10 min (Cambermet/Chimet lag Bramblemet/Sotonmet, consistent with west→east high-tide timing); weather events induce ~20% tide-height changes. Multi-output GP exploits correlations to predict accurately through sensor dropouts and missing-data intervals.
- **Active selection**: keeping tide uncertainty below 10 cm needed only **119 observations** (multi-output) vs. **358** (independent GPs); GP preferentially samples undelayed Sotonmet/Bramblemet yet Chimet predictions remain accurate.
- **Changepoints**: Nile one-step lookahead recovers input-scale changepoint at **AD 720–722** (nilometer construction, AD 715); Dow–Jones output-scale (variance) changepoints align with the **OPEC oil embargo (19 Oct 1973)** and **Nixon resignation (9 Aug 1974)** plus weaker Watergate-era point (early 1973).
- **Stellar light curves (HD 189733)**: quasi-periodic (SE×RQ+WN) kernel learned $h=6.68$ mmag, $T=11.86$ d, $w=0.91$, $\alpha=0.23$, $\lambda=17.81$ d, $\sigma=2.1$ mmag — period in excellent agreement with Henry & Winn [24].

## 💡 Limitations & Identified Research Gaps
- Computational cost dominated by covariance-matrix inversion, scaling as $O(n^3)$ with retained samples → motivates sparse/inducing-point approximations and adaptive sample retention.
- Kernel/mean choice is subjective-looking; paper argues domain knowledge mitigates this, but automated kernel composition/search is left open.
- Maximum-likelihood hyperparameter fits ignore integrand width ("potentially problematic"); full Bayesian marginalization is expensive — Bayesian quadrature itself needs tractable sub-fits.
- Algorithmic rather than theoretical hurdles (implementation) explicitly not covered due to space.
- Future directions flagged: latent force models coupling GPs with differential equations, GPs inside larger probabilistic models, numerical integration, mixture-of-experts, unsupervised learning — relevant gaps for scalable probabilistic EV-load forecasting.

## 📚 BibTeX & Citation Reference
```bibtex
@article{roberts2013gaussian,
  title   = {Gaussian processes for time-series modelling},
  author  = {Roberts, Stephen and Osborne, Michael and Ebden, Mark and Reece, Steven and Gibson, Niall and Aigrain, Suzanne},
  journal = {Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences},
  volume  = {371},
  number  = {1984},
  pages   = {20110550},
  year    = {2013},
  doi     = {10.1098/rsta.2011.0550}
}
```

## 🔗 Key References & Citation Graph
- Rasmussen & Williams (2006), *Gaussian Processes for Machine Learning* [1] — canonical GP text underpinning the tutorial
- Osborne et al. (2008/2010) [2], [10] — multi-output GPs, active selection, changepoints/faults
- Garnett et al. (2009) [9]; Reece et al. (2009) [11], [12] — sequential changepoint prediction and sensor-fault covariances
- Adams & MacKay (2007), *Bayesian online changepoint detection* (`http://arxiv.org/abs/0710.3742`) [22]
- O'Hagan (1991) Bayes–Hermite quadrature [18]; Rasmussen & Ghahramani (2003) Bayesian Monte Carlo [19]
- Gibson et al. (2012) [25] — GP framework for exoplanet transit systematics
- Vault context:
  - [[2022_Cao_Robust_Deep_Gaussian_Process_Load]] — robust deep GP load forecasting against anomalous events, direct descendant
  - [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — neural alternative producing full predictive distributions
  - [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — quantile/attention-based probabilistic successor
  - [[2001_Hippert_Neural_Networks_STLF_Review]] — earlier deterministic NN era this Bayesian view responds to
