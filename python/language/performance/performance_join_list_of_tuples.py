# import libraries
import tkinter
import pandas as pd
from timeit import timeit
import matplotlib.pyplot as plt

# function 1 
def fun1(l):
    return ' '.join([''.join(w) for w in l])

# function 2
def fun2(l):
    return ' '.join([x+y for x, y in l])

list_of_tuples = [('eː', 'n'), ('a', 'k'), ('a', 's')]

# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2',],
       columns=[1, 10, 25, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000],
)

# each function to be looped over the mul.factors
# timeit is used and output to dataframe
for f in res.index: 
    for c in res.columns:
        l = list_of_tuples * c
        stmt = '{}(l)'.format(f)       # f(l)
        setp = 'from __main__ import l, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)


# using matplotlib to plot 
ax = res.div(res.min()).T.plot(loglog=True) 
ax.set_xlabel("N")
ax.set_ylabel("time (relative)")

plt.show()