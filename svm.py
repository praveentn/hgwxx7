import tkinter as tk

# Support Vector Machine

# Separation of classes!!

# A Support Vector Machine (SVM) is a discriminative classifier formally defined by a separating hyperplane. 
# In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples. 
# In two dimensional space this hyperplane is a line dividing a plane in two parts where in each class lay in either side. 

# SVM is a supervised machine learning algorithm which can be used for both classification or regression problems. It's mainly used in classification problems.

# Support Vectors are the co-ordinates of individual observation. 

# Support Vector Machine is a frontier which best segregates the two classes (hyper-plane/ line).

# Tuning Parameters

# Kernel defines the type of separation (linear, polynomial, exponential)

# Regularization parameter (C parameter in sklearn classification) tells the SVM optimization how much you want to avoid misclassifying each training example.

# Gamma parameter defines how far the influence of a single training example reaches, with low values meaning ‘far’ and high values meaning ‘close’. In other words, with low gamma, points far away from plausible seperation line are considered in calculation for the seperation line. Where as high gamma means ONLY those points close to plausible line are considered in calculation.

# Margin is a separation of line to the closest class points. A good margin is one where this separation is larger for both the classes. Images below gives to visual example of good and bad margin. A good margin allows the points to be in their respective classes without crossing to other class.

# import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import accuracy_score

# import built-in iris dataset
iris = datasets.load_iris()
print(type(iris))
# print(iris)

iris_X = iris.data[:, :2]
# print(iris_X)

iris_y = iris.target
print(iris_y)

# Visualizing the relationship between sepal and target classes
def visuvalize_sepal_data():
	plt.scatter(iris_X[:, 0], iris_X[:, 1], c=iris_y, cmap=plt.cm.coolwarm)
	plt.xlabel('Sepal length')
	plt.ylabel('Sepal width')
	plt.title('Sepal Width & Length')
	plt.show()

visuvalize_sepal_data()

# Visualizing the relationship between Petal and target classes
def visuvalize_petal_data():
    iris_Xp = iris.data[:, 2:]   # last two features are for petal
    plt.scatter(iris_Xp[:, 0], iris_Xp[:, 1], c=iris_y, cmap=plt.cm.coolwarm)
    plt.xlabel('Petal length')
    plt.ylabel('Petal width')
    plt.title('Petal Width & Length')
    plt.show()

visuvalize_petal_data()



iris_X_train = iris_X[:-10]
iris_y_train = iris_y[:-10]
iris_X_test  = iris_X[-10:]
iris_y_test  = iris_y[-10:]

# initialize instance of SVM Classification 
svc = svm.SVC(kernel='linear', C=10.0, gamma=0.37)
print(type(svc))

print("Training model")
#train model
svc.fit(iris_X_train, iris_y_train)

predicted_labels = svc.predict(iris_X_test)
print("Accuracy score after classification: " + str(accuracy_score(iris_y_test, predicted_labels)*100) + "%")

# change to rbf kernel
# svc = svm.SVC(kernel='rbf', C=1,gamma=0.37).fit(iris_X, iris_y)

# create a mesh to plot in
x_min, x_max = iris_X[:, 0].min() - 1, iris_X[:, 0].max() + 1
y_min, y_max = iris_X[:, 1].min() - 1, iris_X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
print(Z)
print(type(Z))

Z = Z.reshape(xx.shape)
print(Z)
print(type(Z))

plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
plt.scatter(iris_X[:, 0], iris_X[:, 1], c=iris_y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()



C = 1.0  # SVM regularization parameter

# title for the plots
titles = ['SVC with Linear kernel',
	   'Linear SVC (Linear kernel)',
	    'SVC with RBF kernel',
	    'SVC with Polynomial (degree 3) kernel']

# SVC with linear kernel
svc = svm.SVC(kernel='linear', C=C).fit(iris_X, iris_y)
predicted_labels = svc.predict(iris_X_test)
print("Accuracy score after classification for " + titles[0] + ": " + str(accuracy_score(iris_y_test, predicted_labels)*100) + "%")

# LinearSVC (linear kernel)
lin_svc = svm.LinearSVC(C=C).fit(iris_X, iris_y)
predicted_labels = lin_svc.predict(iris_X_test)
print("Accuracy score after classification for " + titles[1] + ": " + str(accuracy_score(iris_y_test, predicted_labels)*100) + "%")

# SVC with RBF kernel
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(iris_X, iris_y)
predicted_labels = rbf_svc.predict(iris_X_test)
print("Accuracy score after classification for " + titles[2] + ": " + str(accuracy_score(iris_y_test, predicted_labels)*100) + "%")

# SVC with polynomial (degree 3) kernel
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(iris_X, iris_y)
predicted_labels = poly_svc.predict(iris_X_test)
print("Accuracy score after classification for " + titles[3] + ": " + str(accuracy_score(iris_y_test, predicted_labels)*100) + "%")


h = .02  # step size in the mesh

# create a mesh to plot in
x_min, x_max = iris_X[:, 0].min() - 1, iris_X[:, 0].max() + 1
y_min, y_max = iris_X[:, 1].min() - 1, iris_X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
	                     np.arange(y_min, y_max, h))


for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].

    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    
    # Plot also the training points
    plt.scatter(iris_X[:, 0], iris_X[:, 1], c=iris_y, cmap=plt.cm.coolwarm)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()



# References

# 1. SVM (Support Vector Machine)
# https://medium.com/machine-learning-101/chapter-2-svm-support-vector-machine-theory-f0812effc72