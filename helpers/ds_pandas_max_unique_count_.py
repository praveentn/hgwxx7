>>> import pandas as pd

>>> data = {'shoe': ['a', 'b'], 'fury': ['c','d','e','f'], 'chaos': ['g','h', 'i']}
>>> data
{'shoe': ['a', 'b'], 'fury': ['c', 'd', 'e', 'f'], 'chaos': ['g', 'h', 'i']}

>>> df = pd.DataFrame({k:pd.Series(v) for k, v in data.items()})
>>> df
  chaos fury shoe
0     g    c    a
1     h    d    b
2     i    e  NaN
3   NaN    f  NaN

>>> print(df.count().max())
4

>>> df.notnull().sum(0).max()
4
>>>