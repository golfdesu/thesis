"""Round 3: comprehensive broken-link cleanup for the thesis vault.

1. RAW_FIXES      - literal/regex repairs of malformed links
2. RETARGETS      - alias links -> existing notes
3. CURATED_STUBS  - new notes with hand-written overviews
4. AUTO_STUBS     - generic notes for every remaining broken target
                    referenced >= MIN_AUTO_COUNT times

Run repeatedly until satisfied:
    python scripts/fix_links_round3.py
"""

import html
import re
from collections import Counter
from pathlib import Path

WIKI = Path(r"C:\Users\chaya\Documents\Obsidian\Thesis\wiki")
MIN_AUTO_COUNT = 2

WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

RAW_FIXES = [
    # malformed queueing link (contains mojibake)
    (re.compile(r"\[\[M/G/[^\]]*\]\]"), "[[Queuing_Model|M/G/\u221e queueing model]]"),
    (re.compile(r"\[\[\[Charging_Demand_Series\]\]"),
     "[[EV_Charging_Demand|Charging demand series]]"),
    (re.compile(r"\[\[Charging_Demand_Series\]\]"),
     "[[EV_Charging_Demand|Charging demand series]]"),
    (re.compile(r"\[\[Stationary/Non-stationary Transformers\]\]"),
     "[[Stationary_Transformer|Stationary / Non-stationary Transformers]]"),
]

# targets that should NOT get stub notes (category-style / meta links)
SKIP_TARGETS = {
    "papers & literature",
    "hyperparameters",
}

