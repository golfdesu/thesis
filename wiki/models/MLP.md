---
name: "Multi-Layer Perceptron (MLP)"
type: model
category: baseline-model
last_updated: 2026-08-02
tags: [model, mlp, baseline, feedforward, neural-network]
---

# 🧠 Multi-Layer Perceptron (MLP)

## Definition

A **Multi-Layer Perceptron (MLP)** is a fully-connected feedforward neural network consisting of an input layer, one or more hidden layers, and an output layer. Each neuron applies a non-linear activation function. MLPs serve as important baseline models in EV load forecasting, and in some benchmarks outperform more complex deep learning architectures.

## Architecture

$$h^{(l)} = \sigma\left(W^{(l)} h^{(l-1)} + b^{(l)}\right)$$

Where:
- $h^{(l)}$ = output of layer $l$
- $W^{(l)}$ = weight matrix
- $b^{(l)}$ = bias vector
- $\sigma$ = activation function (ReLU, Tanh, GELU)

## Key Characteristics

| Property | Description |
|----------|-------------|
| **Temporal modeling** | None — treats each input independently (no sequential memory) |
| **Scalability** | High — fast training and inference |
| **Interpretability** | Moderate — can apply SHAP or permutation importance |
| **Data requirement** | Low — works well with limited data |
| **Complexity** | Low — fewer hyperparameters than RNN/Transformer |

## Role in EV Load Forecasting Literature

> [!IMPORTANT]
> [[2024_Bampos_EV_Load_Forecasting_DAM]] demonstrates that **MLP outperforms complex deep learning** (LSTM, Transformer) on 36-hour rolling Day-Ahead Market evaluation across 4 public EV datasets, especially when combined with multiplicative trend-residual decomposition. This is a critical finding for thesis benchmarking.

## Literature Usage

| Paper | How MLP Is Used | Performance |
|-------|----------------|-------------|
| [[2024_Bampos_EV_Load_Forecasting_DAM]] | Primary model; beats LSTM/Transformer on DAM benchmark | Best or near-best on 3/4 datasets |
| [[2020_Huang_Ensemble_EV_Load]] | Base learner in ensemble stacking (alongside ANN, RNN, LSTM) | Meta-LR combines predictions |
| [[2001_Hippert_Neural_Networks_STLF_Review]] | Early benchmark for STLF; critical review of architectural choices | Historical reference |
| [[2015_Raza_Review_AI_Load_Demand]] | Reviewed as classic AI approach for smart grid load forecasting | Survey reference |
| [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] | Benchmark in probabilistic day-ahead forecasting study; ranking BLSTM < unidirectional LSTM < MLP < RF/SVR < ARIMA | Upgrading MLP → BLSTM added ~€0.5–10k retailer profit |
| [[2019_Zhu_ApplSci_EV_Load_Forecasting]] | DNN (feedforward MLP-equivalent) baseline with 2–4 hidden layers | Test-NRMSE 3.69–3.81%; least accurate of four models but trained fastest (68.88 s) |
| [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] | ANN base model whose per-hour selection is learned by a Q-learning agent across charging regimes | Q-Learning ensemble cuts smart-charging MSE from 7.22 to 4.63 (>50% claimed gain) |
| [[2024_Zhong_V2G_SVE_Evaluation_Metric]] | Day-ahead forecaster evaluated by V2G scheduling value (not just statistical quality) | Lowest scheduling value error: avg SPDR 0.30%, despite MLR winning on MAPE/RMSE/MAE |
| [[2025_Zheng_Coherent_Hierarchical_EV_Load]] | Baseline in coherent hierarchical probabilistic EV charging forecasting | Worst total MAE 13.49 vs proposed LSTM+PICNN 2.15 |
| [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] | 3-hidden-layer MLP (128→64→32) among six ML/DL models benchmarked over 12 cities | Beaten by LSTM/GRU/RF/SGD on MAE; SGD best overall |
| 2024 — [[2024_Huo_Data_Driven_EVCS_Demand_Forecasting]] | Rao-1-tuned single-hidden-layer ANN for one-step hourly station demand on ACN Caltech+JPL | Best of ANN/SVR/BRT — JPL RMSE 6.93 kW, R² 0.974; Caltech RMSE 4.50 kW |
| 2024 — [[2024_Ma_LASSO_BPNN_Mid_Term_EV_Load]] | BPNN (MLP-family) trained on LASSO-screened monthly factors across four Qingpu station types | Beats LASSO-SVR/XGBoost/RF; Residential RMSE 28.863→20.631 vs plain BPNN (MAPE 11.73%→8.64%) |

## Advantages in EV Load Forecasting

1. **No overfitting to temporal artifacts**: Unlike LSTMs, MLPs don't overfit to recent sequence patterns.
2. **Robust to data scarcity**: Fewer parameters → lower variance.
3. **Fast inference**: Critical for real-time V2G dispatch.
4. **Easy interpretability**: SHAP values applicable directly.

## Related Pages

- [[LSTM]]
- [[GRU]]
- [[XGBoost]]
- [[Ensemble_Stacking]]
- [[Transformer]]
