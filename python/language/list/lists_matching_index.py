# find matching indices of elements in two lists

def find_matching_index(list1, list2):
    ''' input -> lists
        output -> set of indices
    '''
    
    inverse_index = { element: index for index, element in enumerate(list1) }

    return [ (index, inverse_index[element]) for index, element in enumerate(list2) 
                                                    if element in inverse_index ]

find_matching_index([1,2,3], [3,2,1]) 
# [(0, 2), (1, 1), (2, 0)]

find_matching_index([1,2,4], [3,2,1])
# [(1, 1), (2, 0)]
