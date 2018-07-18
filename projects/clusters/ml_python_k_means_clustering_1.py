import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

import tkinter
import pandas as pd
import matplotlib.pyplot as plt

'''
# define number of samples
n_samples = 100

# define random state value to initialize the center
random_state = 20

# define number of feature as 5
X,y = make_blobs(n_samples=n_samples, n_features=5, random_state=None)
# print(X,y)

# The goal of K-means algorithm is to find groups in the data, with the number of groups represented by the variable K. 
# mean distance to the centroid as a function of K is plotted and the "elbow point," where the rate of decrease sharply shifts, can be used to roughly determine K.

# define number of cluster to be formed as 3 and 
# in random state and fit features into the model
predict_y = KMeans(n_clusters=3, random_state=random_state)

print(predict_y)

predict_y_fit = predict_y.fit_predict(X)
# estimator function
# print(predict_y_fit)
print(type(predict_y_fit))
# print(predict_y_fit.labels_)
print(predict_y_fit.shape)

df = pd.DataFrame(predict_y_fit)
# print(df)
print(df.describe())

print(df[0].value_counts())
'''
# rule
'''
df[0].value_counts().plot.bar()
plt.show()

df[0].value_counts().plot.pie()
plt.gca().set_aspect("equal")
plt.show()


labels = []
for i, dfi in enumerate(df.groupby(df[0])):
    labels.append(dfi[0])
    plt.bar(i, dfi[1].count(), label=dfi[0])
plt.xticks(range(len(labels)), labels)
plt.legend()
plt.show()
'''

data = pd.read_csv('data_1024.csv', sep='\t')
print(data.describe())
print(data.head())


# plt.scatter(data['Distance_Feature'], data['Speeding_Feature'])
# plt.show()

X = np.matrix(list(zip(data['Distance_Feature'].values,data['Speeding_Feature'].values)))
kmeans = KMeans(n_clusters=2)
print(kmeans)

kmeans_fit = kmeans.fit(X)
print(kmeans_fit)

kmeans_predict = kmeans_fit.predict(X)
print(kmeans_predict)
print(kmeans_predict.shape)

dfx = pd.DataFrame(X)

plt.scatter(dfx[0], dfx[1], c=kmeans_predict, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
print(centers)
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

plt.show()


kmeans = KMeans(n_clusters=4)
kmeans_fit = kmeans.fit(X)
kmeans_predict = kmeans_fit.predict(X)
plt.scatter(dfx[0], dfx[1], c=kmeans_predict, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()




