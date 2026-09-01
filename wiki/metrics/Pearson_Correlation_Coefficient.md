---
type: metric
name: "Pearson Correlation Coefficient"
category: association-metric
formula: "ρ = cov(X,Y) / (σ_X · σ_Y)"
unit: Dimensionless (−1 to +1)
last_updated: 2026-08-26
tags:
  - metric
  - pearson_correlation_coefficient
---

# Pearson Correlation Coefficient

## Definition

The **Pearson correlation coefficient** measures the linear relationship between forecast $\hat{y}$ and observation $y$:

$$\rho = \frac{\sum_{i=1}^{n}(y_i - \bar{y})(\hat{y}_i - \bar{\hat{y}})}{\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}\,\sqrt{\sum_{i=1}^{n}(\hat{y}_i - \bar{\hat{y}})^2}} = \frac{\mathrm{cov}(y, \hat{y})}{\sigma_y\, \sigma_{\hat{y}}}$$

$\rho = 1$ perfect positive linear agreement; $0$ no linear relation. It captures shape/timing similarity but ignores bias and scale — a forecast offset by a constant still gets ρ = 1, so pair it with [[MAE]]/[[RMSE]]. Short name: [[Pearson_Correlation]].

## Referenced in this knowledge base

[[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]], [[2024_Zhong_V2G_SVE_Evaluation_Metric]]
