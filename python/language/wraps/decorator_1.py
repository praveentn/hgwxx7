# using decorators in python

# load wraps from functools
from functools import wraps

# decorator function
def decor(fun):
    @wraps(fun)
    def with_logging(*args, **kwargs):
        print(fun.__name__ + " is being called!")
        return fun(*args, **kwargs)
    return with_logging


# calling a decorator
@decor
def adder(x):
    """return sum()"""
    return x + x


# call adder()
adder(8)
adder is being called!
16
