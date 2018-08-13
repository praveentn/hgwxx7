'''
One Class SVM
'''
import tkinter
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

import pandas as pd
from sklearn import svm

tr_data = pd.read_csv('novelty_4.csv') 
#print(tr_data.head(1))

X = tr_data.drop(['Class','R','S'], axis=1, inplace=True)

nu = [.001, .01, .05, .1, .5,]
gamma = [.001, .01, .05, .1, 1, 10, 100]

#for n in nu:
#    for g in gamma:
clf = svm.OneClassSVM(nu=0.02, kernel="rbf", gamma=.001)
clf.fit(tr_data)

pred = clf.predict(tr_data)
#print(type(pred))

tr_data['pred'] = pred
#print(tr_data.head(1))

# inliers are labeled 1, outliers are labeled -1
normal = tr_data[['P','Q']][pred == 1].values
abnormal = tr_data[['P','Q']][pred == -1].values

#print(normal)
#print(abnormal)

plt.figure('One Class SVM')
plt.plot(normal[:,0],normal[:,1],'bx')
plt.plot(abnormal[:,0],abnormal[:,1],'ro')
plt.xlabel('Latency (ms)')
plt.ylabel('Throughput (mb/s)')
plt.show()

