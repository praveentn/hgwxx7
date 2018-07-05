import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
import seaborn as sns

data = load_iris()
df = pd.DataFrame(data['data'])
df.head(5)
fig, axes = plt.subplots(figsize=(13, 3))
axes = sns.countplot(x=2, data=df, orient='h')
plt.show()