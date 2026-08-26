---
type: paper
title: "Attention Is All You Need"
authors: [Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin]
year: 2017
journal_conference: "Advances in Neural Information Processing Systems 30 (NIPS 2017), Long Beach, CA"
doi_url: "https://arxiv.org/abs/1706.03762"
models_used: ["[[Transformer]]", "[[Scaled_Dot_Product_Attention]]", "[[Multi_Head_Attention]]", "[[ByteNet]]", "[[ConvS2S]]"]
datasets_used: ["[[WMT_2014_EN-DE]]", "[[WMT_2014_EN-FR]]", "[[Penn_Treebank|WSJ_Penn_Treebank]]", "[[BerkleyParser_Corpus]]"]
features_used: ["[[Token_Embeddings]]", "[[Sinusoidal_Positional_Encoding]]", "[[Byte_Pair_Encoding]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[BLEU]]", "[[Perplexity]]", "[[F1_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Attention Is All You Need

## 🎯 Main Objective & Contribution
- Introduces the **Transformer**: the first sequence transduction model relying **entirely on self-attention**, dispensing with recurrence ([[LSTM]], [[GRU]]) and convolutions entirely.
- Removes the inherent sequential bottleneck of RNNs (hidden state $h_t$ as a function of $h_{t-1}$), enabling full parallelization within training examples — training to SOTA in as little as 12 hours on 8 P100 GPUs.
- Reduces path length between any two positions to $O(1)$ (vs $O(n)$ recurrent, $O(\log_k(n))$ dilated convolutional) at per-layer complexity $O(n^2 \cdot d)$, counteracting attention averaging with multi-head attention.
- Establishes new single-model state-of-the-art on WMT 2014 EN→DE and EN→FR and generalizes to English constituency parsing; the architectural foundation for all subsequent forecasting transformers ([[Informer]], [[Autoformer]], [[PatchTST]], [[Temporal_Fusion_Transformer]]).

## 🧠 Methodology & Model Architecture
**Overall structure:** encoder-decoder. Encoder maps $(x_1,...,x_n)$ to continuous representations $z=(z_1,...,z_n)$; auto-regressive decoder emits $(y_1,...,y_m)$ one element at a time. Both are stacks of $N=6$ identical layers with residual connections + layer normalization: output of each sub-layer is $\text{LayerNorm}(x + \text{Sublayer}(x))$, all outputs dimension $d_{\text{model}} = 512$. Decoder adds a third cross-attention sub-layer over the encoder output and applies causal masking (softmax inputs for illegal connections set to $-\infty$).

**1. Scaled Dot-Product Attention (Equation 1):**
$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
The $1/\sqrt{d_k}$ scaling counters large-magnitude dot products ($q\cdot k = \sum_{i=1}^{d_k} q_i k_i$ has mean 0 and variance $d_k$ under independent unit-variance components) that push softmax into low-gradient regions. Faster than additive attention since it uses optimized matrix multiplication.

**2. Multi-Head Attention** — $h=8$ parallel heads with $d_k = d_v = d_{\text{model}}/h = 64$:
$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,\dots,\text{head}_h)\,W^O$$
$$\text{head}_i = \text{Attention}(Q W_i^Q,\ K W_i^K,\ V W_i^V)$$
with projections $W_i^Q, W_i^K \in \mathbb{R}^{d_{model}\times d_k}$, $W_i^V \in \mathbb{R}^{d_{model}\times d_v}$, $W^O \in \mathbb{R}^{h d_v \times d_{model}}$. Used in three roles: encoder-decoder attention, encoder self-attention, and masked decoder self-attention.

**3. Position-wise Feed-Forward Network (Equation 2)** — two linear transforms with ReLU, inner dimension $d_{ff}=2048$, parameters differ per layer:
$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$$

**4. Sinusoidal Positional Encoding** — wavelengths forming geometric progression from $2\pi$ to $10000\cdot 2\pi$:
$$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}}), \qquad PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})$$
Chosen because $PE_{pos+k}$ is a linear function of $PE_{pos}$ (easy relative-position learning) and may extrapolate to longer sequences than seen in training; learned embeddings gave nearly identical results (Table 3 row E).

