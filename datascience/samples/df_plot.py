import tkinter 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame([
['abcd',         'sw-off ',        '07:53:15 +05:00'],\
['abcd',         'sw-off ',        '07:53:15 +05:00'],\
['abcde',         'sw-off ',        '07:53:15 +05:00'],\
['abcd',         'sw-on',          '07:53:15 +05:00'],\
['abcdf',         'sw-off ',        '07:53:15 +05:00'],\
['abcd',         'sw-on',          '07:53:15 +05:00'],\
['abcd',         'sw-on',          '00:53:15 +05:00'],\
['abcd',         'sw-on',          '01:53:15 +05:00'],\
['abcd',         'sw-off',          '02:53:15 +05:00'],\
['abcde',         'sw-off',          '02:53:15 +05:00'],\
['abcde',         'sw-off',          '02:53:15 +05:00'],\
['abcde',         'sw-off',          '02:53:15 +05:00'],\
['abcd',         'sw-off ',        '07:53:15 +05:00'],\
['abcd',         'sw-on',          '03:53:15 +05:00'],\
['abcd',         'sw-on',          '05:53:15 +05:00'],\
['abcd',         'sw-off',          '04:53:15 +05:00'],\
['abcd',         'sw-on',          '08:53:15 +05:00'],\
['abcd',         'sw-off',          '06:53:15 +05:00'],\
['abcde',         'sw-off',          '09:53:15 +05:00'],\
])

df.columns = ['username',    'switch_state',    'time',]

print(df)

df = df.loc[df['switch_state']=='sw-off']
df['count'] = df.groupby(['username','time'])['username'].transform('count')

plt.scatter(df['time'], df['username'])
plt.show()
