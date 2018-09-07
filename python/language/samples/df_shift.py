import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 2)), columns=['a', 'b'])
print(df2)

df2['c'] = df2['a'].reindex(df2.index - df2['b']).values
print(df2)
