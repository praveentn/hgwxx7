# using yield /generator

>>> def generator_function(x):
...     for i in range(x):
...         yield i
...
>>>

>>> for item in generator_function(7):
...     print(item)
...
0
1
2
3
4
5
6
>>>
