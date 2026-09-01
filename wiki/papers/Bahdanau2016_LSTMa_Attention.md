---
type: paper
title: "Neural Machine Translation by Jointly Learning to Align and Translate"
authors: [Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio]
year: 2016
journal_conference: "ICLR 2015; arXiv:1409.0473 (cited as 2016 in LSTNet references)"
doi_url: "https://arxiv.org/abs/1409.0473"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Introduces the **additive attention mechanism** for sequence-to-sequence tasks: instead of compressing an entire source sequence into one fixed vector, the decoder learns to **softly attend** to all source hidden states, weighted per output step ("alignment").
- This removed the information bottleneck of encoder-decoder RNN translation and became the conceptual ancestor of the Transformer attention used throughout modern forecasting (see [[Multi_Head_Attention]]); the [[LogSparse_Transformer]]-era LSTMa variant applies this attention to recurrent forecasting backbones.

## 🧠 Methodology & Model Architecture
- Encoder BiGRU produces annotations $h_j$; the decoder scores compatibility $e_{ij} = v_a^\top \tanh(W_a s_{i-1} + U_a h_j)$, normalises with softmax into weights $\alpha_{ij}$, and forms a context vector $c_i = \sum_j \alpha_{ij} h_j$ fed together with state and previous target to predict the next token.
- Training maximises the conditional log-likelihood of translations end-to-end (attention learned jointly, no alignment supervision).

## 📈 Performance & Results
- Substantially improved English-French translation quality vs. vanilla encoder-decoder RNNs, especially on long sentences; alignment visualisations match linguistic intuition.

## 💡 Limitations & Identified Research Gaps
- Sequential decoding limits parallelism (later fixed by self-attention Transformers); additive scoring is slower than dot-product forms at scale.

## 📚 BibTeX & Citation Reference
- D. Bahdanau, K. Cho, Y. Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate," ICLR 2015; arXiv:1409.0473 (commonly cited with 2016 arXiv revision dates in energy-forecasting reference lists)
