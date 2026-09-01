---
type: dataset
name: "Wikipedia Web Traffic Dataset"
title: "Wikipedia Web Traffic Dataset"
location: "Global (Wikipedia pageviews, multiple language projects)"
resolution: "daily"
access: "open (Kaggle / Wikimedia dumps)"
tags: [dataset, ltsf-benchmark]
---

# Wikipedia Web Traffic Dataset

Large-scale web-traffic series used for long-horizon forecasting: daily page views for ~145,000 Wikipedia articles from the Kaggle *Web Traffic Time Series Forecasting* competition, starting 1 July 2015 (original run through Sep 2017; extended versions reach mid-2022). Each series is tagged with access type (all/mobile/desktop/spider); missing values are typically zero-filled. Commonly used as a single aggregated series or a subset of articles in LTSF papers.

- **Reference**: [https://github.com/Nixtla/neuralforecast](https://github.com/Nixtla/neuralforecast)
- **Competition**: https://www.kaggle.com/c/web-traffic-time-series-forecasting

## Literature Usage
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — See Wikipedia_Pageviews: TimesFM pretraining used Wikimedia pageviews (5.6M hourly series, ~360B points total).
