
'''
    Deque -  doubly-linked list of fixed length blocks
    
    Deques have O(1) speed for appendleft() and popleft() while lists have O(n) performance for insert(0, value) and pop(0).

    List append performance is hit and miss because it uses realloc() under the hood. As a result, 
    it tends to have over-optimistic timings in simple code (because the realloc doesn't have to move data) 
    and really slow timings in real code (because fragmentation forces realloc to move all the data). 
    
    In contrast, deque append performance is consistent because it never reallocs and never moves data.

'''

# load libraries
import timeit
from collections import deque

# append - append and pop 
def appends():
    s_append, s_pop = s.append, s.pop

# deque - append and pop 
def deques():
    d_append, d_pop = d.append, d.pop

# main
if __name__ == '__main__':
    ''' main  '''
    s = list(range(1000))
    d = deque(s)

    print(timeit.timeit('appends()', setup="from __main__ import appends"))
    print(timeit.timeit('deques()', setup="from __main__ import deques"))

# 0.2518334704937214
# 0.19763738898872668

# Append takes more time than deque as we can see from the output
