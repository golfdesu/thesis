---
type: dataset
name: "GIFT-Eval"
location: "Heterogeneous (23 base datasets: energy, retail, weather, finance)"
resolution: "Mixed frequencies / horizons (97 tasks)"
access: "open - https://huggingface.co/datasets/Salesforce/GiftEval"
tags: [dataset, benchmark, gift-eval, foundation-model]
---

# GIFT-Eval — General Time Series Forecasting Benchmark

97 evaluation tasks (dataset x frequency x horizon) from 23 base datasets (Aksu et al. 2024a). Companion corpora: GIFT-Eval Pretrain (2024c, large pretraining corpus, non-overlapping) and GIFT-Eval train (2024b, official train splits). Context 4096. Metrics: CRPS rank / MASE rank / CRPS / MASE. Leaderboard tiers: foundation-model (zero-shot), finetuned, ensemble, agentic.

## Literature Usage
- [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — Probabilistic zero-shot (97 configs, 100 samples); Sundial #1 MASE 0.673 / #2 CRPS 0.472.
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Zero-shot (FM-only): Toto 2.0 sweeps top-3 CRPS ranks 20.3/21.1/21.4 vs PatchTST-FM r1 23.1, Chronos-2 23.5 (monotonic scaling on ranks; 22M beats Toto 1.0 35.1 by 8pts despite no public pretraining). Full leaderboard: FnF ensemble #1 (CRPS rank 12.8) and 2.5B-FT #2 (13.4); pool weight Toto family 39%% > Chronos-2 32%%.
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — Evaluated on 97 tasks/55 datasets (high-frequency + long horizons). WQL W 81.9 S 51.4 and MASE W 83.8 S 30.2 for Chronos-2 (vs TimesFM-2.5 77.5/51.0, TiRex 76.5/50.2). Test portions excluded from training; train portions partially overlap (synthetic-only variant also reported, 50.4 vs 51.4 WQL, Fig.8b).
