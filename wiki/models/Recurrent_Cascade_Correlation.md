---
type: model
name: "Recurrent Cascade Correlation"
category: Neural Network / Constructive Learning Architecture
status: needs-review
tags:
  - model
  - architecture
  - recurrent-neural-network
---

# Recurrent Cascade Correlation

## Definition

Cascade-Correlation grows a network one hidden unit at a time: each new hidden unit is trained (via gradient ascent on correlation with residual error) while all downstream weights stay frozen, then installed as a cascade layer. The **recurrent** variant adds self-recurrent connections on hidden units so the network can process time-series/sequence data.

## Referenced in this knowledge base

[[1997_Long_Short_Term_Memory]] — cited as a predecessor architecture in LSTM discussions.
