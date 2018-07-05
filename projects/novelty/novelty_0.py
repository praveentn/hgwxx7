import tkinter as tk 
import numpy as np  
import pandas as pd  
from sklearn import utils
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib.font_manager

# random data
c = np.random.randint(low=-2.5, high=3, size=(100))
d = np.random.randint(low=-2.5, high=3, size=(77))
e = np.random.randint(low=-5, high=1, size=(22))

# train
X_train = np.array([np.arange(0,100), c]).T
print(X_train)
print(X_train.shape)

# normal
X_test = np.array([np.arange(0,77), d]).T
print(X_test)
print(X_test.shape)

# outlier
X_outliers = np.array([np.arange(78,100), e]).T
print(X_outliers)
print(X_outliers.shape)

# fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)
print(clf)

y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)

print(y_pred_train, y_pred_test, y_pred_outliers)

n_error_train = y_pred_train[y_pred_train == 1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == -1].size

xx, yy = np.meshgrid(np.linspace(0, 100, 100), np.linspace(-5, 5, 100))
print(xx.shape)

# plot the line, the points, and the nearest vectors to the plane
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

print(Z.shape)
print(Z.min())

# print(np.c_[xx.ravel()])
# print(np.c_[yy.ravel()])

plt.figure(figsize=(11,7))
plt.title("Novelty Detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')

s = 15
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c='white', s=s, edgecolors='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c='blueviolet', s=s*2, edgecolors='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c='gold', s=s*3, edgecolors='k')
plt.axis('tight')
#plt.xlim((-5, 5))
#plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned frontier", "training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.xlabel(
    "error train: %d/100 ; errors novel regular: %d/77 ; "
    "errors novel abnormal: %d/22"
    % (n_error_train, n_error_test, n_error_outliers))
plt.show()