RETARGETS = {
    # ---------- datasets ----------
    "Palo_Alto_EV_Charging": "Palo_Alto_EV",
    "Palo_Alto_EV_Charging_Station_Usage_Dataset": "Palo_Alto_EV",
    "Palo_Alto_EV_Usage": "Palo_Alto_EV",
    "Boulder_EV_Dataset": "Boulder_Colorado",
    "Boulder_EV_Charging_Stations_Dataset": "Boulder_Colorado",
    "Boulder_CO_EV": "Boulder_Colorado",
    "Boulder_City_EV_Charging_Dataset": "Boulder_Colorado",
    "Perth_UK_EV": "Perth_EV",
    "Perth_ChargePlace_Scotland": "ChargePlace_Scotland",
    "Crowdcharge": "CrowdCharge_EV",
    "Paris_Belib": "Paris_Belib_EV",
    "Pecan_Street_Dataport": "Pecan_Street",
    "REFIT_Dataset": "REFIT",
    "Caltech_ACN_Dataset": "Caltech_ACN",
    "JPL_ACN_Dataset": "Caltech_ACN",
    "Beijing_Fast_Charging_Dataset": "Beijing_Fast_Charging",
    "Kaggle_Dallas_Port": "Dallas_Port_EV",
    "Shenzhen_EV_Charging_Dataset": "Shenzhen_ST_EVCDP",
    "Shenzhen_PEV_Aggregator_Dataset": "Shenzhen_ST_EVCDP",
    "Shenzhen_Core_Station_Dataset": "Shenzhen_ST_EVCDP",
    "Shenzhen_PEV_Charging_Station_Dataset": "Shenzhen_ST_EVCDP",
    "Real_world_EV_charging_dataset": "Real_World_EV_DC_Charging",
    "Real_World_EV_Charging_Load_Profiles": "Real_World_EV_DC_Charging",
    "UrbanEV": "UrbanEV_Dataset",
    "ElaadNL_EV": "ElaadNL",
    "NYISO_LBMP_Dataset": "NYISO",
    "CAISO_Electricity_Prices": "CAISO",
    "National_Household_Travel_Survey": "NHTS_2009",
    "ElectricityLoadDiagrams": "Electricity_ECL",
    # weather data sources -> Weather hub
    "Weather_NOAA": "Weather",
    "NOAA_Weather_Data": "Weather",
    "ECMWF_Weather_Data": "Weather",
    "Meteostat_Weather": "Weather",
    "KNMI_Weather_Data": "Weather",
    "Open-Meteo_Weather_Data": "Weather",
    "Boulder_Weather_Data": "Weather",
    "ERA5_Reanalysis": "Weather",
    "NREL_SAM_Weather": "Weather",
    "ENTSOE_Transparency_Platform": "Weather",
    # LTSF benchmark aliases
    "ETT_Dataset": "ETT",
    "ILI_Dataset": "ILI",
    "M4_Competition": "M4",
    "M4_Dataset": "M4",
    "M3_Dataset": "M3",
    "TOURISM_Dataset": "Tourism",
    "Exchange_Rate": "Exchange",
    "Exchange_Rates": "Exchange",
    "Exchange_Dataset": "Exchange",
    "Traffic_PEMS_SF_Dataset": "Traffic",
    "METR-LA": "Traffic",
    "PEMS-BAY": "Traffic",
    "PEMS08": "Traffic",
    "TrafficL_PeMS": "Traffic",
    "GEFCom2012_RES_Data": "GEFCom2014",
    "Taxi_NYC": "NYC_Taxi",
    "Permuted_MNIST": "MNIST",
    "Sequential_MNIST": "MNIST",
    "Wind": "Wind_Speed",
    "Humidity_Forecast": "Humidity",
    "Lagged_Temperature": "Temperature",
    "Temperature_Max_Min": "Temperature",
    "Wet_Bulb_Temperature": "Temperature",
    "Wet_Bulb": "Temperature",
    "Dry_Bulb_Temperature": "Temperature",
    "Sensible_Temperature": "Temperature",
    "Air_Temperature": "Temperature",
    "Ambient_Temperature": "Temperature",
    "Daily_Temperature": "Temperature",
    "Average_Temperature": "Temperature",
    "Daily_Average_Temperature": "Temperature",
    "Daily_Moving_Average_Temperature": "Temperature",
    # calendar / temporal feature aliases
    "Calendar_Encoding": "Calendar_Features",
    "Calendar_Covariates": "Calendar_Features",
    "Calendar_Variables": "Calendar_Features",
    "Calendar_Information": "Calendar_Features",
    "Calendar_Timestamps": "Calendar_Features",
    "Timestamp_Calendar_Features": "Calendar_Features",
    "Temporal_Features": "Calendar_Features",
    "Time_Covariates": "Calendar_Features",
    "Time_Index_Features": "Calendar_Features",
    "Time_Aware_Features": "Calendar_Features",
    "Day_of_Week": "Calendar_Features",
    "Day_of_Week_Flag": "Calendar_Features",
    "Weekday": "Calendar_Features",
    "Weekday_Flag": "Calendar_Features",
    "Weekday_Indicator": "Calendar_Features",
    "Weekend_Indicator": "Calendar_Features",
    "Week_of_Year": "Calendar_Features",
    "Month_Of_Year": "Calendar_Features",
    "Month": "Calendar_Features",
    "Season": "Calendar_Features",
    "Day_Type": "Calendar_Features",
    "Day_Type_Dummy": "Calendar_Features",
    "Cyclical_Time_Features": "Cyclical_Encodings",
    "Temporal_Feature_Encoding": "Cyclical_Encodings",
    "Cyclic_Temporal_Indicator": "Cyclical_Encodings",
    "Sine_Cosine_Time_Encoding": "Cyclical_Encodings",
    "Binary_Holiday": "Holiday_Flag",
    "Binary_Working_Day": "Holiday_Flag",
    "School_Holidays": "Holiday_Flag",
    "Working_Day_Flag": "Holiday_Flag",
    "Workday_Indicator": "Holiday_Flag",
    # lag / window features
    "Lagged_Load": "Historical_Load",
    "Historical_Load_Lag": "Historical_Load",
    "Historical_Load_Lags": "Historical_Load",
    "Historical_Lags": "Lag_Features",
    "Lagged_Values": "Lag_Features",
    "Look_Back_Window": "Lookback_Window",
    "Time_Step_Lookback": "Lookback_Window",
    # SoC family
    "SOC": "State_of_Charge",
    "Arrival_SoC": "State_of_Charge",
    "Starting_SOC": "State_of_Charge",
    "Initial_SOC": "State_of_Charge",
    "Target_Departure_SoC": "State_of_Charge",
    "SOC_At_Arrival_Departure": "State_of_Charge",
    # charging session features
    "Maximum_Charging_Power": "Charging_Power",
    "Charging_Rate_kW": "Charging_Power",
    "Charger_Power_Rating": "Connector_Power_Rating",
    "Charge_Duration": "Charging_Duration",
    "Charging_Duration_Log": "Charging_Duration",
    "Charging_Time": "Charging_Duration",
    "Arrival_Time": "Arrival_Departure_Time",
    "Departure_Time": "Arrival_Departure_Time",
    "EV_Arrival_Departure_Time": "Arrival_Departure_Time",
    "EV_Arrival_Departure_Times": "Arrival_Departure_Time",
    "Parking_Time": "Arrival_Departure_Time",
    "Transaction_Start_Time": "Arrival_Departure_Time",
    "Connector_Occupancy_Time": "Station_Occupancy",
    "Charging_Occupancy": "Station_Occupancy",
    "Pile_Occupancy_Demand": "Station_Occupancy",
    "Station_Availability": "Station_Occupancy",
    "Arrival_Rate": "EV_Arrival_Rate",
    "Plug_in_Probability": "EV_Arrival_Rate",
    "Charging_Energy_kWh": "EV_Charging_Demand",
    "Required_Charging_Energy": "EV_Charging_Demand",
    "Charging_Load_Sequence": "Historical_Load",
    "Historical_Charging_Demand": "Historical_Load",
    "Historical_Charging_Load": "Historical_Load",
    "Historical_EV_Charging_Load": "Historical_Load",
    "Historical_EV_Load": "Historical_Load",
    "Hourly_Load": "Historical_Load",
    "Minute_Level_Load": "Historical_Load",
    "Historical_Charging_Volume": "Historical_Load",
    "Historical_Charging_Power": "Historical_Load",
    "Hourly_Charging_Events": "EV_Charging_Demand",
    "EV_Load_Forecasting": "EV_Charging_Demand",
    "EV_Charging_Load_Forecasting": "EV_Charging_Demand",
    "EV_Load_Curve": "EV_Charging_Demand",
    "Average_Weekly_EV_Demand": "EV_Charging_Demand",
    "V2G_Scheduling": "V2G",
    "Grid_Topology_Affiliation_Matrix": "Grid_Topology",
    "Graph_Adjacency_Matrix": "Adjacency_Matrix",
    "Distance_Based_Adjacency_Matrix": "Adjacency_Matrix",
    "Dynamic_Adjacency_Matrix": "Adjacency_Matrix",
    "Gaussian_Kernel_Adjacency": "Adjacency_Matrix",
    "MAD_Similarity": "Adjacency_Matrix",
    "DTW_Similarity": "Adjacency_Matrix",
    # attention / transformer components
    "Scaled_Dot_Product_Attention": "Multi_Head_Attention",
    "ProbSparse_Queries": "ProbSparse_Attention",
    "VanillaTransformer": "Transformer",
    "Transformer_Encoder": "Transformer",
    "Residual_Connections": "Transformer",
    "Layer_Normalization": "Transformer",
    "Convolutional_Network": "CNN",
    "Fully_Connected_Network": "MLP",
    # LSTM internals
    "Input_Gate": "LSTM",
    "Output_Gate": "LSTM",
    "Cell_State": "LSTM",
    "Memory_Cell_Block": "LSTM",
    "Constant_Error_Carousel": "LSTM",
    "Vanilla_RNN": "RNN",
    "Elman_Network": "RNN",
    "Bi-LSTM": "BiLSTM",
    "BLSTM": "BiLSTM",
    "DNN": "ANN",
    "MLR": "Linear_Regression",
    "CNN-LSTM-Attention": "CNN_LSTM_Attention",
    "CNN-LSTM-Transformer": "CNN_LSTM_Transformer",
    "LSTM-Transformer": "LSTM_Transformer",
    "CNN_BiLSTM": "BiLSTM",
    "CNN-BiLSTM": "BiLSTM",
    "S-Mamba": "S_Mamba",
    "Mamba-3": None,  # handled by round-2 stub (kept for clarity)
    "TimesBlock": "TimesNet",
    "Second_Raw_Moment_Estimate": "Adam",
    "First_Moment_Estimate": "Adam",
    "Bias_Correction_Terms": "Adam",
    "AdaMax": "Adam",
    "AdaDelta": "Adam",
    "FedSGD": "FedAvg",
    "FOMAML": "MAML",
    "First_Order_MAML": "Reptile",
    "Few_Shot_Adaptation": "MAML",
    "Model Agnostic Meta-Learning": "MAML",
    "Inductive_Transfer_Learning": "Meta_Learning",
    "Stacking_Ensemble": "Ensemble_Stacking",
    "Ensemble_Learning": "Ensemble_Stacking",
    "ARMA_Baseline": "ARIMA",
    "Weekly_Persistence": "Persistence_Model",
    "Split_Conformal_Prediction": "Conformal_Prediction",
    "Inductive_Conformal_Prediction": "Conformal_Prediction",
    "Nonconformity_Score": "Conformal_Prediction",
    "Calibration_Set": "Conformal_Prediction",
    "Conditional_Diffusion_Model": "DDPM",
    "DiffWave": "DDPM",
    "Intrinsic_Mode_Functions": "VMD",
    "DWT_db4_Wavelet_Denoised_Prices": "Wavelet_Decomposition",
    "Non_Homogeneous_Poisson_Process": "Queuing_Model",
    "Virtual_Queues": "Queuing_Model",
    "M_G_Infinity_Queuing_Model": "Queuing_Model",
    "Model_Predictive_Control": "MPC",
    "Receding_Horizon_Control": "MPC",
    "K-Means++": "KMeans_Clustering",
    "Principal_Components": "PCA",
    "Negative_Log_Likelihood": "NLL",
    "Training_Cost_Negative_Log_Likelihood": "NLL",
    "CRPSsum": "CRPS",
    "CRPS_Sum": "CRPS",
    "nRPS": "RPS",
    "Pinball_Score": "Pinball_Loss",
    "P50_Loss": "Pinball_Loss",
    "P90_Loss": "Pinball_Loss",
    "Prediction_Interval_Width": "MPIW",
    "Coverage_Rate": "PICP",
    "Explained_Variance_Score": "R_squared",
    "Normalized_Mean_Square_Error": "NRMSE",
    "Normalized_Deviation": "ND",
    "R-squared": "R_squared",
    "ACC": "Accuracy",
    "Accuracy_Rate": "Accuracy",
    "Accuracy_Index": "Accuracy",
    # paper-reference style links -> vault paper notes
    "Vaswani2017_Attention_Is_All_You_Need": "2017_Attention_Is_All_You_Need",
    "Li2019_LogTrans": "2019_Li_LogSparse_Enhancing_Locality_Transformer",
    "Wu2021_Autoformer": "2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation",
    "Zhou2022_FEDformer": "FEDformer",
    "Zhou2021_Informer": "2021_Zhou_Informer_Beyond_Efficient_Transformer",
    "TimeMachine": "2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting",
    "Forwardformer": "2024_Qu_Forwardformer_Day_Ahead_Load",
    "Tao2018? Prophet": "Prophet",
    "Taylor2018_Prophet": "Prophet",
    "2026_PC_M3_Mamba_EV_Clusters": "PC-M3",
    "2023_MetaProbformer_for_Charging_Load_Probabilistic_Forecasting_of_Electric_Vehicle_Charging_Stations":
        "2023_Huang_MetaProbformer_EV_Load",
    "2024_Wang_Shengyou_ML_Geographical_Transferability_EV":
        "2026_Wang_Shengyou_ML_Geographical_Transferability_EV",
    "2001_Neural_Networks_for_Short_Term_Load_Forecasting_A_Review_and_Evaluation":
        "2001_Hippert_Neural_Networks_STLF_Review",
    "2017_Zhang_DCRNN_Deep_Spatio_Temporal_Residual_Networks": "DCRNN",
    # horizons / strategy concepts
    "STLF": "Short_Term_Forecasting",
    "LTSF": "Long_Term_Forecasting",
    "LSTF": "Long_Term_Forecasting",
    "Day_Ahead_Market": "Day_Ahead_Forecasting",
    "TOU_Electricity_Price": "Electricity_Tariff",
    # misc models
    "TCN_GLU": "TCN",
    "Multiscale_Dilated_TCN_Kernels": "TCN",
    "DeepTCN": "TCN",
    "GCN_TRN": "GCN",
    # ---------- round 4 (singles cleanup) ----------
    "2009_National_Household_Travel_Survey": "NHTS_2009",
    "Month_of_Year": "Calendar_Features",
    "Recurrent_Neural_Network": "RNN",
    "Backpropagation_ANN": "ANN",
    "Shenzhen": "Shenzhen_ST_EVCDP",
    "PEMS": "Traffic",
    "M4_Hourly": "M4",
    "Amazon_EC_Sub_Dataset": "Amazon_EC_Dataset",
    "ELIA_Belgian_Grid": None,
    "Belgian_Power_Grid_Data": "ELIA_Belgian_Grid",
    "Elia_Belgian_Grid_Data": "ELIA_Belgian_Grid",
    "NASDAQ100 Stock Price Data": "NASDAQ100_Stock_Price_Dataset",
    "UC_Davis_PHEV_PH EV_Center_Data": "UC_Davis_PH_EV_Center_Data",
    "UC_Davis_PHEV_PHEV_Center_Data": "UC_Davis_PH_EV_Center_Data",
    "Distribution System State Estimation": "Distribution_System_State_Estimation",
    "LTSF-Linear": "DLinear",
    "LTSF_Linear": "DLinear",
}

