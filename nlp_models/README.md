This folder contains experiments performed with various SOA NLP models for different tasks:

<ins>BERT</ins>

BERT (Bi-Directional encoders from transformers) is from a [paper](https://arxiv.org/pdf/1810.04805.pdf) published by 
Google in 2018. It is based on transformers  
(introduced in [Attention is all you need](https://arxiv.org/abs/1706.03762)). 
It is designed to be used as a pre-trained model that can be fine-tuned for a range of tasks including 
Question Answering, language inference and discourse analysis, without much change to the architecture.

- The BERT-intro notebook 
[developed while going through a Coursera tutorial](https://www.coursera.org/projects/sentiment-analysis-bert) , 
is focussed using a simple model with only one oputput layer to see the performance of the model for 
Sentiment Analysis on [SMILE dataset](https://www.kaggle.com/ashkhagan/smile-twitter-emotion-dataset). 
The introduction notebook focuses on tweets with single sentiments, for the purpose of simplicity.

- IN BERT-SA notebook, the focus is fine-tuning the BERT model to recognize multiple sentiments in the text. 
While the model still remains mostly the same, data pre-processing is modified a bit. The model is also fine-tuned 
to learn the complexities of a multi-label classification

- In BERT-NMT, neural machine translation is performed.
