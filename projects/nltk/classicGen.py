import nltk
import sklearn
from nltk import word_tokenize as wt

# --------- optional start ------------ #
f = open('NEWS.txt', encoding='utf-8')
raw = f.read()

# WORD TOKENIZER
tokens = wt(raw)

# CREATE NLTK TEXT 
txt = nltk.Text(tokens)
# ----------optional end -------------- #

# CLASSIFIER
from nltk.corpus import names

# SINGLE FEATURE GENERATOR & CLASSIFICATION #
# ------------------- start --------------- #
def feature_generator(word):
    return {'last_letter': word[-1]}

print(feature_generator('praveen'))

import random

names = ([(name, 'male') for name in names.words('male.txt')] + \
			[(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

featuresets = [(feature_generator(n), g) for (n,g) in names]
print(featuresets[:10])
print(len(featuresets))

from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(featuresets, test_size=0.25, random_state=42)

print(len(train_set), type(train_set))
print(len(test_set), type(test_set))

# CLASSIFIER
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(classifier)

def classify_gender(s):
    return classifier.classify(feature_generator(s))

print(classify_gender('Praveen'))
print(classify_gender('Ra'))

# ACCURACY SCORE
print(nltk.classify.accuracy(classifier, test_set))

# INFORMATIVE FEATURES
print(classifier.show_most_informative_features(5))

# ----------------- end ------------------ #


# MULTIPLE FEATURES + CLASSIFIER #
# ------------------- start -------------- #

def feature_generator2(word):
    return {'name_length': len(word), 'last_letter': word[-1]}

featuresets2 = [(feature_generator2(n), g) for (n,g) in names]

train_set2, test_set2 = train_test_split(featuresets2, test_size=0.25, random_state=42)

print(len(train_set2), type(train_set2))
print(len(test_set2), type(test_set2))

classifier2 = nltk.NaiveBayesClassifier.train(train_set2)
print(classifier2)

def classify_gender2(s):
    return classifier2.classify(feature_generator2(s))

print(classify_gender2('Praveen'))
print(classify_gender2('Fa'))


# ACCURACY SCORE
print(nltk.classify.accuracy(classifier2, test_set2))

# INFORMATIVE FEATURES
print(classifier2.show_most_informative_features(5))
# ------------------ end ---------------- #