# folder overrides for auto-stubs, and targets to skip entirely
FOLDER_OVERRIDES = {
    "PV": "features",
    "Nottingham": "datasets",
    "PyTorch": "guides",
    "Keras": "guides",
    "OCPP": "guides",
    "Smart_Grid": "guides",
    "Demand_Response": "guides",
    "Energy_Management_System": "guides",
    "Direct_Current_Fast_Charging": "guides",
    "Artificial_Intelligence": "guides",
    "Transduction": "guides",
    "Grid_Demand": "features",
    "Electricity_Usage": "features",
    "NPIW": "metrics",
    "Sister_Point_Forecasts": "guides",
    "Distribution_System_State_Estimation": "guides",
    "Beltagy2020_Longformer": "papers",
    "Bahdanau2016_LSTMa_Attention": "papers",
    "Gaillard2016_GEFCOM2014_Aggregation": "papers",
    "Berrisch_Ziel_CRPS_Learning": "papers",
    "Wintenberger2017_BOA": "papers",
    "Zaffran2022_Adaptive_Conformal": "papers",
}

CURATED_STUBS = {
    # ---- metrics ----
    "sMAPE": ("metrics", "Symmetric Mean Absolute Percentage Error; MAPE variant that symmetrizes the denominator to avoid penalizing low actual values."),
    "NMAE": ("metrics", "Normalized Mean Absolute Error: [[MAE]] divided by a normalizing constant (mean load or capacity), making forecasts comparable across stations."),
    "RPS": ("metrics", "Ranked Probability Score: quadratic measure of the distance between a full predictive distribution and the observation, standard for probabilistic forecasts."),
    "NLL": ("metrics", "Negative Log-Likelihood: proper scoring rule evaluating the full predictive density; lower is better."),
    "Precision": ("metrics", "Fraction of predicted positives that are correct; pairs with [[Recall]] and [[Accuracy]]."),
    "Recall": ("metrics", "Fraction of actual positives that are detected; pairs with [[Precision]]."),
    "AUC": ("metrics", "Area Under the ROC Curve: threshold-independent classification quality measure."),
    "Pearson_Correlation": ("metrics", "Linear correlation coefficient between forecast and observation; see [[Pearson_Correlation_Coefficient]]."),
    "MSPE": ("metrics", "Mean Squared Percentage Error; percentage-based analogue of MSE, related to [[MAPE]]."),
    # ---- features ----
    "Solar_Radiation": ("features", "Incoming solar radiation (GHI/DNI/DHI components); weather covariate for PV-aware load forecasting."),
    "Pressure": ("features", "Barometric pressure covariate (station or sea-level); minor weather input used in some forecasting studies."),
    "Weather_Forecast": ("features", "Numerical weather predictions used as future covariates in day-ahead forecasting (as opposed to observed weather)."),
    "Weather_Features": ("features", "Family of meteorological input variables ([[Temperature]], [[Humidity]], [[Wind_Speed]], radiation, precipitation) driving demand."),
    "Lag_Features": ("features", "Autoregressive input features constructed from past values of the target series (y(t-lag)); the workhorse of tabular forecasting pipelines."),
    "Lookback_Window": ("features", "Length of the historical input window fed to sequence models; key hyperparameter trading context against compute."),
    "Static_Covariates": ("features", "Time-invariant inputs (location, capacity, connector type) in the Temporal Fusion Transformer input taxonomy."),
    "Past_Observed_Inputs": ("features", "Time-varying inputs observable only up to forecast time in the [[Temporal_Fusion_Transformer]] taxonomy."),
    "Known_Future_Inputs": ("features", "Time-varying inputs known in advance (calendar, planned events, weather forecasts) in the [[Temporal_Fusion_Transformer]] taxonomy."),
    "Charging_Power": ("features", "Power delivered during a charging session (kW); bounded by vehicle and connector limits."),
    "Charging_Duration": ("features", "Session length from plug-in to plug-out; determines energy delivered at a given power level."),
    "Station_Occupancy": ("features", "Number/proportion of occupied chargers at a station over time; direct precursor of station-level load."),
    "Battery_Capacity": ("features", ""),
    "Depth_of_Discharge": ("features", "Fraction of battery capacity cycled between charges; degradation-related battery feature."),
    # ---- models ----
    "Seq2Seq": ("models", "Encoder-decoder sequence-to-sequence framework mapping an input sequence to an output sequence; basis of many early deep forecasters."),
    "Kalman_Filter": ("models", "Recursive Bayesian estimator for linear-Gaussian state-space models; classic adaptive baseline for load forecasting."),
    "PCA": ("models", "Principal Component Analysis: linear dimensionality reduction retaining maximal variance; used for input compression and clustering."),
    "Gaussian_Process": ("models", "Non-parametric Bayesian regression with kernel-defined uncertainty; see [[Deep_Gaussian_Process]] and [[Sparse_GP]]."),
    "SVM": ("models", "Support Vector Machine; classification sibling of [[SVR]] using maximum-margin kernels."),
    "LightGBM": ("models", "Microsoft's gradient-boosted tree framework; fast tabular baseline (cf. [[XGBoost]])."),
    "MQ-RNN": ("models", "Multi-Quantile RNN: seq2seq network trained on multiple quantile outputs for probabilistic forecasting."),
    "LSTNet": ("models", "Long- and Short-term Time-series Network combining convolutional, recurrent, and skip-recurrent components."),
    "Chronos": ("models", "Amazon's pretrained time-series foundation model family tokenizing scaled values for probabilistic zero-shot forecasting."),
    "Chronos-Bolt": ("models", "Faster, patch-based descendant of [[Chronos]] for point and quantile forecasting."),
    "TimesFM": ("models", "Google's decoder-only patched time-series foundation model for zero-shot point forecasting."),
    "Moirai": ("models", "Salesforce's masked-encoder universal time-series foundation model handling arbitrary variates and frequencies."),
    "LagLlama": ("models", "Open-source lag-feature-based foundation model for univariate probabilistic forecasting."),
    "Time-MoE": ("models", "Billion-scale mixture-of-experts time-series foundation model."),
    "GNN": ("models", "Graph Neural Network umbrella term; spatial-relational building block behind [[GCN]], [[GAT]], and spatio-temporal variants."),
    "NILM": ("models", "Non-Intrusive Load Monitoring: disaggregating aggregate meter readings into appliance-level consumption."),
    "Queuing_Model": ("models", "Stochastic arrival-service models (M/G/\u221e etc.) describing aggregate EV plug-in demand at stations."),
    "Holt_Exponential_Smoothing": ("models", "Double exponential smoothing with level and trend components; classical baseline (ETS family)."),
    "STL": ("models", "Seasonal-Trend decomposition using Loess; classical decomposition baseline and preprocessing step."),
    "Wavelet_Decomposition": ("models", "Multi-resolution signal decomposition; preprocessing for denoising and component-wise forecasting (cf. [[VMD]])."),
    "KMeans_Clustering": ("models", "Centroid-based partitional clustering; groups stations or load shapes before per-cluster modeling."),
    "MPC": ("models", "Model Predictive Control: rolling-horizon optimization using forecasts; cf. [[Stochastic_MPC]] and [[Lyapunov_Optimization]]."),
    "V2G": ("models", "Vehicle-to-Grid: bidirectional charging letting EV fleets provide storage services; scheduling studied with [[Lyapunov_Optimization]] and [[MPC]]."),
    "BWO": ("models", "Black Widow Optimization metaheuristic; used to tune hybrid decomposed forecasters."),
    "DCRNN": ("models", "Diffusion Convolutional Recurrent Neural Network: traffic-style spatio-temporal graph forecasting with diffusion convolution."),
    "EGAT": ("models", "Edge-augmented Graph Attention Network used in federated EV load studies."),
    # ---- guides ----
    "Adjacency_Matrix": ("guides", "Matrix encoding graph connectivity between nodes (stations, regions); weighted by distance, correlation, or topology in spatio-temporal models."),
    "Grid_Topology": ("guides", "Physical/network structure of the distribution grid; constrains feasible charging schedules and defines electrical adjacency."),
    "Conformal_Prediction": ("guides", ""),
}

