# using reduce 

# load library
import functools

# define a list
my_list = [10,15,20,25,35]

# using reduce to perform an operation
sum_numbers = functools.reduce(lambda x,y: x+y, my_list)

print(sum_numbers)
# 105

# check the output - use sum
print(sum(my_list))
# 105
