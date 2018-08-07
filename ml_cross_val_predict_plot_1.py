import tkinter
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_predict

import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

X = diabetes.data[:150]
y = diabetes.target[:150]
print(X, y)
print(X.shape, y.shape)

lasso = linear_model.Lasso()
print(lasso)

y_pred = cross_val_predict(lasso, X, y)
print(y_pred)

fig, ax = plt.subplots()
ax.scatter(y, y_pred, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