AUTO_FOLDER_HINTS = [
    # (regex on target, folder)
    (r"^19\d\d_|^20\d\d_", "papers"),
    (r"data$|dataset|_data\b|corpus|archive|benchmark|mujoco|rllab|mnist|cifar|wmt|reber|synthetic|toy_|air-|pm25|covid|mobility|grid$|power_system|electric_load|^ael_|^cel_|travel_survey|telemetry|pageviews|stock|forex|market_|retail|water_levels|photometry|sensor_network|charging_site|ev_pl|arrival_data|statistics_bureau|installation_events|submetering|feeder_|utility_load|household_electricity|appliance_level|us_city|uk_national_grid|singapore_grid|ontario_grid|new_york_grid|california_grid|victoria_australia|belgian|greek_power|taiwan_power|norway_residential|hong_kong_ev|shanghai_ev|liuyue|qingpu|suzhou|indianapolis|southern_germany|lower_saxony|ausgrid|nrel|nsrdb|greenflux|ideal_|refit|swat|^psm$|^msl$|^smap$|jsb_|amazon_ec|uci_eeg|uc_davis|jining|nw_europe|dallas_port|hospital_semi", "datasets"),
    (r"loss|error|score|accuracy|precision|recall|coverage|width|sharpness|interval|deviation|distance|perplexity|bleu|correlation|likelihood|aic|bic|variance$|bias$|rate$|ratio$|index$|^ace$|^owa$|^nd$|^dcl$|^rae$|^acc$|qualified|utilization|congestion|unbalance|h1_error|l2_error|energy_score", "metrics"),
    (r"feature|flag|indicator|encoding|embedding|temperature|radiation|humidity|wind|rain|snowfall|cloud|pressure|visibility|lag|window|demand|load$|power|charging|arrival|departure|\bsoc\b|speed|duration|occupancy|time$|timestamp|seasonal|trend|cycle|elasticity|mileage|travel|driv|vehicle|battery|range|fleet|connector|charger|pile|station_id|poi|social|income|education|economic|holiday|workday|weekday|weekend|month|season$", "features"),
    (r"optimizer|descent|sampling|algorithm|search|learning_rate|epochs|regularization|initialization|batch|gradient|adam|sgd|rmsprop|adagrad|quadrature|mcmc|em_algorithm|regret|online_aggregation|scenario_reduction|latin_hypercube|monte_carlo|genetic|particle_swarm|ant_colony|immune|kkt|linear_programming|polytope|optnet|admm|bayesian", "hyperparameters"),
]
DEFAULT_FOLDER = "models"


