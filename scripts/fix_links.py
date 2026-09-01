"""Fix broken wiki-links in the Obsidian thesis vault.

1. Retargets unambiguous broken links to existing notes.
2. Creates stub notes for frequently-referenced missing concepts.

Usage:
    python scripts/fix_links.py
"""

import re
from pathlib import Path

WIKI = Path(r"C:\Users\chaya\Documents\Obsidian\Thesis\wiki")

# target -> existing note (same meaning, different name)
RETARGETS = {
    # horizons
    "Short_Term": "Short_Term_Forecasting",
    "Long_Term": "Long_Term_Forecasting",
    "Day_Ahead": "Day_Ahead_Forecasting",
    "Spatial_Temporal": "Spatial_Temporal_Forecasting",
    # metrics
    "R2": "R_squared",
    "R2_Score": "R_squared",
    "Quantile_Loss": "Pinball_Loss",
    # datasets
    "Boulder_EV_Charging_Dataset": "Boulder_Colorado",
    "Palo_Alto_EV_Charging_Dataset": "Palo_Alto_EV",
    "Dundee_EV_Charging_Dataset": "Dundee_EV",
    "Perth_EV_Charging_Dataset": "Perth_EV",
    "ACN_Data": "Caltech_ACN",
    "ACN_Dataset": "Caltech_ACN",
    "ACN-Data": "Caltech_ACN",
    "Traffic_Flow": "Traffic",
    "Electricity_Dataset": "Electricity_ECL",   # created below
    "Electricity_Price": "Electricity_Tariff",
    # papers
    "1997_Long_Short_Term_Memory": "1997_Hochreiter_Long_Short_Term_Memory",
    "2020_DeepAR_Probabilistic_Forecasting_with_Autoregressive_Recurrent_Networks":
        "2020_Salinas_DeepAR_Probabilistic_Forecasting",
    # ETT sub-variants -> parent benchmark page
    "ETTh1": "ETT",
    "ETTh2": "ETT",
    "ETTm1": "ETT",
    "ETTm2": "ETT",
    # calendar feature aliases
    "Hour_Of_Day": "Calendar_Features",
    "Day_Of_Week": "Calendar_Features",
    # dataset renames
    "EVnetNL_ElaadNL_Dataset": "ElaadNL",
    "Traffic_Dataset": "Traffic",
    "Traffic_PEMS-SF": "Traffic",
    "Traffic_PEMS": "Traffic",
    "ILI_CDC": "ILI",
    "Weather_Jena": "Weather",
    "ECL_Dataset": "Electricity_ECL",
    "Optuna": "Optuna_TPE",
    # models
    "TFT": "Temporal_Fusion_Transformer",
    "Probformer": "MetaProbformer",
    "Mamba": "Mamba_SSM",
    "Mamba-2": "Mamba_SSM",
    "N-BEATS": "NBEATS",
    "Relative_Humidity": "Humidity",            # created below
}

