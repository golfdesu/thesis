---
type: paper
title: "Electric Vehicle Charging Load Forecasting: An Experimental Comparison of Machine Learning Methods"
authors: [Iason Kyriakopoulos, Yannis Theodoridis]
year: 2026
journal_conference: "arXiv preprint arXiv:2512.17257 [cs.LG] (v2, 31 Mar 2026; dated April 1, 2026), University of Piraeus"
doi_url: "https://doi.org/10.48550/arXiv.2512.17257"
models_used: ["[[ARIMA]]", "[[XGBoost]]", "[[GRU]]", "[[LSTM]]", "[[Transformer]]"]
datasets_used: ["[[Palo_Alto_EV]]", "[[Boulder_Colorado]]", "[[Dundee_EV]]", "[[Perth_EV]]"]
features_used: ["[[Historical_Load]]", "[[Calendar_Features]]", "[[Holiday_Indicator]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Station_ID_One_Hot]]", "[[Region_ID_One_Hot]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Electric Vehicle Charging Load Forecasting: An Experimental Comparison of Machine Learning Methods

## 🎯 Main Objective & Contribution
A systematic, reproducible experimental benchmark — not a new model — comparing five forecasting families (**ARIMA**, **XGBoost**, **GRU**, **LSTM**, **Transformer**) for EV charging energy consumption (kWh) across:
- **Three temporal resolutions**: short-term (10–30 min ahead, 10-min steps), mid-term (2–8 h ahead, 2-h steps), long-term (1–5 days ahead, 1-day steps);
- **Three spatial aggregation levels**: station, region, city;
- **Four real-world datasets**: Palo Alto (USA), Boulder (USA), Dundee (UK), Perth (Australia).

Contributions: (i) unified multi-scale EV charging benchmark; (ii) consistent/reproducible evaluation protocol with public codebase and dataset links; (iii) systematic comparison showing model rankings change with horizon and spatial scale; (iv) family-level insights — Transformers dominate short-term regional/city forecasts (MAE 10–15% lower than ARIMA/XGBoost), GRU/LSTM consistently win mid- and long-term (in some mid-term city cases >50% MAE reduction vs ARIMA); XGBoost competitive only locally; ARIMA fails to scale to longer horizons/coarser aggregations.

## 🧠 Methodology & Model Architecture
**Problem formulation (EV Charging Load Forecasting Problem):**
$$X = \{x_1, x_2, \ldots, x_T\}$$
where $x_t$ is total energy consumed at step $t$; the goal is to predict:
$$\hat{X} = \{\hat{x}_{T+1}, \hat{x}_{T+2}, \ldots, \hat{x}_{T+H}\}$$
over forecasting horizon $H$ (minutes / hours / days regimes).

**Two modeling strategies:**
1. **Multi-station (global) learning** for XGBoost, GRU, LSTM, Transformer: one model per city × temporal resolution on pooled station data; inputs combine one-hot station/region IDs with calendar/holiday indicators; z-score normalization from training partition; **recursive walk-forward multi-step forecasting** (predictions fed back as lag inputs).
2. **Per-station univariate ARIMA**: restricted grid search $p,q \in \{0,1,2\}$, $d \in \{0,1\}$ selected by lowest AIC; training window capped at 2,048 points (10-min), 1,536 (hourly), 730 (daily); naïve persistence substituted when estimation fails.

**Hyperparameters (fixed, not tuned, for comparability):**
- XGBoost: device=cuda, tree_method=hist, LR 0.05, max_depth 8, subsample 0.8, colsample_bytree 0.8, L2 = 1.0, up to 2000 rounds, early stopping patience 200.
- GRU/LSTM: sequence length = number of lag features, 64 hidden units, Adam ($10^{-3}$), batch size 2048, ≤200 epochs, early stopping patience 20, TensorFlow mixed precision.
- Transformer: d_model=128, 8 attention heads, 4 layers, FFN dim 256, dropout 0.1; same optimizer/batch/early-stopping settings.
- Stack: Python 3.10 (preprocessing) / 3.8 (modeling); pandas, numpy, statsmodels, scikit-learn, tensorflow; single NVIDIA A100 GPU node with 1 TB RAM.

Evaluation protocol: per-dataset MAE and RMSE at every (dataset × spatial level × horizon) combination; MAPE avoided (instability near zero values), R² excluded (poor interpretability in nonlinear forecasting).

## 📊 Dataset & Input Features
Session-level charging data aggregated to fixed **10-minute intervals per station** (energy summed over sessions overlapping each interval), then resampled hourly/daily.

| Dataset | Time range | Stations | Regions | Session records |
|---|---|---|---|---|
| Palo Alto, CA (USA) | Jul 2011 – Dec 2020 | 47 | 3 | 259,415 |
| Boulder, CO (USA) | Jan 2018 – Mar 2021 | 27 | 5 | 24,081 |
| Dundee (UK) | Jan 2017 – Dec 2018 | 67 | 34 | 52,752 |
| Perth (Australia) | Jan 2016 – Dec 2019 | 36 | 22 | 66,664 |

- Preprocessing: retained session start/end times, kWh per session, station ID, regional grouping (ZIP/site label); dropped auxiliary fields (port type, GHG saved, session/user ID); removed rows with missing/invalid entries (negative energy, end < start); timezone standardization to UTC.
- Features: calendar variables (holidays, weekends, day-of-week, month-of-year), multiple lagged target versions at resolution-appropriate offsets, one-hot station/region encodings (multi-station models); z-score normalization; forecasts evaluated in normalized domain (no inverse transform).
- **Dataset source (all four cities)**: https://github.com/yvenn-amara/ev-load-open-data (Amara, "EV load open data," GitHub, 2023)
- **Codebase / full pipeline**: https://github.com/DataStories-UniPi/electric-vehicle-charging-load-forecasting

## 📈 Performance & Results
All values are MAE/RMSE in the normalized domain (Tables 2–4 of the paper). Key findings:

**Short-term (10–30 min):**
- Perth: LSTM best everywhere (station MAE 0.43–0.46, RMSE < 1.1; e.g., city MAE 7.97@10min → 7.27@30min vs Transformer 42.94 → 42.90).
- Boulder: Transformer best at all levels (station MAE ≈ 0.21 vs ARIMA 0.26; city MAE 2.71→2.65).
- Dundee: Transformer dominates region/city (city MAE 14.52→13.22); ARIMA lowest station MAE but Transformer lower RMSE.
- Palo Alto: Transformer best region/city (city MAE 12.84→12.77); XGBoost best station level (MAE ≈ 0.87, RMSE ≈ 1.01).

**Mid-term (2–8 h):**
- GRU lowest errors consistently in Dundee and Perth at all horizons/levels (e.g., Perth city MAE 8.17→6.54).
- Palo Alto: Transformer best region+city (city MAE 6.02@2h → 4.99@8h).
- Boulder: ARIMA best station/regional; LSTM best city (city MAE 2.91@2h → 2.39@8h).
- XGBoost only competitive at Palo Alto station level (lowest RMSE there).
- Counter-intuitive trend: errors decrease as horizon grows due to temporal aggregation smoothing volatility.

**Long-term (1–5 days):**
- Boulder: Transformer lowest MAE at all levels (city MAE 3.47@1d → 2.63@5d).
- Palo Alto: LSTM best station/regional; Transformer lowest city MAE (11.59→10.62), LSTM lowest city RMSE (15.62→14.90).
- Dundee: **Transformer collapses** — city MAE ≈ 93, RMSE ≈ 106–107 (order of magnitude worse); GRU best city (MAE 23.94@1d → 21.48@5d).
- Perth: GRU lowest MAE at all levels; ARIMA lowest city RMSE (22.00@1d → 18.60@5d).

**Transformer failure diagnosis (Dundee):** largest station count (67) and regions (34) but fewest relative records (52,752) → after daily aggregation very short, zero-inflated histories per spatial unit; high-capacity encoder overfits and accumulates recursive multi-step errors, while GRU/LSTM's stronger local-temporal-continuity inductive bias is more robust. Recommendation: Transformers need both long time spans and large effective sample size per spatial unit; otherwise prefer recurrent models.

## 💡 Limitations & Identified Research Gaps
- Input space deliberately restricted to historical load + calendar features; exogenous drivers (weather, electricity prices, traffic, events) unmodeled → reported scores are a **lower bound**.
- Only widely used baselines; excludes GNNs, decomposition hybrids, EV-specific global/foundation models ([29][30] reviewed only) ↔ benchmark positioning against [[2024_Bampos_EV_Load_Forecasting_DAM]], [[2025_Meyer_Benchmark_Foundation_Models]], [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]].
- Recursive multi-step forecasting introduces error accumulation, hurting some architectures (Transformers on sparse data like Dundee) disproportionately.
- Fixed hyperparameters trade peak performance for comparability.
- Future work: hyperparameter optimization/deeper architectures; exogenous variables; explainable AI (XAI); transfer learning across cities (explicitly proposed as follow-up, connecting to [[2024_Ali_MQ_TCN_Transfer_Learning_EV]], [[2023_Huang_MetaProbformer_EV_Load]]).

