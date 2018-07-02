import numpy as np
import pandas as pd
import tkinter as tk
import seaborn as sns
import matplotlib.pyplot as plt

Ncols = 9
cols = ['col_{:d}'.format(i) for i in range(Ncols)]
df = pd.DataFrame(np.random.random(size=(1000,Ncols)),columns=cols)

fig, axs = plt.subplots(3,3) # adjust the geometry based on your number of columns to plot
for ax,col in zip(axs.flatten(), cols):
    sns.kdeplot(df[col], ax=ax)

plt.show()
