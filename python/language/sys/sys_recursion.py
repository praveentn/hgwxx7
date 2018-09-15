>>> sys.getrecursionlimit()
1000

>>> sys.setrecursionlimit(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: recursion limit must be greater or equal than 1

>>> sys.setrecursionlimit(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RecursionError: cannot set the recursion limit to 1 at the recursion depth 1: the limit is too low

>>> sys.setrecursionlimit(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RecursionError: cannot set the recursion limit to 2 at the recursion depth 1: the limit is too low

>>> sys.setrecursionlimit(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RecursionError: cannot set the recursion limit to 3 at the recursion depth 1: the limit is too low

>>> sys.setrecursionlimit(4)

>>> sys.getrecursionlimit()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RecursionError: maximum recursion depth exceeded while calling a Python object
4

>>>