'''
Desired output:
   ID               name
0   1              Kitty
1   2              Puppy
2   3              is example
3   4              stackoverflow
4   5              World
'''

import pandas as pd

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

'''
Input:
   ID               name
0   1        Hello Kitty
1   2        Hello Puppy
2   3   It is an Helloexample
3   4  for stackoverflow
4   5        Hello World
'''

stopwords = ["Hello", "for", "an", "It"]

# Straight-forward way >>>
df = df['name'].replace(stopwords, value='', regex=True)

# Alternately, using 're'
import re
p = re.compile('|'.join(map(re.escape, stopwords)))
df['name'] = [p.sub('', text) for text in df['name']]

print(df)

# List comprehensions are implemented in C and operate in C speed. 
# I highly recommend list comprehensions when working with string 
# and regex data over pandas str functions for the time-being because the API is a bit slow.

# The use of map(re.escape, stopwords) is to escape any possible 
# regex metacharacters which are meant to be treated literally during replacement.

# The pattern is precompiled before calling regex.sub to reduce the overhead of compilation at each iteration.

# Timings

df = pd.concat([df] * 10000)
%timeit df['name'].str.replace('|'.join(To_remove_lst), '')
%timeit [p.sub('', text) for text in df['name']] 

# 100 ms ± 5.88 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
# 60 ms ± 3.27 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
