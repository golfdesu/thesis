---
type: paper
title: "Neural Networks for Short-Term Load Forecasting: A Review and Evaluation"
authors: [Henrique Steinherz Hippert, Carlos Eduardo Pedreira, Reinaldo Castro Souza]
year: 2001
journal_conference: "IEEE Transactions on Power Systems, 16(1), 44-55"
doi_url: "https://doi.org/10.1109/59.912452"
models_used: ["[[MLP]]", "[[ANN]]", "[[ARIMA]]", "[[Linear_Regression]]", "[[Kohonen_SOM]]", "[[Recurrent_Neural_Network]]", "[[Fuzzy_Neural_Network]]", "[[Projection_Pursuit_Regression]]", "[[Adaline]]"]
datasets_used: ["[[Utility_Load_Data_1990s]]", "[[Taiwan_Power_System]]", "[[Greek_Power_System]]", "[[Autonomous_Island_System_Crete]]"]
features_used: ["[[Lagged_Load]]", "[[Temperature]]", "[[Humidity]]", "[[Calendar_Variables]]", "[[Day_Type_Dummy]]", "[[Nonlinear_Temperature_Functions]]", "[[Weather_Forecast]]"]
forecasting_horizon: "[[Day_Ahead]]"
metrics: ["[[MAPE]]", "[[RMSE]]", "[[MSPE]]", "[[MAE]]", "[[Standard_Deviation_Errors]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Neural Networks for Short-Term Load Forecasting: A Review and Evaluation

## 🎯 Main Objective & Contribution
- Critical review of **40 papers (1991–1999, leading EE journals only)** applying [[ANN]]s to short-term load forecasting ([[STLF]]), written to explain researcher skepticism about NN forecasting claims.
- **Two major findings**: (a) most proposed [[MLP]]s — especially profile forecasters with 24 output nodes — were **overparameterized** (more weights than training samples → expected overfitting); (b) models were **not systematically tested** against standard benchmarks and error analysis bypassed standard forecasting practice.
- Establishes methodological protocols still cited today: compare vs. naïve + standard statistical baselines, report in-sample AND out-of-sample errors, use multiple error metrics and error-distribution diagnostics.
- Economic motivation quoted from Bunn & Farmer [10]: a 1% increase in forecast error implied ~£10 million/year extra operating cost (1984 estimate).

## 🧠 Methodology & Model Architecture
- **Review framework**: design choices classified into 4 stages — (A) data pre-processing, (B) NN design, (C) implementation, (D) validation; evaluation guidelines adapted from Adya & Collopy [1].
- **Canonical architecture reviewed**: two-layer feed-forward [[MLP]]; neuron = weighted linear sum + nondecreasing differentiable activation (logistic/identity/tanh/sinusoidal). With logistic hidden layer and linear output, the network implements the **nonlinear regression model**:
$$\hat{y} = W_2\,\sigma(W_1 \mathbf{x} + \mathbf{b}_1) + b_2$$
trained by minimizing the quadratic loss (backpropagation / steepest descent on the error surface).
- **Output strategies for 24-hour profiles**: (a) iterative one-step-ahead recursion; (b) multi-model (24 parallel NNs, one per hour); (c) single-model multivariate (one big MLP with 24 output neurons — most common, but forces large nets and yields only 365 training vectors per year of data).
- **Pre-processing taxonomy**: calendar-based classification (weekday/Saturday/Sunday/holiday; up to 11 day-type classes), seasonal classes, weather-similarity classes; class labels injected either as dummy inputs or via separate per-class networks; outlier/Kalman-filter cleaning; detrending/differencing for nonstationarity.
- **Input selection practice**: lagged loads chosen by ACF/PACF analysis or phase-space embedding; temperature as dominant exogenous variable, often transformed by piecewise linear-quadratic functions $f(T)$ to capture the U-shaped load–temperature relation; humidity/wind occasionally included.
- **Overfitting remedies discussed**: early stopping via cross-validation; complexity-penalizing regularization (penalizing second derivatives of output wrt inputs) — **none of the 40 papers used regularization**; pruning algorithms [77].
- Alternative architectures surveyed: projection pursuit regression [95], frequency-domain decomposition into Adalines [71], single-neuron functional-link network (Fourier + polynomial components) [24], Kohonen SOM classification of profiles [20], [54], [84], recurrent NNs [15], [16], [86].

## 📊 Dataset & Input Features
- All 40 reviewed systems were tested on **real utility data** (no public benchmarks): e.g., Taiwan power system [39], [40], Greek power system [6], autonomous (Crete-like) island system [52], small US utilities; sample sizes typically **a few years of hourly data** (≈365 profile-vectors/year).
- Input features across reviewed papers: past-day/past-two-day hourly loads ($L$), dry-bulb temperature ($T$, often as nonlinear $f(T)$ pieces), relative humidity ($H$), wind speed, calendar/day-type dummies, month/season indicators, holiday flags, forecasted vs. observed temperature (most simulations used observed weather → optimistic errors).
- Sampling resolution: hourly loads (one paper [56] did minute-by-minute very-short-term forecasts of next half-hour).
- Data availability: none — proprietary utility SCADA/EMS archives; no URLs/DOIs for data in any reviewed paper. Paper itself: `https://doi.org/10.1109/59.912452`, IEEE Xplore S 0885-8950(01)02306-9.

## 📈 Performance & Results
- This is a review paper: it reports no new forecasts but audits reported results.
- **Overparameterization evidence (Table III)**: computed parameter counts show most profile-forecasting MLPs had **more weights than training points** (hundreds–thousands of parameters vs. ≤ a few hundred profile samples); e.g., 24-output MLPs fed 24–48 lagged-load inputs run into thousands of parameters.
- Only 10 of the 40 papers ([14], [15], [53], [55], [56], [61], [63], [66], [68], [83]) compared against standard **linear regression/ARIMA** baselines; only [23] found linear models actually beat its NNs; almost none reported naïve-persistence baselines or in-sample fits (only [52], [61]).
- **Error reporting critique**: nearly all papers reported only [[MAPE]] (~1–4% typical claims); few reported error SD ([2], [17], [55], [70], [86]), cumulative distributions, percentiles, max errors, histograms, correlograms, or portmanteau tests; authors argue squared-error measures ([[RMSE]], MSPE) better reflect the nonlinear loss function utilities face, plus [[MAE]] for operator needs.
- Conclusion: results are "not convincing" taken individually — yet widespread practical success suggests large NN forecasters may work despite overparameterization, which is not yet theoretically understood.

## 💡 Limitations & Identified Research Gaps
- No adequate rate between #training points and #weights has been established ("how many parameters are too many" remains open).
- Comparisons to other NNs/fuzzy engines deemed invalid baselines; ARMAX/regression fitting effort discouraged fair benchmarking — a persistent evaluation gap.
- Treating a day as a 24-dim vector starves training sets; multi-model and iterative approaches underexplored; chaotic behavior of iterated MLP outputs noted ([19], [20]).
- Weather-forecast uncertainty ignored in simulations (real deployment errors will be larger) — cf. [27], [75].
- Calls for rigorous reporting standards: full error-distribution analysis, graphical diagnostics, significance of comparisons — directly relevant to modern EV-charging forecasting benchmarking practice.

## 📚 BibTeX & Citation Reference
```bibtex
@article{hippert2001neural,
  title   = {Neural Networks for Short-Term Load Forecasting: A Review and Evaluation},
  author  = {Hippert, Henrique Steinherz and Pedreira, Carlos Eduardo and Souza, Reinaldo Castro},
  journal = {IEEE Transactions on Power Systems},
  volume  = {16},
  number  = {1},
  pages   = {44--55},
  year    = {2001},
  doi     = {10.1109/59.912452}
}
```

## 🔗 Key References & Citation Graph
- Park et al. (1991) [68] and Peng, Hubele & Karady (1992) [70] — pioneering ANN STLF papers audited here
- Bakirtzis et al. (1996) [6] — Greek system MLP with nonlinear temperature inputs
- Khotanzad et al. ANNSTLF (1997 [49], 1998 [50]) — modular NN systems deployed at utilities
- Adya & Collopy (1998) [1] — evaluation guidelines adopted by this review
- Zhang, Patuwo & Hu (1998) [96] — state-of-the-art review of NN forecasting
- Bunn & Farmer (1985) [10] — economic impact of load-forecast error
- Vault context:
  - [[1997_Hochreiter_Long_Short_Term_Memory]] — recurrent successor to the static MLPs reviewed here
  - [[2015_Raza_Review_AI_Load_Demand]] — later AI-in-load-forecasting review continuing this line
  - [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — modern echo of the "benchmark simple linear models" message
  - [[2019_Zhu_EV_Load_Forecasting]] — deep-learning STLF inheriting these evaluation debates