## 📚 BibTeX & Citation Reference
```bibtex
@article{kyriakopoulos2026evcomparison,
  title   = {Electric Vehicle Charging Load Forecasting: An Experimental Comparison of Machine Learning Methods},
  author  = {Kyriakopoulos, Iason and Theodoridis, Yannis},
  journal = {arXiv preprint arXiv:2512.17257},
  year    = {2026},
  url     = {https://arxiv.org/abs/2512.17257},
  note    = {University of Piraeus, Greece; v2 dated April 1, 2026}
}
```

## 🔗 Key References & Citation Graph
- Koohfar et al. (2023), Transformer-based EV charging demand on 5 years of Boulder data, Sustainability 15(3):2105 → vault: [[2023_Koohfar_Transformer_EV_Demand]].
- Zhu et al. (2019), deep learning (LSTM/GRU/ANN) EV load comparison, Appl. Sci. 9(9):1723 → vault: [[2019_Zhu_EV_Load_Forecasting]] / [[2019_Short_Term_Load_Forecasting_for_Electric_Vehicle_Charging_Stations_Based_on_Deep_Learning_Approaches]].
- Louie (2017), SARIMA aggregated station load, Electr. Power Compon. Syst. 45(14):1498–1511.
- Lu et al. (2018), Random Forest EV charging load, Energies 11(11):3207.
- Unterluggauer et al. (2021), multivariate multi-step LSTM, Finland, IET Electr. Syst. Transp. 11(4):405–419.
- Ma & Faye (2021), hybrid LSTM occupancy prediction, Dundee, arXiv:2106.04986.
- Hüttel et al. (2021), deep spatio-temporal (TGCN) forecasting, arXiv:2106.10940.
- Zhang et al. (2024), GNN spatial-temporal station load, J. Intell. Fuzzy Syst. 46(4).
- Wei et al. (2023), GA-Prophet-LSTM station load, J. Phys.: Conf. Ser. 2592:012092.
- van Etten et al. (2024), global N-HiTS/Transformer/ARIMA cross-city benchmark (London, Palo Alto, Perth, Boulder), VEHITS 2024:40–51 — closest related benchmark; complementary (transferability focus vs this paper's horizon/scale focus).
- Manai et al. (2024), real-time availability (classification) forecasting, Procedia Comput. Sci. 246:930–939.
- Mystakidis et al. (2025), traffic/weather-aware LogZI regression, Trondheim, Int. J. Mach. Learn. Cybern. 16:6737–6763.
- Cho et al. (2014), GRU, arXiv:1406.1078; Hochreiter & Schmidhuber (1997), LSTM → vault: [[1997_Hochreiter_Long_Short_Term_Memory]]; Vaswani et al. (2017), Transformer → vault: [[2017_Attention_Is_All_You_Need]]; Chen & Guestrin (2016), XGBoost, KDD:785–794.
- Amara (2023), EV load open data: https://github.com/yvenn-amara/ev-load-open-data
- Funding: Horizon Europe grant No. 101070416 (Green.Dat.AI, https://greendatai.eu); University of Piraeus Research Center.
