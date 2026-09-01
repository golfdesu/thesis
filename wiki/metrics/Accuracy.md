---
type: metric
name: "Accuracy"
category: Stub (auto-generated)
status: needs-review
tags:
  - metric
  - accuracy
---

## Definition
$$\mathrm{Accuracy} = \frac{\text{correct predictions}}{\text{total predictions}}$$

Fraction of correct predictions, used for classification tasks (e.g. classification-related components in meta-learning papers such as [[MAML]] and [[Reptile]]).

| Property | Value |
|----------|-------|
| Lower/Higher | Higher is better |
| Caution | Misleading on imbalanced classes |

## Usage in EV / Load Forecasting Papers
Appears mainly in classification sub-tasks or event detection rather than load regression.
