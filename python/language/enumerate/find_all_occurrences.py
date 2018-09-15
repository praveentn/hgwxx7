# enumerate use case - find all occurrences of an element in a list

# my_list
my_list = [1,2,1,2,1,2,3,4,5,4,3,2,2,3,4,5,6,2,2,2,1,1,1,1,0,0]

# elem whose indices needs to be found
req_elem = 2

# indices will have the indices/positions of the required element, here 2
indices = [i for i, x in enumerate(my_list) if x == req_elem]
indices
# [1, 3, 5, 11, 12, 17, 18, 19]

'''
how enumerate works?
    i has the index 
    x has the element
'''
