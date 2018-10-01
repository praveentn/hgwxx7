# loaf libraries

import pandas as pd

# read csv file
df = pd.read_csv('input.csv')

print(df.sample(5))
'''
     time        date
4  198898  2017-12-06
3  198897  2017-12-06
2  198896  2017-12-05
1  198895  2017-12-05
5  198899  2017-12-07
'''

# using pandas datetime
print(pd.to_datetime(df['date']).dt.year.value_counts())
# 2017    6
# Name: date, dtype: int64
