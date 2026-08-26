---
type: paper
title: "Benchmarking Time Series Foundation Models for Short-Term Household Electricity Load Forecasting"
authors: [Marcel Meyer, David Zapata Gonzalez, Sascha Kaltenpoth, Oliver Müller]
year: 2025
journal_conference: "IEEE Access"
doi_url: "https://doi.org/10.1109/ACCESS.2025.3648056"
models_used: ["[[Chronos]]", "[[Chronos-Bolt]]", "[[TimesFM]]", "[[TimesFM_2.0]]", "[[LagLlama]]", "[[Moirai]]", "[[Time-MoE]]", "[[Sundial]]", "[[PatchTST]]", "[[VanillaTransformer]]", "[[iTransformer]]", "[[Temporal_Fusion_Transformer]]", "[[SeasonalAverage]]"]
datasets_used: ["[[Lower_Saxony_Dataset]]", "[[Southern_Germany_Dataset]]", "[[IDEAL_Dataset]]", "[[REFIT_Dataset]]"]
features_used: ["[[Household_Electricity_Consumption]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[MAE]]", "[[MSE]]", "[[APNE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Benchmarking Time Series Foundation Models for Short-Term Household Electricity Load Forecasting

## 🎯 Main Objective & Contribution
- **Research question**: "Can zero-shot TSFMs match the capabilities of state-of-the-art trained-from-scratch Transformers in forecasting household electricity load?"
- **Contribution**: First multi-dataset, time-series-cross-validation benchmark of zero-shot Time Series Foundation Models ([[Chronos]], [[Chronos-Bolt]], [[TimesFM]], [[TimesFM_2.0]], [[LagLlama]], [[Moirai]], [[Time-MoE]], [[Sundial]]) against trained-from-scratch (TFS) Transformers ([[PatchTST]], [[VanillaTransformer]], [[iTransformer]], [[Temporal_Fusion_Transformer]]) on univariate household STLF.
- **Key methodological contributions**:
  - Contamination-aware dataset selection: excludes datasets present in TSFM pre-training corpora (Electricity Dataset, Ausgrid Solar Home, London Smart Meters, Portuguese Household); rejects BuildingsBench and TimeGPT-1 due to undisclosed training data → leakage risk.
  - Leakage-safe global train-test split: a single split date per dataset chosen via percentile logic over household max dates (0.25th percentile of max dates; 0.8th percentile of possible time points), preventing cross-household leakage of global patterns (e.g., Covid-19).
- **Finding**: Zero-shot TSFMs are comparable to — and with longer input sizes (96/168 h) often better than — TFS Transformers, while requiring no domain-specific training.

## 🧠 Methodology & Model Architecture
- **Benchmark design**: 6 zero-shot TSFMs (official weights, no fine-tuning) vs 4 TFS Transformers (implemented in NeuralForecast, trained globally on all households' training splits) vs statistical baselines ([[SeasonalAverage]] seasonality=24, Naive Forecast). No extensive hyperparameter tuning — default parameters from original papers.
- **Training/evaluation protocol**: time series cross-validation with calibration window — TFS models retrained from scratch on most recent 365 days before each rolling split date, moved forward by horizon length each fold. All models cut to exact input size before prediction. Input sizes ∈ {24, 96, 168} h × horizons ∈ {24, 96, 168} h; >2 million training points, >6 million evaluated forecast points per setup (0.2% data reduction where some models failed).
- **Household-aggregated MAE metric** ($MAE_h$, Eq. 1) — averages per-household mean absolute errors to prevent long-series households dominating:
$$MAE_h = \frac{1}{h}\sum_{h=1}^{h}\left(\frac{1}{n}\sum_{i=1}^{n}|y_{h,i} - \hat{y}_{h,i}|\right)$$
where $\hat{y}_{h,i}$ / $y_{h,i}$ = prediction/actual for household $h$, prediction $i$ of $n$; $h$ = number of households. Same aggregation gives $MSE_h$.
- **[[APNE]]** (adjusted p-norm error per house, Haben et al.): mitigates the "double penalty" effect on temporally displaced peaks by minimizing error over a restricted temporal permutation within adjustment window $w$; used with p-norm 4, $w$ from 3→1 (hourly instead of half-hourly data). MAPE/SMAPE discarded (near-zero consumption values).
- **Statistical testing**: Friedman omnibus test → pairwise Wilcoxon signed-rank tests with Holm–Bonferroni correction (α = 0.05, 0.01); average rank computed from per-household rankings on $MAE_h$.
- **Preprocessing**: gaps longer than 3 consecutive days truncated (longest clean segment kept); remaining internal missing values linearly interpolated (training only — evaluation set untouched); end-of-series gaps filled from t−24h; predictions and ground truth normalized by mean/std per series.
- TSFM specifics: LagLlama run with RoPe scaling (inputs > context length 32); Moirai originally designed for context 1000.

## 📊 Dataset & Input Features
- Four real-world evaluation datasets (>300 households total), hourly aggregated, kWh, univariate net grid import:

| Dataset | Location | Households | Period | Mean | Median | Std |
|---|---|---|---|---|---|---|
| [[IDEAL_Dataset]] | Edinburgh area, UK | 254 | 10/08/2016–01/07/2018 | 0.3713 | 0.2220 | 0.4395 |
| [[Lower_Saxony_Dataset]] | near Hameln, DE | 34 | 02/05/2018–31/12/2020 | 0.3417 | 0.2337 | 0.3411 |
| [[Southern_Germany_Dataset]] | Konstanz, DE | 6 | 15/04/2015–06/09/2017 | 0.4035 | 0.2900 | 2.6643 |
| [[REFIT_Dataset]] | Loughborough area, UK | 20 | 17/09/2013–10/07/2015 | 0.5151 | 0.3279 | 0.5197 |

- Southern Germany test set: 16,959 observations; post-July-2017 constant values dropped. Lower Saxony: active power all phases; district-heating pump meters excluded; 4 PV households removed (ambiguous net metering). One Konstanz house has an EV (filtered out by taking grid-total import). IDEAL included but Moirai/Sundial/Time-MoE excluded there (pre-training contamination).
- **Dataset URLs / DOIs** (from references):
  - Electricity Dataset (excluded, in pre-training): UCI ElectricityLoadDiagrams20112014 (Trindade, 2015)
  - Ausgrid Solar Home Dataset (excluded): https://www.tandfonline.com/doi/full/10.1080/14786451.2015.1100196
  - London Smart Meters (excluded): https://data.london.gov.uk/dataset/smartmeter-energy-use-data-in-london-households
  - Southern Germany: Open Power System Data household package — https://data.open-power-system-data.org/household_data/2020-04-15/
  - Lower Saxony: Schlemminger et al., Scientific Data — https://doi.org/10.1038/s41597-022-01156-1
  - REFIT: Murray et al., Scientific Data — https://doi.org/10.1038/sdata.2016.122
  - IDEAL: Pullinger et al., Scientific Data — https://www.nature.com/articles/s41597-021-00921-y
  - Danish Energinet (excluded): https://www.energidataservice.dk/tso-electricity/PrivIndustryConsumptionHour
- **Code availability**: full preprocessing/training/evaluation code at https://anonymous.4open.science/r/benchmarking_tsfm_household_load_forecasting-DF75/
- EDA: strong 24-h autocorrelation, weekly + seasonal cycles, non-stationary, positive skew; winter consumption peak.

## 📈 Performance & Results
- Overall best models by dataset (normalized $MAE_h$):

| Model | IDEAL | Lower Saxony | REFIT | S. Germany |
|---|---|---|---|---|
| Chronos-Bolt | 0.513 | **0.490** | **0.528** | **0.478** |
| TimesFM | 0.514 | 0.491 | 0.530 | 0.478 |
| TimesFM 2.0 | **0.509** | 0.493 | 0.532 | 0.485 |
| Sundial | —* | 0.499 | 0.529 | 0.497 |
| Time-MoE | —* | 0.533 | 0.566 | 0.521 |
| PatchTST (best TFS) | 0.516 | 0.494 | 0.535 | 0.499 |
| iTransformer | 0.589 | 0.588 | 0.648 | 0.598 |
| TFT | 0.577 | 0.580 | 0.635 | 0.616 |
| VanillaTransformer | 0.549 | 0.556 | 0.603 | 0.573 |
| SeasonalAverage | 0.609 | 0.572 | 0.577 | 0.539 |
| Naive-Forecast | 0.703 | 0.608 | 0.733 | 0.718 |

\*Excluded (dataset in pre-training data).
- Chronos-Bolt is best on $MAE_h$ across Lower Saxony, REFIT, Southern Germany; TimesFM 2.0 best on IDEAL; PatchTST best on IDEAL $MSE_h$ (0.969). Best $MSE_h$: Time-MoE & Sundial (e.g., 0.892/0.894 Lower Saxony). Best $APNE_h$: Time-MoE (1.563 S. Germany) & Sundial (1.594).
- Input-size effect: at input size 24, PatchTST ranks best (rank 2.36 @ horizon 24); TSFMs overtake it at input sizes 96 and 168 — Chronos-Bolt rank 2.05–2.62, TimesFM 2.0 rank 2.18–2.95, Sundial ~3.25–3.54 vs PatchTST 3.73–4.76. LagLlama (best rank 7.91) and Moirai (up to rank 14.00, MSE>10 on REFIT) fail to beat even SeasonalAverage.
- Statistical robustness: >99% of pairwise comparisons significant (p<0.05); <1.5% remain at α=0.01.
- SeasonalAverage beats several deep models at 96 h/168 h horizons (strong daily pattern).

## 💡 Limitations & Identified Research Gaps
- Possible cross-domain temporal information leakage: TSFMs pre-trained on data covering the same calendar period may encode global patterns (Covid-19, geopolitical crises); only solvable with post-training collection dates. Unaddressed in original TSFM papers.
- No hyperparameter tuning of TFS baselines (compute constraints) could understate their performance.
- Restricted input sizes (max 168 h) disadvantage architecture-dependent models (LagLlama's lags, Moirai's context 1000); longer contexts unexplored.
- Univariate only — multivariate extension with weather covariates proposed as future work; fine-tuning and energy-domain-pre-trained foundation models identified as promising directions.
- TSFMs predict conservatively, underestimating extreme load peaks relevant for grid capacity (small APNE gap to baseline).

## 📚 BibTeX & Citation Reference
```bibtex
@article{meyer2025benchmarking,
  author  = {Meyer, Marcel and Zapata Gonz{\'a}lez, David and Kaltenpoth, Sascha and M{\"u}ller, Oliver},
  title   = {Benchmarking Time Series Foundation Models for Short-Term Household Electricity Load Forecasting},
  journal = {IEEE Access},
  volume  = {13},
  year    = {2025},
  doi     = {10.1109/ACCESS.2025.3648056}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — VanillaTransformer base architecture [8]
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — SOTA TFS baseline [36]
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — TFS baseline [37]
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — LSTM+attention TFS baseline [38]
- [[2021_Rasul_TimeGrad_Diffusion_Forecasting]] — same first author as [[LagLlama]]
- Related vault papers: [[2025_Han_Vertical_Federated_EGAT_LSTM]] and [[2025_Zhu_Personalized_Federated_Learning]] (household-level load forecasting), [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] (LLM-based EV forecasting)
