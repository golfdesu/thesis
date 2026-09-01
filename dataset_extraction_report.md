# 📊 Comprehensive Dataset Extraction Report (Thesis Corpus)

รายงานนี้สำรวจและสรุปข้อมูล **Dataset** ที่ถูกใช้งาน/กล่าวถึงในบทความวิจัยทั้งหมดในโฟลเดอร์ `raw_sources/` รวมถึง **ลิงก์ยาว (URLs)**

---

## 📌 Summary Table: Datasets & Links by Paper

---

## 🔁 Detailed Paper-by-Paper Dataset & Link Breakdown

### 1. 1997_Long_Short_Term_Memory.pdf

- **Title**: Long Short-Term Memory
- **Identified Datasets**: Synthetic Temporal Dependency Benchmarks
- **🔗 Extracted Web Links**:
- [`[http://www7.informatik.tu-muenchen.de/˜hochreit`](http://www7.informatik.tu-muenchen.de/˜hochreit)](http://www7.informatik.tu-muenchen.de/˜hochreit`)

- **📁 Key Dataset Text Snippets / Context**:
- > Hochreiter, J. (1991). Untersuchungen zu dynamischen neuronalen Netzen. Diploma thesis, Institut f¨ur Informatik, Lehrstuhl Prof. Brauer, Technische Universit¨at M¨unchen. See [http://www7.informatik.tu-muenchen.de/˜hochreit.](http://www7.informatik.tu-muenchen.de/˜hochreit.) Hochreiter, S., & Schmidhuber, J. (1995). Long short-term memory (Tech. Rep. No. FKI-207-95). Fakult¨at f¨ur Informatik, Technische Universit¨at M¨unchen.

---

### 2. 2001_Neural_Networks_for_Short_Term_Load_Forecasting_A_Review_and_Evaluation.pdf

- **Title**: Neural Networks for Short-Term Load Forecasting: A Review and Evaluation
- **Identified Datasets**: Utility Power System Load Data (1990s)
- **🔗 Dataset Links**: No direct external data URL mentioned in PDF text.
- **📁 Key Dataset Text Snippets / Context**:
- > day’s peak load or next day’s total load. In the second group are the ones that have several output nodes to forecast a sequence of hourly loads. Typically, they have 24 nodes, to forecast next day’s 24 hourly loads (this series of hourly loads is called the “load profile ).

- > the ones that have several output nodes to forecast a sequence of hourly loads. Typically, they have 24 nodes, to forecast next day’s 24 hourly loads (this series of hourly loads is called the “load profile ). We start with the first group. Reference [68] used three small-

- > “load profile ). We start with the first group. Reference [68] used three small- sized NNs to forecast hourly loads, total loads and peak loads TABLE I INPUT CLASSIFICATION

- > two NNs, one of which included a linear neuron among the sig- moidal ones in the hidden layer. Reference [23] experimented with feed-forward and recurrent NNs to forecast hourly loads, and was the only paper to report that linear models actually per- formed better than those NNs.

- > These NNs with only one output neuron were also used to forecast profiles, in either of two ways. The first way was by re- peatedly forecasting one hourly load at a time, as in [28], [29]. The second way was by using a system with 24 NNs in parallel, one for each hour of the day: [61] compared the results of such

---

### 3. 2014_A_Scalable_Stochastic_Model_for_the_Electricity_Demand_of_Electric_and_Plugin_Hybrid_Vehicles.pdf

- **Title**: A Scalable Stochastic Model for the Electricity Demand of Electric and Plug-In Hybrid Vehicles
- **Identified Datasets**: National Household Travel Survey (NHTS) EV Travel Profiles
- **🔗 Extracted Web Links**:
- [`[http://www.sciencedirect`](http://www.sciencedirect)](http://www.sciencedirect`)

- [`[http://nhts.ornl.gov`](http://nhts.ornl.gov)](http://nhts.ornl.gov`)

- [`[http://www.cs.unc.edu/~welch/media/pdf/`](http://www.cs.unc.edu/~welch/media/pdf/)](http://www.cs.unc.edu/~welch/media/pdf/`)

- **📁 Key Dataset Text Snippets / Context**:
- > University of California Davis, Davis, CA 95616 USA. Color versions of one or more of the ﬁgures in this paper are available online at [http://ieeexplore.ieee.org.](http://ieeexplore.ieee.org.) Digital Object Identiﬁer 10.1109/TSG.2013.2275988 literature hypothesizes simple models of aggregate arrival rates

- > work the inclusion of geographical information that would 1949-3053 © 2013 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [http://www.ieee.org/publications_standards/publications/rights/index.html](http://www.ieee.org/publications_standards/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 31,2026 at 11:27:33 UTC from IEEE Xplore.  Restrictions apply.

- > transformed daily count vector is conditionally independent of all other count vectors in the historical dataset given for day

- > nate the subscript from our notation from this point on. A. Data Set Description We will compute the parameters of our model as follows. The probability density function (PDF) of charge durations and

- > these issues will affect the statistics for PHEV charging events derived here, this does not limit our model from being re-pa- rameterized when new larger data sets of PHEV or EV charging become available. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 31,2026 at 11:27:33 UTC from IEEE Xplore.  Restrictions apply.

---

### 4. 2014_Adam_A_Method_for_Stochastic_Optimization.pdf

- **Title**: A Scalable Stochastic Model for the Electricity Demand of Electric and Plug-In Hybrid Vehicles
- **Identified Datasets**: National Household Travel Survey (NHTS) EV Travel Profiles
- **🔗 Dataset Links**: No direct external data URL mentioned in PDF text.
- **📁 Key Dataset Text Snippets / Context**:
- > our initialization bias correction technique, and section 4 provides a theoretical analysis of Adam’s convergence in online convex programming. Empirically, our method consistently outperforms other methods for a variety of models and datasets, as shown in section 6. Overall, we show that Adam is a versatile algorithm that scales to large-scale high-dimensional machine learning problems. 2

- > from ﬁrst-order information. The Sum-of-Functions Optimizer (SFO) (Sohl-Dickstein et al., 2014) is a quasi-Newton method based on minibatches, but (unlike Adam) has memory requirements linear in the number of minibatch partitions of a dataset, which is often infeasible on memory-constrained systems such as a GPU. Like natural gradient descent (NGD) (Amari, 1998), Adam employs a preconditioner that adapts to the geometry of the data, since bvt is an approximation to the diagonal

- > To empirically evaluate the proposed method, we investigated different popular machine learning models, including logistic regression, multilayer fully connected neural networks and deep convolu- tional neural networks. Using large models and datasets, we demonstrate Adam can efﬁciently solve practical deep learning problems. We use the same parameter initialization when comparing different optimization algorithms. The

- > EXPERIMENT: LOGISTIC REGRESSION We evaluate our proposed method on L2-regularized multi-class logistic regression using the MNIST dataset. Logistic regression has a well-studied convex objective, making it suitable for comparison of different optimizers without worrying about local minimum issues. The stepsize α in our logistic regression experiments is adjusted by 1/

- > √ t decay on its stepsize should theoratically match the performance of Adagrad. We examine the sparse feature problem using IMDB movie review dataset from (Maas et al., 2011). We pre-process the IMDB movie reviews into bag-of-words (BoW) feature vectors including the ﬁrst 10,000 most frequent words. The 10,000 dimension BoW feature vector for each review is highly sparse. As sug-

---

### 5. 2015_A_Review_on_AI_Based_Load_Demand_Forecasting_Techniques_for_Smart_Grid_and_Buildings.pdf

- **Title**: A Review on Artificial Intelligence Based Load Demand Forecasting Techniques for Smart Grid and Buildings
- **Identified Datasets**: Smart Grid & Building Energy Management Benchmarks
- **🔗 Extracted Web Links**:
- [`[http://crossmark.crossref.org/dialog/?doi=10.1016/j.rser.2015.04.065&domain=pdf`](http://crossmark.crossref.org/dialog/?doi=10.1016/j.rser.2015.04.065&domain=pdf)](http://crossmark.crossref.org/dialog/?doi=10.1016/j.rser.2015.04.065&domain=pdf`)

- **📁 Key Dataset Text Snippets / Context**:
- > journal homepage: www.elsevier.com/locate/rser Renewable and Sustainable Energy Reviews [http://dx.doi.org/10.1016/j.rser.2015.04.065](http://dx.doi.org/10.1016/j.rser.2015.04.065) 1364-0321/& 2015 Elsevier Ltd. All rights reserved. Abbreviations: AI, Arti?cial Intelligence; ANN, Artiﬁcial neural network; AR, Auto-Regressive; ARIMA, Auto-Regressive Integrated Moving Average; ARMA, Auto-Regressive

- > The Load (MW) Load data of year 2008 Fig. 3. One year 24 hourly load Proﬁle of year 2008. M.Q. Raza, A. Khosravi / Renewable and Sustainable Energy Reviews 50 (2015) 1352–1372 1355

- > two types: training data and testing data. Training data is used to train the network and testing data is utilized to measure the performance of forecast model. Four year 2005 to 2008 hourly load and weather data of New-ISO England grid is used to train the neural network [10]. Load data of 2009 year is used to test and

- > 1.22.1. ANN with fuzzy logic and genetic algorithm A fuzzy logic based load forecast with ANN models are generally developed to classify a large input load data set to accurately predict the load demand. Yang et al. [67] constructed a forecasting model to consider the effect of weather and holidays

- > on forecast accuracy. Fuzzy logic membership functions and rule bases are constructed for temperature and holiday factor. At the second stage, ANN model is used to predict the hourly load demand. Hourly load forecast results show that, ANN model with fuzzy logic produces better forecast results than the single ANN

---

### 6. 2017_Attention_Is_All_You_Need.pdf

- **Title**: Attention Is All You Need
- **Identified Datasets**: WMT 2014 English-German, WMT 2014 English-French
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/`](https://github.com/)](https://github.com/`)

- [`[https://github.com/tensorflow/tensor2tensor`](https://github.com/tensorflow/tensor2tensor)](https://github.com/tensorflow/tensor2tensor`)

- **📁 Key Dataset Text Snippets / Context**:
- > 5.1 Training Data and Batching We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared source- target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT

- > sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared source- target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary [38]. Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000

- > to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. The code we used to train and evaluate our models is available at [https://github.com/](https://github.com/) tensorflow/tensor2tensor. Acknowledgements

---

### 7. 2017_Finn_MAML_Model_Agnostic_Meta_Learning.pdf

- **Title**: Attention Is All You Need
- **Identified Datasets**: WMT 2014 English-German, WMT 2014 English-French
- **🔗 Dataset Links**: No direct external data URL mentioned in PDF text.
- **📁 Key Dataset Text Snippets / Context**:
- > 2.2. A Model-Agnostic Meta-Learning Algorithm In contrast to prior work, which has sought to train re- current neural networks that ingest entire datasets (San- toro et al., 2016; Duan et al., 2016b) or feature embed- dings that can be combined with nonparametric methods at

- > the K datapoints are all in one half of the input range, the 1Code for the regression and supervised experiments is at github.com/cbfinn/maml and code for the RL experi- ments is at github.com/cbfinn/maml_rl

- > 1Code for the regression and supervised experiments is at github.com/cbfinn/maml and code for the RL experi- ments is at github.com/cbfinn/maml_rl

- > learning curve at meta test-time. Note that MAML continues to improve with additional gradient steps without overﬁtting to the extremely small dataset during meta-testing, achieving a loss that is substantially lower than the baseline ﬁne-tuning approach. model trained with MAML can still infer the amplitude and

- > and few-shot learning algorithms, we applied our method to few-shot image recognition on the Omniglot (Lake et al., 2011) and MiniImagenet datasets. The Omniglot dataset consists of 20 instances of 1623 characters from 50 dif- ferent alphabets. Each instance was drawn by a different

---

### 8. 2018_Nichol_Reptile_First_Order_Meta_Learning.pdf

- **Title**: On First-Order Meta-Learning Algorithms
- **Identified Datasets**: Omniglot
- **🔗 Dataset Links**: No direct external data URL mentioned in PDF text.
- **📁 Key Dataset Text Snippets / Context**:
- > Meta-learning has emerged recently as an approach for learning from small amounts of data. Rather than trying to emulate Bayesian inference (which may be computationally intractable), meta-learning seeks to directly optimize a fast-learning algorithm, using a dataset of tasks. Speciﬁ- cally, we assume access to a distribution over tasks, where each task is, for example, a classiﬁcation problem. From this distribution, we sample a training set and a test set of tasks. Our algorithm is

- > setting. A second approach is to learn the initialization of a network, which is then ﬁne-tuned at test time on the new task. A classic example of this approach is pretraining using a large dataset (such as ImageNet [2]) and ﬁne-tuning on a smaller dataset (such as a dataset of diﬀerent species of bird [20]). However, this classic pre-training approach has no guarantee of learning an initialization that

- > A second approach is to learn the initialization of a network, which is then ﬁne-tuned at test time on the new task. A classic example of this approach is pretraining using a large dataset (such as ImageNet [2]) and ﬁne-tuning on a smaller dataset (such as a dataset of diﬀerent species of bird [20]). However, this classic pre-training approach has no guarantee of learning an initialization that is good for ﬁne-tuning, and ad-hoc tricks are required for good performance. More recently, Finn

- > derivative terms, avoiding this problem but at the expense of losing some gradient information. Surprisingly, though, they found that FOMAML worked nearly as well as MAML on the Mini- ImageNet dataset [18]. (This result was foreshadowed by prior work in meta-learning [1, 13] that ignored second derivatives when diﬀerentiating through gradient descent, without ill eﬀect.) In this work, we expand on that insight and explore the potential of meta-learning algorithms based on

- > • We provide a theoretical analysis that applies to both ﬁrst-order MAML and Reptile, showing that they both optimize for within-task generalization. • On the basis of empirical evaluation on the Mini-ImageNet [18] and Omniglot [11] datasets, we provide some insights for best practices in implementation. 2

---

### 9. 2019_Electric_Vehicle_Charging_Load_Forecasting_A_Comparative_Study_of_Deep_Learning_Approaches.pdf

- **Title**: Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting
- **Identified Datasets**: Electricity_ECL
- **🔗 Extracted Web Links**:
- [`[http://dx.doi.org/10.3390/en10081168`](http://dx.doi.org/10.3390/en10081168)](http://dx.doi.org/10.3390/en10081168`)

- [`[http://dx.doi.org/10.3390/en11113207`](http://dx.doi.org/10.3390/en11113207)](http://dx.doi.org/10.3390/en11113207`)

- [`[https://orcid.org/0000-0001-8580-534X`](https://orcid.org/0000-0001-8580-534X)](https://orcid.org/0000-0001-8580-534X`)

- [`[http://www.ncbi.nlm.nih.gov/pubmed/9377276`](http://www.ncbi.nlm.nih.gov/pubmed/9377276)](http://www.ncbi.nlm.nih.gov/pubmed/9377276`)

- [`[http://creativecommons.org/`](http://creativecommons.org/)](http://creativecommons.org/`)

- **📁 Key Dataset Text Snippets / Context**:
- > and generalization ability, artiﬁcial neural network (ANN) has become successful in delivering load forecasting tasks [11]. However, increasing resolution and dimensionality of the emerging dataset challenge canonical ANN approaches. Deep learning methods have been on the spotlight and seen remarkable success in image semantic segmentation and feature classiﬁcation [12–14], natural language processing [15] and various computational extensive science and engineering ﬁelds

- > simulated annealing algorithm to select the kernel parameters. Guo et al. [23] utilized time-indexed autoregressive with exogenous terms (ARX) models with two-stage weighted least squares regression for modeling hourly cooling load. Due to the different types of load and the complexity of inﬂuencing factors, the selection of input features and the method in constructing load forecasting models become important. Many intelligent

- > difﬁcult for quantifying the external factors that affect the charging load of PEVs, and it is impossible to establish a deterministic model. In our previous study [43], the deep learning method is used for hourly level PEV load forecasting and obtained well performance. However, the minute level super-short-term forecasting is more challenging. In this paper, the super-short-term PEV charging load model is established using minute level historical data for training, validation and test. Moreover,

- > e.g., from the beginning of each charging process to the end of charging time for each charging post. Therefore, the framework starts from data pre-processing for the input, and the preprocessed input is the PEV charging load power per minute. Then, the whole prepared data set is divided into training, test and validation set. The training set is used to train the model, while the validation set is used to tune the hyper-parameters in order to get the best performance forecasting model, and the test set is

- > LSTM Forecasting Module Figure 3. The LSTM based forecasting framework. The data set should be normalized before being fed into the model, through which the calculations in the training is simpliﬁed and the network convergence is accelerated. The normalization formula is as follows:

---

### 10. 2019_Li_LogSparse_Enhancing_Locality_Transformer.pdf

- **Title**: Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting
- **Identified Datasets**: Electricity_ECL
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/nlpdata/mrc_bert_baseline/blob/master/bert/optimization.py`](https://github.com/nlpdata/mrc_bert_baseline/blob/master/bert/optimization.py)](https://github.com/nlpdata/mrc_bert_baseline/blob/master/bert/optimization.py`)

- [`[https://www.kaggle.com/sohier/30-years-of-european-wind-generation`](https://www.kaggle.com/sohier/30-years-of-european-wind-generation)](https://www.kaggle.com/sohier/30-years-of-european-wind-generation`)

- **📁 Key Dataset Text Snippets / Context**:
- > for time series with ﬁne granularity and strong long-term dependencies under constrained memory budget. Our experiments on both synthetic data and real- world datasets show that it compares favorably to the state-of-the-art. 1 Introduction

- > long-term dependencies. On the other hand, real-world forecasting applications often have both long- and short-term repeating patterns [7]. For example, the hourly occupancy rate of a freeway in trafﬁc data has both daily and hourly patterns. In such cases, how to model long-term dependencies becomes the critical step in achieving promising performances.

- > long-term dependencies. On the other hand, real-world forecasting applications often have both long- and short-term repeating patterns [7]. For example, the hourly occupancy rate of a freeway in trafﬁc data has both daily and hourly patterns. In such cases, how to model long-term dependencies becomes the critical step in achieving promising performances. Recently, Transformer [1, 14] has been proposed as a brand new architecture which leverages attention

- > are three fold: • We successfully apply Transformer architecture to time series forecasting and perform extensive experiments on both synthetic and real datasets to validate Transformer’s potential value in better handling long-term dependencies than RNN-based models. • We propose convolutional self-attention by employing causal convolutions to produce queries and

- > attn score in layer 10 Figure 2: Learned attention patterns from a 10-layer canonical Transformer trained on traffic-f dataset with full attention. The green dashed line indicates the start time of forecasting and the gray dashed line on its left side is the conditional history. Blue, cyan and red lines correspond to attention patterns in layer 2, 6 and 10, respectively, for a head when predicting the value at the time

---

### 11. 2019_Short_Term_Load_Forecasting_for_Electric_Vehicle_Charging_Stations_Based_on_Deep_Learning_Approaches.pdf

- **Title**: Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting
- **Identified Datasets**: Electricity_ECL
- **🔗 Extracted Web Links**:
- [`[http://dx.doi.org/10.1029/JC090iC05p08995`](http://dx.doi.org/10.1029/JC090iC05p08995)](http://dx.doi.org/10.1029/JC090iC05p08995`)

- [`[http://creativecommons.org/`](http://creativecommons.org/)](http://creativecommons.org/`)

- [`[http://creativecommons.org/licenses/by/4.0/`](http://creativecommons.org/licenses/by/4.0/)](http://creativecommons.org/licenses/by/4.0/`)

- [`[http://www.mdpi.com/journal/applsci`](http://www.mdpi.com/journal/applsci)](http://www.mdpi.com/journal/applsci`)

- [`[https://orcid.org/0000-0001-5316-1711`](https://orcid.org/0000-0001-5316-1711)](https://orcid.org/0000-0001-5316-1711`)

- **📁 Key Dataset Text Snippets / Context**:
- > four featured deep learning approaches are employed and compared in forecasting the EVs charging load from the charging station perspective. Numerical results show that the gated recurrent units (GRU) model obtains the best performance on the hourly based historical data charging scenarios, and it, therefore, provides a useful tool of higher accuracy in terms of the hourly based short-term EVs load forecasting.

- > load from the charging station perspective. Numerical results show that the gated recurrent units (GRU) model obtains the best performance on the hourly based historical data charging scenarios, and it, therefore, provides a useful tool of higher accuracy in terms of the hourly based short-term EVs load forecasting. Keywords: short-term load forecasting; electric vehicles; deep learning; gated recurrent units

- > distributed network, which calls for more powerful tools for establishing accurate prediction models. In this paper, four deep learning models are preliminarily used to forecast EV charging station load, where real-world EV charging station datasets are adopted in the numerical study. The rest of the paper is organized as follow: Section 2 briefly describes three deep learning models; Section 3 introduces the dataset and proposes the data pre-processing method as well as load forecasting framework; the

- > where real-world EV charging station datasets are adopted in the numerical study. The rest of the paper is organized as follow: Section 2 briefly describes three deep learning models; Section 3 introduces the dataset and proposes the data pre-processing method as well as load forecasting framework; the experimental results are shown in Section 4, followed by Section 5 concludes the paper and outlooks the future research.

- > This section proposes the preliminaries of data processing methods and the model data formation. Moreover, load forecasting models are addressed. 3.1. Introduction of the Dataset The dataset provided by a company composes the charging load data of a large charging station from April 2017 to June 2018. Given the complicated practical application, the dataset includes

---

### 12. 2020_DeepAR_Probabilistic_Forecasting_with_Autoregressive_Recurrent_Networks.pdf

- **Title**: Ensemble Learning for Charging Load Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Boulder Colorado EV Charging Station Dataset (20, 562 transactions, 2018-2020)
- **🔗 Extracted Web Links**:
- [`[http://dx.doi.org/10.1002/j.2158-1592.2001.tb00165.x`](http://dx.doi.org/10.1002/j.2158-1592.2001.tb00165.x)](http://dx.doi.org/10.1002/j.2158-1592.2001.tb00165.x`)

- [`[http://www.jstatsoft`](http://www.jstatsoft)](http://www.jstatsoft`)

- [`[http://arxiv.org/abs/1412.6980`](http://arxiv.org/abs/1412.6980)](http://arxiv.org/abs/1412.6980`)

- [`[http://www.jstatsoft.org/article/view/v027i03`](http://www.jstatsoft.org/article/view/v027i03)](http://www.jstatsoft.org/article/view/v027i03`)

- **📁 Key Dataset Text Snippets / Context**:
- > casting, one can overcome many of the challenges faced by widely-used classical approaches to the problem. We show through extensive empirical evaluation on several real-world forecasting data sets accuracy improvements of around 15% compared to state-of-the-art methods. 1

- > intensive manual feature engineering and model selection steps required by classical techniques. In this work we present DeepAR, a forecasting method based on autoregressive recurrent networks, which learns such a global model from historical data of all time series in the data set. Our method arXiv:1704.04110v3  [cs.AI]  22 Feb 2019

- > Amazon. The distribution is over a few orders of magnitude an approximate power-law. This ob- servation is to the best of our knowledge new (although maybe not surprising) and has fundamental implications for forecasting methods that attempt to learn global models from such datasets. The scale-free nature of the distribution makes it difﬁcult to divide the data set into sub-groups of time se- ries with a certain velocity band and learn separate models for them, as each such velocity sub-group

- > servation is to the best of our knowledge new (although maybe not surprising) and has fundamental implications for forecasting methods that attempt to learn global models from such datasets. The scale-free nature of the distribution makes it difﬁcult to divide the data set into sub-groups of time se- ries with a certain velocity band and learn separate models for them, as each such velocity sub-group would have a similar skew. Further, group-based regularization schemes, such as the one proposed

- > for the 500K time series of ec, show- ing the scale-free nature (approximately straight line) present in the ec dataset (axis labels omitted due to the non- public nature of the data).

---

### 13. 2020_Ensemble_Learning_for_Charging_Load_Forecasting_of_Electric_Vehicle_Charging_Stations.pdf

- **Title**: Ensemble Learning for Charging Load Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Boulder Colorado EV Charging Station Dataset (20, 562 transactions, 2018-2020)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://bouldercolorado.gov/open-data/`](https://bouldercolorado.gov/open-data/)](https://bouldercolorado.gov/open-data/`)

- **📁 Key Dataset Text Snippets / Context**:
- > learner. The feasibility and advantage of our proposed model are demonstrated by experiments conducted on a real-world dataset and comparisons with the other four baselines. Index Terms—load forecasting, electric vehicle charging station, ensemble learning

- > The framework of the proposed ensemble learning-based forecasting model is presented in Fig. 4. As we can see, the original electric vehicle charging load dataset is ﬁrst pre- processed to obtain proper data for experiments. The original data is composed of random transactions, which means that

- > charging load of the charging stations per hour. To prevent some invalid data from impacting the prediction accuracy, we pre-process the dataset by replacing defective data with the average charging load of the same time before the day and after the day.

- > A. Experimental Setting To verify the effectiveness and feasibility of the proposed method, the experiment under a real-world dataset [24] is conducted by comparing the ensemble learning method for charging load forecasting with 4 baselines including LR,

- > of the three base learners as the independent variables when functions in the ensemble learning algorithm. In this paper, we utilize a dataset of electric vehicle charging loads from 1 January 2018 to 31 July 2020 of all city-owned electric vehicle charging stations in Boulder,

---

### 14. 2021_An_Ensemble_Methodology_for_Hierarchical_Probabilistic_EV_Load_Forecasting_at_Regular_Charging_Stations.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`mailto:nazir.refa@elaad.nl`](mailto:nazir.refa@elaad.nl)

- [`[https://www.elaad.nl`](https://www.elaad.nl)](https://www.elaad.nl`)

- [`mailto:gijs.van.der.poel@elaad.nl`](mailto:gijs.van.der.poel@elaad.nl)

- **📁 Key Dataset Text Snippets / Context**:
- > Applied Energy journal homepage: www.elsevier.com/locate/apenergy [https://doi.org/10.1016/j.apenergy.2020.116337](https://doi.org/10.1016/j.apenergy.2020.116337) Received 4 August 2020; Received in revised form 19 November 2020; Accepted 2 December 2020

- > the forecast lead time is indicated with k, and thus the forecast origin is h −k. To differentiate vectors from scalars, the former is indicated with bold symbols. For the sake of clarity, data (and forecasts) having hourly time resolution are considered; nevertheless, the proposal can be easily adapted to other time resolution frameworks.

- > of EV load at the high- level region for the target horizon h. This combination is performed through a PLQR model, which is applied to an input dataset that includes the baseline forecasts and historical high-level EV load data P = {P1,P2, ⋯, Pn, ⋯, Ph−k}. The penalization is applied to make the model more

- > 2.1. Data pre-processing unit The data pre-processing unit is described in this sub-Section considering the actual application to a large-scale charging dataset and a weather dataset, in order to comprehensively embrace the entire procedure to be followed to get the time series of EV load and the ar­

- > The data pre-processing unit is described in this sub-Section considering the actual application to a large-scale charging dataset and a weather dataset, in order to comprehensively embrace the entire procedure to be followed to get the time series of EV load and the ar­ ranged predictors for the probabilistic models.

---

### 15. 2021_Day_Ahead_Forecast_of_Electric_Vehicle_Charging_Demand_with_Deep_Neural_Networks.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/rebelosa/`](https://github.com/rebelosa/)](https://github.com/rebelosa/`)

- **📁 Key Dataset Text Snippets / Context**:
- > Vehicle Charging Demand with Deep Neural Networks. World Electr. Veh. J. 2021, 12, 178. [https://doi.org/](https://doi.org/) 10.3390/wevj12040178 Academic Editor: Peter Van den

- > and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

- > on the EV charging demand forecasting of small and large EV ﬂeets, and highlights the contribution of this research with respect to the literature gaps. Section 3 provides a World Electr. Veh. J. 2021, 12, 178. [https://doi.org/10.3390/wevj12040178](https://doi.org/10.3390/wevj12040178) [https://www.mdpi.com/journal/wevj](https://www.mdpi.com/journal/wevj) ·anmutacan/encantiles-

- > contribution of this research with respect to the literature gaps. Section 3 provides a World Electr. Veh. J. 2021, 12, 178. [https://doi.org/10.3390/wevj12040178](https://doi.org/10.3390/wevj12040178) [https://www.mdpi.com/journal/wevj](https://www.mdpi.com/journal/wevj) ·anmutacan/encantiles- 100 %

- > forecast, due to a higher stochastic behavior, short-term horizon, and high time resolution. Consequently, this paper builds on previous works by forecasting a small EV ﬂeet on a day-ahead horizon and on a 15 min timestep resolution. The small EV ﬂeet dataset is based on real data of a hospital semi-public charging site. To achieve better forecast results of such a difﬁcult use case, multiple new contributions are included such as additional input

---

### 16. 2021_Deep_Learning_Based_Probabilistic_Forecasting_of_Electric_Vehicle_Charging_Load_With_a_Novel_Queuing_Model.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Extracted Web Links**:
- [`[https://www.gov.uk/government/uploads/system/uploads/attac`](https://www.gov.uk/government/uploads/system/uploads/attac)](https://www.gov.uk/government/uploads/system/uploads/attac`)

- [`[https://orcid.org/0000-0001-7462-0753`](https://orcid.org/0000-0001-7462-0753)](https://orcid.org/0000-0001-7462-0753`)

- [`[http://tris.highwaysengland.co.uk/download/721b4186-feab-4691-`](http://tris.highwaysengland.co.uk/download/721b4186-feab-4691-)](http://tris.highwaysengland.co.uk/download/721b4186-feab-4691-`)

- [`[https://orcid.org/0000-0002-9586-2345`](https://orcid.org/0000-0002-9586-2345)](https://orcid.org/0000-0002-9586-2345`)

- [`[http://yann.lecun.com/exdb/lenet/`](http://yann.lecun.com/exdb/lenet/)](http://yann.lecun.com/exdb/lenet/`)

- **📁 Key Dataset Text Snippets / Context**:
- > University of Sydney, Camperdown, NSW 2006, Australia. Color versions of one or more ﬁgures in this article are available at [https://doi.org/10.1109/TCYB.2020.2975134.](https://doi.org/10.1109/TCYB.2020.2975134.) Digital Object Identiﬁer 10.1109/TCYB.2020.2975134 The errors in long-term EV charging load forecasts can cause

- > charging start times, travel distances, and charging durations were considered to study demand forecasting for the battery- swap stations in [5]. The half-hourly rolling vehicle-to-grid (V2G) capacity was estimated using the dynamic real-time EV scheduling based on an accurate EV load model that

- > ing process. The V2G capacity for regulation was estimated 2168-2267 c⃁2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:27:00 UTC from IEEE Xplore.  Restrictions apply.

- > data from weekdays and weekends during the four different seasons. The data for the ﬁrst two months of each season are chosen as the training dataset and the remaining one month of data are chosen as the testing dataset. The input data are decomposed using the WT approach into one approxima-

- > seasons. The data for the ﬁrst two months of each season are chosen as the training dataset and the remaining one month of data are chosen as the testing dataset. The input data are decomposed using the WT approach into one approxima- tion frequency and three detail frequencies. The structure of

---

### 17. 2021_Forecast_Enhanced_Lyapunov_Optimization_for_Real_Time_EV_Charging_Scheduling.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Extracted Web Links**:
- [`[https://arxiv.org/abs/2604.16873v1`](https://arxiv.org/abs/2604.16873v1)](https://arxiv.org/abs/2604.16873v1`)

- [`[https://www.gridstatus.io/`](https://www.gridstatus.io/)](https://www.gridstatus.io/`)

- **📁 Key Dataset Text Snippets / Context**:
- > horizon (e.g., from several minutes to a few hours). For example, a two-step learning framework was developed to forecast the half-hourly step electricity prices in [19], with an error of only 2.12% in predicting the peak electricity price. Wind power has been forecast by machine learning techniques

- > [19] S. Ghimire, R. C. Deo, D. Casillas-P´erez, and S. Salcedo-Sanz, “Two- step deep learning framework with error compensation technique for short-term, half-hourly electricity price forecasting,  Applied Energy, vol. 353, p. 122059, Jan. 2024. [20] P. Wang, J. Guo, F. Cheng, Y. Gu, F. Yuan, and F. Zhang, “A MPC-based

- > urban distribution systems,  Applied Energy, vol. 383, p. 125302, Apr. 2025. [24] “Grid Status,  [https://www.gridstatus.io/,](https://www.gridstatus.io/,) 2025. [25] K. G. Olivares, C. Challu, G. Marcjasz, R. Weron, and A. Dubrawski, “Neural basis expansion analysis with exogenous variables: Forecasting

---

### 18. 2021_Lim_TFT_Temporal_Fusion_Transformers.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/google-research/google-research/tree/master/tft`](https://github.com/google-research/google-research/tree/master/tft)](https://github.com/google-research/google-research/tree/master/tft`)

- [`[https://www.kaggle.com/c/favorita-grocery-sales-forecasting/`](https://www.kaggle.com/c/favorita-grocery-sales-forecasting/)](https://www.kaggle.com/c/favorita-grocery-sales-forecasting/`)

- **📁 Key Dataset Text Snippets / Context**:
- > cialized components to select relevant features and a series of gating layers to suppress unnecessary components, enabling high performance in a wide range of scenarios. On a variety of real-world datasets, we demonstrate signiﬁcant per- formance improvements over existing benchmarks, and showcase three practical interpretability use cases of TFT.

- > inputs, (3) a sequence-to-sequence layer to locally process known and observed inputs, and (4) a temporal self-attention decoder to learn any long-term depen- dencies present within the dataset. The use of these specialized components also facilitates interpretability; in particular, we show that TFT enables three valuable interpretability use cases: helping users identify (i) globally-important

- > variables for the prediction problem, (ii) persistent temporal patterns, and (iii) signiﬁcant events. On a variety of real-world datasets, we demonstrate how TFT can be practically applied, as well as the insights and beneﬁts it provides. 2. Related Work

- > we show that by interpreting attention patterns, TFT can provide insightful explanations about temporal dynamics, and do so while maintaining state-of- the-art performance on a variety of datasets. Time Series Interpretability with Attention: Attention mechanisms are used in translation [17], image classiﬁcation [22] or tabular learning [23]

- > use cases in Sec. 7 demonstrate that TFT is able to analyze global temporal relationships and allows users to interpret global behaviors of the model on the whole dataset – speci?cally in the identi?cation of any persistent patterns (e.g. seasonality or lag eﬀects) and regimes present. 3. Multi-horizon Forecasting

---

### 19. 2021_Reinforcement_Learning_Based_Load_Forecasting_of_Electric_Vehicle_Charging_Station_Using_Q_Learning_Technique.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0003-3532-5318`](https://orcid.org/0000-0003-3532-5318)](https://orcid.org/0000-0003-3532-5318`)

- [`[https://orcid.org/0000-0003-2254-5370`](https://orcid.org/0000-0003-2254-5370)](https://orcid.org/0000-0003-2254-5370`)

- [`[https://orcid.org/0000-0002-5373-8354`](https://orcid.org/0000-0002-5373-8354)](https://orcid.org/0000-0002-5373-8354`)

- [`[https://keras.io`](https://keras.io)](https://keras.io`)

- **📁 Key Dataset Text Snippets / Context**:
- > (e-mail: kavousi@sutech.ac.ir). Color versions of one or more of the ﬁgures in this article are available online at [https://ieeexplore.ieee.org.](https://ieeexplore.ieee.org.) Digital Object Identiﬁer 10.1109/TII.2020.2990397 accurate EV charging load demand forecasting is one of the key

- > energy consumption. The authors also took into account EVs uncertainty parameters, for example, the start time of charging, the duration of charging, the EVs hourly number for battery swapping, and the travel distance. While simulations with Monte Carlo technique are very precise, the behavior of EV owners has

- > complicated controllers’ real-time implementation, the deep 1551-3203 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 07:06:09 UTC from IEEE Xplore.  Restrictions apply.

- > literature, to reach the above goals [19], [20], different machine learning techniques are employed. Artiﬁcial neural network (ANN) was mainly employed in [21] for the data set that does not have a time dependency among the available datasets. Moreover, the recurrent neural networks (RNNs) are mostly employed for

- > learning techniques are employed. Artiﬁcial neural network (ANN) was mainly employed in [21] for the data set that does not have a time dependency among the available datasets. Moreover, the recurrent neural networks (RNNs) are mostly employed for the data set that is time-dependent. Some examples of RNN tech-

---

### 20. 2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/thuml/Autoformer`](https://github.com/thuml/Autoformer)](https://github.com/thuml/Autoformer`)

- **📁 Key Dataset Text Snippets / Context**:
- > of-the-art accuracy, with a 38% relative improvement on six benchmarks, covering ﬁve practical applications: energy, trafﬁc, economics, weather and disease. Code is available at this repository: [https://github.com/thuml/Autoformer.](https://github.com/thuml/Autoformer.) 1 Introduction

- > We extensively evaluate the proposed Autoformer on six real-world benchmarks, covering ﬁve mainstream time series forecasting applications: energy, trafﬁc, economics, weather and disease. Datasets Here is a description of the six experiment datasets: (1) ETT [48] dataset contains the data collected from electricity transformers, including load and oil temperature that are recorded every

- > mainstream time series forecasting applications: energy, trafﬁc, economics, weather and disease. Datasets Here is a description of the six experiment datasets: (1) ETT [48] dataset contains the data collected from electricity transformers, including load and oil temperature that are recorded every 6

- > 2.770 1.125 5.264 1.564 5.278 1.560 4.882 1.483 5.548 1.720 6.870 1.879 7.127 1.918 * ETT means the ETTm2. See Appendix A for the full benchmark of ETTh1, ETTh2, ETTm1. 15 minutes between July 2016 and July 2018. (2) Electricity1 dataset contains the hourly electricity consumption of 321 customers from 2012 to 2014. (3) Exchange [25] records the daily exchange rates of eight different countries ranging from 1990 to 2016. (4) Trafﬁc2 is a collection of hourly data

- > 15 minutes between July 2016 and July 2018. (2) Electricity1 dataset contains the hourly electricity consumption of 321 customers from 2012 to 2014. (3) Exchange [25] records the daily exchange rates of eight different countries ranging from 1990 to 2016. (4) Trafﬁc2 is a collection of hourly data from California Department of Transportation, which describes the road occupancy rates measured by different sensors on San Francisco Bay area freeways. (5) Weather3 is recorded every 10 minutes

---

### 21. 2021_Zhou_Informer_Beyond_Efficient_Transformer.pdf

- **Title**: An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations
- **Identified Datasets**: ElaadNL Public EV Charging Network Dataset (Netherlands)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/zhouhaoyi/ETDataset`](https://github.com/zhouhaoyi/ETDataset)](https://github.com/zhouhaoyi/ETDataset`)

- [`[https://github.com/`](https://github.com/)](https://github.com/`)

- [`[https://github`](https://github)](https://github`)

- [`[https://github.com/zhouhaoyi/Informer2020`](https://github.com/zhouhaoyi/Informer2020)](https://github.com/zhouhaoyi/Informer2020`)

- **📁 Key Dataset Text Snippets / Context**:
- > a step-by-step way, which drastically improves the inference speed of long-sequence predictions. Extensive experiments on four large-scale datasets demonstrate that Informer sig- niﬁcantly outperforms existing methods and provides a new solution to the LSTF problem.

- > to the point where this trend is holding the research on LSTF. As an empirical example, Fig.(1) shows the forecasting re- sults on a real dataset, where the LSTM network predicts the 2d 4d

- > mance. E.g., starting from length=48, MSE rises unaccept- ably high, and the inference speed drops rapidly. hourly temperature of an electrical transformer station from the short-term period (12 points, 0.5 days) to the long-term period (480 points, 20 days). The overall performance gap

- > 0 0 Table 1: Univariate long sequence time-series forecasting results on four datasets (ﬁve cases). 4 Experiment

- > 4 Experiment Datasets We extensively perform experiments on four datasets, in- cluding 2 collected real-world datasets for LSTF and 2 pub-

---

### 22. 2022_GCN_TRN_Efficient_Transformer_based_Electric_Vehicle_Charging_Demand_Forecasting_System.pdf

- **Title**: Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events
- **Identified Datasets**: Metropolitan Load Data (Boston, Seattle, Chicago, Philadelphia), Country-Level Load Data (Germany, France, Northern Italy), Google/Apple Mobility Index
- **🔗 Extracted Web Links**:
- [`[https://doi.org/10.1145/3569966.3570101`](https://doi.org/10.1145/3569966.3570101)](https://doi.org/10.1145/3569966.3570101`)

- **📁 Key Dataset Text Snippets / Context**:
- > both spatial and temporal data related EV Charging Station Avail- ability. The model is tested for its performances using the Dundee City dataset. And the result reflects that our model surpassed an accuracy of 80% and attained more accurate predictions than the classic baselines.

- > International Conference on Computer Science and Software Engineering (CSSE 2022) (CSSE 2022), October 21–23, 2022, Guilin, China. ACM, New York, NY, USA, 7 pages. [https://doi.org/10.1145/3569966.3570101](https://doi.org/10.1145/3569966.3570101) Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed

- > © 2022 Association for Computing Machinery. ACM ISBN 978-1-4503-9778-0/22/10...$15.00 [https://doi.org/10.1145/3569966.3570101](https://doi.org/10.1145/3569966.3570101) 1 INTRODUCTION

- > Data Description In this section, we evaluate the accuracy and effectiveness of our newly proposed model using the dataset of the Dundee EV Charging Station from February 13 2018 to February 28 2018. During the described time period, there were a total of 2746 usage records and

- > (12) (4)The Explained Variance Score is the dispersion of the errors of a dataset: ???= 1 −???

---

### 23. 2022_Kim_RevIN_Reversible_Instance_Normalization.pdf

- **Title**: Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events
- **Identified Datasets**: Metropolitan Load Data (Boston, Seattle, Chicago, Philadelphia), Country-Level Load Data (Germany, France, Northern Italy), Google/Apple Mobility Index
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/zhouhaoyi/ETDataset`](https://github.com/zhouhaoyi/ETDataset)](https://github.com/zhouhaoyi/ETDataset`)

- [`[https://github.com/cure-lab/SCINet`](https://github.com/cure-lab/SCINet)](https://github.com/cure-lab/SCINet`)

- [`[https://github.com/zhouhaoyi/Informer2020`](https://github.com/zhouhaoyi/Informer2020)](https://github.com/zhouhaoyi/Informer2020`)

- **📁 Key Dataset Text Snippets / Context**:
- > Figure 1: Multivariate time-series forecasting results comparing our method with the state-of-the-art baselines, i.e., Informer (Zhou et al., 2021), N-BEATS (Oreshkin et al., 2020), and SCINet (Liu et al., 2021). The analysis is conducted on electricity consuming load (ECL) dataset, with a prediction length of seven days. The predictions of the baselines are inaccurately (a) shifted and (b) scaled. When adopted to the baselines, our method signiﬁcantly improves their forecasting performance

- > performance improvements in time-series forecasting, as shown in Fig. 1. We demonstrate the effectiveness of RevIN via extensive quantitative and qualitative analyses on various real-world datasets, addressing the distribution shift problem. ∗Both authors contributed equally. The order of the ﬁrst authors was determined by coin ﬂip. 1

- > arbitrary deep neural networks with negligible cost. • By adding RevIN to the baseline, we achieve state-of-the-art performance on seven large- scale real-world datasets by a signiﬁcant margin. • We conduct extensive evaluations of RevIN using quantitative analysis and qualitative vi- sualizations to verify its effectiveness, addressing the distribution shift problem.

- > spired by statistical models, N-BEATS (Oreshkin et al., 2020) designed an interpretable layer for time-series forecasting by encouraging the model to learn trend, seasonality explicitly, and residual components. This model shows superior performance on the M4 competition dataset. Distribution shift. Although there are various models for time-series forecasting, they often suf-

- > sequential process in RevIN: (a) the original input x, (b) the input ˆx normalized by RevIN, (c) the model prediction output ˜y, and (d) the output ˆy denormalized by RevIN, the ?nal prediction. The analysis is conducted on the ETT and ECL datasets using SCINet (Liu et al., 2021) as the baseline. reciprocal of the normalization in Eq. 2 (Fig. 2(a-3)) as ˆy(i)

---

### 24. 2022_Robust_Deep_Gaussian_Process_Based_Probabilistic_Electrical_Load_Forecasting_Against_Anomalous_Events.pdf

- **Title**: Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events
- **Identified Datasets**: Metropolitan Load Data (Boston, Seattle, Chicago, Philadelphia), Country-Level Load Data (Germany, France, Northern Italy), Google/Apple Mobility Index
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/chennnnnyize/Load-Forecasting-During-COVID-19`](https://github.com/chennnnnyize/Load-Forecasting-During-COVID-19)](https://github.com/chennnnnyize/Load-Forecasting-During-COVID-19`)

- **📁 Key Dataset Text Snippets / Context**:
- > zch@et.aau.dk; fbl@et.aau.dk). Color versions of one or more ﬁgures in this article are available at [https://doi.org/10.1109/TII.2021.3081531.](https://doi.org/10.1109/TII.2021.3081531.) Digital Object Identiﬁer 10.1109/TII.2021.3081531 I. MOTIVATIONS AND CONTRIBUTIONS

- > power generation dispatch is to meet the load demand, good 1551-3203 © 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:57:42 UTC from IEEE Xplore.  Restrictions apply.

- > 3) Comprehensive comparisons with other benchmark ma- chine learning methods have been carried out using a series of datasets at both the city and country level. It shows that our proposed approach has a better capability of dealing with anomalous events with a limited number

- > the prediction of future loads. Three different kernels have been evaluated in [26]. The selection of covariance kernel function requires expert knowledge of the dataset, which is difﬁcult to obtain when dealing with unforeseen scenarios, such as the COVID-19. This article builds on the DGP and develops a new

- > the COVID-19 pandemic, the unprecedented changes in con- sumption patterns and the magnitude of load demand make it difﬁcult to construct a good dataset that is sufﬁcient for the training of parametric methods, especially at the beginning of the pandemic. Also, the parametric methods cannot be directly

---

### 25. 2023_MetaProbformer_for_Charging_Load_Probabilistic_Forecasting_of_Electric_Vehicle_Charging_Stations.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://facebook.github.io/prophet/`](https://facebook.github.io/prophet/)](https://facebook.github.io/prophet/`)

- [`[https://github.com/XingshuaiHuang/MetaProbformer`](https://github.com/XingshuaiHuang/MetaProbformer)](https://github.com/XingshuaiHuang/MetaProbformer`)

- [`[https://platform.elaad.io/analyses/ElaadNL_opendata.php`](https://platform.elaad.io/analyses/ElaadNL_opendata.php)](https://platform.elaad.io/analyses/ElaadNL_opendata.php`)

- [`[https://open-data.bouldercolorado.gov/datasets/`](https://open-data.bouldercolorado.gov/datasets/)](https://open-data.bouldercolorado.gov/datasets/`)

- **📁 Key Dataset Text Snippets / Context**:
- > adapt fast to unseen environments, we further extend it to MetaProbformer, a meta-learning-based forecasting framework. Extensive experiments have been done on real-world datasets for both point forecasting and probabilistic forecasting. Experimental results show that our methods can consistently outperform

- > research [21], [22] combined Transformer-based architecture 1558-0016 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:49:52 UTC from IEEE Xplore.  Restrictions apply.

- > named MetaProbformer is presented by combining Probformer with a meta-learning algorithm. (III) Experiments on real-world datasets demonstrate the superior performance of the proposed forecasting framework on point and probabilistic forecasting, short-term and long-

- > load forecasting. Then [11] proposed a new ARIMA method that further adapted ARMA to non-stationary time series through differencing for hourly load forecasting. Moreover, some variants of ARIMA [24], [25] applied to load forecasting improve the ARIMA model at the individual, aggregated

- > and seasonal levels, respectively [26]. In addition to the above-mentioned autoregressive methods, a linear Gaussian state space model [27] was also utilized to make hourly load forecasting. Furthermore, [28] employed Kalman Fil- tering to forecast short-term power load and control load

---

### 26. 2023_Multi_Branch_ResNet_Transformer_for_Short_Term_Spatio_Temporal_Solar_Irradiance_Forecasting.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0001-9189-5150`](https://orcid.org/0000-0001-9189-5150)](https://orcid.org/0000-0001-9189-5150`)

- [`[https://orcid.org/0000-0003-1022-2021`](https://orcid.org/0000-0003-1022-2021)](https://orcid.org/0000-0003-1022-2021`)

- [`[https://orcid.org/0000-0002-2663-0751`](https://orcid.org/0000-0002-2663-0751)](https://orcid.org/0000-0002-2663-0751`)

- [`[https://orcid.org/0000-0002-5464-1773`](https://orcid.org/0000-0002-5464-1773)](https://orcid.org/0000-0002-5464-1773`)

- **📁 Key Dataset Text Snippets / Context**:
- > z.zhao@temple.edu; ldu@temple.edu; sbiswas@temple.edu). Color versions of one or more ﬁgures in this article are available at [https://doi.org/10.1109/TIA.2023.3285202.](https://doi.org/10.1109/TIA.2023.3285202.) Digital Object Identiﬁer 10.1109/TIA.2023.3285202 m

- > volatility in high penetration of DERs, especially ubiquitous 0093-9994 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 09:15:17 UTC from IEEE Xplore.  Restrictions apply.

- > the National Solar Radiation Database (NSRDB) [26], which is widely used to examine solar irradiance forecasting perfor- mances. The collected dataset consists of 18 sites in Philadel- phia, Pennsylvania, from 2000 and 2017 with a 30-minute interval. For performance evaluation, 12 sites are choose in south

- > the ﬁrst 12 sites. All chosen solar sites’ geological locations are depicted in Fig. 7. The dataset contains not only the historical GHI (W/m2), DHI (W/m2), and DNI (W/m2) but also the clear-sky GHI (W/m2), clear-sky DHI (W/m2), and clear-sky DNI (W/m2)

- > solar zenith angle (◦), wind speed (m/s), precipitable water (mm), wind direction (◦), relative humidity (%), temperature (◦C), pressure (mb), and cloud type. All variables in the dataset are numerical except cloud type, which will be converted to one-hot code. All variables’ descriptive statistics are presented

---

### 27. 2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/zhouhaoyi/ETDataset`](https://github.com/zhouhaoyi/ETDataset)](https://github.com/zhouhaoyi/ETDataset`)

- [`[https://github.com/laiguokun/multivariate-time-series-data`](https://github.com/laiguokun/multivariate-time-series-data)](https://github.com/laiguokun/multivariate-time-series-data`)

- **📁 Key Dataset Text Snippets / Context**:
- > We also apply our model to self-supervised pre- training tasks and attain excellent ﬁne-tuning performance, which outperforms supervised training on large datasets. Transferring of masked pre-trained repre- sentation on one dataset to others also produces SOTA forecasting accuracy. 1

- > training tasks and attain excellent ﬁne-tuning performance, which outperforms supervised training on large datasets. Transferring of masked pre-trained repre- sentation on one dataset to others also produces SOTA forecasting accuracy. 1 INTRODUCTION

- > 0.410 Running time (s) with L = 336 Dataset w. patch w.o. patch

- > 680 x 4 Table 1: A case study of multivariate time series forecasting on Trafﬁc dataset. The prediction hori- zon is 96. Results with different look-back window L and number of input tokens N are reported. The best result is in bold and the second best is underlined. Down-sampled means sampling every

- > from a single channel. This was proven to work well with CNN (Zheng et al., 2014) and linear models (Zeng et al., 2022), but hasn’t been applied to Transformer-based models yet. We offer a snapshot of our key results in Table 1 by doing a case study on Trafﬁc dataset, which consists of 862 time series. Our model has several advantages: 1. Reduction on time and space complexity: The original Transformer has O(N 2) complexity

---

### 28. 2023_Prediction_of_Electric_Vehicles_Charging_Demand_A_Transformer_Based_Deep_Learning_Approach.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary`](https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary)](https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary`)

- [`[https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2`](https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2)](https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2`)

- [`[https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv`](https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv)](https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv`)

- [`[https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore`](https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore)](https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore`)

- **📁 Key Dataset Text Snippets / Context**:
- > Transformer-Based Deep Learning Approach. Sustainability 2023, 15, 2105. [https://doi.org/10.3390/](https://doi.org/10.3390/) su15032105 Academic Editor: Lei Zhang

- > and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).

- > Under these circumstances, accurate EV charging load prediction is an essential foun- dation for evaluating the impact of the EVs on the power grid and planning and operating Sustainability 2023, 15, 2105. [https://doi.org/10.3390/su15032105](https://doi.org/10.3390/su15032105) [https://www.mdpi.com/journal/sustainability](https://www.mdpi.com/journal/sustainability)

- > dation for evaluating the impact of the EVs on the power grid and planning and operating Sustainability 2023, 15, 2105. [https://doi.org/10.3390/su15032105](https://doi.org/10.3390/su15032105) [https://www.mdpi.com/journal/sustainability](https://www.mdpi.com/journal/sustainability)

- > for predicting building energy loads using neuron node numbers [17]. The LSTM showed the greatest performance in a study by Kong et al. that applied it to the forecasting of residential load [18]. Similarly, Lu et al. applied different neural network models for hourly level aggregated EV load forecasting, and according to the backtesting results, LSTM outperformed other models [19].

---

### 29. 2023_Wu_TimesNet_Temporal_2D_Variation_Modeling.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/M4Competition/M4-methods/tree/master/Dataset`](https://github.com/M4Competition/M4-methods/tree/master/Dataset)](https://github.com/M4Competition/M4-methods/tree/master/Dataset`)

- [`[https://github.com/M4Competition/`](https://github.com/M4Competition/)](https://github.com/M4Competition/`)

- [`[https://github.com/thuml/TimesNet`](https://github.com/thuml/TimesNet)](https://github.com/thuml/TimesNet`)

- **📁 Key Dataset Text Snippets / Context**:
- > consistent state-of-the-art in ﬁve mainstream time series analysis tasks, including short- and long-term forecasting, imputation, classiﬁcation, and anomaly detection. Code is available at this repository: [https://github.com/thuml/TimesNet.](https://github.com/thuml/TimesNet.) 1 INTRODUCTION

- > including short- and long-term forecasting, imputation, classiﬁcation and anomaly detection. Implementation Table 1 is a summary of benchmarks. More details about the dataset, experiment implementation and model conﬁguration can be found in Appendix A. Table 1: Summary of experiment benchmarks.

- > benchmarks used in Autoformer (2021), including ETT (Zhou et al., 2021), Electricity (UCI), Trafﬁc (PeMS), Weather (Wetterstation), Exchange (Lai et al., 2018) and ILI (CDC), covering ﬁve real-world applications. For the short-term dataset, we adopt the M4 (Spyros Makridakis, 2018), which contains the yearly, quarterly and monthly collected univariate marketing data. Note that each dataset in the long-term setting only contains one continuous time series, where we obtain samples by sliding

- > (PeMS), Weather (Wetterstation), Exchange (Lai et al., 2018) and ILI (CDC), covering ﬁve real-world applications. For the short-term dataset, we adopt the M4 (Spyros Makridakis, 2018), which contains the yearly, quarterly and monthly collected univariate marketing data. Note that each dataset in the long-term setting only contains one continuous time series, where we obtain samples by sliding window, while M4 involves 100,000 different time series collected in different frequencies.

- > 2.139 0.931 2.497 1.004 7.382 2.003 2.616 1.090 2.847 1.144 2.077 0.914 3.006 1.161 7.635 2.050 5.137 1.544 4.839 1.485 4.724 1.445 Table 3: Short-term forecasting task on M4. The prediction lengths are in [6, 48] and results are weighted averaged from several datasets under different sample intervals. See Table 14 for full results. Models TimesNet N-HiTS N-BEATS ETSformer LightTS DLinear FEDformer Stationary Autoformer Pyraformer Informer LogTrans Reformer (Ours)

---

### 30. 2023_Zeng_DLinear_Are_Transformers_Effective_LTSF.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/zhouhaoyi/ETDataset`](https://github.com/zhouhaoyi/ETDataset)](https://github.com/zhouhaoyi/ETDataset`)

- [`[https://github.com/laiguokun/multivariate-time-series-data`](https://github.com/laiguokun/multivariate-time-series-data)](https://github.com/laiguokun/multivariate-time-series-data`)

- [`[https://github.com/cure-lab/LTSF-Linear`](https://github.com/cure-lab/LTSF-Linear)](https://github.com/cure-lab/LTSF-Linear`)

- [`[https://github.com/cure-lab/LTSF-`](https://github.com/cure-lab/LTSF-)](https://github.com/cure-lab/LTSF-`)

- **📁 Key Dataset Text Snippets / Context**:
- > for comparison. Experimental results on nine real-life datasets show that LTSF-Linear surprisingly outperforms existing sophisticated Transformer-based LTSF models in all cases, and often by a large margin. Moreover, we con-

- > Transformer-based solutions for other time series analysis tasks (e.g., anomaly detection) in the future. Code is avail- able at: [https://github.com/cure-lab/LTSF-](https://github.com/cure-lab/LTSF-) Linear. 1. Introduction

- > ical time series with a one-layer linear model to forecast fu- ture time series directly. We conduct extensive experiments on nine widely-used benchmark datasets that cover various real-life applications: trafﬁc, energy, economics, weather, and disease predictions. Surprisingly, our results show that

- > trend in the data. • Meanwhile, to boost the performance of LTSF-Linear when there is a distribution shift in the dataset, NLin- ear ﬁrst subtracts the input by the last value of the se- quence. Then, the input goes through a linear layer,

- > 5. Experiments 5.1. Experimental Settings Dataset. We conduct extensive experiments on nine widely-used real-world datasets, including ETT (Electricity

---

### 31. 2023_Zhang_Crossformer_Cross_Dimension_Dependency.pdf

- **Title**: MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations
- **Identified Datasets**: City of Palo Alto EV Dataset, Boulder Colorado EV Dataset, ElaadNL Public EV Dataset, Perth UK EV Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/Thinklab-SJTU/Crossformer`](https://github.com/Thinklab-SJTU/Crossformer)](https://github.com/Thinklab-SJTU/Crossformer`)

- [`[https://github.com/nnzhan/MTGNN`](https://github.com/nnzhan/MTGNN)](https://github.com/nnzhan/MTGNN`)

- [`[https://github.com/laiguokun/LSTNet`](https://github.com/laiguokun/LSTNet)](https://github.com/laiguokun/LSTNet`)

- [`[https://github.com/alipay/Pyraformer`](https://github.com/alipay/Pyraformer)](https://github.com/alipay/Pyraformer`)

- [`[https://github.com/MAZiqing/FEDformer`](https://github.com/MAZiqing/FEDformer)](https://github.com/MAZiqing/FEDformer`)

- [`[https://github.com/thuml/Autoformer`](https://github.com/thuml/Autoformer)](https://github.com/thuml/Autoformer`)

- [`[https://github.com/thuml/`](https://github.com/thuml/)](https://github.com/thuml/`)

- [`[https://github.com/zhouhaoyi/Informer2020`](https://github.com/zhouhaoyi/Informer2020)](https://github.com/zhouhaoyi/Informer2020`)

- [`[https://github.com/zhouhaoyi/`](https://github.com/zhouhaoyi/)](https://github.com/zhouhaoyi/`)

- **📁 Key Dataset Text Snippets / Context**:
- > {zhangyunhao, yanjunchi}@sjtu.edu.cn Code: [https://github.com/Thinklab-SJTU/Crossformer](https://github.com/Thinklab-SJTU/Crossformer) ABSTRACT Recently many deep models have been proposed for multivariate time series (MTS)

- > Utilizing DSW embedding and TSA layer, Crossformer establishes a Hierarchical Encoder-Decoder (HED) to use the information at different scales for the ﬁnal forecasting. Extensive experimental results on six real-world datasets show the effectiveness of Crossformer against previous state-of-the-arts. 1

- > the number of segments L in cross-time stage. While in Cross-Dimension Stage, we can not partition dimensions and directly apply MSA will cause the complexity of O(D2) (as shown in Fig. 2 (b)), which is unaffordable for datasets with large D. Instead, we propose the router mechanism for potentially large D. As shown in Fig. 2 (c), we set a small ﬁxed number (c << D) of learnable vectors for each time step i as routers. These routers ﬁrst aggregate messages from all dimensions by

- > Published as a conference paper at ICLR 2023 Table 1: MSE/MAE with different prediction lengths. Bold/underline indicates the best/second. Results of LSTMa, LSTnet, Transformer, Informer on the ﬁrst 4 datasets are from Zhou et al. (2021). Models LSTMa

- > 4.1 PROTOCOLS Datasets We conduct experiments on six real-world datasets following Zhou et al. (2021); Wu et al. (2021a). 1) ETTh1 (Electricity Transformer Temperature-hourly), 2) ETTm1 (Electricity

---

### 32. 2024_A_Physics_Informed_and_Attention_Based_Graph_Learning_Approach_for_Regional_Electric_Vehicle_Charging_Demand_Prediction.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://quhaoh233.github.io/page/`](https://quhaoh233.github.io/page/)](https://quhaoh233.github.io/page/`)

- [`[https://github.com/IntelligentSystemsLab/ST-EVCDP`](https://github.com/IntelligentSystemsLab/ST-EVCDP)](https://github.com/IntelligentSystemsLab/ST-EVCDP`)

- **📁 Key Dataset Text Snippets / Context**:
- > duces physics-informed meta-learning in the pre-training step to facilitate prior knowledge learning. Evaluation results on a dataset of 18,061 EV charging piles in Shenzhen, China, show that the proposed approach can achieve state-of-the-art forecasting performance and the ability to understand the adaptive changes

- > is data-induced and therefore prevalent in existing data-driven 1558-0016 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:58:12 UTC from IEEE Xplore.  Restrictions apply.

- > with high accuracy and correct interpretation. 4) Through a rigorous evaluation based on a real-world dataset with samples of 18,061 EV charging piles, the effectiveness of the proposed model is demonstrated, including its ability to understand the complex relation-

- > (9) The two kinds of tuning samples can be merged to form the tuning dataset. Even though such pairs of impulses and responses cannot fully express the complex patterns in the real world, it is sufficient to make the initial parameters inclined

- > IV. MODEL EVALUATION In this section, the proposed approach is evaluated on an EV charging dataset collected in Shenzhen and compared with other representative prediction models. Note that the datasets and code used in this paper are shared in Github,

---

### 33. 2024_A_Reliable_Evaluation_Metric_for_Electrical_Load_Forecasts_in_V2G_Scheduling_Considering_Statistical_Features_of_EV_Charging.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Extracted Web Links**:
- [`[https://insideevs.com/news/631099/us-bev-dominated-us-made-models/`](https://insideevs.com/news/631099/us-bev-dominated-us-made-models/)](https://insideevs.com/news/631099/us-bev-dominated-us-made-models/`)

- [`[https://orcid.org/0000-0002-5246-2835`](https://orcid.org/0000-0002-5246-2835)](https://orcid.org/0000-0002-5246-2835`)

- [`[https://orcid.org/0009-0008-4738-4861`](https://orcid.org/0009-0008-4738-4861)](https://orcid.org/0009-0008-4738-4861`)

- [`[https://www.ausgrid.com.au/Industry/Our-Research/Data-to-`](https://www.ausgrid.com.au/Industry/Our-Research/Data-to-)](https://www.ausgrid.com.au/Industry/Our-Research/Data-to-`)

- [`[https://cm.asu.edu`](https://cm.asu.edu)](https://cm.asu.edu`)

- **📁 Key Dataset Text Snippets / Context**:
- > zyshao@gzhu.edu.cn). Color versions of one or more ﬁgures in this article are available at [https://doi.org/10.1109/TSG.2024.3392910.](https://doi.org/10.1109/TSG.2024.3392910.) Digital Object Identiﬁer 10.1109/TSG.2024.3392910 Considering the interests of different stakeholders, a broad

- > forecasts at decision-making stages. Herein, V2G scheduling 1949-3053 c⃁2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:46:18 UTC from IEEE Xplore.  Restrictions apply.

- > IV. PROPOSED V2G SCHEDULING VALUE-ORIENTED METRIC Given that the datasets capturing EV charging behav- ior are generated using the statistical features delineated in Section III-A, myriad EV charging datasets satisfying

- > Given that the datasets capturing EV charging behav- ior are generated using the statistical features delineated in Section III-A, myriad EV charging datasets satisfying these criteria can be created. However, the V2G scheduling performance derived from each dataset is different, i.e., the

- > in Section III-A, myriad EV charging datasets satisfying these criteria can be created. However, the V2G scheduling performance derived from each dataset is different, i.e., the scheduling result obtained by this way is not representative, indicating that the result of the optimization problem cannot

---

### 34. 2024_Day_ahead_electric_vehicle_charging_behavior_forecasting_and_schedulable_capacity_calculation_for_electric_vehicle_parking_lot.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Extracted Web Links**:
- [`[https://doi.org/`](https://doi.org/)](https://doi.org/`)

- [`[http://orca.cf.ac.uk/policies.html`](http://orca.cf.ac.uk/policies.html)](http://orca.cf.ac.uk/policies.html`)

- [`[https://doi.org/10.1145/3292500.3330936`](https://doi.org/10.1145/3292500.3330936)](https://doi.org/10.1145/3292500.3330936`)

- [`[https://dl.acm.org/doi/epdf/10.5555/1283383.1283494`](https://dl.acm.org/doi/epdf/10.5555/1283383.1283494)](https://dl.acm.org/doi/epdf/10.5555/1283383.1283494`)

- [`[https://doi.org/10.1007/s40565-019-00573-3`](https://doi.org/10.1007/s40565-019-00573-3)](https://doi.org/10.1007/s40565-019-00573-3`)

- **📁 Key Dataset Text Snippets / Context**:
- > ORCA – Online Research @ Cardiff This is an Open Access document downloaded from ORCA, Cardiff University's institutional repository:[https://orca.cardiff.ac.uk/id/eprint/172146/](https://orca.cardiff.ac.uk/id/eprint/172146/) This is the author’s version of a work that was submitted to / accepted for publication.

- > Cardiff This is an Open Access document downloaded from ORCA, Cardiff University's institutional repository:[https://orca.cardiff.ac.uk/id/eprint/172146/](https://orca.cardiff.ac.uk/id/eprint/172146/) This is the author’s version of a work that was submitted to / accepted for publication. Citation for final published version:

- > vehicle charging behavior forecasting and schedulable capacity calculation for electric vehicle parking lot. Energy 309 , 133090. 10.1016/j.energy.2024.133090 Publishers page: [https://doi.org/10.1016/j.energy.2024.133090](https://doi.org/10.1016/j.energy.2024.133090) Please note: Changes made as a result of publishing processes such as copy-editing, formatting and page numbers may

- > source. You are advised to consult the publisher’s version if you wish to cite this paper. This version is being made available in accordance with publisher policies. See [http://orca.cf.ac.uk/policies.html](http://orca.cf.ac.uk/policies.html) for usage policies. Copyright and moral rights for publications made available in ORCA are retained by the copyright holders.

- > ??,???-??,??? ? Clustering input dataset ?? Typical set of EVCB in m-th period

---

### 35. 2024_DiffPLF_Conditional_Diffusion_Probabilistic_Forecasting_EV_Charging.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-`](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-)](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-`)

- [`[https://github.com/LSY-Cython/DiffPLF`](https://github.com/LSY-Cython/DiffPLF)](https://github.com/LSY-Cython/DiffPLF`)

- [`[https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-usage-of-california-city`](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-usage-of-california-city)](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-usage-of-california-city`)

- **📁 Key Dataset Text Snippets / Context**:
- > adapted to various prediction horizons and execute controllable generation conditioned on different EV numbers. Our code is publicly available at [https://github.com/LSY-Cython/DiffPLF](https://github.com/LSY-Cython/DiffPLF) for better study of EV grid integration. II. PROBLEM FORMULATION

- > V. NUMERICAL EXPERIMENTS A. Experimental Setup 1) Data description: We harness a real-world dataset in the city of Palo Alto, California termed EV Charging Station Us- age Open Data1. It elaborates daily charging session details of

- > 1) Data description: We harness a real-world dataset in the city of Palo Alto, California termed EV Charging Station Us- age Open Data1. It elaborates daily charging session details of individual stations, including charging durations and delivered 1[https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-)

- > age Open Data1. It elaborates daily charging session details of individual stations, including charging durations and delivered 1[https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-) usage-of-california-city 23rd Power Systems Computation Conference

- > that when running DiffPLF on every test sample, we generate 1000 future charging load profiles in parallel. 2[https://dev.meteostat.net/](https://dev.meteostat.net/) Fig. 5. Randomly selected testing samples. In each subplot, we depict the

---

### 36. 2024_Divide_Conquer_Transformer_Predicting_EV_Charging_Events_Smart_Meter.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://www.pecanstreet.org/dataport/`](https://www.pecanstreet.org/dataport/)](https://www.pecanstreet.org/dataport/`)

- **📁 Key Dataset Text Snippets / Context**:
- > for predicting EV charging events several minutes ahead with high accuracy based on smart meter data. We evaluate our proposed method using a real-world dataset and compare it with four representative machine learning and deep learning models arXiv:2403.13246v1  [cs.LG]  20 Mar 2024

- > serve EV charging event prediction. • Extensive experiments and insights into EV charging event prediction using real-world datasets: Our method, DCT-EV, outperforms benchmark models, establishing a new state-of-the-art in providing both 10-minute and 60-

- > presents the design of our DCT-EV model. Section III presents the experimental results, including comparisons between DCT- EV and benchmark models on a real-world dataset and the discussion of the evaluation results. Section IV concludes the paper and outlines some future work directions.

- > In our experiment, we preprocess minute-interval residential electricity meter data with EV charging load records in 2018 from Pecan Street [27]. The dataset provides smart meter data aligned with EV charging profiles, which will be used to construct EV charging label for the experiment. After analyzing

- > first 80% of each home’s records are for model training, the remaining 20% are reserved for testing. The dataset exhibits an imbalance, primarily because EV charging events occur for only a few hours per week, resulting in limited EV charging records. As a classification problem,

---

### 37. 2024_Electric_vehicles_load_forecasting_for_day_ahead_market_participation_using_machine_and_deep_learning_methods.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://ev.caltech.edu/dataset`](https://ev.caltech.edu/dataset)](https://ev.caltech.edu/dataset`)

- **📁 Key Dataset Text Snippets / Context**:
- > • Evaluation of forecasting in specific horizon required for DAM participation. • Nine diverse EV Load Curves forecasting methods. • Forecasts are evaluated on four public, real-world EV datasets. • Evaluation for a year-long period and diverse characteristics of EV charging data. • Methodology for constructing EV Load Curve from session-based tabular EV dataset.

- > • Forecasts are evaluated on four public, real-world EV datasets. • Evaluation for a year-long period and diverse characteristics of EV charging data. • Methodology for constructing EV Load Curve from session-based tabular EV dataset. A R T I C L E I N F O Keywords:

- > crucial. This paper presents an extensive investigation of nine diverse EVLC forecasting methodologies, encompassing statistical, machine learning, and deep learning techniques. These methodologies are evaluated on four public, real-world EV datasets, keeping in line with the specific forecasting horizon required for DAM. The study incorporates models with and without online historical data, ensuring broad applicability across varied data availability scenarios. An exploration of seasonal variations in forecasting performance is conducted via one

- > four public, real-world EV datasets, keeping in line with the specific forecasting horizon required for DAM. The study incorporates models with and without online historical data, ensuring broad applicability across varied data availability scenarios. An exploration of seasonal variations in forecasting performance is conducted via one year-long rolling simulations, providing deep insight on seasonal patterns. Furthermore, a detailed methodology for constructing EVLCs from session-based, tabular EV datasets is presented. The conducted research establishes a

- > data availability scenarios. An exploration of seasonal variations in forecasting performance is conducted via one year-long rolling simulations, providing deep insight on seasonal patterns. Furthermore, a detailed methodology for constructing EVLCs from session-based, tabular EV datasets is presented. The conducted research establishes a first-of-its-kind comprehensive comparison of EVLC forecasting methodologies for the real-world challenge of DAM participation. The research results provide indispensable guidance to wholesale electricity market partic­

---

### 38. 2024_Energy_Consumption_Prediction_Strategy_for_Electric_Vehicle_Based_on_LSTM_Transformer_Framework.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Extracted Web Links**:
- [`[https://ssrn.com/abstract=4747046`](https://ssrn.com/abstract=4747046)](https://ssrn.com/abstract=4747046`)

- [`[https://www.visualcrossing.com/`](https://www.visualcrossing.com/)](https://www.visualcrossing.com/`)

- [`[https://www.visualcrossing.com`](https://www.visualcrossing.com)](https://www.visualcrossing.com`)

- **📁 Key Dataset Text Snippets / Context**:
- > captures characteristics of time-series data with increased efficiency. Upon rigorous evaluation, the model achieved the mean absolute percentage error (MAPE) of 4.63% for state of charge (SOC) of EV’s battery in experimental dataset, outperforming LSTM and multivariate regression (MLR). The ablation experiment shows that the MAPE of the model is reduced by 18.47% and 15.27% respectively after considering the

- > types of vehicles. Based on this framework, a long-distance EV energy consumption prediction strategy based on short-distance is proposed, with a MAPE of 6.7% when SOC value is reduced from 90 to 40 in the selected dataset. *Corresponding author. E-mail address: jianzhang@seu.edu.cn (Zhang Jian).

- > *Corresponding author. E-mail address: jianzhang@seu.edu.cn (Zhang Jian). This preprint research paper has not been peer reviewed. Electronic copy available at: [https://ssrn.com/abstract=4747046](https://ssrn.com/abstract=4747046) Preprint not peer reviewed

- > renewable energy sources, thus diminishing greenhouse gas emissions. Concurrently, precise predictions of vehicle energy consumption contribute to the reduction of This preprint research paper has not been peer reviewed. Electronic copy available at: [https://ssrn.com/abstract=4747046](https://ssrn.com/abstract=4747046) Preprint not peer reviewed

- > speed [9] and found that the energy utilization of EVs in urban road environments was higher than that in highway scenarios [22]. Moreover, effectively controlling This preprint research paper has not been peer reviewed. Electronic copy available at: [https://ssrn.com/abstract=4747046](https://ssrn.com/abstract=4747046) Preprint not peer reviewed

---

### 39. 2024_Feature_enhanced_deep_learning_method_for_electric_vehicle_charging_demand_probabilistic_forecasting_of_charging_station.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/Kenny4everlucky/FEDQR_dataset`](https://github.com/Kenny4everlucky/FEDQR_dataset)](https://github.com/Kenny4everlucky/FEDQR_dataset`)

- **📁 Key Dataset Text Snippets / Context**:
- > Applied Energy journal homepage: www.elsevier.com/locate/apenergy [https://doi.org/10.1016/j.apenergy.2024.123751](https://doi.org/10.1016/j.apenergy.2024.123751) Received 20 January 2024; Received in revised form 7 June 2024; Accepted 16 June 2024

- > realize a probabilistic forecasting solution for short-term EV charging demand of individual station considering multiple external features and time series data. Its superiority is verified on the dataset of a regionally representative charging station. In general, the main contributions of this paper are summarized as follows.

- > can make the value of RMSE realistic. And the NRMSE can eliminate scale dependence and allow for easier comparison of models of different scales or even datasets. NRMSE =̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ 1

- > the two gates so that only one of the two gates is active. The GLU’s presence diminishes the importance of structures that are not necessary for datasets. In GRN, the input of the GLU is the dense layerd1, and outputs GLUω(d1) = σ

- > 4. Case studies 4.1. Experiments description 4.1.1. EV Datasets description The performance of the proposed FEDM approach is verified by the T. Cao et al.

---

### 40. 2024_Hierarchical_Probabilistic_Conformal_Prediction_for_Distributed_Energy_Resources.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Extracted Web Links**:
- [`[https://data.census.gov`](https://data.census.gov)](https://data.census.gov`)

- [`[https://www.woodmac.com/reports/`](https://www.woodmac.com/reports/)](https://www.woodmac.com/reports/`)

- [`[https://www.seia.org/research-resources/solar-market-insight-report-2023-q4`](https://www.seia.org/research-resources/solar-market-insight-report-2023-q4)](https://www.seia.org/research-resources/solar-market-insight-report-2023-q4`)

- [`[https://arxiv.org/abs/2411.12193v4`](https://arxiv.org/abs/2411.12193v4)](https://arxiv.org/abs/2411.12193v4`)

- [`[https://www.woodmac.com/reports/energy-markets-energy-transition-outlook-2023-highlights-150161487/`](https://www.woodmac.com/reports/energy-markets-energy-transition-outlook-2023-highlights-150161487/)](https://www.woodmac.com/reports/energy-markets-energy-transition-outlook-2023-highlights-150161487/`)

- **📁 Key Dataset Text Snippets / Context**:
- > Substation Figure 1: Geographical distribution of incremental photovoltaic (PV) unit installations col- lected from a real-world dataset. The most recent five-year interval (2019–2024) shows significantly higher growth and greater spatial disparity compared to the preceding interval

- > gorithm, and Section 5 provides theoretical analyses of its validity and efficiency. Finally, Section 6 presents empirical evaluations comparing our method with existing baselines for DER adoption modeling on both synthetic and real-world datasets. 3

- > M, model λ, prediction horizon ∆t, calibration data size n. 1: Initialize Ek = ∅for all k = 1, . . . , K. 2: Split HT into training dataset Dtr and calibration dataset Dcal; 3: Fit multivariate Hawkes process model λ on Dtr by maximizing log-likelihood (4); 4: for j ∈{1, . . . , n} do

- > n+1 ∼λ(·|xn+1); 13: Return prediction intervals according to (8). We begin by splitting the dataset HT using a cutoff time index τ ∈[0, T). The data prior to τ, denoted as Dtr := {(ti, ki) : ti < τ}, is used to train the multivariate Hawkes process via maximum likelihood estimation using the log-likelihood in Eq. (4). The post-τ

- > Substation- level Figure 4: Illustration of our proposed algorithm. The training phase splits the dataset (D), where the training data (Dtr) is used to fit the model (λ), and then used with the calibration data (Dcal) to calculate the set of neighbor-aware non-conformity scores (E). Finally, Quantile

---

### 41. 2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/thuml/iTransformer`](https://github.com/thuml/iTransformer)](https://github.com/thuml/iTransformer`)

- **📁 Key Dataset Text Snippets / Context**:
- > multivariate correlations; meanwhile, the feed-forward network is applied for each variate token to learn nonlinear representations. The iTransformer model achieves state-of-the-art on challenging real-world datasets, which further empowers the Transformer family with promoted performance, generalization ability across differ- ent variates, and better utilization of arbitrary lookback windows, making it a nice

- > ent variates, and better utilization of arbitrary lookback windows, making it a nice alternative as the fundamental backbone of time series forecasting. Code is avail- able at this repository: [https://github.com/thuml/iTransformer.](https://github.com/thuml/iTransformer.) 1 INTRODUCTION

- > X:,n as the whole time series of each variate indexed by n. It is notable that Xt,: may not contain time points that essentially reflect the same event in real-world scenarios because of the systematical time lags among variates in the dataset. Besides, the elements of Xt,: can be distinct from each other in physical measurements and statistical distributions, for which a variate X:,n generally shares. 3.1

- > validate the generality of the proposed framework and further dive into the effectiveness of applying the Transformer components on the inverted dimensions of time series. Datasets We extensively include 7 real-world datasets in our experiments, including ECL, ETT (4 subsets), Exchange, Traffic, Weather used by Autoformer (Wu et al., 2021), Solar-Energy datasets

- > the Transformer components on the inverted dimensions of time series. Datasets We extensively include 7 real-world datasets in our experiments, including ECL, ETT (4 subsets), Exchange, Traffic, Weather used by Autoformer (Wu et al., 2021), Solar-Energy datasets 5

---

### 42. 2024_Load_Forecasting_of_Electric_Vehicle_Charging_Stations_Attention_Based_Spatiotemporal_MultiGraph_Convolutional_Networks.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0003-1039-0439`](https://orcid.org/0000-0003-1039-0439)](https://orcid.org/0000-0003-1039-0439`)

- [`[https://orcid.org/0000-0002-4034-2932`](https://orcid.org/0000-0002-4034-2932)](https://orcid.org/0000-0002-4034-2932`)

- [`[https://orcid.org/0000-0003-2937-7680`](https://orcid.org/0000-0003-2937-7680)](https://orcid.org/0000-0003-2937-7680`)

- [`[https://orcid.org/0000-0002-7211-060X`](https://orcid.org/0000-0002-7211-060X)](https://orcid.org/0000-0002-7211-060X`)

- [`[https://orcid.org/0000-0002-7838-0352`](https://orcid.org/0000-0002-7838-0352)](https://orcid.org/0000-0002-7838-0352`)

- **📁 Key Dataset Text Snippets / Context**:
- > of multiple charging stations is proposed, which can effectively share spatiotemporal relationships among stations. Finally, exper- iments on real-world dataset illustrate that STMGCN is capable of improving the accuracy of charging stations load forecasting compared with the baselines, which shows the effectiveness of

- > wenzhong.gao@du.edu). Color versions of one or more ﬁgures in this article are available at [https://doi.org/10.1109/TSG.2023.3321116.](https://doi.org/10.1109/TSG.2023.3321116.) Digital Object Identi 100097 er 10.1109/TSG.2023.3321116 consumption and no tailpipe air pollutants compared with con-

- > simulate daily taxi trip-chain rules. The model driven approach 1949-3053 c 100270 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on August 07,2026 at 16:08:45 UTC from IEEE Xplore.  Restrictions apply.

- > ment. The problem formulation and GCNs-based charging load forecasting framework are introduced in Section III. The experiments based on charging station dataset are shown in Section IV. Finally, the conclusions and future works on the charging load forecasting model are presented in Section V.

- > error (RMSE). IV. EXPERIMENTS A. Datasets The model is evaluated on the charging load dataset from Beijing, China. The datasets include historical data on charg-

---

### 43. 2024_Location_based_Probabilistic_Load_Forecasting_of_EV_Charging_Sites_Deep_Transfer_Learning_with_Multi_Quantile_Temporal_Convolutional_Network.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Extracted Web Links**:
- [`[https://www.mdpi.com/`](https://www.mdpi.com/)](https://www.mdpi.com/`)

- [`[https://www.mdpi.com/1996-1073/15/17/6195`](https://www.mdpi.com/1996-1073/15/17/6195)](https://www.mdpi.com/1996-1073/15/17/6195`)

- [`[https://www.mdpi.com/2071-1050/15/3/2105`](https://www.mdpi.com/2071-1050/15/3/2105)](https://www.mdpi.com/2071-1050/15/3/2105`)

- [`[https://www.iea.org/reports/global-ev-outlook-2022`](https://www.iea.org/reports/global-ev-outlook-2022)](https://www.iea.org/reports/global-ev-outlook-2022`)

- [`[https://www.iea.org/reports/global-ev-outlook-2024`](https://www.iea.org/reports/global-ev-outlook-2024)](https://www.iea.org/reports/global-ev-outlook-2024`)

- ** 102327  Key Dataset Text Snippets / Context**:
- > among heterogeneous temporal features and irregular energy usage patterns [8][9]. Some models are very sensitive to outliers [10], and some can not handle large datasets well arXiv:2409.11862v1  [cs.LG]  18 Sep 2024

- > sites incorporating quantile regression techniques and TCN capabilities. To evaluate MQ-TCN architecture using real- world datasets for load forecasting tasks, we are motivated to explore the following research questions in this research: 1) How to develop a multivariate multi-step load forecast-

- > four real-world EV charging sites: Caltech, JPL, Office-1, and NREL [21]. Here, the Caltech, JPL, and Office-1 data is obtained from the primary dataset, ’ ACN’ [22]. Experimental evaluation of these datasets using proposed MQ-TCN archi- tecture in comparison to the XGBoost [23] and Deep Auto-

- > and NREL [21]. Here, the Caltech, JPL, and Office-1 data is obtained from the primary dataset, ’ ACN’ [22]. Experimental evaluation of these datasets using proposed MQ-TCN archi- tecture in comparison to the XGBoost [23] and Deep Auto- Regressive recurrent networks (DeepAR) [24] models leads to

- > MQ-TCN model, using only 2 weeks of data, it reached a PICP score of 96.88% as illustrated in Figure 1 for hourly forecasting at NREL site. This resulted in an improvement of 18.23% compared to the XGBoost model trained on 6 months of data without TL. In similar TL

---

### 44. 2024_On_the_Utilization_of_Autoformer_Based_Deep_Learning_for_EV_Charging_Load_Forecasting.pdf

- **Title**: Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network
- **Identified Datasets**: Caltech ACN (54 chargers), JPL Dataset (50 chargers), Office-1 Dataset (8 chargers), NREL Dataset (141 chargers, 59 months data)
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://open-data.bouldercolorado.gov/datasets/`](https://open-data.bouldercolorado.gov/datasets/)](https://open-data.bouldercolorado.gov/datasets/`)

- ** 104407  Key Dataset Text Snippets / Context**:
- > work addresses this problem by adopting an Autoformer-based deep learning model to predict the EV charging load using an open source charger dataset from 51 public charging stations in Boulder, Colorado, U.S. EV load predictions for 30 days, 60 days, and 90 days are obtained using the proposed Autoformer model

- > scarcity of publicly accessible data on user-speci 104821 c driving patterns and/or region-speci 104862 c EV energy requirements [6]. Most available datasets consist of time-series operational data from EV chargers with limited volume and/or time span. Yet, these datasets provide details of the start and end times

- > Most available datasets consist of time-series operational data from EV chargers with limited volume and/or time span. Yet, these datasets provide details of the start and end times of charging, the durations of the charging sessions, and the amount of energy delivered at prede 105360 ned charging locations,

- > Boost, random forests and support vector machines (SVM) are developed in [11], [12] and [13] using open source EV charger datasets, to predict the EV electricity demand from public fast chargers. However, these models require large volumes of training data to provide accurate predictions.

- > then presents the methodology followed for developing and training the Autoformer DL model for EV demand prediction using time-series charger datasets. Outcomes of the proposed predictor are then reported in Section IV along with the discussions of these outcomes. The paper is  105965 nally concluded

---

### 45. 2025_A_Stochastic_Model_Predictive_Control_Based_Energy_Management_Approach_for_Microgrids_With_Electric_Vehicles.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0003-2696-5436`](https://orcid.org/0000-0003-2696-5436)](https://orcid.org/0000-0003-2696-5436`)

- [`[https://orcid.org/0000-0001-8218-586X`](https://orcid.org/0000-0001-8218-586X)](https://orcid.org/0000-0001-8218-586X`)

- [`[https://orcid.org/0000-0002-7906-4255`](https://orcid.org/0000-0002-7906-4255)](https://orcid.org/0000-0002-7906-4255`)

- [`[https://orcid.org/0009-0002-0212-0025`](https://orcid.org/0009-0002-0212-0025)](https://orcid.org/0009-0002-0212-0025`)

- [`[http://www.elia.be/en`](http://www.elia.be/en)](http://www.elia.be/en`)

- ** 106921  Key Dataset Text Snippets / Context**:
- > layer considers the power allocation of individual EVs [12], 2332-7782 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 07:10:45 UTC from IEEE Xplore.  Restrictions apply.

- > pp. 284–289. [29] Elia. (2022). Belgium’s Electricity Transmission System Operator. [Online]. Available: [http://www.elia.be/en](http://www.elia.be/en) Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 07:10:45 UTC from IEEE Xplore.  Restrictions apply.

---

### 46. 2025_BWO_ICEEMDAN_iTransformer_Power_System_Load_Forecasting.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://doi.org/10.3390/a18050243`](https://doi.org/10.3390/a18050243)](https://doi.org/10.3390/a18050243`)

- [`[https://www.mdpi.com/article/10.3390/a18050243?type=check_update&version=1`](https://www.mdpi.com/article/10.3390/a18050243?type=check_update&version=1)](https://www.mdpi.com/article/10.3390/a18050243?type=check_update&version=1`)

- [`[https://doi.org/10.3390/e26080699`](https://doi.org/10.3390/e26080699)](https://doi.org/10.3390/e26080699`)

- [`[https://www.mdpi.com/journal/algorithms`](https://www.mdpi.com/journal/algorithms)](https://www.mdpi.com/journal/algorithms`)

- [`[https://doi.org/10.3390/systems11090456`](https://doi.org/10.3390/systems11090456)](https://doi.org/10.3390/systems11090456`)

- ** 108784  Key Dataset Text Snippets / Context**:
- > for Power Systems with Parameter Optimization. Algorithms 2025, 18, 243. [https://doi.org/10.3390/a18050243](https://doi.org/10.3390/a18050243) Copyright: © 2025 by the authors. Licensee MDPI, Basel, Switzerland.

- > conditions of the Creative Commons Attribution (CC BY) license ([https://creativecommons.org/](https://creativecommons.org/) licenses/by/4.0/). algorithms

- > often fall short when it comes to forecasting nonlinear data like electricity load. Machine Algorithms 2025, 18, 243 [https://doi.org/10.3390/a18050243](https://doi.org/10.3390/a18050243)

- > relevant algorithms employed in the forecasting model. Section 3 outlines the design of the proposed forecasting model in detail. Section 4 describes the experimental setup and dataset, discusses the experimental results, and compares the load forecasting performance of different methods. Finally, the conclusion is presented in Section 5. 2. Methodology

- > The load data was first divided into training, validation, and test sets, and decomposi- tion was performed separately on each set to avoid data leakage, which could affect the authenticity of the prediction. The results are shown in Figures 2–4. All three datasets were decomposed into thirteen intrinsic mode functions and one residual, demonstrating that the data decomposition technique exhibits consistency and stability across different data

---

### 47. 2025_Benchmarking_Time_Series_Foundation_Models_for_Short_Term_EV_Charging_Demand_Forecasting.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/Nixtla/neuralforecast`](https://github.com/Nixtla/neuralforecast)](https://github.com/Nixtla/neuralforecast`)

- [`[https://github.com/amazon-science/chronos-forecasting`](https://github.com/amazon-science/chronos-forecasting)](https://github.com/amazon-science/chronos-forecasting`)

- [`[https://github.com/time-series-foundation-models/lag-llama`](https://github.com/time-series-foundation-models/lag-llama)](https://github.com/time-series-foundation-models/lag-llama`)

- [`[https://github.com/Time-MoE/Time-MoE`](https://github.com/Time-MoE/Time-MoE)](https://github.com/Time-MoE/Time-MoE`)

- [`[https://github.com/SalesforceAIResearch/uni2ts`](https://github.com/SalesforceAIResearch/uni2ts)](https://github.com/SalesforceAIResearch/uni2ts`)

- [`[https://github.com/google-research/timesfm`](https://github.com/google-research/timesfm)](https://github.com/google-research/timesfm`)

- [`[https://github.com/thuml/Sundial`](https://github.com/thuml/Sundial)](https://github.com/thuml/Sundial`)

- [`[https://github.com/Nixtla/statsforecast`](https://github.com/Nixtla/statsforecast)](https://github.com/Nixtla/statsforecast`)

- ** 111727  Key Dataset Text Snippets / Context**:
- > The recent development of time series foundation models (TSFM), which are (pre-)trained on large and diverse time series datasets, offers the possibility to depart from the tradi- tional method of training one model per task and iteratively re- training it. Out-of-the-box, without further domain adaptation

- > This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3648056 This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

- > series) with TSFM to determine the suitability of foundation models in household electricity STLF. We evaluate in our benchmark with two real-world datasets from Germany and two real-world datasets from Great Britain, leading in total to over 300 individual households. All datasets

- > models in household electricity STLF. We evaluate in our benchmark with two real-world datasets from Germany and two real-world datasets from Great Britain, leading in total to over 300 individual households. All datasets reflect a realistic use case from a DSO’s perspective, including

- > We evaluate in our benchmark with two real-world datasets from Germany and two real-world datasets from Great Britain, leading in total to over 300 individual households. All datasets reflect a realistic use case from a DSO’s perspective, including households with different start and end times, several load

---

### 48. 2025_Charging_stations_demand_forecasting_using_LSTM_based_hybrid_transformer_model.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://doi.org/10.1155/2022/2870668`](https://doi.org/10.1155/2022/2870668)](https://doi.org/10.1155/2022/2870668`)

- [`[https://doi.org/10.1038/s41598-025-20421-y`](https://doi.org/10.1038/s41598-025-20421-y)](https://doi.org/10.1038/s41598-025-20421-y`)

- [`[https://doi.org/10.1111/exsy.13539`](https://doi.org/10.1111/exsy.13539)](https://doi.org/10.1111/exsy.13539`)

- ** 114111  Key Dataset Text Snippets / Context**:
- > decoder for forecasting the demand at electric vehicle charging stations (EVCS). The proposed model is compared with traditional deep learning-based LSTM and Transformer models. The research employs open datasets from ACN, including charging data from Caltech and JPL. Both datasets are used to train and test the models. Predictions are made for 30 days, 120 days, and 240 days ahead, with results compared to actual demand. Performance is evaluated using Mean Absolute Error (MAE) and Mean

- > model also shows better accuracy across all horizons for JPL data by reducing MAE and MSE by up to 24.91% and 23.17% at 30 days, 5.00% and 5.17% at 120 days, and 3.90% and 4.86% at 240 days. The results indicate that the Hybrid Transformer model outperforms the baseline models for both datasets in medium-term and long-term predictions. The 30, 120, and 240-day predictions demonstrate lower error rates with the proposed model when utilizing Caltech and JPL charging data for these time

- > Scientific Reports |        (2025) 15:36639 1 | [https://doi.org/10.1038/s41598-025-20421-y](https://doi.org/10.1038/s41598-025-20421-y) www.nature.com/scientificreports Content courtesy of Springer Nature, terms of use apply. Rights reserved

- > study is to enhance the precision of medium-term and long-term forecasts. The research proposes a Hybrid Transformer model with LSTM-based Encoder-Decoder. The proposed model is implemented using the ACN dataset, which includes Caltech and JPL charging stations. The proposed model and the baselines are trained and tested using both datasets. The performance comparison is performed with the baselines, including the LSTM, and Transformer models. The main contributions of this research work are as follows:

- > Transformer model with LSTM-based Encoder-Decoder. The proposed model is implemented using the ACN dataset, which includes Caltech and JPL charging stations. The proposed model and the baselines are trained and tested using both datasets. The performance comparison is performed with the baselines, including the LSTM, and Transformer models. The main contributions of this research work are as follows: •	 To the best of our knowledge, this is the first study to propose an LSTM encoder-decoder-based Transformer

---

### 49. 2025_Coherent_Hierarchical_Probabilistic_Forecasting_of_Electric_Vehicle_Charging_Demand.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/CW-Huang/CP-Flow`](https://github.com/CW-Huang/CP-Flow)](https://github.com/CW-Huang/CP-Flow`)

- [`[https://github.com/meteostat/meteostat-python`](https://github.com/meteostat/meteostat-python)](https://github.com/meteostat/meteostat-python`)

- [`[https://github.com/cvxgrp/cvxpylayers`](https://github.com/cvxgrp/cvxpylayers)](https://github.com/cvxgrp/cvxpylayers`)

- ** 117173  Key Dataset Text Snippets / Context**:
- > eee.hku.hk). Color versions of one or more  117263 gures in this article are available at [https://doi.org/10.1109/TIA.2023.3344544.](https://doi.org/10.1109/TIA.2023.3344544.) Digital Object Identi 117413 er 10.1109/TIA.2023.3344544 Outlook, there were over 16.5 million EVs on the road in 2021,

- > proposed to use the reconciliation-based forecasting method 0093-9994 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:58:09 UTC from IEEE Xplore.  Restrictions apply.

- > monly adopted in electricity demand forecasting tasks. The weather features consist of the air temperature (°C), the dew point (°C), and hourly precipitation level (mm). The weather data used for feature construction are obtained from the Python API of Meteostat [37], which provides access to

- > weather data used for feature construction are obtained from the Python API of Meteostat [37], which provides access to open data from national weather services including the National Oceanic and Atmospheric Administration (NOAA). Since the ACN data contains three EVCSs located in California, US,

- > Fig. 5 shows the training and data partitioning of hierarchi- cal reconciling with trainable parameters. The DCL maps the 1[Online]. Available: [https://github.com/cvxgrp/cvxpylayers](https://github.com/cvxgrp/cvxpylayers) Fig. 5. Training and data partitioning of hierarchical reconciling.

---

### 50. 2025_Data_Driven_Long_Term_Learning_Model_for_EV_Charging_Load_Prediction.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[http://dx.doi.org/10.1080/00207720110067421`](http://dx.doi.org/10.1080/00207720110067421)](http://dx.doi.org/10.1080/00207720110067421`)

- ** 119334  Key Dataset Text Snippets / Context**:
- > to one year [12]. According to reference [13], forecasting in a power grid aims to assist decision-making at the precision of hourly, daily, weekly, and monthly changes in load. Load is defined as the system load, peak system load, and system en- ergy [12]. This paper proposes a solution for the prediction of

- > demands. Without requiring costly training processes, these methods use mathematical formulas and historical demand data to capture hourly, daily, and seasonal variations in load patterns. Fig. 3 shows a stepwise block diagram that helps to understand the pathway used in traditional load prediction.

- > • Deep learning approaches: They can automatically ex- tract complicated historical and geographic patterns from big datasets, they have become a powerful instru- ment for modelling EV charging station load demand [31].[32]. In complex EV load datasets, Convolutional

- > from big datasets, they have become a powerful instru- ment for modelling EV charging station load demand [31].[32]. In complex EV load datasets, Convolutional Neural Networks (CNNs) have been used to capture local seasonal and geographical correlations, while hy-

- >  • Flexible architecture. • Requires large dataset for good generaliza- tion.

---

### 51. 2025_Deep_Learning_Predicts_Real_World_Electric_Vehicle_DC_Charging_Profiles_and_Durations.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/acse-`](https://github.com/acse-)](https://github.com/acse-`)

- [`[https://github.com/acse-sl420/ev_charging_ml`](https://github.com/acse-sl420/ev_charging_ml)](https://github.com/acse-sl420/ev_charging_ml`)

- [`[https://doi.org/10.5281/zenodo.17183022`](https://doi.org/10.5281/zenodo.17183022)](https://doi.org/10.5281/zenodo.17183022`)

- [`[https://doi.org/10.5281/zenodo.17183746`](https://doi.org/10.5281/zenodo.17183746)](https://doi.org/10.5281/zenodo.17183746`)

- ** 121480  Key Dataset Text Snippets / Context**:
- > Article [https://doi.org/10.1038/s41467-025-65970-y](https://doi.org/10.1038/s41467-025-65970-y) Deep learning predicts real-world electric vehicle direct current charging pro 121702 les and

- > sophisticated machine learning techniques15–19. These studies, often based on real- world datasets, have achieved strong performance in tasks such as state-of-health estimation, lifetime prediction, and retired battery sorting, and represent meaningful progress toward the development

- > speci 122015 cally focused on predicting EV charging pro 122061 les remains comparatively limited. Existing work in this area has largely relied on relatively small datasets, often collected under laboratory or semi- controlled conditions using instrumented cells or proprietary bat- tery management system (BMS) data20–24. Such data are frequently

- > energy34–36 or climate and weather forecasting37,38, underscores the potential of these techniques to address complex predictive tasks when supported by large-scale, high-quality datasets. In this context, this workintroduces a deep learning framework thatis built on 909,135 real-world DCFC charging sessions, encompassing a wide variety of EV

- > and grid conditions, also affect the charging pro 122757 le. To effectively analyse and comprehend these diverse charging behaviours, it is crucial to employ an extensive dataset that encom- passes the variability in charging patterns across various conditions and EV models. In this work, a carefully curated dataset of 909,135

---

### 52. 2025_EV_STLLM_Electric_Vehicle_Spatio_Temporal_Large_Language_Model.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://arxiv.org/abs/2507.09527v1`](https://arxiv.org/abs/2507.09527v1)](https://arxiv.org/abs/2507.09527v1`)

- ** 123458  Key Dataset Text Snippets / Context**:
- > this field usually struggle to capture the complex spatio-temporal dependencies in EV charging behaviors, and their limited model parameters hinder their ability to learn complex data distribution representations from large datasets. To this end, we propose a novel EV spatio-temporal large language model (EV- STLLM) for accurate prediction. Our proposed framework is divided into two modules. In the data processing module, we utilize variational mode decomposition (VMD) for data denoising, and improved

- > (e.g., daily vs. weekly) and multiple frequencies (e.g., short-term fluctuations vs. long-term trends). More importantly, the limited parameter scale of these models constrains their ability to learn complex data distributions and deep representations from large-scale datasets [7]. In contrast, Large Language Models (LLMs) are characterized by their large parameter scale and sophisticated architectures, granting them superior representation learning capabilities essential for deeply understanding and analyzing complex

- > Sun et al. used SVM to preprocess multi-source input data and effectively correct for anomalies, thereby improving the accuracy of the charging load prediction model [20]. However, AI-based models use only a single model, which cannot show good generalization in different data sets. Therefore, hybrid models have begun to attract the attention of researchers, such as the hybrid CNN-LSTM-Attention deep learning model [21] and the ARIMA-LSTM model [22]. For example, Tian et al. proposed a combination of

- > Despite significant advancements in forecasting EV charging loads, practical application of current methodologies faces several critical challenges. First, due to the limitation of the number of parameters, it is difficult for existing models to fully learn the full data distribution information of EV charging datasets. In addition, these small single models can only perform well in a few datasets, therefore, when generalizing to other different EV charging datasets, they often cannot guarantee accuracy and have difficulty in showing

- > methodologies faces several critical challenges. First, due to the limitation of the number of parameters, it is difficult for existing models to fully learn the full data distribution information of EV charging datasets. In addition, these small single models can only perform well in a few datasets, therefore, when generalizing to other different EV charging datasets, they often cannot guarantee accuracy and have difficulty in showing good general characteristics [26]. Second, they have difficulty understanding the relationships between

---

### 53. 2025_Electric_Vehicles_Charging_Stations_Load_Forecasting_Based_on_Hybrid_XGBoost_BiLSTM_Model.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://ev.caltech.edu/dataset`](https://ev.caltech.edu/dataset)](https://ev.caltech.edu/dataset`)

- ** 126607  Key Dataset Text Snippets / Context**:
- > Accurate load forecasting for Electric Vehicle Charging Stations (EVCS) is critical for optimizing energy management and ensuring grid stability amid growing electric vehicle adoption. This study investigates short-term, hourly load forecasting at the station level using a hybrid XGBoost–BiLSTM stacking model (Hybrid 3) with an XGBoost meta-learner. From the Adaptive Charging Network (ACN–Caltech) dataset (April 25, 2018–September 13, 2021), 31,424 raw charging sessions were

- > investigates short-term, hourly load forecasting at the station level using a hybrid XGBoost–BiLSTM stacking model (Hybrid 3) with an XGBoost meta-learner. From the Adaptive Charging Network (ACN–Caltech) dataset (April 25, 2018–September 13, 2021), 31,424 raw charging sessions were preprocessed, yielding 14,496 cleaned sessions for modeling. These were split into 80% training and 20% testing sets using a fixed random seed (42) for reproducibility. Hybrid 3 was benchmarked

- > BiLSTM—while slightly underperforming the top Boosting ensemble (XGBoost + BiLSTM + LightGBM). Robustness was confirmed via five-fold walk-forward validation (mean MAE = 2.5351 kWh, SD = 1.2885). Cross-site evaluation on an independent synthetic dataset (n = 1,965,239 sessions) showed reduced generalization, highlighting site-specific temporal patterns. One-Way ANOVA (p = 0.2073, η2 = 0.2062) indicated no statistically significant but practically relevant differences

- > Scientific Reports |          (2026) 16:374 1 | [https://doi.org/10.1038/s41598-025-29739-z](https://doi.org/10.1038/s41598-025-29739-z) www.nature.com/scientificreports

- > Infrastructure Law), and China leads with over 1.4 million public charging points, including high-speed chargers along major corridors. However, volatile EV charging demand, driven by unpredictable user behaviors, strains grid infrastructure4. Precise short-term, hourly, station-level load forecasting is essential for optimizing power consumption, resource allocation, and ensuring grid stability5,6. EV load forecasting methods include physically based and data-driven approaches. Physically based methods, like trip chain analysis7, Monte Carlo simulations8,

---

### 54. 2025_Enhanced_Transformer_BiLSTM_Deep_Learning_Framework_for_Day_Ahead_Energy_Price_Forecasting.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://data.mendeley.com/datasets/s54n4tyyz4/2`](https://data.mendeley.com/datasets/s54n4tyyz4/2)](https://data.mendeley.com/datasets/s54n4tyyz4/2`)

- ** 129393  Key Dataset Text Snippets / Context**:
- > Harrisburg, Middletown, PA 17057 USA (e-mail: mpk5904@psu.edu). Color versions of one or more  129534 gures in this article are available at [https://doi.org/10.1109/TIA.2025.3599812.](https://doi.org/10.1109/TIA.2025.3599812.) Digital Object Identi 129684 er 10.1109/TIA.2025.3599812 risks, as implementing effective bidding strategies is crucial for

- > BiLSTM architectures, has been developed for forecasting 0093-9994 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of arti 129952 cial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 09:12:55 UTC from IEEE Xplore.  Restrictions apply.

- > [14], [15]. While these methods can handle complex data, they may not be effective when dealing with large-scale and highly complex datasets. Due to the ability to handle complex and large-scale data, DL approaches have drawn signi 130614 cant attention from researchers, especially for time-series forecasting.

- > for DA EPF in the Australian energy market, aiming to improve accuracy over traditional methods. Although XGBoost demon- strates higher accuracy and ef 130846 ciency with structured datasets, it struggles with sequential data, requiring extensive feature engineering to capture temporal dependencies. In [19], a multi-

- > that BiLSTM provides better accuracy than LSTM and GRU methods, demonstrating its capability to capture trends and memorize random events, as well as patterns in the datasets. In [26], a BiLSTM model with an attention-based mechanism was introduced for electricity load and price forecasting, uti-

---

### 55. 2023_Cheng_VMD_Prophet_LSTM.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://doi.org/10.7500/AEPS20200226011`](https://doi.org/10.7500/AEPS20200226011)](https://doi.org/10.7500/AEPS20200226011`)

- [`[https://doi.org/10.13335/j.1000-3673.pst.2018.0433`](https://doi.org/10.13335/j.1000-3673.pst.2018.0433)](https://doi.org/10.13335/j.1000-3673.pst.2018.0433`)

- [`[https://www.frontiersin.org/journals/energy-research#editorial-board`](https://www.frontiersin.org/journals/energy-research#editorial-board)](https://www.frontiersin.org/journals/energy-research#editorial-board`)

- [`[https://www.frontiersin.org/articles/10.3389/fenrg.2023.1297849/full`](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1297849/full)](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1297849/full`)

- [`[https://doi.org/10.19635/j.cnki.csu-epsa.000843`](https://doi.org/10.19635/j.cnki.csu-epsa.000843)](https://doi.org/10.19635/j.cnki.csu-epsa.000843`)

- ** 132472  Key Dataset Text Snippets / Context**:
- > “q 132523  markers is complete data set for each day. From Figure 3, it can be observed that the raw data has a certain periodicity. Given the 15-min data granularity, this study de 132697 nes 96 time steps as

- > photovoltaic power prediction) to further verify the prediction performance and generalization ability of this method. Data availability statement The original contributions presented in the study are included in the article/Supplementary material, further inquiries can be directed

---

### 56. 2025_Long_Short_Term_Financial_Time_Series_Forecasting_Based_on_Residual_Multiscale_TCN_Sparse_Expert_Network_and_Informer.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://www.kaggle.com/datasets/`](https://www.kaggle.com/datasets/)](https://www.kaggle.com/datasets/`)

- ** 133504  Key Dataset Text Snippets / Context**:
- > ablation experiments  133572 rst validate the eﬀectiveness and necessity of the proposed strategies and network structure. Subsequent comparison experiments on the NASDAQ100 dataset demonstrate that ResMMoT-Informer excels in both long- and short-term time series forecasting tasks in the stock market, with signi 133861 cantly

- > available at [https://doi.org/10.1109/TNNLS.2025.3584369,](https://doi.org/10.1109/TNNLS.2025.3584369,) provided by the authors. Digital Object Identi 134026 er 10.1109/TNNLS.2025.3584369 a crucial component of  134082 nancial markets, the stock market

- > fully reﬂect all available information in an eﬃcient market, making it impossible for investors to achieve excess returns through publicly available information. However, as  134302 nancial markets have become more complex and data technologies have advanced, the limitations of EMH and RWT have been

- > 2162-237X © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of arti 134537 cial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 09:10:15 UTC from IEEE Xplore.  Restrictions apply.

- > integration. The structure of this article is organized as follows. Section II introduces the dataset and outlines the data pro- cessing procedures employed in the experiments. Section III provides an in-depth explanation of the overall framework of

---

### 57. 2025_Meta_Learning_Enhanced_Physics_Informed_Graph_Attention_Convolutional_Network_for_Distribution_Power_System_State_Estimation.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0002-5783-5653`](https://orcid.org/0000-0002-5783-5653)](https://orcid.org/0000-0002-5783-5653`)

- [`[https://orcid.org/0000-0003-4480-7394`](https://orcid.org/0000-0003-4480-7394)](https://orcid.org/0000-0003-4480-7394`)

- [`[https://orcid.org/0000-0003-0588-8064`](https://orcid.org/0000-0003-0588-8064)](https://orcid.org/0000-0003-0588-8064`)

- ** 135967  Key Dataset Text Snippets / Context**:
- > map the measurements to the system states directly, thereby 2327-4697 © 2025 IEEE. All rights reserved, including rights for text and data mining, and training of arti 136182 cial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on August 07,2026 at 16:10:47 UTC from IEEE Xplore.  Restrictions apply.

- > task is divided into a supporting set for training and a query set for testing. In the  136702 ne-tuning process, the data for the new task is similarly divided into the corresponding data set. Note that the query data set is used to represent the testing performance of the model during both the meta-learning and  136925 ne-tuning process.

- > for testing. In the  136972 ne-tuning process, the data for the new task is similarly divided into the corresponding data set. Note that the query data set is used to represent the testing performance of the model during both the meta-learning and  137195 ne-tuning process. Algorithm 1: Meta-PIGACN.

- > Algorithm 1: Meta-PIGACN. TABLE I THE SIZES OF TRAINING AND TESTING DATASETS TABLE II THE LOCATION OF WT AND PV

- > percentages of the measurements are added to the measurement data. Besides, to evaluate the performance of the proposed method against topology changes, the data set is generated with different topologies and RES scenarios, where the details are shown in Table I. Note that in each topology, 90% and 10%

---

### 58. 2025_Multi_Scale_Spatial_Temporal_Graph_Attention_Network_for_Charging_Station_Load_Prediction.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/`](https://github.com/)](https://github.com/`)

- [`[https://github.com/fbohu/Deep-Spatio-Temporal-`](https://github.com/fbohu/Deep-Spatio-Temporal-)](https://github.com/fbohu/Deep-Spatio-Temporal-`)

- [`[https://github.com/fbohu/`](https://github.com/fbohu/)](https://github.com/fbohu/`)

- ** 138340  Key Dataset Text Snippets / Context**:
- > heterogeneity in energy demand, ensuring a nuanced understanding of regional variations. Our framework’s efficacy is underscored by its superior performance over existing baselines on four real-world EV charging station datasets, showcasing its prowess in tackling the intricacies of low spatial resolution and spatial heterogeneity. INDEX TERMS Charging station load forecasting, graph attention, low spatial resolution, spatial hetero-

- > 29000 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/) VOLUME 13, 2025

- > proposed module can better handle this problem. We conducted extensive experiments on four real-world electric vehicle charging station datasets, and conducted two tasks, namely 7-1 (take 7 days of historical data to predict 1 day) and 30-7 (take 30 days of historical data to predict 7).

- > [25]. Shanmuganathan et al. implemented empirical mode decomposition-arithmetic optimization algorithm-deep long short-term memory [26] on the EV charging dataset of Geor- gia Institute of Technology in Atlanta, USA. Architectures based on LSTM are often used to overcome the problems

- > Institute of Technology [13], similar methods have been used in [27] for the MID 2008 survey of EV user mobility behavior Open dataset. At the same time, integrated LSTM with feed- forward neural networks [28] has also been proven to have good effects. With the advancement of the encoder-decoder

---

### 59. 2025_Multi_View_Graph_Contrastive_Representative_Learning_for_Intrusion_Detection_in_EV_Charging_Station.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://securelist.com/remotely-controlled-ev-home-`](https://securelist.com/remotely-controlled-ev-home-)](https://securelist.com/remotely-controlled-ev-home-`)

- [`[http://arxiv.org/abs/1810.00826`](http://arxiv.org/abs/1810.00826)](http://arxiv.org/abs/1810.00826`)

- [`[http://creativecommons.org/licenses/by/4.0/`](http://creativecommons.org/licenses/by/4.0/)](http://creativecommons.org/licenses/by/4.0/`)

- [`[https://www.bbc.com/news/uk-england-hampshire-1006816`](https://www.bbc.com/news/uk-england-hampshire-1006816)](https://www.bbc.com/news/uk-england-hampshire-1006816`)

- [`[https://orcid.org/0000-0003-4895-9192`](https://orcid.org/0000-0003-4895-9192)](https://orcid.org/0000-0003-4895-9192`)

- ** 141015  Key Dataset Text Snippets / Context**:
- > feature correlations. Additionally, MVGCRL is extended to a self-supervised learning version by minimizing the distance between node embeddings and input features, followed by fine-tuning for improved classification. Experiments on real-world datasets demonstrate that our approach outperforms both traditional supervised methods and state-of-the-art self-supervised learning models, offering an effective solution for enhancing cybersecurity in EV charging infrastructures.

- > charging station operators. Technologies such as the Open Charge Point Protocol (OCPP) [1] enable remote communication between EVCS and [https://doi.org/10.1016/j.apenergy.2025.125439](https://doi.org/10.1016/j.apenergy.2025.125439) Received 23 September 2024; Received in revised form 22 December 2024; Accepted 23 January 2025 Applied Energy 385 (2025) 125439

- > Applied Energy 385 (2025) 125439 Available online 19 February 2025 0306-2619/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license ( [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/) ).

- > HPC logs for intrusion detection. The second challenge lies in the difficulty of obtaining large-scale, high-quality labeled datasets in practice, particularly for IDSs. The lack of such data limits the effectiveness of supervised learning approaches and makes enhancing node representations for multi-class classification

- > features. In contrast, GNN-based methods applied to IDSs typically focus on binary classification tasks or rely heavily on structural feature engineering—both of which necessitate extensive labeled datasets not readily available in real-world scenarios. These limitations highlight the need for more advanced techniques. To address this issue, this paper

---

### 60. 2025_Personalized_Federated_Learning_for_Household_Electricity_Load_Prediction_with_Imbalanced_Historical_Data.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[http://arxiv.org/abs/2002.10619`](http://arxiv.org/abs/2002.10619)](http://arxiv.org/abs/2002.10619`)

- [`[http://creativecommons.org/licenses/by/4.0/`](http://creativecommons.org/licenses/by/4.0/)](http://creativecommons.org/licenses/by/4.0/`)

- [`[http://crossmark.crossref.org/dialog/?doi=10.1016/j.apenergy.2025.125419&domain=pdf`](http://crossmark.crossref.org/dialog/?doi=10.1016/j.apenergy.2025.125419&domain=pdf)](http://crossmark.crossref.org/dialog/?doi=10.1016/j.apenergy.2025.125419&domain=pdf`)

- [`[https://orcid.org/0000-0001-5125-1860`](https://orcid.org/0000-0001-5125-1860)](https://orcid.org/0000-0001-5125-1860`)

- [`[https://orcid.org/0009-0007-4886-8801`](https://orcid.org/0009-0007-4886-8801)](https://orcid.org/0009-0007-4886-8801`)

- ** 143995  Key Dataset Text Snippets / Context**:
- > Applied Energy 384 (2025) 125419 Available online 6 February 2025 0306-2619/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license ([http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)). Contents lists available at ScienceDirect Applied Energy

- > hold load prediction compared to simply federating the energy usage data from different households. [https://doi.org/10.1016/j.apenergy.2025.125419](https://doi.org/10.1016/j.apenergy.2025.125419) Received 17 October 2024; Received in revised form 13 December 2024; Accepted 21 January 2025

- > stringent privacy requirements of residential power consumption data. Federated learning provides a promising solution to these issues by enabling collaborative model training across distributed datasets while preserving privacy. 2.2. Federated learning

- > difficulties. Despite these advancements, current PFL methods face limitations in handling highly imbalanced and sparse datasets, as well as in achiev- ing a balance between global and local learning for fine-grained predic- tions. The PF-HoLo framework proposed in this study addresses these

- > By repeated iterations and parameter exchanges between the global model and the local models, the global model  145340 gradually incorporates insights and knowledge from the diverse datasets across households. After completing all training with the specified number of rounds, the final global model  145525 is obtained, which represents a collaborative learn-

---

### 61. 2025_Probabilistic_Forecast_of_EV_Charging_Demand_using_Quantile_Regression_and_LSTM_with_Attention_Mechanism.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0002-1274-1506`](https://orcid.org/0000-0002-1274-1506)](https://orcid.org/0000-0002-1274-1506`)

- [`[https://dl.acm.org/profile/99661331324`](https://dl.acm.org/profile/99661331324)](https://dl.acm.org/profile/99661331324`)

- [`[https://dl.acm.org/action/exportCiteProcCitation?dois=10.1145%2F3679240.3734687&targetFile=custom-bibtex&format=bibtex`](https://dl.acm.org/action/exportCiteProcCitation?dois=10.1145%2F3679240.3734687&targetFile=custom-bibtex&format=bibtex)](https://dl.acm.org/action/exportCiteProcCitation?dois=10.1145%2F3679240.3734687&targetFile=custom-bibtex&format=bibtex`)

- [`[https://doi.org/10.1145/3679240.3734687`](https://doi.org/10.1145/3679240.3734687)](https://doi.org/10.1145/3679240.3734687`)

- [`[https://dl.acm.org/sig/sigenergy`](https://dl.acm.org/sig/sigenergy)](https://dl.acm.org/sig/sigenergy`)

- ** 146801  Key Dataset Text Snippets / Context**:
- > SIGENERGY E-Energy '25: Proceedings of the 16th ACM International Conference on Future and Sustainable Energy Systems (June 2025) hps://doi.org/10.1145/3679240.3734687 ISBN: 9798400711251 .

- > In The 16th ACM International Conference on Future and Sustainable Energy Systems (E-ENERGY ’25), June 17–20, 2025, Rotterdam, Netherlands. ACM, New York, NY, USA, 3 pages. [https://doi.org/10.1145/3679240.3734687](https://doi.org/10.1145/3679240.3734687) 1 Introduction

- > © 2025 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-1125-1/25/06 [https://doi.org/10.1145/3679240.3734687](https://doi.org/10.1145/3679240.3734687) A key challenge in managing distributed energy systems like microgrids is handling uncertainty. In this context, point forecast-

- > estimations [1], or Bayesian techniques [5]. This study applies a Quantile Regression (QR) framework to the EV demand forecasting method from [4], using the Dutch ASR dataset. 2 Methodology

- > 3 Case Study The dataset utilized in this study is sourced from the SmoothEMS Met GridShield project in the Netherlands, collected from the ASR office parking lot in Utrecht, while weather data are from KNMI

---

### 62. 2025_REST_Network_Ensemble_Deep_Learning_EV_Charging_Load_Forecasting_Port_Supply_Chains.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://orcid.org/0000-0001-9487-1752`](https://orcid.org/0000-0001-9487-1752)](https://orcid.org/0000-0001-9487-1752`)

- [`[https://orcid.org/0000-0001-7181-2100`](https://orcid.org/0000-0001-7181-2100)](https://orcid.org/0000-0001-7181-2100`)

- [`[https://orcid.org/0000-0002-7658-7085`](https://orcid.org/0000-0002-7658-7085)](https://orcid.org/0000-0002-7658-7085`)

- [`[https://orcid.org/0000-0002-3284-537X`](https://orcid.org/0000-0002-3284-537X)](https://orcid.org/0000-0002-3284-537X`)

- [`[https://creativecommons.org/licenses/by/4.0/`](https://creativecommons.org/licenses/by/4.0/)](https://creativecommons.org/licenses/by/4.0/`)

- ** 149007  Key Dataset Text Snippets / Context**:
- > 133128 2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/) VOLUME 13, 2025

- > Convolutional Neural Networks (CNNs) have shown an ability to capture temporal and spatial patterns in complex datasets [7], [8]. Transformer models, in particular, offer strong performance in modeling long-range dependencies, while hybrid designs that combine CNNs with attention

- > specifically for the unique operational context of artificial ports—especially when it comes to dealing with imbalanced datasets and domain-specific variability. C. OBJECTIVES AND CONTRIBUTIONS OF THE STUDY To bridge this gap, we propose a deep learning-based

- > The structure of this paper is designed to guide the reader through each stage of our research. Section II introduces the dataset used in the study, along with a detailed explanation of the preprocessing steps such as normalization, class balancing, and feature preparation. In Section III,

- > tool for predicting the workload of EV charging stations. This was shown in the research by [17] when it came to handling massive datasets in different energy-related fields. A lot of LSTM (Long Short-Term Memory) networks have found usage here. To illustrate their capability in capturing

---

### 63. 2025_Short_term_demand_forecasting_of_electric_vehicle_charging_stations_using_context_aware_temporal_transformer_model.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://doi.org/10.3390/en16031309`](https://doi.org/10.3390/en16031309)](https://doi.org/10.3390/en16031309`)

- [`[https://doi.org/10.3390/en12142692`](https://doi.org/10.3390/en12142692)](https://doi.org/10.3390/en12142692`)

- [`[https://doi.org/10.1063/1.5012469`](https://doi.org/10.1063/1.5012469)](https://doi.org/10.1063/1.5012469`)

- [`[https://doi.org/10.1007/978-3-030-35543-2_14`](https://doi.org/10.1007/978-3-030-35543-2_14)](https://doi.org/10.1007/978-3-030-35543-2_14`)

- [`[https://doi.org/10.3390/electronics12010055`](https://doi.org/10.3390/electronics12010055)](https://doi.org/10.3390/electronics12010055`)

- ** 151430  Key Dataset Text Snippets / Context**:
- > Scientific Reports |        (2025) 15:36652 1 | [https://doi.org/10.1038/s41598-025-20557-x](https://doi.org/10.1038/s41598-025-20557-x) www.nature.com/scientificreports

- > !e accuracy and performance of the model using di#erent CS data need to be validated. !e main contribution of this work is the development of a Context-Aware Temporal Transformer (CAT-Former) model based on Contextual and Temporal Features, which is implemented using a public dataset of Boulder City. Furthermore, the proposed model is evaluated based on di#erent charging locations within the city to analyze the performance of di#erent charging trends. !e data used for the model training and testing are collected from multiple

- > vidual and hybrid models, along with the Transformer and Hybrid Transformer models. !is paper is organized as follows: Section "Literature review" reviews the related works. Section "Methodology" details the methodology. Section "Design and implementation" shows the dataset analysis, design, and implementation, including an overview of the baseline and proposed model and implementation details. Section "Results and discussion" discusses the results. Section Conclusion concludes this study.

- > Scientific Reports |        (2025) 15:36652 2 | [https://doi.org/10.1038/s41598-025-20557-x](https://doi.org/10.1038/s41598-025-20557-x) www.nature.com/scientificreports/

- > charging station (FCS) charging power consumption with an LSTM neural network. Deep learning methods like window normalization and weight initialization were used to forecast fast-charging power demand. !e forecasting model was validated using the real-world EV dataset from Jeju Island, South Korea. !e forecasting results indicate that the proposed LSTM model outperforms Bi-LSTM, GRU, and RNN with RMSE of 61.63, NMAE of 5.15%, and NRMSE of 6.65%.

---

### 64. 2025_Vertical_Federated_Learning_Method_for_EV_Charging_Station_Load_Prediction.pdf

- **Title**: REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains
- **Identified Datasets**: Dallas_Port_Logistics_Dataset
- **🔗 Extracted Web Links**:
- [`[https://doi.org/10.3390/app142110032`](https://doi.org/10.3390/app142110032)](https://doi.org/10.3390/app142110032`)

- [`[https://doi.org/10.1093/bib/bbab578`](https://doi.org/10.1093/bib/bbab578)](https://doi.org/10.1093/bib/bbab578`)

- [`[https://doi.org/10.1038/nature14539`](https://doi.org/10.1038/nature14539)](https://doi.org/10.1038/nature14539`)

- [`[https://doi.org/10.1007/s40565-019-0516-7`](https://doi.org/10.1007/s40565-019-0516-7)](https://doi.org/10.1007/s40565-019-0516-7`)

- [`[https://www.ncbi.nlm.nih.gov/pubmed/26017442`](https://www.ncbi.nlm.nih.gov/pubmed/26017442)](https://www.ncbi.nlm.nih.gov/pubmed/26017442`)

- ** 154285  Key Dataset Text Snippets / Context**:
- > Prediction in Coupled Transportation and Power Distribution Systems. Processes 2025, 13, 468. https:// doi.org/10.3390/pr13020468 Copyright: © 2025 by the authors.

- > and Power Distribution Systems. Processes 2025, 13, 468. https:// doi.org/10.3390/pr13020468 Copyright: © 2025 by the authors. Licensee MDPI, Basel, Switzerland.

- > conditions of the Creative Commons Attribution (CC BY) license ([https://creativecommons.org/](https://creativecommons.org/) licenses/by/4.0/). Article

- > the federated data-driven method. Processes 2025, 13, 468 [https://doi.org/10.3390/pr13020468](https://doi.org/10.3390/pr13020468)

- > Figure 1. The problems of charging station load prediction. Meanwhile, ID is a series of time points, not confidential data. This indicates there is rarely a distribution skew in sample quantity and labels in the federated dataset. Starting from the properties of DN and TN data, both are spatio-temporal correlated data. As shown in Figure 1, the characteristic distribution skew exists in both the temporal and

---

### 65. 2026_Attention_Enhanced_CNN_LSTM_Models_for_Forecasting_EV_Fast_Charging_Load_at_Public_Stations.pdf

- **Title**: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management
- **Identified Datasets**: ACN-Data
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/optuna/optuna`](https://github.com/optuna/optuna)](https://github.com/optuna/optuna`)

- ** 155867  Key Dataset Text Snippets / Context**:
- > dependencies, handling high variability in EV charging pat- terns, and maintaining scalability and efficiency with large datasets, which hinder their effectiveness, particularly for fast- charging stations. Most studies focus on single-step forecast- ing, which limits their ability to capture the temporal depen-

- > content may change prior to final publication. Citation information: DOI 10.1109/TIA.2026.3677828 © 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on July 21,2026 at 06:51:26 UTC from IEEE Xplore.  Restrictions apply.

- > been systematically examined or validated. Studies that focus on DC fast chargers remain limited, often relying on small, aggregated, or seasonal datasets that reduce model generalizability and robustness. For example, [19] employed CNNs to forecast fast-charging loads in the

- > chitecture. Section III presents the hyperparameter optimiza- tion framework used to fine-tune the models across multiple forecasting horizons. Section IV describes the dataset, feature engineering, and model development process. Section V eval- uates the forecasting results across both single-step and multi-

- > them well-suited for multi-dimension time-series analysis, and significantly enhances the model’s forecasting performance, particularly in multivariate time-series datasets. In our setting, the CNN does not model spatial structure in a geographic sense. Instead, its 1-D convolutions operate over the time axis

---

### 66. 2026_Decomposition_and_Stacked_Meta_Learning_for_Short_Term_Electric_Vehicle_Load_Forecasting.pdf

- **Title**: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management
- **Identified Datasets**: ACN-Data
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://ev.caltech.edu/dataset`](https://ev.caltech.edu/dataset)](https://ev.caltech.edu/dataset`)

- [`[https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-`](https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-)](https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-`)

- ** 158467  Key Dataset Text Snippets / Context**:
- > rely on implicit sequence learning and struggle to jointly capture multi-scale temporal structure, nonlinear interactions, and cross- dataset heterogeneity in EV charging demand. This paper pro- poses a decomposition-driven hybrid forecasting framework that integrates Seasonal-Trend decomposition using Loess (STL) with

- > fused through a Gradient Boosting Regressor meta-learner to enhance robustness and generalization. Experimental evaluation on four real-world EV charging datasets (ACN, Palo Alto, Perth, and Paris) demonstrates consistent performance gains over representative statistical, ensemble, and deep learning baselines.

- > Perth, and Paris) demonstrates consistent performance gains over representative statistical, ensemble, and deep learning baselines. On the ACN dataset, the proposed framework achieves MAE 0.614, RMSE 0.797, and MAPE 12.7%, corresponding to more than 90% and 88% reductions in RMSE and MAPE, respectively,

- > content may change prior to final publication. Citation information: DOI 10.1109/TSG.2026.3677496 © 2026 IEEE. All rights reserved, including rights for text and data mining and training of artificial intelligence and similar technologies. Personal use is permitted, but republication/redistribution requires IEEE permission. See [https://www.ieee.org/publications/rights/index.html](https://www.ieee.org/publications/rights/index.html) for more information. Authorized licensed use limited to: Chiang Mai University provided by UniNet. Downloaded on August 07,2026 at 16:04:50 UTC from IEEE Xplore.  Restrictions apply.

- > interpretability. • To conduct comprehensive experimental evaluation across four real-world EV charging datasets of varying scale and variability, demonstrating consistent performance im- provements and strong generalization compared to repre-

---

### 67. 2026_Mamba_3_Improved_Sequence_Modeling_using_State_Space_Principles.pdf

- **Title**: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management
- **Identified Datasets**: ACN-Data
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/state-spaces/mamba`](https://github.com/state-spaces/mamba)](https://github.com/state-spaces/mamba`)

- [`[https://github.com/state-spaces/mamba/issues/129`](https://github.com/state-spaces/mamba/issues/129)](https://github.com/state-spaces/mamba/issues/129`)

- [`[https://doi.org/10.5281/zenodo.12608602`](https://doi.org/10.5281/zenodo.12608602)](https://doi.org/10.5281/zenodo.12608602`)

- [`[https://zenodo.org/records/12608602`](https://zenodo.org/records/12608602)](https://zenodo.org/records/12608602`)

- [`[https://huggingface.co/meta-llama/Llama-3.2-1B`](https://huggingface.co/meta-llama/Llama-3.2-1B)](https://huggingface.co/meta-llama/Llama-3.2-1B`)

- ** 161382  Key Dataset Text Snippets / Context**:
- > our Mamba-3 variants advance the performance-latency Pareto frontier through their strong modeling capabilities and hardware-efficient design. 1[https://github.com/state-spaces/mamba.](https://github.com/state-spaces/mamba.) 2

- > 2In the original Mamba-2 paper,  161692 does not appear because it is viewed as folded into the B term. In this paper, B 161776 represents the continuous parameter, whereas in Mamba-2, B 161838 represents the discretized parameter which is equivalent to  161902  161906 B 161911 . 3While the Mamba-1 paper reports ZOH discretization, the implementation follows [https://github.com/state-spaces/mamba/issues/129.](https://github.com/state-spaces/mamba/issues/129.) 4

- > 4.1 Language Modeling All models are pretrained with 100B tokens of the FineWeb-Edu dataset (Penedo et al. 2024) with the Llama-3.1 tok- enizer (Grattafiori et al. 2024) at a 2K context length with the same standard training protocol. Training and evaluation details can be found in Appendix D.

- > Table 4: Retrieval capabilities measured by a mixture of real-world and synthetic retrieval tasks. Real-world retrieval tasks utilize cloze variants of the original datasets and are truncated to 2K length. Mamba-3 demonstrates strong associative recall, question-answering, and length generalization on needle-in-a-haystack (NIAH), but suffers with information extraction of semi-structured and unstructured data. The Transformer baseline uses RoPE which may explain its length generalization issues, and hybrid models utilize NoPE (no

- > 97.2 56.8 Table 5: Left: Ablations on core modeling components of Mamba-3 SISO, results on test split of dataset. Right: Formal language evaluation (scaled accuracy, %). Higher is better. SISO models are trained on short sequences and evaluated on longer lengths to test length generalization. For GDN we report the variant with eigenvalue range [−1, 1].

---

### 68. 2026_Multi_scale_fusion_transformer_for_EV_charging_station_load_prediction.pdf

- **Title**: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management
- **Identified Datasets**: ACN-Data
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://github.com/shivkumarjadon6/Hourly_EV`](https://github.com/shivkumarjadon6/Hourly_EV)](https://github.com/shivkumarjadon6/Hourly_EV`)

- ** 163812  Key Dataset Text Snippets / Context**:
- > Scientific Reports |         (2026) 16:8609 1 | [https://doi.org/10.1038/s41598-026-38562-z](https://doi.org/10.1038/s41598-026-38562-z) www.nature.com/scientificreports

- > nonlinear feature, thereby enabling more generalized load prediction16–18. For example, Chang et al. proposed an LSTM-based model to address the volatility of peak periods and power distributions in fast-charging loads, achieving strong prediction performance on a real-world dataset from Jeju Island19. Lu et al. applied various neural network architectures to the task of hourly aggregated load prediction, and verified that the LSTM model offered superior accuracy compared to other architectures through the backtesting procedure20. Guo et al.

- > an LSTM-based model to address the volatility of peak periods and power distributions in fast-charging loads, achieving strong prediction performance on a real-world dataset from Jeju Island19. Lu et al. applied various neural network architectures to the task of hourly aggregated load prediction, and verified that the LSTM model offered superior accuracy compared to other architectures through the backtesting procedure20. Guo et al. designed a multithreaded load prediction model that integrates user behavioral preferences by incorporating

- > Scientific Reports |         (2026) 16:8609 2 | [https://doi.org/10.1038/s41598-026-38562-z](https://doi.org/10.1038/s41598-026-38562-z) www.nature.com/scientificreports/

- > Scientific Reports |         (2026) 16:8609 3 | [https://doi.org/10.1038/s41598-026-38562-z](https://doi.org/10.1038/s41598-026-38562-z) www.nature.com/scientificreports/

---

### 69. 2026_PC_M3_Physics_Constrained_Mamba_MIMO_Aggregator_Real_Time_Energy_Management_EV_Clusters.pdf

- **Title**: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management
- **Identified Datasets**: ACN-Data
- **🔗 Dataset & Code Links (Direct/Long URLs)**:
- [`[https://platform.elaad.io/analyses/`](https://platform.elaad.io/analyses/)](https://platform.elaad.io/analyses/`)

- [`[https://ev.caltech.edu/dataset`](https://ev.caltech.edu/dataset)](https://ev.caltech.edu/dataset`)

- [`[https://github.com/zach401/acnportal`](https://github.com/zach401/acnportal)](https://github.com/zach401/acnportal`)

- ** 166211  Key Dataset Text Snippets / Context**:
- > virtual power plant; constraint-aware deep learning; differentiable projection Electronics 2026, 15, 2380 [https://doi.org/10.3390/electronics15112380](https://doi.org/10.3390/electronics15112380)

- > aggregators replace the true envelope with a zonotope, a ball, or a linear programming outer bound [5,6]; these enjoy analytical guarantees but, in our reimplementation on the datasets used here (Section 5), overshoot the true envelope by 10–25% of envelope width and lose most of the inter-temporal coupling that makes EV flexibility valuable. Learning- based aggregators use deep sequence models to predict flexibility or to solve the dispatch

- > aggregation and control method for heterogeneous EV clusters. The framework supports bidirectional V2G/G2V whenever a vehicle’s polytope admits a non-zero discharge rate [https://doi.org/10.3390/electronics15112380](https://doi.org/10.3390/electronics15112380)

- > Electronics 2026, 15, 2380 3 of 30 pi, but the public datasets we use for evaluation (ACN-Data, ElaadNL) are charge-only; bidirectional behaviour is exercised in this paper only through the synthetic dsgrid-TEMPO 10,000-vehicle stress test.

- > disaggregation training loop, benchmarked in Section 5.2 against LP/MILP/MPC and learned baselines. We evaluate PC-M3 on three open datasets that together cover behaviour, geography, and scale: ACN-Data [2] with the ACN-Sim simulator [12] (114,503 real workplace charg- ing sessions and a closed-loop test-bed), ElaadNL [13] (≈10,400 Dutch public charging

---

### 70. 2026_When_Mamba_Meets_KAN_Hybrid_Learning_Network_EV_Charging_Demand_Prediction.pdf

- **Title**: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management
- **Identified Datasets**: ACN-Data
- **🔗 Dataset Links**: No direct external data URL mentioned in PDF text.
- ** 168173  Key Dataset Text Snippets / Context**:
- > stage, we adopt a Kolmogorov–Arnold Network (KAN) to enhance nonlinear representation capacity for fine-grained demand projec- tion. Extensive experiments on a real-world EV charging dataset demonstrate that HyKANet consistently outperforms state-of-the-art spatio-temporal models across multiple forecasting horizons. Visu-

- > ternal encoding and bidirectional attention to adaptively integrate temporal and contextual signals. (d) We conduct extensive experi- ments on real-world datasets, showing that HyKANet consistently outperforms state-of-the-art baselines across multiple forecasting horizons and metrics.

- > both spatial and temporal dimensions. 3. EXPERIMENTS Dataset and Setup. HyKANet is implemented in PyTorch and evaluated on an Intel(R) i7-11700 CPU (2.5GHz) with an NVIDIA RTX 3090 GPU. Each experiment is repeated five times, and aver-

- > evaluated on an Intel(R) i7-11700 CPU (2.5GHz) with an NVIDIA RTX 3090 GPU. Each experiment is repeated five times, and aver- age results are reported. The dataset is split into 70%/15%/15% for training, validation, and testing. The model is trained with Adam op- timizer (learning rate 0.001, weight decay 1e−5), batch size 64, and

- > captures multi-scale temporal dependencies, hierarchical spatial patterns, and the influence of external contextual factors. Exten- sive experiments on real-world datasets demonstrate that HyKANet achieves superior prediction accuracy and generalization compared to state-of-the-art baselines.

---

## Newly ingested papers (2026-08-20)

### An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling

- **File**: `2018_Bai_Empirical_TCN_Sequence_Modeling.pdf`
- **Datasets**: synthetic sequence, music and language tasks
- **Paper**: [https://arxiv.org/abs/1803.01271](https://arxiv.org/abs/1803.01271)
- **Code**: [https://github.com/locuslab/TCN](https://github.com/locuslab/TCN)

### N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting

- **File**: `2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting.pdf`
- **Datasets**: M3, M4 and Tourism
- **Paper**: [https://arxiv.org/abs/1905.10437](https://arxiv.org/abs/1905.10437)
- **Code**: [https://github.com/ElementAI/N-BEATS](https://github.com/ElementAI/N-BEATS)

### N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting

- **File**: `2023_Challu_NHiTS_Neural_Hierarchical_Interpolation.pdf`
- **Datasets**: M4, Tourism, Electricity, Traffic and Wikipedia
- **Paper**: [https://arxiv.org/abs/2201.12886](https://arxiv.org/abs/2201.12886)
- **Code**: [https://github.com/Nixtla/neuralforecast](https://github.com/Nixtla/neuralforecast)

### Long-term Forecasting with TiDE: Time-series Dense Encoder

- **File**: `2024_Das_TiDE_Long_Term_Forecasting.pdf`
- **Datasets**: ETT, Electricity, Traffic, Weather, ILI and Exchange
- **Paper**: [https://arxiv.org/abs/2304.08424](https://arxiv.org/abs/2304.08424)
- **Code**: [https://github.com/google-research/google-research/tree/master/tide](https://github.com/google-research/google-research/tree/master/tide)
---

# [2026-08-23] Thorough Re-Ingestion Pass  Newly Verified Dataset Links

Full-text re-extraction of all 80 PDFs (

aw_sources/ -> scratch/txt/) with per-paper note rewrites. New/corrected dataset & code links discovered during the pass:

| Paper | Resource | URL |
|---|---|---|
| 2013 Roberts GP | GP tutorial code / GPML | ftp://ftp.robots.ox.ac.uk/pub/outgoing/mebden/misc/GPtut.zip ; [http://www.gaussianprocess.org/gpml](http://www.gaussianprocess.org/gpml) |
| 2014 Alizadeh | NHTS 2009 | [http://nhts.ornl.gov](http://nhts.ornl.gov) |
| 2017 Vaswani | tensor2tensor | [https://github.com/tensorflow/tensor2tensor](https://github.com/tensorflow/tensor2tensor) |
| 2017 Finn MAML | code (+RL) | [https://github.com/cbfinn/maml](https://github.com/cbfinn/maml) ; [https://github.com/cbfinn/maml_rl](https://github.com/cbfinn/maml_rl) |
| 2018 Bai TCN | code | [https://github.com/locuslab/TCN](https://github.com/locuslab/TCN) |
| 2019 Li LogSparse | NREL solar, EU wind | [https://www.nrel.gov/grid/solar-power-data.html](https://www.nrel.gov/grid/solar-power-data.html) ; [https://www.kaggle.com/sohier/30-years-of-european-wind-generation](https://www.kaggle.com/sohier/30-years-of-european-wind-generation) |
| 2020 Huang Ensemble | Boulder EV open data | [https://bouldercolorado.gov/open-data/electric-vehicle-charging-stations](https://bouldercolorado.gov/open-data/electric-vehicle-charging-stations) |
| 2021 Buzna Hierarchical | ElaadNL / ECMWF | [https://platform.elaad.nl](https://platform.elaad.nl) ; [https://www.ecmwf.int](https://www.ecmwf.int) |
| 2021 Zhang Queuing | Highways England WebTRIS + UK NTS | [http://tris.highwaysengland.co.uk/download/721b4186-feab-4691-94a0-2ded8f3ea94f](http://tris.highwaysengland.co.uk/download/721b4186-feab-4691-94a0-2ded8f3ea94f) ; [https://www.gov.uk/government/statistics/national-travel-survey-2005](https://www.gov.uk/government/statistics/national-travel-survey-2005) |
| 2021 Rasul TimeGrad | GluonTS datasets | [https://github.com/awslabs/gluonts](https://github.com/awslabs/gluonts) |
| 2021 Lim TFT | TFT code / Favorita / Oxford-Man | [https://github.com/google-research/google-research/tree/master/tft](https://github.com/google-research/google-research/tree/master/tft) ; [https://www.kaggle.com/c/favorita-grocery-sales-forecasting](https://www.kaggle.com/c/favorita-grocery-sales-forecasting) ; [https://realized.oxford-man.ox.ac.uk](https://realized.oxford-man.ox.ac.uk) |
| 2021 Stankeviciute CF-RNN | code | [https://github.com/kamilest/conformal-rnn](https://github.com/kamilest/conformal-rnn) |
| 2021 Tashiro CSDI | code | [https://github.com/ermongroup/CSDI](https://github.com/ermongroup/CSDI) |
| 2021 Wu Autoformer | code | [https://github.com/thuml/Autoformer](https://github.com/thuml/Autoformer) |
| 2021 Zhou Informer | ETT / code | [https://github.com/zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset) ; [https://github.com/zhouhaoyi/Informer2020](https://github.com/zhouhaoyi/Informer2020) |
| 2022 Kim RevIN | SCINet repo | [https://github.com/cure-lab/SCINet](https://github.com/cure-lab/SCINet) |
| 2022 Cao Robust DGP | COVID load code / ENTSO-E | [https://github.com/chennnnnyize/Load-Forecasting-During-COVID-19](https://github.com/chennnnnyize/Load-Forecasting-During-COVID-19) ; [https://transparency.entsoe.eu](https://transparency.entsoe.eu) |
| 2023 Challu NHiTS | code | [https://github.com/Nixtla/neuralforecast](https://github.com/Nixtla/neuralforecast) |
| 2023 Huang MetaProbformer | code + Palo Alto/Boulder/ElaadNL/Perth | [https://github.com/XingshuaiHuang/MetaProbformer](https://github.com/XingshuaiHuang/MetaProbformer) ; [https://data.cityofpaloalto.org](https://data.cityofpaloalto.org) ; [https://data.pkc.gov.uk/dataset/ev-charging-data](https://data.pkc.gov.uk/dataset/ev-charging-data) |
| 2023 Koohfar | Boulder EV data dictionary | [https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv](https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv) |
| 2023 Wu TimesNet | code | [https://github.com/thuml/TimesNet](https://github.com/thuml/TimesNet) |
| 2023 Zeng DLinear | code | [https://github.com/cure-lab/LTSF-Linear](https://github.com/cure-lab/LTSF-Linear) |
| 2023 Zhang Crossformer | code | [https://github.com/Thinklab-SJTU/Crossformer](https://github.com/Thinklab-SJTU/Crossformer) |
| 2024 Qu PAG | ST-EVCDP (Shenzhen) code | [https://github.com/IntelligentSystemsLab/ST-EVCDP](https://github.com/IntelligentSystemsLab/ST-EVCDP) |
| 2024 Zhong V2G-SVE | ASU Campus Metabolism / Ausgrid | [https://cm.asu.edu](https://cm.asu.edu) ; [https://www.ausgrid.com.au](https://www.ausgrid.com.au) |
| 2024 Ke DC-Former | Pecan Street Dataport | [https://www.pecanstreet.org/dataport/](https://www.pecanstreet.org/dataport/) |
| 2024 Bampos DAM | Palo Alto / Electric Nation / ACN | [https://data.cityofpaloalto.org](https://data.cityofpaloalto.org) ; [https://opennetzero.org/dataset/electric-nation](https://opennetzero.org/dataset/electric-nation) ; [https://ev.caltech.edu/dataset](https://ev.caltech.edu/dataset) |
| 2024 Cao FEDM | FEDQR dataset (on request) | [https://github.com/Kenny4everlucky/FEDQR_dataset](https://github.com/Kenny4everlucky/FEDQR_dataset) |
| 2024 Zhou HPCP | US Census / Project Sunroof | [https://data.census.gov](https://data.census.gov) ; [https://sunroof.withgoogle.com](https://sunroof.withgoogle.com) |
| 2024 Helmy Autoformer | Boulder dataset (direct) | [https://opendata.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0](https://opendata.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0) |
| 2025 Meyer Benchmark | OPSD / REFIT / IDEAL repos | [https://data.open-power-system-data.org](https://data.open-power-system-data.org) ; REFIT & IDEAL DOIs in paper note |
| 2025 Zheng Coherent | Meteostat / CP-Flow | [https://meteostat.net](https://meteostat.net) ; [https://github.com/cvxgrp/CP-Flow](https://github.com/cvxgrp/CP-Flow) |
| 2025 Alghamdi RESTNet | Dallas port EV Kaggle | [https://doi.org/10.34740/KAGGLE/DSV/9490653](https://doi.org/10.34740/KAGGLE/DSV/9490653) |
| 2025 Tian MSSTGAN | 4-city data repo (Palo Alto/Boulder/Dundee/Perth) | [https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand](https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand) |
| 2025 Matrone QR-LSTM | KNMI weather | [https://www.knmi.nl/nederland-nu/klimatologie/daggegevens](https://www.knmi.nl/nederland-nu/klimatologie/daggegevens) |
| 2025 Hussain CAT-Former | Boulder direct link | [https://opendata.bouldercolorado.gov/datasets/95992b3938be4622b07f0b05eba95d4c_0](https://opendata.bouldercolorado.gov/datasets/95992b3938be4622b07f0b05eba95d4c_0) |
| 2025 Bao ResMMoT | NASDAQ100 Kaggle | [https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data](https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data) |
| 2026 Chen PC-M3 | ACN-Data / ElaadNL / dsgrid-TEMPO / ACN-Sim | [https://ev.caltech.edu/dataset](https://ev.caltech.edu/dataset) ; [https://platform.elaad.io/analyses/](https://platform.elaad.io/analyses/) ; [https://data.openei.org/submissions/5958](https://data.openei.org/submissions/5958) ; [https://github.com/zach401/acnportal](https://github.com/zach401/acnportal) |
| 2026 Romia CNN-LSTM | NREL SAM weather | [https://sam.nrel.gov](https://sam.nrel.gov) |
| 2026 Liu MFT | Norway hourly EV repo | [https://github.com/shivkumarjadon6/Hourly_EV](https://github.com/shivkumarjadon6/Hourly_EV) |

**Metadata corrections applied during re-ingestion**: Cheng VMD-Prophet-LSTM is 2023 (Front. Energy Res., not 2025); Huang Lyapunov paper is arXiv:2604.16873 (Apr 2026); Alizadeh DOI = 10.1109/TSG.2013.2275988; Shi STMGCN DOI = 10.1109/TSG.2023.3321116; Wu Meta-PIGACN DOI = 10.1109/TNSE.2025.3525625; Toubeau fabricated results replaced with verified figures.

---

# [2026-08-23] New Ingestion Batch - 6 Elsevier Papers (raw_sources/new)

| Paper | Key Dataset(s) | Access |
|---|---|---|
| MoghadamDost TFT-Conformal | Palo Alto hourly 2018-2022 + Open-Meteo weather API | on request / open API |
| Wang Xiaoping TriCast | UrbanEV Shenzhen subset (>18k stations, 247 zones, 5-min occupancy+price; Li et al. Sci Data 2025) | on request |
| Wang Xu Similar-Day | UrbanEV Shenzhen (275 traffic zones, hourly Sep 2022-Feb 2023), GitHub repo of Li et al. Sci Data 12 | repo-linked |
| Singh MAML-Informer | ACN-Data (ev.caltech.edu), Boulder Open Data, Palo Alto (via Amara-Ouali et al. DOI 10.3390/en14082233) | open |
| Wang Shengyou Transferability | 12 session datasets: Perth, Dundee, Hong Kong, Palo Alto, Boulder + 7 Perthshire towns (30 days each) | on request |
| Zhang Jinlai USDT | EVnetNL (platform.elaad.io), Perth (data.pkc.gov.uk), Boulder, Palo Alto (data.cityofpaloalto.org) | open |

New dataset page created: `wiki/datasets/UrbanEV_Dataset.md`. DOIs: 10.1016/j.compeleceng.2026.111201, 10.1016/j.patrec.2026.04.028, 10.1016/j.apenergy.2026.127731, 10.1016/j.asoc.2026.115869, 10.1016/j.est.2026.122141, 10.1016/j.segan.2026.102428.


---

# [2026-08-23] New Ingestion Batch 2 - 6 arXiv Foundational Papers

| Paper | Key Dataset(s) | Code |
|---|---|---|
| Graph WaveNet (IJCAI 2019) | METR-LA (207 sensors, 5-min), PEMS-BAY (325 sensors, 5-min) | github.com/nnzhan/Graph-WaveNet |
| DiffSTG (2023) | PEMS08, AIR-BJ, AIR-GZ (Beijing/Guangzhou PM2.5) | github.com/wenhaomin/DiffSTG |
| TimeMachine (2024) | Weather/Traffic/Electricity/ETT x4 | github.com/Atik-Ahamed/TimeMachine |
| Bi-Mamba+ (2024) | ETT/ECL/Traffic/Weather/Solar/Exchange | github.com/Leopold2333/Bi-Mamba+ |
| KAN (2024) | synthetic/Feynman/knot benchmarks | github.com/KindXiaoming/pykan |
| LipSCDE (2023) | MIMIC-III, COVID-19 German districts | none printed |


---

# [2026-08-23] New Ingestion Batch 3 - 11 Papers (EV + foundational)

| Paper | Key Dataset(s) | Access/URL |
|---|---|---|
| Jia EVformer (WEVJ 2026) | ST-EVCDP Shenzhen (18,061 piles, 247 nodes) | github.com/IntelligentSystemsLab/ST-EVCDP |
| Zhou MixerInformer (2025) | Boulder CO 26 stations | opendata.bouldercolorado.gov |
| Kyriakopoulos comparison (2026) | Palo Alto/Boulder/Dundee/Perth | github.com/yvenn-amara/ev-load-open-data |
| He JointPGM (2024) | Exchange/ETT/Electricity/METR-LA/ILI | UCI/CDC links |
| Xiong CNN-LSTM-Transformer (2023) | Boulder ST1 station | bouldercolorado.gov open data |
| Huo ANN/SVR/BRT (2024) | ACN Caltech+JPL | ev.caltech.edu |
| Li CNN-GRU TOU (2024) | mall station 1800 kW China (private) | not public |
| Ma LASSO-BPNN (2024) | Shanghai Qingpu monthly + stats bureau | shqp.gov.cn/public |
| Shi PI evaluation (2024) | US feeder smart meter + synthetic EV | no URL |
| DeVilmarest adaptive net-load (2024) | GB 14 GSP half-hourly; US 7-city COVID | zenodo DOIs 10.5281/zenodo.7849665 / .5031704 |
| Qu Forwardformer (2024) | CEL-NW/SE China; AEL New York State | no URLs printed |


## [2026-08-23] Batch 4 Web-Ingest | New Dataset & Repo URLs (papers 104-108)

| Paper | Datasets / Resources | Links |
|-------|----------------------|-------|
| Yu EnergyMamba (KDD '26) | NYISO load data | https://www.nyiso.com/load-data |
| Yu EnergyMamba (KDD '26) | CAISO today's outlook | https://www.caiso.com/TodaysOutlook |
| Yu EnergyMamba (KDD '26) | Florida census block group smart-meter data | NDA-restricted, not public |
| Yu EnergyMamba (KDD '26) | Official code | https://github.com/UFOdestiny/EnergyMamba |
| Hong & Lee US-grid benchmark (2026) | EIA-930 hourly system load, six ISOs (CAISO/ISO-NE/MISO/PJM/ERCOT/NYISO) | https://www.eia.gov/electricity/gridmonitor/ |
| Hong & Lee US-grid benchmark (2026) | Open-Meteo weather archive | https://open-meteo.com |
| Hong & Lee US-grid benchmark (2026) | Benchmark code + checkpoints | https://github.com/gramm-ai/grid-forecast-benchmark |
| Menati PowerMamba (2024) | ERCOT GridSet (5-year hourly, 22 core / 262 extended channels) + toolbox | https://github.com/alimenati/PowerMamba |
| Bouaachra INLA Scotland (2026) | ChargePlace Scotland open-access repository (Transport Scotland); Oct 2022 - Apr 2025; Glasgow subset 96 CPIDs / 104,041 sessions | chargeplace.org.uk open data portal (exact Zenodo/Git mirror URLs pending from arXiv HTML source) |
| Fernandez-Zapico MPC hub (CDC 2025) | Hub simulation code | https://github.com/diegofz/ChargingEnergyHubs_MPC |
| Fernandez-Zapico MPC hub (CDC 2025) | ENTSO-E Transparency Platform (NL prices/CO2) | https://transparency.entsoe.eu/ |
| Fernandez-Zapico MPC hub (CDC 2025) | EV session source: Gholizadeh & Musilek, Data in Brief 2024 | see paper references |
| Fernandez-Zapico MPC hub (CDC 2025) | NREL OpenEI PVDAQ farm solar array | https://openei.org/wiki/PVDAQ/Sites/Farm_Solar_Array |

### 2024_Das_TimesFM_Decoder_Only_Foundation_Model.pdf

- **Title**: A Decoder-Only Foundation Model for Time-Series Forecasting (TimesFM)
- **Identified Datasets**: Google Trends (~22k queries, ~0.5B points), Wikipedia Pageviews (~360B points, 5.6M hourly series), Synthetic (3M series, 6.1B points), M4 (all granularities, ~99k series), Electricity/ECL (321 clients, 8.4M pts), Traffic (862 sensors 15.1M + LibCity 6,159 series 34.3M), Weather 10-min (42 vars, 2.2M), Favorita Sales (111k series, 139M), LibCity; Evaluation: Monash Archive (18 datasets), Darts (8 series), ETT (ETTh1/2 + ETTm1/2)
- **Extracted Web Links**:
  - https://trends.google.com (Google Trends, Ch.5)
  - https://wikimedia.org/api/rest_v1/ (Wiki Pageviews, Ch.5)
  - https://huggingface.co/datasets/monash_tsf (Monash mirror, p.7)
  - https://github.com/unit8/darts (Darts, p.8)
  - https://github.com/zhouhaoyi/ETDataset (ETDataset)
  - https://github.com/ngruver/llmtime/blob/main/experiments/run_monash.py (llmtime baseline code, p.16)
  - https://github.com/google-research/google-research/tree/master/tide (TiDE ref)
- **Key Dataset Text Snippets / Context**:
  - Pretraining corpus Table 1: ~100B time-points after mixing (80% real / 20% synthetic, equal granularity-group weights); Wiki hourly 5,608,693 series / 239B pts, Wiki daily/weekly/monthly ~66M each; synthetic ARMA+seasonal+trend+step (3M x 2048).
  - Evaluation held-out: Monash 18 datasets (australian electricity demand, bitcoin, pedestrian counts, weather, nn5 daily/weekly, tourism yearly/quarterly/monthly, cif 2016, covid deaths, fred md, traffic hourly/weekly, saugeenday, us births, hospital, solar weekly), Darts 8 series, ETT 4 datasets x 2 horizons (96/192, last-window due to llmtime cost).

---
### 2026_Khwaja_Toto_2_Scaling_Era.pdf — Toto 2.0: Time Series Forecasting Enters the Scaling Era

**Datasets extracted:**
- **BOOM** — Datadog observability benchmark (CPU/memory/latency/error rates; context 2048; CRPS rank/CRPS/MASE) — Cohen et al. 2025
- **GIFT-Eval** — 97 tasks from 23 base datasets (energy/retail/weather/finance; context 4096; Pretrain: https://huggingface.co/datasets/Salesforce/GiftEvalPretrain — 45% of FT mix; train splits: https://huggingface.co/datasets/Salesforce/GiftEval — 15% of FT mix)
- **TIME Benchmark** — 98 tasks from 50 fresh datasets (Qiao et al. 2026, arXiv:2602.12147; avoids legacy ETTh1/Electricity/Traffic/Weather)
- **Datadog Internal Observability** — 2.14T points (42.5% of large mix; 10s 20% / 60s 7.5% / 5+m 15%; private, no customer data)
- **TempoPFN Synthetic** — 2.90T points (57.5% of large mix; Moroshan et al. 2025, PFN framework Muller et al. 2022) — hand-crafted prior with nonstationary trends/changepoints/long-range deps

**URLs / Access:**
- Code: https://www.github.com/DataDog/toto
- Weights (Apache 2.0): https://huggingface.co/collections/Datadog/toto-20
- Library dd_unit_scaling: distributed u-muP (torch.compile/FSDP2/DP-TP) — Apache 2.0
- GIFT-Eval: https://huggingface.co/datasets/Salesforce/GiftEval
- GIFT-Eval Pretrain: https://huggingface.co/datasets/Salesforce/GiftEvalPretrain
---
## [2025-09-01] 2025_Ansari_Chronos_2_Univariate_to_Universal — Chronos-2: From Univariate to Universal Forecasting (Ansari et al. 2025, arXiv:2510.15821v1)

**Datasets extracted (3 benchmarks + pretraining corpora, Table 6, Section 4-5):**

| # | Dataset | Location / Access / URLs | Extracted fields |
|---|---|---|---|
| 1 | fev-bench | https://github.com/amazon-science/chronos-forecasting ; Shchur et al. 2025 — 100 tasks (32 univariate / 26 multivariate / 42 covariate-informed, past-only + known) | 100 tasks, SQL metric, 0% leakage, 0 failures for Chronos-2 |
| 2 | GIFT-Eval | https://huggingface.co/datasets/Salesforce/GiftEval (Aksu et al. 2024) | 97 tasks / 55 datasets, high-frequency + long horizons, WQL/MASE |
| 3 | Chronos Benchmark II | Ansari et al. 2024 (TMLR) — 27 tasks, short histories <300 steps avg | WQL/MASE |
| 4 | GIFT-Eval Pretrain corpus | https://huggingface.co/datasets/Salesforce/GiftEvalPretrain | Real-univariate pretraining mix, test portions excluded |
| 5 | Chronos Corpus | Ansari et al. 2024 — select Table 6 (Electricity 370, Solar 5166, Taxi 2428, Wiki 100k, USHCN 225280, Weatherbench 225280, M4 Daily 4227 etc.) | Frequencies 5min-1M, 22 datasets listed |
| 6 | Synthetic univariates | TSI (Bahrpeyma et al. 2021), TCM (Runge et al. 2023), AR/ETS/KernelSynth | Trend/seasonality/irregularity + causal-graph autoregression |
| 7 | Synthetic multivariate/covariate | Multivariatizers (contemporaneous + sequential) — entirely synthetic, random subset designated as known covariates | Multivariate dependencies (instantaneous + lead-lag/cointegration) |
| 8 | Code repo | https://github.com/amazon-science/chronos-forecasting | GluonTS/AutoGluon dependencies |
| 9 | Benchmark tools | fev-bench tooling (Shchur et al. 2025), GIFT-Eval leaderboard, Chronos Benchmark II | Evaluation with win rate / skill score |

**Energy/retail case studies from fev-bench:** EPF-DE (German day-ahead energy price with load + solar/wind covariates, hourly) and Rossmann weekly store sales (promotion/holiday features) — Figs. 6-7.

**Tables imported to paper note:** Table 1 (capability matrix O(V) vs O(V²)), Table 2 (groupID/W masking for 3 task types), Table 3 (fev-bench SQL), Table 4 (GIFT-Eval WQL/MASE), Table 5 (Chronos Bench II), Fig.2 (pairwise CIs), Fig.3-5 (ICL gains), Fig.8 (ablations: 28M, synthetic-only, 8192 ctx).

**Dataset pages updated/created:** [[fev-bench]], [[Chronos_Benchmark_II]], [[Chronos_Corpus]], [[GIFT-Eval]], [[GIFT_Eval_Pretrain]], [[Electricity_ECL]], [[M4]], [[Solar_Dataset]], [[Traffic]], [[Weather]], [[Wiki_Pageviews]], [[Buildings_900K]].

