# EPL Data 2017-18
# Classifying clubs

# load libraries
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline

# reading data
df = pd.read_json('ml_python_epl_data_17_18.json')

df = df.T
df.reset_index(level=0, inplace = True)

df.columns
df.describe()
df.dtypes

df.head()

# sorting by goals scored
df.sort_values(by=['Goals'],ascending=False)

# na values
df = df.fillna(0)


# to be continued
