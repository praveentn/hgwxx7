# Seaborn Regression Plot

import tkinter
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

s = np.matrix([[1,1],[2,3],[2,4],[3,6],[3,9],[4,12],[4,15],[5,19],\
[5,25],[5,36],[6,41],[6,49],[7,54]])
s
matrix([[ 1,  1],
        [ 2,  3],
        [ 2,  4],
        [ 3,  6],
        [ 3,  9],
        [ 4, 12],
        [ 4, 15],
        [ 5, 19],
        [ 5, 25],
        [ 5, 36],
        [ 6, 41],
        [ 6, 49],
        [ 7, 54]])

df = pd.DataFrame(s)
sns.regplot(df[0], df[1])
#<matplotlib.axes._subplots.AxesSubplot object at 0x0D87E1D0>
plt.show()

sns.regplot(df[0], df[1], order=2)
#<matplotlib.axes._subplots.AxesSubplot object at 0x0EB5E270>
plt.show()
