# numpy repeat - use case 1
# creating a new pandas column from a list
# assuming you've a dataframe df

import numpy as np

my_list = ['A','B','C','D']

df['my_list'] = np.repeat(my_list, 5)
# repeats each item in my_list 5 times