STUBS = {
    # ---- metrics ----
    "MSE": ("metrics", "metric", "Mean Squared Error (MSE)", """## Definition
$$\\mathrm{MSE} = \\frac{1}{n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2$$

Mean of squared errors. Units are the square of the target's units; the square root ([[RMSE]]) is usually reported instead.

| Property | Value |
|----------|-------|
| Unit | Squared target units |
| Lower is better | Yes |
| Outlier sensitivity | High (squared terms) |
| Related | [[RMSE]], [[MAE]], [[R_squared]] |

## Usage in EV / Load Forecasting Papers
Commonly reported for point forecasts of EV charging load; penalizes large errors more heavily than [[MAE]].

## References
- See paper summaries in [[Papers & Literature]] tagged with MSE.
"""),
    "Accuracy": ("metrics", "metric", "Accuracy", """## Definition
$$\\mathrm{Accuracy} = \\frac{\\text{correct predictions}}{\\text{total predictions}}$$

Fraction of correct predictions, used for classification tasks (e.g. classification-related components in meta-learning papers such as [[MAML]] and [[Reptile]]).

| Property | Value |
|----------|-------|
| Lower/Higher | Higher is better |
| Caution | Misleading on imbalanced classes |

## Usage in EV / Load Forecasting Papers
Appears mainly in classification sub-tasks or event detection rather than load regression.
"""),
    "F1_Score": ("metrics", "metric", "F1 Score", """## Definition
$$F_1 = 2 \\cdot \\frac{\\text{precision} \\cdot \\text{recall}}{\\text{precision} + \\text{recall}}$$

Harmonic mean of precision and recall for classification tasks.

| Property | Value |
|----------|-------|
| Range | 0–1 (higher is better) |
| Related | [[Accuracy]] |

## Usage in EV / Load Forecasting Papers
Used in classification-flavored evaluations (anomaly/event detection, intrusion detection).
"""),
    # ---- models ----
    "RNN": ("models", "model", "Recurrent Neural Network (RNN)", """## Overview
A neural network architecture that processes sequences step by step while maintaining a hidden state. Vanilla RNNs suffer from vanishing/exploding gradients, which motivated [[LSTM]] and GRU.

## Role in EV / Load Forecasting
Baseline sequence model; largely superseded by [[LSTM]], GRU, and Transformer families.

## Key References
- [[1997_Hochreiter_Long_Short_Term_Memory]]
"""),
    "BiLSTM": ("models", "model", "Bidirectional LSTM (BiLSTM)", """## Overview
[[LSTM]] variant that processes the sequence in both forward and backward directions and concatenates the hidden states, giving each time step access to past and future context.

## Role in EV / Load Forecasting
Used in hybrid models (e.g. Transformer+BiLSTM) where full-sequence context is available at inference.
"""),
    "SVR": ("models", "model", "Support Vector Regression (SVR)", """## Overview
Kernel-based regression method from statistical learning theory; fits a function within an epsilon-insensitive tube by solving a convex quadratic program.

## Role in EV / Load Forecasting
Classical machine-learning baseline for station-level load forecasting, often compared against deep models.
"""),
    "ARIMA": ("models", "model", "AutoRegressive Integrated Moving Average (ARIMA)", """## Overview
Classical linear statistical time-series model combining autoregression, differencing (integration), and moving-average terms.

## Role in EV / Load Forecasting
Traditional baseline for load forecasting; reviewed in [[2001_Hippert_Neural_Networks_STLF_Review]]. Seasonal variants include SARIMA.

## Key References
- [[2001_Hippert_Neural_Networks_STLF_Review]]
"""),
    "SARIMA": ("models", "model", "Seasonal ARIMA (SARIMA)", """## Overview
Extension of [[ARIMA]] with seasonal autoregressive and moving-average terms for periodic patterns (daily/weekly cycles).

## Role in EV / Load Forecasting
Statistical baseline for daily/weekly-seasonal EV load profiles.
"""),
    "Adam": ("models", "model", "Adam Optimizer", """## Overview
Adaptive moment estimation gradient-descent optimizer combining momentum and per-parameter adaptive learning rates.

## Key References
- [[2014_Kingma_Adam_Stochastic_Optimization]]

## Role in EV / Load Forecasting
The de-facto default optimizer for training virtually all deep forecasting models in this knowledge base.
"""),
    "Prophet": ("models", "model", "Prophet", """## Overview
Decomposable additive time-series model from Facebook (trend + seasonality + holidays) fit with Bayesian methods.

## Role in EV / Load Forecasting
Interpretable baseline; often used inside hybrid pipelines (see [[VMD_Prophet_LSTM]]).
"""),
    "ANN": ("models", "model", "Artificial Neural Network (ANN)", """## Overview
Generic term for feed-forward multilayer perceptron-style neural networks.

## Role in EV / Load Forecasting
Early baseline for station-level load forecasting, reviewed in [[2015_Raza_Review_AI_Load_Demand]]; superseded by deep sequence models.
"""),
    "Random_Forest": ("models", "model", "Random Forest", """## Overview
Ensemble of bagged decision trees using random feature subsets; robust tabular regressor.

## Role in EV / Load Forecasting
Machine-learning baseline for tabular feature-based demand prediction.
"""),
    "Linear_Regression": ("models", "model", "Linear Regression", """## Overview
Ordinary least-squares linear model — the simplest forecasting baseline.

## Role in EV / Load Forecasting
Baseline against which classical and deep models are compared.
"""),
    "DDPM": ("models", "model", "Denoising Diffusion Probabilistic Model (DDPM)", """## Overview
Generative model trained to reverse a gradual noising process; the foundation of diffusion-based probabilistic forecasters.

## Role in EV / Load Forecasting
Backbone of probabilistic forecasting models such as [[TimeGrad]], [[CSDI]], and [[DiffPLF]].

## Key References
- [[2021_Rasul_TimeGrad_Diffusion_Forecasting]]
- [[2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting]]
- [[2024_Li_DiffPLF_Conditional_Diffusion_EV]]
"""),
    "MAML": ("models", "model", "Model-Agnostic Meta-Learning (MAML)", """## Overview
Meta-learning algorithm learning an initialization that adapts to new tasks with few gradient steps.

## Key References
- [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]]
- [[2018_Nichol_Reptile_First_Order_Meta_Learning]]

## Role in EV / Load Forecasting
Used for few-shot adaptation of forecasters to new charging stations (see [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]]).
"""),
    "Reptile": ("models", "model", "Reptile", """## Overview
First-order meta-learning algorithm from OpenAI; simpler alternative to [[MAML]] that repeatedly moves the initialization toward task-specific solutions.

## Key References
- [[2018_Nichol_Reptile_First_Order_Meta_Learning]]
"""),
    "LogTrans": ("models", "model", "LogSparse Transformer (LogTrans)", """## Overview
Transformer with logarithmic sparse attention reducing complexity to O(L log L) for long sequences.

## Key References
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]]

## Role in EV / Load Forecasting
Precursor of locality-aware attention used in long-term forecasting comparisons ([[Informer]], [[Autoformer]]).
"""),
    "FEDformer": ("models", "model", "FEDformer", """## Overview
Frequency Enhanced Decomposed Transformer; combines seasonal-trend decomposition with attention in the frequency domain via Fourier transforms.

## Role in EV / Load Forecasting
Long-term forecasting benchmark model compared alongside [[Informer]], [[Autoformer]], and [[PatchTST]].
"""),
    "NLinear": ("models", "model", "NLinear", """## Overview
Simple normalized linear model from the [[DLinear]] paper ("Are Transformers Effective for Time Series Forecasting?"); subtracts the last value, applies one linear layer, adds it back.

## Key References
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]]
"""),
    "S4": ("models", "model", "Structured State Space Model (S4)", """## Overview
Deep state-space model with structured (HiPPO-initialized) kernels enabling long-sequence modeling; predecessor of the Mamba family ([[Mamba_SSM]]).

## Role in EV / Load Forecasting
Long-sequence benchmark referenced in Mamba-based forecasting papers.
"""),
    "Multi_Head_Attention": ("models", "model", "Multi-Head Attention", """## Overview
Core mechanism of the Transformer: several scaled dot-product attention heads run in parallel, each attending to different representation subspaces.

$$\\mathrm{Attention}(Q,K,V) = \\mathrm{softmax}\\!\\left(\\frac{QK^\\top}{\\sqrt{d_k}}\\right)V$$

## Key References
- [[2017_Attention_Is_All_You_Need]]
"""),
    "Persistence_Model": ("models", "model", "Persistence (Naive) Baseline", """## Overview
Forecasts future load as the most recent observed value (y_hat(t+h) = y(t)). Essential sanity-check baseline for any forecasting study.

## Role in EV / Load Forecasting
Reported as naive baseline in many EV demand papers; strong for short horizons due to high autocorrelation.
"""),
    "BPTT": ("hyperparameters", "", "Backpropagation Through Time (BPTT)", """## Overview
Training algorithm for recurrent networks: unroll the recurrence over time and apply backpropagation through the unrolled graph. Truncated variants (TBPTT) limit memory use.

## Role in EV / Load Forecasting
Foundation of training [[RNN]]/[[LSTM]]-based load forecasters; discussed in [[1997_Hochreiter_Long_Short_Term_Memory]].
"""),
    # ---- features ----
    "Temperature": ("features", "feature", "Temperature", """## Overview
Ambient temperature, the dominant exogenous weather driver of electricity demand (heating/cooling) and EV battery behavior.

## Usage in EV / Load Forecasting
Standard input feature in weather-aware forecasting models; often paired with [[Humidity]].
"""),
    "Humidity": ("features", "feature", "Humidity", """## Overview
Atmospheric moisture (absolute or relative). Weather covariate affecting cooling loads and comfort-driven charging behavior.

## Usage in EV / Load Forecasting
Input feature in weather-sensitive demand models, usually together with [[Temperature]].
"""),
    "Calendar_Features": ("features", "feature", "Calendar Features", """## Overview
Time-stamp derived inputs: hour-of-day, day-of-week, month, holiday flags, typically encoded cyclically (see [[Cyclical_Encodings]]).

## Usage in EV / Load Forecasting
Near-universal input feature capturing daily/weekly/annual periodicity of charging demand.
"""),
    "Holiday_Flag": ("features", "feature", "Holiday Flag", """## Overview
Binary indicator marking public holidays or special days, which shift commuting and charging patterns.

## Usage in EV / Load Forecasting
Calendar-derived binary input used alongside [[Calendar_Features]].
"""),
    "Holiday_Indicator": ("features", "feature", "Holiday Indicator", """## Overview
Alias form of [[Holiday_Flag]]: binary marker for holiday periods in calendar feature sets.

## Usage in EV / Load Forecasting
Used in day-ahead forecasting studies to distinguish holiday load shapes.
"""),
    "Battery_SOC": ("features", "feature", "Battery State of Charge (SOC)", """## Overview
Remaining battery energy as a fraction of capacity. Determines remaining charging need and session duration.

## Usage in EV / Load Forecasting
Key input for charging-demand and scheduling models (cf. [[State_of_Charge]]).
"""),
    "Positional_Encoding": ("features", "feature", "Positional Encoding", """## Overview
Injects order information into Transformer inputs via sinusoidal functions or learned embeddings, since self-attention is permutation-invariant.

$$PE_{(pos,2i)} = \\sin(pos/10000^{2i/d})$$

## Usage in EV / Load Forecasting
Component of every Transformer-based forecaster ([[Informer]], [[PatchTST]], etc.); related to [[Cyclical_Encodings]] for timestamp features.
"""),
    "Precipitation": ("features", "feature", "Precipitation", """## Overview
Rainfall/snowfall weather covariate influencing travel behavior and EV charging timing.

## Usage in EV / Load Forecasting
Exogenous weather feature in environmental-aware forecasting models.
"""),
    # ---- datasets ----
    "Electricity_ECL": ("datasets", "dataset", "Electricity (ECL) Dataset", """## Overview
UCI Electricity Load Diagrams / Electricity Consumption Label (ECL): hourly electricity consumption of 321 clients from 2012–2014, a standard long-term forecasting benchmark.

access: open
resolution: hourly

## Usage in EV / Load Forecasting
Standard benchmark in LTSF papers ([[Informer]], [[Autoformer]], [[PatchTST]], [[DLinear]], [[TimesNet]]) alongside [[ETT]] and [[Weather]].
"""),
    # ---- round 2 stubs ----
    "Quantile_Regression": ("models", "model", "Quantile Regression", """## Overview
Linear regression of conditional quantiles (pinball loss minimization); the statistical basis of many probabilistic forecasters.

## Role in EV / Load Forecasting
Basis of QRA and quantile-based probabilistic load forecasting ([[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]]); deep variants optimize [[Pinball_Loss]].
"""),
    "VMD": ("models", "model", "Variational Mode Decomposition (VMD)", """## Overview
Signal decomposition method splitting a series into a finite number of band-limited intrinsic mode functions.

## Role in EV / Load Forecasting
Pre-processing step in decomposition-then-forecast pipelines, e.g. [[VMD_Prophet_LSTM]] and ICEEMDAN-based hybrids.
"""),
    "Mamba-3": ("models", "model", "Mamba-3", """## Overview
Third-generation selective state-space sequence model extending [[Mamba_SSM]]; referenced in 2026 EV forecasting studies.

## Key References
- [[2026_Lahoti_Mamba_3_Sequence_Modeling]]
"""),
    "PC-M3": ("models", "model", "PC-M3", """## Overview
Power-clustering Mamba variant for probabilistic forecasting across EV charging clusters.

## Key References
- [[2026_Chen_PC_M3_Mamba_EV_Clusters]]
"""),
    "SGD": ("hyperparameters", "", "Stochastic Gradient Descent (SGD)", """## Overview
First-order gradient optimization; with momentum variants still widely used as baseline optimizer alongside [[Adam]].
"""),
    "Dew_Point": ("features", "feature", "Dew Point", """## Overview
Temperature at which air becomes saturated; humidity-related weather covariate used in load forecasting input sets (cf. [[Humidity]]).
"""),
    "Solar_Energy": ("features", "feature", "Solar Energy / Irradiance", """## Overview
Solar radiation or photovoltaic generation covariate; exogenous driver in energy load forecasting benchmarks (e.g. [[Electricity_ECL]], LSTNet-era datasets).
"""),
    "Wind_Speed": ("features", "feature", "Wind Speed", """## Overview
Weather covariate affecting temperature perception, wind generation, and charging station exposure; common exogenous feature in environmental forecasting models.
"""),
    "Battery_Capacity": ("features", "feature", "Battery Capacity", """## Overview
Total energy storage of an EV battery (kWh), determining maximum charge demand per session; distinct from dynamic [[Battery_SOC]].

## Usage in EV / Load Forecasting
Input to V2G scheduling and charging-session demand models.
"""),
    "MASE": ("metrics", "metric", "Mean Absolute Scaled Error (MASE)", """## Definition
$$\\mathrm{MASE} = \\frac{\\mathrm{MAE}}{\\mathrm{MAE}_{\\text{naive}}}$$

[[MAE]] scaled by the in-sample MAE of a naive seasonal forecast; values < 1 beat the naive baseline. Scale-independent.

## Usage in EV / Load Forecasting
Used in benchmark studies (N-BEATS lineage, TimesNet) for scale-comparable comparison.
"""),
    "GRN": ("models", "model", "Gated Residual Network (GRN)", """## Overview
Gated residual MLP block used as the building core of the [[Temporal_Fusion_Transformer]] for static and temporal processing.
"""),
    "Reformer": ("models", "model", "Reformer", """## Overview
Efficient Transformer using reversible layers and locality-sensitive hashing attention to reduce memory/compute for long sequences.

## Role in EV / Load Forecasting
Long-sequence efficiency benchmark compared in [[Informer]]/[[Autoformer]] studies.
"""),
    "ProbSparse_Attention": ("models", "model", "ProbSparse Attention", """## Overview
Query-sparsity attention from [[Informer]]: each key attends only to the top-u dominant queries measured by KL-divergence-based sparsity, achieving O(L log L) complexity.

## Key References
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]]
"""),
    "SCINet": ("models", "model", "SCINet", """## Overview
Sample Convolution and Interaction Network: downsamples time series into sub-series and exchanges information across them for long-horizon forecasting.
"""),
    "ResNet": ("models", "model", "Residual Network (ResNet)", """## Overview
Convolutional network with skip connections enabling deep architectures; the residual-learning idea underlies many forecasting backbones.
"""),
    "GAT": ("models", "model", "Graph Attention Network (GAT)", """## Overview
Graph neural network applying masked self-attention over neighbor nodes with learned attention weights.

## Role in EV / Load Forecasting
Spatio-temporal component in graph-based EV demand models across station networks (cf. [[GCN]]).
"""),
    "T-GCN": ("models", "model", "Temporal Graph Convolutional Network (T-GCN)", """## Overview
Combination of [[GCN]] spatial filtering with gated temporal convolution/recurrence for spatio-temporal graph forecasting.
"""),
    "ICEEMDAN": ("models", "model", "Improved CEEMDAN (ICEEMDAN)", """## Overview
Adaptive empirical mode decomposition variant adding controlled noise pairs; decomposes non-stationary loads into components for hybrid forecasting pipelines (cf. [[VMD]]).

## Key References
- [[2025_Zheng_BWO_ICEEMDAN_iTransformer]]
"""),
    "Conformal_Prediction": ("guides", "", "Conformal Prediction", """## Overview
Distribution-free framework producing prediction sets/intervals with finite-sample coverage guarantees by calibrating on held-out conformity scores.

## Role in EV / Load Forecasting
Foundation of conformalized quantile regression approaches for probabilistic EV demand intervals:
- [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]]
- [[2024_Zhou_Conformal_Prediction_DER]]
"""),
    "FedAvg": ("hyperparameters", "", "Federated Averaging (FedAvg)", """## Overview
Canonical federated learning algorithm averaging client model weights weighted by sample counts each communication round.
"""),
    "Omniglot": ("datasets", "dataset", "Omniglot Dataset", """## Overview
Handwritten character dataset (1,623 characters, 20 samples each) — standard few-shot classification benchmark used to evaluate [[MAML]] and [[Reptile]].
"""),
}

