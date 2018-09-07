# import libraries
import tkinter
import pandas as pd
from timeit import timeit
import matplotlib.pyplot as plt

k = 775
l = list(range(1111))

# function 1 
def fun1(l):
    for i in l:
        if i==k:
            return True

# function 2
def fun2(l):
    if k in l:
        return True


# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2',],
       columns=[1, 10, 25, 50, 100, 500, 1000, 5000, 10000, 50000, 100000,] # 1000000],
)

# each function to be looped over the mul.factors
# timeit is used and output to dataframe
for f in res.index: 
    for c in res.columns:
        l_ = l * c
        stmt = '{}(l_)'.format(f)       # f(l_)
        setp = 'from __main__ import l_, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)


# using matplotlib to plot 
ax = res.div(res.min()).T.plot(loglog=True) 
ax.set_xlabel("N")
ax.set_ylabel("time (relative)")

plt.show()