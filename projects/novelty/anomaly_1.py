import tkinter
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

## HELPER FUNCTIONS ##

def plot_decision_function(model, ax, sv=True):
    ## Create a grid to evaluate the model
    xx, yy = np.meshgrid(np.linspace(-4, 4, 100),
                         np.linspace(-4, 4, 100))
    ## Evaluate the model
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    ## Plot the margin
    ax = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
    ax = plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
    
    ax = plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 6), cmap=plt.cm.PuBu)
    
    if sv:
        ax = plt.scatter(model.support_vectors_[:, 0],
                       model.support_vectors_[:, 1],
                       s=300, linewidth=1, facecolors='none', edgecolors='black')


def plot_new_observations(X_train, X_new, anomaly, ax):
    _ = plt.scatter(X_train[:,0], X_train[:,1],
                    axes=ax, color='w', s=40, edgecolors='k',
                    label='Training data')

    _ = plt.scatter(X_new[:,0], X_new[:,1], axes=ax,
                    color='violet', s=40, edgecolors='k',
                    label='New regular observations')

    _ = plt.scatter(anomaly[:,0], anomaly[:,1], axes=ax,
                    color='gold', s=40, edgecolors='k',
                    label='New abnormal observations')

    _ = ax.legend()
    _ = ax.set_xlim([-4, 4])
    _ = ax.set_ylim([-4, 4])


n_points = 200

## generate a cluster of points for the training 
np.random.seed(42)
X_train = 0.5 * np.random.randn(n_points, 2)

## Plot
fig, ax = plt.subplots(figsize=(12,8))
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax, color='w', s=40, edgecolors='k')
_ = ax.set_xlim([-4, 4])
_ = ax.set_ylim([-4, 4])


model = svm.OneClassSVM(nu=0.05, kernel="rbf", gamma=0.7)
model.fit(X_train)

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=True)

## Add the training points
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax,
                color='w', s=40, edgecolors='k',label='Training data')
_ = ax.legend()


## Compute the empirical error 
y_train = model.predict(X_train)
err_emp_1 = y_train[y_train == -1].size
print("Training error = {}/{}".format(err_emp_1, n_points))


## Reduce nu, i.e. weight more the slack variables
model = svm.OneClassSVM(nu=0.005, kernel="rbf", gamma=0.7)
model.fit(X_train)

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=True)

## Add the training points
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax,
                color='w', s=40, edgecolors='k',label='Training data')
_ = ax.legend()

## Compute the empirical error 
y_train = model.predict(X_train)
err_emp_2 = y_train[y_train == -1].size
print("Training error = {}/{}".format(err_emp_2, n_points))
# Training error = 5/200

"""
As we can see from the picture above, by reducing $\nu$ we are increasing the weight of the slack variables (because $C \sim 1/\nu$). This leads to a reduction of the error but increase the risk of overfitting.
"""

new_observation = 25
new_anomaly = 10

## Generate new observation from the same distribution
np.random.seed(42)
X_new = 0.5 * np.random.randn(new_observation, 2)

## Generate outliers
anomaly = np.random.uniform(low=-3, high=3, size=(new_anomaly, 2))

## Plot
fig, ax = plt.subplots(figsize=(12,8))
plot_new_observations(X_train, X_new, anomaly, ax)

y_new = model.predict(X_new)
y_anomaly = model.predict(anomaly)

err_new = y_new[y_new == -1].size
err_anomaly = y_anomaly[y_anomaly == -1].size

print("Fraction of new regular observations misclassified = {}/{}".format(err_new, new_observation))
print("Fraction of new abnormal observations correctly classified = {}/{}".format(err_anomaly, new_anomaly))

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=False)
plot_new_observations(X_train, X_new, anomaly, ax)
# Fraction of new regular observations misclassified = 0/25
# Fraction of new abnormal observations correctly classified = 10/10

# Let's try to make the problem a little bit more complex, i.e. use two clusters as positive examples

## generate two cluster for the training 
np.random.seed(42)
X_train1 = 0.5 * np.random.randn(n_points//2, 2)+1.5
X_train2 = 0.5 * np.random.randn(n_points//2, 2)-1.5

X_train = np.r_[X_train1, X_train2]

## Plot
fig, ax = plt.subplots(figsize=(12,8))
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax, color='w', s=40, edgecolors='k')
_ = ax.set_xlim([-4, 4])
_ = ax.set_ylim([-4, 4])

model = svm.OneClassSVM(nu=0.06, kernel="rbf", gamma=0.5)
model.fit(X_train)

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=True)

## Add the training points
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax,
                color='w', s=40, edgecolors='k',label='Training data')
_ = ax.legend()

## Compute the empirical error 
y_train = model.predict(X_train)
err_emp_1 = y_train[y_train == -1].size
print("Training error = {}/{}".format(err_emp_1, n_points))

new_observation = 50
new_anomaly = 20

## Generate new observation from the same distribution
np.random.seed(42)
X_new_1 = 0.5 * np.random.randn(new_observation//2, 2)+1.5
X_new_2 = 0.5 * np.random.randn(new_observation//2, 2)-1.5
X_new = np.r_[X_new_1, X_new_2]

## Generate outliers
anomaly = np.random.uniform(low=-4, high=4, size=(new_anomaly, 2))

## Plot
fig, ax = plt.subplots(figsize=(12,8))
plot_new_observations(X_train, X_new, anomaly, ax)


y_new = model.predict(X_new)
y_anomaly = model.predict(anomaly)

err_new = y_new[y_new == -1].size
err_anomaly = y_anomaly[y_anomaly == -1].size

print("Fraction of new regular observations misclassified = {}/{}".format(err_new, new_observation))
print("Fraction of new abnormal observations correctly classified = {}/{}".format(err_anomaly, new_anomaly))

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=False)
plot_new_observations(X_train, X_new, anomaly, ax)
# Fraction of new regular observations misclassified = 2/50
# Fraction of new abnormal observations correctly classified = 18/20

# We can try to move the cluster closer

np.random.seed(42)
X_train1 = 0.5 * np.random.randn(n_points//2, 2)+0.9
X_train2 = 0.5 * np.random.randn(n_points//2, 2)-0.9

X_train = np.r_[X_train1, X_train2]

## Plot
fig, ax = plt.subplots(figsize=(12,8))
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax, color='w', s=40, edgecolors='k')
_ = ax.set_xlim([-4, 4])
_ = ax.set_ylim([-4, 4])


model = svm.OneClassSVM(nu=0.05, kernel="rbf", gamma=0.1)
model.fit(X_train)

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=True)

## Add the training points
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax,
                color='w', s=40, edgecolors='k',label='Training data')
_ = ax.legend()

## Compute the empirical error 
y_train = model.predict(X_train)
err_emp_1 = y_train[y_train == -1].size
print("Training error = {}/{}".format(err_emp_1, n_points))

# If we want to try to separate the two cluster we need to increase the value of gamma and $\nu$ but this increase the errors a lot.

model = svm.OneClassSVM(nu=0.3, kernel="rbf", gamma=1)
model.fit(X_train)

fig, ax = plt.subplots(figsize=(12,8))

## Plot the decision function
plot_decision_function(model, ax, sv=True)

## Add the training points
_ = plt.scatter(X_train[:,0], X_train[:,1], axes=ax,
                color='w', s=40, edgecolors='k',label='Training data')
_ = ax.legend()

## Compute the empirical error 
y_train = model.predict(X_train)
err_emp_1 = y_train[y_train == -1].size
print("Training error = {}/{}".format(err_emp_1, n_points))