**5. Training setup:** shared weight matrix between both embedding layers and pre-softmax linear transform (scaled by $\sqrt{d_{model}}$); [[Adam]] optimizer with $\beta_1=0.9$, $\beta_2=0.98$, $\epsilon=10^{-9}$; residual dropout $P_{drop}=0.1$ (0.3 for big EN-DE); label smoothing $\epsilon_{ls}=0.1$ (hurts perplexity but improves BLEU); beam search size 4, length penalty $\alpha=0.6$.

**6. Learning rate warmup schedule (Equation 3)** — linear warmup then inverse-square-root decay, warmup_steps = 4000:
$$\text{lrate} = d_{model}^{-0.5} \cdot \min(step\_num^{-0.5},\ step\_num \cdot warmup\_steps^{-1.5})$$

## 📊 Dataset & Input Features
- **WMT 2014 English-German**: ~4.5 million sentence pairs, shared source-target byte-pair vocabulary of ~37,000 tokens.
- **WMT 2014 English-French**: 36M sentences, 32,000 word-piece vocabulary. Batches of ≈25,000 source + 25,000 target tokens, batched by approximate sequence length.
- **English constituency parsing (generalization test)**: Wall Street Journal portion of Penn Treebank (~40K training sentences, 16K vocab); semi-supervised variant adds high-confidence + BerkleyParser corpora (~17M sentences, 32K vocab).
- Hardware/schedule: base model 100K steps × 0.4 s = 12 h on 8× NVIDIA P100; big model 300K steps × 1.0 s = 3.5 days. FLOPs estimated using 9.5 TFLOPS sustained per P100.
- **Code/data availability**: official implementation at https://github.com/tensorflow/tensor2tensor; preprint https://arxiv.org/abs/1706.03762.

## 📈 Performance & Results
- **EN→DE (newstest2014): Transformer (big) 28.4 BLEU**, beating the best prior result *including ensembles* by >2 BLEU (GNMT+RL ensemble 26.30, ConvS2S ensemble 26.36). Base model already 27.3.
- **EN→FR: Transformer (big) 41.8 BLEU** vs GNMT+RL ensemble 41.16, ConvS2S ensemble 41.29, at 2.3×10¹⁹ FLOPs (< 1/4 of competitors' training cost).
- Ablations (newstest2013 dev): single head −0.9 BLEU vs h=8; too many heads also hurts; reducing $d_k$ hurts quality; bigger models help (d_model=1024/d_ff=4096 → PPL 4.66, BLEU 26.0); dropout essential (P_drop 0.0 → PPL 5.77); sinusoidal ≈ learned positional embeddings (4.92 PPL both).
- **Constituency parsing (WSJ §23 F1)**: 91.3 WSJ-only (beats Berkeley Parser 90.4 with no task-specific tuning); 92.7 semi-supervised, second only to RNN-Grammar generative 93.3.
- Attention visualization shows heads tracking long-distance syntactic dependencies ("making...more difficult") and anaphora resolution ("its").

## 💡 Limitations & Identified Research Gaps
- Self-attention cost is quadratic $O(n^2 \cdot d)$ in sequence length; authors propose restricted neighborhood self-attention of size $r$ (path length $O(n/r)$) as future work — later realized by [[Informer]]/sparse attention for long EV load windows.
- Attention averaging reduces effective resolution; multi-head attention is the mitigation but raises parameter/compute cost.
- Generation remains sequential/auto-regressive at inference; authors list making generation less sequential and extension to image/audio/video modalities as open goals.
- Not a time-series or load-forecasting paper: no exogenous covariates, probabilistic outputs, or calendar features — adaptation to load forecasting required later work (decomposition, frequency encodings, quantile heads).

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{vaswani2017attention,
  title={Attention Is All You Need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, {\L}ukasz and Polosukhin, Illia},
  booktitle={Advances in Neural Information Processing Systems 30 (NIPS 2017)},
  year={2017},
  eprint={1706.03762},
  url={https://arxiv.org/abs/1706.03762}
}
```

## 🔗 Key References & Citation Graph
- Replaces recurrent sequence models built on [[1997_Hochreiter_Long_Short_Term_Memory]]
- Optimizer used: [[2014_Kingma_Adam_Stochastic_Optimization]]
- Convolutional alternative evaluated against: [[2018_Bai_Empirical_TCN_Sequence_Modeling]]
- Direct EV/load-forecasting descendants in vault: [[2021_Zhou_Informer_Beyond_Efficient_Transformer]], [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]], [[2021_Lim_TFT_Temporal_Fusion_Transformers]], [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]], [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]], [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]]
