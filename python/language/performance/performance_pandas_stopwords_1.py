# import libraries
import re
import tkinter
import pandas as pd
from timeit import timeit
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "ID": [1, 2, 3, 4, 5],
        "name": [
            "Hello Kitty",
            "Hello Puppy",
            "It is an Helloexample",
            "for stackoverflow",
            "Hello World",
        ],
    }
)

stopwords = ["Hello", "for", "an", "It"]

# function 1 
def fun1(df):
    return df['name'].str.replace('|'.join(stopwords), '')

# function 2
def fun2(df):
    p = re.compile('|'.join(map(re.escape, stopwords)))
    return [p.sub('', text) for text in df['name']]

# function 3
def fun3(df):
    return df['name'].replace(stopwords, value='', regex=True)


# create a pandas dataframe 
# index has the list of functions
# columns has the multiplication factor - 
# to increase input list size (thereby complexity)
res = pd.DataFrame(
       index=['fun1', 'fun2', 'fun3',],
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