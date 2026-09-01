---
type: paper
title: "Probabilistic Forecast of EV Charging Demand using Quantile Regression and LSTM with Attention Mechanism"
authors: [Silvana Matrone, Amirhossein Heydarian Ardakani, Emanuele Ogliari, Elham Shirazi, Sonia Leva]
year: 2025
journal_conference: "ACM E-Energy '25: 16th ACM International Conference on Future and Sustainable Energy Systems (June 17-20, 2025, Rotterdam, Netherlands)"
doi_url: "https://doi.org/10.1145/3679240.3734687"
models_used: ["[[QR_LSTM_Attention|QR-LSTM-Attention]]", "[[LSTM]]", "[[Seq2Seq|Encoder-Decoder with Attention]]", "[[Quantile_Regression]]", "[[Persistence_Model|Persistence Benchmark]]"]
datasets_used: ["[[SmoothEMS_Met_GridShield_ASR_Utrecht_Dataset]]", "[[Weather]]"]
features_used: ["[[Historical_Load]] (96 input steps = previous day)", "[[Temperature]]", "[[Global_Solar_Radiation]]", "[[Number_of_Active_Sessions]]", "[[Calendar_Features]] (month, day, hour, minute)"]
forecasting_horizon: "[[Day_Ahead_Forecasting|24-Hour Day-Ahead Probabilistic Forecast, Rolling Horizon Refreshed Hourly (15-min resolution)]]"
metrics: ["[[CRPS]]", "[[Pinball_Loss]] (q20/q50/q80)", "[[PICP]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Probabilistic Forecast of EV Charging Demand using Quantile Regression and LSTM with Attention Mechanism

## 🎯 Main Objective & Contribution
- Point forecasts alone are inadequate for microgrid/distributed energy management under uncertainty; few studies address **probabilistic** EV charging demand forecasting.
- Extends the authors' prior point-forecast [[LSTM]]-attention model (Matrone et al. 2024, IEEE T-ITS) into a probabilistic framework via **[[Quantile_Regression]]**: three separate LSTM encoder-decoder attention models trained for the **20th, 50th (median), and 80th quantiles**, producing continuous prediction bands for day-ahead EV charging demand.
- Evaluated on real data from an office parking lot in Utrecht (NL); best model cuts CRPS by **67.70%** vs a persistence benchmark.

## 🧠 Methodology & Model Architecture
### LSTM Encoder-Decoder with Attention
- **Encoder**: stacked [[LSTM]] layers compressing 96 input steps into a lower-dimensional representation — the last hidden state of the final LSTM layer becomes the **Context Vector** fed to the decoder.
- **Decoder**: generates predictions per required time step by interpreting the context vector.
- **Attention layer**: dynamically refines the context vector by computing a weighted sum of all encoder hidden states; alignment scores assess relevance between the previous decoder output and each current hidden state.

### Quantile Regression (pinball loss)
(**Eq. 1 — pinball loss**, minimized separately per quantile $\tau$):
$$ L_\tau(y, \hat{y}) = \begin{cases} \tau\,(y - \hat{y}) & \text{if } y \geq \hat{y} \\ (1-\tau)(\hat{y} - y) & \text{if } y < \hat{y} \end{cases} $$
Asymmetric: $\tau \in [0,0.5)$ penalizes underforecasting less (lower quantiles), $\tau \in (0.5,1]$ penalizes overforecasting less; $\tau=0$ reduces to absolute error.

### Evaluation Metrics
(**Eq. 2 — Continuous Ranked Probability Score**):
$$ \text{CRPS}(\hat{F}, y) = \sum_{i=1}^{N} \left( \hat{F}(y_i) - \mathbb{1}\{y_i \geq y\} \right)^2 \Delta y_i $$
where $\hat{F}(y_i)$ is the forecast CDF up to $y_i$, $\mathbb{1}\{\cdot\}$ is the Heaviside step function; plus **[[PICP]]** (percentage of true values inside predicted interval).

### Hyperparameter Sweep
Encoder/decoder depth {1, 2} layers × units {24, 48, 64} → six configurations; 80/20 train/test split.

## 📊 Dataset & Input Features
- **[[SmoothEMS_Met_GridShield_ASR_Utrecht_Dataset]]**: EV charging demand from the **ASR office parking lot in Utrecht, Netherlands**, collected within the SmoothEMS Met GridShield project.
  - Resolution: **15-minute discretization**
  - Split: 80% train / 20% test
  - Input window: **96 steps (= previous full day)** → predict next day, no lag
  - Forecast protocol: **rolling horizon refreshed once every hour**, providing a 24-hour horizon.
  - Size (#sessions/#chargers): not disclosed in the paper text.
- **[[Weather]]**: Royal Netherlands Meteorological Institute weather data — official download page: https://www.knmi.nl/nederland-nu/klimatologie/daggegevens (accessed 2025-04-07).
- **Input features**: month, day, hour, minute, temperature, global radiation, number of active charging sessions.
- Paper is Open Access (CC BY 4.0), ACM ISBN 979-8-4007-1125-1/25/06; no separate code/data repository stated beyond KNMI weather portal.

## 📈 Performance & Results
| Model | Pinball q50 | Pinball q20 | Pinball q80 | CRPS | PICP |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 24-1 | 1.730 | 3.870 | 4.028 | 6.754 | 61.00% |
| 24-2 | 1.851 | 4.210 | 3.487 | 6.874 | 62.05% |
| 48-1 | 1.494 | 4.095 | 2.800 | 6.197 | 72.12% |
| **48-2 (best)** | **1.486** | **4.020** | **2.847** | **6.111** | **78.60%** |
| 64-1 | 1.715 | 3.821 | 3.523 | 6.532 | 73.58% |
| 64-2 | 1.570 | 3.906 | 2.812 | 6.217 | 66.02% |
| Benchmark | 10.606 | 7.986 | 8.885 | 18.918 | 51.78% |

- **Benchmark**: weekly persistence median + fixed-width intervals (10% of persistence prediction) around it for q20/q80.
- Improvements of Model 48-2 over benchmark: Pinball q20 ↓ **81.39%**, q50 ↓ **62.09%**, q80 ↓ **68.04%**; CRPS ↓ **67.70%**; PICP ↑ **+26.82 percentage points** (78.60% vs 51.78%).
- Trade-off insight: 48 and 64-unit models beat 24-unit ones especially on point forecast; 2-layer 48-unit config achieves best CRPS/PICP balance — deeper/wider (64-2) does not help coverage.

## 💡 Limitations & Identified Research Gaps
- Only three discrete quantile models rather than a full predictive distribution; quantile crossing not discussed.
- Single site (one parking lot), single dataset; generalization to other station types untested.
- Authors' stated future work: include **additional input lags** and **extend the forecasting horizon** beyond 24 h.
- No exogenous events (holidays, pricing) beyond calendar/weather features; no comparison against modern deep probabilistic baselines (e.g., DeepAR, diffusion models).
- Thesis gap: clean, reproducible QR-LSTM-Attention benchmark for [[Day_Ahead_Forecasting]] probabilistic EV load forecasting; motivates conformal or distributional extensions.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{matrone2025probabilistic,
  title     = {Probabilistic Forecast of {EV} Charging Demand using Quantile Regression and {LSTM} with Attention Mechanism},
  author    = {Matrone, Silvana and Heydarian Ardakani, Amirhossein and Ogliari, Emanuele and Shirazi, Elham and Leva, Sonia},
  booktitle = {Proceedings of the 16th ACM International Conference on Future and Sustainable Energy Systems (E-Energy '25)},
  address   = {Rotterdam, Netherlands},
  publisher = {ACM},
  year      = {2025},
  pages     = {1005--1007},
  doi       = {10.1145/3679240.3734687}
}
```

## 🔗 Key References & Citation Graph
- Zhu et al. (2019), *Electric Vehicle Charging Load Forecasting: A Comparative Study of Deep Learning Approaches* (Energies) — see [[2019_EV_Load_Forecasting]], ref [6].
- Matrone et al. (2024), *EV supply equipment day-ahead power forecast based on deep learning and the attention mechanism* (IEEE T-ITS) — direct predecessor point-forecast model, ref [4].
- Huber, Dann & Weinhardt (2020), *Probabilistic forecasts of time and energy flexibility in battery electric vehicle charging* (Applied Energy) — quantile-based EV probabilistic forecasting, ref [1].
- Islam et al. (2018), *A Day-Ahead Forecasting Model for Probabilistic EV Charging Loads at Business Premises* (IEEE Trans. Sustain. Energy), ref [2].
- Zhou et al. (2022), *Using Bayesian Deep Learning for Electric Vehicle Charging Station Load Forecasting* (Energies) — Bayesian alternative, cf. [[2023_MetaProbformer_EV_Load]], ref [5].
- KNMI (n.d.), *Daggegevens van het weer in Nederland*, https://www.knmi.nl/nederland-nu/klimatologie/daggegevens — weather source, ref [3].

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_QR_LSTM_Attention_EV_Load_refs]]
