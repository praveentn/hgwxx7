import tkinter
import numpy as np
import pandas as pd
import category_encoders as ce

from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier


col_names = ['age', 'work-class', 'fnlwgt', 'education', 'education-num', 'marital-status', 
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
            'hrs-per-week', 'native-country', 'income']

data = pd.read_csv('income.csv', header = None, names = col_names, na_values = " ?")

print(data.shape)
data.head(n = 10)

## Search for NAN values:
print(data[data.isnull().any(axis=1)].count())
print(data.isnull().values.sum())
data = data.dropna(axis = 0)
print(data.shape)

data.dtypes


## first the simplest ones
# Income: map >50K: 1, <=50K: 0
data['income'] = data['income'].map({' >50K': 1, ' <=50K': 0})
# data['income'].astype('int32')
# Sex: map Male: 1, Female: 0
data['sex'] = data['sex'].map({' Male': 1, ' Female': 0})
# data['sex'].astype('int32')
data.head(n = 10)

##  Merge Never-worked & Without pay
data['work-class'] = data['work-class'].replace([' Without-pay', ' Never-worked'], 'Unpayed')
print(data['work-class'].value_counts().count())
data['work-class'].unique()

## Not many different categories so will use Label Encoding
labels = data['work-class'].astype('category').cat.categories.tolist()
mapping = {'work-class': {k: v for k, v in zip(labels, list(range(1, len(labels)+1)))}}

data.replace(mapping, inplace = True)

data.head(n = 10)

data = data.drop(columns = ['education-num'], axis = 1)
print(data['education'].value_counts())

data.head(n = 2)

data['education'] = data['education'].replace([' 10th', ' 11th', ' 12th'], 'HS-Student')
data['education'] = data['education'].replace([' 7th-8th', ' 9th'], 'Mid-Student')
data['education'] = data['education'].replace([' 5th-6th', ' 1st-4th'], 'Elem-Student')

print(data['education'].value_counts())

labels = data['education'].astype('category').cat.categories.tolist()
mapping = {'education': {k: v for k, v in zip(labels, list(range(1, len(labels)+1)))}}

data.replace(mapping, inplace = True)

data.head(n = 10)

labels = data['marital-status'].astype('category').cat.categories.tolist()
mapping = {'marital-status': {k: v for k, v in zip(labels, list(range(1, len(labels)+1)))}}
data.replace(mapping, inplace = True)

labels = data['relationship'].astype('category').cat.categories.tolist()
mapping = {'relationship': {k: v for k, v in zip(labels, list(range(1, len(labels)+1)))}}
data.replace(mapping, inplace = True)

labels = data['race'].astype('category').cat.categories.tolist()
mapping = {'race': {k: v for k, v in zip(labels, list(range(1, len(labels)+1)))}}
data.replace(mapping, inplace = True)

data.head(n = 10)

## Occupation & Nativity have many categories > Binary Encode
encoder = ce.BinaryEncoder(cols = ['occupation', 'native-country'])
data = encoder.fit_transform(data)

data.head(n = 10)

labels = data['income']
features = data.drop(columns = ['income'], axis = 1)

labels.head(n = 5)
features.head(n = 5)

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.25, random_state = 2)
print(X_train.shape)
print(X_test.shape)

model = XGBClassifier()
model.fit(X_train, y_train)
print(model)

y_hat_train = model.predict(X_train)
train_pred = [round(value) for value in y_hat_train]

train_accuracy = accuracy_score(y_train, train_pred)
print('Train Accuracy: ', train_accuracy)

y_hat_test = model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_hat_test)
print('Test Accuracy: ', test_accuracy)