# targets that should point at newly-created stubs
RETARGETS_AFTER_STUB = {}

TAG_BY_CAT = {
    "metrics": ["metric"],
    "models": ["model"],
    "datasets": ["dataset"],
    "features": ["feature"],
    "hyperparameters": ["hyperparameter", "optimization"],
}


def apply_retargets(text):
    changed = 0
    for old, new in RETARGETS.items():
        pattern = re.compile(r"\[\[" + re.escape(old) + r"(?=[]|#|])")
        text, n = pattern.subn("[[" + new, text)
        changed += n
    return text, changed


def main():
    notes = sorted(WIKI.rglob("*.md"))
    total_links_fixed = 0
    files_changed = 0
    for note in notes:
        text = note.read_text(encoding="utf-8", errors="replace")
        new_text, n = apply_retargets(text)
        if n:
            note.write_text(new_text, encoding="utf-8")
            total_links_fixed += n
            files_changed += 1
    print(f"Retargeted {total_links_fixed} links across {files_changed} files")

    created = []
    for name, (folder, ftype, title, body) in STUBS.items():
        path = WIKI / folder / f"{name}.md"
        if path.exists():
            print(f"SKIP (exists): {path.name}")
            continue
        tags = TAG_BY_CAT.get(folder, []) + [name.lower()]
        front = (
            "---\n"
            f"type: {ftype}\n"
            f'name: "{title}"\n'
            "category: Stub (auto-generated)\n"
            "status: needs-review\n"
            f"tags:\n" + "".join(f"  - {t}\n" for t in tags) +
            "---\n\n"
        )
        path.write_text(front + body.strip() + "\n", encoding="utf-8")
        created.append(path.name)
    print(f"Created {len(created)} stub notes:")
    for c in created:
        print(f"  + {c}")


if __name__ == "__main__":
    main()
