---
type: model
name: "NorMuon"
category: Stub (auto-generated)
status: needs-review
tags: [model, normuon]
---

# NorMuon

Row-normalized Muon (Li et al. 2025) — per-neuron balancing reinstating beta2 variance mechanism.

## Literature Usage
- [[2026_Toto_2_Scaling_Era]] — Core optimizer for Toto 2.0 matrix params: vt=beta2 vt-1+(1-beta2)mean_cols(Ot*Ot), Wt<-Wt-1 - eta Ot/sqrt(vt+eps) (Eq.5); optimal eta 0.652, mu 0.96, beta2 0.999; AdamW retained for projections/biases; paired with Polar Express + Nesterov + cautious decay.
