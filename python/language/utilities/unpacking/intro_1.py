# arguments unpacking simplified!!
# *

a, b = range(2)
a
0

b
1

a, b, *rest = range(5)
a
0

b
1

rest
[2,3,4]

# first and last lines
with open('file.name') as f:
    first, *_, last = f.readlines()
    

# Refactor functions
def f(a, b, *args):
    print(a, b, *args)

# instead -> *args => a, b, *args
def f(*args):
    a, b, *args = args
    print(a, b, *args)
 