def sanitize(name):
    return re.sub(r'[\\/:*?"<>|]+', "_", name).strip()


def humanize(name):
    return name.replace("_", " ").replace("-", " ").strip()


def extract_target(link_body):
    return link_body.split("|")[0].split("#")[0].strip()


def scan_broken(notes_lower):
    counts = Counter()
    referrers = {}
    for note in sorted(WIKI.rglob("*.md")):
        text = note.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for m in WIKI_LINK_RE.finditer(text):
            target = extract_target(m.group(1))
            if not target:
                continue
            if target.lower() not in notes_lower:
                counts[target] += 1
                referrers.setdefault(target, []).append(note.stem)
    return counts, referrers


def apply_retargets(text):
    n = 0
    for old, new in RETARGETS.items():
        if new is None:
            continue
        pattern = re.compile(r"\[\[" + re.escape(old) + r"(?=[]|#|])")
        text, k = pattern.subn("[[" + new, text)
        n += k
    return text, n


def make_note(name, folder, overview="", referrers=None):
    path = WIKI / folder / f"{sanitize(name)}.md"
    if path.exists():
        return False
    title = humanize(sanitize(name))
    tags = [folder.rstrip("s")] + [sanitize(name).lower()]
    front = (
        "---\n"
        f"type: {folder.rstrip('s')}\n"
        f'name: "{title}"\n'
        "category: Stub (auto-generated)\n"
        "status: needs-review\n"
        f"tags:\n" + "".join(f"  - {t}\n" for t in tags) +
        "---\n\n"
        f"# {title}\n\n"
    )
    body = overview.strip() or (
        f"{title} \u2014 concept referenced in this research knowledge base. "
        "This stub was auto-generated during broken-link cleanup and needs expert review."
    )
    content = front + body.strip() + "\n\n## Referenced in this knowledge base\n\n"
    if referrers:
        content += ", ".join(f"[[{r}]]" for r in referrers[:8]) + "\n"
        if len(referrers) > 8:
            content += f"\n*(+{len(referrers) - 8} more)*\n"
    else:
        content += "*(none recorded)*\n"
    path.write_text(content, encoding="utf-8")
    return True


