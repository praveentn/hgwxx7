# ways to normalize numerical (min-max scaling) data
# data is scaled to a fixed range - usually 0 to 1

'''
Standardizing the features so that they are centered around 0 with 
a standard deviation of 1 is not only important if we are comparing
measurements that have different units, but it is also a general 
requirement for many machine learning algorithms.
'''

# input list (il)
il = [1,1,1,2,3,2,2,2,1,1,1,2,1,12,111]

# find the min, max and range
rng = max(il) - min(il)

# following code will give a generator
# which will have the normalized output
((x - min(il))/rng for x in il)

# output
[0.0, 0.0, 0.0, 0.00909090909090909, 0.01818181818181818, 0.00909090909090909, 
 0.00909090909090909, 0.00909090909090909, 0.0, 0.0, 0.0, 0.00909090909090909, 0.0, 0.1, 1.0]
