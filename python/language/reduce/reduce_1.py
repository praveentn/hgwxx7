# load library
from functools import reduce

# normal way
product = 1
list = [1, 2, 3, 4]

for num in list:
    product = product * num


# using reduce!
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
product
24