def guess_folder(target):
    key = target.lower()
    if key in SKIP_TARGETS:
        return None
    if target in FOLDER_OVERRIDES:
        return FOLDER_OVERRIDES[target]
    for pattern, folder in AUTO_FOLDER_HINTS:
        if re.search(pattern, target, re.IGNORECASE):
            return folder
    return DEFAULT_FOLDER


def main(min_auto_count=None):
    if min_auto_count is None:
        min_auto_count = MIN_AUTO_COUNT
    notes = sorted(WIKI.rglob("*.md"))
    names = {n.stem.lower() for n in notes}
    notes_lower = {n.stem.lower(): n.stem for n in notes}

    # 1. raw fixes + retargets
    fixed_files = 0
    total_raw = 0
    total_retargets = 0
    for note in notes:
        text = note.read_text(encoding="utf-8", errors="replace")
        original = text
        for rx, repl in RAW_FIXES:
            text, k = rx.subn(repl, text)
            total_raw += k
        text, k = apply_retargets(text)
        total_retargets += k
        if text != original:
            note.write_text(text, encoding="utf-8")
            fixed_files += 1
    print(f"raw fixes: {total_raw}, retargeted links: {total_retargets} "
          f"(in {fixed_files} files)")

    # 2. curated stubs
    created_curated = 0
    for name, (folder, overview) in CURATED_STUBS.items():
        if make_note(name, folder, overview):
            created_curated += 1
    print(f"curated stubs created: {created_curated}")

    # refresh known names, then auto-stub pass
    notes = sorted(WIKI.rglob("*.md"))
    names = {n.stem.lower() for n in notes}
    counts, referrers = scan_broken(names)

    auto_candidates = {t: c for t, c in counts.items()
                       if c >= min_auto_count and guess_folder(t) is not None}
    created_auto = 0
    for target, _cnt in sorted(auto_candidates.items(),
                               key=lambda kv: -kv[1]):
        folder = guess_folder(target)
        if make_note(target, folder, "", referrers.get(target)):
            created_auto += 1
    print(f"auto stubs created (count>={min_auto_count}): {created_auto} "
          f"of {len(auto_candidates)} candidates")

    # final tally
    notes = sorted(WIKI.rglob("*.md"))
    names = {n.stem.lower() for n in notes}
    counts, _ = scan_broken(names)
    print(f"remaining broken targets: {len(counts)} "
          f"({sum(counts.values())} occurrences)")


if __name__ == "__main__":
    import sys
    min_count = int(sys.argv[1]) if len(sys.argv) > 1 else None
    main(min_count)
