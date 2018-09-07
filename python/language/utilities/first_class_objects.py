# functions are first class in Python

>>> def my_fun(a,b):
...     '''return bth power of a'''
...     return a**b
...
>>>

>>> my_fun
<function my_fun at 0x007DC660>

>>> funs = [my_fun,my_fun]

>>> funs[0]
<function my_fun at 0x007DC660>

>>> funs[1]
<function my_fun at 0x007DC660>

>>> funs_v = [x(3,4) for x in funs]

>>> funs_v
[81, 81]

>>>

