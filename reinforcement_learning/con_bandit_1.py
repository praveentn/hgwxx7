Python 3.6.9 |Anaconda, Inc.| (default, Jul 30 2019, 14:00:49) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>> import vowpalwabbit
>>>
>>> import pandas as pd
>>> import sklearn as sk
>>> import numpy as np
>>>
>>> # generate sample data that could originate from previous random trial, e.g. AB test, for the CB to explore
... ## data here are equivalent to example in https://github.com/JohnLangford/vowpal_wabbit/wiki/Contextual-Bandit-Example
... train_data = [{'action': 1, 'cost': 2, 'probability': 0.4, 'feature1': 'a', 'feature2': 'c', 'feature3': ''},
...               {'action': 3, 'cost': 0, 'probability': 0.2, 'feature1': 'b', 'feature2': 'd', 'feature3': ''},
...               {'action': 4, 'cost': 1, 'probability': 0.5, 'feature1': 'a', 'feature2': 'b', 'feature3': ''},
...               {'action': 2, 'cost': 1, 'probability': 0.3, 'feature1': 'a', 'feature2': 'b', 'feature3': 'c'},
...               {'action': 3, 'cost': 1, 'probability': 0.7, 'feature1': 'a', 'feature2': 'd', 'feature3': ''}]
>>>
>>>
>>> train_df = pd.DataFrame(train_data)
>>>
>>> ## add index to df
... train_df['index'] = range(1, len(train_df) + 1)
>>> train_df = train_df.set_index("index")
>>>
>>> # generate some test data that you want the CB to make decisions for, e.g. features describing new users, for the CB to exploit
... test_data = [{'feature1': 'b', 'feature2': 'c', 'feature3': ''},
...             {'feature1': 'a', 'feature2': '', 'feature3': 'b'},
...             {'feature1': 'b', 'feature2': 'b', 'feature3': ''},
...             {'feature1': 'a', 'feature2': '', 'feature3': 'b'}]
>>>
>>>
>>> test_df = pd.DataFrame(test_data)
>>>
>>> ## add index to df
... test_df['index'] = range(1, len(test_df) + 1)
>>> test_df = test_df.set_index("index")
>>>
>>>
>>> # take a look at dataframes
... print(train_df)
       action  cost  probability feature1 feature2 feature3
index
1           1     2          0.4        a        c
2           3     0          0.2        b        d
3           4     1          0.5        a        b
4           2     1          0.3        a        b        c
5           3     1          0.7        a        d
>>> print(test_df)
      feature1 feature2 feature3
index
1            b        c
2            a                 b
3            b        b
4            a                 b
>>>
>>> # import vowpal wabbit's python wrapper
... import vowpalwabbit
>>> from vowpalwabbit import pyvw
>>>
>>> # create python model - this stores the model parameters in the python vw object; here a contextual bandit with four possible actions
... vw = pyvw.vw("--cb 4")
Num weight bits = 18
learning rate = 0.5
initial_t = 0
power_t = 0.5
using no cache
Reading datafile =
num sources = 1
>>>
>>> vw
<vowpalwabbit.pyvw.vw object at 0x0000021411AC0458>
>>>
>>> # use the learn method to train the vw model, train model row by row using a loop
... i==1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'i' is not defined
>>> for i in train_df.index:
...     ## provide data to cb in requested format
...     action = train_df.loc[i, "action"]
...     cost = train_df.loc[i, "cost"]
...     probability = train_df.loc[i, "probability"]
...     feature1 = train_df.loc[i, "feature1"]
...     feature2 = train_df.loc[i, "feature2"]
...     feature3 = train_df.loc[i, "feature3"]
...     ## do the actual learning
...     vw.learn(str(action)+":"+str(cost)+":"+str(probability)+" | "+str(feature1)+" "+str(feature2)+" "+str(feature3))
...
5.000000 5.000000            1            1.0    known        1        3
2.500000 0.000000            2            2.0    known        2        3
2.083333 1.666667            4            4.0    known        2        4
>>>
>>> # predict row by row and output results
... j==1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'j' is not defined
>>> for j in test_df.index:
...     feature1 = test_df.loc[j, "feature1"]
...     feature2 = test_df.loc[j, "feature2"]
...     feature3 = test_df.loc[j, "feature3"]
...     choice = vw.predict("| "+str(feature1)+" "+str(feature2)+" "+str(feature3))
...     print(j, choice)
...
1 3
2 3
1.952381 1.428571            8            8.0  unknown        3        3
3 3
4 3
>>>
>>>
>>> # the CB assigns every instance to action 3 as it should per the cost structure of the train data; you can play with the cost structure to see that the CB updates its predictions accordingly
...
>>>
>>> # BONUS: save and load the CB model
... # save model
... vw.save('cb.model')
>>> del vw
>>> # load from saved file
... vw = pyvw.vw("--cb 4 -i cb.model")
Num weight bits = 18
learning rate = 0.5
initial_t = 0
power_t = 0.5
using no cache
Reading datafile =
num sources = 1
>>> print(vw.predict('| a b'))
    n.a.     n.a.            1            1.0  unknown        3        3
3
>>>
>>>
>>>
>>> import os
>>>
>>> os.getcwd()

finished run
number of examples = 9
weighted example sum = 9.000000
weighted label sum = 0.000000
average loss = 1.952381
total feature number = 28
'C:\\Continuum\\anaconda3\\envs'
>>>
>>>
>>> exit()

finished run
number of examples = 1
weighted example sum = 1.000000
weighted label sum = 0.000000
average loss = n.a.
total feature number = 3

