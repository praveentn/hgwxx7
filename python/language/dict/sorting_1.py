xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Recommended one 

import operator

sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
