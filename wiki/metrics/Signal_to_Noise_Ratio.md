---
type: metric
name: "Signal to Noise Ratio (SNR)"
category: signal-quality-metric
formula: "SNR_dB = 10 · log10(P_signal / P_noise)"
unit: Decibels (dB)
last_updated: 2026-08-26
tags:
  - metric
  - signal_to_noise_ratio
  - snr
---

# Signal to Noise Ratio

## Definition

**SNR** compares the power of a meaningful signal to the power of background noise:

$$\text{SNR}_{\text{dB}} = 10 \log_{10}\!\left(\frac{P_{\text{signal}}}{P_{\text{noise}}}\right) = 20 \log_{10}\!\left(\frac{A_{\text{signal}}}{A_{\text{noise}}}\right)$$

where $P$ are mean square (power) values and $A$ amplitudes — the 10× form applies to power ratios, the 20× form to amplitude ratios. Higher is better. In optimization contexts ([[2014_Kingma_Adam_Stochastic_Optimization]]) it denotes the ratio of the gradient's mean to its standard deviation, i.e. $ \text{SNR} = \|\mathbb{E}[g]\| / \sqrt{\mathrm{Var}[g]} $, which Adam's update implicitly estimates.

| Property | Description |
|----------|-------------|
| **Higher is better** | ✅ Yes |
| **Unit** | dB for power ratios; dimensionless for the raw ratio |

## Referenced in this knowledge base

[[2014_Kingma_Adam_Stochastic_Optimization]]
