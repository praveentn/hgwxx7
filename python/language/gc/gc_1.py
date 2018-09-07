# explicitly free memory
# garbage collection

import gc

gc.collect()

>>> gc.collect()
347 # integer denoting the freed memory in bytes

# The del statement might be of use, 
# but it isn't guaranteed to free the memory.
