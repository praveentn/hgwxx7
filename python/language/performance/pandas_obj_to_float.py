# import libraries
import operator
from itertools import islice
from timeit import timeit
from itertools import chain
import tkinter
import pandas as pd
import matplotlib.pyplot as plt

# function 1 
def fun1(l):
    df = pd.DataFrame(l)
    print(len(df))
    return df[0].astype(float)

# function 2
def fun2(l):
    df = pd.DataFrame(l)
    print(len(df))
    return df[0].transform(float)

# function 2
def fun3(l):
    df = pd.DataFrame(l)
    print(len(df))
    return df[0].transform(lambda x: float(x))

# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2', 'fun3',],
       columns=[1, 10, 25, 50, 100, 500, 1000, 5000, 10000, 50000], #100000],
       dtype=float
)

# each function to be looped over the mul.factors
# timeit is used and output to dataframe
for f in res.index: 
    for c in res.columns:
        l = [1,2,3,4,5,6,7,8,9,10] * c
        stmt = '{}(l)'.format(f)       # f(l)
        setp = 'from __main__ import l, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)


# using matplotlib to plot 
ax = res.div(res.min()).T.plot(loglog=True) 
ax.set_xlabel("N")
ax.set_ylabel("time (relative)")

plt.show()


