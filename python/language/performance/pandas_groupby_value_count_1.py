# import libraries
import tkinter
import pandas as pd
from timeit import timeit
import matplotlib.pyplot as plt

df = pd.DataFrame([
 ['A',    4.3],
 ['B',    3.1],
 ['C',    8.9],
 ['D',    2.1],
 ['E',    3.9],
 ['F',    4.5],
 ['B',    3.1],
 ['C',    8.9],
 ['A',    2.1],
 ['A',    3.9],
 ['B',    4.5],
 ['C',    3.27],
 ['D',    8.7],
 ['E',    2.37],
 ['F',    3.7],
 ['B',    4.7],
 ['B',    3.37],
 ['C',    8.7],
 ['A',    2.7],
 ['A',    3.7],
 ['A',    4.3],
 ])

df.columns = ['Parameter',  'Value']

# filter
def fun1(df):
    return df.groupby('Parameter').filter(lambda x : x['Parameter'].shape[0]>=4)

# value_counts + isin
def fun2(df):
    v = df.Parameter.value_counts()
    return df[df.Parameter.isin(v.index[v.gt(4)])]

# groupby + transform 
def fun3(df):
    return df[df.groupby('Parameter')['Parameter'].transform('size') > 4]


# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2', 'fun3'],
       columns=[1, 10, 25, 50, 100, 500, 1000, 5000,] # 10000, 50000, 100000,] # 1000000],
)

# each function to be looped over the mul.factors
# timeit is used and output to dataframe
for f in res.index: 
    for c in res.columns:
        l = pd.concat([df] * c)
        stmt = '{}(l)'.format(f)       # f(l)
        setp = 'from __main__ import l, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)


# using matplotlib to plot 
ax = res.div(res.min()).T.plot(loglog=True) 
ax.set_xlabel("N")
ax.set_ylabel("time (relative)")

plt.show()
