# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 
import nltk
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

%matplotlib inline


dir = os.getcwd()
dir

train_data = pd.read_csv("../input/train.csv")

train_data.head()

len(train_data)

train_data = train_data[train_data.Tweet != 'Not Available']

# stopwords, URL's, RT cleanup coming soon!

len(train_data)

train_data.head()

feedback = train_data['Tweet']
train = []
sia = SentimentIntensityAnalyzer()
for sentence in feedback:
     # print(sentence)
     s = sia.polarity_scores(sentence)
     for v in s:
         # print('{0}: {1}, '.format(v, s[v]), end='\n')
         if v == 'compound' and s[v] > 0:
             train.append((sentence, "pos"))
         elif v == 'compound' and s[v] <= 0:
             train.append((sentence, "neg"))

train

dictionary = set(word.lower() for sentence in train for word in word_tokenize(sentence[0]))
dictionary

t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]

classifier = nltk.NaiveBayesClassifier.train(t)

test_data = "Why should I tweet against someone?"

test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}

test_data_features

classifier.classify(test_data_features)

