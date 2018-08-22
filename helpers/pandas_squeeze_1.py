# vstack all the arrays of a column into a larger array

import numpy as np
import pandas as pd

s = pd.Series([np.array([[1,0,0,0,1]]), 
               np.array([[0,1,0,1,0]]), 
               np.array([[0,1,0,1,0]])])

res = np.array(s.values.tolist()).squeeze()

# res
# array([[1, 0, 0, 0, 1],
#        [0, 1, 0, 1, 0],
#        [0, 1, 0, 1, 0]])
