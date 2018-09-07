# import libraries
import tkinter
import itertools
import collections
import numpy as np
import pandas as pd
from timeit import timeit
from itertools import chain
import matplotlib.pyplot as plt

documents = [['Human', 'machine', 'interface'],['A', 'survey', 'of', 'user'],['The', 'EPS', 'user'],
             ['System', 'and', 'human'],['Relation', 'of', 'user'],['The', 'generation'],
             ['The', 'intersection'],['Graph', 'minors'],['Graph', 'minors', 'a']]

df = pd.DataFrame({'date': np.array(['2014-05-01', '2014-05-02', '2014-05-10', '2014-05-10', '2014-05-15', '2014-05-15', '2014-05-20', '2014-05-20', '2014-05-20'], dtype=np.datetime64), 'text': documents})

'''
Desired Output: (based on unique dates + concatenate string)
        date                                               text
0 2014-05-01                        [Human, machine, interface]
1 2014-05-02                              [A, survey, of, user]
2 2014-05-10               [The, EPS, user, System, and, human]
3 2014-05-15              [Relation, of, user, The, generation]
4 2014-05-20  [The, intersection, Graph, minors, Graph, 'minors', 'a']
'''

# function 1 
def fun1(df):
    return df.groupby('date').text.sum()

# function 2
def fun2(df):
    return df.groupby('date').text.agg('sum')

# function 1 
def fun3(df):
    return df.groupby('date').text.agg(lambda x: [item for z in x for item in z])

# function 2
def fun4(df):
    return df.groupby('date').text.agg(lambda x: list(itertools.chain.from_iterable(x)))


# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2','fun3', 'fun4',],
       columns=[1, 10, 25, 50, 100, 500, 1000, 5000, 10000,] # 50000, 100000, 1000000],
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



