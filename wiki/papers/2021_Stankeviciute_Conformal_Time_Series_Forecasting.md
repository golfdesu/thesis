---
type: paper
title: "Conformal Time-Series Forecasting"
authors: [Kamilė Stankevičiūtė, Ahmed M. Alaa, Mihaela van der Schaar]
year: 2021
journal_conference: "NeurIPS 2021 (35th Conference on Neural Information Processing Systems)"
doi_url: "https://proceedings.neurips.cc/paper/2021/file/9232fe81225bcaef853ae32870a2b0fe-Paper.pdf"
models_used: ["[[CF-RNN]]", "[[Conformal_Prediction]]", "[[Inductive_Conformal_Prediction|ICP]]", "[[LSTM]]", "[[BJ-RNN]]", "[[MQ-RNN]]", "[[DP-RNN]]"]
datasets_used: ["[[MIMIC-III]]", "[[UCI_EEG]]", "[[COVID19_UK_Dataset]]", "[[Synthetic_AR_Noise]]"]
features_used: ["[[Nonconformity_Score]]", "[[Calibration_Set]]", "[[Multi_Horizon_Forecast]]", "[[Direct_Forecasting_Strategy]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[Joint_Coverage]]", "[[Prediction_Interval_Width]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Conformal Time-Series Forecasting

## 🎯 Main Objective & Contribution
- **Core problem**: RNN-based multi-horizon forecasts issue point estimates only; existing uncertainty methods (Bayesian RNNs, quantile RNNs like [[MQ-RNN]], ensembles/bootstrapping like [[BJ-RNN]]) require architecture changes, are hard to calibrate, scale poorly ([[BJ-RNN]] exact inference is $O(P^3)$ in parameters $P$), and lack finite-sample frequentist coverage guarantees.
- **Primary contribution**: Extends **inductive conformal prediction (ICP)** to the multi-horizon time-series setup → **Conformal Forecasting RNN ([[CF-RNN]])**: a lightweight post-hoc wrapper around *any* direct multi-horizon point forecaster producing distribution-free prediction intervals with theoretical $(1-\alpha)$ joint coverage over the whole trajectory — no retraining of the base model.
- Key insight: time-steps within a series are non-exchangeable, but the dataset is treated as a set of **exchangeable whole-series observations** $(y_{1:T}, y_{T+1:T+H})$.

## 🧠 Methodology & Model Architecture
- Wrapper around a direct-strategy [[LSTM]] (all $H$ steps predicted simultaneously from one embedding — robust to error accumulation and gives conditionally independent predictions needed for the guarantee).
- **Multi-horizon forecast** (Eq. 1):
$$\hat{y}_{(t'+1):(t'+H)} = (\hat{y}_{t'+1}, \ldots, \hat{y}_{t'+H}) \in \mathbb{R}^{H \times d}$$
- **Trajectory validity target** (Eq. 2):
$$P\left[y_{t+h} \in [\hat{y}^L_{t+h}, \hat{y}^U_{t+h}], \forall h \in \{1,\ldots,H\}\right] \geq 1-\alpha$$
- **ICP validity** (Eq. 3): $P[y^{(l+1)} \in \Gamma^\alpha(x^{(l+1)}) \mid D] \geq 1-\alpha$ under exchangeability; standard regression **nonconformity score** (Eq. 4):
$$R_i = A(D,(x^{(i)},y^{(i)})) = \Delta(M(x^{(i)}|D), y^{(i)})$$
- Single-step ICP interval (Eq. 5): $\Gamma^\alpha(x^{(l+1)}) = [\hat{y}^{(l+1)} - \hat{\varepsilon},\ \hat{y}^{(l+1)} + \hat{\varepsilon}]$ with $\hat{\varepsilon}$ = $\lceil(m+1)(1-\alpha)\rceil$-th smallest calibration residual.
- **H-dimensional nonconformity score** (Eq. 6):
$$R_i = \begin{bmatrix} |y^{(i)}_{t+1}-\hat{y}^{(i)}_{t+1}|, & \ldots, & |y^{(i)}_{t+H}-\hat{y}^{(i)}_{t+H}| \end{bmatrix}^\top$$
- **Bonferroni + finite-sample correction**: critical scores $\hat{\varepsilon}_h$ = the $\lceil(m+1)(1-\alpha/H)\rceil$-th smallest residual in each horizon's score distribution ($m$ = calibration size).
- **Per-horizon prediction interval** (Eqs. 7–8):
$$\Gamma^\alpha_h(y^{(l+1)}_{1:t}) = \left[\hat{y}^{(l+1)}_{t+h} - \hat{\varepsilon}_h,\ \hat{y}^{(l+1)}_{t+h} + \hat{\varepsilon}_h\right] \quad \forall h \in \{1,\ldots,H\}$$
- **Theorem 1 (Conformal forecasting validity)** (Eq. 9):
$$P(\forall h \in \{1,\ldots,H\}. \ y_{t+h} \in [\hat{y}_{t+h}-\hat{\varepsilon}_h, \hat{y}_{t+h}+\hat{\varepsilon}_h]) \geq 1-\alpha$$
(proof from conditional validity of ICP in Vovk [51] + Boole's inequality; Algorithm 1 gives the full calibration procedure).
- Synthetic data generator (Eq. 10): $y_t = \sum_{k=0}^{t} a_k \cdot x_k + \epsilon_t$, with $x_t \sim N(\mu_x, \sigma_x^2)$, memory $a=0.9$, noise $\epsilon_t \sim N(0, \sigma_t^2)$; five static ($\sigma_t^2 = 0.1n$) and five time-dependent ($\sigma_t^2 = 0.1tn$) variance profiles, $n \in \{1,\ldots,5\}$.
- Univariate focus ($d=1$); multivariate extension left as future work.

## 📊 Dataset & Input Features
| Dataset | # Training sequences (with calibration) | Window $T$ | Horizon $H$ |
| --- | --- | --- | --- |
| [[MIMIC-III]] (daily white blood cell counts, ICU) | 3823 (2000) | [3, 47] | 2 |
| [[UCI_EEG]] (downsampled EEG, 3 visual stimuli) | 19200 (15360) | 40 | 10 |
| [[COVID19_UK_Dataset]] (daily cases, UK local authority districts) | 300 (200) | 100 | 50 |
| [[Synthetic_AR_Noise]] (autoregressive + noise) | 2000 (1000 train / 1000 calib) | 15 | 5 |

- Features: observed history window $y_{1:t}$; per-horizon calibration residuals; target coverage level $1-\alpha$ (default 90%, $\alpha=0.1$).
- **Links / data availability**:
  - Code: https://github.com/kamilest/conformal-rnn
  - Paper PDF: https://proceedings.neurips.cc/paper/2021/file/9232fe81225bcaef853ae32870a2b0fe-Paper.pdf
  - MIMIC-III: freely accessible critical care database (Johnson et al., Sci. Data 2016)
  - EEG: UCI ML repository, http://www.ics.uci.edu/~mlearn/MLRepository.html
  - COVID-19 UK: https://coronavirus.data.gov.uk/ (accessed 2021-05-25)

## 📈 Performance & Results
- Baselines: [[BJ-RNN]] (blockwise jackknife, frequentist), [[MQ-RNN]] (multi-quantile/pinball), [[DP-RNN]] (Monte Carlo dropout). All share the same underlying LSTM hyperparameters and direct forecasting strategy.
- **Synthetic data (90% target joint coverage)**: CF-RNN achieves 90.6–94.6% coverage across all static/time-dependent noise profiles vs MQ-RNN ~57–67% and DP-RNN ~0–5%; BJ-RNN hits 97–100% but with far wider intervals (e.g. width 98.45 ± 25.95 vs CF-RNN's 16.45 ± 3.69 at static $n=1$) and prohibitive compute ($O(P^3)$).
- CF-RNN intervals adapt to noise: nearly constant width under static noise (16.45–17.34), widening monotonically under time-dependent noise (19.80 → 49.00 as variance accumulates).
- **Real-world data (Table 5)** — CF-RNN is the *only* model to reach target coverage on all three datasets:
  - MIMIC-III: joint coverage 94.0 ± 1.2% (MQ-RNN 89.3 ± 1.2%, DP-RNN 40.2 ± 13.9%); CI length 20.59 ± 3.10
  - EEG: 96.5 ± 1.0% (MQ-RNN 48.0 ± 4.0%, DP-RNN 3.3 ± 0.7%); CI length 61.86 ± 18.02
  - COVID-19: 89.7 ± 5.3% (MQ-RNN 15.0 ± 5.9%, DP-RNN 0.0%); CI length 733.95 ± 582.52
- **Bonferroni ablation (Table 6)**: without correction, joint coverage collapses (EEG 59.4%, COVID-19 55.5%) even though independent per-horizon coverage looks fine → Bonferroni correction is essential for trajectory-level guarantees.
- Larger calibration sets shrink intervals; fixed-width trade-off limits reliable horizon depth (low coverage targets allow valid long-horizon prediction).

## 💡 Limitations & Identified Research Gaps
- Univariate focus ($d=1$); multivariate extension left as future work.
- Intervals are widest among compared models (conservative efficiency); future work targets narrower, more adaptive per-observation intervals.
- Relies on exchangeability of whole-series observations; adaptation lag possible under strong non-stationarity.
- Direct (not recursive) forecasting strategy required for the theory.
- Relevant gap for EV load forecasting: cheap post-hoc $(1-\alpha)$ trajectory guarantees for any point forecaster without retraining.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{stankeviciute2021conformal,
  title={Conformal Time-Series Forecasting},
  author={Stankevi{\v{c}}i{\=u}t{\.{e}}, Kamil{\.{e}} and Alaa, Ahmed M. and van der Schaar, Mihaela},
  booktitle={Advances in Neural Information Processing Systems},
  volume={34},
  pages={17416--17428},
  year={2021}
}
```

## 🔗 Key References & Citation Graph
- Vault papers: [[2024_Zhou_Conformal_Prediction_DER]], [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] (quantile/pinball alternative), [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] (multi-series probabilistic setting), [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]] (post-hoc model-agnostic wrapper analogy), [[1997_Hochreiter_Long_Short_Term_Memory]] (underlying LSTM)
- Cited-in-text foundations: conformal prediction (Vovk et al., Algorithmic Learning in a Random World 2005), ICP (Papadopoulos et al. 2002), EnbPI (Xu & Xie 2021), BJ-RNN (Alaa & van der Schaar 2020), MQ-RNN (Wen et al. 2017), SQF-RNN (Gasthaus et al. 2019), Monte Carlo dropout (Gal & Ghahramani 2016), DeepAR (Salinas et al. 2020), Conformalized Quantile Regression (Romano et al. 2019), MIMIC-III (Johnson et al. 2016)
