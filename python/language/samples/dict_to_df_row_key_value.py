'''
dict / list to rows
'''

d={
  'information': ['row1', 'row2', 'row3', 'row4'],
  'record': [
      'val1', {'val2': {'a': 300, 'b': [ {"b1": 10.5}, {"b2": 2} ]  }, 'val3': { 'a': 10, 'b': 15 } },
      'val4', 
		[{	'val5': [ {	'a': { 'c': [ {	'd': { 'e': [ {	'f': 1 },{'g': 3 }]	}} ]}}]},
		{'b': 'bar'}
		]
	]
}

import itertools
import collections
import pandas as pd

ch = lambda ite: list(itertools.chain.from_iterable(ite))

def isseq(obj):
    if isinstance(obj, str): return False
    return isinstance(obj, collections.abc.Sequence)

def unnest(k, v):
    if isseq(v): return ch([unnest(k, v_) for v_ in v])
    if isinstance(v, dict): return ch([unnest("_".join([k, k_]), v_) for k_, v_ in v.items()])
    return k,v

def pairwise(i):
    _a = iter(i)
    return list(zip(_a, _a))

a = ch([(unnest(k, v)) for k, v in zip(d['information'], d['record'])])
print(pd.DataFrame(pairwise(a)))

'''
                     0     1
0                 row1  val1
1          row2_val2_a   300
2       row2_val2_b_b1  10.5
3       row2_val2_b_b2     2
4          row2_val3_a    10
5          row2_val3_b    15
6                 row3  val4
7  row4_val5_a_c_d_e_f     1
8  row4_val5_a_c_d_e_g     3
9               row4_b   bar
'''
