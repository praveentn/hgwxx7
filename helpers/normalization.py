# ways to normalize numerical data

'''
Standardizing the features so that they are centered around 0 with 
a standard deviation of 1 is not only important if we are comparing
measurements that have different units, but it is also a general 
requirement for many machine learning algorithms.
'''

# input list (il)
il = [1,1,1,2,3,2,2,2,1,1,1,2,1,12,111]

# find the min, max, sum, average and range
avg = sum(il) / len(il)
rng = max(il) - min(il)

# following code will give a generator
# which will have the normalized output
((x - avg)/rng for x in il)

# output
[-0.07757575757575758, -0.07757575757575758, -0.07757575757575758,
-0.06848484848484848, -0.059393939393939395, -0.06848484848484848,
-0.06848484848484848, -0.06848484848484848, -0.07757575757575758,
-0.07757575757575758, -0.07757575757575758, -0.06848484848484848,
-0.07757575757575758, 0.022424242424242426, 0.9224242424242425]
