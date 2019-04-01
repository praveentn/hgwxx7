
## Word Embeddings

There are numerous embeddings you can find online trained on different corpuses (large bodies of text). Here, we'll be using Keras to come up with custom embeddings for a particular corpus of words.

When we have enough data and computational power, it’s usually better to train and build one's own embeddings for a specific task.

### Files:
corpus: ../data/neural_network_patent_query.csv<br/>
utils file: ../utils.py (helper functions)<br/>
notebook: rnn_word_embedding_1.ipynb<br/>

### Requirements:
tensorflow==1.12.0<br/>
Keras==2.2.4<br/>
Keras-Applications==1.0.6<br/>
Keras-Preprocessing==1.0.5<br/>
numpy==1.15.4<br/>
pandas==0.23.4<br/>

Credits: https://github.com/WillKoehrsen/recurrent-neural-networks
