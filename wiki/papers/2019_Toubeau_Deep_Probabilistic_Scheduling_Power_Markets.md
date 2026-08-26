---
type: paper
title: "Deep Learning-Based Multivariate Probabilistic Forecasting for Short-Term Scheduling in Power Markets"
authors: [Jean-François Toubeau, Jérémie Bottieau, François Vallée, Zacharie De Grève]
year: 2019
journal_conference: "IEEE Transactions on Power Systems, Vol. 34, No. 2 (March 2019), pp. 1203-1215"
doi_url: "https://doi.org/10.1109/TPWRS.2018.2870041"
models_used: ["[[BLSTM|Bidirectional LSTM (BLSTM)]]", "[[LSTM]]", "[[MLP]]", "[[ARIMA]]", "[[SVR]]", "[[Random_Forest|RF]]", "[[Empirical_Copula]]"]
datasets_used: ["[[Belgian_Power_Grid_Data]]", "[[NWP_Belgium]]"]
features_used: ["[[Electricity_Load]]", "[[Wind_Power]]", "[[Solar_Power]]", "[[Market_Price|Day-Ahead Electricity Price]]", "[[Weather_Features|NWP: temperature, wind speed, cloud cover, solar radiation]]", "[[Calendar_Encoding|Mutually exclusive binary hour/day/month + holiday index]]", "[[Lagged_Values]]"]
forecasting_horizon: "[[Day_Ahead]]"
metrics: ["[[RMSE]]", "[[Pinball_Loss|Quantile (Pinball) Loss]]", "[[ACF_Deviation|Autocorrelation Function Deviation]]", "[[Pearson_Correlation]]", "[[Spearman_Correlation]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Deep Learning-Based Multivariate Probabilistic Forecasting for Short-Term Scheduling in Power Markets

## 🎯 Main Objective & Contribution
- Generates **short-term multivariate probabilistic forecasts and predictive scenarios** for day-ahead operational scheduling of electricity aggregators/VPPs in power markets (predictions issued daily at 12:00 for hours m = 12–36 ahead).
- Four contributions:
  1. Tailored architectural variations exploiting the structure of day-ahead planning: **bidirectional LSTM ([[BLSTM]])** since all 24 hourly predictions are needed simultaneously; bidirectional processing lowers forecast error and avoids the error accumulation of recursive unidirectional strategies.
  2. Compares **two uncertainty characterizations** trained on the same BLSTM: parametric Gaussian likelihood vs non-parametric [[Quantile_Regression]] (pinball loss).
  3. Extends intervals/densities to **predictive scenarios** via copula-based sampling of the multivariate forecast distribution, capturing both temporal autocorrelation and cross-variable dependencies.
  4. Evaluates value not only statistically but through a **scenario-based stochastic optimization** case study of an electricity retailer's day-ahead multi-market bidding.

## 🧠 Methodology & Model Architecture
- **Two-step procedure**: (1) probabilistic forecasting per variable per time step with deep recurrent nets; (2) sampling of the D-dimensional joint distribution ($D = \#T \cdot \#I$, time steps × variables) using an empirical copula.
- **[[LSTM]] composite equations** for layer $l \in [1, N_L]$ with hidden state $s_t^{(l)}$ and cell activation $c_t$:
$$i_t = \sigma\left(W_{i\iota}s_t^{(l-1)} + W_{h\iota}s_{t-1} + W_{c\iota}c_{t-1}\right) \tag{Input gate}$$
$$f_t = \sigma\left(W_{i\varphi}s_t^{(l-1)} + W_{h\varphi}s_{t-1} + W_{c\varphi}c_{t-1}\right) \tag{Forget gate}$$
$$c_t = f_t c_{t-1} + i_t \tanh\left(W_{i\gamma}s_t^{(l-1)} + W_{h\gamma}s_{t-1}\right) \tag{Cell state update}$$
$$o_t = \sigma\left(W_{io}s_t^{(l-1)} + W_{ho}s_{t-1} + W_{co}c_t\right) \tag{Output gate}$$
$$s_t = o_t \tanh(c_t) \tag{Hidden output}$$
Bidirectional topology (Schuster & Paliwal) processes sequences forwards and backwards into one output vector — suited to offline multi-step prediction where all horizon outputs are needed at once; faster to train and robust to biased inputs.
- **Parametric (Gaussian) training** — minimize negative log-likelihood over the training window:
$$E_L = -\sum_{t=t_0}^{T} \ln L(y_{i,t} \mid \theta(s_t)) \tag{Negative log-likelihood loss}$$
with Gaussian likelihood
$$L_G = (2\pi\sigma^2)^{-1/2}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) \tag{Gaussian likelihood}$$
and BLSTM output heads
$$\mu(s_t) = w_\mu s_t \tag{Mean head}$$
$$\sigma(s_t) = \ln(1+\exp(w_\sigma s_t)) \tag{Std-dev head (softplus)}$$
- **Non-parametric (quantile) training** — predict quantiles $q \in Q$ directly, where $q = P(y_{t+k} \le y_{t+k}^{(q)} \mid y^{\to t})$ (Eq. 10); quantiles are affine functions of BLSTM outputs. Minimize total pinball loss summed over all quantiles of interest:
$$E_Q = \sum_{q \in Q}\ q \max(0,\ d - y^{(q)}) + (1-q)\max(0,\ y^{(q)} - d) \tag{Quantile / pinball loss}$$
with $q \in \{1,5,10,25,50,75,90,95,99\}\%$. Gradient forced to zero at the non-differentiable kink of perfect prediction. Differentiable loss → daily retraining with only newly revealed data is cheap (no metaheuristics needed).
- **Copula-based scenario generation** (empirical, parameter-free): Phase I builds the copula model from history by probability-integral-transforming data onto the unit D-cube $[0,1]^D$ and estimating the empirical copula density over $K^D$ sub-cubes:
$$c(u) = \frac{N_j}{n\left(\frac{1}{K}\right)^D},\quad j = (j_1,\dots,j_D) \tag{Empirical copula density}$$
with marginal densities obtained by integration,
$$c_d(u_1,\dots,u_d) = \int_0^1 \cdots \int_0^1 c(u)\, du_{d+1}\cdots du_D \tag{Marginal density}$$
and conditional distribution functions used sequentially during sampling:
$$C_d(u_d \mid u_1,\dots,u_{d-1}) = \frac{\int_0^{u_d} c_d(u_1,\dots,u_{d-1},u)\,du}{c_{d-1}(u_1,\dots,u_{d-1})},\quad d = 2,\dots,D \tag{Conditional CDF}$$
Phase II samples dependent uniforms $u^{gen}$ (first from U(0,1), then conditionally), then converts to original dimensions by inverse transform sampling on the BLSTM marginal predictive distributions. Sparse-array/hash-based storage alleviates the curse of dimensionality, enabling larger granularity K.
- **Model selection**: two-nested-loops procedure — outer loop over input-vector configurations (e.g., hourly index as incremental [0.1–2.4], 5-bit Gray coding, or 24 mutually exclusive binary inputs), inner loop over hyperparameters (#hidden layers, #neurons, weight-noise variance, learning rate). Training by online [[BPTT]]; regularization via early stopping and weight noise. Best temporal encoding: mutually exclusive binary (given sufficient capacity).
- Implementation in Matlab; ~1 min/train MLP vs ~5 min LSTM architectures (parallelizable, done once); real-time inference < 1 s.

## 📊 Dataset & Input Features
- **Data**: hourly historical data from **2012 until 2017** for aggregated load, wind generation, PV generation and day-ahead electricity prices in **Belgium**; test set = one month of winter 2017 (out-of-sample). Predictions benchmarked against the Belgian TSO's (Elia) published day-ahead forecasts under identical conditions (issued at 12:00 day-ahead). Targets are maximum extractable renewable energy and non-shiftable load.
- **Inputs selected**: last measured values (previous 6–24 h) for all variables; same-day-of-week previous week values for load and price; mutually exclusive binary encodings for hour-of-day/day-of-week/month-of-year plus holiday index; day-ahead NWP features (temperature, wind speed, cloud cover, solar radiation) at a single Belgian location; prices additionally use predicted load and renewables as explanatory inputs.
- **Case-study portfolio**: retailer owning 1% of Belgian load and 20% of installed onshore wind + PV capacity, balancing quarter-hourly via the day-ahead market.
- **Links/data availability**: DOI https://doi.org/10.1109/TPWRS.2018.2870041 ; IEEE Xplore http://ieeexplore.ieee.org ; cited arXiv sources https://arxiv.org/abs/1609.08144 , https://arxiv.org/abs/1704.04110 , https://arxiv.org/abs/1711.11053v1 . No public code/data repository stated; funding: Public Service of Wallonia (Smartwater project).

## 📈 Performance & Results
- **Point forecasts (Table I, RMSE)**: ranking BLSTM < unidirectional LSTM < MLP < RF/SVR < ARIMA ≈ TSO tool; recurrent models beat the system operator's tool. Best topologies: 3-layer BLSTM for wind, load, and prices; 4-hidden-layer BLSTM for PV; optimal capacity small (10–20 neurons/layer) due to limited historical data.
- **Parametric vs non-parametric (Table III)**: non-parametric quantile regression slightly outperforms the Gaussian assumption (better-calibrated, tighter intervals across q ∈ {1..99}%); Gaussian errors acceptable especially for PV.
- **Correlation analysis (Table IV)**: prices negatively correlated with renewable share, positively with demand; wind-load correlation weak — justifying multivariate copula treatment.
- **Scenario quality (Fig. 7, Table V)**: copula sampling reproduces smooth time profiles, while independent sampling yields spurious sharp ramps; mean ACF deviation between scenario and actual data much smaller with the copula method — temporal dependence correctly captured.
- **Decision value (Fig. 9, month-long simulation)**: replacing independent sampling with copula-based scenarios in the stochastic optimization raised retailer profit by ≈ **4×10⁵ € (>10% relative increase)**; upgrading MLP → BLSTM forecasts added ≈ **0.5×10⁵ €**, avoiding overly conservative policies.

## 💡 Limitations & Identified Research Gaps
- Optimal architecture is dataset-size-dependent: limited history forces shallow networks (10–20 neurons), so accuracy should grow as more data accumulates; retraining extent (how much to modify prior optimum with new data) left outside scope.
- Data-driven models ignore structural/market constraints (acceptable for zonal European day-ahead clearing, but noted as future work to combine data-driven models with physically-based market rules).
- Empirical copula suffers curse of dimensionality (mitigated only via hash/sparse storage, not vine copulas); scenario count/tractability trade-off remains.
- Quantile loss kink requires numerical gradient handling; no EV-specific modeling (load is aggregate non-shiftable) — gap for thesis: applying BLSTM+copula pipelines to EV charging station probabilistic scenarios.

## 📚 BibTeX & Citation Reference
```bibtex
@article{toubeau2019deep,
  title={Deep Learning-Based Multivariate Probabilistic Forecasting for Short-Term Scheduling in Power Markets},
  author={Toubeau, Jean-Fran{\c{c}}ois and Bottieau, J{\'e}remie and Vall{\'e}e, Fran{\c{c}}ois and De Gr{\`e}ve, Zacharie},
  journal={IEEE Transactions on Power Systems},
  volume={34},
  number={2},
  pages={1203--1215},
  year={2019},
  publisher={IEEE},
  doi={10.1109/TPWRS.2018.2870041}
}
```

## 🔗 Key References & Citation Graph
- Foundation: [[1997_Hochreiter_Long_Short_Term_Memory]] (Hochreiter & Schmidhuber); Bidirectional RNNs (Schuster & Paliwal, IEEE Trans. Signal Process. 1997)
- Uncertainty paradigms cited: DeepAR (Flunkert et al., arXiv:1704.04110 → vault [[2020_DeepAR_Probabilistic_Forecasting_with_Autoregressive_Recurrent_Networks]]), Multi-horizon Quantile Recurrent Forecaster (Wen et al., arXiv:1711.11053), Quantile Regression (Koenker & Bassett, Econometrica 1978)
- Scenario-generation lineage: Morales et al. (2010), Pinson et al. (Wind Energy 2008), vine copulas (Wang et al., IEEE TPWRS 2018), empirical copula tools (Strelen & Nassaj, 2007)
- Related vault papers: [[2019_Zhu_EV_Load_Forecasting]], [[2020_DeepAR_Probabilistic_Forecasting_with_Autoregressive_Recurrent_Networks]], [[2021_Lim_TFT_Temporal_Fusion_Transformers]]
